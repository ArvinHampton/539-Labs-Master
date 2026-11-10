# MR2 FINDINGS — DUAL-CONTINUE filtr invent-then-prove — 2026-10-27 (America/Chicago)
## STATUS: Soft SF PARTIAL — w(θ³f) ≤ 10 PROVED Soft SF; w ≠ 2, 4 PROVED Soft SF; w ∉ {6,8} OPEN (residual GAP-FILTR-68). CANDIDATE (10) stays "invented pending mathematical proof", NOT OPERATIVE. Katz 40 Soft SF-named PARALLEL is unchanged and was not worked.
REPORTS ONLY. No RECS. Kerr BLOCKED. No tip fold. No Owner pick of the filtration. No agent messages.

## Locks
- tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md`: BEFORE 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, AFTER 7cddb188…dfc91 — MATCH. tip_touched NO.
- Invent-lift OW actual sha: 6c97dcadaa70d65036e849b778c99ef6f708e5432794afa10cdc8721de64e39e. This MISMATCHES the brief's 04b2c268…. It MATCHES the parent steering value 6c97dcad…. The work continued under the on-disk HARD GATE.
- HARD GATE: no NEW invent is written. This file is proof-pursuit of the already-invented CANDIDATE (10).
- Parent hygiene: MR2-FINDINGS-DUAL-CONTINUE-filtr-invent-hygiene_2026-10-27.md, 3ccb0b7b640a96a76f8c83300b87da6f0ee40844296af73452fd5262442c2ea2 (MATCH). Lines 3–4 and 18–20 give the CANDIDATE and PARALLEL labels. The convention is in filtr-invent-pick L14: minimal k with θ³f mod 7 ∈ M_k(Γ₀(7)) mod 7, p=N=7.
- Lit: lit/bm/*.txt has no Jochnowitz hit, so this check does not depend on a lit cite.

## Proof pursuit (script MR2_filtr_invent_prove_check_2026-10-27.py, sha 1647b1ca465b08eb27265f9e941064d8e5d635dd1fafa98dcf0c5591a36edbed)
- f = 7.4.a.a. It was rebuilt from E4, E4(7z) and g² (g = 7E2(7z) − E2(z)) using the Hecke checks a4 = a2² − 8 and a6 = a2·a3: q − q² − 2q³ − 7q⁴ + 16q⁵ + 2q⁶ − 7q⁷ + …
- The mod-7 q-expansion of θ³f was compared, to 120 coefficients, against spans built from E4, E6, their 7z-rescalings, g and f:
  - wt 2: rank 1 = dim M_2(Γ₀(7)), augmented rank 2. NOT in the span, so w ≠ 2 is PROVED. A non-membership found on finitely many coefficients is rigorous.
  - wt 4: rank 3 = dim M_4(Γ₀(7)), augmented rank 4. NOT in the span, so w ≠ 4 is PROVED.
  - wt 10: span rank 6, augmented rank 6. θ³f IS in the span on 120 coefficients. The Sturm bound for weight 10 on Γ₀(7) is 10·8/12 < 7 ≪ 120, so the congruence holds identically. This PROVES w ≤ 10.
  - wt 6: span rank 4, augmented rank 5. wt 8: span rank 5, augmented rank 6. Both are "not in the span", but these spans are not shown to equal all of M_6 / M_8 mod 7. So w ∉ {6,8} is NOT proved. Residual GAP-FILTR-68.
  - Odd weights are 0 on Γ₀(7) with trivial character.
- GAP-FILTR-68 would also close if one proved, on Γ₀(p), that the filtration is ≡ weight mod p−1 (that is, 10 ≡ 4 mod 6, which would exclude 6 and 8). That Hasse-type argument at level p = N is not proved here.
- Structural note (correlation only): a_n·n³ mod 7 is a twist by the Legendre symbol (·/7), since χ_cyc³ ≡ (·/7) mod 7.

## Invent label
CANDIDATE (10) keeps the label "invented pending mathematical proof" and is NOT OPERATIVE. If GAP-FILTR-68 closes, the remaining statement is w = 10. Katz 40 stays Soft SF-named PARALLEL, in a different ambient. OW c3288fbf… stays locked pending an Owner pick.

## Carried
INV-Ind PROVED (42227d2f…); GAP-SG-K1 CLOSED (70644418…); β↔ρ CLOSED (a93a7677…); GAP-SK-p3-1 OPEN; OPEN-SK-p3 OPEN; Kerr BLOCKED; tip LOCK. NEW OPEN: GAP-FILTR-68.
