# FINDINGS: PP Soft SF audit of Eigen O5/O6 pass 2 (2026-11-05, ~13:50 CST)
REPORTS ONLY. No CERT. tip untouched. invent HOLD STANDS. Under OW 06748ff2… (MATCH).
Input: 24bb435c051789364bcc… MATCH (22 lines). PRESS 0b89395d….
Verdict: CONFIRM, with 3 notes.
- O5(a): PP checked that 3 has order 42 mod 49 (3⁶ ≡ 43, not 1), so σ₃ generates the group. The logic holds. Status is honest as a "mod-p statement at one prime".
  - N1. A single prime can coincide by accident. Before the "field ℚ" result is relied on, repeat the σ₃ check at a second e1 prime. Until then, O5(a) and O5(b) are RESOLVED-mod-p, which is evidence, not a Tier P proof over ℚ.
- O5(c) REMAINING is fine: the lattice-bound diagnostic is sound, and the missing height bound is declared. O5(d) is not attempted and is declared as such.
- O6: PP recomputed with h₁=[0]+[1] and h₂=−[0]+[1]+3[2] in ℤ[ℤ/3]. Target [1] gives weights +1 and −1, so W=0, N=2. Target [0] gives W=2, N=4, and target [2] gives W=4, N=4. The chosen reading is unique and correctly labelled as not in the source.
  - N2. The definition of N, the sum of |path weights|, should be stated explicitly in the file.
- N3. The cited compute directory grok-batches/eigen-o5-n36-stab-2026-11-05/ does not exist under /workspace/quantum-comp. Fix the path before Keeper files it.
Soft SF → Auditor Keeper (once N3 is fixed).
