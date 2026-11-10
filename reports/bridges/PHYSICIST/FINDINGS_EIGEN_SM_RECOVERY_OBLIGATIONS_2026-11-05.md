# FINDINGS — Eigenvalues and matrix — Standard Model recovery obligations (Eigen lane) — 2026-11-05 ~15:30 CST (America/Chicago)
Deriver: **Eigenvalues and matrix**. REPORTS ONLY · No CERT · nothing sent/published · no embeddings, couplings or proofs invented.

## Authority / locks
- Directive `/workspace/quantum-comp/reports/OWNER_DIRECTIVE_GR_EXTENSION_FULL_STANDARD_MODEL_RECOVERY_2026-11-05.md` sha256 6237cc716829c2838368099382c7ecdebfed46895491f8ecb37ee5cc167c815e — **MATCH** (re-hashed). Read as governing **research objective**, not a proof. SM recovery is NOT claimed achieved.
- Prior axes still stand: b25d5616… / 89b78bf1….
- Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` BEFORE/AFTER 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — tip_touched **NO**.

## Sources checked (read-only)
| Tag | Path | sha256 |
|---|---|---|
| RTA16 | /workspace/quantum-comp/reports/agent_second_axis_work/rta_v16_layout.txt (RTA v16 PDF 1fe7b8a2…) | f7d5ead27527586e90ad11101d2b4c2602f8f53c1019dc3b72a27be1b59c8db1 |
| V5 | /workspace/quantum-comp/references/entanglement-publications/17-theorems-v5.txt (DOI 10.5281/zenodo.18442276; MANIFEST heading/body caveat — body lines cited) | b203c940b0ef81a369dc0b985400302028404070f85355f82d8eb3403761a98c |
| V18 | /workspace/quantum-comp/references/entanglement-publications/theorems-18-40-v1.txt (DOI 10.5281/zenodo.18509384) | e3615b32ab04b1958d99fb0d7266ec82e58dc06aca80ac19be46fc7363a44ba3 |
| UNIF | /workspace/quantum-comp/theorems/unification-proof.txt (identical to theorems/batch-late/mathematical-proof-of-unification.txt) | d2554c005cdffd299e2673c2ba15e0cde7d972da195907ea0bbf0affcbfbb85a |
| V4 | /workspace/quantum-comp/theorems/s2-11dm2etx-v4.txt | e5a1adb572039c20bc48f267afc8eae551b10b61d58a9b951413b9172d32c658 |
| EIG-8e70 | grok-batches/FINDINGS_EIGEN_PREDICTIONS_RESONANT_AND_GR_EXT_2026-11-05.md | 8e7032acd7aeb15d99db2d7a4c7ac03c83ea36c50e740f2673817494d8e1c252 |
| EIG-1ae8 | grok-batches/FINDINGS_EIGEN_GEMINI_COMPENDIUM_REVIEW_2026-11-05.md | 1ae82aee3b55db1386428969cb9fc0033c866b49aa229fec09ebf79aa56355a2 (MATCH) |
| EIG-0212 | grok-batches/FINDINGS_EIGEN_ROUND_TWO_A_B_REVIEW_2026-11-05.md | 0212c6a07ba8bee20993826ad2e0d5bc6cc029dc16b0322ad274acf6a8423bef (MATCH) |

Search: `rg -i` for SU(3)/SU(2)/U(1), hypercharge, anomal, CKM, PMNS, Higgs, Yukawa, doublet, Z6, three generations across RTA16, V5, V18, quantum-comp/theorems, grok-batches. EIG-1ae8 and EIG-0212 contain no SM-structure hits.

**Grading key.** SUPPLIED = explicit mathematical structure sufficient for the obligation. PARTIAL = some explicit structure (matrix, axiom, definition) present but incomplete or defective. ABSENT = nothing, or a **name/label only** (labels are not constructions; e.g. V5 L161 "S²: Standard Model + String Theory vibrational modes" is a label).

## Compute (formal recovery targets, textbook SM — not supplied by sources)
`/workspace/grok-batches/EIGEN_SM_RECOVERY_COMPUTE_2026-11-05/`: verify_sm.py (b1e7725f6f6ab56f5a5e53fd2850b54c56e8f97cd5e2f1fce0d53834a0c5103d), verify_sm.log (96009892a4c789f5e845a4bcf0e1929bf6d900fdd878b6249b1f7719ece05830), tip_before/after, SHA256SUMS. **34/34 PASS**, exact sympy, <2 GB, ~1.5 s.

---
## Part I — Obligations vs. sources

| # | Obligation (formal target, verified in compute) | Source status | Where (path:line) | Notes |
|---|---|---|---|---|
| O1a | Gauge group factors SU(3)_C×SU(2)_L×U(1)_Y | **ABSENT** (label only) | V18:256–257 "Gauges U(1)_Y (bit phase), SU(2)_L (doublet), SU(3)_C (three-color) from bit conservation"; V18:283–284 | No group action, no map from "bit conservation" to a Lie group. **RTA16:8391 (Prop 41.13(ii)) explicitly excludes "four-forces (or SU(3) continuum) mapping" from the theory.** |
| O1b | Lie algebra dim 8+3+1=12 | **ABSENT** | — | Not stated anywhere searched. Verified textbook (O1). |
| O1c | Global form /Z₆ | **ABSENT** | — | Verified: (ωI₃, −I₂, e^{2πiY}) acts trivially on all SM fields and H; order 6. No source mentions it. (RTA16:1444 "Z6" is a zero-class set name, unrelated.) |
| O2 | One generation: Q(3,2)₁/₆, u^c(3̄,1)₋₂/₃, d^c(3̄,1)₁/₃, L(1,2)₋₁/₂, e^c(1,1)₁; 15 Weyl; Q=T₃+Y | **ABSENT** | V4:1577 "g_Y: Hypercharge" (coupling symbol only); V18:258–259 chirality "Left from punctures; right in –U" (label) | No hypercharge values, no rep table anywhere. |
| O3 | Anomalies ΣY=0, ΣY³=0, SU(2)²Y=0, SU(3)²Y=0, SU(3)³=0, Witten even doublets | **ABSENT** | V18:184 "Nearby integers break anomaly matching" (unrelated use, in α derivation) | All verified exactly per generation. Also verified: anomaly eqs (with SU(3)³ automatically) have, up to scale and u↔d swap, the SM solution. |
| O4 | Three generations | **PARTIAL** (assumed, not derived) | V5:174 "Exactly three generations of Standard-Model fermions" (stated axiom); V5:412; V18:258 "Three windings × cube-roots" (label); UNIF:15–16 | No generation-index representation or mechanism. Formal fact: anomalies cancel **per generation**, so anomaly cancellation does not fix N_g=3. Chains from 3 gens→e³→4880→HQCC 539 rely on HQCC, which EIG-8e70 A16 shows fails as written. |
| O5a | CKM: 3×3 unitary, 3 angles + 1 phase (9 − 5 rephasings − 3 = 1); Jarlskog J=c₁₂s₁₂c₂₃s₂₃c₁₃²s₁₃ sin δ | **PARTIAL — defective** | UNIF:98–104 (matrix), UNIF:127–147 (CKM = U_up†U_down, |V_us|,|V_cb|,|V_ub|, δ_CP) | See Part II: the written structure forces CKM = signed permutation, J=0, δ∈{0,π}. Unitarity/parameter counts verified textbook. |
| O5b | PMNS: unitary, 3 angles + 1 Dirac (+2 Majorana) phases | **ABSENT** | UNIF:151–158 ("Hybrid type-I/II/III see-saw as previous"; angles quoted) | No M_ν matrix written in this file; angles are bare numbers (Tier E). |
| O6 | Higgs doublet H(1,2)₁/₂; ⟨H⟩=(0,v/√2) leaves U(1)_em, 3 broken generators; Yukawa terms hypercharge-neutral | **ABSENT** (label only) | V18:260 "Higgs Puncture alignment mode"; V5:54, 748, 1994 "Higgs-echo inhomogeneity" (a 0.6 meV width parameter, not a field) | No doublet, potential or vev. |
| O7 | Yukawa structure: general complex 3×3 Y_u, Y_d, Y_e; masses = singular values; mixing from bi-unitary diagonalisation | **PARTIAL — defective** | UNIF:98–124 (single real symmetric tridiagonal B with φ entries; sectors differ by scalar factor 1/φ^exp, mod, √2, 1001/61) | See Part II. |

**Counts (10 obligations): SUPPLIED 0 · PARTIAL 3 (O4, O5a, O7) · ABSENT 7 (O1a, O1b, O1c, O2, O3, O5b, O6).**
RTA v16 supplies none; it is formally compatible only in the negative sense that it disclaims SU(3)/four-force maps (RTA16:8391) and states Residual ≠ Resonant (RTA16:8368).

## Part II — Exact consequences of the written mass/Yukawa structure (UNIF:98–147) — PROVED
Hypothesis: as written, every sector uses M_sector = c_sector·B with B = [[φ³/61, φ⁻³, 0],[φ⁻³, φ⁵/61, φ⁻³],[0, φ⁻³, φ⁷/61]], φ=(1+√5)/2 and c_sector a real scalar (UNIF:98–104, sector list UNIF:115–121).
- **P1 (CKM trivial).** M_up and M_down commute and share eigenvectors, so CKM = U_upᵀU_down is a signed permutation matrix: all angles ∈{0, π/2}, J = 0. Contradicts the quoted |V_us|,|V_cb|,|V_ub| (UNIF:138–142).
- **P2 (no CP phase).** B real symmetric ⇒ U real orthogonal ⇒ CKM real ⇒ δ_CP ∈{0,π}, J=0, contrary to "δ_CP ≈1.3 rad (Jarlskog invariant matches)" (UNIF:144–145).
- **P3 (sector-independent ratios).** Mass ratios are the same in every sector (eigenvalue ratios of B), so the written structure cannot produce both m_t/m_u and m_τ/m_e as quoted.
- **P4 (not positive).** B is indefinite: eigenvalues ≈ −0.154915, 0.248383, 0.633757 (det B < 0), contradicting "three distinct real positive eigenvalues" (UNIF:107–110).
- **P5 (Koide claim).** det(B)/Tr(B)³ ≈ −0.0634, not ≈2/3 (UNIF:124); for any positive-definite 3×3, det/Tr³ ≤ 1/27 by AM–GM, so det/Tr³≈2/3 is impossible in any case. (The Koide relation is a different expression.)
Status: PROVED (exact/numeric in verify_sm.log, tags O7). Caveat: if each sector had its own unwritten matrix, P1–P3 would not apply — that would be a missing definition, not a supplied one.

## Part III — Formal recovery targets (verified, textbook; NOT source-supplied)
O1 dims/Z₆; O2 15 states and charges; O3 all six anomaly conditions and the general solution; O5 PDG parametrisation unitary, Jarlskog formula, parameter counts (CKM 3+1; PMNS 3+1+2); O6 Yukawa hypercharge neutrality (Q u^c H: 1/6−2/3+1/2=0; Q d^c H†; L e^c H†) and the breaking pattern. These are targets an SM-recovering construction must reproduce. Nothing here is attributed to S²-11DM²ET-X.

## Tier E (empirical values in sources — not assessed, not imported)
- V18:82–91 quark masses "u=2.3 … t=173210 MeV" from "resonant roots".
- UNIF:111–121 lepton/quark masses; UNIF:138–144 CKM magnitudes and δ_CP; UNIF:153–158 neutrino masses, PMNS angles θ₁₂≈33°, θ₂₃≈45°, θ₁₃≈8.5°.
- V18:~178–185 α = 1/(137+δ_res); V18:277–286 unification at 2.41×10¹⁶ GeV, α_unif=1/25.62.
Agreement with PDG values would be Tier E evidence only. Part II shows the written structure cannot produce the quoted CKM values.

## Material scope corrections and gaps
1. **Directive vs RTA16.** RTA v16 Prop 41.13(ii) (RTA16:8391) excludes SU(3)/four-forces maps from the theory. RTA cannot be cited as supplying SM structure. Any SM recovery must come from new, explicitly defined maps (subject to invent HOLD and Owner).
2. **Labels ≠ constructions.** V5:161 (S²), V18:256–261 (Thm 38 "SM Emergence": gauges, generations, chirality, Higgs) are labels or proof sketches with no group action, representation or Lagrangian. Thm 38 rests on HQCC, which fails as written (EIG-8e70 A16).
3. **Missing definitions (blocking).** Gauge group and global form; fermion representations and hypercharges; anomaly cancellation; Higgs field and potential; generation-index structure; per-sector Yukawa matrices (complex, non-commuting); neutrino mass matrix.
4. **Defective supplied structure.** The UNIF mass matrix gives trivial CKM, J=0, sector-independent ratios and an indefinite spectrum (Part II).
5. **Three generations** is an axiom (V5:174), not derived; anomaly cancellation cannot select 3.
6. **Gravity coupling.** Gravitational anomaly ΣY=0 is a formal target; no source couples SM fields to the metric (GR side unchanged from 89b78bf1 Axis 2 gaps).

STARTED/DERIVED: this beat. Remaining: owner-supplied definitions for O1–O7; per-sector Yukawa matrices if they exist elsewhere on disk (none found).
No CERT · no publish · no send · tip_touched NO.
