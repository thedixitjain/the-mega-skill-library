---
name: ruview-flash
description: "Build and flash RuView ESP32 firmware (8MB or 4MB), then confirm the CSI stream."
category: general-purpose
source_repo: ruvnet/RuView
source_path: "plugins/ruview/commands/ruview-flash.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/plugins/ruview/commands/ruview-flash.md
---


# /ruview-flash

Build + flash RuView firmware to an ESP32-S3 sensing node.

1. Invoke the **`ruview-hardware-setup`** skill.
2. Determine variant from `$ARGUMENTS` (default `8mb`). For `4mb`: `cp firmware/esp32-csi-node/sdkconfig.defaults.4mb firmware/esp32-csi-node/sdkconfig.defaults` first. For `8mb`: ensure it's built from `sdkconfig.defaults.template` (no mock).
3. Build using the **Python-subprocess** command from `CLAUDE.local.md` (ESP-IDF v5.4 does NOT work under Git Bash — strip `MSYSTEM*` env vars). Never use `cmd.exe /C` from bash.
4. Flash: same subprocess, `[python, idf_py, '-p', '<COM port>', 'flash']` (default port **COM8**), or `python -m esptool ... write_flash ...` with the four binaries.
5. Confirm: serial monitor via pyserial (not `idf.py monitor`), then `cd v2 && cargo run -p wifi-densepose-sensing-server` to see frames arrive.
6. If no frames: re-run `/ruview-provision`, check channel matches the AP, drop any `--filter-mac`.

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `plugins/ruview/commands/ruview-flash.md`
