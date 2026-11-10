# DRAFT — Author blanks: dim V / exact k / ρ (P1 generators, P2 ρ(W₇) eigenspace)

**Status:** DRAFT FOR ARVIN APPROVAL ONLY. Nothing here has been written into the live residual-C draft. Invent-ban ON.
**Prepared:** 2026-10-25 ~17:10 CDT (America/Chicago)

## 0. Sources read (sha256 checked live)
| Source | Path | sha256 |
|---|---|---|
| residual-C draft (live, read-only) | `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` | ea85cbbc239d2e050e2b639908ae70dc850090270f08081662e26606036a7feb (MATCH) |
| fork-ii map (read-only) | `/workspace/residual-c-local-map-implications-fork-ii.md` | 75c57264cc81049ea1e2d322c036d06f56a4bc774d3b851568ee5c1f7a73494a |
| 9 Maths chain | `/workspace/quantum-comp/maths/theorem-lemma-chain-9-maths.txt` | 904104d26c0c029df9a9e39f7ef5235f4b3a2f7befb0349e7bdf0187a6df5a0a (MATCH) |
| Einstein–Hampton appendix (Zenodo 10.5281/zenodo.23010998, box copy) | `/workspace/quantum-comp/nonlocal/Einstein_Hampton_Equation_Rewrite_Appendix_2026-09-28.txt` | 08b8541a1b40e16961984833915437aa4a96b680fe1404ad3e722191308ede39 |
| EH Lean | `/workspace/quantum-comp/oct17-master/lean/EinsteinHamptonCurvature.lean` | 53f9a4a81c3b05a3e3eb5cedf396a67ec4e6ba3bee0485e020d95f6c4d5b7aa6 |
| MR1/Local notes | `residual-c-p1-option2-FILL-PACK.md`, `residual-c-p1-remainder-OPTIONS.md`, `residual-c-p2-w7-action-OPTIONS.md` (all /workspace) | — |

The Zenodo record was not fetched again this run. Only the box copy was read.

## 1. Constraints already fixed by Arvin, with draft line refs (DERIVED_FROM_WRITTEN, already accepted)
- G = Γ₀(49)⁺ = ⟨Γ₀(49), W₇⟩. Draft l.9, l.30, l.46.
- ρ : G → GL(V) is direct (MR1 Option 2), and ρ(W₇) is non-scalar. Draft l.10, l.36.
- dim V ≥ 2. This is deduced from non-scalar ρ(W₇). Draft l.16 [R9], l.37.
- k ∈ ℤ, k < 0. Multiplier is trivial, there is no cover, and R4 is PSL₂-style, so ρ(W₇)² = Id_V and the eigenvalues are ±1. Draft l.39–40, P2-A l.62.
- The P2 eigenspace cut applies to the P3 form space, not to ρ. Draft l.63, l.67.

## 2. Blank 1: `[[ dim V ]]`
**Label: ABSENT → NEED ARVIN WRITE**
- Written search: the EH appendix L1–L7 and Lean have no representation space. The 9 Maths chain (l.1218–1235, Def 5.1) defines ρ : G_obs → End(M_osc). That is a *different* representation (an observable group acting on oscillation modules). It gives no dimension, and nothing identifies M_osc with V. Using it here would be an invention.
- **Proposed text (placeholder only):** "V ≅ ℂ^d with d = `[[ d — Arvin ]]`, d ≥ 2 (deduced, draft l.37)."
- **Missing:** an integer d ≥ 2 from Arvin, ideally with the Written source or reason. For example, if Arvin intends V = ℂ[cusps of X₀(49)] or a W₇-orbit carrier, Arvin must say so; it is not inferred here.
- **Ask:** SUPPLY d (an integer ≥ 2) and its Written justification.

## 3. Blank 2: exact `[[ k ]]`
**Label: ABSENT → NEED ARVIN WRITE** (homonym hazard flagged)
- EH L5–L7 (appendix l.29–40; Lean header l.9–13) define a warp slope k with A = k·y and k² = Φ/1728 (with K = 8k²). This k is a real geometric parameter, set by the flux Φ. It is **not** the modular weight. It is not an integer by Written, and its sign convention is not tied to k < 0. **Do NOT import it as the P1 weight.** If Arvin intends a link, it must be Written explicitly.
- The 9 Maths chain contains no modular weight.
- **Proposed text (placeholder only):** "k = `[[ k — Arvin ]]` ∈ ℤ, k < 0 (draft l.39–40, P1-R1)."
- **Missing:** a negative integer from Arvin. Note that P5a then uses κ = 2 − k > 2 (draft l.143).
- **Ask:** SUPPLY a negative integer k. Also state explicitly that it is unrelated to the EH warp k, or Write the link.

## 4. Blank 3: ρ matrices
### 4a. P1: ρ on generators
**Label: ABSENT → NEED ARVIN WRITE**
- No Written source gives generators of Γ₀(49) or any matrices of ρ. The EH appendix, the Lean file and the 9 Maths chain contain no level-49 or Fricke content (grep for 49 / Fricke / W₇ / weight returned no modular hits).
- **Proposed structural text (DRAFT_FOR_ARVIN_APPROVAL; it adds no numbers):** "ρ is specified by Written matrices ρ(γ_i) ∈ GL_d(ℂ) for a Written generating set {γ_i} of Γ₀(49), together with ρ(W₇), subject to: (i) the relations of Γ₀(49) (PSL₂-style); (ii) ρ(W₇)² = Id (draft l.40); (iii) ρ(W₇γW₇⁻¹) = ρ(W₇)ρ(γ)ρ(W₇)⁻¹ (draft l.63); (iv) compatibility with trivial χ (draft l.40). `[[ generators + matrices — Arvin ]]`."
- **Missing:** the generating set, d×d matrices, and their source.
- **Ask:** ACCEPT the structural text, or REVISE it. In either case, SUPPLY the matrices or Write a construction rule.

### 4b. P2: ρ(W₇) eigenspaces
**Label: partly DERIVED_FROM_WRITTEN; the choice is NEED ARVIN WRITE**
- DERIVED_FROM_WRITTEN: ρ(W₇)² = Id_V and ρ(W₇) is non-scalar. So V = V₊ ⊕ V₋, and both are nonzero: dim V₊ ≥ 1 and dim V₋ ≥ 1 (draft l.40, l.60–62). This is pure linear algebra on accepted premises; it is not a new claim.
- ABSENT: dim V₊ and dim V₋ (these depend on d and the matrix), and the chosen sign. The draft l.64 sign is Arvin-blank; MR1 recommends +1 for pairing with P5a, but that is a recommendation only.
- **Proposed text (DRAFT_FOR_ARVIN_APPROVAL):** "Since ρ(W₇)² = Id and ρ(W₇) ≠ ±Id, V = V₊ ⊕ V₋ with both summands nonzero; dims `[[ d₊, d₋ — Arvin ]]`, d₊ + d₋ = d. The residual lies in the `[[ +1 / −1 — Arvin ]]` eigenspace of the induced W₇ action on the P3 form space."
- **Ask:** ACCEPT the splitting text. SUPPLY the sign (±1) and d₊/d₋, which follow once 4a is given.

## 5. Summary
| Blank | Status |
|---|---|
| dim V | NEED ARVIN WRITE (only d ≥ 2 is derived) |
| exact k | NEED ARVIN WRITE (only k ∈ ℤ, k < 0 is derived; the EH k is a different symbol) |
| ρ on generators | NEED ARVIN WRITE (structural template drafted) |
| ρ(W₇) eigenspaces | Splitting V₊⊕V₋, both nonzero = DERIVED_FROM_WRITTEN; dims and sign = NEED ARVIN WRITE |

**One-line ask for Arvin:** ACCEPT the §4a/§4b structural texts (or REVISE them), and SUPPLY d, k (< 0), the generator matrices, and the ± sign.
