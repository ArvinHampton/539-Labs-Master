#!/usr/bin/env python3
"""Pass-2 explore-all: load graph JSON and print verdict."""
import json
from pathlib import Path
p = Path(__file__).resolve().parents[1] / "rh_explore_all_resolutions_pass2_results.json"
d = json.loads(p.read_text())
print(json.dumps({
    "status": d["status"],
    "pass": d["pass"],
    "unconditional": len(d["unconditional_resolutions_found"]),
    "open_hyps": d["count_open_hypotheses"],
    "dead": d["count_dead_routes"],
    "proved_assets": d["count_proved_assets"],
    "verdict": d["global_verdict"][:240],
}, indent=2))
