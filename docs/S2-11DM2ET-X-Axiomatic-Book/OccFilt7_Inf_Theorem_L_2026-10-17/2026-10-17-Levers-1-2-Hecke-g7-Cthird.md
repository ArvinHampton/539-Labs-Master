# Levers 1 & 2: Hecke-type form for g_s; C_third as an HM double sum
Date: 2026-10-17 (America/Chicago). Master tip 48684e3 (unchanged). Read-only: nothing pushed, emailed, or sent.
Scripts and outputs are in `2026-10-17-levers-1-2/`: `bailey.py`, `denom_test.py`, `verify.py` (+ `verify.txt`), `mcheck.py`, `cthird.txt`.
HM = Hickerson–Mortenson, arXiv:1208.1421. Every equation and theorem number below was read on the arXiv page.

## Lever 1: Hecke-type form for g_s

### Calibration (passed)
- **s = 1.** g_1 is the 5th-order f_0. I checked HM eq. (0.3), (q)_∞ f_0(q) = Σ_{n≥0,|j|≤n} (−1)^j q^{5n²/2+n/2−j²}(1−q^{4n+2}), by exact integer coefficients. It **matches through q^200** (`verify.py`).
  - Through the Bailey lemma (a = 1), β_n = 1/(−q;q)_n gives α_n that are **finite Laurent polynomials** for n ≤ 7 (`bailey.py`): degrees 0, 2, 7, 15, 26, 40, 57, 77, with sparse ±2 coefficients. That is exactly the shape that produces a Hecke-type sum.
- **s = 2.** g_2 is the 3rd-order φ. HM eq. (4.5), third line, φ(q) = m(q^5,q^12,q^4) + m(q^5,q^12,q^8) + q^{−1}m(q,q^12,q^4) + q^{−1}m(q,q^12,q^8), with m from HM Def. 0.1, **matches through q^180** (`mcheck.py`).
  - My first implementation of the last line of (4.5), 2m(q,−q^3,−1) + 2qJ_12^3/(J_4 J_{3,12}), did not match. I did not find the cause, which could be my series handling of base −q^3. I make no claim either way about that line.
  - Bailey data for s = 2: α_n·(1+q^{2n}) has **exactly 2 terms** for n = 1..5. That is consistent with α_n = 2(−1)^n q^{n(n+1)/2}(1+q^n)/(1+q^{2n}), checked only for n ≤ 7, and only matching the observed terms. One factor 1/(1+q^{2n}) per n is the Lambert-series shape behind an Appell–Lerch form, which is what HM (4.5) is.

### s = 7, 8, 11 verdict: negative, with the reason stated
- Same inversion (Bailey pair relative to a = 1, base q, β_n = 1/(−q^s;q^s)_n), truncated at q^400 (`denom_test.py`).
  - α_n is **not** a polynomial.
  - α_n(1+q^{sn}) is still an infinite series for n ≥ 2: it is nonzero up to the truncation edge.
  - Only the full product (−q^s;q^s)_n clears the denominators. That is forced trivially, because every β_j with j ≤ n divides into it.
  - The cleared numerators are dense and growing. For s = 7, n = 1..5, there are 5, 14, 25, 43 and 78 nonzero terms, at degrees 8, 24, 48, 80, 120.
  - s = 8 and s = 11 behave the same way.
- **The obstruction.** The Hecke step needs α_n to be either a single-index alternating theta segment (as at s = 1) or such a segment over one Lambert factor (as at s = 2). For s ≥ 3 the natural pair has neither shape. The mixed bases are the cause: q^{n²} with base q, against denominators with base q^s.
  - I know of no published Bailey pair, in HM, Andrews' Hecke-type papers, or Slater's list, with β_n = 1/(−q^s;q^s)_n relative to base q for s ≥ 3. This is "not found", not "proven not to exist". I did not search Slater's list exhaustively.
  - Re-basing to q^s (writing q^{n²} = (q^s)^{n²/s}) breaks integrality unless s | n², so it does not help directly.
- **What would still be open:** a different Bailey pair (other a, conjugate Bailey pairs), or a split of n by residue mod s. Neither is attempted here.
- **Status:** g_7 is **NEGATIVE** for this method. No identity and no candidate.

## Lever 2: C_third as an HM double sum

### Master definition
`Residual_Twin_Support_Path1_Empirical_Locks_2026-08-24.md` and `Residual_False_Theta_Construction_Attempt_C_2026-08-23.md` (tip 48684e3) define
C_third = Σ_{n,k≥1} q^{Q_minus(n,k)}, with Q_minus = n² + 7nk + (7/2)k(k−1).
- Q_plus = Q_minus + 7k (`U1_LEDGER_P_PATH4_EULER_Not_Closed_On_Family_2026-09-02.md`).
- My first degrees are 8, 18, 22, 30, 39, 43, 44, 58, 60, 67, 71, 78. These match Master.
- Note: `Pursue_All_C_Closure_Status_2026-08-23.md` calls these points "weight −1", while the explicit sum is written with +1. Master is internally inconsistent on the overall sign. I used the explicit sum.

### Identity (exact)
**C_third(q) = q^8 · f_{2,7,7}(−q^{10}, −q^{14}, q) + Σ_{n,k≥0} q^{Q_plus(n,k)}**
- f_{a,b,c} is as in HM Definition 0.2 (eq. 0.4).
- Proof: shift r = n−1, s = k−1. Then Q_minus = 8 + 2C(r,2) + 7rs + 7C(s,2) + 10r + 14s.
  - The choices x = −q^{10} and y = −q^{14} cancel the (−1)^{r+s}.
  - The r,s ≥ 0 orthant of f is C_third.
  - The r,s < 0 orthant enters with sign −1. Substituting (r,s) = (−1−n, −1−k) turns it into Σ_{n,k≥0} q^{Q_plus(n,k)}.
- Checked to **q^500** (`cthird.txt`).
- Discriminant: b² − ac = 49 − 14 = **35**, matching Master's disc 35, signature (1,1).
- Side remark: the axes of Q_plus give Σq^{n²} and Σq^{7k(k+1)/2}, which are exactly the C_axis pieces. I did not check whether Σ_{n,k≥0} q^{Q_plus} relates to P_orth on Master.

### HM theorem scope (checked exactly)
- **Thm 0.4** needs ac < b² (14 < 49, holds) **and** a | b and c | b. Here 2 ∤ 7, so it fails.
- **Thms 0.3, 0.6, 0.9, 0.10, 0.11** all need a = c (2 ≠ 7), so they fail.
- Splitting r and s by residues (r = m r′, s = n s′) gives the form (2m², 7mn, 7n²). Divisibility would need 2m | 7n and n | m, which is impossible, so no split helps. I also confirmed by search over m, n < 30.
- Parity splitting (HM Prop 5.1) keeps (a,b,c) unchanged.
- **Conclusion: no HM theorem as stated covers f_{2,7,7}.** I cannot write an HM Appell–Lerch expression with a citation.

### Zwegers route (heuristic only)
- Gram matrix A = [[2,7],[7,7]], det −35.
- The dual cone vectors are c_1 = A^{−1}e_1 and c_2 = A^{−1}e_2. They have Q(c_1) = −1/10 and Q(c_2) = −1/35, both negative, which is the condition Zwegers' indefinite theta functions require (thesis, Ch. 2).
- So a non-holomorphic completion is expected via Zwegers' framework. I did **not** verify the theorem number or the cone-component sign condition against the thesis PDF. **Cat B.**
- Possible further citation: Mortenson's later general-(a,b,c) work. **Unverified;** I give no reference.

## Category A
1. The g_1 and HM (0.3) identity, plus a coefficient match to q^200. The identity itself is cited.
2. The g_2 and HM (4.5) third-line identity, plus a coefficient match to q^180. The identity itself is cited.
3. C_third = q^8 f_{2,7,7}(−q^{10},−q^{14},q) + Σ_{n,k≥0} q^{Q_plus}. This is a direct reindexing of HM Def. 0.2, so the proof is elementary. Disc 35.
4. f_{2,7,7} is outside the hypotheses of HM Thms 0.3, 0.4, 0.6, 0.9, 0.10 and 0.11. This follows from the hypotheses as stated, including under all residue splits.

## Category B
1. The Bailey-pair α_n for s = 7, 8, 11 are non-polynomial, and only (−q^s;q^s)_n clears them. This rests on truncation to q^400 and n ≤ 5–7.
2. The s = 2 closed form for α_n is a guess fitted for n ≤ 7.
3. The claim that no published Bailey pair fits g_s for s ≥ 3 rests on a non-exhaustive search.
4. A Zwegers completion of f_{2,7,7} should exist (negative-norm dual vectors), but the theorem number is unverified.

## Effect on open items
- **QM of g_s:** unchanged; still a CONJECTURE. Lever 1 gives no Hecke or Appell–Lerch route for s = 7, 8, 11, so there is no mock-modular handle from which to derive QM. s = 1 and s = 2 remain the only cases with published structure.
- **Θ_third completion:** improved in form, not closed.
  - C_third is now exactly one HM building block plus a positive-cone remainder, with disc 35 confirmed.
  - The citable Appell–Lerch formula is blocked by HM's divisibility hypothesis.
  - The completion still rests on Zwegers' general theory, which is Cat B until the theorem and cone conditions are checked against the source.
- Object B, Per_off, OccFilt_7(∞), Remark 8.5 and Slash_two are untouched. HQCC is not involved.

## Next steps
(a) Fetch the Zwegers thesis PDF (arXiv:0807.4834) and check the exact theorem for θ_{c_1,c_2}, plus the cone-component condition B(c_1,c_2) for A = [[2,7],[7,7]].
(b) Settle the sign convention for C_third on Master.
(c) For g_7, try conjugate Bailey pairs, or a split by n mod 7 that puts the exponent and the denominator on a common base.

---
## Follow-up (2026-10-17, evening)
New scripts in `2026-10-17-levers-1-2/`: `zwegers.pdf`/`zwegers.txt` (arXiv:0807.4834v1, fetched), `zwegers_check.py`, `zw2.py`, `zwegers_check.txt`, `retry.py`, `retry.txt`.

### F1. Zwegers: the hypotheses hold (Cat A for the citation and the hypothesis check)
**Source.** S. Zwegers, *Mock Theta Functions*, PhD thesis, Utrecht 2002 (arXiv:0807.4834v1). All of the following is quoted from the fetched text.
- **§2.2 setup.** A is a symmetric, non-degenerate integer matrix, Q(x) = ½⟨x,Ax⟩, B(x,y) = ⟨x,Ay⟩, and Q has type (r−1, 1).
  - "The set of vectors c with Q(c) < 0 has two components. If B(c1,c2) < 0 then c1 and c2 belong to the same component."
  - C_Q := {c : Q(c) < 0, B(c,c0) < 0}.
- **Definition 2.1.**
  - For c1, c2 ∈ C̄_Q: ϑ_{a,b}(τ) = Σ_{ν∈a+Z^r} ρ(ν;τ) e^{2πiQ(ν)τ + 2πiB(ν,b)}.
  - ρ = ρ^{c1} − ρ^{c2}, where ρ^c(ν;τ) = E(B(c,ν)√y / √(−Q(c))) for c ∈ C_Q.
  - E(z) = 2∫_0^z e^{−πu²}du (Definition 1.6), and E(z) = sgn(z)(1 − β(z²)) with β(x) = ∫_x^∞ u^{−1/2}e^{−πu}du (Lemma 1.7).
  - For c ∈ C_Q, R(c) = R^r, so any characteristic a is allowed.
- **Proposition 2.4.** The series converges absolutely.
- **Corollary 2.9.** Elliptic and modular transformation laws:
  - (4) ϑ_{a,b}(τ+1) = e^{−2πiQ(a) − πiB(A^{−1}A*, a)} ϑ_{a, a+b+½A^{−1}A*}(τ).
  - (5) ϑ_{a,b}(−1/τ) = (i/√(−det A)) (−iτ)^{r/2} e^{2πiB(a,b)} Σ_{p∈A^{−1}Z^r mod Z^r} ϑ_{b+p,−a}(τ).
  - This is a vector-valued weight-r/2 law, so weight 1 here.

**Hypothesis check for A = [[2,7],[7,7]].** Here Q(r,s) = r² + 7rs + (7/2)s², and det A = −35, so the type is (1,1).
- c1 = A^{−1}e1 = (−1/5, 1/5), so B(c1,ν) = ν_1.
- c2 = −A^{−1}e2 = (−1/5, 2/35), so B(c2,ν) = −ν_2.
- Q(c1) = −1/10 < 0 and Q(c2) = −1/35 < 0.
- B(c1,c2) = −1/5 < 0, so c1 and c2 lie in the same component. Taking c0 = c1, both are in C_Q. **Every hypothesis of Definition 2.1, Prop. 2.4 and Cor. 2.9 holds.**
- Exact rationals: Q(c_i) = ½(A^{−1})_{ii} and B(c1,c2) = −(A^{−1})_{12}.

**Characteristic that reproduces the HM sign rule.** Take a = (−7/10, 1/5) and b = 0, and write ν = (n,k) + a. Then:
- Q(ν) = Q_minus(n,k) − 7/20, since B((n,k),a) = −(7/2)k and Q(a) = −7/20.
- B(c1,ν) = n − 7/10 and B(c2,ν) = −(k + 1/5). Neither is ever 0, so there are no boundary ambiguities.
- As y → ∞, ρ → sgn(n−7/10) + sgn(k+1/5). That is 2 on {n≥1, k≥0}, −2 on {n≤0, k≤−1}, and 0 elsewhere.

**Holomorphic-part identity** (exact integers, to q^399):
Θ_hol(q) := Σ_{n≥1,k≥0} q^{Q_minus} − Σ_{n≤0,k≤−1} q^{Q_minus} = q^8 f_{2,7,7}(−q^{10},−q^{14},q) + θ_3(q), where θ_3(q) = Σ_{n∈Z} q^{n²}.
Equivalently, Θ_hol = C_third + Σ_{n≥1} q^{n²} − Σ_{n≥0,k≥1} q^{Q_plus(n,k)}.

**Completion (explicit), with q = e^{2πiτ} and y = Im τ:**
ϑ_{a,0}(τ) = q^{−7/20} [ 2Θ_hol(q) − Σ_{(n,k)∈Z²} ( sgn(n−7/10) β(10(n−7/10)² y) + sgn(k+1/5) β(35(k+1/5)² y) ) q^{Q_minus(n,k)} ]
- The first β term is 10 = 1/(−Q(c1)); the second is 35 = 1/(−Q(c2)).
- ϑ_{a,0} transforms by Cor. 2.9 (4)–(5) as weight 1, vector-valued over the 35 classes of A^{−1}Z²/Z².
- Status: the formula is Cat A by citation plus direct substitution. The numerical checks below are Cat B.

**Numerical check of Cor. 2.9(5) on this ϑ_{a,0}.** τ = it, 35 exact classes, summing n,k over [−60, 60]:
- t = 0.9: both sides 0.00071505516999, difference 1.7e−16.
- t = 1.3: both sides 0.03201813467272, difference 5.9e−17.
- A first run with plain erf disagreed at about 1e−10 because erf saturates in floating point. It was fixed by computing with erfc.

**What this means for C_third and Θ_third:**
- C_third = Θ_hol − Σ_{n≥1} q^{n²} + Σ_{n≥0,k≥1} q^{Q_plus(n,k)}.
- Θ_hol is (½q^{7/20} times) the holomorphic part of a Zwegers weight-1 indefinite theta function, so it is mock modular with an explicit completion. Σ q^{n²} is a theta function.
- The remainder Σ_{n≥0,k≥1} q^{Q_plus} is **a positive-definite-cone partial sum, not a theta function**. So C_third alone is **not** shown to be mock modular. Only the combination Θ_hol is completed.
- **Θ_third completion is CLOSED for the Zwegers piece Θ_hol and OPEN for C_third itself.**
- Side remark: Master's H_s cone uses c1 = (−1,1) and c2 = (−4,1) (`Review_Missed_Variables_Bridge_C_2026-08-23.md` l.55). That is a different setup and I did not reconcile it.

### F2. Master sign convention: no contradiction; one correction to my earlier note
- **H_s cone weight** w = −1 on third-quadrant points (n<0, k<0). Since C = P_orth − H_s, each such point contributes **+1** to C. Locations:
  - `Open_Paths_C_Closure_Continuation_2026-08-23.md` l.12, l.16, l.18 (C_third = Σ_{n,k≥1} q^{Q(−n,−k)}, with Q = Q_plus, so Q_plus(−n,−k) = Q_minus(n,k))
  - `Pursue_All_C_Closure_Status_2026-08-23.md` l.46 ("third-quadrant points of weight −1")
  - `C_Axis_Pairing_and_Natural_Characteristic_2026-08-23.md` l.39 and l.53 ("w = −1, each contributing +1 to C")
  - `U1_GS_BRIDGE_C_AUDIT_d534333_2026-08-23.md` l.51 ("w = −1: contribution +1")
  - `Review_Missed_Variables_Bridge_C_2026-08-23.md` l.55, l.72–79
- **Explicit +1 sum for C_third:**
  - `Residual_False_Theta_Construction_Attempt_C_2026-08-23.md` l.24
  - `Residual_Twin_Support_Path1_Empirical_Locks_2026-08-24.md` l.14
  - `Residual_Ternary_Algebra_Full_Manuscript_Draft_2026-08-24.md` l.208
  - `PUSH_LOG_2026-08-23_Open_Paths_C_Continuation.md` l.12
- **These are consistent**: weight −1 in H_s gives coefficient +1 in C. My earlier statement in this file ("Master is internally inconsistent on the sign") is **withdrawn**.
- **Suggested wording fix only:** the "weight −1" sentences should say "H_s-weight −1 (contributing +1 to C)". `Pursue_All_C_Closure_Status_2026-08-23.md` l.46 is the one line that omits this.
- Also, `Discrete_Bridge_E8_to_Fifth_Order_2026-08-24.md` l.9 calls the form Q = n² + 7nk + (7/2)k(k+1) (that is, Q_plus). That is consistent once paired with (−n,−k), but stating which form is meant would help.

### F3. g_7 Bailey retry: negative (bounded attempt)
**(a) Split n = 7m + j.** g_7 = Σ_{j=0}^{6} q^{j²} h_j(q^7), where h_j(p) = Σ_m p^{7m²+2mj}/(−p;p)_{7m+j}.
- The exponent and the denominator now share base p, but the Pochhammer length is 7m+j, not m. The Bailey lemma needs weight p^{N²}a^N in the index N = 7m+j, and the weight here is p^{N²/7}. So the mismatch only moves; it does not go away.
- The first 30 coefficients of each h_j are in `retry.txt`. h_0, h_1 and h_2 have no OEIS hits.

**(b) Change of a, and conjugate pairs.**
- Calibration: Bailey inversion relative to a = q is polynomial for s = 1, with degrees 0, 4, 11, 21, 34, 50.
- At s = 7 it does not terminate, with nonzero terms up to the q^300 truncation, the same as a = 1.
- Conjugate Bailey pairs in Andrews' form, Σ(ρ1)_n(ρ2)_n(aq/ρ1ρ2)^n β_n, give quadratic weights only in the base of the pair:
  - In base q^7 the quadratic coefficient is a multiple of 7/2, so q^{n²} can never appear.
  - In base q the pair must have β_n = 1/(−q^7;q^7)_n, which is the pair shown above to be non-terminating for a = 1 and a = q.

**Obstruction (Cat B, computational plus structural).**
- No Bailey-lemma specialization pairs the weight q^{n²} with a terminating pair for β_n = 1/(−q^7;q^7)_n.
- Slater's list was not searched exhaustively.
- **Verdict: no Hecke form found for g_7; stopped.** QM of g_s is unchanged (CONJECTURE).

### Updated Cat A / Cat B
- **Cat A (new):**
  - The Zwegers Def. 2.1 / Prop. 2.4 / Cor. 2.9 hypotheses hold for A = [[2,7],[7,7]] with c1 = (−1/5, 1/5), c2 = (−1/5, 2/35).
  - The identity Θ_hol = q^8 f_{2,7,7}(−q^{10},−q^{14},q) + θ_3 (elementary reindexing).
  - The explicit completion ϑ_{a,0} above.
  - The Master sign conventions are consistent.
- **Cat B (new):**
  - The numerical checks of Cor. 2.9(5), to about 1e−16.
  - The g_7 retry negatives (truncated computations).
