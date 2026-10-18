> **Master-copy notation note (added 2026-10-18 at push; report text below is otherwise verbatim).** Bold W in this report is the unit stabiliser, unrelated to W_P. §3A (general proof of S₀ = ψ(W)) supersedes the 'B for general s' sentence in §3. PARTIAL_notes.md is an interim note kept for provenance. Category convention for Master (rev. 5): Cat A = proved, or exact (including exact finite computation); floating-point-only results = Cat B. Naming as in rev. 4: W_P = Fix(P); V_Eis/d_Eis = Eisenstein span/dimension; Theorem G = Lewis–Zagier; Lemma Prod1/Prod2; d_2(k,v). No 'Theorem L' label is introduced (Theorem L = the framework's Parity Dominance Theorem; Lemma L keeps its name). Erratum: ERRATUM_Consolidated_Rev5_2026-10-18.md. Consolidated statement: Bridge_C_Consolidated_rev5_2026-10-18/ (§13). No TPC/RH claim; distinct from HQCC termination claims; CORE_FREEZE holds.

# u_L criterion: closure (ambiguous-class proof, coverage, coset property)

Date: 2026-10-18, written about 15:10 CDT. Local only: nothing pushed, GitHub not touched. Builds on `2026-10-18-Cusp-Onset-Closure.md` (A1, A3) and `2026-10-18-Open-Algebraic.md` (item 6).

Labels: **Cat A** = proved, or an exact finite computation. **Cat B** = floating-point, a pattern, or a conjecture. No TPC/RH claims.
Naming: W_P = Fix(P); d_Eis = the Eisenstein dimension. Below, **W** (bold, no subscript) is the unit stabiliser of §3. It is unrelated to W_P.

Folder: `2026-10-18-uL-Criterion-Closure/`. The file list is in §5.

## 0. Status

| Item | Result | Status |
|---|---|---|
| 1a. Ambiguous count \|Ḡ^σ\| = 2^{ω(s)}φ(s−2): odd s, s(s−2) squarefree | Proved two ways: (i) Chevalley's formula in its ray-class form, with unit-norm index 1; (ii) a direct genus-theory δ-computation | **A** (uses the classical theorems of Chevalley and Gauss genus theory) |
| 1b. Squarefree criterion | Eis ⇔ h(Q(√(s(s−2)))) = 2^{ω(s)}. Number of non-genus characters = φ(s−2)(h − 2^{ω(s)}). Also proved: S = ker(Cl⁺_M → Cl⁺_{P₂P_m}), x̄ = 0, and only the coprime c-part occurs | **A** (now a theorem; was B) |
| 1c. Exact cross-check of 1a/1b | 47 values of s ≤ 151: every identity holds. Eis only at s = 5, 7, 13, 15 | A per s |
| 2. s = 32, 34, 36, 40 | Coprime parts complete at B = 200000 by enumeration, and identical to the bound-free exact sets. **All four are CUSP** | **A** |
| 2. s = 24 mixed-prime parts | **None exist, for any exponents**: every admissible β has v_{P₁₁}(β) = v_{P₁₁}(D′) | **A** (local proof, exact) |
| 2. s = 24 (1,12), (12,1) | Both non-empty, 32 classes each (2 S₀-cosets), genus-pure. The same holds for (1,16) and (16,1) | **A** |
| 3. Coset property | Lemma: T_𝔠 + ψ(**W**) = T_𝔠 for every 𝔠. So the property holds for **all c-parts at once** whenever S₀ = ψ(**W**) | Lemma **A** |
| 3. S₀ = ψ(**W**), global exact check | Holds at every s = 5..44 | A per s |
| 3. Local condition R_p = **W**_p, all s and all p | **Proved in general** (§3A, added 17:50 CDT): it reduces to "ratios of exact-valuation elements of β₀+L lie in the multiplier order of L". The cases checked are p ∤ f, odd p \| c with p \| s or p \| s−2, and p = 2 for s odd, s = 2t with t odd, t ≡ 2 mod 4, and t ≡ 0 mod 4 | **A** |
| 3. Coset property for every s and every c-part | Follows: S₀ = ψ(**W**) for all s | **A** |
| 3. Full u_L verdict, all (infinitely many) c-parts | **Eis** at s = 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 20, 24, 28. **CUSP** at every other s in 5..44 | **A** |

## 1. Ambiguous-class count and the squarefree criterion (Cat A)

**Setting.** Let s be odd with D = s(s−2) squarefree, and m = s−2. Then:
- D ≡ 3 mod 4, K = Q(√D), O = Z[√D], c = 1.
- The ramified primes are P₂, P_p for p | s, and P_q for q | m. So t = 1 + ω(s) + ω(m).
- ε = s−1+√D is fundamental (y = 1 is minimal in x² − Dy² = 1, and norm −1 is impossible mod 4). N ε = +1, so h⁺ = 2h.

**Step 1: the admissible set.**
- With c = 1 the lattice Λ = 2Z + (s+√D)Z equals P₂. So L = dΛ = 2mP₂ = P₂³P_m².
- β₀ = β(s,−2) = −2√D, and D′ = (β₀, 2d, d(s+√D)) = P₂²P_m.
- Every β ∈ β₀ + L has v_{P₂} = 2 and v_{P_q} = 1 exactly. **So only the coprime c-part occurs.**
- Writing β = β₀(1+z) with z ∈ P₂P_mP_s⁻¹, we get T₀ = t₀ + ker(Cl⁺_M → Cl⁺_{P₂P_m}).
- Hence S = ker(Cl⁺_M → Cl⁺_{P₂P_m}) and Ḡ = Cl⁺_{P_m∞∞}/⟨j⟩.
- Cl⁺_{P_m} ≅ Cl⁺_{m}, since (O/P₂)^× = 1 and ε ≡ 1+√D kills the additive part. Both have order 2hφ(m).

**Step 2: x̄ = 0.**
- D′ is ambiguous, so σ𝔞 = 𝔞·(β̄/β).
- β̄/β is totally positive and ≡ −1 mod every P_q (σ√D = −√D, and v_{P_q}(β) = 1).
- So σt₀ − t₀ = [(−1 mod P_m, ++)] = j, i.e. x̄ = 0.

**Step 3a: the count via Chevalley.** Take Chevalley's ambiguous class number formula for K/Q with modulus 𝔪 = m∞ (Gras's ray form):

 |Cl⁺_m(K)^σ| = |Cl_{m∞}(Q)| · ∏_{v∤𝔪} e_v / (2 · [E_{Q,𝔪} : E_{Q,𝔪} ∩ N K^×]).

Evaluating each piece:
- |Cl_{m∞}(Q)| = φ(m).
- ∏_{v∤𝔪} e_v = 2^{1+ω(s)} (the primes 2 and p | s).
- **Unit-norm index = 1**: E_{Q,m∞} = {x ∈ {±1} : x ≡ 1 mod m, x > 0} = {1}, since m ≥ 3.
- For comparison, the unmodded wide index is [{±1} : {±1} ∩ NK^×] = 2: some prime q ≡ 3 mod 4 divides D, so (−1, D)_q = −1. Also N(E_K) = {1}.

Hence |Cl⁺_m(K)^σ| = 2^{ω(s)}φ(m).

Passing to Ḡ = Cl⁺_m/⟨j⟩: σ fixes j. Take λ ≡ 1 mod m with signs (+,−). Its class u satisfies σu − u = [λ̄/λ] = j. So the connecting map Ḡ^σ → H¹(⟨σ⟩, ⟨j⟩) = ⟨j⟩ is onto, and |Ḡ^σ| = |Cl⁺_m(K)^σ| = 2^{ω(s)}φ(m).

**Step 3b: independent direct proof.**
- 0 → Ū → Ḡ → Cl(K) → 0, where Ū = ((Z/m)^× × {±}²)/⟨(−1,−−),(−1,++)⟩ has order φ(m) and σ acts trivially on it.
- σ acts as −1 on Cl. By genus theory Cl^σ = Cl[2] has order 2^{t−2}, and every ambiguous class is strongly ambiguous: the two counts 2^{t−1}/[±1 : NK^×∩±1] and 2^{t−1}/[±1 : N E_K] are both 2^{t−2}.
- The classes are generated by P₂, P_p and P_q. The relations are (√D) = P_sP_m and (s+√D) = P₂P_s.
- Ambiguous ideals prime to m (P₂, P_p) lift to σ-fixed classes. This gives a subgroup of order 2^{ω(s)}.
- For P_q, write 𝔞 = (γ)P_q⁻¹. Then δ[P_q] = [γ̄/γ] = e_q, the element equal to −1 at q and 1 elsewhere. These elements span 2^{ω(m)−1} in (Z/m)^×/±1.
- So |ker δ| = 2^{ω(s)} and |Ḡ^σ| = φ(m)·2^{ω(s)}.

**Conclusion (Cat A).** This combines the earlier Cat A reduction ("Eis ⇔ (1−σ)Ḡ ⊆ {0, x̄}") with x̄ = 0:
- Eis ⇔ |Ḡ^σ| = |Ḡ| ⇔ **h = 2^{ω(s)}**;
- the number of non-genus pure characters is φ(m)(h − 2^{ω(s)});
- because only the coprime part exists, this decides u_L completely for these s.

The proof relies on published classical theorems (Chevalley's ambiguous class number formula, Gauss genus theory), not on numerics.

**Exact check** (`c1_check.py/.json/.log`), 47 values of s ≤ 151. All of the following hold at every s: |Ḡ| = hφ(m), |Ḡ^σ| = 2^{ω}φ(m), x̄ = 0, only the coprime part, the Chevalley value, and 2-rank = t−2. Eis only at s = 5, 7, 13, 15.

## 2. Coverage

The bound-free exact method (`alg_T.py`, with `T_c_fast`; justification in §3) computes T_𝔠 = {[(β)/(D′𝔠)] : β ∈ β₀+L, β ≫ 0, exact valuations} over finitely many residues mod M·D′𝔠, with no bound B.

It was validated against every earlier enumeration (`validate.log/.json`): all 30 complete coprime parts for s ≤ 44 agree (T and S identical), and all 50 stored deep T-sets are equal. `test_fast.py` confirms T_c_fast = T_c.

**s = 32, 34, 36, 40.** Enumeration with the bound raised to B = 200000 makes every coprime part complete (`enum/enum_s*_B200000.log`). The sets equal the exact ones (`cmp_enum_32_40.json`). All four are **CUSP (Cat A)**:

| s | \|G\| | \|T₀\| = \|S₀\| | \|Ḡ\| | H̄ | non-genus = \|Ḡ\| − \|Ḡ^σ\| |
|---|---|---|---|---|---|
| 32 | 4096 | 64 | 32 | 2 | 16 |
| 34 | 2048 | 16 | 64 | 2 | 32 |
| 36 | 4096 | 32 | 64 | 2 | 32 |
| 40 | 4608 | 32 | 72 | 2 | 36 |

Deep parts at these s (exact, `inc_s{32,36,40}_parts.jsonl`):
- **s = 32:** only P₂², P₂³ occur among 80 tested. P₂² is non-pure, P₂³ is pure. The enumeration at B = 200000 is complete and agrees (`enum/deep_cparts_s32_p2_e3_B200000.json`).
- **s = 34:** no deep part, for any exponents (local check below).
- **s = 36:** 38 non-empty 3-parts among 442 tested. The non-pure ones are exactly those with e₁ + e₂ even (for example (1,1), (2,2), (2,8)).
- **s = 40:** only P₂¹, which is pure (complete at B = 200000).
- The verdict at all four s is CUSP from the coprime part alone.

**s = 24.**
- **No mixed-prime parts exist, for any exponents.** At p = 11 every residue of β₀+L already has the exact valuation v_{P₁₁}(D′) (`local_orbit_5_150.json`: n_good = n_resid = 11). This is a proof, not just a search.
- Among all 323 vectors with exponents up to (8,8,3), the only non-empty parts are (1,e) and (e,1) for e = 2..8. All are pure and each is 2 S₀-cosets.
- **(1,12) and (12,1)**, plus (1,16) and (16,1): 32 classes each, genus-pure, each a union of S₀-cosets.
- (1,12,1), (2,12) and their mirrors are empty (`inc_s24_mixed.jsonl`, `inc_s24_e12.jsonl`).

**Only-coprime criterion.** If n_good = n_resid at every p | M, no deep part exists at that s. This holds for 88 s ≤ 129, including 34 and every c = 1 case.

## 3. Coset property

**Lemma (Cat A).** Define **W** = {u ∈ (O/M)^× : u(β₀+L) ≡ β₀+L mod MO}. Take λ ∈ O with λ ≫ 0, coprime to M and λ mod M ∈ **W**. Then β ↦ λβ maps admissible β with c-part 𝔠 to admissible β with the same 𝔠, because λ preserves valuations at M and MO ⊆ L. Hence T_𝔠 + ψ(**W**) = T_𝔠 for **every** 𝔠, where ψ(λ) = [(λ)].

The facts used:
- B = β₀ + L ⊇ β₀ + MO. This holds because 2cO ⊆ Λ, which also proves the union-of-classes property.
- The class of (β)/I depends only on β mod M·I and on its signs.
- Every β ≫ 0 in B is a unit multiple of exactly one cone point.

**Corollary.**
- If S₀ = ψ(**W**), every T_𝔠 is a union of S₀-cosets.
- If in addition H̄ = 1, the reduction lemma of Cusp-Onset-Closure §4 makes every c-part genus-pure, so u_L is Eisenstein, over infinitely many parts.

**Sufficient local condition.** Let R_p be the ratio set {β/β₁ mod* p^v} of coprime-part residues. Then **W**_p ⊆ R_p always, and R_p = **W**_p for all p ⇒ T₀ is a ψ(**W**)-coset ⇒ S₀ = ψ(**W**).
- For p ∤ [O:Λ], L_p = dO_p and R_p is 1 + (an ideal) or the full unit group. So R_p = **W**_p (proved).
- The bad primes p | [O:Λ] (always p = 2, plus p | c) are checked exactly.

**Results.**
- Global S₀ = ψ(**W**) at every s = 5..44 (`coset_all_5_44.log`, `coset_s*_e0.json`).
- Local R_p = **W**_p at every s = 5..150 (`local_orbit_5_150.json`).
- So the coset property holds for all c-parts at every s ≤ 150 (Cat A per s). For general s it is **B**: no uniform proof at the bad 2-adic and p | c primes.
- Direct checks on computed parts, all exact. Every non-empty part is a union of S₀-cosets, at:
  - s = 9: 64 parts, exponents ≤ 8, all pure;
  - s = 16: P₂ only;
  - s = 24: 18 parts;
  - s = 18, 32, 36 and 40 as well.
- In `inc_s18_parts.jsonl` the third exponent entry is ignored (s = 18 has 2 primes over M). Its "[0,0,1]" row is the coprime part, which is non-pure, as known.

**Full verdicts for s ≤ 44 (Cat A):**
- Eis: s = 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 20, 24, 28. Here H ⊆ S₀ + ⟨j⟩ and S₀ = ψ(**W**).
- CUSP: every other s, because the coprime part is non-pure.


## 3A. General proof that S₀ = ψ(**W**) (added 2026-10-18, about 17:50 CDT) — Cat A

Notation:
- θ = c√D₀, so θ² = s(s−2).
- Λ = 2Z + (s+θ)Z, L = dΛ with d = 2(s−2), β₀ = β(s,−2) = −2θ, and B = β₀ + L.
- The multiplier order A_L = {u : uL ⊆ L} is:
  - Z[θ] for s odd, where Λ = {x+yθ : x ≡ y mod 2};
  - Z[θ′] with θ′ = θ/2 for s = 2t even, where Λ = 2Z[θ′] and θ′² = t(t−1).
- For p | M let v = v_p(M). Then p^vO_p ⊆ L_p, because MO ⊆ L.

**Step 0 (reduction).** Fix β₁ ∈ B with exact valuations at every P | M.
- R_p, the ratio set, is {β/β₁ : β ∈ B_p exact}. **W**_p = {u ∈ O_p^× : uB_p = B_p}, taken mod p^v.
- For u = β/β₁ ∈ R_p we automatically have (u−1)β₁ = β − β₁ ∈ L_p.
- So u ∈ **W**_p ⇔ uL_p ⊆ L_p ⇔ u ∈ A_{L,p} (+ p^vO_p, which is harmless since p^vO_p ⊆ L_p).
- Also **W**_p ⊆ R_p always: u ∈ **W**_p gives uβ₁ ∈ B with the same valuations.
- **Hence R_p = W_p ⇔ every ratio of two exact elements of B_p lies in A_{L,p}.**

Once R_p = **W**_p holds at every p:
- R = ∏_p R_p = **W**, by CRT.
- T₀ = [(β₁)/D′] + ψ(**W**). Ratios of totally positive elements are totally positive, so ψ is defined on them.
- ψ(**W**) is a subgroup, so S₀ = Stab(T₀) = ψ(**W**).
- By the §3 Lemma, every T_𝔠 is then a union of S₀-cosets, for every s and every 𝔠.

T₀ ≠ ∅ always. Exact elements exist at each p (exhibited below, or by CRT on ideals where L_p is an O_p-ideal), and CRT across p glues them.

**Case 1: p ∤ f(A_L)** (A_{L,p} = O_p). The ratio is a unit of O_p = A_{L,p}. ✓

**Case 2: odd p | c.** Then p² | s(s−2), so p divides exactly one of s and s−2. Since p is odd, Λ_p = Z[θ]_p.
- **p | s:** p ∤ d, so B_p = −2θ + Z[θ]_p = Z[θ]_p and D′_p = O_p. The exact elements are Z[θ]_p ∩ O_p^× = Z[θ]_p^× (an element of an order is a unit iff its norm is). Ratios lie in Z[θ]_p^×. ✓
- **p | s−2**, with e = v_p(s−2) = v_p(d) ≥ 2:
  - β = p^e x + (p^e y − 2)θ = θ(w + ηxθ). Here w = p^e y − 2 is a unit, and η = p^e/(s(s−2)) is a p-adic unit.
  - w + ηxθ is a unit of Z[θ]_p, since its norm is ≡ w² mod p.
  - So every β ∈ B_p is θ times a Z[θ]_p-unit. All β are exact, and ratios lie in Z[θ]_p^×. ✓

**Case 3: p = 2, s odd.** D₀ ≡ 3 mod 4 and c is odd, so f(Z[θ]) = c is odd and this is Case 1. ✓

**Case 4: p = 2, s = 2t.** Work with B′ := B/4 = −θ′ + 2(t−1)Z₂[θ′]. Let k = v₂(t−1) and m = v₂(t(t−1)) ≥ 1. Each β′ = 2^{k+1}x + wθ′ with w odd.
- **t odd** (k = m): β′ = θ′(w + 2ε′xθ′), where ε′ is a unit. The bracket has odd norm. ✓
- **t ≡ 2 mod 4** (k = 0, m = 1): β′ = θ′(w + ε′xθ′). Its norm is w² − ε′²x²t(t−1), which is odd. ✓
- **t ≡ 0 mod 4** (k = 0, m ≥ 2):
  - Put η = θ′/2, which is integral since η² = t(t−1)/4 ∈ Z. Let A′ = Z[η] ⊋ A = Z[θ′] = Z[2η].
  - Then B′ = 2(−η + A) = 2·{x + wη : w odd} ⊆ 2A′, and B′ contains 2·(A′-units). So D′₂ = 2O₂, and β′ is exact ⇔ β′/2 ∈ A′^×.
  - Take β′/2 = x + wη and β₁′/2 = x₁ + w₁η (w, w₁ odd), and let u = u₀ + u₁η ∈ A′^× be their ratio. The η-coefficient of u(x₁ + w₁η) is u₀w₁ + u₁x₁ ≡ 1 mod 2.
    - If η² is even, units of A′ have odd constant term, so x₁ and u₀ are odd. Hence u₁ ≡ 0.
    - If η² is odd (m = 2), units have x + w odd, so x₁ is even. Hence u₀ is odd, and since u₀ + u₁ is odd, u₁ is even.
  - Either way u ∈ Z[2η] = A. ✓

**Conclusion (Cat A, all s).** R_p = **W**_p for every p | M. Hence S₀ = ψ(**W**) and the coset property holds for every s and every c-part. Combined with H̄ = 1 and the reduction lemma, **the u_L verdict is decided by the coprime part for every s**. Eis ⇔ H̄ = 1 holds in general (Cat A), given the earlier Cat A reduction of A1.

This agrees with the exact checks: global at s = 5..44, local at s = 5..150.

## 4. Still open (B)
- (Closed in §3A: R_p = **W**_p for all s.)
- A closed criterion (h-type) for non-squarefree s(s−2) and for even s. H̄ is computed exactly per s but has no formula.
- Running at the time of writing: an enumerative cross-check of the s = 36 3-parts (`enum/enum_deep_s36_p3.log`). It is not needed, because the exact sets are already in `inc_s36_parts.jsonl`.

## 5. Files (`2026-10-18-uL-Criterion-Closure/`)
- **Core:**
  - `alg_T.py` (exact T_𝔠, `T_c_fast`, criterion data);
  - `coset.py` (**W**, ψ(**W**), S₀);
  - `run_inc.py` (incremental per-part output);
  - `local_orbit.py`.
- **Task 1:** `c1_check.py`, `c1_check.json`, `c1_check.log`.
- **Validation:** `validate.py`, `validate.log`, `validate.json`, `test_fast.py`, `cmp_enum.py`, `cmp_enum_32_40.json`.
- **Coverage:**
  - `enum/` (B = 200000 runs: `deep_cparts_s{32,34,36,40}_coprime_B200000.json`, `deep_cparts_s32_p2_e3_B200000.json`, `deep_cparts_s40_p2_e1_B200000.json`, logs);
  - `inc_s{9,16,18,24,32,36,40}_*.jsonl`;
  - `summary_parts.txt`;
  - `coset_s34_parts.json`, `coset_s9_e2.json`.
- **Coset property:** `coset_all_5_44.log`, `coset_s{5..44}_e0.json`, `local_orbit_5_150.json`, `local_orbit_5_150.log`.
- **Notes:** `PARTIAL_notes.md`.
