# AUDITOR — Corpus crawl batch 08a — intake owner-20261105-1715 vs PP relays — 2026-11-09

Role: Auditor. Reports only. Written 2026-11-09 ~13:20 CST (America/Chicago). Authority: Owner "All haults lifted" (12:34 CST, pt1864u). Limits kept: exclusive create; no frozen/hashed record edited; no sidecars created; no CERT; no Gemini; no external sends; no verdict changed. PDFs were text-extracted (pdftotext -layout) only in /tmp/aud08. Tip sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91: MATCH.
Split: 6 intake artifacts + 8 relay records = 14 > 10 → 08a (folder 1715) / 08b (1854, 1910, 1944 + blockers + recommendation).

## 1. Custody
| Tag | File | sha256 | Sidecar | mtime CST |
|---|---|---|---|---|
| P1715 | intake/owner-20261105-1715/01M6PZWMGT7HB8CRARJ1RXF4BE.pdf (22 pp, "Gemini Review and Resolutions", Google Docs renderer; 722 extracted lines) | 65b08abbeb0a5f86a464ccfd7c7636d7dde5885789141fdc121f21a134211242 | NONE | 11-06 14:40 |
| T1806 | intake/owner-20261105-1715/OWNER_TRANSFER_NORMALIZATION_BIANCHI_1806.txt (95 newline-terminated lines) | 50ae4db7d91eb975da21648f03f71a86c7db217a7520226f6744adb7b13f6bcb | NONE | 11-06 14:40 |
| PP | reports/FINDINGS_PP_OWNER_PDF_1715_MATH_REVIEW_2026-11-05.md | 17ab357b2e88c99296a18f4750ce8360a780bda152d24653831ba98e776f5bc2 | NONE | — |
| AdA | …_ADDENDUM_A_2026-11-05.md | ae8aa76fc3ae5b906886e147abdba39b83bfe66e646953c42299825a9a4feb27 | NONE | — |
| AdB | …_ADDENDUM_B_BETA_2026-11-05.md | 8bf983618669514d473ca8174fd8c0b7000f1f50df96bd1a80469260049de38d | NONE | — |
| AdC | …_ADDENDUM_C_BLUEPRINT_1734_2026-11-05.md | d6344622ebf73c09435b84f78cc280fbdb4b828a0b59ed072fb845b100cd8f49 | NONE | — |
| AdF | …_ADDENDUM_F_1806_2026-11-05.md | 607feed0d5d71a06ef547368a9979d68346d8f5a1e4f2074ecb41883bb9c5013 | NONE | — |
Hash citations: P1715's sha is cited NOWHERE in the corpus (0 hits outside intake; PP cites it by filename only) (B8-1). T1806 sha 50ae4db7 is cited only by Auditor batch 06a; AdF.1 cites filename + line count. No intake file has a sidecar.
P1715 :721–722 is an Owner note: "Verified Gemini response to Auditor report. Give to PP for mathematical certification." Content is Gemini-generated; read here as data only.

## 2. P1715 vs PP (base review) — line-level
PP's L-numbers match a layout extraction exactly (§1 L1–28, §2 L30–52, §3 L54–73, script L200–259) → relay MATCH.
- PP :5 row p=7 identically 0 → det K₁₄₀ = 0 → PROVED (re-run exactly: rank 23 of 25, det 0, 65 nonzero entries). P1715 :70–73, :184–188, Thm 2 :605–660 "det ≠ 0" → REFUTED-by-proof.
- PP :6 (35/9) = +1 vs K(3,3) = −1 → PROVED. Auditor extension: the inert list {3,9,13,27} (P1715 :67, :179, :385) is wrong at 9 AND 13 (both χ₁₄₀ = +1); the true χ = −1 set has 24 residues (3,11,27,37,39,41,47,51,53,57,61,69,71,79,83,87,89,93,99,101,103,113,129,137), matching AdC :8. REFUTED-by-proof.
- NEW (not flagged in PP/A–F): P1715 :647–649 "8007581 ≡ 121 (mod 140) … distinct split class" → REFUTED-by-proof: 8007581 is prime and ≡ 1 (mod 140) (AdC :13 states ≡1 without flagging the PDF) (B8-2).
- PP :7 descent/D1–D3 non sequitur → consistent; OPEN items stand. PP :8 script does not parse (`elif residue in:` at P1715 :214) → MATCH.
- PP :9 Gal(ℚ(ζ₄₉)/ℚ) cyclic order 42, conductor ℚ(√35) = 140 → PROVED.
- PP :12–13 junction: zero LHS forces S = 0; y = const slice of 5D is 4D → PROVED; AdA :4–7 qualification (vacuum junction consistent; Thm 1 arithmetic [K] = −6k correct only with dim Σ = 3; 5D gives −8k, LHS 6kγ; "iff Weyl" unproved) → PROVED/consistent with P1715 :458–515. Auditor adds: P1715 §1 :20–24 (LHS = 0) and Thm 1 :454 (LHS = 8πG₄S ≠ 0) are mutually inconsistent conditions → REFUTED as a single specification.
- PP :18 "a_μ … muon g−2 measured value" → MISLABEL (already C3-4: it is the 2020 SM prediction). AdA :10 regrade to "stipulated parameter" → consistent.
- PP :18 κ = √(2/0.7858) = 1.5953611 → PROVED arithmetic; provenance of κ/Λ₀ OPEN (278 corpus files cite 1.595361; not crawled).
- AdB β-table: β(κ) = (1+κ)^{−7/20} values in P1715 :697–703 → re-computed, all β values correct; PP's Δ re-computations confirmed (e.g. Δ(1.595350) = +1.0624e−6 vs printed +1.03e−6). "LOCKED BOUNDARY"/"REFUTED DEFECT" labels have no defined target → OPEN (not math).
- PP :19 N − |W| = 0 unproved → P1715 :576–577 sets Σ3^{−k} − Σ3^{−k} ≡ 0, i.e. assumes N = |W| → circular; Lemma 1 REFUTED-as-proof (claim OPEN). AdA :11 withdrawal of "∇₃ undefined" → correct (P1715 :550–551 defines it).
- PP :22 RTL encodes the same rule → MATCH (P1715 :376–396).

## 3. T1806 vs AdF / AdF.1 — line-level
AdF :2 began relay-based ("attachment path NOT readable"); AdF.1 :42 later read the intake copy. All AdF.1 line citations (6, 8, 14, 25, 27, 30, 47–49, 52, 57, 70, 75–82, 89–92, 96) land on the stated content → relay MATCH.
- AdF :4 U₁₄₀ ≅ C2×C4×C6, non-cyclic, order 48 → PROVED; T1806 :6 "cyclic" → REFUTED.
- AdF.1 :45 symmetry iff a_c = a_{c⁻¹w⁻²} → PROVED (re-derived).
- AdF.1 :46 self-loop c = w⁻¹ makes row sums C_xx → PROVED under the reading that Σ_{z∼x} includes z = x (T1806 :25 is ambiguous) → CONDITIONAL on reading.
- AdF.1 :47 q ≡ 0 ⇒ Φ = 0 contradicts ‖Φ‖ = 1 (T1806 :27 vs :57) → PROVED.
- AdF.1 :48 quadratic form ≠ trace (example) → PROVED.
- AdF :25–30 / AdF.1 :50: Kasner (−1/3, 2/3, 2/3) gives R₁₁ = ½t^{−10/3} ≠ 0 in the quoted IX equation → PROVED (re-computed); p₂ = p₃ so "distinct" false → PROVED.
- AdF.1 :53 none of the four "RESOLVED" rows resolved → consistent.
No relay discrepancy found in F/F.1 beyond the line-count nuance (95 by wc vs 96 displayed; last line unterminated).

## 4. Batch 08a findings
- B8-1: P1715 (65b08abb…) and T1806 (50ae4db7…) uncited by hash in PP records; intake files carry no sidecars.
- B8-2: P1715 :647–649 "8007581 ≡ 121 (mod 140)" false (≡ 1), unflagged in PP chain.
- B8-3: P1715 inert set wrong at 13 as well as 9 (PP flagged 9 only).
Continued in 08b.
