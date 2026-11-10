# FINDINGS (Local-derived) — carry-forward of Owner decision t4337 (16:44 CST), 2026-11-09 ~16:48 CST America/Chicago

Source: OWNER_WRITE_MAINCHAT_t4337_BRANE_M5_FACE_10D_XI_TWIST140_REST_NEUTRAL_2026-11-09_1644.md (sha256 f283cffd365ca7368a9f7b5dfdca7ee177ed54db25a28c1944999a5af755e5b6). Owner's words, as quoted there: "As mine: define the brane as a stack of wrapped M5-branes, the face as the 10D matching hypersurface, and Ξ := 49a1 twisted by 140. Everything else (DP-a, Layer2, joint carrier, R_c's role, baseline) stays neutral."
Amends OW 5f59e33e (16:31 withdrawal of t4327, ed526f70) only for those three items. No Local file was ever written under t4327, so no withdrawal note is needed.
Additive only. No prior file edited. Tip 7cddb188 untouched. No CERT. Nothing sent outside. No Gemini.

## 1. Adopted definition carried into the Local lane
- **D-Ξ (Owner DEFINITION):** Ξ := 49a1 ⊗ χ₁₄₀, the quadratic twist of 49a1 by the character of ℚ(√35) (discriminant 140). The twist by −20 is not Ξ.
- Arithmetic facts about this curve (carried by citation, not re-derived here): conductor 19600 and root number −1, so the Fricke sign is +1. See the PP 1525 audit (389c2f7c…) and RELABEL ce4d9e80…, where that sign is PROVED locally in PARI. Because Ξ is fixed by a specific twist, the definition picks one curve. The existence of other Fricke +1 classes at level 19600 doesn't make it ambiguous.

## 2. Status under D-Ξ (labels kept distinct)
| Item | Label |
|---|---|
| Ξ named (definition) | DEFINED by the Owner, not a theorem |
| Conductor 19600 and Fricke +1 for Ξ | PROVED (cited, PP 1525) |
| Λ₀ = √(7/8)·L(1,χ₁₄₀) (MR1 0ea030ae…, Local-verified) | PROVED as an identity. Under D-Ξ its link to Ξ is structural, because χ₁₄₀ is Ξ's twisting character. |
| Dynamical derivation of Λ₀ (why the physics selects ℚ(√35)) | OPEN |
| W₄₉ does not extend Weil(140) (trace argument, ae951f3e…) | PROVED (unchanged) |
| Weil carrier g₊ = θ₁² − 7θ₁(7·)², Fricke +1 at Γ₀(49) | PROVED (unchanged, ae951f3e and ce4d9e80) |
| Relation of Ξ's newform (f₄₉ₐ₁⊗χ₁₄₀, level 19600) to the level-49 Weil carrier | OPEN. No equivariant map was constructed. |
| Identifying the weight-3/2 Ξ with integral-weight carriers | OPEN (unchanged) |
| Induced-carrier step | CONDITIONAL (unchanged) |
| χ₁₄₀ acting on all of Γ₀(140) | CONDITIONAL (unchanged) |
| Joint carrier | UNDEFINED (Owner neutral). Its minimal level (980 vs 19600) is not posed; recorded only as OPEN. |
| α preserves B (O4) | HOLD (α undefined) |
| Bridge C | PARTIAL |

## 3. Out of lane, recorded by reference only
Brane := a stack of wrapped M5-branes. Face := the 10D matching hypersurface. Both are Owner definitions for the Non Local and MR2 lanes; this file carries no Local claims about them. DP-a, Layer2, R_c's physical role and the baseline stay neutral, and the vacuum choice stays on HOLD (OW aaadb280). The Λ₀ and R_c := κℓ_P definitions stand.

## 4. Rollup of this file's new entries
New proofs: 0 (all PROVED items are cited). DEFINED: 1 (D-Ξ). New structural remark: 1 (the Λ₀–Ξ link). CONDITIONAL: 2 (unchanged). OPEN: 4 (Λ₀ dynamics, Ξ↔Weil carrier map, weight-3/2 identification, joint-carrier level as unposed). REFUTED: 0. HOLD: 1 (O4).
For PP audit.
