# AUDITOR FINDINGS — t1135u MR1 V₄₂ basis Cat B Write CONFIRM — 2026-10-25 (~20:40 CDT, America/Chicago)

**Verdict: MATCH-with-SF** (soft SF only; no hard blocker)
**Clear-for-fold: YES** (W-V42-1 into tip §2 P1 as Cat B; fold NOT performed in this step)
**residual-C tip untouched: Y**

## Shas (full, recomputed)
| Artifact | Path | sha256 |
|---|---|---|
| Write | reports/OWNER_WRITE_MR1_V42_BASIS_t1135u_2026-10-25.md | 9fe6172f7404e9ccbcf1bd4125675cf1319cc924a5f7dc8d1e0ca11273c32592 (= expected) |
| deepen FINDINGS | /workspace/grok-batches/MR1-AUTHOR-PURSUE-W7-GENS-BASIS-DEEPEN_2026-10-25.md | 46c267e5b7264a7682fb30fb23cee1bb16dcf841e9b1da493de15abec3ca45fd |
| rel.pkl | reports/heavy-daily/2026-10-18-V42-Structure/rel.pkl | f8dadf42d8bd1bb4f03e572b9c7616e5745e44dc21c4ae8fb5e4b56d2617e511 |
| relations.py | reports/heavy-daily/2026-10-18-V42-Structure/relations.py | 12730d9515b711e8c46aa1ae10f9fcabf53233d22dcaac4262a1d0d67b63efac |
| relations.txt | same dir | 5ad9dfe08992673c8df24e3711423aa388441839ee86ea45c8431ed92a2545b9 |
| V42-Structure.md | reports/self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/V42_Structure_2026-10-18/2026-10-18-V42-Structure.md (identical copy in bridges/_git_v8_unpushed_clone) | 234c9128bca04fe584e79952a1d534d2762a9edbc760062778ac7aa6c7962ed0 |
| residual-C tip | /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | c7121aa8bf7d2e534f0ad55ce1b4a1a1a26db8289087979f3a263efe9565a5ef (live; mtime 20:34:37 CDT < Write mtime 20:37:17 CDT) |

## 1. W-V42-1 class table — MATCH
Re-ran relations.py union-find logic on rel.pkl independently: 159 prop pairs; zero = [71,95,107,117,127,129,131,133,135,137,139] (11); 129 nonzero labels → 42 classes; sizes {1:3, 2:15, 4:24}. All 42 `rep: [members]` lines diff-identical to the Write. Agrees with relations.txt ("42 proportionality classes, sizes [(1,3),(2,15),(4,24)]") and V42-Structure l.33 ("So V has a monomial basis of 42 distinct functions.").

## 2. Cat B float-c hygiene — MATCH
All c stored as Python complex; 50 of 159 non-integer; the Write's example −0.809017−0.587785j is present verbatim (stored at 6-decimal precision). Write correctly claims no exact algebraic c, no ρ matrices, and lists exact c as NOT Written. Note: V42-Structure §3 is headed "(Cat A)" by Author for the geometric class count; Write's Cat B for the basis *packaging with c* is consistent with rev4 and stricter, so accepted.

## 3. Category / Bridge — MATCH
Cat B (not Cat A). No Bridge YES / no READY YES / no Z₇↔W₇ / no W₇ rule / no Γ₀(49) gens / no k=−2. Bridge PARTIAL, READY NO.

## 4. Tip untouched — Y. 5. No fold in this step — confirmed (Auditor did not fold).

## Soft SF
- SF-1: Write cites relations.py sha truncated `12730d95…` "(see FINDINGS)"; full sha 12730d9515b711e8c46aa1ae10f9fcabf53233d22dcaac4262a1d0d67b63efac verified here — use full sha at fold.
- SF-2: Write does not give paths for rel.pkl / V42-Structure.md; paths recorded above.
- SF-3: c in rel.pkl are 6-decimal rounded; any future exact-c Write must recompute, not rely on pkl values.
- SF-4: Fold must recompute tip sha and come back for Auditor re-CONFIRM (per Write apply path).
