# FINDINGS — MR2 Soft SF literature check: γ=7/20 (KK/LCFT) and β(κ) — 2026-11-03

## Scope / authority
- Role: Math Research 2 Soft SF, Project Quantum Comp. Cue: OW 8a0325da… Cat A scope; Owner call-ea806234 via Physicist.
- REPORTS ONLY. No CERT. No tip edit. No fan-out.
- Hashes (sha256sum, 2026-11-03 ~11:00 CST):
  - tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` BEFORE 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 / AFTER same — **tip_touched NO**
  - OW defs 9aec847a7ccb8a815255c1d3c645367fbf12205a079085ddf40f7975cf8e095f (match)
  - OW Cat A lift 8a0325da19ba3802652a654523b681cf74a623d28a4f1a4484999420098a453b (match)
  - PP Cat A rerun FINDINGS b6c74d80bb641741a53075ca2221968fde1e2d26eb87ebffb2248bb93365a554
- Prior context only: PP-FINDINGS-TUBULIN_22_TO_13_WILSON (PP FALSE under const R_x).

## Q1 — γ = 7/20 from KK reduction / LCFT / KK tower matching Siegel lift
**Soft SF: ABSENT (with rigor of search below).**
- Searched: arXiv API (abs:"logarithmic conformal" AND abs:"anomalous dimension" → 4 hits, none containing 7/20); web search "7/20" anomalous dimension Kaluza-Klein / logarithmic CFT → no primary source; on-disk `/workspace/quantum-comp/lit/*.txt` grep "7/20" → 0 hits.
- No paper found deriving 7/20 as an anomalous dimension or scaling exponent from KK reduction, from LCFT Jordan-cell anomalous dimensions, or from non-compact KK tower scaling limits matched to Siegel-lift fields.
- RELATED MISS (context, NOT a 7/20 match):
  - arXiv:1908.10437 (Banerjee–Dey, JHEP 12 (2019) 114): LogCFT large-spin double-trace anomalous dimensions; coupling-dependent, no 7/20.
  - arXiv:1210.8159 (Mitev–Quella–Schomerus): exact anomalous dimensions in supergroup WZW (logarithmic) via quasi-abelian perturbation; coupling-dependent, not 7/20.
  - arXiv:2005.07708 (Gorbenko–Zan): O(n<2) LCFTs, RG flow between fixed points; no 7/20.
  - arXiv:1902.02738 (Losev–Mnev–Youmans): log TCFT, coupling-dependent anomalous dims; no 7/20.
- Owner OW §3 claim "Exponent −7/20 from non-compact KK tower scaling limits in LCFT landscape matching Siegel lift fields" — **invented pending mathematical proof** (no cite in corpus; no public cite found).

## Q2 — β(κ) / running R_x with ∫κ dlnμ = ln(1+κ*)
**Soft SF: ABSENT.**
- No written β_κ ODE found in Owner corpus (PP row 4 gap (i) confirmed) nor in public literature producing (1+κ*)^{-7/20} as a Wilson-integral closed form.
- Structural note (no invention): with C1(μ)=C1(μ0)exp(−(7/20)∫κ dlnμ), a fixed-point snapshot κ→κ* gives (μ/μ0)^{−(7/20)κ*}, μ-dependent; the closed form requires ∫κ dlnμ = ln(1+κ*) over the flow, a condition on the full trajectory that no cited β satisfies. Not supplied here (per method step 5).
- RELATED MISS: Goldberger–Wise radion stabilization hep-ph/9907447; holographic RS/dilaton RG (Rattazzi–Zaffaroni hep-th/0012248) — radion/GW-scalar running exists, but no κ with this integral identity and no 7/20.
- Owner OW §3 "Wilson closed form holds as invariant snapshot only when continuous flow approaches a localized fixed point" — **invented pending mathematical proof**.

## Net
Cat A Wilson (1+κ*)^{-7/20} has **no literature Soft SF support** for γ=7/20 nor for the β-integral identity. PP row 4 gaps (i) β_κ and (ii) γ derivation remain open / invent-pending.

## Shortlist checked (≤8)
1908.10437; 1210.8159; 2005.07708; 1902.02738; 2311.01437 (Checkerboard CFT anomalous dims, no 7/20); 1106.4893 (logarithmic minimal models, no 7/20); hep-ph/9907447; hep-th/0012248.

## For PP Soft SF audit
- Q1 ABSENT; Q2 ABSENT; both OW §3 claims labeled invented pending mathematical proof.
- Limits: search was keyword-based (arXiv API + web + on-disk grep); full-text exhaustiveness not claimed. tip_touched NO.
