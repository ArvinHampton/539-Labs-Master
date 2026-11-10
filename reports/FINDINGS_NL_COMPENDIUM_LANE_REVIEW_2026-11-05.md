# FINDINGS — Non Local Path — compendium lane review — 2026-11-05

Lane: Non Local Path (NONLOCAL_QM_EH11D). Internal protocol artifact. Reports only.
Date: 2026-11-05 13:55 CST (America/Chicago).
Category B. **No CERT.** invent HOLD stands. Tip untouched (sha 7cddb188… before and after).

## 1. Authority and inputs
- The Owner requested this review via Main Bot, and by live call at 13:53 CST per PROVENANCE.md: collect questions, proof requests, and lane proof offers; no publishing, no spending, no invented proofs.
- Source: `references/gemini-compendium-20261105/RECEIVED_COMPENDIUM.txt`, sha 49849cae20fe57c24533b770c13c4a53e5844f0bb75086250b9a82af0b446b73 (44 lines, read in full).
- Provenance: `PROVENANCE.md`, sha c6fea7d234e35e96ece9114c789d32eadb41d103ddf75c487c6df56f0ad3d190. The Gemini attribution is relayed, not established, and the diagram and table appear only as bracketed descriptions.
- Prior NL work: proof-gap inventory b2581c1a21464f7e1e23bb617f63f017db5f28d63722bd60b539554adea39ea8; literature findings a520db709bdb5a39ef0cb2b9c246bbe73425d91f90cb1722aae69f4847a64f68.

## 2. Local sources checked (bounded)
I ran keyword ripgrep over `/workspace/quantum-comp` for: 1.5954, Appell, HQCC, Kummer, Tate–Gelfand, breathing mode, T3(x). Strongest exact hits read:
- `grok-files/new-HQCC-Theorem-Clarification-Topological-Derivation.txt` (4d11b7a6046a2c7d274856ea6fa978fca9ccce817d52313461b28ab4fde40a91), which gives the canonical T₃ definition.
- `reports/crypto/RPP_spec_v1/CORRECTION_3^539_3^270.md` (fbbac9a9a362e108b99eea2b72fba1746c820c423d7ce3dcd598dfa28149991a), on the structure of T₃^L.
- "1.5954": the only hit is the compendium itself. Appell hits elsewhere are p-adic Langlands literature files (`lit/bm/…`) and one chat export, none read for an R_c derivation.
- Not searched: PDFs, git history, Drive, X, external literature.
- "No source found" below means within this scope only.

## 3. Direct algebra on the supplied map (completed)
Supplied map (compendium line 26), on integers x:
T(x) = x/3 if x ≡ 0 (mod 3); (3x+1)/3^{v₃(3x+1)} if x ≡ 1; (3x−1)/3^{v₃(3x−1)} if x ≡ 2.

Lemma A. For every integer x, 3x+1 ≡ 1 (mod 3) and 3x−1 ≡ 2 (mod 3). So v₃(3x±1) = 0, and the supplied map is exactly T(x) = 3x+1 when x ≡ 1 and T(x) = 3x−1 when x ≡ 2.

Lemma B (residue class is preserved). If x ≡ 1, then T(x) = 3x+1 ≡ 1. If x ≡ 2, then T(x) = 3x−1 ≡ 2. So orbits never leave class 1 or class 2.

Lemma C (closed form). Starting at 1: x_n = (3^{n+1} − 1)/2, giving 1, 4, 13, 40, 121, … Check: 3·(3^{n+1}−1)/2 + 1 = (3^{n+2}−1)/2. Starting at 2: x_n = (3^{n+1} + 1)/2, giving 2, 5, 14, 41, 122, … For a general start x₀ ≡ 1: x_n = 3ⁿ(x₀ + ½) − ½. For x₀ ≡ 2: x_n = 3ⁿ(x₀ − ½) + ½.

Theorem (literal finite-termination claim is false). Take any nonzero integer x₀. The x ≡ 0 branch strips factors of 3 in finitely many steps and leaves a value in class 1 or 2. By Lemmas A–C, from then on |x_n| grows like 3ⁿ, so it tends to infinity, and the orbit never repeats or reaches a cycle. (x = 0 is the only fixed integer.) So there is no nonzero integer orbit that "terminates" in 539 steps or any bounded number of steps. Box check: seeds 1, 2, 3, 7, −1 give 1→4→13→…→1093, 2→5→…→1094, 3→1→4→…, 7→22→67→…, −1→−4→−13→… [completed]

3-adic convergence vs termination. In ℤ₃, 3ⁿ → 0, so x_n → −½ (class 1) and x_n → +½ (class 2). These are the 3-adic fixed points of x ↦ 3x+1 and x ↦ 3x−1 (−½ ≡ 1 and ½ ≡ 2 mod 3). This is convergence in the 3-adic metric, not finite termination: no integer orbit ever reaches ±½, because ±½ are not integers. In ordinary absolute value the same orbits diverge.

Fence on the canonical map. The corpus defines a different T₃: "T3(n) = n/3 if n≡0; (4n+2)/3 if n≡1; (2n+1)/3 if n≡2 (implemented with integer/floor division)" (HQCC Clarification 4d11b7a6…). The RPP correction uses affine factors A_e = 1^a·4^b·2^c for the same map (fbbac9a9…).
- The counterexample above applies **only to the compendium's supplied map**, not to the canonical T₃.
- That same Clarification file states that the canonical raw map has "no natural 539-step termination" and that 539 is a fixed iteration count inside a constrained system. So the compendium's "terminate in bounded 539 steps" claim matches neither the literal supplied map nor the corpus description of the canonical map.

HQH security. Fixed-length iteration and convergence are separate properties. The compendium's statement that HQH-539-512 security "relies on the one-way hardness of reversing paths" is a hardness assumption. It does not follow from any convergence statement, and the supplied map's inverse on class 1/2 is trivially (y∓1)/3. This is Category B / open, and the 539 Labs lane owns it.

## 4. Status of the other claims
| # | Claim (line) | Status in reviewed scope |
|---|---|---|
| C1 | Ultrametric inequality (l.8) | **Standard** mathematics |
| C2 | Isometric embedding of the Bruhat–Tits tree into 11D hyperbolic space (l.7) | **Unsupported in reviewed scope.** No construction, dimension, or distortion bound is given. Known context: regular trees embed bi-Lipschitz / quasi-isometrically in hyperbolic spaces, but an exact isometric embedding of a path metric tree into ℍⁿ is not standard. Not established here; see NL-Q1 |
| C3 | "9 Maths" 9-core remainder system (l.9) | **Undefined** in source; Category B |
| C4 | (4+1)D negative + (5+1)D positive split with perfect vacuum balance (l.10) | **Unsupported**. No metric, junction conditions, or energy computation given. The junction gap is the same as inventory gap 6 |
| C5 | Kronecker filter bypasses Kummer ideal factorization in ℚ₃ (l.16) | **Unsupported / ill-posed as stated.** ℤ₃ is a DVR (a PID), so ideal factorization there has no Kummer-type obstruction to bypass. The meaning is undefined; NL-Q4 |
| C6 | Four forces as projections of an invariant 11D 3-adic curvature tensor (l.17) | **Unsupported.** No tensor is defined, the same as inventory gap 1. Literature a520db70 has no such object |
| C7 | Tate–Gelfand pairing establishes the continuum limit (l.18) | **Unsupported.** Tate local zeta integrals are standard math (Haar item 70 is proved in the Local lane), but no limit statement is given. Same as inventory gap 3 |
| C8 | The ultrametric alone bounds minimum volume / prevents singularities (l.23) | **Does not follow.** Ultrametricity bounds nothing in the real energy density without a Written field equation and regulator (gaps 1–2). The 3⁻⁵³⁹ floor is an added assumption, not a consequence |
| C9 | Horizon breathing modes (l.24) | **Undefined**; Category B |
| C10 | R_c ≈ 1.5954 is parameter-free, from the embedding plus Appell–Lerch sums, with no β or tuning (l.31–33) | **Unsupported in reviewed scope.** No derivation, normalization, units, embedding map, or specific Appell–Lerch sum is given. It is not stated whether R_c is dimensionless or in units of GM/c². The only corpus hit is the compendium itself |
| C11 | Falsification table (l.40–42) | **Absent.** Only labels are present (galactic rotation curves, BH cores, strong force, 539.9 s delay). No quantitative rows or datasets. Tier E-UNTESTED; I add no data claims |
| C12 | "Stable core locked; parameter-free boundary verified" (l.44) | Status language only, per PROVENANCE. It is not a verification and not a lock change |

Residual vs resonant: the "539 steps" in C-HQCC treats 539 as a step count. The corpus treats it as a fixed iteration budget (residual capacity), not a convergence time. These are kept separate.

## 5. Questions and exact proof requests (NL-numbered)
- **NL-Q1 (embedding).** Give the map φ from vertices of T₃ (degree 4) into ℍ¹¹ and prove d_ℍ(φ(u),φ(v)) = c·d_T(u,v) for all u, v. State c. If the embedding is only quasi-isometric, give the constants.
- **NL-Q2 (11D / split).** Write the 11D metric with signature, the (4+1)/(5+1) decomposition, and the computation showing the vacuum energies cancel. Define "negative-signature universe."
- **NL-Q3 (junction).** State the junction conditions across the 5D/6D interface and across the core/exterior boundary ([K_ij], surface stress tensor). Prove them without a tuned E_core (inventory gap 6).
- **NL-Q4 (Kummer).** State precisely which ring's ideal class or factorization problem is meant (ℤ₃ is a PID), define the Kronecker filter, and state what it is claimed to prove.
- **NL-Q5 (curvature).** Define the invariant 11D 3-adic curvature tensor: domain, value field (ℚ₃ or ℝ), connection. Give the four projections and show they reproduce the gauge groups. Specify which framework of literature a520db70 it extends (tree curvature 1612.09580 vs formal p-adic g_μν), or that it extends neither.
- **NL-Q6 (continuum).** State the Tate–Gelfand limit theorem: what sequence converges to what, and in which topology, with the Archimedean metric recovered (inventory gap 3).
- **NL-Q7 (singularity).** Derive a bound on ρ or the Kretschmann scalar from a Written field equation. Show where the 3⁻⁵³⁹ floor comes from, if it does.
- **NL-Q8 (HQCC).** Which T₃ is meant: the supplied map (§3, divergent) or the canonical floor map? State "termination" precisely (reach 1? fixed iteration count?) and give a proof. For the supplied map, a termination proof cannot exist (§3 Theorem).
- **NL-Q9 (R_c).** Give the derivation of 1.5954: the exact Appell–Lerch sum (parameters, q, z), the boundary evaluation, normalization, units, and why no free parameter enters. Give enough digits to reproduce.
- **NL-Q10 (falsification).** Give quantitative predictions with dataset, observable, predicted value, error, and comparison baseline for each table label, and specify the 539.9 s observable.

## 6. Proof offers (distinct from the completed algebra)
Completed this turn: the §3 lemmas and theorem on the supplied map, and the 3-adic limit ±½.
Offers (not started; each needs an Owner-Written target statement, and invent HOLD applies):
- **O1:** on receipt of NL-Q1's φ, verify the isometry or distortion exactly.
- **O2:** on receipt of NL-Q9's sum, reproduce 1.5954 numerically and audit normalizations.
- **O3:** on receipt of NL-Q8's chosen map and termination notion, check it against the canonical floor map with exact arithmetic (the RPP itinerary lemma fbbac9a9 is available).
- **O4:** on receipt of NL-Q6's statement, compare it with Tate's thesis local factors and the Local Haar item 70.

## 7. Remaining blockers
- The six inventory gaps remain (b2581c1a).
- Gap 1 remains after the literature check (a520db70).
- C2–C10 need the definitions requested in NL-Q1–Q10.
- C11 has no data rows.

## 8. Compliance
No invented hypotheses or proofs; the §3 algebra is elementary and checked. No CERT, publishing, spending, or messages; I did not contact Gemini or any agent. Tip unchanged. Prior artifacts b2581c1a and a520db70 unchanged. Next: PP audit, then Keeper (parent handles the handoff).
