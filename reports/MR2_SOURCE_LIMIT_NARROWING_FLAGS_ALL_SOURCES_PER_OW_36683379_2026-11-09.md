# MR2 — Source-limit narrowing flags (all sources, math-checked) — 2026-11-09 ~18:16 CST (America/Chicago)

**Role:** Math Research 2 (geometric-literature). REPORTS ONLY. No CERT. Tip `7cddb188…` untouched. No Gemini, no external sends.

## Authority (both records cited)

| Record | Path | sha256 |
|---|---|---|
| OW 18:14 (widen beyond arXiv / AI research) | `OWNER_WRITE_VOICE_11fd320e_CITATION_SCOPE_WIDEN_BEYOND_ARXIV_AI_RESEARCH_2026-11-09_1814.md` | `3f1608039bc68b62332a07a7621da749ca303f690993048bef5133282fbc9320` (MATCH) |
| OW 18:15 amend (ALL sources; math must be verified) | `OWNER_WRITE_VOICE_11fd320e_CITATION_SCOPE_ALL_SOURCES_MATH_CHECKED_AMENDS_3f160803_2026-11-09_1815.md` | `36683379e18ac23c46236b37ed45ec1ddf70a93ac9094d2abc476c953433904f` (MATCH) |

**Rule applied:** no source restriction (arXiv, journals, DOI/PMC/AMS, books, wikis, AI-assisted work, other preprints). Cited-but-unverified stays labeled. Math of each cite is checked where quick. **A citation alone never upgrades a status to PROVED.** At most ABSENT → “candidate source found, math check pending.”

**Supersedes:** any draft under the older arXiv-only filename `MR2_ARXIV_ONLY_SCOPE_NARROWING_FLAGS_PER_OW_3f160803_2026-11-09.md` (not filed this pass).

**Method:** Scan all `reports/MR2_*` (and the named FINDINGS_MR2_* packets). Grep for ABSENT / NOT FOUND IN SEARCHED SOURCES / no literature / arXiv-only / unverified / excluded-by-origin. Read closely the known packets. Widened WebSearch/WebFetch beyond arXiv for the top-priority items. Cap ~45 min.

---

## 1. Flagged items (brief table)

| # | File (sha prefix) | Finding | Narrowed by source limit? | Priority | Non-arXiv / widened sources to search |
|---|---|---|---|---|---|
| F1 | `FINDINGS_MR2_SOFTSF_LIT_7_20_KK_LCFT_AND_BETA_KAPPA_2026-11-03.md` (`ea074e50…`) | Q1: γ=7/20 from KK/LCFT/Siegel-lift **ABSENT** | **yes** — search was arXiv API + keyword web + on-disk lit | **P0** | INSPIRE, Semantic Scholar, zbMATH, MathSciNet, journals (JHEP/PRD/NPB), theses, AI-assisted write-ups |
| F2 | same (`ea074e50…`) | Q2: β(κ) → (1+κ*)^{-7/20} **ABSENT** | **yes** — same bound | **P0** | same + radion/dilaton monograph chapters; EPJC/Springer |
| F3 | `MR2_LIT_7_20_KAPPA_FULLTEXT_COVERAGE_2026-11-05.md` (`5ceaff72…`) | EXACT Q1/Q2 **NOT FOUND IN SEARCHED SOURCES** on 16 full texts; Springer EPJC snippet-only | **yes** — explicitly “arXiv-centric”; paywalled non-arXiv left unread | **P0** | Springer EPJC Landau–Potts (doi 10.1140/epjc/s10052-020-08687-0); INSPIRE fulltext; publisher OA mirrors |
| F4 | `NL_ERRATUM12_1800_ACCEPT_PP_fe0c3d92_2026-11-09_1813.md` (`53d4f945…`) | Erratum-12 §8: SSU, Sadun–Segert, Taubes, BLS, Wiki Bolza marked **CONDITIONAL/unverified** solely for sitting outside arXiv-only allowance; Jenni (1984) “not on arXiv, unverified” | **yes** — pure origin rule (OW names these marks) | **P0** | PNAS, Bull. AMS, CMP, JDG, Commentarii Math. Helv.; Wikipedia Bolza (secondary); Jenni 1984 primary |
| F5 | `FINDINGS_MR2_SOFTSF_CAT_A_FOOLPROOF_539_CORPUS_S1_KK_S3_NONARCH_2026-11-03.md` (`993fded2…`) | Cat A §1/§3 shortlist: F2 T₃=539 **ABSENT**; F4 Π_fast/G₄/Ad **ABSENT**; F5/F6 ultrametric map/distance **ABSENT**/PARTIAL | **possibly** — on-disk lit was math.NT-only; public shortlist arXiv/Phys.Rep/books but no Zenodo/AI/wiki/GitHub sweep | **P1** | Vladimirov–Volovich–Zelenov book; Brekke–Freund Phys.Rep; Dragovich reviews; Zenodo; AI-assisted p-adic QCD notes |
| F6 | `MR2_FULL_SM_RECOVERY_GEOMETRY_OBLIGATIONS_2026-11-05.md` (`92e7ba64…`) | O1–O10 mostly **MISS** Soft SF Written defs | **possibly** — MISS is primarily Soft SF disk gap; Zenodo TTC/HMT PDFs “not opened” could hide neighbor cites | **P1** | Zenodo 18442276 / 18509384 full PDFs; string/M-theory geom-eng books (e.g. IBANEZ/URANGA); theses |
| F7 | `MR2_GEOMETRIC_CONSEQUENCES_TWO_AXES_2026-11-05.md` (`3fd1a334…`) | G2 “45 candidates” **ABSENT as Written**; G3 continuum/Israel/R_c Soft SF objects missing; Zenodo TTC/HMT PDFs not opened | **yes** for Zenodo unread; **no** for G2 (documentary Soft SF mismatch) | **P1** | Zenodo record PDFs; Owner/AI write-ups claiming the 45-list |
| F8 | `MR2_GEMINI_COMPENDIUM_CITATION_REVIEW_2026-11-05.md` (`6f773883…`) | C1/C3/C7/C9 Gemini focus strings **ABSENT** in entanglement txts; Zenodo Hyperbolic Measure / Resonant NT PDFs not opened | **yes** — title-only Zenodo refs left unread | **P1** | Zenodo 17877353 (HMT); Resonant Number Theory Zenodo; wikis on BT trees / Appell–Lerch |
| F9 | `MR2_ROUND_TWO_AB_GEOMETRY_JUNCTION_RESPONSE_2026-11-05.md` (`ce5d594a…`) | Appell–Lerch→R_c=1.59543… Soft SF evaluation **ABSENT**; non-Arch Israel **MISS** | **possibly** — Soft SF disk ABSENT primary; literature neighbors for classical Israel/Appell exist outside arXiv | **P2** | classical Israel papers (journals); Appell–Lerch / mock-modular books; AI-assisted R_c derivations (cite-but-unverified) |
| F10 | `MR2_11D_ADS5_S4_SIGMA2_TO_PHI_V35_MAP_PROPOSAL_2026-11-09.md` (`fd191d28…`); `MR2_KK_SPECTRUM_…BF_BOUND…` (`7824e789…`); `MR2_TWISTED_SUSY_VACUA_…COMPARE…` (`98e502c3…`) | Method self-limits: “Public arXiv PDFs only / read only” | **yes** — explicit self-imposed arXiv-only literature diet on 2026-11-09 geometry passes | **P2** | journal versions of MN/GM/BBBW/CLP; books; non-arXiv theses; AI-assisted geometry notes |
| F11 | `MR2_MN2_Z2_WALL_BOUNDARY_CURVATURE_E8_BOLZA_2026-11-09.md` (`bd47ff5e…`) | Uses Bolza systole; inherits Γ2/Jenni unverified status from erratum-12 regime | **yes** — Bolza global-max claim rested on non-arXiv Jenni under old rule | **P1** | Jenni 1984; Schmutz 1993; secondary surveys |

**Not narrowed by source origin (recorded so they are not re-litigated as scope artifacts):**

| Item | Why **no** |
|---|---|
| Soft SF disk ABSENT of Written Appell–Lerch evaluation / QI chart / Israel γ,K objects | Failure is missing Soft SF Written object on disk, not a banned external source |
| Cat A F4 G₄ notation collision (corpus period vs M-theory 4-form) | Content mismatch, not origin |
| G2 “45 list” documentary mismatch (28 PROVABLE-CANDIDATE tags vs Owner “45”) | Internal Soft SF inventory, not literature origin |
| Recent EOM/curvature PROVED-at-samples results | Computation, not lit ABSENT |

---

## 2. Widened searches performed this pass (top priorities)

Access window: 2026-11-09 ~18:15–18:16 CST (America/Chicago). Tools: WebSearch (public). No sign-in, no Gemini, no CERT.

### 2.1 F1/F2/F3 — γ=7/20 and β(κ) closed Wilson form (P0)

**Queries (widened):** anomalous dimension 7/20 + KK/LCFT/Wilson/κ; INSPIRE/DOI-oriented radion/dilaton β; Goldberger–Wise / warped γ.

**Candidate sources found (none EXACT):**

| Candidate | Link | Relevance | Math verified? | Verdict effect |
|---|---|---|---|---|
| Generic KK↔CFT anomalous-dimension reviews (e.g. arXiv:2212.01135 lineage; AdS Virasoro–Shapiro Wilson coeffs) | https://ar5iv.labs.arxiv.org/html/2212.01135 ; APS PRL abstract | GENERIC BACKGROUND — no 7/20 | pending (not target) | **none** — does not move ABSENT |
| GW / dilaton EFT theses & INSPIRE files (radion dual to dilaton; δ nearly marginal) | https://inspirehep.net/files/5b9f1c78bd25a2bf8fd349ccef6f6ceb ; https://inspirehep.net/literature/2626419 | ADJUSTABLE β / δ free — not (1+κ*)^{-7/20} | pending | **none** |
| Springer EPJC Landau–Potts log-CFT (prior snippet) | doi:10.1140/epjc/s10052-020-08687-0 | still no evidence of 7/20 in public snippets | pending (full text unread) | **stays open** as unread non-arXiv neighbor |

**Net for F1–F3:** after widened search, **still no EXACT Q1 or EXACT Q2 candidate**. Status remains **NOT FOUND IN SEARCHED SOURCES** (now including INSPIRE/DOI-oriented hits). **Does not become PROVED.** Optional later: retrieve Springer full text if Owner authorizes publisher OA path.

### 2.2 F4 — Erratum-12 / fe0c3d92 ‘unverified’ marks (P0)

These marks are NL’s, but OW 36683379 / 3f160803 explicitly require re-application. MR2 wall/Bolza work (F11) inherits the Bolza/Jenni piece.

| Cite (erratum-12) | Candidate source found | Link | Math verified? | Status move |
|---|---|---|---|---|
| Sibner–Sibner–Uhlenbeck (Y12) | PNAS 86 (1989) 8610: non-self-dual YM critical points on S⁴, charge 0 | https://doi.org/10.1073/pnas.86.22.8610 | **partially** — abstract claim checked: existence of finite-action nonminimal unstable critical points via min-max; full proof not re-derived | ABSENT/unverified-by-origin → **candidate source found, math check pending** (existence statement); **not PROVED** |
| Sadun–Segert (Y12) | Bull. AMS 24 (1991) 163–170; also CMP 145 (1992) 363–391 | https://doi.org/10.1090/s0273-0979-1991-15978-1 | **partially** — Theorem 1 statement (NSD on quadrupole bundles n±≠1) read from public text; formula k=(n₋²−n₊²)/8 checked numerically for odd pairs (3,3)→0, (3,5)→2, (5,7)→3, (1,3)→1 | same: **candidate found, math check pending** |
| Taubes (Y12) | Likely CMP “Stability in Yang-Mills theories” (doi:10.1007/bf01211160) and/or JDG self-dual stability papers | https://doi.org/10.1007/bf01211160 ; https://doi.org/10.4310/jdg/1214436701 | **pending** — title/DOI located; which exact Taubes lemma NL used for Y12 not re-pinned this pass | **candidate source found, math check pending** |
| Bourguignon–Lawson–Simons (Y13) | PNAS 76 (1979) 1550–1553; follow-on CMP 79 (1981) 189–230 | https://www.pnas.org/doi/10.1073/pnas.76.4.1550 | **partially** — PNAS abstract: weakly stable SU(2)/SU(3) YM on S⁴ ⇒ (anti)self-dual; YM on Sⁿ, n≥5, unstable. Key implication read; full second-variation proof not re-derived | **candidate found, math check pending** |
| Jenni (1984) Bolza global systole max (Γ2) | Cited as Jen84 / Jenni 1981/1984 across surveys; Fortier Bourque–Rafi arXiv:1807.08367 cites global max to Jenni; Schmutz local max 1993 | Secondary: https://ar5iv.labs.arxiv.org/html/1807.08367 ; UNC notes PDF | **partially** — formula sys=2 arccosh(1+√2)≈3.05714183896 **PROVED as numerical identity** and matches alternate 4 arccosh(csc(π/8)/2); second length 2 arccosh(3+2√2)≈4.89690489536 matches Aurich–Steiner citation. **Global-maximality theorem itself** still **pending** (primary Jenni PDF not retrieved this pass) | formula: verified; maximality theorem: **candidate found, math check pending** |
| Wikipedia Bolza page (Γ2 secondary) | public wiki | Wikipedia “Bolza surface” | **pending** as primary; usable only as pointer | secondary only |

**Net for F4:** the arXiv-only “unverified” marks are **source-limit artifacts**. Candidate journal/DOI sources exist for all four Y12/Y13/Γ2 families. **None upgraded to PROVED.** Recommended next Soft SF step: pin the exact lemma NL needs from each PDF and have PP audit the math.

### 2.3 F5 — Ultrametric color distance / SU(3)→3-adic (P1, sample)

Widened search for “ultrametric color charge” / “p-adic QCD” / 3-adic YM confinement found **no** paper that maps continuous SU(3) covariant derivatives onto 3-adic sheets with a proved equivalence. Y-junction lattice QCD remains the established neighbor (already in Cat A shortlist). **ABSENT for the Soft SF map stands** (not a pure origin artifact). Math verified? N/A (no candidate exact source).

### 2.4 F11 — Bolza systole numbers used by MR2 wall file

Independent check (this pass):

- `2*acosh(1+sqrt(2)) = 3.057141838961996`
- `2*acosh(3+2*sqrt(2)) = 4.896904895356152`
- Identity with `4*acosh(csc(π/8)/2)`: **exact match to float64**

**Math verified?** **yes** for the numerical systole/second-length formulas. Global-max theorem: **pending** (Jenni primary). Citation does **not** PROVE the MR2 warped-systole margins; those remain CONDITIONAL/OPEN per prior PP notes.

---

## 3. Priority queue for follow-up (Owner / PP)

1. **P0 — Erratum-12 cites (F4):** retrieve PNAS/Bull.AMS/CMP/JDG PDFs; PP math-audit the exact Y12/Y13 lemmas; relabel from “unverified-by-origin” to “cited-but-unverified, math check in progress / done.”
2. **P0 — 7/20 + β(κ) (F1–F3):** keep ABSENT as search outcome; optionally fetch Springer EPJC full text; do **not** invent β.
3. **P1 — Zenodo unread PDFs (F7/F8/F6):** open HMT / Resonant NT / TTC deposits for neighbor cites only; Soft SF disk ABSENT of model objects stays ABSENT until Written.
4. **P1 — Cat A F5/F6 (F5):** book-level p-adic physics is context only; Soft SF map remains invent-pending.
5. **P2 — Self-imposed arXiv-only diet on 11-09 geometry files (F10):** re-open journal versions / non-arXiv theses under the new OW when deepening MN2/BBBW citations.

---

## 4. Integrity / posture

| Object | sha256 / note |
|---|---|
| tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` — **not touched** |
| This file | see sidecar |
| No CERT · No Gemini · No external send · No tip edit · Nothing adopted |

**Counts this pass:** flagged narrowing items **11** (F1–F11) · explicit **no**-narrowing notes **4** · widened searches run **4** clusters · EXACT Q1/Q2 still not found · erratum-12 journal candidates **found** (math pending/partial) · Bolza length formulas **verified numerically**.

WORKING Soft SF invent-free source-limit flag file. Parent delivers path+sha to Physicist and Mathematician and to Professor Proof as needed.
