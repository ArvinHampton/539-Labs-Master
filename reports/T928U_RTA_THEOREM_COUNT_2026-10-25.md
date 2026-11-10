# T928U — Theorems established with Residual Ternary Algebra (RTA)
Date: 2026-10-25, ~5:00 PM CDT (America/Chicago). Invent-ban: labels/status quoted from artifacts only.

## Sources read
| Source | Path / DOI | sha256 |
|---|---|---|
| Zenodo 23644022 "Residual Ternary Algebra and a modular foundation" (v12, pub 2026-10-25) | fetched via zenodo API -> /workspace/quantum-comp/reports/self-audit/zenodo/RTA_FOUNDATION_BOUND_v12.pdf | d2fda41b513f16e37d6088019ab8aadae03c9a692782e298734378659fd95653 |
| Zenodo 22143607 main draft | reports/self-audit/zenodo/22143607_Final_draft-_5th_Order_Unification_and_Residual_Ternary_Algebra.pdf (+txt) | — |
| Zenodo 22143607 supplemental | reports/self-audit/zenodo/22143607_Final_Supplemental_...Residual_Ternary_Algebra.pdf (+txt) | — |
| 9-maths chain | /workspace/quantum-comp/maths/theorem-lemma-chain-9-maths.txt | 904104d26c0c029df9a9e39f7ef5235f4b3a2f7befb0349e7bdf0187a6df5a0a |
| RTA manuscript draft 2026-08-24, Hudson-Ware absorption, Exec summary 2026-09-16, IACR ePrint HQH-539-512 | reports/self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/ ; reports/crypto/PRESENTATION_SUPPORT/.../IACR_ePrint_HQH539512_Residual_Ternary_Algebra_2026-09-07.txt | — |
| Bridge C consolidated rev2–rev9.2, Clean, Clean-v2 | /tmp/sw2/*.pdf.txt | — |
| A53 RTA maps | /tmp/repo539/reports/s_family_paths/A53_RTA_maps/REPORT.md, prereg.md | — |

## ABSENT / negative results
- **Residual_Contacts: ABSENT.** No file with that name anywhere on the box. It is only *referenced* in 22143607 main draft ("document Theorem_Lemma_Chain_9_Maths_Residual_Contacts").
- theorem-lemma-chain-9-maths.txt: **0 occurrences of "ternary"/RTA**. Its Theorem 1, Final Closure Theorem and pillar theorems are not stated with RTA → not counted.
- RTA manuscript draft 2026-08-24: Propositions only, no Theorem labels.
- Hudson-Ware absorption note: no theorem; says "Classical Twin Prime Conjecture and classical Riemann Hypothesis remain open and unclaimed."
- A53 REPORT/prereg: no theorem labels.
- Bridge C rev reports: carry earlier numbering of results later consolidated into 23644022 (e.g. rev9.2 "Theorem 11.3 (Tensor factorisation, s = 7)" = v12 Thm 19.3; "Theorem 13.16 (dim V(98))" = v12 Thm 20.5). Not counted separately (duplicates).
- IACR ePrint and Exec Summary: repeat 22143607 Theorem 8.4 → duplicate, not recounted.

## Count
**Total distinct established theorems: 64**
- (1) within RTA (about RTA objects T3/g_s/Bridge Series C/companions): **61** (60 from 23644022 + Thm 8.4 of 22143607)
- (2) RTA used as tool for another domain: **3** (23644022 Thms 26.7, 26.9 — K3 surfaces, framed by Cor. 26.6 "The residual law in K3 terms"; 22143607 supplemental "Theorem 1 (Minimal Unification Core – discrete half)"). The (1)/(2) split is my classification; the sources do not use it.
- Not counted: 18 Corollaries + many Propositions in 23644022; "Theorem 1.1" (external cited result); "Remark (Category B) 11.11" (open problem 1: "Prove the cusp-row identities of Theorem 11.11 (currently Category B)").
- 23644022 Part IV: "written RTA objects (T3, Ores, 539, the packaging identities) have no written link to it [the modular framework]"; shadow Ξ question "is open".

## 23644022 (DOI 10.5281/zenodo.23644022) — 62 theorems; convention: "Status (Category A)" unless noted
Part I (s-series g_k): 5.1; 5.3; 5.5 (zero classes for b∈{1,2}); 6.6; 6.9 (table: "algebraic + exact integer certificate for s ≤ 2500 + cited bound [20] for s ≥ 2501"); 7.4; 7.6; 7.7; 8.1 (parity dominance — "analytic reduction + finite computer-assisted verification"); 8.12 (result of Algorithm C); 8.22 (zero sets).
Part II (Bridge Series C): 11.1 Shared remainder; 11.2 Real-quadratic (ray-class) identification; 11.3 Radial asymptotics and partial zeta values; 11.4 Gauss-mean pattern and zero set; 11.5 Baker obstruction: scalar no-go ("(i) is proved conditional on Baker's theorem [1] and on the q-expansion principle"); 11.6 Theta lift and vector-valued S/T law; 11.7 Lewis–Zagier period formula; 11.8 Eisenstein/cusp split; 11.9 Herglotz closed form; 11.10 Closed form of E_R ("proof is given in outline ... No arithmetic proof of Theorem 11.10 is claimed"); 14.1 Profile S/T law; 15.3 Cocycle of the E-part; 19.3 Tensor factorisation s=7 ("conditional on the cited congruence..."); 19.5 Tensor factorisation for odd s; 20.1 Dimensions; 20.5 dim V(98)=2406; 20.11 Prime-square structure ("Conditional on (C3), which is cited and not re-proved"); 21.2 Coset property; 21.3 Squarefree criterion; 22.1 H_s in closed form; 22.5 Period 72 at x=1/3; 23.7 Closed forms for H_s^axes; 24.1 C_third: one coset, one cone weight, one P kernel, two chains; 24.4 Phase obstruction ("Unconditional"); 24.5 Sign obstruction ("Conditional on the cited analyticity of harmonic-Maass cocycles"); 24.6 Structure of C_third; 25.1 Rational ζ-curve; 25.2 Radial expansion of g_s; 26.2 Weil realisation of the label representation; **26.7 N2-polarised K3 surfaces** ("Category A (cited)") [type 2]; **26.9 Automorphisms of N2-polarised K3 surfaces** ("Category A (cited)") [type 2]; 27.4 Uniqueness of the Maass completion; 27.7 Uniqueness and residual ambiguity of the vector completion; 27.13 Dimension of the cusp space ("Category A (computer-assisted)").
Part III: 33.4 T-law and S-law; 34.5 Profile of C and of q^(-7/20)C; 34.6 Radial asymptotics at leading order; 34.7 Vector-valued S-law of C at leading order; 35.4 Expansion of a piece; 35.6 Radial expansion of the companion series; 37.10; 37.11; 37.13; 38.2; 38.4; 38.5; 39.2; 39.3; 39.4; 39.23 (unnamed).
Part IV: 40.3 The normalized Bridge Series and the 35-component law vector ("Proof. Theorems 34.5, 34.6, 34.7, 35.6, Corollary 35.8 and Proposition 35.10").
(Per-theorem status lines not shown above were not individually audited; the paper's convention is Category A = proved/exact/computer-assisted.)

## 22143607 (DOI 10.5281/zenodo.22143607)
- **Theorem 8.4 (Residual Fricke-type law for Bridge Series C)** — main draft §8; proof given; cocycle "vanishes to machine precision ... within truncation of the coefficient tables". Remark 8.5: "a residual discrete identity under packaging principle (S) at the four sample points ... Uniqueness of residual_slash off the four sample points, and full continuous Fricke verification away from the sample set, remain open." [type 1]
- **Theorem 1 (Minimal Unification Core – discrete half)** — supplemental; "These objects are Category A. They do not by themselves prove continuum physics." Accompanying Lemmas 1–7 state continuum parts are Category B. [type 2]
- All other numbered results there are Propositions (2.2–9.1), not theorems.

---
sha256 of this report body (all lines above this footer): 098997104a3b18d6da92b826df1cfd02d23030af2df4ef66a10ec7f0644141c1
