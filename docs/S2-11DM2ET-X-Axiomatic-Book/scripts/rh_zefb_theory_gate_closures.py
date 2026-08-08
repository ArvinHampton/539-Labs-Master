#!/usr/bin/env python3
import json
from pathlib import Path
p = Path(__file__).resolve().parents[1] / "rh_zefb_theory_gate_closures_results.json"
d = json.loads(p.read_text())
print(json.dumps({
    "status": d["status"],
    "closed": d["gate_closures"]["counts"]["closed_assets_and_locks"],
    "open": d["gate_closures"]["counts"]["open_resolution_gates"],
    "RH": d["gate_closures"]["counts"]["unconditional_RH_resolution"],
    "zefb": d["ZEFB"]["code"],
}, indent=2))
