# FINDINGS — PP DERIVE item (4): Israel junction and the brane stress S_ab — 2026-11-09 (America/Chicago)
Agent: Professor Proof (Soft SF). Additive file; nothing edited. Tip 7cddb188… untouched. No CERT. Nothing sent outside.
Authority: OW 68a2b8e1f14e8722… and OW 33d25a790fb1e0da…. LOCK 96f8d42e… read; no purged mapping is used.
Scripts/logs: /workspace/audit-scratch/pp_derive_1320/item4_israel.py (.log).
Convention:
- n = ∂_y (unit normal); K_MN = ½ ∂_y g_MN on y = const; [X] = X(y₀⁺) − X(y₀⁻).
- [K_ab] − h_ab[K] = −κ² S_ab (Israel 1966, Nuovo Cimento B44, 1); κ² = 8πG₁₁.

## Rollup
PROVED 6 · CONDITIONAL 2 · OPEN 3 · REFUTED 1.
Verdict: **CONDITIONAL.** No Owner record defines the junction or the brane (564 OWNER_WRITE* files searched: "Israel" and "junction" appear only in the 1320 authorization; Auditor B13 §6 CONFIRMED). The results below are PROVED for the EH-ds geometry. They are CONDITIONAL as statements about the model until the Owner adopts the brane and the metric.

## Inputs (corpus, not Owner Writes)
- **Israel file.** oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/Israel_Junction_Conditions_2026-10-03.md, sha 31c14d684042255fffe277e67933e459a51634c40948e89b237ba106887386fe. It states [K_μν] − [K]q_μν = −8πG₁₁ S_μν, "trace combination 3k q", visible face S⁻ = (3k/8πG₁₁) q, and leaves n₂ for the hidden face unselected.
- **EH appendix** 08b8541a1b40e16961984833915437aa4a96b680fe1404ad3e722191308ede39: (Isr+) [K − Kq]₀ = −8πG₁₁(τ₊q + T(m) + T(H)), and (Isr−) at y = b with the opposite sign.
- **Metric.** EH-ds, or DP-metric (FINDINGS_PP_DERIVE_11D_METRIC_2026-11-09_1329.md, 4d07bd1b…). Both have A = ky and an unwarped fibre, so the junction algebra is identical.

## 1. Extrinsic curvature (PROVED, sympy)
For ds² = e^{−2A}η + dy² + e^{2B}ĝ₆, the faces are 10-dimensional: x^μ × fibre.
- K_μν = −A′ h_μν and K_ab = +B′ h_ab.
- For EH-lock (A′ = k, B′ = 0): K_μν = −k h, K_ab = 0, K = −4k.

## 2. General Z₂ face (PROVED)
- **Stress on a mirror-symmetric face.** With A′(y₀⁻) = −A′(y₀⁺) and B′(y₀⁻) = −B′(y₀⁺):
  - S_μν = (6/κ²)(−A′ + 2B′) h_μν
  - S_ab = (2/κ²)(−4A′ + 5B′) h_ab
- **Pure tension** (S ∝ h on all 10 directions) **holds iff B′ = −A′.**

## 3. Faces of EH-lock / DP-metric (B′ = 0; PROVED)
| face | S_μν (4D) | S_ab (fibre, 6D) |
|---|---|---|
| +U, y = 0, Z₂ | −(6k/κ²) h_μν (tension σ₄ = 6k/κ² > 0) | −(8k/κ²) h_ab (σ_f = 8k/κ²) |
| −U, y = b, Z₂ | +(6k/κ²) h_μν (negative tension) | +(8k/κ²) h_ab |
| one-sided boundary (no Z₂) | combination (K − Kh)/h = 3k | combination 4k |
- **R1 (REFUTED).** A pure-tension visible face on EH-ds is impossible: B constant gives B′ = 0 ≠ −k, which contradicts §2 unless k = 0. So "Convention C reads the visible face as pure tension" (Israel file l.13–15) is false on the full 10D worldvolume.
- **R2 (PROVED).** The Israel file's "3k q" is correct only on the 4D block, and only one-sided without Z₂ doubling. The file omits the fibre block (4k one-sided, 8k with Z₂). The 3k vs 6k difference is a convention factor of 2 between one-sided and Z₂.
- **R3 (PROVED).** The sign pattern of EH (Isr+) and (Isr−) agrees with §3: positive tension at +U, negative at −U, as in RS1.
- **What the model implies for S_ab (CONDITIONAL on adopting a Z₂ 10D face on EH-ds or DP-metric):**
  - S_ab = −σ₄ h_μν ⊕ −σ_f h_ab + S^(m)_ab, with σ_f/σ₄ = 4/3.
  - The brane must carry a fibre-direction stress (σ_f − σ₄) = 2k/κ² in addition to the 4D tension, and EH's τ₊q cannot be a single isotropic τ.
  - For DP-metric with N = 4880 in ℓ_p units: σ₄ = 1.2178 × 10⁻⁷ and σ_f = 1.6237 × 10⁻⁷, in ℓ_p⁻¹⁰.

## 4. Constraints (PROVED)
- **Hamiltonian constraint** {K_ab}S^ab = [T_nn]. For Z₂, {K_ab} = 0, so [T_yy] = 0 is required. It is satisfied, because the flux is y-homogeneous.
- **Momentum constraint** D^a S_ab = −[T_bn]. T_μy = 0, so it holds for the constant-tension background.

## 5. Brane dimension (PROVED from the literature, sharp)
- The Israel conditions apply only to codimension-1 hypersurfaces, which here means 10D faces.
- The model text calls the transfer branes "D2-branes" (s2-11dm2etx-v4.pdf, 74969d9a…). A 2-brane in 11D has codimension 8. For codimension ≥ 2, GR admits no distributional thin-shell limit (Geroch–Traschen, PRD 36, 1017, 1987), so no Israel condition exists for them.
- So the junction can only describe 10D end-of-world faces. "D2-brane" and "Israel junction" cannot refer to the same object.

## 6. OPEN items (exact gaps)
- **O1.** Z₂ parity of C₃. CS invariance needs C → −C. Then F_{S⁴} (no y-leg) is odd and must jump by 2q·vol across the face, which needs a magnetic brane source (Hořava–Witten-type). Owner choice needed.
- **O2.** The hidden-face n₂, still unselected (Israel file l.19). With B′ = 0, §3 fixes S at y = b without n₂. n₂ can enter only through T(−), which is undefined.
- **O3.** The brane matter S^(m) and the induced 4D equations (Shiromizu–Maeda–Sasaki-type projection) need T(m), T(H) and T(−) to be defined. They are undefined, so this is OPEN.

## Owner decisions needed
- **D-Isr-1.** Is the brane the 10D face (codimension 1)? If so, the "D2" wording must go.
- **D-Isr-2.** Z₂ (orbifold) or one-sided boundary.
- **D-Isr-3.** Accept an anisotropic S (σ_f/σ₄ = 4/3), or allow B′ = −A′ at the face, which breaks "B constant".
- **D-Isr-4.** The C₃ parity (O1).
