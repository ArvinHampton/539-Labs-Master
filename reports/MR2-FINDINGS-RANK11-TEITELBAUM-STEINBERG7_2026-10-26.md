# MR2 FINDINGS — Rank 11 ONLY: Teitelbaum / Bruhat–Tits Steinberg-at-7 slice (κ=4, k=−2)
Status: PARTIAL (Cat B). Scalar numbers are COMPUTED. The ρ̄/V₄₂ numeric split is ABSENT.
tip Soft SF LOCK sha (start/end): 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | tip_touched Soft SF NO | Rank 11 only | Soft SF invent HOLD | Opt 1 Weil NOT selected | Bridge PARTIAL READY NO | CatB-2 not promoted
Assignment: VANISHING_LEAD_ASSIGNMENTS sha 348bf88e… (verified). Prior: Connection 2b49ca25… (Teitelbaum row, R6) and Corpus map b271f42a… (V-BT-SLICE, V-R6).

## 1. Definition
- **Meaning of k.** Tip modular k=−2 corresponds to classical weight κ=4. In this report, Teitelbaum "weight k" always means the classical weight, which is 4. The coefficients are therefore P^{k−2}=P², i.e. Sym²-valued (dimension 3).
- **The slice.** C_har(Γ, P²) is the space of P²-valued harmonic cocycles on the edges of the Bruhat–Tits tree of PGL₂(ℚ₇), for an S-arithmetic group Γ. Here Γ is either Γ₀(M)[1/7] with 7∤M, or a {7}-unit group of a definite quaternion algebra. By Teitelbaum (Invent. Math. 101, 1990, "Values of p-adic L-functions and a p-adic Poisson kernel") and Darmon (Annals 154, 2001, "Integration on H_p×H", §1), this space is isomorphic to the forms of weight 4 and level 7M that are **7-new**. Those forms have local type at 7 equal to Steinberg (or its unramified twist).
- **Local types at 7 for newforms at level 49 with trivial character.** There are three:
  - (a) St⊗χ_quad, with χ the ramified quadratic character;
  - (b) ramified principal series π(χ,χ⁻¹), with cond χ=7;
  - (c) depth-zero supercuspidal.
- **Oldforms** come from level 1 and level 7. The level-7 newforms have type St at 7.
- **Which piece the cochains see.** Teitelbaum's cochains for Γ₀(7)[1/7] see only the level-7 Steinberg newforms. The level-49 St⊗χ forms are the χ-twists of those level-7 forms. They are therefore visible only **after twisting**, not as cocycles at level 49.

## 2. Applicability at N=49=7²: PARTIAL
The classical Teitelbaum, Darmon, and Dasgupta–Teitelbaum setup (Dasgupta–Teitelbaum, "The p-adic upper half plane", AWS 2007 notes) needs p‖N, or a definite quaternion algebra ramified at p. It does not apply directly when p²‖N. It applies only to the twist-related piece (a), via (a)=χ⊗(7-new forms of level 7). Pieces (b) and (c) are outside the theory. The citations are the same Cat A works already verified in the Connection report. No new Cat A is invented.

## 3. Numeric dimension: scalar Γ₀(49) COMPUTED; ρ̄-twisted ABSENT
**Formula.** For k=4: dim S_k(Γ₀(N)) = (k−1)(g−1) + ⌊k/4⌋ν₂ + ⌊k/3⌋ν₃ + (k/2−1)c.

**Inputs per level:**

| Level | g | ν₂ | ν₃ | c |
|---|---|---|---|---|
| 1 | 0 | 1 | 1 | 1 |
| 7 | 0 | 0 | 2 | 2 |
| 49 | 1 | 0 | 2 | 8 |

**Results:**
- dim S₄(Γ₀(1)) = 0
- dim S₄(Γ₀(7)) = 1
- dim S₄(Γ₀(49)) = 10
- New(49) = 10 − 2·1 − 3·0 = 8
- **Steinberg-at-7 slice at level 49, i.e. St⊗χ_quad = twists of S₄^new(7): 1**
- Pieces (b)+(c) at level 49: 7 (I did not split these)
- The cochain space C_har(Γ₀(1)[1/7], P²) itself is 2·dim S₄^new(7) = 2 (two copies under the Darmon convention). This is a level-7 object.

**Twisted ρ̄ (V₄₂).** There is no published or computed split of 592 into old / St / PS / SC. Sage and Magma are not on the box, and LMFDB has no ρ̄-twisted spaces. The local structure of ρ̄ at 7 is not Written. Twisting would change each piece by isotypic multiplicities that the tip does not fix. **ABSENT numeric.** MR1 AMEND-1 (N₃₆⊕N₆, 503+89) is an isotypic split, not a split by local type at 7, so I do not use it here.

## 4. Remainder table

| Piece | Scalar S₄(Γ₀(49)) | ρ̄-twisted (of 592) | Teitelbaum-visible? |
|---|---|---|---|
| Old from level 1 | 0 | ABSENT (o₁) | No |
| Old from level 7 (St at 7, 2 copies) | 2 | ABSENT (o₇) | Yes, at level 7 only, not as level-49 cochains |
| New St⊗χ_quad (Steinberg-at-7 slice) | 1 | ABSENT (s) | Only via χ-twist (PARTIAL) |
| New PS(χ,χ⁻¹) + supercuspidal | 7 | ABSENT (r) | No |
| Total | 10 | 592 = o₁+o₇+s+r | — |

## 5. Rank 11 vanishing status: NO in the scalar case; UNKNOWN for ρ̄
- **Scalar.** The slice has dimension 1, so it does not vanish.
- **ρ̄-twisted.** UNKNOWN. Suppose s=0 were shown. The remainder would still be o₁+o₇+r = 592. **This is never a full P5a vanish.**

## Soft SF risks
- Slice vanishing ≠ P5a vanishing. Old forms and supercuspidals/PS (7 of 10 in the scalar case) remain.
- p² caveat: at level 49 the slice is reached only by twisting from level 7. It is not a native harmonic-cochain space.
- Do not invent a Weil dictionary or a ρ̄ local type at 7. The twisted split stays ABSENT.

Commands: sha256sum (verified inputs); python3 genus-formula evaluation (level 7 → 1, level 49 → 10; level 1 = 0 by (g,ν₂,ν₃,c)=(0,1,1,1), standard). Sage/Magma unavailable.
