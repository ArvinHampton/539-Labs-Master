# FINDINGS 2026-10-24 — order61 / order62 / NONLOCAL inventory_check (Auditor, read-only)
Pass 22:13–22:25 CDT. No verdicts altered. No physics added.

## order61 (BRIDGE_C_35/order61/), status: COMPLETE and VERIFIED
- Hashes: PREREG.sha256 is OK (9cc780f1…04d). SHA256SUMS: 9/9 OK, covering PREREG, RESULTS, 2 scripts, 3 data files and 2 logs.
- mtime order (CDT): PREREG.md and its sha were written 22:11:54. Scripts followed at 22:12:17, rg47a data at 22:12:18 and rg47d at 22:12:19. RESULTS (22:12:35) and SUMS came last. **The absolute bar of 1e−12 and the rank tolerance of 1e−9 were fixed and hashed about 23 s before the scripts existed.**
- Verdicts vs PREREG and logs:
  - RG47a-bis: **PASS, matches the coordinator's claim.** abs_resid is 2.29e−16 against a bar of 1e−12. The control is 3.34, above 1e−4. The pieces are bit-identical to order58 (diff 0). The script criterion on line 28 equals the PREREG criterion.
  - RG47d: **FAIL, matches the claim.**
    - The gate reproduced: rank 75, joint 148 and 150.
    - R_both excess is 34 at w=½ and 2 at w=1.
    - The script criterion on line 39 is max(excess) ≤ 0, as the PREREG requires.
    - The controls of 71/49 and 84/72 equal the PREREG values.
    - The sensitivity runs at 1e−6 and 1e−12 give the same numbers and are disclosed only.
  - RG48-Weil: **SKIP (ABSENT), matches the claim.** This is the conditional branch the PREREG allows. The missing items are listed. Milgram stays Cat B.

### Findings
- N-61-1 (note), RESULTS.md, "w=½ is the wrong weight: R pairs with weight 1".
  - Evidence: the claim is an interpretation. It is disclosure only and not a preregistered statistic.
  - Fix: tag the sentence as interpretation (Cat B) or leave it in the characterization section.
- N-61-2 (note), the RG47a-bis PASS.
  - Evidence: this PASS is a new prereg with an absolute statistic. It does **not** retro-convert order58 RG47a, which stays FAIL under its literal PREREG.
  - Fix: make sure downstream summaries do not report "RG47a PASS" without the "-bis" suffix.
- N-61-3 (note), CHAT vs PAPER. Every order61 input is a disk artifact from orders 3, 56, 58 and 60. Tag: PAPER/ARTIFACT. No chat sources.
- **No blockers or warnings for order61.**

## order62 (BRIDGE_C_35/order62/), status: PREREG ONLY
- PREREG.sha256 is OK (83a7b465…eaa), written at 22:13:37. data/, logs/ and scripts/ are empty. There is no RESULTS.md and no SUMS.
- Hash-before-run readiness: **READY.**
  - The PREREG fixes: PASS(1) as ≤ 1e−12, PASS(2) as excess_proj ≤ 0 at w=1, and the rank tolerance of 1e−9.
  - The gate is order61's 34/2 excess.
  - The pieces source is order61/data/rg47a_bis_raw.npy, which is in the order61 SUMS.
- N-62-1 (note): w=½ is disclosure only in order62. This follows the order61 observation and is a post-order61 design choice. That is legitimate because it is declared before the run. Re-audit once RESULTS lands.

## NONLOCAL inventory_check (remaining files read: EH_K11N_HUNT, LEAN_L1L7_ASSUMPTIONS, ARVIN_WRITTEN_NL_VARS, EXPANDED_SEARCH_LOG)
- W-NL-1 (warning), ARVIN_WRITTEN_NL_VARS GC-1 and GC-2, and EH_K11N_HUNT.
  - Claim: these are "written" Φ=8πG11·G² and flux 4880→k items, labelled Cat A-chat.
  - Evidence: the source is A22 chat exports cd250095 and a01dcbad, which are assistant-side text and not paper. The EH1 zenodo text layer is garbled and contains no k(N) expression.
  - Fix: tag both as **CHAT** and not Cat A. They must not clear an NL gate without the Physicist accepting them as written.
- W-NL-2 (warning), the flux-unit convention.
  - Evidence: cd250095:612 says the prefactor moves with the unit convention, and a01dcbad reports a 3-unit miss (N = 4876.82).
  - Fix: keep k(N) OPEN and do not cite 0.02531 as derived.
- N-NL-1 (note), LEAN_L1L7_ASSUMPTIONS.
  - L2 fibre is `True`, L3 Γ is defined directly, and L6 and L7 rest on hypotheses (hK, h1, h2).
  - The Lean header claims a 09-29 build, but EH1 App. C says "No kernel run". This conflict is unresolved and no kernel run was performed.
  - Fix: label L1–L7 as "assumed-block algebra" and not as an 11D derivation.
- N-NL-2 (note), EXPANDED_SEARCH_LOG EH-Ω5.
  - Ω₁₁D appears only as a structural volume-ratio formula from chat eda69302:1567.
  - Tag: CHAT, Cat B. NL1 stays blocked (no invention).
- Stream separation: these files read BRIDGE_C_35 read-only for search only. I saw no local-map mix-in.

## order57 quote checks (order5:41, order8 M1, order12:23-24, Residual_False_Theta §3)
DEFERRED; I ran out of time this pass. This is carried forward.

## Counts this pass
Blockers 0 / Warnings 2 / Notes 6.

## ADDENDUM 22:25 CDT: order62 RESULTS landed (22:14:08), full audit
- Hashes: PREREG OK. SHA256SUMS 5/5 OK.
- mtime order: PREREG 22:13:37, then script 22:13:50, then data and log 22:13:51, then RESULTS and SUMS 22:14:08. **The bars were hashed before the run.**
- RG47e: **FAIL, consistent with the PREREG.**
  - The gate reproduced 34/2.
  - PASS1 is true (2.67e−15 ≤ 1e−12).
  - PASS2 is false (excess_proj 2 at w=1).
  - The script criteria on lines 32–34 equal the PREREG criteria.
  - The sensitivity runs and w=½ are disclosure only.
- N-62-2 (note), excess_R2 = 105.
  - This is the rank of a matrix around 1e−15 under a relative tolerance. RESULTS correctly calls it noise-floor and not meaningful.
  - Fix: none needed. Optionally state an absolute floor for future runs.
- N-62-3 (note), RG48 SKIP (ABSENT).
  - The s11 Thm tensor7 ρ_lab matrices are PAPER (tex). They are correctly *not* assumed to be the companion lattice.
  - Treating order13 as superseding RG48 is a Physicist decision. It has not been made.
- N-62-4 (note), the suggested order63 RG47f ("carriers den 5,7 → ρ5/ρ7 sectors").
  - This is a heuristic link (Cat B). It needs a PREREG before any claim is made.
- Counts revised for this pass: Blockers 0 / Warnings 2 / Notes 8 (N-62-1 is superseded but kept).
