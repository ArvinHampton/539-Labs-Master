# PREREG: Bridge C (s = 7) and the 35-component law vector against RTA's Bridge Series C

Owner: Arvin Hampton (539 Labs). Written 2026-10-24, about 8:00 AM CDT (America/Chicago), before any computation in this folder.
Folder: `reports/bridges/BRIDGE_C_35/` (new files only). `SF/` = `reports/s_family_paths/`.
Rules in force: CORE_FREEZE (H_s not redefined, no certifier code touched; A35 `symbols.py` and A51 code imported read-only or re-implemented in new files). Category A = proof or exact certificate (mod-p ranks used only as one-sided bounds). Category B = floating point / finite range. Residual-vs-Resonant lock: a link counts only as a map defined here that predicts something new and passes. No TPC or RH claim. The prior T3-to-g_k route (`reports/bridges/CRYPTO_RNT_RTA`) is parked and not reused.

## 0. Status of the earlier A52 draft
The A52 draft (`SF/A52_bridgeC_to_RTA_draft/prereg_draft.md`) was already frozen and run as A53 (`SF/A53_RTA_maps/`, sha256 a44f6779...). Its Map 1 (vector Fricke closure V∘D_7 ⊂ V) is refuted (Category A); its Map 2 (module structure over odd s) is generic and not a link. Neither is reused here. The maps below are new.

## 1. Written objects used (no others)
Bridge C side (Category A, ledger v7 §3 and §8):
- A = [[2,7],[7,7]], Q(ν) = ½νᵀAν, B(ν,β) = νᵀAβ, D = A⁻¹Z²/Z² (order 35), a = (7/10, −1/5), h_A = (1/2, 0).
- G_{α,β}(x) = mean over ν ∈ α+Z² of e(xQ(ν)+B(ν,β)); K2_μ = G_{a+μ,0}, K3_μ = G_{μ,a}, K4_μ = G_{μ,0}; V = span of the 105 components (the 35-component law vector), dim V = 36 (entries 40, 93).
- T-law and S-law (entry 39); exact M_S, M_T (entry 94); spec(T|V) = spec(T|E), 36 distinct values (entry 95).
RTA side (manuscript `oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/Residual_Ternary_Algebra_Full_Manuscript_Draft_2026-08-24.md` §9–10; `reports/heavy-daily/2026-10-17-Bridge-C-Residual-Law.md` A2 and B3):
- Q_7(n,k) = n² + 7nk + (7/2)k(k+1); orthant series P_orth = Σ_{n,k≥0} q^{Q_7(n,k)}; cones c1 = (−1,1), c2 = (−4,1); w(v) = ½(sgn B(c1,v) − sgn B(c2,v)); H_7 = Σ_{v∈Z²} w(v) q^{Q_7(v)}; Bridge Series C = P_orth − H_7.
- chi_nat(7) = (7/10, −1/5) = a.
- Residual-Law A2 Lemma 3 (written, proof sketch only): for x = h/m, t·S(e(x)e^{−t}) → I·G(x) for S ∈ {P_orth, C}, with I = log(6+√35)/(2√35) and G(x) = (2m)^{−2} Σ_{(n,k) mod 2m} e(xQ_7(n,k)); H_7 contributes 0.
- Residual-Law B3 (written, not attempted): a vector-valued leading-order law should exist over the 35 characteristic components.
Not used because nothing written supports a map: T3, O_res/539 packaging, the g_k family (including the MIX classes k = 4, 8, 12 and the proved even k = 2, 6, 10, 14). See §5.

## 2. Map A (membership): the leading profile of RTA's C is not in V
Definition. Λ_C(x) := lim_{t→0+} t·C(e(x)e^{−t}), for x ∈ Q. By Lemma 3, Λ_C = I·G. Map A asserts the A52 draft's derived-unchecked item 8 premise in its literal form: G ∈ V.
Algebra fixed now (by hand): Aa = (0, 7/2), so Q_7(ν) = Q(ν+a) − Q(a) with Q(a) = −7/20; hence G(x) = e(7x/20)·K2_0(x), where K2_0 = G_{a,0} (μ = 0).
**Prediction (committed): G ∉ V.** Reason: the factor e(7x/20) is the radial value of q^{7/20}; G is 1-periodic (Q_7 is integer-valued) while V's T-eigenvalues are 36 distinct values; membership would need exponent 0 in spec(T|V) and that eigenvector to equal G.
Test A1 (Category A if it refutes membership). Points X216 = {h/m : 1 ≤ m ≤ 15, 1 ≤ h ≤ 3m, gcd = 1}. Columns: the 105 components (exactly as A51 `rank216.py`) plus the column G. Values reduced mod the four A51 primes p ≡ 1 mod Lev = 3 531 528 000 (17 657 640 001, 21 189 168 001, 35 315 280 001, 42 378 336 001). Statistic r_p = rank of the 216 × 106 matrix.
- r_p = 37 at any prime ⇒ G ∉ V (exact: rank only drops mod p; dim V = 36). Prediction confirmed.
- r_p = 36 at all four ⇒ G ∈ V on X216 (evidence only); prediction falsified.
Test A2 (secondary, proof route). Compute spec(T|V) exactly from M_T (T-exponents mod 1). If 0 ∉ spec(T|V), then G ∉ V is proved independently of A1 (a 1-periodic nonzero element of V would be a T-eigenvector of eigenvalue 1).
New content: corrects/decides a written but unchecked premise (A52 item 8, "RTA's leading profile is a coordinate of the K2 family / cyclic vector of V").

## 3. Map B (vector-valued law for RTA's C at leading order)
Definition. Untwist: Λ_C(x) = I·e(7x/20)·K2_0(x). Map B asserts that RTA's C carries, at the 1/t order, the vector-valued S-law of the 35-component law vector, explicitly:
(B) for every rational x ≠ 0: Λ_C(−1/x) = I·e(−7/(20x))·(1/(|x|√35))·Σ_{p∈D} e(−B(p,2a))·K3_p(x).
(Derivation fixed now: entry 39 S-law with α = a, β = 0 gives K2_0(−1/x) = (|x|√35)^{−1} Σ_p G_{p,−a}(x); since A(2a) = (0,7) ∈ Z², G_{p,−a} = e(−B(p,2a))·G_{p,a} = e(−B(p,2a))·K3_p by entry 37.)
Predictions (new, checkable):
- B-exact: identity (B) with Λ_C replaced by I·G holds at all 216 points of X216 (G at y = −1/x computed directly as a finite mean; RHS from the K3 values). Checked exactly mod the four primes (each nonzero difference would refute; 0 at all four primes is an exact certificate per point only if combined with the proof; the proof is entry 39 + entry 37).
- B-radial (Category B): the actual RTA series C (as defined in §1, with half-weights on walls from sgn 0) satisfies t·C(e(y)e^{−t}) → RHS of (B) at y = −1/x for the 30 points x ∈ X216 with m ≤ 5. Fit t·C = c0 + c1 t^{1/2} + c2 t + c3 t^{3/2} by least squares on t ∈ {8e-4, 4e-4, 2e-4, 1e-4, 5e-5, 2.5e-5}, truncating lattice sums at Q_7 ≤ 40/t. Let ref = I/den(y) (den = reduced denominator). Pass at a point if |c0 − RHS| ≤ 0.02·ref; falsify if > 0.10·ref at any point; otherwise inconclusive. Overall: confirmed if all pass; falsified if any falsifies.
- B-proof: a full proof of Lemma 3 (orthant and cone, with remainder O(t^{−1/2})) is to be written in RESULTS; with it, (B) is Category A.
What Map B claims as a link: the RTA object C has a leading-order transformation law under x ↦ −1/x that is vector-valued in V (weight |x|^{−1}), after removing the multiplier q^{7/20}. It does not claim a law for C itself (excluded by Residual-Law A3), nor a W_7 law (refuted inside V by A53).

## 4. Map C (Fricke sample, descriptive corollary of B), declared now
At the four RTA sample points x ∈ {1/7, 3/7, 5/7, 1}, compute exactly |Λ_C(x)| and |Λ_C(−1/(7x))| from G (entry 18 magnitudes: 0 if 2|m or 5|m; I/m if 7∤m; I√7/m if 7|m). Prediction: the ratio |Λ_C(−1/(7x))|/(|7x|^{−1/2}|Λ_C(x)|) is not constant across the four points (consistent with the RTA manuscript §12). Exact check, Category A, but it is a consequence of entry 18 and Lemma 3, so it is NOT counted as a new link.

## 5. Declared untestable / no map
- g_k family (MIX classes k = 4, 8, 12; proved even k): the 35-component law vector is defined from A_7 (and A_s for odd s in A53). No written object relates g_k coefficients or their sign classes to Gauss means or to V. P_7 = (−q^7;q^7)_∞ g_7 = Σ q^{Q_7}/(q^7;q^7)_k (manuscript §7) has radial growth governed by the eta-quotient, not by a 1/t lattice profile, so the 35-component law vector does not see g_7 at leading order. No map.
- T3, O_res, 539: no Bridge C object depends on them. No map.
- s = 33 / s = 39 sector_exact: on hold (memory limit); not used.

## 6. Order of work
Hash this file → write scripts → record script hashes in NOTES.md → run A1, A2, B-exact, B-radial, C → RESULTS.md. Any change after hashing goes in NOTES.md with a timestamp; predictions, statistics and thresholds above do not change.
