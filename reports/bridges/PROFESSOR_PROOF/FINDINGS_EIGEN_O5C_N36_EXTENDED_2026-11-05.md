# FINDINGS — Eigen O5(c) N36 extended-prime run — 2026-11-05

Status: PARTIAL; runtime unavailable. Inspected at 15:40 CST (America/Chicago). No CERT. No external sends, Gemini, deletion, or fabricated reconstruction.

## Resume attempt and stop reason
Owner-reported halt of PID 887352 at 15:17 CST and release at 15:38 CST were respected. PID 887352 is absent. Its prime 8022281 log is incomplete and no e1 output exists for that prime. All partials were retained.

After a weekly usage reading of 68.5% (below the requested 80% gate), a fresh prime 8022281 invocation was attempted using the existing generated script: `/tmp/pm/bin/sage -python solve36w_z.sage.py 7 8022281`, from `/workspace/grok-batches/eigen-n36-503`. It exited 127 before computation: `/tmp/pm/bin/sage: No such file or directory`. `/tmp/pm` itself is absent and `command -v sage` found no Sage. No substitute runtime, installation, or old driver was launched. No new solver PID was created; no jobs remain from this attempt. Evidence: `/workspace/grok-batches/eigen-o5c-n36-moreprimes-2026-11-05/fresh_p8022281_e1.log`. Restoring the Sage runtime is required to resume.

## Completed primes / evidence
25 existing e1 outputs were inventoried and SHA-256 recorded in `/workspace/grok-batches/eigen-o5c-n36-moreprimes-2026-11-05/extended_existing_outputs.sha256`. The prior completed batch added primes 7978181, 7982101, 7985041, 7995821, 8007581 beyond the baseline 20: 5 of the permitted maximum 30 extra primes; 25 extras remain available under the cap. These five logs end in `done`; their outputs exist. The existing reconstruction log loaded all 25, reported rank 503 and 503 RREF rows for each, and identical pivots. This is prior computed evidence, not a fresh deserialization check in this attempt. Newly completed primes in this attempt: zero.

Bits gained by the five completed extras: sum(log2(p)) = 114.648583712 bits. Bits newly gained by this resume attempt: 0. Prime 8022281 is NOT counted.

## Holdout / rational reconstruction
Latest completed result: `/workspace/grok-batches/eigen-o5c2-n36-batches-2026-11-05/recon_batch1.log`: 24 training primes, log10(M)=165.572065535653; holdout prime 8007581; rows 0, 1, 100, 250, 502 each FAIL; `ALL_ROWS_HOLDOUT False`. The existing script samples at most 12 nonpivot entries per row. This failed sample test does not reconstruct or exactly verify the full RREF. No fresh reconstruction ran because Sage is absent. No holdout pass, no full QQ reconstruction, no exact verification, and no QQ rank claim are made. The earlier ~10^121 height statement is historical heuristic evidence, not a rigorous lower bound derived solely from failed LLL candidates.

## Stabilizer citation and PP N1 hygiene
`/workspace/grok-batches/eigen-o5c-n36-moreprimes-2026-11-05/stab2.log` records p=7957601, exp 1 vs 3: piv_eq True, rref_eq True, diff 0, stack_rank 503. These are computed finite-field comparisons, not a proof over QQ. Per PP note N1, any `ok(...,True)` assertions are argument steps, not computed checks. No such assertion is promoted to a computed check here.

## Usage and integrity
Weekly usage reading before attempted prime: 68.5% used, shared with other apps on the plan; resets Tuesday Nov 10 at 09:49 CST (America/Chicago). Extra usage comes from additional usage credits. No additional prime was launched, so no further per-prime reading was needed. The 80% stop threshold was not reached; missing runtime caused the stop.
Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` SHA-256 before and after: `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91`. Expected hash matches. Tip untouched. Before/after sidecars retained in `/workspace/grok-batches/eigen-o5c-n36-moreprimes-2026-11-05`. Existing killed-job log, scripts, markers, and outputs were not overwritten or deleted.

## Deliverables
This report and companion PRESS, each with .sha256 sidecar, are copied to the requested seven bridge/report destinations and verified there with sha256sum -c. The output inventory sidecar checks file integrity only, not mathematical correctness.
