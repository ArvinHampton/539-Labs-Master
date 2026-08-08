#!/usr/bin/env python3
"""Emit explore-all resolution map JSON (static ledger; no false theorems)."""
import json
from pathlib import Path

# Re-load sibling JSON if present, else minimal stub
here = Path(__file__).resolve().parents[1]
src = here / "rh_explore_all_resolutions_results.json"
if src.exists():
    data = json.loads(src.read_text())
else:
    data = {"status": "RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF", "note": "run package writer"}
print(json.dumps({"status": data.get("status"), "no_unconditional": data.get("no_unconditional_resolution_today"),
                  "n_paths": len(data.get("explored_resolution_paths", {})),
                  "n_dead": len(data.get("dead_routes_closed", [])),
                  "one_liner": data.get("global_conclusion", "")[:200]}, indent=2))
