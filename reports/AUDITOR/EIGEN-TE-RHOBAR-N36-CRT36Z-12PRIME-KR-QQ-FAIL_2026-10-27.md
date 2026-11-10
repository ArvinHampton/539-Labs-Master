# EIGEN Soft SF — N36 crt36z 12-prime CRT: Kr QQ FAIL PERSISTS — 2026-10-27 ~13:26 CDT America/Chicago
STATUS: Soft SF FAIL (Kr QQ CRT). NOT CERT. tip Soft SF LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` tip_touched **NO**. Kerr BLOCKED. REPORTS ONLY. No RECS. No invent roots/Kr QQ/ν.

## Trigger REB (rebuild + CRT exited)
- Watcher Trigger REB at 13:26:22 CDT; monitoring from 13:24:35 CDT.
- `rebuild_e1_extra_then_crt.sh` and `crt36z.sage.py` both exited (not running).
- Target sobj ABSENT: no `crt36z.sobj`, no `n36_combo_Kr_rref_QQ_m7_crt12.sobj` (script saves only if fail==0 and hfail==0).
- `crt36z_rebuild.log` written 13:26:16 CDT, sha256 `bca13f10fb2e95286860ad2b0a13de39a44b4023210f3197dbe6fe324704c45e`. No FAIL/SIGSEGV/Traceback/Error line; no SAVED line.

## e1 land (12/12 MATCH mod-p)
Primes (12): [7840981, 7851761, 7860581, 7863521, 7864501, 7867441, 7872341, 7873321, 7875281, 7876261, 7885081, 7946821].
Artifacts: `n36wz_modp_m7_p*_e1.sobj` under `/workspace/grok-batches/eigen-n36-503/` (12 files).

## crt36z 12-prime numbers (Written from crt36z_rebuild.log)
- **entries** = 5,091,737
- **recon_ok+holdout** = **538**
- **no_recon** = 1,996,078
- **holdout_fail** = 3,095,121
- **max height** ≈ **25.3394988669925**
- Recon rate ≈ 1.06e-4 (unchanged order vs 6-prime).

## Compare prior 6-prime FAIL Soft SF (2eb525c5… / EIGEN-TE-RHOBAR-N36-CRT36Z-KR-QQ-FAIL_2026-10-26)
From `crt36z_auto.log` sha256 `a880a774f24f63ff880297eccf1ff5be125a2092e2910705d127be9721d6f4b2` (unchanged Oct 26 19:26):
- primes 6; recon_ok+holdout **539**; no_recon 1,995,671; holdout_fail 3,095,527; max height ≈ 39.17.
- Adding the 6 extra e1 primes from Soft SF NAMED-GAP-REBUILD-LIVE did **not** improve reconstruction; holdout still fails on ~60.8% of nonzero positions; no_recon ~39.2%.

## Named gap STANDS
- **ABSENT:** certified Kr over QQ from coordinated solve36w_z e1 CRT (12-prime product still insufficient for rational reconstruction + holdout CERT).
- Prior ∞ CRT CERT `n36_basis_q18_inf_QQ_m7_crt6.sobj` STANDS (different object).
- G1-mem Soft SF GAP **stands** until usable Kr QQ + exact zero-polar. Zero-polar **HOLD**.
- Extra-prime rebuild set from Soft SF NAMED-GAP-REBUILD-LIVE is **exhausted** for this CRT path (no invent; no fake CERT).

## What is NOT claimed
- No invented Kr QQ entries. No fake CERT. No exact ν invent.
- tip Soft SF LOCK tip_touched **NO**. Kerr BLOCKED. H3 BOTH NAMED PARALLEL stands. Mesh CANCELLED (not operated).
