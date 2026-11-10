# RESULTS — BRIDGE_C_35 order59 (LOCAL Bridge C only)
PREREG.md sha256 bec0231d04935da34142bf8195f8a1b73e8ce06bbfbfa655376e8e7f7bd64260 (hashed before any test; re-verified OK).

## RG49 — S_lab convention lock: PASS (Cat A-numeric)
ρ(S)=S_lab^{-1}, ρ(T)=T. Max-abs residuals: unitary 5.8e-15; S_lab²=P 5.8e-15; P²=I 6.7e-15; ρ(S)⁴=I 1.1e-14; (ρ(S)ρ(T))³=ρ(S)² 1.2e-14 PASS.
Control (S_lab T)³=S_lab² residual 1.00 → FAILS as required. P≠I (residual 1.00). Agrees with 2026-10-19 step1_2_exact.json (exact).
Convention lock only; Map-C6 letter→M_S ABSENT (not invented).

## RG50 — a_H wire: PASS (condition MET)
Audit: em.py (res["H_s"][1]), closed_forms.py (PSLQ on a_H), em_check.py (numeric) claim the H_s t^{-1/2} coefficient; git-tracked in _git_v8_unpushed_clone and byte-identical to heavy-daily copies.
a_H = √π(√1190−17√14)/170 = −0.30352541272067272833…; |em.res − a_H| = 3.9e-31. Numeric: (H_s(t) − a_H/√t)/√t = −0.395961 (t=1e-4), −0.395946 (t=2.5e-5); drift 1.5e-5 → remainder O(√t), t^{-1} term 0.
Wrong-radical controls FAIL: K1 (+17√14) diff 1.33, drift 4.0e4; K2 (√1191) diff 1.5e-4, drift 4.53.
C≈0.8174 not used.

## Files
PREREG.md, PREREG.sha256, scripts/{rg49_sconv.py,rg50_aH.py,em.py(unchanged copy)}, data/{my_matrices.npz(copy),rg49.json,rg50.json}, logs/{rg49.log,rg50.log}, SHA256SUMS.
