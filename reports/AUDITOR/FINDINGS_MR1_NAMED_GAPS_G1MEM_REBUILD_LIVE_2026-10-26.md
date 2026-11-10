# FINDINGS — MR1 Named Gaps — G1-mem Rebuild LIVE (Soft SF, write-only)
Date: 2026-10-26, snapshot 21:40 CDT (America/Chicago). Author: Math Research 1 executor.
Authority: Physicist CONTINUE Soft SF named gaps → Auditor; OW blanket sha256 9b993a72bcdfed3fe2d78c15cbe76d0c8197958ca5ac60111546cd5e7ec6498b.
NO RECS. No invent. Kerr BLOCKED. Mesh CANCELLED. tip_touched NO.

## STATUS: **G1-mem OPEN / GAP STANDS** — G1 NO promote.

## Cites
- Eigen G1MEM `EIGEN-TE-RHOBAR-N36-G1MEM_2026-10-26.md` live sha256 d768dbd926715938f952851947680790589892359c31865634abdb7c27fab29d (unchanged; P1/P2/P3 ABSENT; G1 NO promote).
- Prior Soft SF (cite only): G1-mem/G-PATH-A 27dd3cc3…eddc3; Alt B d2bd5c9f…a77; Lit L3/G3 c88aae9c…702; Card1F Step3 cf59ba13…6ad; G-BASIS-89 CORRECTION 243f9cc5…adf.
- Side: G-PATH-A still OPEN (f0f61da0…); no re-audit.

## Rebuild LIVE (`/workspace/grok-batches/eigen-n36-503/`)
- `rebuild_e1_extra_watch.log/.out` (mtime 21:39): REBUILD_E1_START 21:03:12 CDT primes = 7867441 7872341 7873321 7875281 7876261 7885081.
- OK e1 p=7867441 at 21:08:12 CDT; since then "wait solve42g for e1 p=7872341" every 90 s (last 21:39:42 CDT). 1/6 rebuild primes done.
- Driver `rebuild_e1_extra_then_crt.sh` PID 2815455 LIVE.

| e1 sobj | sha256 |
|---|---|
| n36wz_modp_m7_p7840981_e1.sobj | 638d0a6f4fa42649cacdda5be0024f1913ddbe0c5fb6990aac97019258b8488f |
| n36wz_modp_m7_p7851761_e1.sobj | a98e3658bc992dead31a02dad8d3db91217621b6bd99527ef423273ddfeedb84 |
| n36wz_modp_m7_p7860581_e1.sobj | 951c3583e89bcad2869d58927b826d2d443e247649bd03d1c0f2f77d089f1f70 |
| n36wz_modp_m7_p7863521_e1.sobj | 90b9c05d3d033d3640dfbc687a00654944df7e7af9c4202fcc12b4ab8a39a632 |
| n36wz_modp_m7_p7864501_e1.sobj | 136444874e0e1127b74c9570cb8c59b6726afbcf9e83c8c894fc242d1df972cf |
| n36wz_modp_m7_p7867441_e1.sobj (NEW, rebuild) | ddb071f03bfa2951fd986d78f4f8ceafda09f4cc84be9169702eb819a622d3b2 |
| n36wz_modp_m7_p7946821_e1.sobj | 28a6e68faf9795beeaf1a733aa398c5c86660a584afe7c9b82d78471db949670 |

e1 primes FOUND: 7. ABSENT (rebuild queue): 7872341, 7873321, 7875281, 7876261, 7885081.

## Processes (pgrep only; nothing started/killed)
- PID 2673289: GONE.
- solve42g LIVE: `resume_solve42g_serial.sh` PID 2816202; `solve42g.sage.py 6 1027606441 7` PIDs 2886173/2886226 — still blocking the e1 rebuild.

## CRT / P2
- `crt36z_auto.log` (19:26 CDT, pre-rebuild, 6 primes excl. 7867441): entries 5091737, recon_ok+holdout 539, no_recon 1995671, holdout_fail 3095527 → FAIL.
- `ARTIFACTS_CRT.sha256` lists only QQ m7 crt6 / n36w modp artifacts; no Q(ζ49) Kr CRT artifact on disk. **P2 ABSENT.**
- Zero-polar char-0 check: **ABSENT** (none found).
- P1 (multi-prime e1 set sufficient for reconstruction) not closed; P3 ABSENT per Eigen.

## Tip
`/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` tip_pre 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91; tip_touched NO.
