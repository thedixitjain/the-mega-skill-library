---
name: ruview-provision
description: "Provision WiFi credentials, sink IP, and optional channel / MAC-filter overrides onto a RuView ESP32 node."
category: security-and-compliance
source_repo: ruvnet/RuView
source_path: "plugins/ruview/commands/ruview-provision.md"
source_url: https://github.com/ruvnet/RuView/blob/HEAD/plugins/ruview/commands/ruview-provision.md
---


# /ruview-provision

Write NVS config to an ESP32 sensing node.

1. Invoke the **`ruview-configure`** skill (§"Runtime device config" — has the full `provision.py` flag table).
2. Run `python firmware/esp32-csi-node/provision.py --help` for the authoritative options (on Windows: `PYTHONUTF8=1 PYTHONIOENCODING=utf-8 python …` — the help text has non-ASCII). Collect any missing params (port — default **COM8**, SSID, password, target sink IP, `--target-port` default 5005, `--node-id`).
3. Run:
   ```bash
   python firmware/esp32-csi-node/provision.py --port <PORT> \
     --ssid "<SSID>" --password "<PW>" --target-ip <IP> --target-port 5005 --node-id <0-255> \
     [--channel <N>] [--filter-mac <MAC>] [--hop-channels 1,6,11 --hop-dwell 200] \
     [--tdm-slot <i> --tdm-total <n>] [--edge-tier {0|1|2}] [--pres-thresh 50] [--fall-thresh 15000] \
     [--vital-win 300] [--vital-int 1000] [--subk-count 32] \
     [--seed-url http://… --seed-token … --zone lobby] [--swarm-hb 30] [--swarm-ingest 5] [--dry-run]
   ```
4. Explain trade-offs: `--channel` pins the node (AP's channel) vs. `--hop-channels` for ADR-061 multi-freq hopping; `--filter-mac` restricts to one transmitter vs. omit for all (more data, more noise); `--edge-tier` 0/1/2 = off/stats/vitals; `--tdm-slot`/`--tdm-total` slot a multi-node mesh.
5. ⚠️ **Issue #391**: flashing rewrites the *entire* `csi_cfg` NVS namespace — every key not on the CLI is erased. Pass the full set you want; warn the user before re-provisioning a working node. `--force-partial` bypasses the WiFi-creds requirement (knowingly). `--dry-run` builds the NVS binary without flashing.
6. Fleet provisioning: `scripts/generate_nvs_matrix.py` (subprocess-first).
7. Verify: serial monitor (pyserial on the port, 115200) should show `adaptive_ctrl` ticks + `csi_collector: CSI cb #… len=128 …` lines; the sink (`cd v2 && cargo run -p wifi-densepose-sensing-server`) should report incoming UDP frames if `--target-ip` points at this host.

---

**Source:** [`ruvnet/RuView`](https://github.com/ruvnet/RuView) → `plugins/ruview/commands/ruview-provision.md`
