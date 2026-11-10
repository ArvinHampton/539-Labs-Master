# FINDINGS — Auditor CONFIRM · PR2 R1–R5 ABSENT-final / REJECT Φ OWNER_WRITE (t48s1) — 2026-10-25 ~21:36 CDT (America/Chicago)
CONFIRM-only. No physics invented; tip not edited; no messages sent.

## Verdict: **MATCH-with-SF**

## Recomputed sha256 (Auditor box)
| Item | Claimed | Recomputed | Result |
|---|---|---|---|
| OWNER_WRITE `quantum-comp/reports/OWNER_WRITE_PR2_R1R5_ABSENT_FINAL_REJECT_PHI_t48s1_2026-10-25.md` | 6ebca69d…eb41 | 6ebca69da1973aac62655faf95c38b5662801b3c8c48f9b1f03eaee9c8e2eb41 | MATCH |
| Catalog v0.5.10 `/workspace/obs-data-PR2-COSMO-BIO-NEURO.md` | 684e1195…353d | 684e1195cb19b0a31c2092b82b7e85e25435a89de0965d13f7464c5cb43e353d | MATCH |
| Backup v0.5.9 `obs-data-PR2-COSMO-BIO-NEURO.pre-v0510-fe7307cb.md` | fe7307cb…021f | fe7307cb72226000e10685103e5ffe7ce48b0c05e29d01c985a33296f626021f | MATCH |
| Wave-4 FINDINGS | 1726b6ad… | 1726b6ad44afb6913d9e149183c6782c477e1aab56be1ce5fae1bb1d021fecc7 | MATCH |
| Prior Auditor CONFIRM t2115u | 050d5b64… | 050d5b6430327a12ee23f3a28f5b7dc2c4cba75bc8919566524116dc008d8b89 | MATCH |
| Live tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | LOCK 788defed… | **d5f8b9d33e855d85c4792325d9aa11714bc61e21c6856893fbb355e18ae00c04** (mtime 21:33:53 CDT) | DRIFT (Soft SF) |

## Catalog diff v0.5.9 → v0.5.10
- Changed only: header line 2 (version/label), §7 Boundaries (+5 R1–R5 pointer lines), new §14 changelog.
- §2–§4 (lines 19–130) byte-identical to backup: **VERIFIED**.
- Content is status/pointer only: I1, I2 (Γ_PBH, Γ_★, Γ_E, S_rev, λ, α), W4.3 map = ABSENT-final; Ecosmos Φ (`21ecbd40`) REJECTED as Author Write; Bridge PARTIAL / READY NO; no Cat A; DESI FORCE blocked. **No rates, values or I1–I3 content invented or imported.**

## Tip
- tip_touched by PR2: **NO** (verified). Backup `residual-c-field-WRITTEN_PREMISES_DRAFT.pre-1m-match-relabel-788defed.md` = 788defed… (MATCH to LOCK). Diff 788defed → d5f8b9d3 = 2 lines in §1m only (heading + Status), relabeling "pending Auditor re-CONFIRM" to cite Auditor t2131u MATCH-with-SF `3b01ef79…`. That's an MR2 §1m relabel, label-only; no PR2/t48s1 text; no numbers.
- The Write's own drift note (90bbf508 → 788defed, other lane) is consistent with on-disk backups.

## Soft SF
1. **SF-TIP:** brief LOCK 788defed… is stale. Live tip = d5f8b9d3… (MR2 §1m label-only relabel at 21:33:53 CDT, not PR2). Re-bind the tip LOCK to d5f8b9d3….
2. **SF-AUTH:** the Owner's PR2-widget t48s1 words ("Yes — Approve all R1–R5; apply ABSENT-final / REJECT Φ to catalog under Author powers") **cannot be verified from the Auditor box**. They're quoted only inside the Write. The separate APPROVE-ALL for the seven rec packs (~21:32 CDT) doesn't by itself cover this Write.

No FAIL conditions: all hashes match, §2–§4 are unchanged, PR2 did not touch the tip, and nothing was invented.
