# SOFTSF PRESS — MR1 PROMOTE CSV provenance re-stamp (Auditor Pack A SF-1) — 2026-10-26
- Class: Physicist packaging resolve (no physics; no exact-ν invent; no tip edit).
- Auditor FINDINGS Pack A SF-1: original Soft SF PRESS MR1 PROMOTE listed CSV edit pairs whose claimed pre/post shas did not resolve cleanly on disk.
- tip Soft SF LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` tip_touched NO. Kerr BLOCKED.

## Live CSV paths (operative now)
| CSV | path | live sha256 | sidecar |
|---|---|---|---|
| TE-SIMPSON-FILL-MODP_N18 | /workspace/grok-batches/TE-SIMPSON-FILL-MODP_N18_2026-10-26.csv | `38534aa1102da03cf96d7d76cdd454f8ef0530c4ef12439ec0cbf3c4346010f3` | MATCH refreshed |
| TE-SIMPSON-FILL-SCHEDULE_TORD_N18 | /workspace/grok-batches/TE-SIMPSON-FILL-SCHEDULE_TORD_N18_2026-10-26.csv | `4de5113b477836c6347d33d7142d4dfcdfd001fbb1b32085b62f5b2fabb6976e` | MATCH refreshed |
| TE-SIMPSON-FILL-MODP-N36_N18 | /workspace/grok-batches/TE-SIMPSON-FILL-MODP-N36_N18_2026-10-26.csv | `0e17098c61b5ee7823dad690fa998389a84e504055e599ca31c36a423deacbf2` | MATCH refreshed |

ν=21 and ν=25 FILLED-MODP rows present on all three live CSVs (content checked; packaging only).

## Corrected provenance map (vs original PRESS claimed before→after)
| CSV | claimed pre | claimed post | resolution |
|---|---|---|---|
| MODP_N18 | 533217db… | 453d3c4f… | claimed pre ABSENT on disk; claimed post = promote-era snapshot only at grok-batches/mr1-basis-header-extract/backup_pre_edit/TE-SIMPSON-FILL-MODP_N18_2026-10-26.csv (`453d3c4fc1607465ec37d67c9c13a4963256eaa84fddacee7637508ad3e6ecfd` MATCH claimed post). Live drifted later (GA1 NON-SIMPSON annotation append) → live `38534aa1102da03cf96d7d76cdd454f8ef0530c4ef12439ec0cbf3c4346010f3`. |
| SCHEDULE_TORD_N18 | 8423cb32… | f7ec76ef… | claimed pre ABSENT; claimed post = promote-era snapshot only under backup_pre_edit/ (`f7ec76eff6b8888039e65cac8babaecd47285699fedca6577ca20df3ca2a6ea5` MATCH). Live drifted later → live `4de5113b477836c6347d33d7142d4dfcdfd001fbb1b32085b62f5b2fabb6976e`. |
| MODP-N36_N18 | 20c93d25… | 24fc6122… | both claimed pre and claimed post ABSENT on disk (full-tree search). Live current `0e17098c61b5ee7823dad690fa998389a84e504055e599ca31c36a423deacbf2` (rows for ν=21,25 present; later than promote Soft SF). |

## Interpretation
- Original Soft SF "after" hashes for MODP/SCHEDULE were real promote-era bytes, but those bytes now live only under backup_pre_edit/ (folder name is historical; content matches claimed post, not a further-pre state).
- Live CSVs are strictly newer than the promote Soft SF stamp; sidecars now reaffirm live shas.
- Pre hashes from the original Soft SF are ABSENT — cannot reconstruct pre-edit bytes from disk; marked ABSENT (not invented).
- N36 claimed pre/post ABSENT; live N36 is the operative packaging record.

## STATUS
STATUS MATCH — provenance re-stamped. Pack A SF-1 packaging flag CLEARED by this Soft SF. No tip touch. No CF980 CERT lift. Exact ν Owner-reserved until Eigen Soft SF FINDINGS stands.
