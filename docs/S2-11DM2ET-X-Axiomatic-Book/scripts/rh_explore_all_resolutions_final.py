#!/usr/bin/env python3
import json
from pathlib import Path
p = Path(__file__).resolve().parents[1] / "rh_explore_all_resolutions_final_results.json"
d = json.loads(p.read_text())
print(json.dumps({
    "unconditional": len(d["unconditional_resolutions_found"]),
    "closed": d["closed_count"],
    "open": d["open_count"],
    "routes": d["routes_total"],
    "available": d["routes_available"],
}, indent=2))
