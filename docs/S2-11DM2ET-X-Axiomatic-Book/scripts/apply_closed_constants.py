#!/usr/bin/env python3
"""Apply closed-constant replacements across S2-11DM2ET-X corpus."""
from __future__ import annotations

import json
import os
import re
import shutil
import zipfile
from datetime import datetime, timezone
from pathlib import Path

CONST = {
    "kappa_dark": "243/539",
    "kappa_dark_f": 243 / 539,
    "f_snap": "243/4880",
    "f_snap_f": 243 / 4880,
    "beta_pbh": "11/61",
    "beta_pbh_f": 11 / 61,
    "two_beta": 2 * 11 / 61,
}

TEXT_REPLACEMENTS: list[tuple[str, str]] = [
    # kappa
    (r"KAPPA_DARK\s*\|\s*0\.45\b", "KAPPA_DARK | 243/539"),
    (r"kappa_dark\s*=\s*0\.45\b", "kappa_dark = 243/539"),
    (r"\\kappa_\{\\rm dark\}\s*=\s*0\.45\b", r"\\kappa_{\\rm dark} = 243/539"),
    (r"\\kappa_\{\\mathrm\{dark\}\}\s*=\s*0\.45\b", r"\\kappa_{\\mathrm{dark}} = 243/539"),
    (r"κ_dark\s*=\s*0\.45\b", "κ_dark = 243/539"),
    (r"derived from the same κ_dark\s*=\s*0\.45", "derived from κ_dark = 243/539"),
    # beta
    (r"beta_PBH\s*=\s*0\.18\b", "beta_PBH = 11/61"),
    (r"\\beta_\{\\rm PBH\}\s*=\s*0\.18\b", r"\\beta_{\\rm PBH} = 11/61"),
    (r"\\beta_\{\\mathrm\{PBH\}\}\s*=\s*0\.18\b", r"\\beta_{\\mathrm{PBH}} = 11/61"),
    (r"\\beta_\{\\text\{PBH\}\}\s*=\s*0\.18\b", r"\\beta_{\\text{PBH}} = 11/61"),
    (r"β_PBH\s*=\s*0\.18\b", "β_PBH = 11/61"),
    (r"β_PBH\s*≈\s*0\.18\b", "β_PBH = 11/61"),
    (r"β_PBH\(eff\)\s*≈\s*0\.18", "β_PBH = 11/61"),
    (r"amplitude β_PBH\s*=\s*0\.18", "amplitude β_PBH = 11/61"),
    (r"echo amplitude 0\.18", "echo amplitude 11/61"),
    (r"amplitude 0\.18\s*ρ_DM", "amplitude (11/61) ρ_DM"),
    (r"with amplitude 0\.18", "with amplitude 11/61"),
    (r"Raw β_PBH capped at ~0\.0304; effective 0\.18 via void dilution/leakage",
     "β_PBH = 11/61 exactly (D/|P|); void-dilution scaffolding retired"),
    (r"reconciles with observed 0\.18", "matches closed value 11/61"),
    (r"for β_PBH\s*=\s*0\.18 after void", "for β_PBH = 11/61 (closed)"),
    (r"required for β_PBH\s*=\s*0\.18 after", "required for closed β_PBH = 11/61"),
    (r"fixes β_PBH\(eff\)\s*≈\s*0\.18", "fixes β_PBH = 11/61"),
    (r"β_PBH=0\.18 at", "β_PBH=11/61 at"),
    # snap / ring
    (r"ρ_snap\s*=\s*0\.05\s*ρ_DM", "ρ_snap = (243/4880) ρ_DM"),
    (r"ρsnap=0\.05", "ρsnap=(243/4880)"),
    (r"0\.05\s*ρ_DM", "(243/4880) ρ_DM"),
    (r"0\.05\s*\\rho_\{\\rm DM\}", r"(243/4880)\\rho_{\\rm DM}"),
    (r"0\.05\s*GM/c", "(243/4880) GM/c"),
    (r"saturates at 0\.05 GM", "saturates at (243/4880) GM"),
    (r"photon-ring thickness \(0\.05 GM/c", "photon-ring thickness (243/4880 GM/c"),
    (r"Δr_\{?\\text\{ring\}\}? ≈ 0\.05", r"Δr_{ring} = (243/4880)"),
    (r"\\\\Delta r_\{\\text\{ring\}\} \\\\approx 0\.05", r"\\\\Delta r_{\\\\text{ring}} = (243/4880)"),
    # broken formula
    (r"61\s*[×x\*]\s*243\s*/\s*4880\s*[≈=]\s*0\.030[0-9]*",
     "11/61 [closed β_PBH; retired false 61*243/4880]"),
    (r"61\s*\\\\times\s*243\s*/\s*4880", r"11/61"),
    # waveform sin amplitude (legacy 0.18 ~ beta)
    (r"\+\s*0\.18\s*[×x]\s*sin", "+ (11/61) × sin"),
    (r"\+\s*0\.18\s*\\\\sin", r"+ (11/61)\\sin"),
    (r"\+\s*0\.18\s*\\sin", r"+ (11/61)\\sin"),
    (r"\+\s*0\.18\s*sin", "+ (11/61) sin"),
    (r"0\.18\s*×\s*sin", "(11/61) × sin"),
    (r"0\.18\s*\\\\times\s*sin", r"(11/61)\\times sin"),
    (r"0\.18\s*×\s*cos\(2πt / 539\.9\)", "(11/61) × cos(2πt / 539.9)"),
    (r"0\.18\s*\\cos\(2\\pi t / 539\.9\)", r"(11/61)\\cos(2\\pi t / 539.9)"),
    (r"\\\\approx 0\.36\s*\\\\,?\s*\\\\cos", rf"\\\\approx {CONST['two_beta']:.4f}\\\\,\\\\cos"),
    (r"≈\s*0\.36\s*cos", f"≈ {CONST['two_beta']:.4f} cos"),
]

DOCX_SUBS = [
    ("κ_dark = 0.45", "κ_dark = 243/539"),
    ("κ_dark=0.45", "κ_dark=243/539"),
    ("kappa_dark = 0.45", "kappa_dark = 243/539"),
    ("derived from the same κ_dark = 0.45", "derived from κ_dark = 243/539"),
    ("derived from the same κ_dark=0.45", "derived from κ_dark=243/539"),
    ("β_PBH = 0.18", "β_PBH = 11/61"),
    ("β_PBH=0.18", "β_PBH=11/61"),
    ("beta_PBH = 0.18", "beta_PBH = 11/61"),
    ("β_PBH ≈ 0.18", "β_PBH = 11/61"),
    ("β_PBH(eff) ≈ 0.18", "β_PBH = 11/61"),
    ("β_PBH(eff)≈0.18", "β_PBH=11/61"),
    ("amplitude β_PBH = 0.18", "amplitude β_PBH = 11/61"),
    ("A_echo = β_PBH = 0.18", "A_echo = β_PBH = 11/61"),
    ("echo amplitude 0.18", "echo amplitude 11/61"),
    ("amplitude 0.18 ρ_DM", "amplitude (11/61) ρ_DM"),
    ("with amplitude 0.18", "with amplitude 11/61"),
    ("ρ_snap = 0.05 ρ_DM", "ρ_snap = (243/4880) ρ_DM"),
    ("ρ_snap=0.05 ρ_DM", "ρ_snap=(243/4880) ρ_DM"),
    ("ρsnap=0.05", "ρsnap=(243/4880)"),
    ("0.05 ρ_DM", "(243/4880) ρ_DM"),
    ("0.05 GM/c²", "(243/4880) GM/c²"),
    ("0.05 GM/c^2", "(243/4880) GM/c^2"),
    ("saturates at 0.05 GM/c²", "saturates at (243/4880) GM/c²"),
    ("0.05 GM/c² instead of zero", "(243/4880) GM/c² instead of zero"),
    ("Δr_ring ≈ 0.05 GM/c²", "Δr_ring = (243/4880) GM/c²"),
    ("61 × 243 / 4880 ≈ 0.03036885", "11/61 ≈ 0.180328 [closed β_PBH]"),
    ("61 × 243 / 4880 = 14823 / 4880 ≈ 0.03036885",
     "β_PBH = 11/61 (closed); retired false 61×243/4880"),
    ("Raw β_PBH capped at ~0.0304; effective 0.18 via void dilution/leakage",
     "β_PBH = 11/61 exactly (D/|P|); void-dilution scaffolding retired"),
    ("reconciles with observed 0.18", "matches closed value 11/61 ≈ 0.1803"),
    ("for β_PBH = 0.18 after void dilution", "for β_PBH = 11/61 (closed)"),
    ("required for β_PBH = 0.18 after void dilution", "required for closed β_PBH = 11/61"),
    ("fixes β_PBH(eff) ≈ 0.18 after void dilution", "fixes β_PBH = 11/61"),
    ("β_PBH=0.18 at 5σ", "β_PBH=11/61 at 5σ"),
    ("β_PBH=0.18 at 6σ", "β_PBH=11/61 at 6σ"),
    ("≈ 0.36 cos", f"≈ {CONST['two_beta']:.4f} cos"),
    ("≈0.36 cos", f"≈{CONST['two_beta']:.4f} cos"),
]

KEYWORDS = (
    "kappa", "PBH", "snap", "539.9", "S2-11", "HQCC", "β_PBH", "beta_PBH",
    "KAPPA_DARK", "rho_snap", "0.05 GM", "photon ring", "κ_dark", "negPBH",
)


def patch_text(content: str) -> tuple[str, bool]:
    orig = content
    for pat, repl in TEXT_REPLACEMENTS:
        content = re.sub(pat, repl, content, flags=re.IGNORECASE)
    return content, content != orig


def patch_docx(path: str) -> tuple[bool, str]:
    try:
        with zipfile.ZipFile(path, "r") as zin:
            xml = zin.read("word/document.xml")
    except Exception as e:
        return False, str(e)
    s = xml.decode("utf-8", errors="ignore")
    orig = s
    for a, b in DOCX_SUBS:
        s = s.replace(a, b)
    if s == orig:
        return False, "no-change"
    tmp = path + ".tmp_closed.docx"
    with zipfile.ZipFile(path, "r") as zin, zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            data = zin.read(item.filename)
            if item.filename == "word/document.xml":
                data = s.encode("utf-8")
            zout.writestr(item, data)
    shutil.move(tmp, path)
    return True, "patched"


def main() -> None:
    log: list[dict] = []
    text_roots = [
        r"C:\Users\bradl\S2-11DM2ET-X-Axiomatic-Book",
        r"C:\Users\bradl\Downloads",
        r"C:\Users\bradl\Desktop\539Labs\docs",
    ]
    for root in text_roots:
        if not os.path.isdir(root):
            continue
        for dp, dns, fns in os.walk(root):
            dns[:] = [d for d in dns if d not in ("venv", ".git", "node_modules", "__pycache__")]
            for fn in fns:
                if not fn.lower().endswith((".tex", ".md", ".txt", ".py", ".json")):
                    continue
                if "timing" in fn.lower() and fn.endswith(".txt"):
                    continue
                if fn == "apply_closed_constants.py":
                    continue
                # Do not rewrite the SSOT / log files (they document legacy forms).
                if fn in (
                    "CLOSED_CONSTANTS.md",
                    "EXECUTION_LOG_closed_constants.json",
                    "EXECUTION_SUMMARY.md",
                    "Resolved_BH_negPBH_GW250114_Statement.md",
                ):
                    continue
                path = os.path.join(dp, fn)
                try:
                    with open(path, "r", encoding="utf-8", errors="ignore") as f:
                        text = f.read()
                except OSError:
                    continue
                if not any(k in text for k in KEYWORDS):
                    continue
                new, changed = patch_text(text)
                if changed:
                    with open(path, "w", encoding="utf-8", newline="") as f:
                        f.write(new)
                    log.append({"path": path, "note": "text closed-constants patch"})
                    print("TEXT", path)

    docx_roots = [
        r"C:\Users\bradl\OneDrive\Imports",
        r"C:\Users\bradl\Downloads",
    ]
    name_keys = [
        "S2", "11DM", "HQCC", "PBH", "Hyperbolic", "negPBH", "Brane", "Unification",
        "Theorem", "Gabriel", "Qutrit", "Collatz", "Hampton", "539", "Friction",
        "Math", "Axiom", "Torsion", "Neutrino", "Galactic", "Stellar", "Solar",
        "CMB", "Entanglement", "Leakage", "MCP", "M-CP", "primordial", "Proof",
        "Resolution", "Rebuttal", "Paper", "Lemma", "Phase",
    ]
    docx_scanned = docx_changed = 0
    for root in docx_roots:
        if not os.path.isdir(root):
            continue
        for dp, _dns, fns in os.walk(root):
            for fn in fns:
                if not fn.lower().endswith(".docx"):
                    continue
                if not any(k.lower() in fn.lower() for k in name_keys):
                    continue
                path = os.path.join(dp, fn)
                docx_scanned += 1
                ok, msg = patch_docx(path)
                if ok:
                    docx_changed += 1
                    log.append({"path": path, "note": f"docx {msg}"})
                    print("DOCX", path)

    out_dir = Path(r"C:\Users\bradl\S2-11DM2ET-X-Axiomatic-Book")
    payload = {
        "when": datetime.now(timezone.utc).isoformat(),
        "constants": CONST,
        "changes": log,
        "docx_scanned": docx_scanned,
        "docx_changed": docx_changed,
        "text_changed": sum(1 for x in log if x["note"].startswith("text")),
    }
    log_path = out_dir / "EXECUTION_LOG_closed_constants.json"
    with open(log_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    print("DOCX scanned", docx_scanned, "changed", docx_changed)
    print("TOTAL changes", len(log))
    print("Wrote", log_path)


if __name__ == "__main__":
    main()
