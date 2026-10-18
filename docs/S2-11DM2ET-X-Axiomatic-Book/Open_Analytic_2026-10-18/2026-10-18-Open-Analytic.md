> **Master-copy notation note (added 2026-10-18 at push; report text below is otherwise verbatim).** Item 4 (cocycle) is superseded by Cocycle_Closure_2026-10-18/. report_backup_1425.md is the pass-1 snapshot, kept for provenance. Category convention for Master (rev. 5): Cat A = proved, or exact (including exact finite computation); floating-point-only results = Cat B. Naming as in rev. 4: W_P = Fix(P); V_Eis/d_Eis = Eisenstein span/dimension; Theorem G = Lewis–Zagier; Lemma Prod1/Prod2; d_2(k,v). No 'Theorem L' label is introduced (Theorem L = the framework's Parity Dominance Theorem; Lemma L keeps its name). Erratum: ERRATUM_Consolidated_Rev5_2026-10-18.md. Consolidated statement: Bridge_C_Consolidated_rev5_2026-10-18/ (§13). No TPC/RH claim; distinct from HQCC termination claims; CORE_FREEZE holds.

# Open items — analytic track (H_s, F1 removal, C_third)

Date: 2026-10-18, about 14:00–14:25 CDT; second pass 14:25–14:57 CDT (items marked **[pass 2]**). Local only; nothing pushed. The dimension/cusp algebra is handled elsewhere and is not repeated here.
Naming: W_P = Fix(P); d_Eis = the Eisenstein dimension (neither is needed below).
Labels: **Cat A** = proved or exact. **Cat B** = floating-only, fitted, or citation-only. No TPC/RH claims.

Folder: `2026-10-18-Open-Analytic/`. Files are listed in §6.

## 0. Status at a glance

| # | Item | Result | Status |
|---|---|---|---|
| 2 | Remove F1 (2-D Euler–Maclaurin for the cone sums) | Proved directly (§2): a 1-D Zagier lemma, a quadrant lemma, and a decomposition of the cone into translated quadrants, with explicit half-weight Bernoulli rule. The proof covers every rational x | **A** |
| 2 | H_s closed forms at x = 0 (t^{−1/2} … t^{5/2}) are now unconditional | The symbolic derivation (H_em2/H_closed2) computes exactly the terms of the proved expansion. An independent exact-term engine reproduces it | **A** (exact computer algebra on a proved expansion; no F1) |
| 1 | Instability at s = 7, 9, 10 | **Fixed.** The old fits used t outside the asymptotic window t ≪ 1/(mP)². Inside it, direct sums agree with the expansion to 1e−14 at every tested (s, x) | Diagnosis A; agreement B (floating) |
| 1 | t^{5/2} confirmed at more s | s = 7, 9, 10, 11, 13 (3–4 digits) on top of 6 and 8 | B |
| 1 | t^{7/2} | Symbolic closed form in (s, g) obtained (§1.3). It agrees with the engine at 9 values of s | **A** |
| 1 | **[pass 2]** x = 1/2, odd s: vanishing to all orders | **Proved** (§1.6): corners cancel between Q₊ and Q₋ (ν ↦ −ν); the area and both edge Gauss–Bernoulli sums vanish by two sign-reversing shifts (k ↦ k+2 and ν ↦ ν+2u₂). So H_s(−e^{−t}) = O(t^N) for every N | **A** |
| 1 | **[pass 2]** x = 1/2, even s (incl. 16 \| s), through t^{9/2} | **Proved symbolically** (§1.4): γ₀ = 0, eb_r = 4Σ_j(−1)^jB̃_r(j/4), ea_r = [16\|s]·eb_r. The forms of pass 1 are reproduced exactly, including the 16 \| s √Δ polynomials for g = 8 and 24; t^{7/2} and t^{9/2} added. Agrees with the engine to ≥ 33 digits | **A** |
| 1 | **[pass 2]** Area Gauss sum at x = 1/2 vanishes for all s | Proved: the phase is (−1)^n (s even) or antiperiodic under k ↦ k+2 (s odd) | **A** |
| 1 | **[pass 2]** x = 1/3 closed form | c_e = γ₀A_e(s) + Σ_r eb_r Y_{e,r}(s) + Σ_r ea_r X_{e,r}(s,g) (§1.5). γ₀ and eb depend on s mod 3 only. ea depends on s mod 144; the exhaustive table shows it is in fact s mod 72, taking 4 shapes (ea = eb, ea = eb with odd-r signs flipped, a fourth vector ±V, or 0). Explicit through t^{5/2}; pickles to t^{9/2}. Agrees with the engine to ≥ 30 digits at 10 values of s | **A** |
| 1 | **[pass 2]** t^{9/2} at x = 0 | Closed form in (s, g) (§1.7). Two independent symbolic routes (H_em4→H_closed4, and sym_engine with P = 1) agree to 170 digits at 8 values of s. Both agree with the engine at 9 values of s. H_{9/2}(5) = 0 | **A** |
| 3a | Unit-cone weight-1 piece vanishes | Rigorous proof (§3.1), both the holomorphic q-series and Zwegers' completion. Exact count check at s = 5..13 | **A** |
| 3b | Weight-0 integral = Zwegers' 2012 mock Maass theta | Proved directly from the kernel by orbit unfolding: ∫_{Γ_F} Ξ₀ = √y Σ_{γ-orbits} e(Qx) K₀(2π\|Q\|y). This is exactly Zwegers' Θ_a. No paywalled source needed | **A** (Fourier-series identity). Modularity A by Siegel/Vignéras (standard) |
| 3c | Rank-3 rewrite with θ₃ (higher depth) | **Negative.** C_third is a sum, not a product. Embedding Θ_w in rank 3 needs a wall δ_{k,0}, not a cone, so the depth stays ≤ 1 | B (structural argument) |
| 4 | Quantum-modular cocycle for the E-part with \|cx+d\| | **[pass 2]** κ_L(x) − \|cx+d\|^{−1}κ_L(γ′x) = −(1/π)∫_{γ′^{−1}∞}^{i∞}[u_L, R_x^{1/2}] checked at s = 7 for 4 matrices γ′ with c = ±140, 280 (d = 1, 141) at 45 rationals, both signs of cx+d: max deviation 7·10⁻¹³. With the holomorphic factor (cx+d)^{−1} the cx+d < 0 rows miss by 0.4 to 1.4·10³. The cusp-form assumption is replaced by "u_L has zero constant term at ∞, hence at γ′^{−1}∞" (§4) | Identity on H: A modulo the constant C = −π/2 (30-digit numerics). Boundary statement at rationals: B (strong numerics; non-tangential limits not proved) |

## 1. H_s radial coefficients

### 1.1 Setup
- H_s(q) = Σ_{ν∈C} w(ν)(q^{Q₊(ν)} − q^{Q₋(ν)}), with Q_±(n,k) = n² + snk + sk(k±1)/2.
- Cone: C = {n ≥ 0, 3sk ≥ (s−8)n}, generated by u₁ = (0,1) and u₂ = (m,b), where m = 3s/g, b = (s−8)/g, g = gcd(24, s−8). Note gcd(m,b) = 1, since gcd(3s, s−8) = gcd(24, s−8).
- Weight ½ on both edges. The origin contributes 0.
- q = e(x)e^{−t}, x = a/N; ε = √t.

### 1.2 Engine and the instability fix
`asym_engine.py` evaluates every term of the proved expansion (§2): area, both edges and the corner, at every order. It uses period P = 2N, so P = 1 when x = 0.
- Edge and corner terms are exact sympy rationals times Γ-values.
- The area term is a Gauss sum times a 1-D angular integral (mpmath, 40 digits).
- `validate_direct.py` compares the engine against vectorised direct sums.

Results:
- **x = 0.** The engine reproduces h_{−1/2}, h_{3/2}, h_{5/2} at s = 6 and 8, and all integer orders including corners vanish (A per s).
- At s = 7, 9, 10, 11, 13 with t ≲ (0.25/m)², |H − expansion| ≈ 1e−14 to 1e−15 (`val_x0.log`).
- **Diagnosis.** The expansion only becomes valid once t ≪ 1/(mP)². For larger t, corrections that are exponentially small for t ≪ 1/(mP)², with m up to 39 at s = 13, dominate. The earlier H_s-Closure fits (and the "oscillating" t^{5/2} numerics at s = 7, 9) sat outside this window.

Recovered coefficients, (H − lower orders)/t^{e/2}, against the engine (B):

| s | h_{5/2} recovered | h_{5/2} engine | h_{7/2} recovered | h_{7/2} engine |
|---|---|---|---|---|
| 7 | −0.03725 | −0.037240 | −0.02334 | −0.023446 |
| 9 | −0.07415 | −0.074170 | (roundoff-limited) | −0.056109 |
| 10 | −0.09894 | −0.098891 | −0.07955 | −0.079897 |
| 11 | −0.12826 | −0.128145 | −0.10943 | −0.109532 |
| 13 | −0.20024 | −0.201227 | (roundoff-limited) | −0.189076 |

### 1.3 t^{7/2} at x = 0
- Engine values (A per s): −0.0234460 (s = 7), −7.644990 (s = 8), −0.0561090 (s = 9), −0.0798970 (s = 10), −0.1095320 (s = 11), −0.1890760 (s = 13).
- Symbolic closed form in (s, g): `H_em3.py` (sinh orders j ≤ 9, Bernoulli p ≤ 8) → `H_closed3.py`. See `H_closed3.txt` and the status line below.

**Result:** `H_closed3` finished at about 14:18 CDT.

  H_{7/2} = √(2πs)·[R₇(s) + S₇(s,g)·√((s−2)(7s−32))], with

  R₇ = −(315s⁸ + 2184s⁷ − 65304s⁶ + 455264s⁵ − 1598160s⁴ + 3244800s³ − 3857408s² + 2506752s − 688128)/(61931520(s−2)⁵),

  S₇ = (polynomial of g-degree 8 and s-degree 12)/(61931520(s−2)⁵(7s−32)⁵). The full expression is in `H_closed3.txt` and `check_t72.txt`.

Checks:
- It reproduces H_{−1/2} … H_{5/2} identically.
- It agrees with the independent engine to every printed digit at s = 6, 7, 8, 9, 10, 11, 13, 20, 25 (`check_t72.py/.txt`).
- At s = 5, S₇√Δ = −R₇, so H_{7/2}(5) = 0, consistent with H₅ ≡ 0.
- The t³ edge/area part vanishes.
- The denominator pattern (s−2)^{r+3/2}(7s−32)^{r+3/2}, with g only in even powers up to g^{2r+1}, continues.

**Status: Cat A** (exact computer algebra on the expansion proved in §2).

### 1.4 x = 1/2 **[pass 2: proved, Cat A]**
Everything below follows from the exact reductions of §1.6 applied to the proved expansion (§2). Script: `x_half_closed.py` → `x_half_closed_K5.txt`, `x_half_closed_K9.txt`.

**Odd s.** H_s(−e^{−t}) = O(t^N) for every N (§1.6, Proposition O). Inside the window t ≪ 1/(4m)² the direct sums are 0 to 1e−14. Outside it they are large (e.g. H₇(−e^{−0.01}) ≈ −7.95). These are the exponentially small terms e^{−c/(m²t)} that the expansion does not see.

**Even s.** γ₀ = 0. The edge data are eb_r = 4Σ_{j=0}^{3}(−1)^j B̃_r(j/4) = 4·2^{1−r}(2 − 2^{1−r})B_r for r ≥ 2 (and 0 for r = 1 and for odd r), and ea_r = [16 | s]·eb_r. With D := (s−2)(7s−32):

| order | H/√(2πs), 16 ∤ s | extra term when 16 \| s: √D × |
|---|---|---|
| t^{−1/2} | 0 | 0 |
| t^{1/2} | −1/8 | g²/(8(s−2)(7s−32)²) |
| t^{3/2} | (s−4)/64 | g²(s³ − 16s² + 64s − 2g²(s−2))/(64(s−2)²(7s−32)³) |
| t^{5/2} | −(31s² − 168s + 192)/3072 | g²(3s⁶ − 96s⁵ + 1152s⁴ − 6144s³ + 12288s² − 20g²s⁴ + 248g²s³ − 1184g²s² + 1536g²s + 48g⁴(s−2)²)/(3072(s−2)³(7s−32)⁴) |
| t^{7/2} | (s−4)(173s² − 632s + 544)/24576 | degree-(9 in s, 8 in g) polynomial /(24576(s−2)⁴(7s−32)⁵); see `x_half_closed_K9.txt` |
| t^{9/2} | −(25261s⁴ − 245680s³ + 845440s² − 1226240s + 634880)/3932160 | see `x_half_closed_K9.txt` |

All integer orders vanish. Checks:
- The pass-1 reconstructions (h_{1/2}, h_{3/2}, h_{5/2}; for 16 | s the g = 8 and g = 24 polynomials, e.g. g = 8, e = 3: g²(s³−16s²−64s+256), g = 24: 9·64(s³−16s²−1088s+2304)) are reproduced identically. They are now **Cat A**.
- Universal form + Gauss data vs the exact-term engine: s = 6, 7, 9, 10, 12, 16, 32, 48, every order through t^{5/2}, deviation ≤ 7e−38 (`check_sym.py`, `check_sym_1-2_K5.json`). t^{7/2} and t^{9/2}: see §1.8.

### 1.5 x = 1/3 **[pass 2: closed form, Cat A]**
By §1.6, for every rational x the coefficient of t^{e/2} (e odd; even orders vanish) is

  c_e(s) = γ₀·A_e(s) + Σ_r eb_r·Y_{e,r}(s) + Σ_r ea_r·X_{e,r}(s,g),

with universal functions A_e, Y_{e,r} (g-free) and X_{e,r} that depend on x only through P = 2N (`sym_engine.py`, pickles `sym_universal_P6_K5.pkl`, `sym_universal_P6_K9.pkl`). At x = 1/3:
- **γ₀** = i/√3 (s ≡ 0), (1 + i√3)/6 = e(1/6)/3 (s ≡ 1), 0 (s ≡ 2 mod 3). These depend on s mod 3 only (proved: Q₊(n,k) mod 3 depends on (s mod 6, n mod 3, k mod 6), and γ₀ and G(j) are full sums).
- **eb_r** depends on s mod 3 only (same argument). For example eb₁ = 0, −1, e(1/6) and eb₂ = 2/3 − i√3/6, 1/4 + i√3/36, 1/3 − i√3/9 for s ≡ 0, 1, 2 (`x_third_classes.json`).
- **ea_r** is a function of s mod 144 (proved: H(c) depends only on (s mod 6, w mod (3,6), u₂ mod (3,6)), and s ↦ s+144 preserves g and m, b mod 6 and admits a w′ ≡ w mod 6). The exhaustive table over s = 5..240 covers every class and shows that ea is in fact periodic mod 72, with four shapes:
  - s ≡ 0 mod 3: ea = eb;
  - s ≡ 1 mod 3: ea = eb for odd s, and ea_r = (−1)^r eb_r for even s;
  - s ≡ 2 mod 9: ea = 0;
  - s ≡ 5 mod 9: ea_r = (−1)^r eb_r for odd s, ea = eb for even s;
  - s ≡ 8 mod 9: ea = ±V, V = (1, 2i√3/9, −1/18, −i√3/81, 5/648, …), with sign + for s ≡ 8, 26, 62 and − for s ≡ 17, 35, 44, 53, 71 (mod 72).
- Explicit forms through t^{5/2}: `x_third_closed_K5.txt`. For s ≡ 2 mod 3 the (γ₀, eb) part is short:
  - t^{−1/2}: −(1 + i√3)/(12s);
  - t^{1/2}: [−(19s+16) + i√3(13s−16)]/(288s);
  - t^{3/2}: (93s² − 32s − 384)/(4608s) − i√3(33s² − 160s + 128)/(1536s);
  - t^{5/2}: −(913s³ − 2032s² − 3712s + 7168)/(36864s) + i√3(2733s³ − 18992s² + 37760s − 21504)/(110592s);
  each multiplied by √(2πs). The ea part uses X_{−1,1} = −g√(2πs)/(6s√D), etc. (`x_third_closed_K5.txt`).
- Check: s = 5 (ea_r = (−1)^r eb_r) gives c_{−1} = 0, consistent with H₅ ≡ 0. Universal form vs the engine: s = 5, 6, 7, 8, 9, 10, 11, 14, 17, 20, all orders through t^{5/2}, deviation ≤ 2.4e−35 (`check_sym_1-3_K5.json`; for K = 9 see §1.8). Pass-1 table values are reproduced.

### 1.6 Exact reductions behind §1.4–1.5 and the odd-s proof **[pass 2, Cat A]**
Notation from §2: pieces p ∈ Π with offsets (α_p, β_p) and phases φ_±(p) = e(xQ_±(p)); atomic sums S0_± = Σφ_±, TEb_±[r] = Σφ_± B̃_r(β), TEa_±[r] = Σφ_± B̃_r(α), TC_±[r,r′] = Σφ_± B̃_r(α)B̃_{r′}(β); F_± = e^{−tQ_±} on the cone.

**(R1) Corners cancel for every rational x.** Q₋(−ν) = Q₊(ν). So F₋(−X,−Y) = F₊(X,Y), giving ∂^{n₁,n₂}F₋(0) = (−1)^{n₁+n₂}∂^{n₁,n₂}F₊(0). Also p ↦ −p mod ΛU sends (α,β) to (1−α, 1−β) (or 0 to 0) and φ₋(p) to φ₊(−p). Since B̃_r(1−u) = (−1)^r B̃_r(u), including the half-weight rule at u = 0, we get TC₋[r,r′] = (−1)^{r+r′}TC₊[r,r′]. In the corner term r = n₁+1 and r′ = n₂+1, so the signs multiply to +1, and the Q₋ corner equals the Q₊ corner. H takes their difference: 0 at every order. □

**(R2) The same map** gives S0₋ = S0₊, TEb₋[r] = (−1)^r TEb₊[r] and TEa₋[r] = (−1)^r TEa₊[r]. Inserting this into Lemma 2:
- the area survives only for odd i and contributes −2λ^i/i!·γ₀·J_i at t^{(i−2)/2}, where γ₀ = S0/(P²m) and J_i = ∫∫_{cone} k^i e^{−Q₂} dn dk (algebraic in s; `sym_engine.J`);
- the edges survive only for i + r even, with factor 2(−λ)^i/(i!(r+1)!).
So **every integer order vanishes for every rational x**. This proves the observation of pass 1 for all x.

**(R3) Distribution relations.**
- *Edge along u₁.* Let G(j) = Σ_{k mod P} e(xQ₊(j,k)), periodic in j mod P. Then TEb₊[r] = m^{1−r}·eb_r, with eb_r = Σ_{j<P} G(j)B̃_r(j/P).
- *Edge along u₂.* Pick w ∈ Z² with det(w,u₂) = 1, i.e. k_w m − b n_w = 1, so that Z² = Zw ⊕ Zu₂. Let H(c) = Σ_{y mod P} e(xQ₊(cw + yu₂)). It does not depend on the choice of w, and it is periodic in c mod P. Then TEa₊[r] = m^{1−r}·ea_r, with ea_r = Σ_{c<P} H(c)B̃_r(c/P).
- The half-weight rule at 0 passes through the distribution relation (Σ_i B₁(i/m) = B₁(0) is corrected by the same +½).

`gauss_data.py` implements (R3). `sym_engine.py` implements (R1)–(R2) symbolically in (s, g). Agreement with the exact-term engine to ≥ 30 digits (§1.4, §1.5, §1.8) is a consistency check of the bookkeeping.

**Proposition O (odd s, x = 1/2; Cat A).** For odd s, γ₀ = eb = ea = 0. Hence, by (R1)–(R3), every coefficient vanishes, and H_s(−e^{−t}) = O(t^N) for all N.
- *Proof.* For odd s, Q_±(n,k+2) − Q_±(n,k) = 2sn + s(2k+2±1) is odd. So φ(n,k+2) = −φ(n,k). Each G(j) is a sum over k mod 4 and is therefore 0. This gives eb = 0, and γ₀ = 0 since γ₀ = P^{−2}ΣG(j).
- For the u₂ edge, b = (s−8)/g is odd (g | 24 and s−8 is odd, so g ∈ {1,3}), and 4Q₂(u₂) ≡ 2sb² ≡ 2 mod 4. Hence Q_±(ν+2u₂) − Q_±(ν) = 2B(ν,u₂) + 4Q₂(u₂) ± sb ≡ 1 mod 2. So H(c) (a sum over y mod 4) is 0, and ea = 0. □

**Even s, x = 1/2.** Q₊(n,k) ≡ n mod 2, so G(j) = 4(−1)^j and γ₀ = 0. Also H(c) = Σ_y (−1)^{cn_w + ym}:
- it is 0 if m is odd;
- if m is even then n_w is odd, and H(c) = 4(−1)^c, so ea = eb.

m = 3s/g is even exactly when 16 | s: if s = 16k then g = 8·gcd(3, 2k−1); if s ≡ 8 mod 16 then 16 | s−8; if v₂(s) ≤ 2 then v₂(g) = v₂(s). This is the origin of the 16 | s √Δ term: the u₂-edge integral is a Gaussian in Q₂(u₂) = sD/(2g²). □

### 1.7 t^{9/2} at x = 0 **[pass 2, Cat A]**
- `H_em4.py` (sinh orders j ≤ 11, Bernoulli p ≤ 10) → `H_closed4.py` → `H_closed4.txt/.pkl`.
- Result: H_{9/2} = √(2πs)[R₉(s) + S₉(s,g)√((s−2)(7s−32))], with
  R₉ = −(s−4)(693s⁹ − 112854s⁸ + 1619016s⁷ − 10450800s⁶ + 38666512s⁵ − 89155808s⁴ + 130900480s³ − 119291904s² + 61587456s − 13762560)/(5449973760(s−2)⁶).
  S₉ has g-degree 10 and denominator 5449973760(s−2)⁶(7s−32)⁶; the full expression is in `H_closed4.txt`.
- Checks:
  - (a) the exact-term engine at s = 6, 7, 8, 9, 10, 11, 13, 20, 25 agrees to ≤ 2e−18, the double-precision floor (`check_t92.py/.txt`);
  - (b) a second, independent symbolic route (the universal form with P = 1, γ₀ = 1, eb_r = ea_r = B̃_r(0)) agrees with H_closed4 at every order t^{−1/2} … t^{9/2} to 170 digits at s = 5, 6, 7, 9, 13, 16, 32, 101 (`check_x0_two_routes.py/.txt`);
  - (c) H_{9/2}(5) = 0, consistent with H₅ ≡ 0;
  - (d) the t⁴ edge/area part vanishes.
- Values: H_{9/2} = 0.0041041851 (s = 6), 0.0101661729 (7), 40.81463220 (8), 0.0360742408 (9), 0.0585332874 (10), 0.0891887698 (11), 0.1809971281 (13).

### 1.8 Higher-order consistency runs
The t^{7/2} and t^{9/2} universal forms at x = 1/2 and 1/3 were checked against the engine through t^{9/2}:
- x = 1/2 at s = 6, 7, 16: deviation ≤ 5e−34 (`check_sym_1-2_K9.json`);
- x = 1/3 at s = 5, 7, 8: deviation ≤ 7e−30 (`check_sym_1-3_K9.json`).

The larger deviations at s = 5 and 7 come from the 40-digit mpmath area quadrature in the engine, not from the symbolic side. So the x = 1/2 table rows t^{7/2} and t^{9/2} are Cat A.

## 2. Removing F1: the needed 2-D Euler–Maclaurin expansion, proved (Cat A)

**Lemma 1** (1-D; Zagier's asymptotic lemma). Let g ∈ C^∞([0,∞)) with every derivative of rapid decay, and α ∈ [0,1]. For every M,

  Σ_{j≥0} g(ε(j+α)) = ε^{−1}∫_0^∞ g − Σ_{r=0}^{M−1} (B_{r+1}(α)/(r+1)!) g^{(r)}(0) ε^r + O_M(ε^M).

The constant is ≤ C_M ∫_0^∞ |g^{(M+1)}|. Proof: apply the Euler–Maclaurin formula to f(u) = g(εu) on [α, ∞) with the periodic Bernoulli remainder B̃_{M+1}. The remainder is ≤ (sup|B̃_{M+1}|/(M+1)!) ε^{M+1}∫|g^{(M+1)}(εu)|du = O(ε^M). □

**Half weight at an edge.** Replacing the j = 0 term by ½g(εα) when α = 0 is the average of Σ_{j≥0} g(εj) and Σ_{j≥0} g(ε(j+1)). It changes B₁(0) = −½ to 0 and leaves all B_r(0) = B_r(1) with r ≥ 2 unchanged. Write B̃_r(α) for this rule.

**Lemma 2** (quadrant). Let F be smooth on [0,∞)² with every derivative of rapid decay. Then for every M,

  Σ_{j,k≥0} F(ε(j+α), ε(k+β)) = ε^{−2}∫∫F
    − Σ_r (B̃_{r+1}(β)/(r+1)!) ε^{r−1} ∫_0^∞ ∂_Y^r F(X,0) dX
    − Σ_r (B̃_{r+1}(α)/(r+1)!) ε^{r−1} ∫_0^∞ ∂_X^r F(0,Y) dY
    + Σ_{r,r′} (B̃_{r+1}(α)B̃_{r′+1}(β)/((r+1)!(r′+1)!)) ε^{r+r′} ∂_X^r ∂_Y^{r′} F(0,0)
    + O(ε^M).

Proof: apply Lemma 1 in j for fixed Y = ε(k+β). The remainder is ≤ C ε^{M+2} Σ_k h(ε(k+β)), with h(Y) = ∫|∂_X^{M+3}F(X,Y)|dX of rapid decay, so it is O(ε^{M+1}). The main terms are 1-D sums in k of the rapidly decaying functions Y ↦ ∫F(X,Y)dX and Y ↦ ∂_X^r F(0,Y); apply Lemma 1 again. □

**Lemma 3** (cone → quadrants). Let U₁, U₂ ∈ Z² be independent and Π = Z² ∩ {αU₁ + βU₂ : 0 ≤ α, β < 1}. Then

  Z² ∩ (R≥0U₁ + R≥0U₂) = ⊔_{p∈Π} (p + N₀U₁ + N₀U₂).

A point lies on the edge R≥0U₂ (resp. R≥0U₁) iff its piece has α = 0 and j = 0 (resp. β = 0 and k = 0). So the edge half-weights are exactly the B̃ rule. □

**Application to H_s.**
1. Take U_i = P·u_i, with P = 2N, so that e(xQ_±) is constant on each piece. Check: Q_±(p + Pw) − Q_±(p) = P·B(p,w) + P²Q(w) ± (s/2)Pw₂, and x times this lies in Z.
2. Q₂ = n² + snk + (s/2)k² is positive definite on the closed cone: Q(u₁) = s/2 > 0, Q(u₂) = s(s−2)(7s−32)/(2g²) > 0, and B(u₁,u₂) = s(4s−8)/g > 0. Hence q(X,Y) := Q₂(XU₁ + YU₂) ≥ δ(X² + Y²).
3. The summand is e^{−q(X,Y)}·e^{∓ελℓ(X,Y)}, with ℓ = k-coordinate and λ = s/2. Truncate the second factor's Taylor series at order I. The tail is ≤ (ελ|ℓ|)^I e^{ελ|ℓ|}/I!, and e^{−q + λ|ℓ|} ≤ C e^{−q/2} for ε ≤ 1. A crude lattice bound gives a tail contribution O(ε^{I−2}).
4. Each kept term is a polynomial times e^{−q}, which satisfies Lemma 2.

Hence H_s(e(x)e^{−t}) has a full asymptotic expansion in powers of √t for every rational x. Its coefficients are the finite sums of area, edge and corner terms with Gauss–Bernoulli weights Σ_p e(xQ_±(p)) B̃_r(α_p) B̃_{r′}(β_p).

At x = 0 the offsets α_p run over all of (1/m)Z/Z, because gcd(m,b) = 1. So the Bernoulli sums collapse to the distribution relation Σ_i B_p(i/m) = m^{1−p}B_p. This is exactly the substitution Sx_p = Sy_p = m^{1−p}B_p in `H_closed2.py`/`H_closed3.py`. The angular integrals ANGj are the area terms of Lemma 2.

**Consequences.**
- The closed forms H_{−1/2}, H_{1/2}, H_{3/2}, H_{5/2} (and H_{7/2}, §1.3) **no longer depend on F1**: Cat A, as exact computer algebra on a proved expansion.
- The independent engine, which implements Lemmas 1–3 term by term, agrees numerically (A-level consistency).
- The prior statements "integer orders vanish" (B7) and "C closed forms modulo F1" can drop F1 as far as the expansion is concerned. Any separate "Hecke" input listed in the C closed forms is not addressed here.
- For the corners, "corner terms give only integer powers" follows directly: ∂^{r,r′} of ℓ^i e^{−q} at 0 is non-zero only when r + r′ ≡ i mod 2.

## 3. C_third

Notation as in `2026-10-18-C_third-Closure.md`:
- B(x,y) = xᵀAy, A = [[2,s],[s,s]], ν ∈ a+Z², a = (s/(2(s−2)), −1/(s−2)).
- c₁ = (s,−2)/√(s²−2s), with Q(c₁) = −1 (negative norm) and c₁ ⊥ e₁.
- γ = [[−1,−s],[2,2s−1]], c₂ = γc₁.
- F = [e₁, γe₁) is the unit cone. Both of its edges have positive norm.
- R = [[1,s],[0,−1]].

Exact facts (`R_facts.py/.txt`): RᵀAR = A, det R = −1, Re₁ = e₁, RγR = γ⁻¹, Ra + a = 0, γa − a ∈ Z².

### 3.1 The unit-cone weight-1 piece vanishes (Cat A)
**(i) Holomorphic part.** ρ(ν) := sgn B(ν,c₁) − sgn B(ν,c₂) is ±2 on the interior of F ∪ (−F), ±1 on the two edge rays (which are γ-related), and 0 elsewhere. It is odd in ν.
- F (half-open) is a fundamental domain for ⟨γ⟩ on the branch of {Q > 0} containing e₁, and γ acts freely there.
- So the q^n coefficient of Σ_{a+Z²} ρ(ν)q^{Q(ν)} is ±2[N(a,+,n) − N(a,−,n)], where N(a,±,n) is the number of γ-orbits of ν ∈ a+Z² with Q(ν) = n on the ± branch.
- ν ↦ −ν gives N(a,−,n) = N(−a,+,n).
- R maps a+Z² onto −a+Z², preserves Q, fixes e₁ (so it preserves the + branch), and conjugates γ to γ⁻¹ (so it maps γ-orbits to γ-orbits). Hence N(a,+,n) = N(−a,+,n), and every coefficient is 0. □

Exact check (`weight1_vanish_check.py/.json`): #{(a+Z²) ∩ F, Q = n} = #{(−a+Z²) ∩ F, Q = n} for all n ≤ 60, at every s = 5..13. No mismatch.

**(ii) Zwegers' completion.** Ẑ(τ) = Σ_ν [E(√y B(ν,c₂)) − E(√y B(ν,c₁))] q^{Q(ν)}.
1. *Absolute convergence.* If the two signs differ, then ν ∈ F ∪ −F, where Q ≥ δ|ν|². If they agree, |E(z₂) − E(z₁)| ≤ e^{−π min z_i²}. Each P_{c}(ν) = Q(ν) + ½B(ν,c)² is positive definite: write ν = λc + w with w ⊥ c, so P_c = λ² + Q(w). This gives a convergent majorant.
2. *Group by γ-orbits.* With h(ν) := E(√y B(ν,c₁)), the orbit sum is Σ_k [h(γ^{k−1}ν) − h(γ^kν)]. This telescopes to lim_{k→−∞} h − lim_{k→+∞} h.
3. *Limits.* Write ν = αv₊ + βv₋ (γ-eigenvectors) and c₁ = pv₊ + qv₋, with pq < 0. The limits are sgn(αq) and sgn(βp).
   - Q < 0 orbits (αβ < 0): the limits are equal, so the orbit sums to 0.
   - Q > 0 orbits (αβ > 0): the orbit sums to ±2 according to the branch, exactly as in (i).
   - There are no Q = 0 vectors in a+Z², since a ∉ Z² and Q is anisotropic.
4. Therefore Ẑ = Σ_n ±2[N(a,+,n) − N(a,−,n)]·(the q^n factor) = 0 identically. □

The earlier numerics (≈1e−15 at s = 7, 9, 13) agree. This upgrades C_third-Closure §3.3 from B to **A**.

### 3.2 The weight-0 integral is Zwegers' mock Maass theta, proved from the kernel (Cat A)
Θ̂(τ) := ∫_{t₁}^{t₂} Ξ₀ dt = √y Σ_ν q^{Q(ν)} ∫_{c₁}^{γc₁} e^{−πyB(ν,c)²} dc, where dc is hyperbolic arclength on {Q(c) = −1}.

All terms are positive, so Tonelli applies. The combined exponent is the Siegel majorant, so the sum is finite.

Group ν into γ-orbits. Since B(γ^kν, c) = B(ν, γ^{−k}c), the segments [γ^{−k}c₁, γ^{−k+1}c₁] tile the full geodesic. Each orbit therefore contributes √y q^{Q} ∫_R e^{−πyB(ν,c(u))²} du. Explicitly:
- **Q(ν) > 0:** B(ν,c(u)) = ±2√Q sinh(u − u₀), and ∫_R e^{−4πyQ sinh²u} du = e^{2πyQ}K₀(2πyQ).
- **Q(ν) < 0:** B = ±2√|Q| cosh(u − u₀), and ∫_R e^{−4πy|Q|cosh²u} du = e^{−2πy|Q|}K₀(2πy|Q|).

Multiplying by q^{Q} = e(Qx)e^{−2πyQ} gives

  **Θ̂(τ) = √y Σ_{γ-orbits O ⊂ a+Z²} e(Q(O)x) K₀(2π|Q(O)|y)**   (Cat A).

The right-hand side is exactly Zwegers' Θ_a: its sign weights select one representative per orbit. The positive orbits are counted by the false-indefinite weight ½(1 − sgn sgn) on F ∪ −F, and the negative orbits by the c^⊥ weight. So for c₂ = γc₁ and γa ≡ a, Θ̂ = Θ_a holds with no shadow. This is now proved here rather than cited; it agrees with C_third-Closure check (A) to 1e−15.

Corollaries:
- The Fourier coefficients of this weight-0 form are orbit counts.
- The holomorphic E-part E_L = ½ϑ_a, with ϑ_a = Σ_{orbits, Q>0} q^{Q}, has the same counts on the positive side.
- Modularity of Θ̂ (a Maass form with eigenvalue 1/4) follows from the Siegel/Vignéras transformation law of Ξ₀ together with the γ-invariance of the cycle. This is standard and textbook-level (Borcherds 1998, Thm 4.1), so A.

### 3.3 Rank-3 / higher depth (Cat B, negative)
C_third = ½(1 − θ₃) + ½q^{c₀}Θ_w is a **sum** of a rank-1 and a rank-2 theta.
- A rank-3 lattice sum Σ_{(ν,k)} w′(ν,k)q^{Q(ν)+k²} reproduces it only with w′ = w(ν)δ_{k,0} plus a ν-independent piece. δ_{k,0} is a wall (codimension 1), not a cone condition, so no depth-2 sign structure sgn(B(·,c₁))sgn(B(·,c₂)) with independent negative directions appears.
- A product such as θ₃·Θ_w would be rank 3, but it is not C_third.

Conclusion: no higher-depth (depth-2) object underlies C_third in the natural rank-3 extension. Higher depth is not available for this function (Cat B; an argument, not a classification).

## 4. The C_third gap: a quantum-modular cocycle for the E-part
**[pass 2]** The test was run in the s = 7 setting of `2026-10-17-psi-Cocycle.md`: u_L and u_R, κ_L = the t⁰ radial coefficient of E_L, and the Green form [u,v] = u_w v dw + u v_{w̄} dw̄. The E-part of C_third is ½q^{c₀}E_L. By Theorem P(iii) of `2026-10-18-C_third-Modularity.md`, its integer-order (renormalised) data are those of E_L, so the cocycle of κ_L is what has to be tested.

**Formula.** Let γ′ = [[a,b],[c,d]] act on u_L with trivial multiplier. Then

  **κ_L(x) − |cx+d|^{−1} κ_L(γ′x) = −(1/π) ∫_{γ′^{−1}∞}^{i∞} [u_L, R_x^{1/2}]**,  R_x(w) = Im w/|w−x|².

Derivation on H. Write 2c₀E_L(z) = ∫_z^{i∞}[u_L, R_z^{1/2}] with c₀ = −π/2 (Lemma A2 of the psi-Cocycle report). Pull back by γ′ using R_{γ′z}(γ′w) = (cz+d)²R_z(w), and close the contour (Stokes for the closed 1-form). For real x, the positive branch of R^{1/2} turns (cx+d) into |cx+d|.

**The Lewis–Zagier cusp-form assumption.** It is only used to make the integral converge at its endpoints. Here the endpoints are the cusps ∞ and γ′^{−1}∞. These are Γ-equivalent via γ′, and u_L∘γ′ = u_L. Moreover u_L has **no constant term at ∞**, because a + Z² contains no vector with Q = 0. So u_L decays like √y·e^{−2π|Q|_min y} at both endpoints, and the integral converges absolutely. No cuspidality is needed for γ′ in the stabiliser of the cusp class of ∞.
- For S-type γ′, which connect ∞ to the cusp 0 where u_R carries √y·log ε, the constant term produces the explicit extra term −(log ε)/2. That is exactly what the psi-Cocycle report found.
- So the cusp-form assumption is replaced by an explicit constant-term correction (Cat A for the convergence argument).

**Numerical test** (`cocycle_gamma.py` → `cocycle_gamma.json`, `cocycle_gamma.log`).
- Matrices: γ′_{j,k} = T^{−k}[[1,0],[140j,1]]T^k, i.e. (c,d) = (140,1), (−140,1), (280,1), (140,141).
- The path integral is reduced exactly, by S and the periodicity u_R(w+70) = u_R(w), to the tabulated J_L and J_R of `psi_period.py`.
- κ_L is evaluated exactly by `fastkappa.py`.
- Result: 45 rationals (x with denominators up to 500, γ′x with denominators up to 4000), 16 of them with cx+d < 0. **Max deviation 7.0·10⁻¹³; typical 2·10⁻¹⁴.**
- With the holomorphic factor (cx+d)^{−1}, every row with cx+d < 0 misses by 2|κ_L(γ′x)|/|cx+d|, i.e. 0.39 to 1.4·10³ (`cocycle_holfactor.py/.txt`). So the |cx+d| factor is forced, in agreement with O1.

**Status.**
- The identity on H (holomorphic side, cx+d > 0 boundary) is A, modulo the constant c₀ = −π/2, which is known to 30 digits but not derived by hand.
- The boundary identity at rationals for both signs of cx+d is **B**: it is numerically verified to 1e−13 at 45 points, but the non-tangential validity of the radial expansion and the branch argument on the cx+d < 0 side are not written out.
- Products of the weight-0 log-cocycle with weight-1 forms remain negative (unchanged).

## 5. Open items (analytic) — after pass 2
1. t^{11/2} and beyond: mechanical. The universal form (`sym_engine.py`) only needs K raised; cost grows roughly ×3 per order.
2. A uniform-in-x statement for general N: the reductions R1–R3 hold for every rational x. Only the finite Gauss data (γ₀, eb, ea) still need case analysis per N.
3. The ea mod-72 table at x = 1/3 is proved by "function of s mod 144 + exhaustive table". A conceptual (Gauss-sum) derivation of the four shapes was not attempted.
4. §4: derive c₀ = −π/2 by hand; write out the non-tangential boundary argument, the cx+d < 0 branch, and γ′ outside the ∞-stabiliser (general cusps need the full 72-component vector).

## 6. Files (`2026-10-18-Open-Analytic/`)
- `asym_engine.py`: exact-term expansion (Lemmas 1–3), any rational x.
- `validate_direct.py`; `val_s*_x*_K*.json`; `val_x0.log`, `val_x_nonzero.log`: validation against direct sums.
- `gauss_sums.py/.json/.txt`: area Gauss sums at x = 1/2, 1/3.
- `x_half_scan.py` + `x_half_scan_*.json`; `x_half_16.py` + `x_half_16.json`, `x_half_16_more.json`; `x_half_16_fit.py/.txt`: x = 1/2 closed forms.
- `H_em3.py` → `H_generic3.pkl`, `H_em3.log`; `H_closed3.py` → `H_closed3.pkl/.txt/.log`; `check_t72.py/.txt`: symbolic t^{7/2} and its check.
- `weight1_vanish_check.py/.json`; `R_facts.py/.txt`: §3.1 checks.
- **[pass 2]**
  - `atomic_sums.py`, `atomic_third.py` (+ `atomic_1-3.json`, `atomic_1-3_more.json`, `atomic_third*.log`): exact atomic Gauss–Bernoulli sums.
  - `sym_engine.py` → `sym_universal_P{1,4,6}_K{5,9}.pkl`, `sym_P*.log`: universal symbolic form.
  - `gauss_data.py`: (γ₀, eb, ea).
  - `check_sym.py` → `check_sym_1-{2,3}_K{5,9}.json`, `check_sym_K{5,9}_*.log`: checks against the engine.
  - `x_half_closed.py` → `x_half_closed_K5.txt`, `x_half_closed_K9.txt`.
  - `x_third_classes.py` → `x_third_classes.json`; `x_third_closed.py` → `x_third_closed_K5.txt`.
  - `H_em4.py`, `H_closed4.py` → `H_closed4.txt/.pkl`; `check_t92.py/.txt`; `check_x0_two_routes.py/.txt`: t^{9/2}.
  - `cocycle_gamma.py` → `cocycle_gamma.json/.log`; `cocycle_holfactor.py/.txt`: §4.
  - `report_backup_1425.md`: the report before pass 2.

