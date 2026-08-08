#!/usr/bin/env python3
import json
from pathlib import Path
p = Path(__file__).resolve().parents[1] / "rh_explore_resolutions_pass4_results.json"
d = json.loads(p.read_text())
print(json.dumps({
    "pass": d["pass"],
    "unconditional": len(d["unconditional_resolutions_found"]),
    "routes": len(d["routes_explored_this_pass"]),
    "verdict": d["global_verdict"][:200],
}, indent=2))
