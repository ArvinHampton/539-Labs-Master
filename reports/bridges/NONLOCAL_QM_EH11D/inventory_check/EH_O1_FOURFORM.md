# EH-O1 / four-form (cite only)
- 4k²+K=Φ/144 written in: EH1 23010998 txt:33 (with 6k²−3K=−Φ/96; :38 k²=Φ/1728, K=8k²); Lean statement in A22 chats/a01dcbad-…:745-760 (`L7_fibre_lock`, hypotheses h1,h2 assumed, not derived). Origin of h2 vs fibre block 10k²−2K: **ABSENT** (no derivation found; Lean takes it as hypothesis).
- Four-form: EH1 txt:83 "T(G4). Stress of the eleven-dimensional four-form."; :95 "fsnap. Inserted four-form jump fraction 243/4880."; :134 "Next check that can move L7: four-form weights Tμν/g=−G2/96 vs Tab/g=−G2/288." Status: listed as next, **not performed** in any source found.

## 2026-10-24 update — EH-FF1 (prereg/EH_FOURFORM_20261024, Cat A PASS, conditional)
- Weights written in Execute_Three_Advancement_Paths_2026-09-28.md:4 (a=1/24: Tμν/g=Tyy/g=−G²/96, Tab/g=−G²/288; CJS a=1/12 "other fork").
- Prereg sha256: PREREG.md 797367c2…4075c, run.py 576d65aa…100e. Result: P1 unique k²=Φ/1728, K=Φ/216; P2 h2 ≡ (Gab/g − Gμν/g) block difference; P3 controls (−Φ/144, −Φ/96 fibre weight) fail the lock → non-vacuous.
- **EH-O1 resolved at algebra level:** 4k²+K=Φ/144 is NOT independent; it is (10k²−2K) − (6k²−3K) with RHS −Φ/288+Φ/96. So h2 is DERIVED from L6 + a=1/24 four-form weights.
- Residual ASSUMPTIONS (not written as derivations anywhere found): (i) Φ ≡ G² (never stated as a definition; inferred by juxtaposition); (ii) 8πG11 = 1 normalisation (Lean EinsteinHamptonEquation carries 8πG11 explicitly); (iii) choice a=1/24 over CJS a=1/12 — no derivation of the convention; CJS-fork weights not written numerically → that fork untestable (gap).
