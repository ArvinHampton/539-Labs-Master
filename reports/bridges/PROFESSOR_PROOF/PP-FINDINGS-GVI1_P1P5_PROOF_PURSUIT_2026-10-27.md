# PP-FINDINGS — Professor Proof: G-vi-1 P1–P5 proof pursuit (s∈{7,8,11}) — 2026-10-27 (CDT)
Mode: Soft SF Write-only, copied to the Auditor. REPORTS ONLY. No RECs. No new values invented (HARD GATE). Kerr / Path4 / link (b) not touched.

## 1. Authority (live sha256, verified 2026-10-27 CDT)
| item | sha256 |
|---|---|
| tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` BEFORE | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 MATCH |
| Handoff | 1b90d840a9f1f254c0dce987a4c1304756fa583cd2fa45276a4d86d6ee774233 MATCH |
| Canon invent | 480f6d7298face1e9b15b51fd3d747a83b5c7384556721fcdae80994d4e1344d MATCH |
| Local pursuit | dccf3a8c0369985062f44fabb615e0d357d181f7218af99d0b093f49c43dc43c MATCH |
| Growth class Written (`FINDINGS_LOCAL_WRITTEN_ASYMPTOTIC_GS_PATH4_CARD4_2026-10-26.md`) | b19e12e6c313c98c40e28ce406ec08b3796fe8b0ad0f87a13365da1891c2d949 (as cited in canon) |
| OW route | 0e729e893982fccf7e3232f23bf7eca8b4534d9b4538fe7a4fc2c201f6e57cd9 |

Object (Written, RTA def R5): g_s(q) = Σ_{n≥0} q^{n²}/(−q^s;q^s)_n. Corpus marks quantum modularity of g_s and a scalar transformation law OPEN (DEFINITION_RTA… lines 83–84; Rank 27: no level/multiplier/shadow).

## 2. Literature pass (bounded)
- `lit/`: Chen–Kiming–Wiese 1105.1918, Chen–Kiming 1301.3087, Hu–Tan 1309.1658, Gräf 1705.02158, Anni–Böckle–Gräf–Troya 1807.10082 — none on mock theta / Rademacher at weight ½.
- `lit/bm/`: 0804.1164, 0810.2106, 1005.2008, 1208.3179 (Bringmann–Manschot-class files present) — treat s=1 / fifth-order-type objects; none gives a transformation law for g_s with s≥2.
- `literature/navratil`, `papers/` (project PDFs): no transformation law for g_s.
- Zwegers, Bringmann–Ono, Dragonette primary texts: NOT on disk. Not cited as Written; no cite invented.

## 3. Independent numerical check (exact integer arithmetic; evidence, NOT proof)
Script: `PP_GVI1_gs_coeff_check_2026-10-27.py` (same folder). Exact coefficients a_s(n) of g_s up to n=16000; statistic L(N)=log max_{N−20≤n≤N}|a_s(n)| / √N.
| s | L(4000) | L(8000) | L(12000) | L(16000) | invented β_s |
|---|---|---|---|---|---|
| 7 | 0.3110 | 0.3312 | 0.3416 | 0.3481 | 0.09161 |
| 8 | 0.3013 | 0.3197 | 0.3285 | 0.3339 | 0.08016 |
| 11 | 0.2469 | 0.2653 | 0.2749 | 0.2788 | 0.05830 |
Coefficients have mixed signs; |a_7(n)| reaches ~1.3×10^19 near n=16000, while A_s n^{−1/2} e^{β_s√n} with the invented package gives ~10^3. L(N) rises monotonically across the range and is ~3.8–4.8× the invented β_s. A finite computation cannot refute an asymptotic statement, but the invented package (β_s, A_s, α) is **numerically incompatible over n≤16000** by ~16 orders of magnitude (s=7).

## 4. Per-item verdicts
| # | Claim (invented pending mathematical proof) | Verdict | Precise reason |
|---|---|---|---|
| P1 | N_s = 4s | **NF-WHY** | Needs a modular/mock-modular transformation law for g_s (s≥2). None exists in corpus or on-disk literature (Rank 27; RTA OPEN). The "4·" convention only says weight-½ forms *if they exist* live on Γ₀(4M); it does not show that g_s is one, or fix M=s. Not feasible pending a Zwegers-type completion of g_s. |
| P2 | m_s=1, Δ=1/24, pole at ∞ only | **NF-WHY** (numerically disfavored) | Without P1 there are no cusps to compute principal parts at. Eta-type multiplier admissibility on Γ₀(4s) not established. A single polar term q^{−1/24} at ∞ with c=N_s dominant cannot produce the observed growth (§3); the observed L(N) needs larger effective √Δ/c, i.e. a polar contribution at a cusp with smaller c (or a larger Δ), contrary to "pole at ∞ only". |
| P3 | β_s = 4π√Δ/N_s = π/(2√6·s) | **PARTIAL (PUIP algebra) / NF-WHY (as fact)** | PUIP: *under invented hypotheses H = {P1, P2, g_s a weight-½ harmonic Maass/mock form with convergent Rademacher-type expansion}*, the c=N_s term gives β=4π√Δ/N and the numerics π/(2√6·s) follow — algebra checked (4π√(1/24)/(4s)=π/(√24·s)=π/(2√6·s)). As a statement about g_s: NOT proved; H unproved; Bringmann–Ono convergence not on disk; and §3 numerics contradict the value over n≤16000. |
| P4 | α = −1/2 | **PARTIAL (PUIP algebra) / NF-WHY (as fact)** | PUIP: under H, I_{1/2}(x)~e^x/√(2πx) gives n^{−1/2}·(Δ/n)^{1/4}-cancellation ⇒ α=−1/2 (re-derived, consistent with canon §4). Dragonette (s=1, f(q)) is a pattern check only. No proof for g_s; not separable from §3 data at this range. |
| P5 | A_s = 1/√(8s), a(−Δ)=1, K=1 | **NF-WHY** | PUIP algebra under H: A=a(−Δ)·K/√(2N) = 1/√(8s) if a(−Δ)=K=1. But a(−Δ) and the Kloosterman value require the actual principal part and multiplier (P1/P2), which do not exist in the corpus. Also |K_c| for c=N_s is not generically 1. Numerics (§3) contradict the A·exp scale. |

Tally: PROVED 0 · PARTIAL 2 (P3, P4: PUIP algebra under invented H only) · NF-WHY 3 (P1, P2, P5). All five keep the label **"invented pending mathematical proof"**. None is Owner-Written.

## 5. Flags to Auditor (reports, not RECs)
- F1: The §3 exact-coefficient data is a falsification-grade signal against the invented β_s/A_s package (and against "pole at ∞ only"). It is reproducible from the script.
- F2: Literature needed for any proof (Zwegers thesis; Bringmann–Ono 2006/2012; Dragonette) is not on disk.
- F3: The real missing object is a transformation law for g_s (s≥2); P1–P5 all depend on it.

## 6. Non-claims
No tip edit. No Kerr/Path4/link (b). No C1 evaluated. No new invented values. Numerics are evidence, not proof.

## 7. Tip AFTER — see sidecar / press twin (recomputed post-write). tip_touched NO.
