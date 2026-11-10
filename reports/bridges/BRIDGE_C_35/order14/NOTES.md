# order14 RESULTS
Preregistrations, all written before their tests:
- PREREG.md (sha256 e3d4dd5f…55f6)
- MAP_RG1.md (MAP_RG1.sha256)
- MAP_RG1prime.md (MAP_RG1prime.sha256)
Script hashes are in scripts/SHA256SUMS. c1.py was edited after its first hash to record per-companion max/min over τ; the metric is unchanged, and the edit and rehash are disclosed.

## 1. B(ĉ′) ≡ 0: proved (Category A, PREREG §1)
The isometry ρ = −σ: ν ↦ (−ν1−7ν2, ν2) negates s′ and fixes s and both Gaussians. It preserves every coset, because (Aα)_1 ∈ Z, and every twist, because (Aβ)_1 = 0 for β ∈ {0, a}. Hence B = −B = 0 for all 105 companions.

## 2. Tests by the preregistered rule
| Test | Result | Verdict |
|---|---|---|
| C1: W2d rerun, error / Σ\|terms\| ≤ 1e−25 | max 0.097 (companions 12, 35, 70; all others ≤ 1e−28) | **FAIL by rule** |
| C1 control: B(ĉ1) nonzero | max 1.0 | pass |
| C2: literal line defects on lines with offset ∈ {−1,0,1} | 19 270 uncovered points | **FAIL by rule** |
| E2-int: g(x) is P-even | ≤ 6e−19 at 4 values of x | **pass** |
| RG1: zero set of B(ĉ1) = ρ_m-invariant set | 18 extra zeros (companions 7–13, 36–41, 71–76) | **FAIL**: necessity refuted for the single-reflection rule |
| RG1′, fresh K1 family (35 companions) | predicted zero set ∅, measured ∅; min nonzero 0.997 | pass, but weak: no zeros were predicted, so only the "no spurious zeros" direction is tested |

## 3. Post-hoc (descriptive; recorded after the FAILs)
- **C1:** the FAIL is a float artefact. In the axis companions, the value of s at ν2 = 0 is computed as (2·7 − 7·2)/√35, which rounds to about 1e−31 instead of 0, while Σ|terms| is only about 1e−25. With exact s = √35·ν2 (c1posthoc), |B(ĉ′)|/Σ|terms| ≤ 3.0e−32 for 12, 35 and 70. This agrees with the Category A proof.
- **C2:** the FAIL comes from the offsets prediction, which was too narrow: unreduced representatives give line offsets up to 4. With offsets |·| ≤ 4 (c2posthoc), **0 uncovered points**. All defects lie on lines n = const (direction e2, Q = 7/2) and k = const (direction e1, Q = 1), plus finitely many points. No (21,−1) lines are needed.
  - P-even lines: full and half, in both directions.
  - P-odd lines: full lines along e2; half lines along e1 and e2.
- **RG1′ (post-hoc fit on the 105, then a fresh K1 test):** zeros occur exactly where ρ_m: (u,m) ↦ (u,−m) or ρ_u: (u,m) ↦ (−u,m) preserves the companion. Post-hoc, the union equals the measured zero set exactly.

## 4. Literal full-series hybrid shadow
**Status: NOT located under the preregistered rule** (C1 and C2 FAILed by rule). In substance it is supported by the Category A proof and the post-hoc checks.
- **P-odd sector:** ξ₁-shadow of Ĥ and Ĝ_O, the three distinct unary thetas (5n²/2 shared, R²/34, 35m²/4) with weight-½ partners. In addition there are P-odd line terms: full e2-lines (weight-½ unary thetas, modular, no shadow) and half-lines (false thetas, quantum).
- **P-even sector:** ½𝓗(Φ_orth) (identification) with the single Laplacian defect ±(π/4)√140·y^{3/2}·ϑ⁺_{7/2}·conj(ϑ⁻_{5/2}) at ray e2. The ray-e1 term is proved zero. The defect itself vanishes exactly on the RG1′ companions (post-hoc). In addition there are P-even line terms: full and half lines along e1 and e2.
- The half-lines' quantum partners are the weight-3/2 series Σm e(7m²τ/2) (e2-lines) and Σw e(w²τ) (e1-lines). These are the same two positive-ray partners that appear in the shadows, so **no new unary theta** appears.
- No single weight-1 ξ₁-shadow exists (Lemma O/W, Category A).

## 5. Maps
- **E2:** internal test passed. The Resonant side is OPEN.
- **E3:** OPEN, since no T3/O_res q-series is available. Next measurement: compare its exponents with 5u²/2, u ∈ α1+Z.
- **E1:** the Resonant half is OPEN.
- **RG1 FAILed. RG1′ is preregistered.** It passed its first fresh test (weak). A discriminating fresh test needs a family with predicted zeros.

## 6. Framing (opinion)
- Arvin: P-odd = local, hybrid mock-modular; P-even = non-local, hybrid quantum modular, linked by 5n²/2; "therein is the residual geometric bridge".
- This is recorded as a working claim. It is NOT a proved bridge.
- RG1/RG1′ is the first falsifiable piece of it: endpoint reflections of the residual cone geometry govern where the P-even defect vanishes.

## Disclosures and open next step
- Both preregistered FAILs (C1, C2) came from test-design flaws: float rounding of an exact zero, and an offset range set too narrowly. The fixes are post-hoc.
- Next step: preregister C1′ (exact-s metric) and C2′ (offsets ≤ 4) as fresh tests on the K1 family or a second Q-range, to turn the hybrid into a preregistered pass. Also:
  - give a Category A proof of RG1′ sufficiency at c1;
  - run a discriminating RG1′ test on a family with predicted zeros (e.g. twists β ∈ {hA, a+hA});
  - classify the P-even half-lines by exact offsets and write their partial-theta Eichler partners in closed form.
