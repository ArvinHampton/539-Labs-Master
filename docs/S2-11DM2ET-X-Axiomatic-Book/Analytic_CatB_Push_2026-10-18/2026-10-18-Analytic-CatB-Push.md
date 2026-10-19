# Analytic Cat-B push: x = 1/3 ea period, t^{11/2} and t^{13/2}, general x = a/N

Date: 2026-10-18, 20:41–21:40 CDT. Local only; nothing pushed. No existing file was edited; `sym_engine.py`, `gauss_data.py` and `asym_engine.py` were *copied* into the folder unchanged.
Folder: `2026-10-18-Analytic-CatB-Push/`. Labels: **A** = proved or exact symbolic/rational; **B** = floating-point only. No TPC/RH claims.

## Status

| # | Item | Status |
|---|---|---|
| 1 | x = 1/3, ea: a conceptual proof of the mod-72 period and the shapes; exact check at s = 5..1000 | **A** |
| 1′ | Correction to the Open-Analytic §1.5 wording (the parity rule and "±V") | **A** (exact counterexamples) |
| 2a | x = 0: closed forms for t^{11/2} and t^{13/2} | **A**; 60-digit numerics **B** support |
| 2b | x = 1/2: closed forms for t^{11/2} and t^{13/2} | **A**; numerics B |
| 2c | x = 1/3: t^{11/2} and t^{13/2} as γ₀A + Σeb·Y + Σea·X, with the exact Gauss data of item 1 | **A** (universal form); numerics B |
| 3 | General x = a/N: periodicity theorem, plus a Gauss-sum evaluation of H(c) for odd primes p ∤ a·s(s−2)(7s−32) | **A** (elementary proof plus exhaustive exact check) |

## 1. x = 1/3: why ea has period 72 (Cat A)

Recall H(c) = Σ_{y mod 6} e(Q₊(cw + yu₂)/3), with u₂ = (m,b) and k_w·m − b·n_w = 1, and ea_r = Σ_{c<6} H(c)B̃_r(c/6).

**Lemma 1 (reduction mod 3).**
- Q₊(n,k) mod 3 depends only on (s, n, k) mod 3, because s·k(k+1)/2 is 3-periodic in k.
- Hence H(c) = 2Σ_{y mod 3}(…), and H depends only on s mod 3 and on u₂ mod 3. The w-coset is fixed by det ≡ 1.
- The same holds for G(j), which is the u₁ = (0,1) edge, with w = (−1,0).

**Lemma 2 (reflection).** Replace u₂ by −u₂ mod 3 and take w′ = −w. Then H′(c) = H(−c). Since B̃_r(1−u) = (−1)^r B̃_r(u), with the half-weight at 0, this gives ea′_r = (−1)^r ea_r.

**The reduced lattice data.** Write g = g₂g₃ with g₂ = gcd(8,s). Since g₂² ≡ 1 mod 3, define **ε := g₂ mod 3 = (−1)^{v₂(gcd(s,8))}**. This quadratic character (2/3)^{v₂(g₂)} is the only place where s mod 8 enters.
- **s ≡ 0 mod 3:** u₂ ≡ (0, ε).
- **s ≡ 1 mod 3:** u₂ ≡ (0, −ε).
- **s ≡ 2 mod 3:** here g₃ = 3, and u₂ ≡ ε(2, β) with β = (s−8)/3 mod 3. So s mod 9 enters here.

For s ≡ 2 mod 3 we have Q₊ ≡ (n+k)² + k mod 3. The type is decided by the 3-adic valuation of Δ = 16(s−2)² − 9s(s−2) = (s−2)(7s−32):
- v₃(Δ) ≥ 3 exactly when s ≡ 2 mod 9 (u₂ isotropic mod 3);
- v₃(Δ) = 2 when s ≡ 5 or 8 mod 9.

**Theorem 1.** Let ω = e(1/3).
- **s ≢ 2 mod 3:** ea = eb if b ≡ 2 mod 3, and ea_r = (−1)^r eb_r if b ≡ 1 mod 3. Here b ≡ ε when s ≡ 0 and b ≡ −ε when s ≡ 1. For s ≡ 0, eb_odd = 0, so both cases coincide.
- **s ≡ 2 mod 9:** ea = 0. Along u₂ the phase is linear and non-constant in y, so H ≡ 0.
- **s ≡ 5 mod 9:** ea = eb if ε = −1, and ea_r = (−1)^r eb_r if ε = +1. The proof uses the mod-3 isometry σ(n,k) = (−n−2k, k), which sends (0,1) to (1,1).
- **s ≡ 8 mod 9:** H(c) = 2i√3·ω^{−εc}, using the mod-3 Gauss sum Σ_z e(z²/3) = i√3 and k_w ≡ −ε. Therefore

  ea_r = 2^{2−r}·i√3·Σ_{c=0}^{2} ω^{−εc} B̃_r(c/3).

  This is V = (1, 2i√3/9, −1/18, −i√3/81, 5/648, 13i√3/5832, …) for ε = −1, and (−1)^r V_r for ε = +1.

**Corollary.** ea depends only on (s mod 9, ε(s mod 8)). So the period is 72 = lcm(9, 8), which divides 144. There are three Gauss types (the G-direction, the isotropic direction, and the V-direction), each with a reflection twist.

**Exact check:** every s = 5..1000 and every r = 1..10 against the defining sums, with 0 mismatches (`ea_third_theorem.py` → `ea_third_theorem_5-1000.txt`).

**Correction to Open-Analytic §1.5 (Cat A).** The exact data contradict two parts of the earlier description:
- "Odd vs even s" is wrong. The real criterion is ε. For example, s = 28 and s = 52 (≡ 4 mod 8, ≡ 1 mod 3) have ea = eb, and s = 68 (≡ 5 mod 9) behaves like odd s.
- "−V" is really (−1)^r V. For example, s = 17 gives (−1, 2i√3/9, 1/18, …).

The old file `x_third_classes.json` itself agrees with Theorem 1.

## 2. t^{11/2} and t^{13/2} (Cat A)

**Inputs.**
- `sym_engine.py` was run at P = 1, 4, 6 with K = 13, giving `sym_universal_P{1,4,6}_K13.pkl`.
- At orders up to t^{9/2} these pickles are symbolically identical to the archived K = 9 pickles (`check_K13_vs_K9.txt`).

**Splitting into R and S.** `closed_forms_K13.py` evaluates the exact symbolic coefficient at integer s where D is not a square, with g kept as a symbol. It splits the result uniquely into R + S√D and interpolates in s against the known denominators. The interpolant is then re-verified exactly at 10 held-out values of s. All checks pass (`closed_P{1,4}_K13.json/.log`, `closed_P*_e*.pkl`). The method reproduces the known R₇ and R₉ exactly.

### x = 0

Here c_e = √(2πs)[R_e + S_e(s,g)√D], with D = (s−2)(7s−32):

- R₁₁ = −(15015s¹² + 30908284s¹¹ − 717681996s¹⁰ + 7463717056s⁹ − 46065998960s⁸ + 187694296256s⁷ − 530370542912s⁶ + 1060810666496s⁵ − 1501876140032s⁴ + 1474766766080s³ − 956231974912s² + 368257794048s − 63761809408)/(5667972710400(s−2)⁷)
- R₁₃ = −(s−4)(6435s¹³ − 246052950s¹² + 5717118396s¹¹ − 60654051992s¹⁰ + 388415901904s⁹ − 1671873196832s⁸ + 5094857168704s⁷ − 11268754578560s⁶ + 18222094763008s⁵ − 21373685030912s⁴ + 17728074612736s³ − 9865267773440s² + 3305140912128s − 503819796480)/(136031345049600(s−2)⁸)
- S₁₁ and S₁₃ are polynomials in g (even powers) over (s−2)^k(7s−32)^k, with k = 7 and 8. They are given in full in `closed_P1_K13.json`.
- Both coefficients vanish exactly at s = 5 (`s5_vanish.txt`), consistent with H₅ ≡ 0.

### x = 1/2

Odd s gives 0 to all orders (Prop. O). For even s, c_e = √(2πs)[Rh_e + [16|s]·Sh_e√D], with:

- Rh₁₁ = (s−4)(675691s⁴ − 5253968s³ + 14999488s² − 18628608s + 8491008)/94371840
- Rh₁₃ = −(99680491s⁶ − 1376607512s⁵ + 7694186304s⁴ − 22340631040s³ + 35610767360s² − 29587439616s + 10020978688)/10569646080
- Sh₁₁ and Sh₁₃ are in `closed_P4_K13.json`.

### x = 1/3

- c_e = γ₀A_e + Σ eb_r Y_{e,r} + Σ ea_r X_{e,r}, using the P = 6 K = 13 pickle and the Gauss data from Theorem 1.
- `hs_coeffs.py` evaluates this exactly for any s.
- The coefficients vanish exactly at s = 5.

### Consistency with the independent engine (`check_engine_K13*.jsonl`)

The universal form was compared with the term-by-term engine `asym_engine.py`:
- x = 0, s = 6 and 7: equal to double precision.
- x = 1/2, s = 6: agreement to ≤ 3e−41.
- x = 1/3, s = 7: agreement to 7e−14 at t^{13/2}, limited by the engine's 40-digit area quadrature.
- x = 1/3, s = 5: exactly 0, against the engine's 1e−24 quadrature noise.
- The remaining engine runs (s = 9, 13, 16, 8) were still running when this report was written; if they finish, their rows will be appended to the same files.

### Cat B support: direct 60-digit sums (`numerics_mp.py`, `run_numerics.sh` → `numerics_*.jsonl`)

Method: the coefficient tables are exact integers, evaluated with mpmath at 60 digits. I subtracted the proved terms through t^{9/2} and fitted the remainder over 7 small values of t.

| s, x | rel. error, c₁₁ | rel. error, c₁₃ |
|---|---|---|
| 8, 0 | 1.2e−8 | 6.4e−6 |
| 32, 0 | 4.8e−13 | 3.2e−9 |
| 20, 0 | 1.0e−14 | 1.8e−10 |
| 56, 0 | 5.7e−14 | 6.6e−10 |
| 8, 1/2 | 2.0e−13 | 1.7e−9 |
| 32, 1/2 (16 \| s, √D part) | 1.2e−10 | 2.1e−7 |
| 32, 1/3 (s ≡ 5 mod 9) | 1.9e−9 | 1.6e−6 |

The s = 8, x = 1/3 case (V-shape) was still running.

## 3. General x = a/N (Cat A)

Let N′ = N for odd N and N′ = 2N for even N.

**Theorem 2 (periodicity).**
- γ₀, G and eb depend only on s mod N′.
- H and ea depend only on s mod 24N′.

Proof: Q₊ mod N depends on s mod N′. Also g = gcd(24, s−8) is 24-periodic, and s ↦ s + 24N′ changes m and b by multiples of N′ (since 72/g ∈ Z). Then apply Lemma 1 with N in place of 3. For N = 3 this gives exactly 72.

Exact check, s over two full periods (`general_N.py` → `general_N.json/.log`):
- a/N = 1/3, 1/5, 2/5, 1/7, 3/7, 1/4, 1/6, 1/9: 0 mismatches.
- The observed minimal period of H is 24N for N = 3, 5, 7, 9. It is smaller for even N: 16 for N = 4 and 144 for N = 6.

**Theorem 3 (Gauss evaluation).** Let p ≥ 5 be prime with p ∤ a·s(s−2)(7s−32). Then

  H(c) = 2·(a·Q₂(u₂)/p)·g_p·e( (a/p)·[ −g²(c+δ)²/(2(7s−32)) + c₀ ] ),

where:
- Q₂(u₂) = sΔ/(2g²);
- g_p = Σ_z e(z²/p);
- c₀ = s/(4(s−2));
- δ = det(a_char, u₂), normalised by det(w, u₂) = 1, with a_char = (s/(2(s−2)), −1/(s−2));
- all arithmetic is mod p.

Proof sketch:
- Complete the square: Q₊(ν) = Q₂(ν + a_char) + c₀.
- In the unimodular basis (w, u₂), the Gram determinant is −s(s−2). So the u₂-orthogonal part is −g²c′²/(2(7s−32)).
- Then evaluate the quadratic Gauss sum in y.

The quadratic character is therefore (2a·sΔ/p), which is where √Δ ties to the Gauss data. When p | Δ the sum degenerates, as in the s ≡ 2 mod 9 case at p = 3.

Exact check in Z[ζ_p]: p = 5, 7, 11, 13, every a, s < 400 (≈ 7·10⁴ (s,c) tests), 0 mismatches.

Not done: an explicit evaluation for p | Δ or for composite or even N beyond Theorem 2. Those still need the finite case analysis.

## Files (`2026-10-18-Analytic-CatB-Push/`)
- `ea_third_theorem.py`, `ea_third_theorem_5-1000.txt`
- `sym_engine.py`, `gauss_data.py`, `asym_engine.py` (unchanged copies); `sym_universal_P{1,4,6}_K13.pkl`, `sym_P*_K13.log`
- `check_K13_vs_K9.py/.txt`; `closed_forms_K13.py`; `closed_P{1,4}_K13.{json,log}`; `closed_P{1,4}_e{11,13}.pkl`; `hs_coeffs.py`; `s5_vanish.txt`
- `check_engine_K13.py`, `check_engine_K13_x{0,12,13}.jsonl`
- `numerics_mp.py`, `run_numerics.sh`, `numerics_{A..E}.jsonl`
- `general_N.py`, `general_N.json`, `general_N.log`

---

## Continuation, 2026-10-18, 21:49–22:20 CDT

New files in `2026-10-18-Analytic-CatB-Push/`:
- `latt.py`
- `gauss_local.py` → `gauss_local_run.log`, `gauss_local_*.json`
- `degenerate_p.py` → `degenerate_p.json/.log`
- `even_N.py` → `even_N.json/.log`
- `ea_N4.py` → `ea_N4.json/.log`

An earlier run with a cyclotomic-field-size bug was kept as `gauss_local_run_first_attempt_bugL.log`. The bug is described under C.2.

### C.0 Cross-checks that were still running (now finished)

**Engine vs universal form (`check_engine_K13_*.jsonl`), |sym − engine| at t^{9/2}, t^{11/2}, t^{13/2}:**
- x = 0, s = 6, 7, 9, 13: 0 at double precision.
- x = 1/2:
  - s = 6: ≤ 2.5e−41.
  - s = 16 (16 | s, √D part): ≤ 1.3e−37.
  - s = 7: the symbolic side is exactly 0 (Prop. O). The engine gives ≤ 1.7e−29, which is quadrature noise.
- x = 1/3:
  - s = 8 (V-shape): 0.
  - s = 7: ≤ 7e−14, limited by the engine's area quadrature.
  - s = 5: the symbolic side is exactly 0. The engine gives ≤ 4e−24.

This agreement is a check of the bookkeeping; the Category A status rests on the symbolic form.

**60-digit direct sums, s = 8, x = 1/3 (`numerics_C.jsonl`):** relative error 5.1e−11 for c₁₁ and 1.1e−7 for c₁₃. This is Cat B. All planned numerics are now complete.

### C.1 Item 1: degenerate Gauss sums at x = a/p, with p | s(s−2)(7s−32) (Cat A)

For p ≥ 5 these three cases are disjoint, since a common factor would force p | 18 or p | 32.

Write H(c) = Σ_{y mod 2p} e(a f_c(y)/p), where
- f_c(y) = Q₂(u₂)y² + β_c y + Q₊(cw);
- β_c = c·B(w,u₂) + sb/2;
- Q₂(u₂) = sΔ/(2g²) ≡ 0 mod p (this is the degenerate condition);
- B(w,u₂)² ≡ 4Q(w)Q(u₂) + s(s−2) ≡ s(s−2) mod p.

The y-sum collapses: H(c) = 2p·[p | β_c]·e(a·Q₊(cw)/p). This gives:
- **p | s:** H(c) = 2p·e(a·n_w²c²/p) for every c, where n_w ≡ −b⁻¹. This is a full quadratic character in c (the analogue of the V-type).
- **p | s−2:** H ≡ 0, so ea = 0. Here β_c ≡ b ≢ 0 and u₂ is isotropic mod p (the analogue of s ≡ 2 mod 9 at p = 3).
- **p | 7s−32:** H is a delta at the single class c* ≡ −sb·(2B(w,u₂))⁻¹ mod p, where B(w,u₂)² ≡ s(s−2) ≢ 0. Then

  ea_r = 2^{2−r}·p·e(a·Q₊(c*w)/p)·B̃_r(c*/p).

**General ea formula:** ea_r = 2^{1−r} Σ_{c<p} H(c)B̃_r(c/p), because H is p-periodic (distribution relation).

**Exact check:** p = 5, 7, 11, 13, 17, 19, 23; all a; s < 1200 in all three cases; about 6.2·10⁵ (s,a,c) tests; 0 mismatches. p = 7 never divides 7s−32, so that case is vacuous there. p = 3 is Theorem 1, where 3 | g changes the valuation of Q₂(u₂).

### C.2 Item 2: odd composite N via CRT, and prime powers (Cat A)

**Theorem L (CRT factorization).** Write N = 2^k·∏p^e and split a/N = Σ a_q/q^{e_q} by partial fractions.

  H_{a/N}(c) = [2 if k = 0]·T₂·∏_p T_{p^e},

where:
- T_{p^e} = Σ_{y mod p^e} e(a_p f_c(y)/p^e);
- T₂ = Σ_{y mod 2^{k+1}} e(a₂(A2·y² + B2·y + 2C)/2^{k+1}), with A2 = 2Q₂(u₂), B2 = 2β_c, C = Q₊(cw).

Proof: e(aQ/N) = ∏_q e(a_q Q/q^e); f mod p^e is p^e-periodic in y; then apply CRT to y mod 2N.

So the Gauss data H, G and γ₀ are multiplicative over prime powers. The case k = 0 carries an extra factor 2. ea_r = Σ_c H(c)B̃_r(c/2N) is linear in H and does not factor, because the Bernoulli weights are not multiplicative.

**Lemma R (q-adic reduction, any prime q).** Let v = v_q(α).
- If v ≥ n: Σ_{y mod q^n} e((αy² + βy + γ)/q^n) = q^n·[q^n | β]·e(γ/q^n).
- Otherwise it equals q^v·[q^v | β]·e(γ/q^n)·Σ_{y mod q^{n−v}} e((α′y² + β′y)/q^{n−v}), with α′ = α/q^v and β′ = β/q^v.

**Base cases (α′ a unit).**
- **Odd q:** the sum is e(−β′²(4α′)⁻¹/q^j)·(α′/q)^j·g_{q^j}. Here g_{q^j} = q^{j/2} if j is even, and q^{(j−1)/2}·g_q if j is odd.
- **q = 2:**
  - j = 1: 2·[β′ odd];
  - j ≥ 2: 0 if β′ is odd; otherwise e(−α′⁻¹(β′/2)²/2^j)·(1 + i^{α′})·(2/α′)^j·2^{j/2}.

This gives a closed form of H(c) for every N, which covers prime powers, composites, the degenerate cases and even N. C.1 and Theorem 3 are the special cases n = 1.

**Exact check in Z[ζ_L], L = lcm(8, 2N), against brute force:**
- N = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 21, 25, 27; all a coprime to N; s < 200; every c.
- About 7·10⁵ tests, 0 mismatches.
- The runs for N = 32, 35, 45, 49 were still in progress when this section was written. Their results will be in `gauss_local_run.log` and `gauss_local_*.json`.

**The bug in the first attempt:** I used L = lcm(8, N), which is too small for the 2-adic factor when N = 8 or 16 (its roots of unity need 2N | L). That gave false mismatches at N = 8, in the classes 4 | s. The rerun uses L = lcm(8, 2N); the closed-form functions themselves are unchanged.

### C.3 Item 3: even N (Cat A)

**Exact minimal periods** of s ↦ H_{a/N}, with equality in Z[ζ], over two full periods (`even_N.json`):

| N | period | H ≢ 0 exactly when |
|---|---|---|
| 2 | 16 | 16 \| s |
| 4 | 16 | 4 \| s |
| 6 | 144 | 16 \| s |
| 8 | 96 | 4 \| s |

The same periods hold for a = 3. Each listed period divides the bound 24N′ = 48N proved in Theorem 2. Since Theorem 2 proves that bound, checking every s across it is a complete proof of each minimal period, not just a numerical observation.

**Why 144 for N = 6 (conceptual).** By Theorem L, H_{1/6} = T₂^{(1/2)}·T₃^{(1/3)}, i.e. the 1/2-type factor times the 1/3-type factor.
- The 1/2 factor vanishes unless m is even, i.e. unless 16 | s (Open-Analytic §1.6). Its period is 16.
- The 1/3 factor has period 72 (Theorem 1).
- Hence H_{1/6} is nonzero exactly on 16 | s, with period lcm(16, 72) = 144.

**Why 16 at N = 2 and 4, but 96 at N = 8 (partial conceptual argument).**
- Mod 3, s enters only through g₃, which rescales u₂ by 3⁻¹ ≡ 3 mod 2^{k+1}. One computes Q₊(3ν) = Q₊(ν) + 8Q₂(ν) + s·k_ν.
- For N = 4, the nonzero classes have 4 | s, so this difference is ≡ 0 mod 4. Also det(3w, 3u₂) = 9 ≡ 1 mod 8, so the coset choice for w is preserved. Hence g₃ drops out and the period is 2-power (16).
- For N = 8, the term 8Q₂(ν) is not 0 mod 8, so g₃ matters and the period picks up a factor 3: 96 = 32·3.
- The exact values 16 and 96 themselves come from the exhaustive check above. This scaling argument explains why the factor 3 appears or not; it does not derive those values.

**Closed forms.** For even N, H(c) is given by Theorem L plus Lemma R. For example at x = 1/4 (`ea_N4.json`):
- ea = 0 unless 4 | s.
- For s ≡ 0 mod 16: ea = eb = (0, 1/3 − i/6, 0, −1/240 + 7i/1920, …).
- For s ≡ 4, 8, 12 mod 16: ea = (0, (1+i)/12, 0, −(1+i)/3840, …).
- eb (period divides 8) is the same vector for all of the tested 4 | s.

γ₀ and eb depend on s mod 2N (Theorem 2). For N = 6 the ea part is supported on 16 | s.

**Not done:** a fully conceptual derivation of the minimal periods 16 and 96 for N = 4 and 8 (only the exhaustive proof above); explicit ea tables for N = 8 (they are available from `gauss_local.py`); and inserting the even-N Gauss data into t^{11/2} and t^{13/2} closed forms for x = 1/4 and 1/6. That last step is mechanical with `sym_engine.py` at P = 8 and P = 12, and was not run.
