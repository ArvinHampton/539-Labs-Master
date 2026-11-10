# FINDINGS — PP DERIVE: W₄₉ sign of f⊗χ₋₇ (f = 7.4.a.a), P5a referent, audit of Artin-conductor draft v2 — 2026-11-09 (America/Chicago)
Agent: Professor Proof (Soft SF). Additive file; nothing edited. Tip 7cddb188… untouched. No CERT. No LMFDB query; nothing sent outside. The PyPI install of cypari2 (PARI 2.17.2) is tooling. Usage at start: 17%.
Authority: OW 68a2b8e1f14e8722….
Verified inputs:
- OW c4c0f1c0318691c045b136c01c4de7eb86690ae9c8db4d20b07939a6fd8b24ed (Path C stands; "W₇ = +1" = ε on 7.4.a.a at level 7; sidecar MATCH)
- OW 45aeba5fc0433c808957d1518161cb24664ac97adff112d9df2ff7249a331ab3 (operative P5a = Γ₀(49)⁺, W₇ = +1 axiom version, OPEN)
- OW P5A_REWRITE_GAMMA0_49 0e1c7cac… (history)
- Draft v1 65b367ef88cce23047c70ec0146bfb457c1274af2a3906f573d9a73d19b4b5b9
- Draft v2 ccb568287c9f08c5f976249a5ddf14b710efbeb36b7daf48ef2f9c0a01b826c0
- Auditor 034605bf9be2442686cbf2b0fd69bd790714110574c442e3ce284f03eb7a0666
Scripts and logs: /workspace/audit-scratch/pp_twist49/ — twist49.gp/.log, twist49b.gp/.log, v2items.gp/.log. twist2401.gp was interrupted and gave no result.

## Rollup
PROVED 11 · CONDITIONAL 2 · OPEN 1 · REFUTED 1.

## 1. Sign: W₄₉(f⊗χ₋₇) = −1. MATCH with Auditor R4.
**Convention.** f|_k W_N = w_N f, with W_N = [[0,−1],[N,0]] normalized to an involution.
- Λ(s) = N^{s/2}(2π)^{−s}Γ(s)L(s), and Λ(s) = ε Λ(k−s) with ε = (−1)^{k/2} w_N.
- For k = 4, ε = w_N.
- For p ∥ N with trivial character: a_p = −p^{k/2−1} w_p.

**Computation (my own run; Auditor's script not reused).** These are PROVED.
- **Level 7.** S₄^new(7) has dimension 1. f has a₂..a₈ = −1, −2, −7, 16, 2, −7, 15. mfatkineigenvalues gives W₇ = +1, lfunrootres gives ε = +1, and a₇ = −7 = −7¹·(+1). All consistent.
- **Level 49.** S₄^new(49) has dimension 8 in 5 Galois orbits. I scanned a_n for n ≤ 60 against χ₋₇(n)a_n(f), with a₇ = 0.
  - Exactly one form matches: orbit 1, rational.
  - mftwist(f, −7) gives the same q-expansion, and mfconductor = 49.
  - So g is **new at 49, not old**.
- **The sign.** mfatkineigenvalues gives W₄₉(g) = −1, and lfunrootres gives ε(g) = −1. The two routes agree, consistent with ε = w_N for k = 4.

**Hand cross-check (PROVED).**
- g_7 = St ⊗ ω₇, where ω₇ is the ramified quadratic local component of χ₋₇.
- For ramified χ, ε(½, St⊗χ) = ε(½, χ|·|^{1/2}) ε(½, χ|·|^{−1/2}) = ε(½, χ)² = χ(−1).
- ω(−1) = ∏_v ω_v(−1) = 1, and ω_∞(−1) = χ₋₇(−1) = −1 because χ₋₇ is odd. So ω₇(−1) = −1.
- The other local factors are ε_∞ = i^k = +1 and unramified places = 1.
- So global ε = −1, and w₄₉ = ε = −1. **MATCH.**

## 2. P5a verdict: g is NOT a referent for P5a (Γ₀(49)⁺, "W₇ = +1"). PROVED.
- At level 49 the only Atkin–Lehner involution at 7 is W₄₉, the Fricke involution. There is no W₇, because 7 does not divide 49 exactly.
- Invariance under Γ₀(49)⁺ = Γ₀(49) ∪ W₄₉Γ₀(49) means w₄₉ = +1. Since w₄₉(g) = −1, g is anti-invariant, so g ∉ S₄(Γ₀(49)⁺).
- OW c4c0f1c0 places "W₇ = +1" on f at level 7 (w₇(f) = +1, PROVED above). That sign does not carry over to g: twisting changes the 7-local sign from +1 (St) to −1 (St⊗ω₇).

**All level-49 weight-4 newforms with their Fricke signs (PROVED, PARI).** They are identified by q-expansion only; I assign no LMFDB labels.
| orbit | coefficient field | a₂, a₃, a₅ | w₄₉ = ε |
|---|---|---|---|
| 1 = g = f⊗χ₋₇ | ℚ | −1, 2, −16 | −1 |
| 2 | ℚ (a_p = 0 at p = 3, 5, inert in ℚ(√−7)) | −5, 0, 0 | −1 |
| 3 | ℚ | 2, 7, 7 | +1 |
| 4 = orbit 3 ⊗ χ₋₇ | ℚ | 2, −7, −7 | −1 |
| 5 | quartic, y⁴−2y³−35y²+36y+194 (4 embeddings) | e.g. 4.5311, ±3.5796, … | +1 for all four |
- **Fricke +1 newforms: orbit 3 and the four forms of orbit 5**, five forms in all.
- On the full S₄(49) (dimension 10), the W₄₉ characteristic polynomial is (x−1)⁶(x+1)⁴, and on the new part (x−1)⁵(x+1)³. So the 2-dimensional old space from f splits as +1 ⊕ −1.
- Hence **dim S₄(Γ₀(49)⁺) = 6** for the scalar (trivial ρ) case. This bears on P5a: if ρ̄ were trivial, the claimed vanishing at κ = 4 would be **false**. ρ̄ is unspecified ("components — Arvin"), so P5a stays **OPEN**. This file does not choose ρ̄.

## 3. Audit of draft v2 (ccb56828…), with changes from v1 (65b367ef…)
| v2 item | v2 label | PP verdict | changed from v1? |
|---|---|---|---|
| 1. f Steinberg, ε₇ = +1, root number +1, exponent 1, tame | PROVED | **PROVED** (recomputed §1) | adds "root number +1" |
| 2. f⊗χ₋₇: exponent 2, level 49, a₇ = 0, unique rational match, W₄₉ = −1 | PROVED | **PROVED** (recomputed §1; MATCH Auditor) | W₄₉ = −1 and uniqueness are new |
| 3. Twists by conductor-7 characters: 7-part ≤ 49 | PROVED | **PROVED**. Local a(St⊗χ) = 2 for tame ramified χ and 1 for unramified χ. Order-3 instance computed: f⊗χ lies in S₄(49, χ²) and not in S₄(7, χ²). | **Changed.** v1's "49 is maximal for any twist" is **REFUTED** for characters mod 49 of order 7. |
| 3 (bracket). Wild order-7 χ mod 49 gives level 2401 | stated | Computed: f⊗χ is **not** in S₄(49, χ²) (dim 13) or S₄(343, χ²) (dim 91), using 150 coefficients, above both Sturm bounds. **PROVED that the level exceeds 343.** Level = 2401 exactly is **CONDITIONAL** on the standard local formula a(St⊗χ) = 2a(χ) = 4; the 2401 run was not completed. | new |
| 4. U(140) ≅ C2×C4×C6 = [12,2,2], order 48; (−7/23) = (35/23) = +1 | PROVED | **PROVED** (znstar cyc [12,2,2]; Kronecker symbols recomputed) | — |
| 5. a_n ≡ n¹³σ₁₉(n) mod 49 for 7 ∤ n, n ≤ 5311; fails mod 343 at n = 2 | PROVED | **PROVED** for the finite range (0 failures; n = 2 gives residue 196 mod 343) | adds the failure witness n = 2. The all-n congruence is CONDITIONAL on Chen–Kiming (new and correct). |
| 6. 539 = 7²·11 = ⌊(4880−21)/9⌋ = 3·68 + 5·67 | PROVED | **PROVED** (arithmetic) | v1's "4859 = 9·539 + 8" was dropped. It is true: 4851 + 8 = 4859. |
| 7. λ(s_αδ) = 1 on truncated F | PROVED | **PROVED within PP's definitions** (bd3730eb), not re-run here | reworded from v1's "D̂1(s_αδ) = 1". The project-level statement is still CONDITIONAL (B14-3). |
| CONDITIONAL: Chen–Kiming; D̂1 project statement; T3⁵³⁹(4880) = 2 | CONDITIONAL | **CONDITIONAL**, correct | T3 now tied to DP-b |
| OWNER DEFINITION: "W₇ = +1" = ε₇ on f at level 7 | OW | correct (c4c0f1c0) | **Moved** from v1's CONDITIONAL to OWNER DEFINITION |
| OPEN: P5a referent | OPEN | **OPEN** holds for P5a, and §2 sharpens it: g is PROVED not to be a Γ₀(49)⁺ referent. The Fricke +1 candidates are orbit 3 and orbit 5. | v1 said "sign not computed" |
| OPEN: links among 7², U(140), V42, D̂1; no role for 11; 980 is not a quadratic-twist level | OPEN | **OPEN**. "980 not a quadratic-twist level" was not recomputed here. | new clause |

The one REFUTED item is v1's "any twist" maximality claim, which v2 corrects.

## Owner decisions needed
1. **The P5a referent.** g fails Γ₀(49)⁺. Choose whether P5a's level-49 referent is one of the Fricke +1 newforms (orbit 3 or orbit 5), or whether the vector-valued ρ̄ ("components — Arvin") is to be specified. If ρ̄ is trivial, P5a's vanishing at κ = 4 is false, since dim S₄(Γ₀(49)⁺) = 6.
2. Keep "W₇ = +1" strictly at level 7 (c4c0f1c0). No W₇ exists at level 49.
