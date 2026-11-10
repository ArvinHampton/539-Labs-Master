# FINDINGS — Auditor priority pass, 2026-10-24 (22:05–22:08 CDT, America/Chicago)
Scope: BRIDGE_C_35 order56/57/58, NONLOCAL_QM_EH11D, MISSING_VARS_HUNT spot-check, MAPS_CANDIDATES (light), RTA v11/v12 location.
No source file was modified. No PASS/FAIL verdict was altered. Nothing below adds physics, formulas, or completions.
Counts: **1 blocker / 7 warnings / 8 notes**.

---
### [blocker] order58 RG47a is flagged PASS under a normalization the PREREG did not specify
- **path:** BRIDGE_C_35/order58/PREREG.md (RG47a); scripts/rg47a.py:20-28; logs/rg47a.log; logs/rg47a_post.log
- **claim:** `RG47a_PASS: true` in rg47a.log.
- **evidence:** The PREREG criterion is `max |A1 − Σpieces| / max(|A1|, 1e−300) ≤ 1e−6`. The script uses `resid_rel` with denominator `max(|A1|, 1)` for the PASS flag (line 28). The literal PREREG statistic is computed as `resid_rel_strict = 0.1746`, which is above 1e−6. After the run, rg47a_post.log drops 548 cases with |A1| < 1e−9 and gets 3.9e−14 on the remaining cases. That filter is not in the PREREG. The dominance table is also distorted by near-zero denominators (max_ratio ≈ 1.18e11).
- **fix:** Do not record RG47a as PASS in any order58 RESULTS.md. State that, as preregistered, the criterion is not met (0.1746 > 1e−6), and describe the max(|A1|,1) and |A1| ≥ 1e−9 versions as post-hoc deviations. If a different normalization is wanted, preregister it in a new hashed order. Auditor did not change the log.

### [warning] order58 is incomplete; there is no script/data hash chain
- **path:** BRIDGE_C_35/order58/
- **claim:** order58 is listed as the latest order (order57/POINTER.md: "order58 candidate RG47a/b, RG48").
- **evidence:** Only PREREG.md and PREREG.sha256 exist (sha256 OK). There is no RESULTS.md, no SHA256SUMS, and no SHA256SUMS_all. RG47b has no script, no log, and no recorded SKIP. scripts/rg48b.py was written at 22:05:15 CDT, after rg48 ran (22:04:59), and is not in the PREREG. logs/rg48b.log was 0 bytes when first listed and later 5760 bytes, so a run was in progress during the audit.
- **fix:** Complete the order: hash scripts/data in SHA256SUMS, write RESULTS.md, record RG47b as SKIP with obstruction if no written match statistic exists, and label rg48b as a post-PREREG exploratory step (Cat B) or preregister it separately.

### [warning] order58 RG48 does not run the PREREG's test (Weil χ=±i span)
- **path:** BRIDGE_C_35/order58/scripts/rg48.py:1,20; logs/rg48.log; PREREG.md RG48
- **claim:** RG48 is "full Weil χ=±i basis for P-even … is P-even target in span of χ=±i eigenvectors".
- **evidence:** rg48 only compares discriminant-form q-values and Milgram sums of A (Gram [[2,7],[7,7]], det −35) with definite even binary forms. No eigenvector span or rank test appears in the log. The script has an unresolved inline comment ("…wait det must equal 35"). rg48b then switches to the rescaling A(2) after the run. The PREREG requires the Gram "as written in order12", and the script does not cite that source line.
- **fix:** In RESULTS, report RG48 as not executed as preregistered (or SKIP), cite the order12 line for the Gram, and do not present the q-value mismatch as the Cat A no-go.

### [warning] NONLOCAL EH-FF1 is labelled "Cat A PASS" but depends on three unwritten conventions
- **path:** NONLOCAL_QM_EH11D/MILESTONE_2026-10-24b.md; inventory_check/EH_O1_FOURFORM.md; prereg/EH_FOURFORM_20261024/PREREG.md:2-3
- **claim:** "EH-FF1 Cat A PASS (conditional on Φ≡G², 8πG11=1, a=1/24)"; "h2 is DERIVED".
- **evidence:** The PREREG itself says the conventions are "taken from source juxtaposition (flagged, not derived)". EH_O1_FOURFORM.md says Φ≡G² was "never stated as a definition", and that 8πG11=1 and the a=1/24 choice are not derived. MISSING_VARS_HUNT classes all three as Cat B or ABSENT.
- **fix:** Relabel the milestone wording as "Cat A algebra, conditional on Cat B conventions", for example "Cat A | B-conditional". Keep the PASS verdict (unaltered). Do not cite h2 as derived without the conditional.

### [warning] NONLOCAL EH-RB1: the C2 control differs from the PREREG; result.log is unhashed and edited; the header time is wrong
- **path:** NONLOCAL_QM_EH11D/prereg/EH_RICCIBLOCK_20261024/{PREREG.md,PREREG.sha256,result.log}
- **claim:** The PREREG sets C2 as "3 ext dims instead of 4, fibre 7". The header says "written 2026-10-24 ~22:10 CDT, before run".
- **evidence:** A post-run note in result.log says C2 used "3+1+6(S^6)+1 flat". That is a different split, so it is not the preregistered control. PREREG.sha256 covers only PREREG.md and run.py. result.log is not hashed and has an appended note. The file mtimes are 22:00:50 CDT (PREREG) and 22:01:22 (result.log), which is earlier than the stated ~22:10.
- **fix:** In MILESTONE_c and INVENTORY, record that the C2 control was run in a modified form, and either rerun C2 as preregistered or prereg the new one. Correct the timestamp, and add the result.log hash at the time of writing.

### [warning] NONLOCAL EH-FF1 hash file postdates result.log
- **path:** NONLOCAL_QM_EH11D/prereg/EH_FOURFORM_20261024/
- **claim:** "Prereg sha256 … before run".
- **evidence:** mtimes: PREREG.md and run.py at 21:58:32.187, result.log at 21:58:32.535, PREREG.sha256 at 21:58:32.603 CDT. The sha file includes result.log, so it was written after the run. The files can't show that the PREREG was hashed before the run. All three hashes verify OK now.
- **fix:** Going forward, write PREREG.sha256 before execution and put post-run hashes in a separate RESULTS SHA file. Note this ordering in the milestone.

### [warning] MAPS: Π*_max, g=(−1)^τ, P_res were agent-discovered, then "accepted"; the provenance must stay Cat B
- **path:** MAPS_CANDIDATES/DISCOVER_PI_RULE/RESULTS.md:9; DISCOVER_GRADING_PATH/NOTES.md:11; PI_MAX_PURSUE/PREREG.md:2, RESULTS.md:6; C11_GRADING_ACCEPT/PREREG.md
- **claim:** "Rule accepted (Arvin…)"; PM1 "PASS | A"; C11 FAIL "Category A".
- **evidence:** DISCOVER_PI_RULE says "the rule itself is a free extremal choice". DISCOVER_GRADING_PATH/NOTES says P_res/β̂ are "not Arvin-written" probes. The PM1 Cat A only covers sha256 identity of the word. C11_GRADING_ACCEPT discloses that the result was known beforehand (not blind), which is handled correctly. This is the process pattern of "gate cleared by acceptance of agent-constructed objects". No invented formula was found presented as Arvin-written, but the objects are not corpus-written.
- **fix:** Label Π*_max, g and P_res as "accepted-by-owner, agent-constructed (Cat B provenance)" wherever cited, and keep PM1's "A" scoped to hash identity. C10/C11 FAIL verdicts are unaltered.

### [warning] MAPS checksum mismatch: NOTES.md edited after hashing (2 dirs)
- **path:** MAPS_CANDIDATES/L3_INDEPENDENCE/SHA256SUMS; MAPS_CANDIDATES/MARKOV_FIBRE_FREQ/SHA256SUMS
- **claim:** SHA256SUMS covers the directory contents.
- **evidence:** `sha256sum -c` gives `./NOTES.md: FAILED` in both. Every other entry is OK. NOTES.md is not a PREREG/RESULTS file.
- **fix:** Diff NOTES.md against the hashed version if a copy exists. Re-hash under a new dated SUMS file instead of overwriting, and log the edit.

### [note] ORDER59_BRIEF.md hashed with a corrupted line; the sha file uses an absolute path
- **path:** BRIDGE_C_35/order57/ORDER59_BRIEF.md (item (b), last bullet); ORDER59_BRIEF.sha256
- **evidence:** The text "…a_C vs Â1 / �- Do NOT open a new derivation of a_C vs Â1 / Ξ" is duplicated or truncated with a replacement char. The sha file lists /workspace/… as an absolute path, while the others are relative. The hash verifies OK.
- **fix:** Issue a cleaned brief as a new file (order59 or a v2), and use relative paths.

### [note] order56 wording "confirms A1(Ĥ)=0" should stay sample-scoped
- **path:** BRIDGE_C_35/order56/RESULTS.md (RG46a bullets)
- **evidence:** RG46a PASS is verified against the log: dev 1.07e−15 / 1.78e−15, ctrl 3.245, strip_max 3.22. RG46b FAIL is verified: ranks 75, joint 148/150, gate 36/36 and 36/72. The verdicts match the data. The sentence "That was order5's §1.4 proof sketch, until now only Category B" could be read as upgrading the proof to Cat A. A numeric check on 216×105 samples doesn't do that.
- **fix:** Add "(Cat A-numeric on sample; analytic statement remains Cat B)". The verdict is unchanged.

### [note] C10/C11 status is stale across MAPS files
- **path:** MAPS_CANDIDATES/BATCH2–BATCH7 RESULTS (OPEN), DISCOVER_PI_RULE/RESULTS.md:8-9 (C10 FAIL), C11_GRADING_ACCEPT/RESULTS.md:17 (C11 FAIL)
- **evidence:** The earlier batches say OPEN (no written object at the time). Later FAILs only hold under agent-constructed objects. Top-level MAPS RESULTS.md has C1–C6 only.
- **fix:** Add a status ledger in MAPS_CANDIDATES/NOTES.md: "C10/C11 FAIL under accepted Π*_max / g; OPEN w.r.t. any corpus-written Π/grading". C6 stays OPEN, consistent across files.

### [note] MISSING_VARS_HUNT spot-check: classifications confirmed
- **path:** /workspace/MISSING_VARS_HUNT_2026-10-24.md
- **evidence:** Verified: ERRATUM :18 a_H radical with the "PSLQ" caveat, so "Cat A in part" is correct. CatB_Notes 0.8174 "fit only…Not derived" is Cat B, though it sits about 1 line earlier than the cited 23-24. rev8 tex :283 and :1033 give ρ(S)=S_lab^{-1}. K3_140 :43 "(S_lab,T) fails (ST)³=S²" checks out. Codex :108 cites the json, and the file is absent (re-confirmed). AUDIT_CORPUS :12 says the k≠0 bound is unwritten. C3_RUN/NOTES :6 says no Π. MAPS RESULTS C6 OPEN/B matches. The NONLOCAL items match the inventory_check files. v12 §40.3 quotes are verified in RTA_FOUNDATION_BOUND_v12.pdf (text lines 12225-12243, 719). No wrong classification found.
- **fix:** Off-by-one line cite only. Optional.

### [note] Stream separation: no mix-in found
- **path:** NONLOCAL_QM_EH11D/INVENTORY.md (rows PT3, NLb), EXPANDED_SEARCH_LOG.md:23; BRIDGE_C_35/order56–58
- **evidence:** The NONLOCAL references to Bridge C order15 and RTA are labelled Cat B, and no claim is drawn from them. Bridge C use of N=4880 is the bare integer only. order56–58 make no bulk or 11D claims. order57/AUDIT.md correctly rejects Φ_orth as non-local (v12 Rem 37.15).
- **fix:** None.

### [note] order57 prior notes partially verified
- **path:** BRIDGE_C_35/order57/AUDIT.md, AUDIT_CORPUS.md, WRITTEN_CANDIDATES.md
- **evidence:** Verified: order56 :17 TODO quote and v12 quotes. The AUDIT verdict "NO P̂_orth / Bridge NO" is consistent with the corpus. Hashes are OK. order5:41, order8 M1, order12:23-24 and the Residual_False_Theta quotes were **not** re-opened this pass. WRITTEN_CANDIDATES was not read in full.
- **fix:** Next pass: quote-verify the remaining citations.

### [note] EH2 Lean build status discrepancy (self-reported)
- **path:** NONLOCAL_QM_EH11D/INVENTORY.md row EH2
- **evidence:** The Lean header says it was built 29 Sep, while the appendix says "no kernel run". It hasn't been re-run.
- **fix:** If a Lean toolchain is available, run `lake build` and record the result. Otherwise keep it as "A (claimed)".

### [note] RTA Foundation Bound v11/v12 located; not audited
- **path:** quantum-comp/reports/papers/RTA_FOUNDATION_BOUND/{RTA_FOUNDATION_BOUND_v11.pdf, _v12.pdf, NOTES_v11.md, NOTES_v12.md, src/main_v11.tex, main_v12.tex, partIII_inv_v12, appD_v11}
- **evidence:** v11 adds Prop MPi (order47) and Thm xinv. v12 widens xinv to real-linear Λ (order49). Ξ, E1–E3 and residual smallness are stated as open. Built 20:37 / 20:39 CDT.
- **fix:** Next pass: trace Thm xinv / Prop MPi to order47/48/49 RESULTS and hashes, and check the Cat B remark labelling.

---
### [note] Coordinator gate decisions (order57–59 trail) — recorded, not re-judged
- **path:** BRIDGE_C_35/order57/{WRITTEN_CANDIDATES.md,ORDER59_BRIEF.md}; order58 (in flight); coordinator FYI 2026-10-24
- **claim:** RG49/RG50 cleared (conditional on a_H script); G1 Ξ book series rejected for adoption; G2–G4 accepted as written-only.
- **evidence:** Coordinator message via Physicist and Mathematician. Priority pass did not re-verify a_H script condition or G1–G4 text against corpus; order57 quotes were only partly checked.
- **fix:** Next pass: verify a_H script condition for RG49/RG50 clearance; confirm G1 rejection and G2–G4 written-only acceptance against WRITTEN_CANDIDATES citations. Tag each as CHAT (gate) vs paper (citation).

### [note] Audit dimension: CHAT-vs-paper source tagging
- **path:** AUDITOR process (coordinator request)
- **claim:** Findings should distinguish chat/agent notes from written paper/tex/Lean corpus.
- **evidence:** Requested by Physicist and Mathematician when approving AUDITOR/ folder.
- **fix:** Apply on expand passes (MAPS, RTA, orders 50–55). Priority pass already separates agent-constructed MAPS objects (warning above) as non-corpus.
