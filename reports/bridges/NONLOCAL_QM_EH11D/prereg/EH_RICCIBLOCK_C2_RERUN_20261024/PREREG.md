# EH-RB1-C2R prereg (written 2026-10-24 before run): rerun of EH-RB1 control C2 exactly as preregistered
Original C2 (prereg/EH_RICCIBLOCK_20261024/PREREG.md): "wrong dimension split (3 ext dims instead of 4, fibre 7 → still 11D) ⇒ G_ext ≠ 6k²−3K".
Discrepancy: the original run.py used a 3 ext + y + S^6 + 1 flat dimension split, which is not the preregistered split.
This rerun: metric e^{-2ky}η(3D, Lorentzian) + dy² + e^{2B} r² dΩ_7 (round S^7, κint=6/r²), and K := κint e^{-2B}.
PASS (control fails as required) iff G_ext/g ≠ 6k²−3K, and also G_fib/g ≠ 10k²−2K. FAIL otherwise (the original C2 would then be vacuous).
Also recorded, not a prediction: the exact G_ext expression.
