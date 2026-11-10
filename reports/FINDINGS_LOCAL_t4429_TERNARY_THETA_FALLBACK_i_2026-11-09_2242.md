# FINDINGS (Local-derived) t4429 fallback (i): ternary-theta / genus-difference method for the weight-3/2 preimage of g = 49a1⊗χ₋₄ and of Ξ. 2026-11-09, written 22:42 CST (America/Chicago)

- Additive; no earlier file edited. No CERT. No Gemini. Nothing sent outside. Tip 7cddb188ca340ad9… unchanged. Rule OW 3f160803/36683379 (citation alone never PROVED). ε = root number, w_N = Fricke eigenvalue, ε = −w_N at weight 2.
- Evidence: reports/evidence_local_t4429_ternary_2026-11-09/ (every file has a .sha256 sidecar; table §5).

## 1. Method
- Generators: theta series θ_Q of positive ternary forms Q (Gross / Pacetti–Tornaría style: θ-differences across classes of a ternary genus are weight-3/2 cusp forms).
  - tt_v2*: CM-shape products B_{a,ψ}(τ)·U_{b,M,r}(τ) (binary form x²+xy+2y² with χ-twist ψ on the norm, times unary/coset thetas).
  - tt_v4/v4b/v4c: **all** Minkowski-reduced positive ternary forms of a given discriminant d = det(Gram)/2, deduplicated by θ-series.
- Formal eigen-solve: find Σk_Qθ_Q with c(p²n) + (D/p)(−n/p)c(n) + p·c(n/p²) = λ_p c(n) for p ∈ {3,…,43}, p ∤ d (p ≠ 5 for Ξ), n ≤ N/p², D ∈ {±1, ±2, ±5, ±7, ±10, ±14, ±35, ±70}; linear algebra mod 2³¹−1 (python-flint).
- v4c adds the artefact filter: "specific nullity" = nullity(E_T) − nullity([E_T; E_ref]) (ref f for g, g for Ξ). A nonzero form cannot have two different T(p²)-eigenvalues, so common vectors are truncation artefacts. Genuineness also needs stability as N grows.

## 2. Results
| # | Statement | Grade |
|---|---|---|
| TT-1 | dim(span{θ_{L₁}(aτ)θ(bτ)} ∩ K) = 2 at level 196, G₁ = θ_{L₁}(τ)θ(49τ) − θ_{L₁}(7τ)θ(τ) = 4Kc[3], G₂ = 4Kc[4] | **PROVED** (filed as a row in ERRATUM2 …_2207, 076a0782…; membership/Sturm per PP 2205; Local independent check tt_v5) |
| TT-2 | Method control: the f = 49a1 packet is recovered as genus differences — d = 343 (D = 7, dim 2: θ_{x²+2y²+49z²−xy} − θ_{x²+7y²+14z²−7yz}), d = 686 (D = 14, dim 2), d = 1372 (D = 7 and 14, dim 8), stable from N = 12000 to 20000 | evidence (formal, truncated, mod p) |
| TT-3 | f also has a formal weight-3/2 eigen-combination with **D = 14** (χ₅₆ class) at d = 686 | evidence only; candidate (would sit in a χ₅₆-type space; not checked against a PARI space) |
| TT-4 | **g = 49a1⊗χ₋₄: no genuine formal eigen-combination** in the θ-span of all ternary forms of discriminant d = 2^a7^b, 7 ≤ d ≤ 10976 (36 values; tt_v4 run2), nor d = 2^a7^b·q, q ∈ {3, 5, 15, 25}, 15 ≤ d ≤ 8000 (93 values; tt_v4 run3), for every D tried. CM-shape twisted products (tt_v2c, 549 independent generators): none at N = 30000 | evidence (negative); OPEN as mathematics |
| TT-5 | **Ξ: same negative result** on the run3 discriminant list (which includes 5- and 25-parts), every D tried | evidence (negative); OPEN |
| TT-6 | Every transient nonzero g/Ξ kernel was resolved as an artefact: d = 7168 (common to f and g; then specific nullity 2→1→0 at N = 20000/40000/80000), d = 3920 (2→1→0), d = 5600 (1 at N = 20000, 0 at N = 40000), d = 2800 (common to g and Ξ, vanishing on n < 80) | evidence (exact bookkeeping of the runs) |

**Caveats (why TT-4/TT-5 are not PROVED non-existence):**
1. Linear algebra is mod one prime; truncation N ≤ 80000 is below the weight-3/2 Sturm bound of the θ-levels for large d (≈ 1.5·d·Π(1+1/p) at level 4d, e.g. ≈ 9400 for d = 10976, while independence of generators was measured only on n ≤ 3000 (v4) or N/9 (v4b/c)). A genuine form could be lost if two θ-series agree up to that range but differ beyond it.
2. Only discriminants of the shapes listed were tried, and only quadratic D in the list above.
3. Theta series of ternary forms of a single discriminant need not exhaust the relevant weight-3/2 space (Eisenstein / unary parts, and spaces not spanned by thetas).

## 3. Reading (OPEN; no claim)
The ternary-genus route reproduces f's packet at once but sees no g or Ξ preimage in 2-power × 7-power genera, nor with 3- or 5-parts up to 8000. This matches the ob-route null results at 1568/3136/6272 (D = 1, 8) and B1 (χ₋₄ odd, not a square). A consistent hypothesis: the 2-adic local component of g (ramified principal series twisted by χ₋₄, local sign ε₂ = −1 as in the 2/5/7 analysis) puts the Waldspurger preimage outside the Γ₀(4N)-with-quadratic-character spaces that these genera reach. A possible next route would need lattices with nonsplit 2-adic structure (orders in the quaternion algebra ramified at {2, ∞} or {2, 7}), or Γ₁-level structure. This is OPEN. O-b stays OPEN.

## 4. Status of the other streams (no claims)
- ob_v3 (B5, level 6272, D = 28 then 56): still in the p = 11 step for D = 28 (kernel 88 → 32 after p = 3, 5). Alive, not hung (CPU-bound in mfheckemat(m, 121)). B5 PENDING.
- Chained launcher evidence_local_t4407_computations_2026-11-09/chain_after_ob_v3_s2e_then_12544.sh (186de045…): when ob_v3 exits it runs t4436 s2e_j2_level9800.py (761b905a…), then adds the s1e log sidecar once PID 932685 has ended, then starts ob_v4_12544.py (88e7f271…, timeout 86400 s).

## 5. Evidence (sha256, full)
- cfg_v2_f196.json: 02fc390a5573e8a79bbce1f54e2a1069b3404d9c86bc265bc3d1aacf1134a4cb
- cfg_v2_g_run2.json: 4591e58f4519ee79034a17c471a482e6a00cc44cf0ea988ba878a4222422c88f
- cfg_v2c_g_run3.json: 993500108e020d5088a4d2216bc3d98ba9b9f198b8a7ab78b8cc70c6b5f7f81f
- tt_v1_level196_test.log: 812c702b07895aa366f61721c3f90544a8729f1b06037ba9632438eef27ffa90
- tt_v1_level196_test.py: 6ceaaa738ceb3665c46e4a8d91de734f78c049810c169fadeb695c7ca0821bfa
- tt_v2_run1_f196_validation.log: 9cb3847b5991ca71ab319815da1135ce1e5063d06e4929201ee9a609445dd859
- tt_v2_twisted_products_eigensolve.py: 98c10b0105bcdd301d531263d107407050335a6f63d3ecd44e8cbfd9b5f3a707
- tt_v2b_run1_f196_validation.log: 67746888c228ecb02ac62b7891dc396557b411c3c7ad7dc688b3b9ac7ecf7fd4
- tt_v2b_run2_g_unarycoset1.log: 00c7f961d0767123d81d549c727c473e8f68c7dbd81b109649f35caa8b58b3bb
- tt_v2b_twisted_products_eigensolve.py: 5fd0929de022f7da4d0f511d8a325534a54be2f7c4ae63e567573be49982e262
- tt_v2c_run3_g_N30000.log: 0accc3832406a0e5aa1267331303a729bfb51d9ed9f04eb18bb4fe1af96f9c2b
- tt_v2c_run4_f_samegens_N30000.log: 571e6c3915e10ffd2d36514b715b55fc39c62789627d206b385b719056c65c06
- tt_v2c_twisted_products_eigensolve.py: 992cb12fe7af5bf454e546dbd6668e0ae48ecc1518ac2a80fa1ae3b2bca01b36
- tt_v3_sturm196_explicit.log: ca1ee83da248867109856bb2f2e31c8687c324d1a92a5b870c345f628969e35b
- tt_v3_sturm196_explicit.py: e3fb3fc88c50354fc6d2459630b9c8a1ae6c022ef62d2ed242182b83c8fb8ac5
- tt_v3b_sturm196_explicit.log: ea512df7dee3c25759fcceb7227ce4b754de1af9b1de9308175cb26f7c62d8b3
- tt_v3b_sturm196_explicit.py: 21fd18fe3c1bd171a7bfd1b68eb5d96ecb78a934993c8a93dba1d51457b878d9
- tt_v4_run1_d343_1372_validation.log: 643627c672b6c970bd990f8c3c43bd3991f5d096fd0bd9e596515755cc80dc82
- tt_v4_run2_g_scan_2a7b_le11000.log: 49019470559ef52a84d1e39184587ddd9b176861e71aaa3945dc4df8e015f107
- tt_v4_run3_g_Xi_scan_oddq_le8000.log: c823d998f253e433e5025c1102afd1b6d8d2543268e74df4b1f4d1c76dcbbfd2
- tt_v4_ternary_genus_eigensolve.py: d30db9b46167113678868e5ff5afb3bb3dcedbeb8d582f9c8147c49f50a92da2
- tt_v4b_run1_validation_and_7168.log: 36c232c3f89bcf65f87f65115e791b060c2a35f8f80fd5a5780cf0990f737109
- tt_v4b_ternary_genus_eigensolve.py: 17511984b02065ca9d0e009473d47dc7beb207abad3ecbcdf680a2bb91a4c94f
- tt_v4c_run1_validation_artefacts.log: d988c05a6e781cdf84cc3eef0f258b35d4fbb83c45c002f077bef8b5f21f9086
- tt_v4c_run1b_validation_artefacts.log: a360bcdfbd02bd25c947593e6d0353278e3df535e10dff4a08c3e70b88695074
- tt_v4c_run2_d5600_3920_N40000.log: d72262e04bab75f102233ce3fd89ef51897120b49242388f7e81f07a283a4092
- tt_v4c_run3_d3920_7168_N40000.log: 8efd84af2951124eeafeae9d9d300c711250a3740f2cc33e56f3b98150a5a6b4
- tt_v4c_run4_d3920_N80000.log: d4f3dfd0123543ea240910aba24654a60667dd2efa4dccababee40f18078bff9
- tt_v4c_run5_d7168_N80000.log: 01bd839def9b648d71aad8e533c2d8009fc9e5de2ad673e62df6b819398d5f46
- tt_v4c_ternary_genus_eigensolve.py: 9dd3b5f33ae7c4d391c6caf99d06c09d89752f8ef4fa79897cd01eaed1df249b
- tt_v5_TT1_independent_verify.log: e11397ce999e33091e69b17f1a46ef03143eb52f12f27bc20510812b72c00a64
- tt_v5_TT1_independent_verify.py: 749c37daddc8172d0dc97d3ac970628073254adc4cdae55f78beaf62c01f5400

Sidecar check at writing: 32 OK, 0 failed. Note: tt_v2_run1 and tt_v3 logs are crashes (no elldata on box; matrref not a GP function); tt_v4c_run1 log is a failed spawn (script did not exist yet); all kept.

## 6. Usage
96.1% of the weekly limit at 22:41 CST (resets Tue Nov 10, 09:49 CST). Earlier: 89.6% (21:58), 87.8% (21:45).
