#!/usr/bin/env python3
import json
from pathlib import Path
p = Path(__file__).resolve().parents[1] / "rh_vk_ef_full_review_results.json"
d = json.loads(p.read_text())
print(json.dumps({
    "status": d["status"],
    "n_correlations": len(d["correlations"]),
    "n_missed_angles": len(d["missed_angles"]),
    "n_patterns": len(d["patterns"]),
    "one_liner": d["global_conclusion"][:240],
}, indent=2))
