# MR2 FINDINGS — DUAL-CONTINUE GAP-FILTR-68 proof-pursuit — 2026-10-27 (America/Chicago)
## STATUS: Soft SF CLOSED — GAP-FILTR-68 CLOSED: w(θ³f) ∉ {6,8} PROVED Soft SF. With parent PARTIAL (w ≤ 10, w ≠ 2,4; odd wts 0), w(θ³f) = 10 under the filtr-invent-pick L14 convention. CANDIDATE (10) "invented pending mathematical proof" — proof now on disk; invent-pending ELIGIBLE TO DISCHARGE (Auditor/Eigen Rule 5 review pending). Katz 40 PARALLEL unchanged, not worked. OW c3288fbf… STANDS; no Owner pick.
REPORTS ONLY. No RECS. Kerr BLOCKED. No tip fold. No new invent (HARD GATE: proof-pursuit only).

## Locks (verified on disk 2026-10-27 12:4x CDT)
- tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md BEFORE 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 / AFTER 7cddb188…dfc91 — MATCH. tip_touched NO.
- Token OW OWNER_WRITE_TOKEN_USAGE_HARD_STOP_REMOVED_VISIBILITY_ONLY_2026-10-27.md d622e0a87112f1b50655f7c9495e1fe0e1b150dc1e6b02356d678322af14f29d — MATCH.
- Invent-lift OW OWNER_WRITE_INVENT_BAN_LIFTED_ALL_LANES_PURSUE_FREEDOM_RIGHT_AUTHORITY_2026-10-27.md on-disk 37b8298b15f469044a1257aa4974ada4a4b6bc7c2d45b10c98483c39e446c41f — MISMATCH vs standing 2050914c…; MATCH brief's churn value 37b8298b…. Continued under on-disk.
- Filtration OW OWNER_WRITE_FILTRATION_CONVENTION_BOTH_NAMED_PARALLEL_2026-10-26.md c3288fbfdb3c9c0952eaecb950e0dc67642dba712d550e744c8bcebedc5aa43a — MATCH.
- HARD GATE OW 878631bd…; label OW c9dd3a0a…. Parent FINDINGS d760f4f8dc7b317cbee55cf4e51f8e92ef7adda79cdf64e58cbdc179abd59c62 MATCH; parent script 1647b1ca… MATCH.

## Proof (Path A, computational; script MR2_gap_filtr_68_check_2026-10-27.py sha 0bec69fbd0dccb9808dd63a8b17743eb2dd7c074ad771b9bbf72f9f0736512f9)
1. dim M_k(Γ₀(7)): genus 0, 2 cusps, ε₂=0, ε₃=2 ⇒ dim M_k = 1 + 2⌊k/3⌋ (k ≥ 2 even): M_2=1, M_4=3, M_6=5, M_8=5, M_10=7. (Brief's "⌊k/3⌋+1" is not the Γ₀(7) value; parent's wt-2/4 dims 1,3 agree with this formula.)
2. Integral generators added: weight-3 η-quotients with character (·/−7): h=(η(z)η(7z))³, u=η(z)⁷/η(7z), v=η(7z)⁷/η(z) (Ligozat orders ≥0 at both cusps; integral q-expansions); their pairwise products (trivial character, wt 6), plus g³; wt 8 adds g·(wt-6 set), g²·(wt-4 set).
   Note: E6 ≡ 1 mod 7 (504 = 7·72), so parent's wt-6 set lost rank mod 7 — cause of rank 4.
3. Mod-7 ranks on 120 coefficients: wt 6 rank 5 = dim M_6, augmented by θ³f rank 6; wt 8 rank 5 = dim M_8, augmented rank 6. (Parent's wt-8 rank 5 already equalled dim M_8 = 5; the gap at wt 8 was only that the dim was not stated.)
4. The span of integral forms reduced mod 7 lies in M_k(Γ₀(7),Z)⊗F₇, which has F₇-dim = dim M_k (q-expansion principle). Rank = dim ⇒ span = full space. θ³f mod 7 is outside it (rank jump; non-membership on finitely many coeffs is rigorous). Hence w ∉ {6,8}.
5. Combined with parent: w ≤ 10 (Sturm), w ≠ 2,4, odd wts trivial, w ≠ 0 (θ³f nonconstant, a₀=0). ⇒ w(θ³f) = 10.
- Path B (Hasse / filtration ≡ k mod p−1 at Γ₀(p)): not needed; not pursued; no lit cite relied on.

## Invent label
CANDIDATE (10): statement now carries a Soft SF proof on disk; label "invented pending mathematical proof" may DISCHARGE once Auditor/Eigen Rule 5 accept. Until then STANDS NOT OPERATIVE. Katz 40 PARALLEL (different ambient) untouched.

## Carried
GAP-FILTR-68 CLOSED (this file). INV-Ind PROVED; GAP-SG-K1 CLOSED; β↔ρ CLOSED; GAP-SK-p3-1 OPEN; OPEN-SK-p3 OPEN; Kerr BLOCKED; tip LOCK.
