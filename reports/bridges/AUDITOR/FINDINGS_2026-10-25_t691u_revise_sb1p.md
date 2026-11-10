# FINDINGS — deduce_t691u_revise_sb1p LOCK (G-A1a REVISE S-B1′)
Stamp: 2026-10-25 10:16 CDT (America/Chicago). Auditor: Residual-vs-Resonant. Authority: Arvin widget t691s4368 (G-A1a REVISE S-B1′, keep Written family). Soft-SF only; no PASS/FAIL altered; no physics invented; NL untouched; order78 not started.

## Hash MATCH (base BRIDGE_C_35/)
| file | claimed | recomputed |
|---|---|---|
| deduce_t691u_revise_sb1p/PREREG.md | 6e2ef05a…8b67 | MATCH |
| deduce_t691u_revise_sb1p/RESULTS.md | 547e9739…1d72 | MATCH |
| deduce_t691u_revise_sb1p/SHA256SUMS | 26f71cf3…6269 | MATCH |
| author_candidates/AUTHOR_CANDIDATE_B1_revised_SB1p_selector_2026-10-25.md | 3d502756…366f | MATCH |
| STREAM_IDLE_LOCAL.md | c50b56f5…3a1f | MATCH |
| inventory_check/SHA256SUMS | 0b484887…faef | MATCH |
PREREG.sha256 = 6e2ef05a… MATCH. sha256sum -c: deduce SUMS 4/4 OK; inventory SUMS 42/42 OK.
PREREG-before-RESULTS: mtime PREREG 10:12:09 CDT < RESULTS 10:12:32 CDT; RESULTS cites PREREG sha unchanged. OK.

## Independent numeric re-check (Object A only; no new numbers adopted)
Solve of 4×4 Written system: det 36.1412; (a,b,c,d)=(10.6923, 0.2160, 2.7618, −7.5316) — MATCH RESULTS. F(0⁺)=34.147 MATCH. Products F(x)F(−1/(7x)) at x=1/7,3/7,5/7,1 = 5636.16 / 277.64 / 1298.61 / 2962.76 vs √7≈2.6458 — MATCH (S-B1 fails globally). Grid scan x∈(0,50]: min F≈3.1596 >0 (supports G-R2, NOT a proof; G-R2 stays open).

## Claims
1. Revised S-B1′ admits Object A, excludes deg-3 — CONFIRMED (O(t²), no parity; deg-3 cubic term excluded). Label AUTHOR-CANDIDATE.
2. Written fit fails original S-B1; candidate weakens S-B1 to domain-restricted (x>0 ansatz, x<0 by involution) — CONFIRMED, text states it explicitly; coherence conditional on G-R2. No overclaim.
3. Uniqueness — reconciled: RESULTS says "Within Written family: UNIQUE (4 samples, nonsingular)"; wider class NOT unique (G-A1c); overall verdict PARTIAL. Coordinator "UNIQUE in Written family" = accurate as within-family interpolant uniqueness; dispatch phrasing "PARTIAL within-family only" is imprecise (verdict PARTIAL is global, within-family is UNIQUE). Neither artifact claims UNIQUE-FORCED → no SF. Dual-split NOT FORCED (G-A1b) — CONFIRMED.
4. Bridge PARTIAL; READY NO; residual-C OPEN; δ≡0 / RG76d / Bridge YES NOT forced (h_residual^{high} ABSENT, G-A3) — CONFIRMED.
5. SF-W7-3, CORE_FREEZE, no numeric outside Written family — CONFIRMED (only Object A + derived fit).
6. Candidate explicitly "AUTHOR-CANDIDATE, NOT Cat A, NOT DEDUCED; binding only on Arvin ACCEPT" — CONFIRMED.
7. t691s4368 / G-A1a cited in PREREG, RESULTS, candidate — CONFIRMED.

## Soft SF
- SF-T691-1 (advisory, cosmetic): dispatch wording "Uniqueness PARTIAL within-family only" mismatches RESULTS ("within-family UNIQUE; overall PARTIAL"). Artifacts correct; use RESULTS wording downstream.
- SF-T691-2 (advisory): G-R2 (F≠0 on x>0) supported numerically only; weakened S-B1 coherence must stay conditional until proved/accepted.
No Cat A mislabel found.

## Standing
LOCK CONFIRMED as deduce hygiene + draft candidate. Baseline FINDINGS 4c36c34f7bf7d2282e2a66216b5c1a10597633f1af3748b4d0fdb296c726a1fd STANDS; superseded only after Arvin ACCEPT + CONFIRM. Open: G-A1b, G-A1c, G-R2, G-A3, Arvin ACCEPT of 3d502756…. Bridge PARTIAL; READY NO; residual-C OPEN.
