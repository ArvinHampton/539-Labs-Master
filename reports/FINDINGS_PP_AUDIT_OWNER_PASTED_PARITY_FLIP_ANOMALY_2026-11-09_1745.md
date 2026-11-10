# FINDINGS: PP audit of the Owner-pasted parity-flip / anomaly argument (record fe8bcb00, t4363) side by side with NL's O1 resolution (13ccd162, 1736). 2026-11-09 17:45 CST (America/Chicago)
Agent: Professor Proof (Soft SF). Additive file; nothing edited. No CERT. Nothing adopted. No message sent. No Gemini / outside service. Public arXiv metadata read only (titles verified via export.arxiv.org at 17:41 CST); **all citations CONDITIONAL**. Convention G = ½T^(EH) (OW 2d1e877e). Vacuum HOLD unchanged. b, J7 OPEN. O1 not locked.
Tip: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 re-hashed 17:37 and 17:45: **MATCH (untouched)**.
Scratch: /workspace/audit-scratch/pp_parity_1740/parity_cases.py 26125f67… / parity_cases.log ca971a5e… (sidecars written).

## SUMMARY TABLE (one parity verdict per premise)
Standing premise P-b: the face Z₂ σ is a symmetry of 11D sugra including ∫C∧G∧G and ∫C∧I₈. Notation: σ = (r → 2r_b − r) × τ, τ the action on the face (x, Σ, S⁴); s_x, s_Σ, s₄ orientation signs of τ; s₁₁ = −s_x s_Σ s₄.

| premise | G₄ / S⁴-flux parity | net face M5 charge (brane count) | grade |
|---|---|---|---|
| **P-fix**: face is a Z₂ fixed plane (τ = id) | **ODD, forced.** Even is impossible. "Flip" (worldvolume reversal) is impossible: τ = id ⇒ s_x = s_Σ = +1 | Net face charge = 2N_flux. Without E₈ instantons N_b = 2N_flux ∈ 2ℤ. With the HW E₈ wall sector, N_M5 + n_inst = 2N_flux. At 4880: bulk N = 4880 ⇒ 9760, or N_b = 4880 ⇒ N_flux = 2440 | odd PROVED given P-b; even REFUTED (proof); E₈ requirement CONDITIONAL (HW) |
| **P-nofix (i)**: σ is a Z₂ but τ ≠ id is a face isometry with τ*h = h and τ*K = K (Israel [K] = 2K still holds). Sub-case s_x s_Σ = −1 (τ reverses the M5 worldvolume, the Owner's "flip"), e.g. τ = anticonformal involution of Σ × (φ_i → −φ_i) | **EVEN** (PD1) | **Net face charge 0.** The stack's τ-image is an anti-stack, so N_b(net) = 0. This conflicts with brane := wrapped M5 stack (f283cffd) unless M5/anti-M5 image pairs are admitted | even PROVED given P-b + this τ; existence of τ CONDITIONAL (Σ modulus must admit the involution; leg-by-leg G₄ check not done); static even face additionally obstructed by PD4 (CONDITIONAL) |
| **P-nofix (ii)**: τ ≠ id, s_x s_Σ = +1, e.g. τ = antipodal map of the S⁴ fibre (free on the face) | **ODD** (PD1) | 2N_flux (on the cover) | PROVED given P-b + τ; consistency of the τ action on legs (β), (γ) CONDITIONAL |
| **P-nofix (iii)**: no Z₂ at all (two-sided junction P1/P2) | **Undefined** (PD5) | N_b = N₊ − N₋ ∈ ℤ, free | PROVED |

**Bottom line.** P-fix forces ODD. P-nofix does not force a parity: the parity is −s_x s_Σ, set by how τ acts, or it is undefined if there is no Z₂. The Owner text's "flip ⇒ even" is valid only in P-nofix (i). There it costs zero net M5 charge on the face. NL (1736) is right under P-fix. Its claim that [K] = 2K needs pointwise fixing is REFUTED, so P-fix is a premise, not a consequence. PD1, NL A3 and the Owner text's first step are **the same statement** and agree.

## Rollup
PROVED 16 · CONDITIONAL 7 · OPEN 5 · REFUTED 7 · PENDING 1 (36 items).
- (a) **Not sound.** The pasted text names no anomaly and none of the three candidate mechanisms gives a mismatch for odd S⁴ flux (§2).
- (b) It is conditional on an unstated premise, P-nofix (i): σ acts non-trivially on the face and reverses the worldvolume orientation. That premise contradicts "fixed plane". It is also conditional on P-b and on admitting net-zero face charge (§3).
- (c) It shows at most **CONSISTENT** (in P-nofix (i) only). **REQUIRED is REFUTED** (§4).
- "PP's 17:02 audit" exists (5cbd050a). It contains **nothing** about charge-to-tension gradients or stability, and its numbers are for the **odd** case. Attribution REFUTED by quotation (§5).
- "External topological invariants": not defined anywhere on disk (§5).

---
## 0. Integrity
- **I1 [PROVED].** Each sha256 equals its sidecar (re-hashed 17:37–17:42):
  - record t4363 fe8bcb00e623f7ad…
  - PP 1702 5cbd050abc2fe085…
  - PP 1730 f3c5d73f371b31a7…
  - NL 1711 53096d433d062f51…
  - NL 1713 e2065e05c7d55211…
  - NL 1736 13ccd16251d055aa…
  - OW 9a8ced02a7053846…
  - OW t4367 602b6427feeab322… (17:38, a conditional plan, not a decision: the Owner *intends* to define "Z₂ flips the M5 worldvolume orientation" after this report)
  - /workspace/nl-junction-1730/ face.py, flowlin.py, resolve.py and resolve_1736.log: all sha256 -c OK.
- **I2 [PROVED].** Tip MATCH (header).
- Record fe8bcb00 was read in full. Its seven conflicts are confirmed:
  - #1: the argument does not lock O1 under 9a8ced02 (confirmed, §6).
  - #2: no PP 17:02 gradient audit (confirmed, §5).
  - #3–#5, J7 / Warden / b: not physics, not graded here.
  - #6, Ξ wording: consistent.
  - #7: no conflict.

## 1. Geometry and sign bookkeeping (common to both arguments)
Directions are x (ℝ^{1,3}, 4), Σ (2), r (1) and S⁴ (4). The M5 worldvolume is x × Σ. The M5 transverse space is (r, S⁴). The face is r = r_b, of dimension 10.
- **C0 [PROVED] M-theory parity rule.** Under pullback by σ an 11-form integral picks up s₁₁. ∫C∧G∧G is cubic in C, ∫C∧I₈ is linear in C, and I₈ is a Pontryagin form.
  - With C → c·σ*C, both terms are invariant iff c = s₁₁ (parity_cases.log).
  - So the orbifold condition is G = s₁₁σ*G, and there is no C → −C at fixed orientation. This confirms NL A2 and PD1's premise. Witten hep-th/9609122 ties this parity to shifted quantization (CONDITIONAL citation); it is not needed here.
- **R1 [PROVED] A radial reflection preserves the M5 worldvolume orientation.** τ = id on the face, so s_x = s_Σ = s₄ = +1. σ restricted to the worldvolume is the identity. It reverses the transverse orientation (s_r s₄ = −1) and the total orientation (s₁₁ = −1). An M5 on the face is mapped to itself, not to an anti-M5. This is exactly the HW situation of M5s parallel to the wall.
- **R2 [PROVED] Meaning of "S⁴ flux odd".** Write Φ(r) = ∫_{S⁴_r} G₄ with one fixed S⁴ orientation on both sides.
  - The fibre S⁴ at fixed r does not by itself link a stack on the face. The stack's linking 4-cycle in the 5D transverse (r, S⁴) space is S⁴_{r₊} − S⁴_{r₋}, by Stokes on [r₋, r₊] × S⁴.
  - So the stack charge is Φ(r₊) − Φ(r₋) = (1 − ε)Φ, where Φ(r′) = εΦ(r) and ε = s₁₁s₄.
  - "Odd" (ε = −1) means equal outward-normal flux N on each side, so the face carries 2N. "Even" means the flux passes straight through, so the face carries 0.
- **R3 [PROVED] PD1 = NL A3 = Owner step 1.** ε = s₁₁s₄ = −s_x s_Σ, so odd ⇔ s_x s_Σ = +1 ⇔ σ preserves the worldvolume orientation.
  - NL's radial reflection is the case s_x = s_Σ = +1 ⇒ odd. This is consistent with PD1, and there is no conflict between PP and NL.
  - The Owner text and NL disagree only on the premise: whether σ reverses the worldvolume (possible only if τ ≠ id).
  - parity_cases.log verifies PD1 on five τ's.
- **Q1 [PROVED] Odd quantized flux is possible.** TM|_{S⁴} = TS⁴ ⊕ trivial, and TS⁴ is stably trivial, so p₁ = 0 and λ|_{S⁴} = 0. Witten's condition G/2π − λ/2 ∈ H⁴(ℤ) (CONDITIONAL citation hep-th/9609122) becomes Φ/(2πℓ_P)³ ∈ ℤ.
  - +N and −N are both integral. Charge conservation (Bianchi plus R2) puts 2N on the face.
  - So N units can be odd under a Z₂ that fixes the face: there is neither a quantization obstruction nor a conservation obstruction.

## 2. Question (a): soundness and which anomaly
- **OT1 [PROVED given P-b]** "Preserving orientation forces odd S⁴ flux." This is correct (R3).
- **OT2a [REFUTED, proof] A flux-quantization obstruction to odd flux.** None exists (Q1): λ|_{S⁴} = 0, so there is no half-integer shift on S⁴ and ±N ∈ ℤ.
- **OT2b [REFUTED, counterexample; the counterexample's citations are CONDITIONAL] "Odd ⇒ anomaly-matching failure for the localized M5 stack" via the worldvolume anomaly or inflow.**
  - The M5 worldvolume anomaly (chiral 2-form and fermions, including the normal-bundle SO(5) part ∝ N³p₂(N)/24) is cancelled locally by inflow from ∫C∧G∧G and ∫C∧I₈ (Freed–Harvey–Minasian–Moore, hep-th/9803205, CONDITIONAL). The inflow depends on the stack's own charge, i.e. on [Φ] = 2N in the odd case. It does not depend on the global sign convention on the far side.
  - The odd configuration with M5s on a P-fix wall is the HW wall with M5s at it, i.e. small E₈ instantons (Ganor–Hanany hep-th/9602120; Seiberg–Witten hep-th/9603003; both CONDITIONAL). Its anomaly polynomial has been computed and matches (Ohmori–Shimizu–Tachikawa, "Anomaly polynomial of E-string theories", 1404.3887, CONDITIONAL).
  - So the standard literature contains an anomaly-consistent odd configuration with M5s on the fixed plane. Nothing on disk computes a mismatch.
- **OT2c [CONDITIONAL on HW hep-th/9510209, 9603142] The HW-type anomaly that does exist.** A 10D fixed plane of an orientation-reversing Z₂ (P-fix) carries a localized gravitational anomaly. It is cancelled only by an E₈ vector multiplet on the plane (= NL A6).
  - This anomaly comes from the **fixed plane itself**, with or without M5s, and with G₄ odd, which the CS term forces. It is **not** caused by the odd flux.
  - **Flipping cannot cure it.** Under P-fix a flip is impossible (OT3-fix). Under P-nofix there is no 10D fixed plane, so there is no HW anomaly whatever the parity.
- **Answer (a).** The argument is **not sound**. It names no anomaly.
  - (1) Worldvolume anomaly / inflow: no mismatch for odd. The E-string is the consistent counterexample (CONDITIONAL).
  - (2) Shifted quantization: no obstruction on S⁴ (PROVED).
  - (3) HW Z₂ logic: this is exactly the setting that **forces** odd (G_{ABCD} odd under x¹¹ → −x¹¹ by the CS term). Its anomaly is a fixed-plane gravitational anomaly cancelled by E₈, independent of a parity "choice".
  - **What is actually forced for an M5 stack wrapping the face** (P-fix): odd flux and net face charge 2N_flux = N_M5 + n_inst. An E₈ wall sector is required for anomaly cancellation (CONDITIONAL), and the M5s are small E₈ instantons (CONDITIONAL).

## 3. Question (b): conditional on what
- **OT3-nofix [PROVED given P-b and P-nofix (i)] "Flipping gives even."** This holds if σ = reflection × τ with τ a face isometry reversing the worldvolume (s_x s_Σ = −1) and τ*K = K.
  - Examples (parity_cases.log):
    - τ = anticonformal involution of Σ × (φ_i → −φ_i). φ must flip so that F ∝ vol_Σ is preserved. This gives s₁₁ = +1 and a 7D fixed locus (an A₁-type ℝ⁴/ℤ₂, so 7D SU(2) and no chiral anomaly; CONDITIONAL).
    - τ = x¹ reflection. This breaks 4D Poincaré and gives a codim-2 cone; not recommended.
- **OT3-fix [REFUTED, proof] Flip under P-fix.** P-fix means τ = id, so s_x = s_Σ = +1, which is not a flip. "Fixed plane" and "flips the worldvolume" are **mutually contradictory** definitions.
- **Assumptions the pasted text needs, none on record:**
  - (i) σ is a symmetry of the full theory, including CS and C∧I₈ (P-b; this fixes C → s₁₁σ*C);
  - (ii) the face is **not** a pointwise fixed locus: τ ≠ id;
  - (iii) τ reverses x or Σ and is an isometry of the kept side, preserving h, K, A_i and all G₄ legs (α, β, γ). For Σ this needs a genus-2 modulus admitting an anticonformal involution, which ties to the OPEN Σ shape/systole item;
  - (iv) the Owner admits **zero net M5 charge** on the face (M5/anti-M5 image pairs), against brane := stack of wrapped M5s;
  - (v) a resolution of PD4: in the even case the dr∧fib³ legs (β) are odd, so a static face needs λ₁′ = λ₂′ = 0 at r_b, which holds at no finite face numerically (CONDITIONAL, NL parity_lprime_full.log), or else Euclidean M2 sources;
  - (vi) no E₈-type boundary degrees of freedom are needed. That holds automatically in P-nofix (no 10D orientation-reversing fixed plane), whereas P-fix needs them (OT2c).
- **PD4 inherited [CONDITIONAL].** The even static face is obstructed unless λ′(r_b) = 0.

## 4. Question (c): required or consistent
- **OT6 [REFUTED] "Flipping is REQUIRED."**
  - Under P-fix flipping is impossible (OT3-fix, proof), so it cannot be required there. Odd is forced and, with E₈, is the standard consistent HW wall (CONDITIONAL).
  - Under P-nofix, τ = antipodal map of the S⁴ fibre gives an orientation-preserving, freely acting σ with **odd** flux and no fixed plane (parity_cases.log). So even is not forced there either. The τ-invariance of legs (β, γ) is CONDITIONAL; K-invariance holds because the face data depend on μ only through μ_a² (face.py: Δ̃ = X·μ²).
  - No premise on disk forces even.
- **OT6′ [CONDITIONAL] "Flipping is CONSISTENT."** Only under P-nofix (i), and at the cost of net face charge 0 (PROVED, R2/PD2) and the PD4 static-face obstruction (CONDITIONAL).

## 5. "PP's 17:02 audit", "charge-to-tension gradients", "external topological invariants"
- **OT5a [REFUTED, by quotation] Attribution.** The only candidate is FINDINGS_PP_AUDIT_NL_JUNCTION_AND_XI_FRICKE_2026-11-09_1702.md (5cbd050a…, sidecar OK; file mtime 16:59 CST, header "17:02 CST").
  - `grep -ci "gradient\|stabil"` = **0**.
  - The relevant lines (L55–58) read, verbatim:
    - "**P3e (CONDITIONAL; parity OPEN).**"
    - "Charge per brane: 2κ²T_M5 = 8π³ = (2π)³ = the flux quantum (PROVED). So N_b = 2N if G₄|_{S⁴} is Z₂-odd, and 0 if even."
    - "Tension/charge (odd case): 12568.6/9760 = 1.288 (MN2), 1.255 (MN1), 1.313 (z = 2), 1.326 (z = 3); 5/3 at the UV end. Either way charge ≠ tension, so the face is not BPS."
    - "**Parity OPEN:** no Owner record on disk settles the O1 Z₂ parity of C₃/G₄ (grep of OWNER_WRITE*, 16:58)."
  - So the file reports static tension/charge **ratios**, not gradients. It makes no stability claim, says the face is non-BPS, computes the ratio **only for odd parity**, and states that even parity gives net charge 0, for which the ratio is undefined (infinite). Nothing in it supports "flipping enforces stability of charge-to-tension gradients". If anything it shows the even case removes the charge entirely.
- **OT5b [OPEN; contrary indication CONDITIONAL] "Stability".** No stability notion is defined on disk. In the even case the τ-image of an M5 stack is an anti-stack: a non-BPS M5/anti-M5 system, generically attractive and unstable (CONDITIONAL). This cuts against the pasted claim.
- **OT4 [OPEN, undefined] "External topological invariants".** A grep of reports/*.md finds the phrase only in record fe8bcb00 itself.
- **OT4′ [PROVED].** Whatever is meant, the bulk invariants (N_flux on the kept side, g = 2, twist (p, q), Ξ) are identical under both parities, so preserving them does not distinguish the parities. The face's net M5 charge, also topological, **changes** from 2N_flux (odd) to 0 (even).

## 6. NL 1736 §A graded (side by side)
- **NA0 [REFUTED, counterexample] P-a's justification "[K] = 2K requires the face fixed pointwise".** For σ = reflection × τ with τ an isometry of (h, K) on the face, the jump at y is K(y) + τ*K(τ⁻¹y) = 2K(y). The antipodal S⁴ map and the Σ involution × φ-conjugation are examples: K depends on (r, μ_a²) only.
  - P-a is therefore a **premise** (= P-fix), not a consequence of the 1655–1713 Israel algebra.
- **NA1 [PROVED given P-fix].** **NA2 [PROVED given P-b]** (= C0). **NA3 [PROVED given P-fix, P-b]** (= R1 + R3; agrees with PD1).
- **NA4 [CONDITIONAL].** The net face charge = 2N_flux is PROVED. But once the E₈ sector of NA6 is present, the M5 count is N_b = 2N_flux − n_inst. "N_b = 2N_flux, N_b ∈ 2ℤ" needs n_inst = 0.
- **NA5 [PROVED]** (= Q1). **NA6 [CONDITIONAL, HW]** Agreed. **NA7 [OPEN]** Agreed (inflow for an M5 stack on an HW wall; E-string literature is the lead, CONDITIONAL).
- **NA8 [PROVED, scope corrected].** Even is impossible under **P-fix**. This is valid only for P-fix, not for every Z₂ pairing with [K] = 2K (see NA0 and P-nofix (i)).
- **NA9a [PROVED] (PD5).** For a two-sided gluing with no σ, O1 is undefined.
- **NA9b [REFUTED, counterexample] "If the face is not a fixed plane, O1 has no meaning."** P-nofix (i)/(ii) are Z₂ quotients with τ ≠ id and a defined parity −s_x s_Σ (parity_cases.log).
  - **The remaining Owner question is not only "is the face a fixed plane?" but "how does σ act on (x, Σ, S⁴)?"**
- **Which is right?** NL is right under P-fix (odd forced, even REFUTED). The Owner text's even is right only under P-nofix (i). There it is consistent, never required, and carries net-zero face charge and the PD4 obstruction.
- **NL 1736 §B–§D [PENDING].** Not audited in this file.
- **P-nofix (ii) antipodal-odd option [CONDITIONAL]**, pending a (β, γ) leg check. **P-nofix (i) Σ-involution-even option [CONDITIONAL]**, pending a Σ modulus with an anticonformal involution, the leg check and PD4.

## 7. What would lock even parity under OW 9a8ced02 [OPEN]
No derivation from premises now on disk can force even (counterexamples: P-fix ⇒ odd; antipodal τ ⇒ odd). Even can only be **derived from a definition of σ**, not declared. Required, then PP audit:
1. An Owner definition of σ including τ with s_x s_Σ = −1, and acceptance that the face is **not** a pointwise fixed plane. "Fixed plane + flip" is contradictory. For t4367: defining "flips the M5 worldvolume orientation" commits to P-nofix (i), and the Owner must say whether Σ or x is reversed.
2. A proof that τ is an isometry of the kept side preserving h, K, A_i and every CLP G₄ leg (α, β, γ). For a Σ reversal this needs a genus-2 modulus with an anticonformal involution and φ_i → −φ_i.
3. Analysis of Fix(σ) (for the Σ option, a 7D ℝ⁴/ℤ₂ locus) and of its anomaly and gauge sector. C0 already makes σ a symmetry of the CS and C∧I₈ terms.
4. Reconciliation of net face charge 0 with brane := wrapped M5 stack. The options are admitting M5/anti-M5 image pairs, with a stability analysis, or redefining the brane.
5. Resolution of PD4: show that legs (β) are τ-even for the chosen τ, or find faces with λ′(r_b) = 0, or admit non-static faces or Euclidean M2 sources.
6. Then PD1 gives even as a derivation, which meets the letter of 9a8ced02 (derived, not declared) once items 1–5 are audited.

## Tally detail
- PROVED 16: I1, I2, C0, R1, R2, R3, Q1, OT1, OT3-nofix, OT4′, NA1, NA2, NA3, NA5, NA8, NA9a.
- CONDITIONAL 7: OT2c, OT6′, NA4, NA6, P-nofix(ii) option, P-nofix(i) option, PD4 inherited.
- OPEN 5: OT4, OT5b, NA7, §7 lock derivation, O1 itself.
- REFUTED 7: OT2a, OT2b (counterexample citations CONDITIONAL), OT3-fix, OT5a, OT6, NA0, NA9b.
- PENDING 1: NL 1736 §B–§D.

O1 stays **OPEN**. Both parities stay recorded for every O1-dependent result. Tip 7cddb188 untouched (MATCH). No CERT. Nothing adopted. No message sent.
