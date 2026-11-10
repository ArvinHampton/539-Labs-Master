# PREREG — BRIDGE_C_35 order59 (LOCAL Bridge C only)
Date: 2026-10-24 (America/Chicago). Local modular only. CORE_FREEZE: new files only in order59/. No push/send.
No P̂_orth / Ξ / k≠0 / Map-C6 letter→M_S used or invented.

## RG49 — S_lab convention lock (Cat A-numeric)
Convention: ρ(S) := S_lab^{-1}, ρ(T) := T. Source: Consolidated rev8 rem:Sconv; heavy-daily/2026-10-19-Certified-SRho-Check (step1_2_exact.json).
Input: data/my_matrices.npz (copy of 2026-10-19 ES, ET, EP exponent matrices, ζ=e^{2πi/140}, -1 = zero entry; S_lab = ζ^ES/√35).
Tests (float64, tol 1e-9 max-abs):
 T1 S_lab unitary; T2 S_lab²=P; T3 P²=I; T4 ρ(S)⁴=I;
 T5 (ρ(S)ρ(T))³ = ρ(S)²  [PASS required];
 C1 control: (S_lab T)³ = S_lab²  [must FAIL];  C2 info: P ≠ I.
RG49 PASS iff T1–T5 pass AND C1 fails. Convention only; M_S remains ABSENT.

## RG50 — a_H wire (CONDITIONAL)
a_H = √π(√1190 − 17√14)/170 (ERRATUM_Bridge_C_tminushalf_Coefficient_2026-10-17 E1). C≈0.8174 NOT used.
Condition: an existing hashed script claims the H_s t^{-1/2} coefficient. Audit (pre-test): em.py (res["H_s"][1]), closed_forms.py (PSLQ on a_H), em_check.py (numeric remainder check) in heavy-daily/2026-10-17-P_s-structure are git-tracked in _git_v8_unpushed_clone (blobs b0f34801, 78ceea29, 3c8f9683) and byte-identical (sha256 em.py 5fb526b5…, em_check.py a41af336…, closed_forms.py 78f3f8a4…). Condition MET → RUN.
Adapted script: scripts/rg50_aH.py (imports copied scripts/em.py unchanged).
Tests: A1 |res_H − a_H| < 1e-25 (mp.dps=30); A2 numeric: r(t)=H_s(t) − a_H/√t, require |r(t)|·... ratio r/√t stable: |r/√t(1e-4) − r/√t(2.5e-5)| < 1e-3.
Wrong-radical controls (must FAIL both A1 and A2): K1 √π(√1190 + 17√14)/170; K2 √π(√1191 − 17√14)/170.
RG50 PASS iff A1,A2 pass and K1,K2 fail.
