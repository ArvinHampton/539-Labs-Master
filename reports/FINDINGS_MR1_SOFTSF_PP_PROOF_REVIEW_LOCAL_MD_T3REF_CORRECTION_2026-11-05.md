# Soft SF FINDINGS — MR1 proof-logic review: local.md + labs539_ADDITIVE_CORRECTION_T3REF.md
Prepared 2026-11-05 ~16:03 CST (America/Chicago). Soft SF → Professor Proof (lead); copy Local. Owner 15:58: validation = mathematics, not files. Parent usage 77.1% (<90% STOP). No invention, no CERT, no large compute (only tiny identity sanity checks, n ≤ 150 and a ≤ 7). tip LOCK `7cddb188…` untouched; invent HOLD.

Sources reviewed: `local.md` sha `d1488dff…`; `labs539_ADDITIVE_CORRECTION_T3REF.md` sha `c8e064c7…`.

Status key: PASS · GAP (exact step) · FAIL (counterexample).

## Definition (both files): canonical T3_ref
T(3k)=k, T(3k+1)=4k+2, T(3k+2)=2k+1.
- Step: (4(3k+1)+2)//3 = (12k+6)/3 = 4k+2 exactly. **PASS**
- Step: (2(3k+2)+1)//3 = (6k+5)//3 = 2k+1. **PASS**
- Both files state the same map. **PASS** (consistency)

## C1. T(2)=T(3)=1, so T is not injective (correction file)
Direct evaluation. **PASS**

## C2. Cand-1 on ℕ₀ is false (local.md)
T(0)=0, a fixed point outside {1,2}. **FAIL** for the ℕ₀ statement (counterexample n=0). The refutation stands.

## C3. On n≡1 (mod 3), T increases (local.md)
4k+2 > 3k+1 for k ≥ 0. **PASS**

## C4. Ascending run length = v₃(n+2) (local.md)
Key identity: if n≡1 then T(n)+2 = (4/3)(n+2). Write n+2 = 3^a·m with 3∤m. Each step removes one factor of 3, and n stays ≡1 (mod 3) iff 3 | (n+2). So the run has exactly a steps and ends at 4^a·m − 2. **PASS**
Corollary: for n = 3^a − 2 the run has length a and growth (4/3)^a, so no fixed-L block descent T^L(n) < n works for all n. **PASS** (matches PP's check)

## C5. Cand-1⁺: for all n ≥ 1 the orbit enters {1,2} (local.md)
Assumptions: canonical T3 on ℕ≥1.
- Evidence "all n ≤ 10⁷ converge" is computational (cited Soft SF e7648e07…/PP f1acba95…); not re-run here. It is not a proof.
- **GAP** at the global descent step. No Lyapunov function, covering argument, or averaged-descent lemma is given. Heuristic note only: a branch-weight average log(1/3)+log(4/3)+log(2/3) < 0 suggests descent but is not a proof. Status **OPEN**.

## C6. R_c ≈ 1.5954 via √(2/Λ₀) (local.md item 2)
Arithmetic: √(2/0.7858) = 1.595361. **PASS (arithmetic only)**
Derivation: **GAP** at the Appell–Lerch → R_c equation, which is absent; Λ₀ has no char-0 definition. Classification: **Tier E** (empirical fit), consistent with Owner C §3.

## C7. QI: tree → ℍ² ⊂ ℍ¹¹ exists; constants absent; QI cannot pin R_c
- Existence: standard (regular trees quasi-isometrically embed in ℍ²; cite needed, e.g. Buyalo–Schroeder). **PASS (as literature claim; citation GAP)**
- Specific (λ,ε) or (A,B): **GAP** (absent here; Pack H's ln3 and ln(4/3) not reviewed in this assignment).
- "QI cannot pin R_c": QI constants are non-unique (closed under coarsening), so they don't determine a scalar. **PASS**

## C8. BT tree ↛ ℍⁿ isometrically (local.md "proved/fenced")
Geodesics in ℍⁿ are unique and don't branch; a tree tripod has two geodesics sharing an initial segment and then diverging, which is impossible for an isometric image. **PASS**

## C9. Israel [K]=0 Local map; Bridge C → SM maps (local.md items 4–5)
No proof is offered; these are listed as ABSENT. **GAP** (definitions missing). Nothing to fail.

## Summary
PASS: definition, C1, C3, C4 (+ corollary), C8, C6 arithmetic, C7 non-pinning. FAIL: C2 (ℕ₀ version, n=0) as intended. GAP/OPEN: C5 Cand-1⁺ global descent; C6 derivation (Tier E); C7 constants and citation; C9.
REPORTS ONLY. No CERT.
