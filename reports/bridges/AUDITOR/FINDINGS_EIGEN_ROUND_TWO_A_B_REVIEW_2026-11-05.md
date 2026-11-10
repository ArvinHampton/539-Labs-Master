# FINDINGS — Eigen Round Two: Owner docs A (audit-response) + B (formal corrections) — 2026-11-05 ~14:28 CST America/Chicago

REPORTS ONLY. **No CERT.** Independent second review ≠ endorsement. No invented proofs. No adopting source locks. Nothing sent (no manuscript / config / Gemini). Tip untouched.
Authority intake: `/workspace/pqc-round-two-intake-20261105/parent-relayed-owner-authorization-and-routing.json` sha `22b6556a9e1180865f456734e4e831d08a3f38faa061c0e9272bbb4a2c547425` (parent-relayed Owner voice ~14:23 CST).

## Integrity
| object | sha256 | note |
|---|---|---|
| **A** OWNER_DOCUMENT_ANALYTICAL_REVIEW_AUDIT_RESPONSES_… | `d5b1aae55e24e70290a6feb8c83f70b59cb1f68ea8183e280550bd6bfbadbfd3` | MATCH expected d5b1aae5… |
| **B** OWNER_DOCUMENT_FORMAL_RESOLUTIONS_STRUCTURAL_CORRECTIONS_… | `9c6f83da4f8636b0a6afbf108cbf7139210a82be936cadc94b772784451ded6d` | MATCH expected 9c6f83da… |
| tip BEFORE | `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` | |
| tip AFTER | (footer) | tip_touched **NO** |

## Reused Eigen work (COMPLETED refs — not redone)
| short | full sha | path |
|---|---|---|
| 1ae82aee | `1ae82aee3b55db1386428969cb9fc0033c866b49aa229fec09ebf79aa56355a2` | FINDINGS_EIGEN_GEMINI_COMPENDIUM_REVIEW_2026-11-05.md |
| 8e7032ac | `8e7032acd7aeb15d99db2d7a4c7ac03c83ea36c50e740f2673817494d8e1c252` | FINDINGS_EIGEN_PREDICTIONS_RESONANT_AND_GR_EXT_2026-11-05.md |
| 24bb435c | `24bb435c051789364bcc2835bd5deb1efc11bee68f8ad199adbf3dca2abdb5cf` | FINDINGS_EIGEN_SOFTSF_O5_N36_STABILIZER_O6_READING_2026-11-05.md |
| deebdc5e | `deebdc5ebd5ae483b4b18ef374c0efb6c4bb8da82cb7e3f26e05bc90af979211` | FINDINGS_EIGEN_SOFTSF_LOOSEN_CAT_B_11D_TERNARY_2026-11-05.md |
| de8cadc3 | `de8cadc3c3f5d0bec258cb64b419fb676afe24644cd7b96e99fbba5b77ccb8c7` | FINDINGS_EIGEN_SOFTSF_AMEND_LOOSEN_CAT_B_S2_11DM2ETX_2026-11-05.md |
| 9f7ecd77 | `9f7ecd7750201a2effc3a14f351274566c7ed49a7f1794e52835120bfd994e28` | FINDINGS_EIGEN_SOFTSF_ERRATUM_AMEND2_LOOSEN_CAT_B_2026-11-05.md |
| PP N1 | `72958342a46f7455010f8006510ef780baf7b29041aa9590eca4b43a4a2d5553` | FINDINGS_PP_SOFTSF_AUDIT_GEMINI_LANE_REVIEWS_EIGEN_OPS_LOCAL_2026-11-05.md |

Residual ≠ Resonant (unchanged). Compute: `grok-batches/eigen-round-two-a-b-2026-11-05/compute/`.

---

# Document A — Analytical audit-response (by section)

## A§1 Structural Foundations, Tree Embeddings, & Dimensional Splitting

### Questions (Eigenvalues and matrix)
1. **[Eigen]** A retracts metric isometry F:T₃→H¹¹ to quasi-isometry. If any Hilbert-/ℓ²-isometry U*U=I was previously implied, confirm it is withdrawn; what operator (if any) remains for Eigen to check?
2. **[Eigen]** The (4+1)⊕(5+1) split is called ill-defined. Does A assert that **no** projection calculus P_i on a named module exists, or only that the geometric junction is missing? (Force-as-projection was Eigen Q2 in 1ae82aee.)

### Statements
- S-A1.1: Tripod obstruction to isometric embedding into finite-dim Hⁿ is a Local/geometry claim; Eigen records it as out-of-lane for matrix checks (no F matrix on disk) — **COMPLETED** reuse 1ae82aee C12.
- S-A1.2: Dimensional-split arithmetic (5+6=11) alone is not a spectral object — **COMPLETED** 1ae82aee C15 (trivial arithmetic PROVED; vacuum-balance ABSENT).

### Exact proof requests
- PR-A1: None new in Eigen lane (geometry → Local). If Owner later supplies a Written boundary operator / Israel-matrix form, Eigen can check eigenvalues then.

### Supported offers
| id | offer | mark | ref |
|---|---|---|---|
| OA1a | No Bruhat–Tits isometry matrix ⇒ U*U=I unchecked | COMPLETED | 1ae82aee C12 |
| OA1b | (4+1)+(5+1)=11 arithmetic only | COMPLETED | 1ae82aee C15 |

**A§1 counts:** Q=2 · S=2 · PR=0 · offers=2 (both COMPLETED)

---

## A§2 Definitional Refutation of T₃^alt

### Questions
3. **[Eigen]** A cites T3_ref floor map and seed 4880 → {1,2} in 14 steps. Where on disk is the Soft SF artifact (path+sha) that Eigen should treat as the locked T3_ref definition (not narrative)?
4. **[Eigen]** A states orbits converge 3-adically to ±1/2 in infinite steps. Is any spectral/transfer-operator formulation of that 3-adic convergence claimed (e.g. ρ(T)<1 on a Banach space over ℚ₃), or is that purely valuation-language?

### Statements
- S-A2.1: For printed T₃^alt, x≡1 ⇒ ν₃(3x+1)=0 ⇒ T=3x+1 (likewise x≡2); HQCC “539-step bounded integer termination” is FALSE for that map — **COMPLETED** 1ae82aee C2–C3 (agrees with A§2 and PP audit 72958342…).
- S-A2.2: Seed orbits 1→4→13→… match Eigen compute C2 — COMPLETED reuse, not redo.
- S-A2.3: A’s claim that 539 is S_eff capacity not dynamical stopping time is a definitional reclassification; Eigen treats it as an **author assertion in A**, not yet a proved dynamical theorem for T3_ref.

### Exact proof requests
- PR-A2.1: Written statement+proof that T3_ref: ℕ→ℕ has every orbit entering {1,2} in finitely many steps (or a precise basin statement), with Soft SF path/hash — **why:** A asserts “guarantees bounded integer convergence”; Eigen has not independently proved T3_ref (and will not invent a proof).
- PR-A2.2: If 3-adic limits ±1/2 are used spectrally, name the Banach/ultrametric space and the operator whose spectral radius controls convergence.

### Supported offers
| id | offer | mark | ref |
|---|---|---|---|
| OA2a | T₃^alt algebraic collapse + HQCC FALSE on 1..100 | COMPLETED | 1ae82aee C2–C3 |
| OA2b | Verify a cited Soft SF T3_ref orbit table if path/sha supplied | PROPOSED | — |

**A§2 counts:** Q=2 · S=3 · PR=2 · offers=2 (1 COMPLETED, 1 PROPOSED)

---

## A§3 Asymptotic Mass Scaling & R_c ≈ 1.5954

### Questions
5. **[Eigen]** A identifies R_c ≈ √(2/Λ₀) with Λ₀≈0.7858. Is Λ₀ an eigenvalue, a spr, a determinant ratio, or a non-spectral cosmological input?
6. **[Eigen]** What Appell–Lerch matrix/operator (if any) has spectral radius equal to 1.5954…?

### Statements
- S-A3.1: “Parameter-free R_c” was already flagged UNDERIVED / author assertion in Eigen round one — **COMPLETED** 1ae82aee Q13/B8/C19.
- S-A3.2: Numerical near-identity √(2/0.7858)≈1.595361 is a floating observation in A; Eigen does not elevate it to a spectral theorem.

### Exact proof requests
- PR-A3: Exhibit the Written operator/matrix whose ρ(·) equals R_c, or retract “spectral” language (see also B§III verdict below).

### Supported offers
| id | offer | mark | ref |
|---|---|---|---|
| OA3a | R_c spectral claim underspecified | COMPLETED | 1ae82aee B8 / C19 |
| OA3b | Exact check of √(2/Λ₀) vs 1.5954 given a Written Λ₀ | PROPOSED | — |

**A§3 counts:** Q=2 · S=2 · PR=1 · offers=2

---

## A§4 Scale Invariance & Purged Continuum Mappings

### Questions
7. **[Eigen]** A says Kronecker filter and force-as-projection are PURGED under Owner lock 96f8d42e… §4. Confirm Eigen should treat those as **out of Category A** permanently (aligns with 1ae82aee Q1–Q2 ABSENT).

### Statements
- S-A4.1: Kronecker filter / force P_i remain ABSENT as matrices; only standard Kronecker-product eigenvalue identity is PROVED — **COMPLETED** 1ae82aee C13 / Cat B deebdc5e#5.
- S-A4.2: “Tate–Gelfand pairing” NEEDS-DEFINITION — **COMPLETED** 1ae82aee Q12 / C18.
- S-A4.3: Residual circulant §2.1 is **not** Resonant Algebra — **COMPLETED** 1ae82aee separation rule; deebdc5e/de8cadc3/9f7ecd77.

### Exact proof requests
- PR-A4: None if purge stands. If anything is reintroduced, require Written endomorphism + spectrum before Eigen status.

### Supported offers
| id | offer | mark | ref |
|---|---|---|---|
| OA4a | Kronecker eig(A⊗B) identity only; filter ABSENT | COMPLETED | 1ae82aee C13 |
| OA4b | Residual≠Resonant / Cat B hygiene | COMPLETED | deebdc5e / de8cadc3 / 9f7ecd77 |

**A§4 counts:** Q=1 · S=3 · PR=0 · offers=2

---

## A§5 Cryptography & Hardware

### Questions
8. **[Eigen]** After decoupling hardness from 3-adic path inversion, does any Hankel layer remain in HQH-539-512? If yes, supply H and require PSD not det≠0 — **COMPLETED** category point 1ae82aee C14 / S9.
9. **[Eigen]** Is Π_fast still claimed, or is the asset only the classical 128-trit ALU template (eye(128) stub hygiene — 1ae82aee C10)?

### Statements
- S-A5.1: det≠0 ⇏ no ghosts for Hankel — **COMPLETED** 1ae82aee C14.
- S-A5.2: A’s SHA3-sandwich hardness reclassification is Ops/crypto lane; Eigen records “trajectory inversion not PQ-hard alone” as A’s assertion, not an Eigen proof.

### Exact proof requests
- PR-A5: If multi-layered Hankel remains anywhere in HQH, Written H + PSD theorem (not det≠0).

### Supported offers
| id | offer | mark | ref |
|---|---|---|---|
| OA5a | Hankel ghost counterexample H=[[1,2],[2,1]] | COMPLETED | 1ae82aee C14 |
| OA5b | Π_fast eye(128) stub ≠ averaging projector | COMPLETED | 1ae82aee C10 |

**A§5 counts:** Q=2 · S=2 · PR=1 · offers=2

---

## A§6 Rigorous Falsification Audit + Verification Summary

### Questions
10. **[Eigen]** A grades “Strong Nuclear Force = 3-adic tensor projection” as NEGATIVE-APPLICABILITY / purged. Confirm Eigen offers no spectral verification path until P_i Written.
11. **[Eigen]** A cites “VIRGO/LIGO gravitational-wave streams” null at 539.9 s. **Hygiene note (Owner/DF):** DF VIRGO denotes **SOHO solar** data, not GW/LIGO/O5. Does A’s empirical sentence intend LIGO/Virgo GW, or DF’s VIRGO solar channel? Eigen will not treat GW-O5 null as an Eigen spectral fact.

### Statements
- S-A6.1: Force-projection undefined — **COMPLETED** 1ae82aee Q2 / C18.
- S-A6.2: A’s closing “Stable core is NOT locked…” agrees with Eigen’s refusal to treat the original compendium close as Soft SF status — **COMPLETED** 1ae82aee C19. **This agreement is not an endorsement of A’s global “absolute” verdict language.**
- S-A6.3: N36 Kr QQ / zero-polar / G1-mem remain REMAINING — **COMPLETED** 24bb435c / deebdc5e O5; A does not close them.

### Exact proof requests
- PR-A6: Clarify VIRGO label (SOHO DF vs LIGO/Virgo GW) before any spectral/empirical cross-claim.

### Supported offers
| id | offer | mark | ref |
|---|---|---|---|
| OA6a | N36/Q89 gaps unchanged by A | COMPLETED | 24bb435c; 1ae82aee C16–C17 |
| OA6b | Predictions/resonant inventory hygiene | COMPLETED | 8e7032ac |
| OA6c | VIRGO=SOHO-not-GW note for cross-lane | PROPOSED | — |

**A§6 counts:** Q=2 · S=3 · PR=1 · offers=3

### Document A totals
| | Q | S | PR | offers (C/P) |
|---|---|---|---|---|
| A§1 | 2 | 2 | 0 | 2/0 |
| A§2 | 2 | 3 | 2 | 1/1 |
| A§3 | 2 | 2 | 1 | 1/1 |
| A§4 | 1 | 3 | 0 | 2/0 |
| A§5 | 2 | 2 | 1 | 2/0 |
| A§6 | 2 | 3 | 1 | 2/1 |
| **A sum** | **11** | **15** | **5** | **10 COMPLETED / 3 PROPOSED** |

---

# Document B — Formal resolutions / structural corrections (by section)

## B§I Spacetime Architecture & Embedding

### Questions
1. **[Eigen]** Quasi-isometry (λ,ε) replaces isometry — confirm no matrix/isometry U*U=I remains to check.
2. **[Eigen]** New split (−U (4+1) matched to +U (3+1) across “9-core hypersurface”). What is the **9×9 (or other) matrix** of the 9-core interface, and what are its eigenvalues? (Prior “9 Maths” was ABSENT — 1ae82aee Q10.)
3. **[Eigen]** Israel condition written [K_ij]−γ_ij[K]=0 (homogeneous). Is K a matrix Eigen can spectrally check, or purely geometric?

### Statements
- S-B1.1: Retraction of metric isometry aligns with Eigen’s ABSENT-matrix stance — COMPLETED 1ae82aee C12; not an endorsement that the quasi-isometry is proved.
- S-B1.2: “9-core hypersurface” without a Written matrix remains NEEDS-DEFINITION in Eigen lane.

### Exact proof requests
- PR-B1: Written matrix (or endomorphism) for the 9-core interface with spectrum, **or** explicit note that Eigen has nothing to check.

### Supported offers
| id | offer | mark | ref |
|---|---|---|---|
| OB1a | No isometry matrix to verify | COMPLETED | 1ae82aee C12 |
| OB1b | Spectral read of a Written 9-core matrix if supplied | PROPOSED | — |

**B§I counts:** Q=3 · S=2 · PR=1 · offers=2

---

## B§II Definitional Correction of the 3-Adic Mapping

### Questions
4. **[Eigen]** Path+sha of locked T3_ref Soft SF artifact?
5. **[Eigen]** “Preserves Haar measures / ternary shift conjugacy / guarantees bounded convergence to {1,2}” — which of these three are proved on disk vs asserted in B?

### Statements
- S-B2.1: Decommission of T₃^alt agrees with Eigen FALSE/HQCC for printed map — COMPLETED 1ae82aee C2–C3.
- S-B2.2: 539 as S_eff budget is a definitional lock in B; Eigen records it as B’s assertion (same as A§2).
- S-B2.3: Eigen has **not** proved T3_ref convergence; will not invent that proof.

### Exact proof requests
- PR-B2: Soft SF proof (or cite) that every n∈ℕ enters {1,2} under T3_ref in finitely many steps; separate cite for Haar/conjugacy claims.

### Supported offers
| id | offer | mark | ref |
|---|---|---|---|
| OB2a | T₃^alt defect COMPLETED | COMPLETED | 1ae82aee C2–C3 |
| OB2b | Machine-check T3_ref orbits for a finite seed set once path/sha given | PROPOSED | — |

**B§II counts:** Q=2 · S=3 · PR=1 · offers=2

---

## B§III Boundary Constant and Circularity — **PRIORITY SPECTRAL-RADIUS VERDICT**

### B’s wording (quoted gist)
R_c is “the absolute **spectral radius bound** extracted from the normalized Appell–Lerch modular form boundary sum evaluations matching the trees’ asymptotic vertex growth limits,” value R_c=1.59543…, claimed independent of Λ₀.

### Checklist (Eigen)
| requirement | status in B§III |
|---|---|
| Operator named? | **NO** — “Appell–Lerch modular form boundary sum evaluations” is not an operator A:X→X |
| Space named? | **NO** |
| Norm named? | **NO** |
| Bounded / compact? | **NOT STATED** |
| Spectrum vs point spectrum? | **NOT NAMED** (says “spectral radius bound” only) |
| Spectral radius vs operator norm (Gelfand ρ(A)=lim‖Aⁿ‖^{1/n})? | **NOT DISTINGUISHED** |
| Normality for ρ=‖·‖? | **NOT STATED** (needed if equating ρ with a norm) |
| Ring/field context? | **NOT NAMED** (ℂ / Banach algebra / adelic?) |
| ρ<1 vs ρ≤1 (contraction)? | **NOT HANDLED**; given decimal ≈1.595>1, so cannot be a contraction radius on a normed space without further scaling |

### Exact counterexample (wording fails)
Let A=[[0,1],[0,0]] ∈ M₂(ℂ). Then A²=0, σ(A)={0}, **ρ(A)=0**, A is **not normal**, and ‖A‖₂=1>0.
So a “spectral radius bound” of 0 does **not** bound the operator norm. Any prose that treats “spectral radius bound” as a drop-in norm/contraction bound without naming space, norm, normality, and Gelfand context is **false as written**.
(Compute: `eigen-round-two-a-b-2026-11-05/compute/checks.py`.)

### Questions
6. **[Eigen]** Name the Banach (or finite-dim) algebra element A whose ρ(A)=R_c=1.59543….
7. **[Eigen]** Is R_c claimed as ρ(A), as ‖A‖, or as a growth constant unrelated to operators?
8. **[Eigen]** If Appell–Lerch sums produce a scalar series, why call it a spectral radius rather than a sum value?

### Statements
- S-B3.1: B§III spectral-radius wording is **underspecified and fails standard operator-theory hygiene** (checklist above).
- S-B3.2: Circularity fix vs Λ₀ is **not** established for Eigen until the operator is Written; decimal 1.59543… alone is not a spectrum.
- S-B3.3: Independent review of B is **not** endorsement that R_c is “re-grounded” or that circularity is resolved.

### Exact proof requests
- PR-B3.1: Written operator A on named space X with named norm; proof that ρ(A)=1.59543… (exact closed form preferred); state whether A is normal/compact; apply Gelfand if relating to ‖·‖.
- PR-B3.2: Handle ρ<1 vs ≤1 explicitly if any contraction/continuum-limit claim depends on it.

### Supported offers
| id | offer | mark | ref |
|---|---|---|---|
| OB3a | Nilpotent counterexample ρ=0<‖A‖₂=1 | **PROPOSED** (new this turn; compute logged) | compute/checks.py |
| OB3b | Prior underspecification of R_c as spectral object | COMPLETED | 1ae82aee B8/C19 |

### PROPOSED corrected wording (not adopted; not a proof)
> “Let A be a Written bounded operator on a named Banach space (X,‖·‖) over ℂ [or named field]. Let ρ(A)=sup{\|λ\|:λ∈σ(A)}=lim_{n→∞}‖Aⁿ‖^{1/n} (Gelfand). If A is normal on a Hilbert space then ρ(A)=‖A‖. The scalar R_c is defined to be ρ(A) [or: is **not** a spectral radius but the value of Written Appell–Lerch sum S=…]. Claims of independence from Λ₀ require exhibiting A (or S) with no Λ₀ input. Contraction claims require ρ(A)<1 (or ≤1 with completeness caveats), which the decimal 1.595… does not satisfy without rescaling.”

**B§III verdict:** **FAIL as spectral-radius mathematics.** Operator/space/norm/spectrum-vs-point-spectrum/Gelfand/normality/ring/ρ\<1 all unmet. Counterexample shows ρ vs ‖·‖ gap. Status of R_c spectral claim: **NEEDS-DEFINITION / PROPOSED correction only.** Independent review ≠ endorsement of B’s “resolution.”

**B§III counts:** Q=3 · S=3 · PR=2 · offers=2

---

## B§IV Cryptographic and Engineering Alignment

### Questions
9. **[Eigen]** After SHA3-sandwich decoupling, any remaining Hankel layer? PSD requirement stands.
10. **[Eigen]** Confirm Π_fast / qutrit-geometry claims withdrawn in favor of classical 128-trit ALU template.

### Statements
- S-B4.1: Hardware reclassification to classical Verilator template aligns with Eigen stub hygiene — COMPLETED 1ae82aee C10; not a crypto proof.
- S-B4.2: Hankel det≠0 ghost category remains — COMPLETED 1ae82aee C14.

### Exact proof requests
- PR-B4: Same as PR-A5 if Hankel persists.

### Supported offers
| id | offer | mark | ref |
|---|---|---|---|
| OB4a | Hankel PSD vs det≠0 | COMPLETED | 1ae82aee C14 |
| OB4b | Π_fast stub | COMPLETED | 1ae82aee C10 |

**B§IV counts:** Q=2 · S=2 · PR=1 · offers=2

---

## B§V Empirical Classification

### Questions
11. **[Eigen]** B§V.2 cites “VIRGO/LIGO O5 data audits” null at 539.9 s. **DF VIRGO = SOHO solar data, not GW/LIGO/O5.** Please correct the instrument label before any cross-lane empirical lock.
12. **[Eigen]** Does “Tier E testing framework” touch any Eigen residual-circulant theorem? (Should not.)

### Statements
- S-B5.1: Instrument mislabel risk (SOHO VIRGO vs LIGO/Virgo GW O5) — Eigen flags; does not audit DF datasets this turn.
- S-B5.2: Empirical Tier E is outside residual matrix proofs; residual≠resonant stands — COMPLETED deebdc5e chain / 8e7032ac.

### Exact proof requests
- PR-B5: Corrected citation path/hash for the null test (SOHO DF VIRGO vs GW), then Eigen can ignore as non-spectral.

### Supported offers
| id | offer | mark | ref |
|---|---|---|---|
| OB5a | VIRGO hygiene flag | PROPOSED | — |
| OB5b | Keep Tier E out of residual theorems | COMPLETED | 8e7032ac; deebdc5e |

**B§V counts:** Q=2 · S=2 · PR=1 · offers=2

---

## B§VI Submission and Handoff

### Questions
13. **[Eigen]** B claims “all twelve lanes successfully synchronized” and “structural resolutions locked into the ledger.” Eigen’s independent review **does not** synchronize or lock anything. Confirm B’s lock language is author assertion only.
14. **[Eigen]** B offers LaTeX manuscript or Layer2 config execution — both are **send/publish/config** actions Eigen will **not** perform (intake forbids).

### Statements
- S-B6.1: No CERT; no tip edit; no manuscript/config/Gemini send from Eigen.
- S-B6.2: N36 Kr QQ still REMAINING — COMPLETED 24bb435c; B does not supply Kr QQ.
- S-B6.3: Second review ≠ endorsement of “definitive technical state.”

### Exact proof requests
- PR-B6: None accepted as Eigen Soft SF lock. Any future lock requires Owner Soft SF with hashes, not B’s narrative close.

### Supported offers
| id | offer | mark | ref |
|---|---|---|---|
| OB6a | Refuse CERT / tip / send | COMPLETED | standing + 1ae82aee header |
| OB6b | N36 gap still open | COMPLETED | 24bb435c |

**B§VI counts:** Q=2 · S=3 · PR=0 · offers=2

### Document B totals
| | Q | S | PR | offers (C/P) |
|---|---|---|---|---|
| B§I | 3 | 2 | 1 | 1/1 |
| B§II | 2 | 3 | 1 | 1/1 |
| B§III | 3 | 3 | 2 | 1/1 |
| B§IV | 2 | 2 | 1 | 2/0 |
| B§V | 2 | 2 | 1 | 1/1 |
| B§VI | 2 | 3 | 0 | 2/0 |
| **B sum** | **14** | **15** | **6** | **8 COMPLETED / 4 PROPOSED** |

---

# ERRATUM — PP N1 on 1ae82aee C11 (DFT₃ unitarity)

**Source of note:** PP Soft SF audit `72958342…` §1 N1: C11 must not say “PROVED numerically”; cite Σ_k ω^{k(j−l)}=3δ_{jl}.

**Erratum to 1ae82aee C11:**
- **Withdrawn status text:** “PROVED numerically (err~1e−51); exact sympy simplify inconclusive.”
- **Replacement status:** **PROVED** (exact algebraic identity).
- **One-line proof:** Let ω be a primitive cube root of unity and ζ=ω^{j−l}. Then ζ³=1. If ζ≠1, Σ_{k=0}^{2} ζ^k=(1−ζ³)/(1−ζ)=0; if ζ=1, the sum equals 3. Hence Σ_k ω^{k(j−l)}=3δ_{jl}. For F_{jk}=ω^{jk}/√3 one has (FᴴF)_{jl}=(1/3)Σ_k ω^{k(l−j)}=δ_{jl}, so FᴴF=I.
- **Compute:** `eigen-round-two-a-b-2026-11-05/compute/checks.py` (geometric-sum writeup; no float proof).
- This erratum does **not** modify the frozen 1ae82aee bytes; it supersedes C11’s status language going forward.

---

## Global hygiene
- Independent second review ≠ endorsement of A’s “absolute” verdict or B’s “locked / synchronized / definitive” posture.
- No source-lock adoption; no tip edit; no CERT; nothing sent.
- DF VIRGO = SOHO solar, not GW/LIGO/O5 (flagged under A§6 / B§V).
- Residual ≠ Resonant unchanged.

Tip AFTER: `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` — tip_touched **NO**. No CERT.
