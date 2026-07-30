import { existsSync, readFileSync, writeFileSync } from "node:fs";

/**
 * The minimum .env.local handling the setup scripts need (the Next app loads
 * the same file with its own loader). `KEY=value` and `KEY="value"` only.
 * Keys already present in the shell win, comments and unknown lines are
 * preserved on save.
 */
const ENV_FILE = ".env.local";

export function loadEnvLocal(): void {
  if (!existsSync(ENV_FILE)) return;
  for (const line of readFileSync(ENV_FILE, "utf8").split("\n")) {
    const match = /^([A-Za-z_][A-Za-z0-9_]*)=(.*)$/.exec(line.trim());
    if (!match || process.env[match[1]] !== undefined) continue;
    // Strip one pair of surrounding quotes so a quoted key in .env.local is
    // the same secret here as it is to Next. A quote baked into the vault
    // value would 403 every vendor call.
    process.env[match[1]] = match[2].trim().replace(/^(["'])(.*)\1$/, "$2");
  }
}

export function saveEnvLocal(patch: Record<string, string>): void {
  const pending = new Map(Object.entries(patch));
  const lines = existsSync(ENV_FILE) ? readFileSync(ENV_FILE, "utf8").split("\n") : [];

  const merged = lines.map((line) => {
    const key = /^([A-Za-z_][A-Za-z0-9_]*)=/.exec(line.trim())?.[1];
    if (!key || !pending.has(key)) return line;
    const value = pending.get(key)!;
    pending.delete(key);
    return `${key}=${value}`;
  });
  while (merged.length > 0 && merged[merged.length - 1].trim() === "") merged.pop();
  for (const [key, value] of pending) merged.push(`${key}=${value}`);

  // Owner-only: this file holds three API keys. (mode applies on create;
  // a pre-existing .env.local keeps whatever permissions you gave it.)
  writeFileSync(ENV_FILE, `${merged.join("\n")}\n`, { mode: 0o600 });
}

export function requireEnv(name: string, hint?: string): string {
  const value = process.env[name];
  if (value) return value;
  console.error(`\nMissing ${name} (set it in ${ENV_FILE}).${hint ? `\n  ${hint}` : ""}`);
  process.exit(1);
}
