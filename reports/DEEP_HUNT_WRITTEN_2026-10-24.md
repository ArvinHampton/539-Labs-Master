# DEEP HUNT (written sources) — 2026-10-24 (America/Chicago)
Search/extract only. Nothing invented. Extends MISSING_VARS_HUNT_2026-10-24.md.
Key source: reports/heavy-daily/2026-10-19-Bridge-C-Clean-v2/Bridge_C_Clean_v2_fulltext.txt
sha256 7128a3c7a053e37d146d93f1daa2c81712c1cfdcde87ca822650d9288f432a97 (4187 lines)

## SECTION I — LOCAL (Bridge C modular)
### FOUND
L1. rho = rho5 ⊗ rho7 ⊗ rho2 — reports/heavy-daily/2026-10-19-Bridge-C-Clean-v2/Bridge_C_Clean_v2_fulltext.txt:1562 "ρ = ρ5 ⊗ ρ7 ⊗ ρ2 , where ρp is the Weil representation of (Z/p, qp ) with q5 = 2x2 /5 and q7 = x2 /7". Parity: reports/heavy-daily/2026-10-19-Bridge-C-Clean-v2/Bridge_C_Clean_v2_fulltext.txt:1567 "P = ρ(−I) = Z5 ⊗ Z7 ⊗ I4"; :1565 ρ2 = A3 ⊕ B1 (even characteristics 00,01,10 / odd 11).
L2. rho_lab definition and Weil realisation — reports/heavy-daily/2026-10-19-Bridge-C-Clean-v2/Bridge_C_Clean_v2_fulltext.txt:2912 "ρlab : S 7→ Slab^{-1}, T 7→ Tlab"; :2914 "Theorem 18.2 ... ρlab ≅ ρN2 ... No character twist is needed and no metaplectic sign arises"; :3179 "s = 7, ρ = ρlab is the 140-label representation". (Local order65 "0 hits for ρlab" is WRONG — text extraction spells it "ρlab".)
L3. Weight-parity law tying P-even sector to weight (closest written item to target 1a) — reports/heavy-daily/2026-10-19-Bridge-C-Clean-v2/Bridge_C_Clean_v2_fulltext.txt:2822-2829:
  "(e) Three parities are one (algebra Category A; same-ρ identification Category B). The label parity P = Slab^2, the cone-weight parity ν 7→ −ν and the integer versus half-integer radial orders coincide. A weight-k vector-valued form satisfies ρ(S)^2 f = (−1)^k f, so the E/Eisenstein sector lies in WP and the Zwegers/ϑhol sector in Fix(−P) (dimension 68 = 4(3·3 + 2·4) at s = 7). Hence weight-1 vectors cannot realise any part of V⊥ ⊂ WP. Category B: that Zwegers' completed theta transforms under this same 140-dimensional ρ with the Slab = ρ(S)^{-1} sign."
  Status: gives even weight ↔ P-even (WP) generally; does NOT give an explicit weight-0/2 M-law, and the Zwegers-under-ρlab step is Category B / listed OPEN at reports/heavy-daily/2026-10-19-Bridge-C-Clean-v2/Bridge_C_Clean_v2_fulltext.txt:4027-4028.
L4. Δ definition (target 1c, definition part) — reports/heavy-daily/2026-10-19-Bridge-C-Clean-v2/Bridge_C_Clean_v2_fulltext.txt:2422 "The lattice origin of ∆ = (s − 2)(7s − 32)"; :2439 "∆ = 4Q(c1)Q(c2) = B(c1,c2)^2 + det Gram(c1,c2) = 16(s − 2)^2 − 9s(s − 2)"; status line :2442 "Category A". Gram there: :2423 "A = (2 s; s 2s) ... Q2(n,k) = n^2 + snk + 2s k^2" (at §17+ :2842 "A = (2 7; 7 7) is the Gram matrix of Q7"). No modular transformation law for Δ itself found.
L5. P_orth definition (prior hunt listed ABSENT — now FOUND):
  - oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/U1_LEDGER_P_TL_No_Classical_Realisation_g7_C_2026-09-01.md:35 "P_orth := unsigned orthant sum of q^{Q_s} over n,k >= 0." sha 3a5f7aeaf545c381a597b7fabca3e972f98acbe06c2edddd619caceaec0c14f1
  - reports/bridges/BRIDGE_C_35/PREREG.md:16 "Q_7(n,k) = n² + 7nk + (7/2)k(k+1); orthant series P_orth = Σ_{n,k≥0} q^{Q_7(n,k)}; cones c1 = (−1,1), c2 = (−4,1); w(v) = ½(sgn B(c1,v) − sgn B(c2,v))" sha e4902f508e68e76920429f98e3b4a7330a5a7013beb295bec57de771956ccdac
  (Unhatted P_orth; no separate "P̂_orth" operator definition found.)
### NEAR-MISS
- "corner": reports/heavy-daily/2026-10-19-Bridge-C-Clean-v2/Bridge_C_Clean_v2_fulltext.txt:2198 "Proposition 14.2 ... (i) the corner terms cancel between Q+ and Q−" and :654 — corner terms of the asymptotic expansion, NOT paired with ρlab or EVEN sector.
- Zwegers completion general: reports/heavy-daily/2026-10-19-Bridge-C-Clean-v2/Bridge_C_Clean_v2_fulltext.txt:698-699 (Lemma 5.2, signature-(1,1) ϑ^c_{a,b}), :2192 completion "by citation (Zwegers [18], Cor. 2.9)", :2606-2608 Ξ0/Ξ1 chains (Zwegers 2002/2012) — tied to Q_s Gram (2 s; s 2s), not to an "A(2)=(1,1)" label.
- Ξ: reports/heavy-daily/2026-10-19-Bridge-C-Clean-v2/Bridge_C_Clean_v2_fulltext.txt:2606 "Ξ0 + Ξ1" are integrand kernels (cone integrals), not a Ξ series definition matching target.
### ABSENT
- Explicit corner/EVEN ↔ ρlab pairing formula; explicit weight-0/2 M-law for P-even.
- Any text naming "Gram A(2)=(1,1)" and mapping it to ϑ^c_{a,b}. Only hits for "A(2)" are order65/66/67 brief/prereg/results files restating the target (reports/bridges/BRIDGE_C_35/order67/PREREG.md:4 writes A(2)=[[4,14],[14,14]]) — not a source formula.
- Modular law for Δ.

## SECTION II — NONLOCAL (EH11D / periodic-table) — kept separate
### FOUND (symbol-level only)
N1. Ω₁₁D appears only as a symbol: theorems/periodic-table-codex.txt:46 "scaled by the single geometric factor Ω₁₁D (fixed once by 11D compactification geometry)"; :54-60 multiplies each F term. sha fc74986a000b0f4d535aff78ef7efa5af9d2096fc39e21123b15a6a145bfa409. No numeric/closed form.
N2. CJS a=1/12 — CHAT ONLY (not Cat A paper): reports/s_family_paths/A22_grok_export_search/chats/cd250095-2abb-4dee-b86a-e4481020d5ef.txt:2837 "Cremmer–Julia–Scherk uses a=1/12 and would give K=4k^2." sha b92ff59268bd84b356c220b17ca5b0f9a47d3a7b985577adb399824efed00cd3. Paper-side convention a=1/24, weights −G2/96, −G2/288, k^2=Φ/1728, K=8k^2: oct17-master/docs/.../Einstein-Hampton-2026-09-28/Execute_Three_Advancement_Paths_2026-09-28.md:4. CJS stress weights (−G²/96 / +G²/288, k²=Φ/576) only in chat per reports/bridges/NONLOCAL_QM_EH11D/inventory_check/TWO_FORK_AMBIGUITY.md:7.
### ABSENT
- Ω₁₁D(k,K,b,Φ) closed form or numeric; Z_eff(Z,n,l) screening rule (Z_eff only a symbol, periodic-table-codex.txt:53-54); F_total→ionization/fine-structure map + NIST tolerance; letter→M_S rule; flux→Φ; warped metric + flux quantization; F_total table.
### Search log
rg -S over *.md,*.txt,*.lean,*.json,*.tex,*.py under /workspace/quantum-comp (16,940 text files incl. theorems/, reports/self-audit, reports/bridges, _git* clones, oct17-master, chats, heavy-daily fulltext extracts) with patterns: Ω₁₁D|Omega_{11D}; Z_eff(; F_total =; P_orth =|:=; a = 1/12|CJS; A(2)=(1,1)|Gram A(2); rho_lab|ρlab|ρ5⊗; Zwegers|ϑ^c; Δ/∆; corner|P-even; Ξ; M_S; flux→Φ; warped. Broad patterns (Ξ, M_S, warped, flux) gave hundreds of hits; not exhaustively hand-read — flagged as residual risk. No *.lean files contained targets. Store /cursor/stores/store-030b… holds only grok-bot/ (no project text).
