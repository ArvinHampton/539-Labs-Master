#!/usr/bin/env python3
import json
from pathlib import Path
p = Path(__file__).resolve().parents[1] / "rh_open_routes_closure_analysis_results.json"
d = json.loads(p.read_text())
print(json.dumps(d["summary"], indent=2))
print(d["global_conclusion"][:240])
