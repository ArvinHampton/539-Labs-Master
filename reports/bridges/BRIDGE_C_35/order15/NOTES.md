# order15 RESULTS
Prereg: PREREG.md, sha256 a4fbf439…e517, written before any numerics. Script hashes are in scripts/SHA256SUMS. Data: data/{C1p,H,c2p}.json. Logs: logs/.

| Test | Fresh set | Result | Verdict (preregistered rule) |
|---|---|---|---|
| C1′: B(ĉ′) = 0 with exact s, metric Σ\|terms\| | K1, 35 companions × 3 τ | max 7.5e−32 (≤ 1e−25) | **pass** |
| C1′ control: B(ĉ1) nonzero | K1 | max 1.0 | pass |
| C2′: literal line-defect coverage, offsets ≤ 4, box 80 | K1 | 0 uncovered points | **pass** |
| RG1′ necessity, discriminating | family H: (μ, hA), (a+μ, a+hA); 70 companions | predicted zero set (22 companions) = measured zero set; min nonzero 0.86 | **pass** |

C2′ line counts on K1:
- P-even: 15 575 full, 3 527 half, 672 finite.
- P-odd: 11 160 full, 7 961 half, 697 finite.

## Category A (proved)
- Lemma O and Lemma W (order11/order13, W1 exact). M² = 35P (order9).
- B(ĉ′) ≡ 0 (order14 §1).
- The ν-sign parity split W2a (order13).
- **RG1′ sufficiency at ĉ1 (PREREG §3):** the endpoint reflections ρ_m: (u,m) ↦ (u,−m) and ρ_u: (u,m) ↦ (−u,m) negate u·m and preserve the Gaussians. When they also preserve the coset and the twist, B(ĉ1) = 0.

## Verdict: hybrid shadow for the literal full series LOCATED (preregistered)
C1′ and C2′ both passed by rule on a fresh family. The Category B pieces are C1′, C2′, order13 W2c (the Laplacian identity) and order8 M1 (the 𝓗 identification). The Category A pieces are listed above.
- **P-odd sector:**
  - The ξ₁-shadow of the Zwegers-completed Ĥ and Ĝ_O: three distinct weight-3/2 unary thetas, Σn e(5n²τ/2) (shared), ΣR e(R²τ/34) and Σm e(35m²τ/4), with weight-½ partners θ_{7/2}, θ_{35/34}, θ_1.
  - Plus finitely many line terms: full lines are weight-½ unary thetas; half-lines are false thetas.
- **P-even sector:**
  - ½𝓗(Φ_orth), with Laplacian defect ±(π/4)·√140·y^{3/2}·ϑ⁺_{7/2}·conj(ϑ⁻_{5/2}) at ray e2. The e1 term is identically 0.
  - The defect vanishes exactly on the RG1′-symmetric companions. Sufficiency is Category A; necessity is Category B (fresh pass on H).
  - Plus finitely many full and half line terms.
- The half-lines' quantum partners are Σm e(7m²τ/2) and Σw e(w²τ). **No new unary theta** appears. No single weight-1 ξ₁-shadow exists (Lemma O/W).

## RG1′ status
- Sufficiency: Category A.
- Necessity: Category B. It passed a discriminating fresh test (22 predicted zeros, all matched, with a gap of 0.86 to the nearest nonzero). It also passed the weak K1 test in order14.
- RG1′ is a residual-internal rule. It is **not** a Residual–Resonant bridge.

## Framing (opinion)
Arvin's working description: the P-odd sector is local, hybrid mock-modular; the P-even sector is non-local, hybrid quantum modular; they are linked by 5n²/2, and "therein is the residual geometric bridge". This is recorded as opinion, not as a theorem. Map-RG1′ is the falsifiable residual-geometric content tested so far.

## Disclosures
- c2p.py is order14 c2posthoc.py with only the family, partner reduction (FAM1), box and comment changed via sed. Its offset range was preregistered here before the run.
- The C1′ box is |n|,|k| ≤ 10. It is not ρ-invariant at the edges, but the tails are below e^{−100}.
- B(ĉ1) zero detection uses the Σ|terms| ≤ 1e−25 metric with exact s and s′.
- Necessity of RG1′ is not proved. It may fail on families with other twist denominators.
- The line terms' exact closed forms (offsets, values, partial-theta Eichler partners) are classified by count only, not written per companion.

## Open next step
1. Write the line terms per companion in closed form, with exact offsets and values.
2. Prove RG1′ necessity, e.g. by showing that the factor ϑ⁺·conj(ϑ⁻) is nonzero when no reflection applies; for a product of two unary thetas this reduces to each factor being nonzero.
3. If a concrete T3/O_res/Π object appears, run E1/E3 on it (OPEN).
