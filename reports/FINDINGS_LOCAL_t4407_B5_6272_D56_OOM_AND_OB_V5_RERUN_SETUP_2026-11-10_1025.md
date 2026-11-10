# FINDINGS (Local-derived): 6272 D=56 (ob_v4) ended by OOM, exit 137; B5 stays PENDING; ob_v5 waiter armed, not started. 2026-11-10, written 10:25 CST (America/Chicago)

- **Scope.** Additive. No existing file is edited, deleted, renamed, moved or overwritten (including ob_v4_6272_D56.py, its log and sidecar, and chain_v2). No CERT. No Gemini. Nothing sent outside. Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, checked before and after writing. "Resonant algebra" (RTA historical alias only). A citation alone never makes a claim PROVED (OW 36683379). **Nothing is adopted.**
- **Authority.** Owner t4436. Running jobs were not disturbed: s1e (PID 932685), chain_v2 (PID 1015729), s2e (PIDs 1088107/1088109, timeout 10800, started 10:18:08 CST), and pp_ttheta1_check. The remaining 24 α-3 certificate jobs were not started.
- **This file does not prove B5.** B5 stays PENDING.

## 1. ob_v4_6272_D56 was killed by OOM, not by the 4-hour timeout

- Started by chain_v2 at Tue Nov 10 00:48:10 CST 2026, as `timeout 14400 python3 -u ob_v4_6272_D56.py` (PARI stack 6e9).
- Ended at **Tue Nov 10 10:18:08 CST 2026** with **exit 137**. Wall time about 9.5 hours.
- chain_v2 log (`reports/evidence_local_t4407_computations_2026-11-09/chain_v2_ob_v3_then_D56_s2e_12544.log`) records, exactly:
  - `./chain_v2_ob_v3_then_D56_s2e_12544.sh: line 15: 1045533 Killed                  timeout 14400 python3 -u ob_v4_6272_D56.py > ob_v4_6272_D56.log 2>&1`
  - `ob_v4_6272_D56 exit 137 at Tue Nov 10 10:18:08 CST 2026`
- dmesg at the same timestamp: `Out of memory: Killed process 1054014 (python3) total-vm:8524220kB, anon-rss:4988216kB, file-rss:3044kB, shmem-rss:0kB`. That address space matches the D=56 job (6e9 PARI stack). GNU `timeout` would have returned 124, so this is OOM, not the 4-hour timeout. (The process also ran well past 14400 s, which would have expired at about 04:48 CST.)
- The job log `reports/evidence_local_t4407_computations_2026-11-09/ob_v4_6272_D56.log`, sha256 **4e8ab5c4bb6dd1c68649781d4fbdd696bab6399d5708eb9848b2c2b4609a9198**, still ends at:
  - `N=6272 D=56: mfinit done, dim 388 [131s]`
  - `after p=3: joint kernel dim 88 [188s]`
  - `after p=5: joint kernel dim 32 [488s]`
  - **p=11 never reported.** The final joint-kernel line is absent, so the character is incomplete.
- The log sidecar, written at 10:18 CST, was checked from that directory with `sha256sum -c ob_v4_6272_D56.log.sha256` and is **OK**. It was left untouched; no overwrite and no second sidecar.

## 2. B5 stays PENDING. Settled sub-results at 6272 are unchanged

- **B5 is not filed as proved.** Because D=56 did not finish, the B5 row stays **PENDING**.
- At level 6272, D=1, D=8 and D=28 remain joint kernel 0. D=28 is already **PROVED on the PARI base**, as recorded in ERRATUM_LOCAL_t4429_TERNARY_ac159001_AND_B5_PP_0051_FIXES_2026-11-10_0054.md (F2). Those sub-results are not reopened.
- No Bridge C or t4436 grade is changed by this file. Bridge C stays **49/10/5/2/1 + V₈₄ (67 rows)**. The PP-ruled t4436 tally stays **64/16/5/9/2 (96 rows)**, as in the companion erratum ERRATUM_LOCAL_TDIR_A3_b9fadae5_PP_AUDIT_FIXES_2026-11-10_1024.md. O-b stays OPEN.

## 3. chain_v2 has already started s2e; it was not stopped

The chain treated any exit of ob_v4 as done and, at 10:18:08 CST, started `s2e_j2_level9800.py` (PIDs 1088107 / 1088109, `timeout 10800`, PARI stack 5.5e9). Those processes, and chain_v2 itself (PID 1015729), were left running. After s2e, chain_v2 will wait for s1e (PID 932685) and then start `ob_v4_12544.py` if `ob_v4_12544.log` does not already exist. No fake 12544 log was created.

s1e (PID 932685) was still running at the time of writing, so no s1e follow-up is filed here. The 2026-11-09_0032 follow-up's actual write date remains 2026-11-10 00:32 CST; that file is not renamed or edited.

## 4. Additive rerun: ob_v5 script and waiter (ob_v5 itself not started)

New files, each with a .sha256 sidecar, under `reports/evidence_local_t4407_computations_2026-11-09/`:

| File | sha256 |
|---|---|
| ob_v5_6272_D56.py | 20948ef6af4497083574f437753b590920ad1fa2c23fbf0d509a3097df0fdd75 |
| wait_then_ob_v5_6272_D56.sh | d9ec14a8e1e852e23028869f7cf2e05722dda831fd4d41f2f14c30397a68c020 |

- `ob_v5_6272_D56.py` is a new script (ob_v4 was not overwritten). Same test: joint kernel of T(p²) − χ₋₄(p)a_p(f) for p=3,5,11 in S_{3/2}(Γ₀(6272), χ₅₆). PARI stack 6e9.
- The waiter `wait_then_ob_v5_6272_D56.sh` was started under `setsid`/`nohup` at **10:24:46 CST**, PID **1096505** (SID=PGID=1096505). It does not edit chain_v2. At start it was waiting for s2e; `ob_v5` was not started, and `ob_v5_6272_D56.log` does not exist.
- The waiter will, in order: wait until s2e PIDs 1088107/1088109 are gone; wait until s1e PID 932685 is gone (so chain_v2 can start 12544 if it will); if a 12544 job is running or is about to be started by chain_v2 (chain still alive and `ob_v4_12544.log` not yet present), wait for that job to finish; wait until MemAvailable ≥ 8 GiB and no other ~5GB PARI/`python3` job (RSS ≥ 2 GB) is running; then start `timeout 86400 python3 -u ob_v5_6272_D56.py` (24-hour timeout; p=11 had already been running for about 9.3 hours when ob_v4 was OOM-killed); write a sidecar for the ob_v5 log on exit, never overwriting an existing sidecar; refuse to start if `ob_v5_6272_D56.log` already exists.

Local-derived. Status record only; B5 stays PENDING; nothing adopted.
