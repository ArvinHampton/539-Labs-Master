# FINDINGS T876U — NL L1–L7 ALIGNMENT vs Zenodo primary text (contact/gaps only) — 2026-10-25 ~16:35 CDT
Lane: NONLOCAL_QM_EH11D. Alignment addendum to T875U (T875U body NOT edited). Invent-ban; no mechanism; no Π/α₁; no Soft SF; no kernel run. T876U free.

## 1. Metadata
- Primary: Hampton, Arvin — "The Einstein–Hampton equation: Eleven-dimensional curvature of the S²-11DM²ET-X extension of General Relativity"; DOI https://doi.org/10.5281/zenodo.23010998 (recid 23010998); published 2026-09-28; file Einstein_Hampton_Equation_Rewrite_Appendix_2026-09-28.pdf (DOI/recid/author metadata as relayed by parent; NOT present in extract text — extract header reads "The Einstein-Hampton Equation / 539 Labs · 28 September 2026").
- Extract: `quantum-comp/nonlocal/Einstein_Hampton_Equation_Rewrite_Appendix_2026-09-28.txt` (143 lines) sha256 08b8541a1b40e16961984833915437aa4a96b680fe1404ad3e722191308ede39 — VERIFIED = expected.
- T875U: sha256 at read for alignment 20b7eb0c0fb8d07519995fdc9a2006ff74058b998d63759774d333b45c3a2480 (pre-SF-1, verified). Parent reports post-SF-1 relabel sha e72f5cd811da3d474bcd4d729dcad24eb81dbed6d675a93f83332dd01275de78 (S4 relabelled "Cat A re-derivation" → consistency-check / AUTHOR-WRITTEN algebra; algebra unchanged; closes Auditor MATCH-with-SF 1886ae2a…). On-disk sha at T876U write time: e72f5cd811da3d474bcd4d729dcad24eb81dbed6d675a93f83332dd01275de78.
- Lean: `oct17-master/lean/EinsteinHamptonCurvature.lean` (231 lines) sha256 53f9a4a81c3b05a3e3eb5cedf396a67ec4e6ba3bee0485e020d95f6c4d5b7aa6 — verified.
- Ledger: inventory_check/LEAN_L1L7_ASSUMPTIONS.md (cited, unchanged).

## 2. CONTACT table (Zenodo extract :110–119 vs Lean/T875U)
| L | Zenodo App. B (quote) | Lean / T875U (quote) | Verdict | Note |
|---|---|---|---|---|
| L1 | "Diagonal g g−1=1." | L1_off/time/ext_space/yy/fib: "g·gInv = 1"; off-diag 0 | MATCH | Lean adds off-diagonal zeros (finer). |
| L2 | "∂y gμν=−2A'gμν. Fibre frozen." | L2_lock: deriv exp(−2A)=(−2k)·exp(−2A); "L2_fib_target : Prop := True" | MATCH (ext) / PARTIAL (fibre) | Lean states ext factor under A=ky (−2k = −2A′); "fibre frozen" encoded as trivial True + B constant, not proved as ∂y g_ab=0. |
| L3 | "Only those two Γ from the definition." | L3_lock Γ^y/g=k; Γ^μ_y=−k; fibre Γ = 0 (defs) | PARTIAL | Lean Γ are defs (ledger: "not from metric derivation"); "only those two" not proved as exhaustiveness. Paper "from the definition" vs Lean "defined directly" — contact on definitional status. |
| L4 | "Rμyνy=−∂yΓμνy−ΓμyαΓανy=(A''−(A')2)δ." | L4_Riem_ext := A''−(A')²; L4_lock = −k² | PARTIAL | Lean has the RHS scalar only as a def; the Γ-contraction identity (middle expression) ABSENT in Lean. Numeric agree on lock (−k²). |
| L5 | "A=ky ⇒ −k2 g." | L5_linear: R_ext_Y_ext_Y = −k² | MATCH | Lean scalar is R/g (factor g implicit). |
| L6 | "Contract Fin 11. Rext/g=Ryy=−4k2, Rfib/g=K." | L6_Ric_ext_over_g = L6_Ric_yy := −4k² (defs); L6_lock_Einstein_blocks needs hK: K=8k² | PARTIAL / GAP | −4k² MATCH numerically, but as Lean defs, not a Fin-11 contraction. Rfib/g=K: ABSENT in Lean (no Rfib symbol; rg). Paper L6 = Ricci; Lean L6 = Einstein blocks 6k²−3K, 10k²−2K (these appear in paper :30–32 eq.(L6), not in App. B L6). No −k² vs −4k² mismatch: −k² is R_{μyνy}/g (L4/L5), −4k² is contracted Ric (L6) — both texts agree. |
| L7 | "Solve the two block equations: k2=Φ/1728, K=8k2." | L7_fibre_lock: (h1: 6k²−3K=−Φ/96)(h2: 4k²+K=Φ/144) → k²=Φ/1728 ∧ K=8k² | MATCH | h1/h2 = paper (alg) :34 "6k2−3K = −Φ/96 , 4k2+K = Φ/144" verbatim; hypotheses in both. |

Factor checks: Appendix C :124 "solve = {k2:Φ/1728, K:Φ/216}" — Φ/216 = 8·Φ/1728, consistent with K=8k² (no mismatch). Extract :38 "k = Φ/1728" has superscript ² displaced to next line (PDF text artefact; read as k²). Note the "block equation" h2 (4k²+K) is not the L6 G_fib block (10k²−2K) itself; both corpus texts use h2 as written — recorded, not resolved.

## 3. EH-lock contact
Lean L7 conclusion "k ^ 2 = Phi / 1728 ∧ K = 8 * k ^ 2" = Zenodo EH-lock "k2=Φ/1728, K=8k2" (:38, :87, :119) → **MATCH**. Also matches App. C K=Φ/216. Lock-slice values (−18k², −6k²) in Lean L6 = paper :43 "Gμν = Gyy = −18k g, Gab = −6k2 g" → MATCH. Paper "R = 28k²" ABSENT in Lean.

## 4. Proof-status (corpus disagreement only)
- Zenodo App. C :125: "Lean source: L5, L7. No kernel run here." (also "Hand: L3, L4 from Γ"; "SymPy 28 Sep 2026 …").
- Wrap (S3, 09-28): "L5 is the only finished theorem."
- Lean header (09-29): "Lake 4.34.0 plus Mathlib v4.34.0 built L1-L7 on 29 September 2026 with linter warnings only."
Three corpus statements, dated 09-28 (paper, Wrap) vs 09-29 (Lean header) — disagreement recorded; chronology is consistent with later build but NOT verified. No kernel run by NL. No new proof claim.

## 5. Gaps
- PDF Einstein_Hampton_Equation_Rewrite_Appendix_2026-09-28.pdf: ON box at `/workspace/quantum-comp/reports/self-audit/zenodo/23010998_Einstein_Hampton_Equation_Rewrite_Appendix_2026-09-28.pdf` sha256 b51bb6211aa3c2444ec649e5cdebe93576a966ac506757dd0641f6dce8ea7e68. Alignment used the txt extract `/workspace/quantum-comp/nonlocal/Einstein_Hampton_Equation_Rewrite_Appendix_2026-09-28.txt` sha256 08b8541a…. Substance unchanged. Corrected 2026-10-25 ~16:38 CDT after Auditor ALIGN CONFIRM MATCH-with-SF (Auditor FINDINGS 72ed1a61…): SF-1 optional wording only — prior claim that the PDF was missing from the box was false. DOI/recid/author line not in extract text.
- Lean ABSENT: Rfib/g=K; L4 Γ-contraction identity; "only two Γ" exhaustiveness; R=28k²; Fin-11 contraction (Ric are defs); proof that h1/h2 follow from L6 blocks + T(EH).
- Paper ABSENT: off-diagonal L1 zeros; explicit hypotheses status of h1/h2 (paper "Solve" vs Lean hypotheses — same content).
- Delta: Lean L6 = Einstein blocks under hK; paper App. B L6 = Ricci contraction. Labelling delta, numerics agree.
- Paper :131 "Next check that can move L7: four-form weights Tμν/g=−G2/96 vs Tab/g=−G2/288" — open in paper; NL side per ledger EH-FF1 (cited only).

## 6. Bridge impact
Primary contains no residual_factor, B1, Ω₀, Π, α₁ (rg of extract: none); Φ free. Paper: "L1–L7 contain no time." → **T875U (5) "None" STANDS, unchanged.** Residual-C OPEN (T870U).

## 7. Housekeeping
Stub `/workspace/obs-bridge-NL-61Omega-photon-brane.md` sha256 64e17d5f19e2acc2cdafe6c438b19a11435f24946b21edab6ea478b470d355e4 — untouched, verified. CONTACT/per-L/(5) None untouched. PDF path claim corrected (SF-1 wording). No Local Bridge C / residual-c / T875U body edits. IDLE_AFTER_LOCK.
