#!/usr/bin/env python3
import json
from pathlib import Path
p = Path(__file__).resolve().parents[1] / "rh_zfr_grh_ffml_results.json"
d = json.loads(p.read_text())
print(json.dumps({
    "status": d["status"],
    "zf_rows": len(d["zero_free_regions"]["zf_table_schematic"]),
    "grh_resolves_RH": d["Grand_Riemann_Hypothesis"]["resolves_RH_unconditionally"],
    "ffml": d["FFML"]["code"],
    "unconditional": d["unconditional_resolutions"],
}, indent=2))
