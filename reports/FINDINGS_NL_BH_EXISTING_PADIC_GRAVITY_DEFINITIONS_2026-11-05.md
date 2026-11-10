# FINDINGS — Non Local Path — existing published p-adic gravity definitions vs gap 1 — 2026-11-05

Lane: Non Local Path (NONLOCAL_QM_EH11D). Internal protocol artifact. Reports only.
Date: 2026-11-05 13:30 CST (America/Chicago).
Category B. **No CERT.** invent HOLD `1fadc632…` stands. Tip untouched.

## 1. Authority and scope
Owner Arvin Hampton directly authorized this lane at 13:17 CST on 2026-11-05 to absorb open-lane authority a0c2ed5a… (sha a0c2ed5ab2ee7da8af4942eaf7ea86a1d91b3de6645ae4bfe898cddc538e8068) and to pursue in-lane blockers. This step relies on that direct authorization alone, not on any later agent approval. It is a bounded literature check for **gap 1 only** (a defined 3-adic Einstein tensor / field equations), from the inventory FINDINGS_NL_BH_PROOF_GAP_INVENTORY_2026-11-05.md (b2581c1a…, preserved unchanged; PP 738f966f… confirms six gaps remain; Keeper 8044ddb3… hash-only). The other five gaps are not addressed here.

## 2. Search method and limits
- Tools: public WebSearch (one query) and WebFetch of arXiv pages. Three primary papers were read in full text (arXiv HTML). A fourth item, a review, was seen only as search-result excerpts and is marked as secondary.
- Not read: Aref'eva–Dragovich–Frampton–Volovich, Int. J. Mod. Phys. A6 (1991) 4341 (the original "p-adic gravity" paper; no open copy was fetched). Any statement about its contents below is secondhand and labelled so.
- Not searched: journals behind paywalls, books (Vladimirov–Volovich–Zelenov; Schikhof), rigid-analytic / Berkovich geometry literature, post-2017 p-adic AdS/CFT follow-ups.
- So this is not a survey. "Not found" means not found in these sources.

## 3. Sources and what each actually defines

### S1. Gubser, Heydeman, Jepsen, Marcolli, Parikh, Saberi, Stoica, Trundy — "Edge length dynamics on graphs with applications to p-adic AdS/CFT" — https://arxiv.org/abs/1612.09580 (read in full)
- **Domain:** a graph, namely the Bruhat–Tits tree T_q = PGL(2,Q_q)/PGL(2,Z_q) (eq. 6) or an "almost a tree" with long cycles. This is a discrete bulk; Q_p (or Q_q) appears only as the tree's **boundary**.
- **Fields:** positive real edge variables J_e = 1/a_e² (eq. 2). These are real-valued, not p-adic-valued.
- **Curvature:** Ollivier / Lin–Lu–Yau-type Ricci curvature on edges, κ_xy (eqs. 17, 19). The regular tree has constant negative curvature κ = −2(q−1)/(q+1) (eq. 21).
- **Action and equations:** S_Σ = Σ_edges(κ_xy − 2Λ) + Σ_∂Σ k_x, a discrete Einstein–Hilbert action with a Gibbons–Hawking-like boundary term (eq. 28). The equations of motion are γ_xy = 0 (eqs. 34–36), which the authors call "discrete Einstein equations" (§5).
- **p = 3:** allowed (any prime; q = p^n). For q = 3, the linearized prefactor in (22) vanishes (q − 3 = 0). The variational route (37) has no such issue.
- **Stated limits (authors):** Euclidean signature only; "no intention of taking a continuum limit"; no spin-2 graviton in any obvious sense (§6). Λ does not enter the equations of motion (§3.2).
- **Black holes:** BTZ-like quotients T_q/Γ are mentioned. Their study is explicitly left to future work (§2.1, §5 end).

### S2. Gubser, Knaute, Parikh, Samberg, Witaszczyk — "p-adic AdS/CFT" — https://arxiv.org/abs/1605.01061 (read in full)
- **Domain:** the Bruhat–Tits tree as bulk, with the unramified extension Q_q as boundary.
- **Fields and action:** a single real scalar on vertices (eq. 25), with tree Laplacian (27) and mass–dimension relation (32). **No gravitational field and no Einstein equation.** I include it only as the background that S1 builds on, and because it defines the tree's depth coordinate z₀ = p^ω and the Haar integration on Q_q (eqs. 13–17).

### S3. Djordjević, Dragovich, Nešić, Volovich — "p-adic and adelic minisuperspace quantum cosmology" — https://arxiv.org/abs/gr-qc/0105050 (read in full)
- **Domain:** minisuperspace (finitely many variables: scale factor, lapse N, scalar), with p-adic and adelic arguments. Wave functions are complex-valued.
- **Construction:** a p-adic counterpart of the Einstein–Hilbert action "using form-invariance under change of real to the p-adic number fields". Path integrals use the additive character χ_p and the real-valued Haar measure (eqs. 35–37, 41–43). The real Einstein–Hilbert-plus-boundary action (47) is restated for de Sitter models.
- **Explicit statement (§1):** "As there is not an appropriate p-adic Schrödinger equation, there is also no p-adic generalization of the Wheeler-De Witt equation." The authors use path integrals instead of differential equations.
- **p = 3:** covered (general p ≠ 2). Results are conditions like |λ|_p ≤ p⁻² and adelic discreteness of λ (§§5–7).
- **Black holes / exterior matching:** none.

### S4 (secondary, excerpts only). Dragovich, Khrennikov, Kozyrev, Volovich — "On p-adic mathematical physics" — https://arxiv.org/abs/0904.4205 (§5, as quoted in search results); also the review https://arxiv.org/abs/1705.04758
- Reports that Aref'eva et al. (1991) "explored" p-adic Einstein equations R_μν − ½Rg_μν = κT_μν − Λg_μν "where g_μν is p-adic valued gravitational field", with "elements of p-adic differential geometry" and "p-adic analogs of some known solutions" (1705.04758 excerpt).
- I did not read the 1991 paper. Which solutions it gives, over what domain, and whether a Schwarzschild analogue appears are **unverified**.

## 4. Two kinds of "p-adic gravity" (distinction settled from S1–S4)
| | Graph / Bruhat–Tits curvature (S1) | Formal p-adic-valued Riemannian geometry (S3, S4) |
|---|---|---|
| Spacetime | Discrete tree or graph; Q_p is the boundary only | Coordinates and metric are p-adic numbers |
| Metric / field | Real edge lengths | p-adic-valued g_μν (formal) |
| Curvature | Ollivier-type transport curvature on edges | Christoffel → Riemann → Ricci, transcribed by form-invariance |
| Equations | Discrete γ_xy = 0 from a variational principle | Einstein equations written with p-adic entries; per S3, no p-adic Wheeler–DeWitt equation; used inside path integrals |
| Physical reading (authors) | Euclidean toy model; no continuum limit; no graviton | The Dragovich slide at userpage.fu-berlin.de/~aschmitt/Dragovich.pdf (search excerpt) says the p-adic-valued version "has not direct physical meaning, but can be used in argument of the path integrals" |

Note: a third framework, genuine p-adic differential geometry on totally disconnected spaces (locally analytic manifolds), exists in mathematics. None of the sources I read builds a gravity theory on it, and I did not research it.

## 5. Comparison with the ansatz (no applicability asserted)
The user ansatz is a 4D ℤ₃ core with g_rr → (1 − 2GM/(|r|₃ + 3⁻⁵³⁹))⁻¹.
- **Real vs p-adic values:** in the ansatz, |r|₃ is a real number (a power of 3) inserted into a real Schwarzschild coefficient. That is neither S1 (no |r|_p-valued radial metric; edge lengths are real but live on a tree) nor S3/S4 (fields themselves p-adic-valued). Which of these the ansatz intends is **not defined**.
- **4D ℤ₃ core:** S1's tree has Q_q, an n-dimensional Q_p-vector space, as its boundary. ℤ₃⁴ (as in the Haar item 70 integral, Local lane) is a different object. No source maps ℤ₃⁴ to a tree bulk or to a 4D p-adic manifold carrying the stated metric.
- **Regulator 3⁻⁵³⁹:** no source contains an additive regulator of this form. S2 and S1 use tree depth cutoffs ε = p^Ω (S1 eq. 62; S2 eq. 90), which are scheme choices with stated O(1) ambiguity, not physical floors. Any identification of 3⁻⁵³⁹ with such a cutoff would be new and is not made here.
- **Exterior matching:** no source matches a p-adic or tree interior to a real Schwarzschild exterior. S1's boundary term is internal to the tree. Gap 6 (Israel matching) stays as listed in the inventory; this step does not address it.
- **Signature:** S1 is Euclidean only. The ansatz is Lorentzian Schwarzschild.

## 6. Settled vs unresolved
Settled from the sources I read:
- Published definitions of "p-adic Einstein equations / Einstein-like actions" exist in at least two inequivalent senses: S1 (discrete, on the Bruhat–Tits tree, with explicit action and equations) and S3/S4 (formal p-adic-valued transcription; S3 states there is no p-adic Wheeler–DeWitt differential equation).
- Both admit p = 3.
- Neither, as read, contains a black-hole core, a |r|_p-regulated g_rr, a 3⁻⁵³⁹ regulator, or exterior matching.

Unresolved:
- Which framework, if any, the user's ansatz is meant to sit in.
- An explicit identification from the ansatz variables (r, |r|₃, ℤ₃⁴, 3⁻⁵³⁹, M₃₅) to either S1's tree variables (J_e, depth z₀, q) or S3/S4's p-adic g_μν. No source supplies one.
- The contents of Aref'eva et al. (1991), unread here.

**Gap 1 status: REMAINING.** Existing definitions narrow what a definition could look like, but none is shown to apply to the ansatz, and shared vocabulary is not treated as applicability. Closing the gap needs an Owner-Written choice of framework and identification map; under invent HOLD I proposed none.

## 7. Compliance
No new hypotheses or proofs. No invented citations: every URL above was fetched or returned by search this turn, and S4 and the 1991 paper are marked secondary/unread. No CERT, external messages, routines, or tip edits. Tip sha 7cddb188… matched before and after. The prior inventory b2581c1a… is unchanged. Next: PP audit, then Keeper (parent handles the handoff).
