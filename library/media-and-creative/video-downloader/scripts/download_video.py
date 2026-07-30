#!/usr/bin/env python3
"""
YouTube Video Downloader
Downloads videos from YouTube with customizable quality and format options.
"""

import argparse
import json
import shutil
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

SKILL_ROOT = Path(__file__).resolve().parent.parent
VENV_DIR = SKILL_ROOT / ".venv"

_YT_DLP_CMD: list[str] | None = None

INSTALL_HELP = """yt-dlp is not available. Install it globally, for example:
  pipx install yt-dlp
  brew install yt-dlp
Or create a venv in this skill folder and install:
  python3 -m venv .venv && .venv/bin/pip install yt-dlp
(Windows: .venv\\Scripts\\pip install yt-dlp)
"""


def _venv_python() -> Path:
    if sys.platform == "win32":
        return VENV_DIR / "Scripts" / "python.exe"
    return VENV_DIR / "bin" / "python"


def _venv_yt_dlp() -> Path:
    if sys.platform == "win32":
        return VENV_DIR / "Scripts" / "yt-dlp.exe"
    return VENV_DIR / "bin" / "yt-dlp"


def _yt_dlp_version_ok(cmd: list[str]) -> bool:
    try:
        subprocess.run(
            [*cmd, "--version"],
            capture_output=True,
            text=True,
            check=True,
        )
        return True
    except (OSError, subprocess.CalledProcessError):
        return False


def _ensure_skill_venv_yt_dlp() -> list[str]:
    """Create skill-local venv and pip install yt-dlp (no system site-packages)."""
    VENV_DIR.parent.mkdir(parents=True, exist_ok=True)
    if not VENV_DIR.is_dir():
        try:
            subprocess.run(
                [sys.executable, "-m", "venv", str(VENV_DIR)],
                check=True,
                capture_output=True,
                text=True,
            )
        except subprocess.CalledProcessError as e:
            raise RuntimeError(
                f"Could not create venv at {VENV_DIR}.\n{INSTALL_HELP}\n{e.stderr or e}"
            ) from e
    pip_py = _venv_python()
    try:
        subprocess.run(
            [str(pip_py), "-m", "pip", "install", "--upgrade", "yt-dlp"],
            check=True,
            capture_output=True,
            text=True,
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"Could not install yt-dlp into {VENV_DIR}.\n{INSTALL_HELP}\n{e.stderr or e}"
        ) from e
    bin_path = _venv_yt_dlp()
    if not bin_path.is_file():
        raise RuntimeError(
            f"yt-dlp not found after install at {bin_path}.\n{INSTALL_HELP}"
        )
    return [str(bin_path)]


def resolve_yt_dlp() -> list[str]:
    """Return argv prefix for yt-dlp: system PATH first, else skill .venv."""
    global _YT_DLP_CMD
    if _YT_DLP_CMD is not None:
        return _YT_DLP_CMD

    system = shutil.which("yt-dlp")
    if system and _yt_dlp_version_ok([system]):
        _YT_DLP_CMD = [system]
        return _YT_DLP_CMD

    venv_bin = _venv_yt_dlp()
    if venv_bin.is_file() and _yt_dlp_version_ok([str(venv_bin)]):
        _YT_DLP_CMD = [str(venv_bin)]
        return _YT_DLP_CMD

    _YT_DLP_CMD = _ensure_skill_venv_yt_dlp()
    return _YT_DLP_CMD


def validate_youtube_https_url(url: str) -> str:
    """
    Only https URLs on YouTube hosts (including youtu.be and youtube-nocookie).
    Raises ValueError with a clear message if invalid.
    """
    raw = url.strip()
    parsed = urlparse(raw)
    if parsed.scheme.lower() != "https":
        raise ValueError("Only https:// YouTube URLs are allowed.")
    host = (parsed.hostname or "").lower()
    if not host:
        raise ValueError("Invalid URL: missing hostname.")
    allowed = (
        host == "youtu.be"
        or host == "youtube.com"
        or host.endswith(".youtube.com")
        or host == "youtube-nocookie.com"
        or host.endswith(".youtube-nocookie.com")
    )
    if not allowed:
        raise ValueError(
            "URL host is not allowed. Use youtube.com, youtu.be, or youtube-nocookie.com links."
        )
    return raw


def get_video_info(yt_dlp: list[str], url: str):
    """Get information about the video without downloading."""
    result = subprocess.run(
        [*yt_dlp, "--dump-json", "--no-playlist", url],
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(result.stdout)


def download_video(url, output_path="/mnt/user-data/outputs", quality="best", format_type="mp4", audio_only=False):
    """
    Download a YouTube video.

    Args:
        url: YouTube video URL
        output_path: Directory to save the video
        quality: Quality setting (best, 1080p, 720p, 480p, 360p, worst)
        format_type: Output format (mp4, webm, mkv, etc.)
        audio_only: Download only audio (mp3)
    """
    try:
        url = validate_youtube_https_url(url)
    except ValueError as e:
        print(f"\n❌ {e}")
        return False

    try:
        yt_dlp = resolve_yt_dlp()
    except RuntimeError as e:
        print(f"\n❌ {e}")
        return False

    # Build command
    cmd = [*yt_dlp]

    if audio_only:
        cmd.extend(
            [
                "-x",  # Extract audio
                "--audio-format",
                "mp3",
                "--audio-quality",
                "0",  # Best quality
            ]
        )
    else:
        # Video quality settings
        if quality == "best":
            format_string = "bestvideo+bestaudio/best"
        elif quality == "worst":
            format_string = "worstvideo+worstaudio/worst"
        else:
            # Specific resolution (e.g., 1080p, 720p)
            height = quality.replace("p", "")
            format_string = f"bestvideo[height<={height}]+bestaudio/best[height<={height}]"

        cmd.extend(
            [
                "-f",
                format_string,
                "--merge-output-format",
                format_type,
            ]
        )

    # Output template
    cmd.extend(
        [
            "-o",
            f"{output_path}/%(title)s.%(ext)s",
            "--no-playlist",  # Don't download playlists by default
        ]
    )

    cmd.append(url)

    print(f"Downloading from: {url}")
    print(f"Quality: {quality}")
    print(f"Format: {'mp3 (audio only)' if audio_only else format_type}")
    print(f"Output: {output_path}\n")

    try:
        # Get video info first
        info = get_video_info(yt_dlp, url)
        print(f"Title: {info.get('title', 'Unknown')}")
        print(f"Duration: {info.get('duration', 0) // 60}:{info.get('duration', 0) % 60:02d}")
        print(f"Uploader: {info.get('uploader', 'Unknown')}\n")

        # Download the video
        subprocess.run(cmd, check=True)
        print(f"\n✅ Download complete!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error downloading video: {e}")
        return False
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Download YouTube videos with customizable quality and format"
    )
    parser.add_argument("url", help="YouTube video URL (https only)")
    parser.add_argument(
        "-o",
        "--output",
        default="/mnt/user-data/outputs",
        help="Output directory (default: /mnt/user-data/outputs)",
    )
    parser.add_argument(
        "-q",
        "--quality",
        default="best",
        choices=["best", "1080p", "720p", "480p", "360p", "worst"],
        help="Video quality (default: best)",
    )
    parser.add_argument(
        "-f",
        "--format",
        default="mp4",
        choices=["mp4", "webm", "mkv"],
        help="Video format (default: mp4)",
    )
    parser.add_argument(
        "-a",
        "--audio-only",
        action="store_true",
        help="Download only audio as MP3",
    )

    args = parser.parse_args()

    success = download_video(
        url=args.url,
        output_path=args.output,
        quality=args.quality,
        format_type=args.format,
        audio_only=args.audio_only,
    )

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
