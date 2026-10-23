# DRAFT preregistration: can Bridge C (s = 7, exactly certified) constrain Residual Ternary Algebra (RTA)?

**Owner:** Arvin Hampton (539 Labs) · **Drafted:** 2026-10-22, evening, America/Chicago (CDT) · **Status:** DRAFT FOR REVIEW. Not frozen, not hashed, not run.
`SF/` = `/workspace/quantum-comp/reports/s_family_paths/`. New files only, all in `SF/A52_bridgeC_to_RTA_draft/`.

> **Nothing has been computed for this draft.** No test, rank, Gauss mean or coefficient was evaluated on RTA data. Every number below is quoted from an existing report, or is arithmetic done by hand and labelled "derived here, unchecked".
> **Residual-vs-Resonant lock stays in force.** RTA and Resonant Number Theory stay unmixed. A map below may relax the lock only for the exact map and statistic declared, and only after the pass criteria are met. The retired maps M1 to M3 (A42/A43) are not reused, and neither is their target set R.
> No TPC or RH claim. H_s is not redefined. Nothing is pushed or sent.

## 0. How to read this draft
- Categories: **Category A** = proved, or an exact certificate (exact arithmetic; a mod-p rank is used only as a one-sided bound). **Category B** = floating point, finite-range, or statistical.
- Naming: "Bridge C" is the s = 7 setting. "RTA's Bridge C series" is the series C := P_s − H_s of the RTA manuscript. "C-summand" is the 6-dimensional irreducible piece of rho_7|W. These are three different things.
- Always: "35-component law vector" is the object of Residual-Law B3. The number 36 appears only as dim V = dim E.

## 1. What RTA objects are (found by search; quoted, not re-derived)
Primary source: `oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/Residual_Ternary_Algebra_Full_Manuscript_Draft_2026-08-24.md` (byte-identical copy in `reports/heavy-daily/d7f018c50bd7-…`). Its RTA objects are:
1. The map T3 (Def 2.1), three branches by n mod 3; {1,2} is a 2-cycle. "Ternary" means this three-branch map. Ledger entry 47: itinerary residues give a bijection of Z/3^j with words over {0,1,2}.
2. Packaging arithmetic (sections 3 to 5): B' = 539, 539 = 3·68 + 5·67, 18 + 521 = 539, the linking series Lambda_B.
3. The residual series g_s(q) = Σ q^{n²}/(−q^s;q^s)_n (Def 6.1), and P_s = (−q^s;q^s)_∞ g_s = Σ_{n,k≥0} q^{n²+snk+(s/2)k(k+1)} (section 7, Def 9.1).
4. Bridge C series C := P_s − H_s (Def 9.1), with cones c1 = (−1,1), c2 = (−4,1), C_axis, chi_nat(s) = (s/(2(s−2)), −1/(s−2)), C_third, the shadow Xi (sections 9 to 11).
5. The one named open item: the exact weight-1/2 slash prefactor under the Fricke map W_7: x ↦ −1/(7x) ("residual_slash", `Residual_Fricke_Magnitude_Verification_Slash_C_2026-08-25.md`; four sample points x = 1/7, 3/7, 5/7, 1).
6. The "six rules" are process hygiene, not axioms.

**What is not there:** no operation of arity 3, no grading axiom, no Jacobi- or Filippov-type identity (A18 §1, confirmed by this search: `grep` for "Residual Ternary", RTA, ternary, residual_slash, g_s over the workspace). The corpus itself notes that the bare token "RTA" is not used as an abbreviation (2026-10-19 Implications note). So RTA currently has objects and one open obstruction, but no axioms for a Bridge C structure to satisfy or violate.

Facts about the ternary-valued data that actually exist in the corpus (none is tied to E/C):
1. The residues r_s(n) in {0,1,2} of T3 itineraries (3-adic).
2. sgn g_s(d) in {−1,0,+1}. Proved: for odd k, (−1)^m φ_n(m) ≥ 0, and for k = 3..25 the eventual sign on allowed d is −(−1)^d (A39, A40, A41, A44). These data are already seen.
3. The Legendre symbol: G(h/7) = (h/7)·i/√7 (Residual-Law A2, Lemma 3). It exists because Q_s ≡ n² mod s, so every object built on Q_s shares it.
4. The coefficients of the Bridge C series are not ternary: the value set is {0, 1, 3/2} only through degree 101; the first coefficient 2 is at q^102 (Residual-Law A1).

## 2. What Bridge C exactly gives (precise statement)
Setting (ledger v6 entries 32 to 42; A51). A = [[2,7],[7,7]], Q(ν) = ½νᵀAν, B(ν,β) = νᵀAβ, D = A^{-1}Z²/Z² of order 35, level 70, a = (7/10, −1/5) = chi_nat(7). Gauss means G_{α,β}(x) = mean over ν in α+Z² of e(xQ(ν) + B(ν,β)).

Proved (Category A):
1. **S-law and T-law** (entry 39): G_{α,β}(−1/x) = (1/(|x|√35))·e(B(α,β))·Σ_{p in D} G_{β+p,−α}(x), and G_{α,β}(x+1) = e(−Q(α) − B(α,h_A))·G_{α,β+α+h_A}(x). Closed forms M_S, M_T over Q(ζ_9800) with M_S⁴ = I and (M_S M_T)³ = M_S² (A51 §2).
2. **The module V**: the span of the components of the 35-component law vector candidates K2, K3, K4 (K1 ≡ 0, entry 42). dim V = dim E = 36 (rank equal to dim V at all four primes on 216 rationals, plus the orbit upper bound; A51 §1). V is closed under S (weight |x|^{-1}) and T.
3. **V ≅ E untwisted**, End(V) = 1, and Hom(V⊗χ^k, C) = Hom(C, V⊗χ^k) = 0 for every k in Z/12 (entry 41, A51 §3).
4. **E/C split**: rho_7|W = E + C, both irreducible, not isomorphic; the C-summand has dimension 6, dim C⁺ = dim C⁻ = 3, and C ≅ rho_5⁻ ⊗ rho_7⁻ ⊗ χ³ (entries 32, 36). The 35-component law vector has zero rho_5⁻ ⊗ rho_7⁻ part (entry 38).
5. **T-spectrum**: spec(T|C) = {19, 31, 59, 111, 131, 139}/140, and it is contained in spec(T|E); T|E has dim E distinct eigenvalues. So T alone cannot separate C from E (A51 §4).
6. **Z/3 grading**: R = ST, eigenvalues 1, ω, ω², balanced on E and on C (A15, A16, A18). It also holds on E at all 16 tested s, so it is generic (A18 §2b).

Derived here from the entries above (checkable by hand, **not machine-checked in this draft**):
7. **RTA's series sees the characteristic a.** Since Aa = (0, 7/2), Q_s(n,k) = Q(ν) + B(ν,a) = Q(ν+a) − Q(a), with Q(a) = −7/20 = −c0 (c0 = s/(4(s−2))). So the leading coefficient of RTA's series at rational x is I·G(x) with G(x) = e(−xQ(a))·G_{a,0}(x), a coordinate of the K2-type family. (I = log(6+√35)/(2√35); Residual-Law A2.)
8. **Cyclic vector.** V is irreducible and the coordinate in item 7 is non-zero, so the smallest S,T-closed family of leading profiles containing RTA's profile is all of V (dim V functions). RTA's Bridge C series is not modular (Baker obstruction, Residual-Law A3), but its leading profile is a cyclic vector of an irreducible module that is isomorphic to E.
9. **Origin of the Z/3.** From the S-law and the T-law, S swaps the K2-type and K3-type families and fixes K4-type; T swaps K3-type and K4-type and fixes K2-type. So SL2(Z) acts on the three blocks through SL2(Z/2) ≅ S3, and R = ST permutes the blocks cyclically. The balance of R on V (three blocks of equal size) is then forced by the block structure. If correct, the Z/3 is the cyclic order of three characteristic classes (a mod-2 phenomenon, like the three even theta characteristics), not a 3-adic structure.
10. **Support of the leading profile.** The 1/t profile of the Bridge C series lives entirely in C_third. The axis part and C_mixed carry none (Residual-Law Lemmas 2 and 3: H_s, q^8 f and the axis series contribute 0/t).

Limits (Category A or open, as stated in the sources):
- Bridge C covers the leading 1/t profiles of cone sums only (A51 scope note). It says nothing about the t^{-1/2} terms, the coefficients of g_s, T3, or the packaging integers.
- The scalar W_7 slash is obstructed for every weight and every constant (Residual-Law A5): 178 of 270 rationals have exactly one of G(x), G(−1/(7x)) zero. This does not decide a vector-valued law, because V has 105 coordinates, not one.
- The Master sample magnitudes are not radial values of C (Residual-Law A2 item 5), so they are not data for any map below.

## 3. Lessons from A42, A43, A45, applied to this draft
1. **No empty or forced cells.** Anything forced by Q_s ≡ n² mod 7 (residue support {0,1,2,4}, the Legendre factor) is shared by every object built on Q_s, so it cannot support a link. No cell below uses it.
2. **Every premise carries a tag** (proved / assumed / derived-unchecked). A42's "one contributing n implies non-zero" was false (φ_2(2) = 0) and cost an amendment. Items 7, 9 of section 2 are derived-unchecked, and each map below says whether it depends on them.
3. **Attainable p.** The smallest attainable p-value is computed before any run, and must be below the per-test threshold, or the test is declared exact-only or evidence-only. In A43 only M1 cells could ever pass.
4. **No post-hoc coincidences.** E(36) = 2·18, 540 = 539 + 1, and similar are declared inadmissible (A42 §2.3).
5. **No target sets from packaging integers.** The set R of A42, ord_539(3) = 210 and the divisors of 539 are not used. The RTA manuscript says its s in {7, 8, 11} are "selected by packaging arithmetic" but gives no derivation; this draft does not use that selection as a target (see question 3).
6. **Fixed statistics and conventions before any look** (A43's Z* versus Z*lit ambiguity). Each map fixes its statistic, point set, primes and weight convention here.
7. **Range confounds** (A45 section 3, the k^{3.7} fit). Map 2 uses a fixed list of s and fixed certificates; no fit is used.
8. **Look-elsewhere is counted** (A45 section 4.6: 21 tests, Bonferroni 0.0024). The confirmatory family here has m = 1; Map 2 is a universal exact statement with no p-value.

## 4. Candidate maps
Both maps are exact and use only already-certified machinery (A51 methods, unchanged). Neither introduces a free parameter. They are new in the sense that neither statement appears in the ledger or in A32 to A51.

### Map 1 (sharpest): a vector-valued Fricke law for RTA's open slash obstruction
- **Bridge C structure used:** the S-law and the module V (items 1 to 3 of section 2).
- **RTA object:** the open weight-1/2 slash prefactor under W_7: x ↦ −1/(7x) for the Bridge C series (manuscript section 12).
- **Statement.** For f in V write (f|W_7)(x) := |7x|^{-1} f(−1/(7x)). Because V is S-closed with this weight (entry 40), f|W_7 = (f|S)∘D_7 with D_7 f(x) = f(7x), so V|W_7 ⊂ V if and only if V∘D_7 ⊂ V. The weight exponent 1 is the one found by Residual-Law A5 on the common support, so no weight is left free.
  - **H1:** for every one of the 105 component functions f of K2, K3, K4, the function x ↦ f(7x) lies in V. Equivalently, there is a constant 105-by-105 matrix N (not unique, since the 105 components span only dim V) with g(7x) = N·g(x) for all rational x.
- **New prediction.** The answer to this question is not in the ledger (V was closed only under S and T, A33/A35/A51) or in Residual-Law A5 (scalar only). If H1 holds, RTA's leading profile has an exact vector-valued Fricke law of weight 1, which is the first exact form of RTA's "residual law" at leading order. If H1 fails, no vector-valued form exists inside V.
- **Data used.** Exact Gauss means G_{α,β}(h/m) and G_{α,β}(7h/m) at the 216 rationals h/m of A51 (1 ≤ m ≤ 15, 1 ≤ h ≤ 3m, gcd = 1), at the four A51 primes p = 17 657 640 001, 21 189 168 001, 35 315 280 001, 42 378 336 001, with the same Lev = 3 531 528 000 (denominators of 7h/m divide m, so Lev suffices). No RTA coefficient data are used.
- **Statistic.** r_p = rank over F_p of the 216-by-210 matrix [F | F7], where F holds the 105 components at x and F7 holds the same 105 components at 7x. The reference rank of F alone is dim V (A51).
- **Falsification criterion (exact).** H1 is **refuted** if r_p > dim V at any one of the four primes. Reduction mod p can only lower rank, so r_p > dim V proves a component of V∘D_7 is not in V as a function on Q (Category A).
- **If not refuted** (r_p = dim V at all four primes): this is Category B evidence only. Promotion needs a closed-form N with exact verification, as in A51 section 2. That is a separate step, not part of this preregistration, and needs Arvin's approval.
- **Controls (fixed now).** The same test with D_7 replaced by D_p for every prime p ≤ 97 with p ≠ 7 (24 controls; p = 2 and 5 divide the level 70 and are kept as controls). Primary question: does closure hold at 7 and fail at all 24 controls?
- **Multiple testing.** One confirmatory test (m = 1), per-test α = 0.05. The specificity p-value is (1 + number of controls that close)/(1 + 24). The minimum attainable p is 1/25 = 0.04 < 0.05, reached only if closure holds at 7 and at none of the controls. Any control that closes raises p to at least 2/25 = 0.08 and the link claim fails. The decision rule is refute / not refute; the p-value only gates the claim of specificity.
- **Category:** a refutation is Category A. A confirmation is evidence until proved.
- **Feasibility:** reuses the A51 rank pipeline (FLINT nmod_mat, one thread). Matrices are 216 by 210, for 25 dilations in total (7 plus 24 controls) at 4 primes each; minutes, under 1 GB.
- **Outcomes.**
  1. Refuted at 7: negative. RTA has no leading-order vector Fricke law inside V; the lock stays; the branch is closed.
  2. Not refuted at 7 and refuted at all controls: candidate link, evidence only; proof step required before any relaxation of the lock.
  3. Not refuted at 7 and at some controls: generic closure (or an artifact), not an RTA link.
- **Drafter's prior (not an outcome):** closure is unlikely, because x ↦ 7x does not normalise SL2(Z) and the scalar pattern in Residual-Law A5 is wrong in 178 of 270 places. That scalar fact does not decide the vector question.

### Map 2: transport of the exact module to RTA's s-family
- **Bridge C structure used:** E/C split and the S-law at s = 7, extended to the family. RTA defines P_s, C and chi_nat(s) for every s (manuscript sections 6, 9, 10); chi_nat(s) = a_s = M_s^{-1}(0, s/2) (derived here, unchecked, checked by hand: Q(a_s) = −s/(4(s−2)) = −c0).
- **RTA object:** the leading profiles of P_s at odd s, namely the Gauss means G^{(s)} for M_s = [[2,s],[s,s]], with the three families K2^{(s)} = G_{a_s+μ,0}, K3^{(s)} = G_{μ,a_s}, K4^{(s)} = G_{μ,0}.
- **Statement (odd s only, s in {5, 9, 11, 13, 15, 17, 19, 21, 23, 25}; s = 7 is the anchor).**
  1. dim V_s = d_Eis(s) = 3·G(s(s−2)), with G as in ledger entry 14 (G(35) = 12, so d_Eis(7) = dim E).
  2. V_s is closed under S and T.
  3. V_s ≅ E_s untwisted, where E_s = rho-span(δ_0) in W_s (unchanged A2/A15 pipeline).
  4. Hom(V_s⊗χ^k, C_s) = 0 for every k in Z/12 (cusp silence).
- **New prediction.** Only s = 7 is proved. Item 1 is non-vacuous: G uses prime-power factors, so s = 9 (63 = 9·7), 15, 21 and 25 test the formula where s(s−2) is not squarefree. A failure at those s would show the s = 7 certificate is partly an accident of squarefree discriminant 35.
- **Data used.** Exact Gauss means over boxes 4m by 4m (A51 method) at a fixed point set per s (all h/m with m ≤ 15, 1 ≤ h ≤ 3m, gcd = 1, extended until the rank saturates, with the stopping rule fixed in the frozen version), at primes ≡ 1 mod the relevant Lev. Automorph orbits found by the A35 method with entries of absolute value ≤ 40 for the upper bound.
- **Falsification criterion (exact).**
  - Item 1 fails at s if the exact lower bound (mod-p rank) exceeds 3·G(s(s−2)).
  - Items 3 and 4 fail at s only if an explicit intertwiner (item 4) or an explicit non-isomorphism certificate (item 3) is verified exactly. A mod-p dimension alone is an upper bound and cannot refute.
  - If the orbit upper bound does not reach 3·G(s(s−2)), the result for that s is **inconclusive**, declared now, not a failure.
- **Multiple testing.** A universal exact statement over a fixed list: one failure refutes it, so no α is spent and no p-value exists. Results are reported per s.
- **Category:** A where certified; inconclusive otherwise.
- **Feasibility:** dim W_s = s(s−1) ≤ 600; the A35/A51 pipeline, one thread, under 3 GB. The cost of the 4m-by-4m boxes at m up to 15 is the dominant term and should be measured on s = 9 first.
- **What it can and cannot give.** A full pass means "uniform family: Bridge C is the s = 7 member of a family of exact Eisenstein-type leading-profile modules attached to RTA's P_s". It is **generic by design**: it cannot single out s in {7, 8, 11} or T3 or 539, and it says nothing about the C-summand beyond its invisibility. It is the weaker link to RTA, but it is the natural first step before any claim that Bridge C is RTA-wide.
- **Not counted / descriptive only:** even s (s = 8 is in RTA's list). The ledger has no d_Eis formula for even s, so no prediction is made there. Any even-s output is descriptive.

## 5. Maps considered and not admitted
1. **T3 digits to the Z/3 grading.** The abelian map (digit r goes to R^r) gives the sum of digits mod 3; by entry 47 it is exactly equidistributed on Z/3^j. There is nothing to predict. A non-abelian map into the image of SL2(Z) is the A28-type construction, whose success criterion was the 539 numerology; it is excluded by the lock.
2. **Axis / third / mixed pieces to the three R-eigenspaces.** The leading profile lives in C_third only (section 2 item 10), while the R-eigenspaces on V are balanced (12 + 12 + 12 on E-type data). No profile-compatible assignment exists (Category A, given Residual-Law Lemmas 2 and 3).
3. **{−1, 0, +1} to E/C.** No proved structure supports this. The only Bridge C ternary data is the Legendre factor, which comes from Q_s ≡ n² mod 7 and is shared by every object built on Q_s.
4. **Packaging integers to Bridge C numbers** (Bridge C dimensions and discriminant against 18, 521, 539). This is the retired M1 to M3 pattern, and E(36) = 2·18 is a declared post-hoc coincidence.
5. **A circle-method growth law for g_s from Bridge C.** A41 already has an empirical growth constant c_exp(k) for the odd part; there is no new prediction available, and no Bridge C input beyond the Legendre factor.
6. **Hecke-type reading of T3 branches** (x ↦ (ax+b)/3). The branches have determinants 3, 12, 6, so they are not a Hecke correspondence at 3, and A18 §2a already shows no homomorphism from Z/3 realises T3.

## 6. Link, negative, inconclusive
- **Link (relaxes the lock only for the declared map):** a Map 1 specificity result with p ≤ 0.05, followed by an exact proof of H1 (closed-form N verified exactly). Map 2 alone can never be a link (generic by design).
- **Negative:** Map 1 refuted at 7 (Category A). Map 2 refuted at any s.
- **Inconclusive:** anything where an exact upper or lower bound is missing. No substitution by floating point.
- A pass of Map 2 and a refutation of Map 1 together mean: Bridge C extends uniformly over RTA's s-family but has no vector-valued Fricke form. That is a clean and useful outcome.

## 7. Execution constraints (for the run, after approval)
- Single process, `nice`, `OMP_NUM_THREADS=1`, `ulimit -v 3000000`, under 3 GB.
- Reuse A51 scripts unchanged. Copy them into the run folder, and record hashes only at the freeze step (not done in this draft).
- Controls go through the identical pipeline, interleaved with the s = 7 / D_7 jobs in a fixed order.
- No existing file is modified; nothing is pushed.

## 8. Open points for Arvin before freezing
See REPORT.md, "Questions for Arvin".

## 9. Explicit statement
As of this draft, none of Map 1 or Map 2 has been run at any s or prime. The only arithmetic in this document is: Q(a) = −s/(4(s−2)) = −c0 (by hand), the block action of S and T on K2/K3/K4 read off entries 37 and 39 (by hand), and the minimum attainable p = 1/25 for Map 1. No hash was computed and no preregistration was finalized.
