# PR1 FINDINGS — Vanishing Lead Rank 16: tr_C ρ(S)=0 ⇒ dim C⁺=C⁻ (s-family) — 2026-10-26

Report-only. Cite-verify only; invent HOLD (no new numbers/math).

## Locks
- tip Soft SF LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` — cite only; **tip_touched=NO**; **no tip fold**; catalog not edited.
- Soft SF invent HOLD tip fill; Soft SF F3 CLOSED.
- Bridge **PARTIAL / READY NO / NOT Cat A**.

## Sources verified (sha256 computed 2026-10-26 ~11:13 CDT)
| File | sha256 |
|---|---|
| reports/bridges/_git_v8_unpushed_clone/reports/s_family_paths/LEDGER_CatA_clean_v8/LEDGER.md | `dc060d05932a89d05caeb5771d619d54b0a2ee405bef1195b14bdff1fc5bbd31` (MATCH expected) |
| reports/s_family_paths/LEDGER_CatA_clean_v8/LEDGER.md (CI#27 cited path) | `dc060d05932a89d05caeb5771d619d54b0a2ee405bef1195b14bdff1fc5bbd31` (identical) |
| reports/CORPUS_VANISHING_INVENTORY_2026-10-26.md (row 27 = CI#27) | `fb2983460ebadf7c8fe1d934d33ae05d57d725fcbf716933edb7780d273756c0` |
| reports/MERGED_VANISHING_MAP_STUB_2026-10-26.md (row 16) | `b3e0d20ba9d428c0c0315fe27cfe8e5d4929fac2f762c442475b2aab07aa5627` |
| reports/VANISHING_LEAD_ASSIGNMENTS_2026-10-26.md (Q9 14–16; log line 68) | `7adf41080a3f3f4cae6c8a65dfc5faa0c3d2dd10b4b2b54dc751dfa249cb433e` |

## Claim table (verbatim-cited from ledger v8)
| Ledger entry | Kind | Hypotheses | Claim | Status |
|---|---|---|---|---|
| 1 (L25) | Theorem | TB3 | odd s ≥ 5: tr_C ρ(S)=tr_W ρ(S)=tr_E ρ(S)=0, hence dim C⁺=dim C⁻=d_cusp/2 | Cat A Written / VERIFIED-cite |
| 2 (L34) | Certificate | (with entry 3) | s ≡ 4,6 mod 8, 12 ≤ s ≤ 46, E=ρ-span(δ₀): tr_E S=0 ⇒ tr_C S=0 ⇒ dim C⁺=dim C⁻ | Cat A (computer certificate) / VERIFIED-cite |
| 4 (L39–45) | Theorem + Corollary | F1–F5 | s ≡ 0,2 mod 8: tr_E S=0, tr_C S=0 ⇒ dim C⁺=C⁻; Corollary collects entries 1,2,4 | Cat A Written / VERIFIED-cite |
| 8 (L67–72) | Theorem + certificate | F1–F5 | even s: tr_C S = −∏_p t_p; independent Y=Z−SZS certificate for s=8,16,18,24,26,32,40,48,50,56,58 (Y|_C: C⁺→C⁻ iso); **s=10: C=0** | Cat A / VERIFIED-cite |
| 32 (L213) | Theorem | — | s=7: dim C=6, dim C⁺=dim C⁻=3 (via entry 1) | Cat A / VERIFIED-cite (instance) |

CI#27 (corpus row 27) and MERGED row 16 both point to this ledger at sha prefix `dc060d05932a…` and quote entry 1 and "For s = 10, C = 0" — consistent with ledger text. **No CONFLICT** found.

## Rank 16 status
**VERIFIED-cite — Cat A Written** (s-family, conditional on TB3 / F1–F5 as stated in ledger §0). Coverage per ledger: all odd s ≥ 5; s ≡ 0,2 mod 8; s ≡ 4,6 mod 8 only for 12 ≤ s ≤ 46 (certificate range — not a general theorem outside it).

## Backwards
Cat A ledger hygiene / s-family lawspace only. This is a trace/eigenspace-balance statement on the cusp part C = W ⊖ E of the Weil representation ρ_s; it is **not** a vanishing of S_κ(Γ,ρ̄) cusp forms and asserts nothing about modular cusp-form vanishing. No corpus text found linking it to P5a FAIL (ledger has no "P5a" hits); none asserted here.

## Gaps / recommendations
1. Path hygiene OK: corpus CI#27 path `reports/s_family_paths/LEDGER_CatA_clean_v8/LEDGER.md` exists and is byte-identical (sha `dc060d05…bd31`) to the `_git_v8_unpushed_clone` copy. No correction needed.
2. Row label "various s" / "s-family" should carry the scope caveat: s ≡ 4,6 mod 8 covered only for 12 ≤ s ≤ 46 (certificate), and hypotheses TB3 / F1–F5.
3. "CI#27" tag is a corpus-inventory row number, not a ledger entry number; map to ledger entries 1, 2, 4, 8.

Bridge PARTIAL / READY NO / NOT Cat A. tip_touched=NO. No tip fold.
