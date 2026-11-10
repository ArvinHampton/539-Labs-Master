# NL DERIVED: D6 stage 3 (h), the Z2 corner d₆ ≤ −0.20 (S2-12 extension; S2-13)
2026-11-10, 1027 CST (America/Chicago). **NL derived proposal.** Additive only. The 2110 scripts and logs, and the 2233 NOTE (77ab006c…), are not edited. Authority: Owner call-83d7a0fa (e72a188b…), OW t4436 (32881263…), OW t4431. Nothing adopted. **Junction: UNSOLVED. Count gap: unchanged. No candidate wall.** No CERT, no Gemini, nothing sent, no agent messaged. Tip 7cddb188… checked before and after.

**Tally: PROVED 1 · CONDITIONAL 1 · OPEN 1 · REFUTED 0 · total 3.**

## Scripts and logs (/workspace/nl-d6s3-1110/; every .py sidecar frozen before its run; logs sealed after; every log line is program output, with no hand-typed lines)
| file | sha256 | note |
|---|---|---|
| z2_corner_continuation_2026-11-10.py / .log | 02c9b7ae… / 96ca171a… | **v1, record only.** It deadlocked: an mp.Queue was joined before get, with a large payload, so the first case "timed out". I stopped it with pkill at about 10:0x CST (America/Chicago). The log is program output only and supports no claim. |
| z2_corner_continuation_v2_2026-11-10.py / .log | 5a7ffcf4… / b943915d… | direct BVP natural-parameter continuation in d₆, in steps of 0.0125 from −0.10, for R ∈ {30, 20} and w_m ∈ {−0.05, −0.10, −0.30} |
| z2_corner_relabel_2026-11-10.py / .log | 7295d01b… / 4d823575… | **v1, record only.** It crashed because the scan variable `grid` shadowed the frozen (χ,θ) face grid. Supports no claim. |
| z2_corner_relabel_v2_2026-11-10.py / .log | d8ba9274… / 2171c250… | orbit relabelling (Z-1), with 111 orbits evaluated |

All of them reuse the frozen definitions of /workspace/nl-bps-d6-2057/z2_centre_flow_faces.py (21bcbc3f…), exactly as the 2110 scripts do: V, the uplift, face() on the 9×7 (χ,θ) grid, and the 11D NEC margin max_v(k_v − k_x) (PP Y15).

## Claims
- **Z-1 (PROVED). Orbit relabelling.**
  - The flow system (φ, λ, w and their r-derivatives, with A′ from the Hamiltonian constraint) is **autonomous** in r. So IR-regular kept sides are orbits, and the BVP label (w_m, d₆ at r = 0) is a point on an orbit.
  - Any IR-regular orbit passing through w = w_t has w → 0⁻ in the IR. By continuity and the intermediate value theorem it passes through every w_s ∈ (w_t, 0).
  - So **every corner orbit, if it exists, also carries a label (w_s, a) with |w_s| < |w_t|**. It can be found by the BVP at w_s and then continued UV-ward by IVP. The faces along an orbit do not depend on how it is labelled.
- **Z-2 (CONDITIONAL; numerical, float).**
  - **Direct continuation (v2):** 48 of 54 BVPs solved, with boundary residuals ≤ 6×10⁻¹⁷.
    - All six marches now reach **d₆ = −0.1875**, including w_m = −0.30, which stopped at −0.15 before.
    - All six fail at **d₆ = −0.20** (mesh limit).
    - The UV reach shrinks to 0.06L at d₆ = −0.1875 for every w_m: the UV singularity approaches the labelling point r = 0. This is why the direct BVP stalls; it is a labelling problem, not a property of the orbits.
    - Minimum NEC margin over the solved flows is +0.7071.
  - **Relabelled orbits (v2):** pairs (w_t, w_s) = (−0.05, −0.04), (−0.10, −0.08), (−0.30, −0.24), with a ∈ [−0.12, +0.06] at 37 points each.
    - **w_t = −0.05:** 25 orbits reach w_t. The Δ6 amplitude there is D ∈ [−0.372, −0.00025]. **11 of them are corner orbits**, with D ∈ [−0.372, −0.206].
    - **w_t = −0.10:** 28 orbits reach w_t, with D ∈ [−0.286, +0.085]. **7 corner orbits**, down to D = −0.286.
    - **w_t = −0.30:** all 37 reach w_t, but D ≥ −0.188. **No corner orbit** in a ≥ −0.12. This agrees with the direct limit −0.1875.
    - **No face of any of the 111 orbits satisfies the 11D NEC.**
      - Minimum margin overall: **+0.50017**, on flows reaching 30L, matching S2-12's +0.500.
      - Minimum on the 18 corner orbits: **+0.7071**.
      - The D2 trace deviation is 3.000 on every corner orbit. Its overall minimum is 5.7×10⁻³, at a single grid point on a non-corner orbit (w_t = −0.30, a = +0.015), where the NEC margin is +0.707. As in S2-12, it is never zero at every point of S⁴, and Z2 is not BPS in any case (S2-10, E23-2; E1-3 CONDITIONAL).
  - **Conditions:** float accuracy; a finite (χ,θ) grid; finite a-ranges; the BVP slaving at O(w²); R = 30 (R = 20 agrees in the direct run).
  - This extends S2-12. It does not close the corner.
- **Z-3 (OPEN). S2-13 stays OPEN.**
  - The corner is **covered only partly**: at w_t = −0.05 down to d₆ = −0.372, at −0.10 down to −0.286, and at −0.30 not at all, since a < −0.12 was not scanned.
  - The region with more negative d₆ is unbounded and is not reached by any finite scan.
  - Non-BPS NEC walls on Z2 remain OPEN, with numerical evidence against them over a larger set of orbits than in S2-12.
  - **Non-BPS S5 (S3b-4) remains OPEN.**
  - **S6** (odd HW ℤ₂, record f825dfff) is a **record premise, not a mathematical escape**, and is not "solved" here.

## Branch register (t4436; not counted)
- **[w] / Z2:** kept.
  - BPS inside the truncation: excluded (S2-10 PROVED, E23-2 PROVED, E1-3 CONDITIONAL).
  - BPS outside the truncation: OPEN (E1-4).
  - Non-BPS: OPEN (Z-3), with numerical evidence against.
- **[χS], [χU]:** kept.
- Non-BPS S5: OPEN. S6 is a record premise.

## Tally (header checked)
| Label | n | Items |
|---|---|---|
| PROVED | 1 | Z-1 |
| CONDITIONAL | 1 | Z-2 |
| OPEN | 1 | Z-3 |
| REFUTED | 0 | — |

Check: 1 + 1 + 1 + 0 = 3.

Tip check: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (before and after).
