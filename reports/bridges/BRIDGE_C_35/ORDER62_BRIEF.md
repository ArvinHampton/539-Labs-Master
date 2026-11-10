# ORDER62_BRIEF — Local Path → Physicist gate clear
Date: 2026-10-24 (America/Chicago). After order61. No inventing P̂_orth / Ξ / k≠0 / Map-C6.

## Status
- order61: RG47a-bis PASS (abs 2.29e−16 ≤ 1e−12); RG47d FAIL (excess 34 at w=½, 2 at w=1); RG48-Weil SKIP (ABSENT).
- Leftover R sits in corner/EVEN (disclosure). w=1 defect ~2-dim; singular values ~0.207, 0.153.

## Propose order62 (await CLEAR)
### (a) RG47e — corner residual vs w=1 defect (Cat A-numeric)
- Object: R2 = R − corner/EVEN = Â1 − axis_Q1 − axis_Q7/2 − corner/EVEN (should be ~0 if split identity holds; also test whether corner columns span the 2-dim w=1 defect of R).
- Prereg: (i) max |R2| ≤ 1e−12 (sanity with RG47a-bis); (ii) rank/excess of R at w=1 after projecting out corner/EVEN span — PASS iff excess ≤ 0 (tol 1e−9 matching order61).
- Characterize FAIL: which corner samples carry the defect.

### (b) RG48-Weil ingredients write-up (Cat A write, no invent)
- Only if written sources already contain companion discriminant form + Weil matrices / χ=±i basis construction: assemble and hash, then run span test.
- Else SKIP with ABSENT again — escalate to Arvin for written Weil ingredients. Do not invent matrices. Milgram stays Cat B.

### Out of scope
ray→sawtooth beyond prefactor; Eichler for order6 shadows; inventing P̂_orth/Ξ/k≠0/Map-C6.

## Deliverables if CLEARED
`order62/{PREREG.md,PREREG.sha256,RESULTS.md,SHA256SUMS,scripts/,data/,logs/}` — new files only; CORE_FREEZE; no push/send.
