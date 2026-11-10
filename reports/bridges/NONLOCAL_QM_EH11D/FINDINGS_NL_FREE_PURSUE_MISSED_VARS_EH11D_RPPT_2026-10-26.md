# FINDINGS — NL Free-Pursue Missed Vars: EH-11D / RPPT (Soft SF write-only, non-tip) — 2026-10-26
Lane: Non Local Path · Project Quantum Comp NONLOCAL_QM_EH11D · Written ~17:40 CDT (America/Chicago)
Proof standard (OW `687b27f5…`, `ef6da7e7…`): every item is labeled **PROOF-BACKED** (a proof, or a cite plus lemma) or **UNPROVEN-GAP** (the gap is named). **NO PASS CLAIM on any numerics.** Eight-agent set only.

## (a) WHAT is being pursued
1. **T1: Join-anchor boundary.** List the packaging/sheet variables used on RR-NL-SHEET-01 and in δ_W₇ that have no anchor in the NL-JOIN-1 proof (`946a5910…`), and set them against the Rank-20 SAMPLE boundary (`85c9c5cf…`).
2. **T2: RPPT reverse-parity vs δ_W₇ SAMPLE.** Find out whether the δ_W₇ sample node set has any correlation, parity, or symmetry with the RPPT reverse-parity load or the proved join that could be proved.
3. **T3: Hybrid-MC manifest gaps.** Find the inputs missing from the runnable-spec (`27058bad…`) when it is checked against the frozen sheet (`da91ad83…`). These gaps block Doc-full readiness. No χ² data is invented.

## (b) FIRST FINDINGS

### T1: Join-anchor boundary
- **T1.1 PROOF-BACKED. ρ_DM, β_PBH, κ_dark and z=1…118 have no join anchor.** The NL-JOIN-1 proof's identification parts (P1, P2) use only g_s, X^M, the bracket of E_leak, the Owner sameness LOCK `e41ceac4…`, the join LOCK `7588bc8f…` and DRAFT `cab5868f…`. (P4) cites the sheet `da91ad83…` only as a "frozen, cited" carrier. Sheet §3 labels all four rows CITED-from-Corrected-7D, not join-derived. **Lemma T1.1:** none of the four values occurs as a premise or conclusion of P1–P4. *Proof:* go through each part. The only objects named are g_s, X^M, E_leak, and the LOCK/DRAFT/sheet shas. ∎ So these rows are Doc-cited only. They are not join-proved.
- **T1.2 UNPROVEN-GAP. Index s for g_s is not fixed.** Residual Packaging FINAL `7ab9a254…` defines g_s(q) for s∈{7,8,11}. Neither the join proof nor the sheet says which s, or which combination of s, enters the bracket term g_s X^M on RR-NL-SHEET-01. *Gap:* an Owner-Written choice of s, or a proof that the load does not depend on s. This is the most important missed variable.
- **T1.3 UNPROVEN-GAP. X^M has no value or definition on the sheet.** The glossary `aaf6ab31…` §4.1 labels X^M only as a "Frobenius/strong-sector warp in V_flavor". No sheet row gives X^M, M, or q. *Gap:* the definition of X^M and the domain of q on the sheet.
- **T1.4 UNPROVEN-GAP. The residual weight w is not linked to g_s.** The sheet's null control w≡1 is INVENT-under-lift. No Written statement says how w is built from g_s X^M in the residual-weighted run. *Gap:* the map w = w(g_s, X^M).
- **T1.5 PROOF-BACKED. The δ_W₇ node set lies outside the join.** By proof (P3), δ_W₇ and Rank-20 are used in no step of the proof. So {1/7,3/7,5/7,1} has no join anchor and remains SAMPLE (`85c9c5cf…`, `45bc050a…` §3).

### T2: RPPT reverse-parity vs δ_W₇ SAMPLE
- **T2.1 PROOF-BACKED. W₇ does not preserve the node set.** Let W₇x = −1/(7x) (Auditor `8afcc443…`). For x>0, W₇x<0, so W₇ maps (0,1] into (−∞,0) and sends every node out of the domain x∈(0,1] used by `45bc050a…` §3. ∎ So stratifying on these nodes is **not W₇-equivariant**. Any proposed "parity correlation" between the nodes and the δ_W₇ involution fails in this normalization.
- **T2.2 PROOF-BACKED. The candidate reflection x↦1−x maps odd-numerator sevenths to even ones.** 1−(2k+1)/7 = (6−2k)/7 has an even numerator, and 1↦0∉(0,1]. So the image of {1/7,3/7,5/7,1} is {6/7,4/7,2/7,0}, which does not intersect the original set. ∎ The node set is therefore not invariant under this natural reflection either.
- **T2.3 UNPROVEN-GAP. No reverse-parity involution is Written on x.** The corpus defines reverse parity only on the RPPT 118-element table (z, via Corrected 7D §3.1 `4758d180…`). There is no Written map from z∈{1…118} to the phase x∈(0,1], and no involution on x. *Gap:* a Written z↔x map plus a parity involution. Until both exist, every RPPT↔δ_W₇ correlation is a candidate only.
- **T2.4 PROOF-BACKED (negative). The proved join has no correlation with δ_W₇.** This follows directly from (P3) in `946a5910…` (see T1.5). Any correlation would need a new lemma; none is Written.
- **T2.5 PROOF-BACKED cite (negative). There is no automatic two-sided law.** Ledger `6445aa9f…`: a two-sided law would need √7, but the samples give 5636, 278, 1299 and 2963, and the degree-3 interpolation "is data, not a Fricke identity" (as summarized in `85c9c5cf…` §5). Sample vanishing does not force any correlation.

### T3: Hybrid-MC input-manifest gaps
- **T3.1 UNPROVEN-GAP. E_leak(t) has no functional form or t-range in the manifest.** The sheet freezes parameters only. The integrand, the t-domain, and the minus-U beta rate per element z are not on the sheet. The deepen `ce6520ce…` §2 records that the full text of minus-PT and 7D torsion was ABSENT on box (A27 txt mirrors `7302244a…`/`95ce88b3…` exist but have not been extracted into the manifest). *Gap:* a per-z rate table with its source sha.
- **T3.2 UNPROVEN-GAP. dof, data vector and covariance are ABSENT.** χ²/dof = 0.79 is quoted from the Doc without N_data, the number of fitted parameters, the observations, or the errors. A PR1 recompute cannot reproduce the band without them. *Status:* awaiting Owner-Written inputs. Nothing is fabricated here.
- **T3.3 UNPROVEN-GAP. F_friction has no parameters.** The secondary observable is named, but the sheet carries no F_friction rows.
- **T3.4 UNPROVEN-GAP. Provenance fields are missing.** `27058bad…` has no RNG seed, sample count, integrator or tolerance, SymPy version, or sha-pinned input list. These were also flagged as next steps in `80dc7887…` §4 item 3. *Gap:* manifest schema. Placeholders are allowed. Values are not.
- **T3.5 PROOF-BACKED. The manifest inherits T1.2–T1.4.** By T1.1 and the runnable-spec's join wire "through g_s X^M", the run needs s, X^M and w. Those are open (T1.2–T1.4), so the manifest is incomplete. ∎

## (c) Explicit non-claims
- No Kerr or Path4 C2–C3 physical load. No Kerr numerics. C1 = 0.10 is scoped-gate-only and is not Kerr C1.
- The tip Soft SF LOCK was not touched (pre and post sha below).
- χ² data, dof and coefficients are still **ABSENT**. Every χ²-adjacent item is UNPROVEN-GAP and awaits Owner input. 0.79 is a Doc-quoted reference only.
- No MC was run and nothing was recomputed (Rule 4 → PR1). No δ_W₇ ∀x claim. Rank-20 remains SAMPLE ONLY. NL ≠ Local Bridge C. No Eigen or Ops.

## (d) Authority table (live sha256sum, 2026-10-26)
| Item | sha256 |
|---|---|
| OW FREE_PURSUE | 687b27f5ba8fab6a847563069f66bbb4b9511cf36d14df3e7143a83db335eecd |
| ASSIGN EIGHT | d763ac36900df1f0bb55e0ce8d7f72e96aa29e1b1e44af7269ce0d892dc73bba |
| OW invent-ban lift | ef6da7e7d6d97e115cabf7fa661fbc262180cdde9de39b41a123da2347076192 |
| PROOF NL-JOIN-1 | 946a5910ead0631eca28c5971a74d28d61b66e853f8cb8d88c1cd7b42c88d2fe |
| POSTURE PASS | 62f0e07133833cc7b8d2d2de5371635499f9622f72c575b6049c54fa39736544 |
| Sheet params | da91ad83ac35a2f3a897dbd1794b90d102b409284012b889d6b74849e3af5998 |
| δ_W₇ invent-scope | 45bc050a5c003b4858c1f4e39adf720379dd419ad64830de84384a82e1f3d561 |
| Rank-20 SAMPLE | 85c9c5cf2b64c3363720a2b79b079fb55ab49d480697b9f5d7b82524cfcf7666 |
| RPPT MC deepen | ce6520ce182a8c26ec1c99b783c8d31a4f0620b99b0cc4da71362dbdec82b070 |
| Hybrid MC DESIGN | 6bbc198e9a73ef8d80b8d7c1127404b3226faf66f4893272ba0fdaadd465968b |
| Runnable-spec | 27058bad386fc64dff071324e4f4d248a60113c68349917b42656c93025fe980 |
| Invent-scoped CONTINUE | 80dc7887e87a21ec5e0be81d604971f2e2abec2dc13255fb2815a1fa9ad4023d |
| OWNER REVIEW four beats | df9dc6b0de68e52f6b2bee4c3f735ad04b06aa73914d9dccdd141ff0b4e27712 |
| tip Soft SF LOCK (read-only) | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 |

Soft SF → **Auditor**. tip_touched **NO**. sha256 is in the `.sha256` sidecar.
