# FINDINGS: PP audit of Local O1/O2 (Weil vector carrier, +1 Fricke law, Weil(140)↔Γ₀(49) dictionary). 2026-11-09 (America/Chicago)
Agent: Professor Proof (Soft SF). GO (2) under OW 5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c.
This file is additive; the audited file is not modified. Tip 7cddb188… is untouched. No CERT. No outside service; no LMFDB query was needed.
Scripts and logs are in /workspace/audit-scratch/pp_local_weil_1520/:
- a_num.py (mpmath, 60 digits)
- b.gp and c.gp (PARI 2.17.2)
- d_weil.py and d7.py (explicit 140-dimensional Weil representation)

## 0. Target
- FINDINGS_LOCAL_DERIVE_XI_WEIL_VECTOR_CARRIER_FRICKE_PLUS1_DICTIONARY_2026-11-09.md, sha256 ae951f3e7aa5be4b3829cc34fa29ea2d841ff08bff09529b4bf7f4c7effbb091. The sidecar MATCHES.
- Local's rollup is 12/1/3/1, which matches the file.
- **Objects as Local defines them:**
  - **L₁** = ℤ² with Gram matrix [[2,1],[1,4]], so q = x²+xy+2y². This is the norm form of ℤ[(1+√−7)/2].
  - **θ₁** = θ_{L₁} = Σ q^{x²+xy+2y²}. It lies in M₁(Γ₀(7), χ₋₇).
  - **L₄₉** = L₁ ⊕ L₁(7), so θ_{L₄₉} = θ₁(τ)θ₁(7τ).
  - **N₂** = Gram [[2,14],[14,28]] (T:287).
- **Convention used throughout:** W = (0,−1;49,0) and (g|_kW)(τ) = 49^{k/2}(49τ)^{−k} g(−1/(49τ)). This is det^{k/2} normalization, and it is multiplicative: (gh)|_{k+l}W = (g|_kW)(h|_lW). Local uses the same convention (Local l.11).

## (a) W₄₉ on (θ₁², 7θ₁(7·)²)
**Symbolic (PROVED).**
- Poisson summation gives θ_L(−1/τ) = (τ/i)^{n/2} det(G)^{−1/2} θ_{L^#}(τ).
- For L₁ (n = 2, det 7) the lattice is 7-modular: L₁^#(7) ≅ L₁, checked by PARI qfisom(7G⁻¹, G) ≠ 0. So θ_{L₁^#}(τ) = θ₁(τ/7), and θ₁(−1/τ) = (τ/i)·7^{−1/2}·θ₁(τ/7).
- Substituting τ → 49τ and τ → 7τ gives:
  - **θ₁|₁W = −i√7 θ₁(7·)**
  - **θ₁(7·)|₁W = (−i/√7) θ₁**
- Squaring and using multiplicativity: θ₁²|₂W = −7θ₁(7·)², and (7θ₁(7·)²)|₂W = 7·(−1/7)θ₁² = −θ₁².
- So W acts on (θ₁², 7θ₁(7·)²) **exactly as −σ_x, including the factor 7**.
- g₊ = θ₁² − 7θ₁(7·)² satisfies g₊|₂W = −7θ₁(7·)² + θ₁² = **+g₊**.
- The constant term of g₊ is 1 − 7 = **−6**. Its q-expansion begins −6 + 4q + 12q² + 16q³ + 28q⁴ + … (c.log).

**Numerical (PROVED to working precision).** Direct lattice sums at 60 digits, with no use of the inversion formula, at τ = 0.1+0.3i, −0.23+0.41i and 0.37+0.19i:
- θ₁|₁W / θ₁(7·) = −2.6457513110645905905i = −i√7.
- θ₁(7·)|₁W / θ₁ = −0.37796447300922722721i = −i/√7.
- The F₂ (−σ_x) residuals, g₊|W − g₊, θ_{L₄₉}|₂W + θ_{L₄₉}, and θ_{L₄₉}²|₄W − θ_{L₄₉}² are all ≤ 4×10⁻⁵⁹.

The weight-1 law (−iσ_x on (θ₁, √7θ₁(7·)), square −1) also checks. Here W² = −49·I acts by (−1)^k under this normalization.

**Verdict: Local LD-Ξ1(a) and (b) are CORRECT.**

## (b) S₂(Γ₀(49))⁺
- **PROVED (PARI).** dim M₂(Γ₀(49)) = 8, dim S₂ = 1, dim E₂ = 7. S₂ = ℂ·f with f = 49a1 = [1,−1,0,−2,−1]: conductor 49, j = −3375 (CM by ℚ(√−7)), and a_n equal to the mf coefficients.
- **PROVED.** W₄₉ acts on f by **−1**. mfatkineigenvalues gives [[−1]]. Independently, ellrootno(49a1) = +1, and for k = 2 the Fricke eigenvalue is w = −ε = −1.
- **Therefore S₂(Γ₀(49))⁺ = 0 is PROVED.** Local's REFUTED item ("symmetrizing 49a1 gives a nonzero +1 vector") is **correct**: f + f|W = 0, refuted by proof.
- **PROVED.** g₊ ∈ M₂(Γ₀(49)) has cusp coordinate **0** in mfbasis. The basis order was checked: f has coordinates (0,…,0,1). So g₊ is purely Eisenstein (coordinates [0,0,0,0,0,8,−4,0]).
  - This holds exactly: g₊ is modular by (a), and 301 coefficients exceed the Sturm bound of 9.
  - It agrees with Local's orthogonality argument.

## (c) L₄₉ and θ_{L₄₉}²
- **PROVED (PARI).** L₄₉ has rank 4, det 2401 and level 49, where level means the least N with N·Q(L^#) ⊂ ℤ and an even diagonal. The components have levels 7 and 49.
- **PROVED.** L₄₉ is 49-modular in Quebbemann's sense. The definition: L is N-modular if L^#(N) ≅ L, i.e. there is a similarity of norm N from L^# onto L, with Gram N·G⁻¹ ≅ G.
  - qfisom(49·G₄₉⁻¹, G₄₉) ≠ 0.
  - By hand: L₁^#(49) ≅ L₁(7), and L₁(7)^#(49) = L₁^#(7) ≅ L₁, so the two summands are swapped.
- **PROVED.**
  - θ_{L₄₉} = θ₁θ₁(7·) ∈ M₂(Γ₀(49)) (weight = rank/2 = 2; character χ₋₇² = 1), with **θ_{L₄₉}|₂W = −θ_{L₄₉}**. That is (−i√7)(−i/√7) = −1.
  - θ_{L₄₉}² ∈ M₄(Γ₀(49)) has **weight 4** and **W = +1**. This was checked exactly in PARI with mfatkininit on the full M₄ (dim 18) and numerically in (a).
  - θ_{L₄₉}² is the theta series of L₄₉⊕L₄₉: rank 8, 49-modular.
- **PROVED (new; not in Local's file).** The cusp projection of θ_{L₄₉}² is **nonzero**. Its S₄ coordinates are [8/105, 56/15, …], all ≠ 0. Because W preserves the Eisenstein/cusp splitting, this projection is a nonzero element of S₄(Γ₀(49))⁺, which has dim 6 (FINDINGS_PP_DERIVE_P5a_RHOBAR…_1507).
  - So the weight-4 carrier has a genuine +1 **cuspidal** part. The weight-2 g₊ has none.

## (d) Dictionary
### (i) The e₀-character χ₁₄₀
- **PROVED.**
  - N₂ has det −140 and |D| = 140, with level 140 (lcm of the q-denominators).
  - The 7-part is (ℤ/7, −5t²/7): the q-value multisets agree (d7.log).
  - **N₂ is the norm-form lattice of O_{ℚ(√35)} = ℤ[√35].** x²+14xy+14y² and x²−35y² reduce to the same form Qfb(1,10,−10), so they are properly equivalent.
  - This ties N₂ directly to Reg(ℚ(√35)) and therefore to Λ₀.
- **PROVED for the tested elements (exact up to float rounding).** I built an explicit 140×140 Weil representation with sign 0: ρ(T) = diag e(q), and ρ(S) = |D|^{−1/2}(e(−(γ,δ))).
  - Checks: unitary, S² = (e_γ ↦ e_{−γ}), (ST)³ = S², ρ(S) = S, and a homomorphism test.
  - For 25 random γ ∈ Γ₀(140) (c = 140m, |d| ≤ 300), ρ(γ)e₀ = (140/d)e₀ holds **25/25**.
  - Control: for γ = (1,0;70,1) ∈ Γ₀(70)∖Γ₀(140), e₀ is **not** an eigenvector.
- **CONDITIONAL (literature: Bruinier, LNM 1780, Prop. 1.x; Borcherds).** The general statement for all γ ∈ Γ₀(140) is the standard formula χ_L(d) = ((−1)^{(b⁺−b⁻)/2}|D| / d) = (140/d).
- Local's label "PROVED (numerically on 9 elements; standard)" mixes evidence. Numerics alone are not a proof. **Relabel:** CONDITIONAL (standard theorem) with numerical confirmation, now 25 + 9 elements.

### (ii) W₄₉ does not descend to level 140
- **PROVED.** W₄₉ is not an Atkin–Lehner operator of Γ₀(140), since W_Q needs Q ‖ N and 49 ∤ 140. The only Atkin–Lehner operator at 7 on Γ₀(140) is W₇ (7 ‖ 140). Local does not discuss it.
- **Local item 4 has a gap, but its conclusion is PROVED here by a stronger argument.**
  - Local shows that WγW⁻¹ mod 140 is not determined by γ mod 140. That alone does not exclude an intertwiner A with ρ(WγW⁻¹) = Aρ(γ)A⁻¹ on Γ₀(49).
  - **PP proof:** take γ = T ∈ Γ₀(49), so WTW⁻¹ = (1,0;−49,1) ∈ Γ₀(49).
    - |tr ρ(T)| = |Σ e(q)| = √140 = 11.8322 (Milgram).
    - |tr ρ((1,0;−49,1))| = 31.30495 = 2·√5·7. This is because the matrix is the identity mod 7 and unipotent mod 4 and mod 5.
  - The traces differ, so ρ∘Ad(W) ≇ ρ on Γ₀(49). Hence **no operator ρ(W) on Weil(N₂), even a projective one, extends ρ|Γ₀(49) to Γ₀(49)⁺.**
  - **Relabel item 4:** the conclusion is PROVED (by PP), and Local's argument as written is insufficient.

### (iii) Level 980
- **PROVED.** lcm(49,140) = 980 = 2²·5·7². Γ₀(49) ∩ Γ₀(140) = Γ₀(980), because c ≡ 0 mod 49 and mod 140 ⇔ c ≡ 0 mod 980.
- **PROVED.** The Fricke matrix (0,−1;49,0) does **not** normalize Γ₀(980). Counterexample: W T W⁻¹ = (1,0;−49,1) ∉ Γ₀(980).
  - At level 980 the 49-involution must be the Atkin–Lehner W₄₉^{(980)} (49 ‖ 980), a different matrix.
  - That it acts on level-49 oldforms as level-49 Fricke is CONDITIONAL (Atkin–Lehner / Atkin–Li compatibility, literature).
- **OPEN.** Whether 980 is necessary, i.e. minimal, is OPEN. "Joint carrier" is not defined, and Γ₀(980) is only the common refinement (sufficient).
- Local's "Any joint carrier lives at level 980" is an **overclaim**. Local's own LD-Ξ3 joint object f⊗χ₁₄₀ lives at level 19600, not 980. **Relabel:** OPEN.

## Scan of Local's other labels
| Local item | Local label | PP audit |
|---|---|---|
| §0 fundamental unit; Λ₀ = √(7/8)L(1,χ₁₄₀) | PROVED | Agree. Certified via bnfcertify in FINDINGS_PP_AUDIT_MR1…_1516 (66a69888…). |
| §1 49a1 sign −1 | PROVED | Agree (mfatkineigenvalues; ellrootno). |
| §1 symmetrization +1 vector | REFUTED | **Agree.** Correct refutation by proof. |
| LD-Ξ1 (a), (b) incl. g₊ Eisenstein, (c) | PROVED | **Agree.** All re-proved symbolically and exactly. |
| LD-Ξ2 induced carrier | CONDITIONAL | Agree. Tautological by construction, as Local says. |
| LD-Ξ3 twist: f⊗χ₋₇ = f, level 19600, Fricke +1 | "PROVED by citation" | **Upgrade to PROVED by computation.** elltwist(49a1, −20) and (…, 140) both have conductor 19600 and ellrootno −1, so Fricke w = +1. The −7 twist has conductor 49 and a_p equal to 49a1's for p < 200. |
| Dict. 1 decomposition; 3 image SL₂(ℤ/20)×B(𝔽₇); 5 fields | PROVED | **Agree.** Item 3 is by CRT, since Γ₀(49) is the preimage of B(ℤ/49). Item 5: 35·(−7) = −5·7². |
| Dict. 2 χ₁₄₀ | PROVED (numeric + standard) | **Relabel to CONDITIONAL** (standard theorem) with numerical confirmation. |
| Dict. 4 ρ(W) fails | PROVED | **Conclusion PROVED by PP (trace argument). Local's argument has a gap.** |
| Dict. 6 bridge (49 = \|d_K\|·N𝔣) | PROVED | The 49a1 data (conductor 49, CM j = −3375) are PROVED. The general CM conductor formula is CONDITIONAL (literature). |
| Dict. 7 "any joint carrier at 980" | (in failures list) | Overclaim; **OPEN** (see iii). |
| OPEN items (weight 3/2, 2- and 5-parts, √(7/8)) | OPEN | Agree. |

## Rollup (PP audit items)
- **PROVED 16:**
  - (a): weight-1 law; −σ_x exact incl. 7; g₊ = +1 with constant −6.
  - (b): S₂ = ℂ·49a1 with W = −1; S₂⁺ = 0; g₊ Eisenstein.
  - (c): rank/det/level; 49-modular; θ_{L₄₉} W = −1 and θ² W = +1 at weight 4; cusp projection of θ_{L₄₉}² nonzero in S₄⁺.
  - (d): N₂ ≅ norm form of ℤ[√35]; W₄₉ not Atkin–Lehner at 140; no intertwiner (trace); Γ₀(980) = intersection with lcm 980; Fricke matrix does not normalize Γ₀(980); LD-Ξ3 by computation.
- **CONDITIONAL 3:** the χ₁₄₀ e₀-character for all of Γ₀(140) (theorem cited; 25/25 checked); W₄₉^{(980)} compatibility on oldforms; the CM conductor formula.
- **OPEN 2:** minimality of 980; the undefined "joint carrier".
- **REFUTED 0 new.** Local's single REFUTED item is confirmed.
- **Relabels recommended to Local: 4.** Dict. 2 → CONDITIONAL; Dict. 4 argument gap (conclusion PROVED by PP); LD-Ξ3 → PROVED by computation; Dict. 7 "level 980" → OPEN.

## Verdict
Local's carrier mathematics is correct.
- Fricke acts on (θ₁², 7θ₁(7·)²) exactly as −σ_x. g₊ = θ₁² − 7θ₁(7·)² is a nonzero Fricke +1 form with constant term −6. It is purely Eisenstein, because S₂(Γ₀(49))⁺ = 0 (49a1 has W = −1).
- L₄₉ is a 49-modular rank-4 lattice. θ_{L₄₉}² is a weight-4 Fricke +1 form with a nonzero cuspidal part, so it is the first carrier here with a genuine +1 cusp component.
- The dictionary holds:
  - The e₀-character is χ₁₄₀ on Γ₀(140). It is verified on 25/25 elements, with the general case cited.
  - N₂ is the norm-form lattice of ℤ[√35].
  - No Fricke operator can be added to Weil(N₂), now proved by a trace mismatch rather than Local's incomplete descent argument.
- Four labels need tightening, most importantly that "level 980" is a sufficient common refinement, not a proven minimal level.
