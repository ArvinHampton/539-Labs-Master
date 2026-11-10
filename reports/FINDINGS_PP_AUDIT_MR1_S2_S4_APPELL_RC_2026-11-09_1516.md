# FINDINGS: PP audit of MR1 "closing S2–S4 of B§III (Appell→R_c)". 2026-11-09 (America/Chicago)
Agent: Professor Proof (Soft SF). Additive file. The audited file is unchanged. Tip 7cddb188… untouched. No CERT. No outside service. No Gemini.
Script and log: /workspace/audit-scratch/pp_rc_def_1512/mr1.gp and mr1.log (PARI 2.17.2, \p 60).

## 0. Hashes
- **Audited file: MATCH.** FINDINGS_MR1_B_SEC3_APPELL_RC_S2_S4_CLOSE_ADOPTED_DEFS_2026-11-09.md, sha256 48a2d68710e8ca7725ac064237641abaac1ca184f2f8977486988560a0741dfb. The sidecar matches.
- **Authority: MATCH.** OW 5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c.
- **B: sha MATCH (9c6f83da4f8636b0a6afbf108cbf7139210a82be936cadc94b772784451ded6d), with a provenance note.** B is OWNER_DOCUMENT_FORMAL_RESOLUTIONS_STRUCTURAL_CORRECTIONS_COMPENDIUM_2026-11-05.md. It sits only in distributions/gemini-incoming-20261105-1536/…, so it is Gemini-incoming material and not an Owner write. MR1 calls it "B" without this note.

## R1: ε = 6+√35 is the fundamental unit, and Λ₀ = Reg/√10. **PROVED, confirmed and certified.**
- bnfinit(x²−35, 1) gives disc 140, nfbasis [1, x], so O_K = ℤ[√35]. This matches 35 ≡ 3 mod 4, and the two orders are the same.
- The fundamental unit is x+6, with norm +1. quadunit(140) = 6+w, norm 1.
- **bnfcertify = 1.** The result is unconditional and does not depend on GRH.
- There is no unit of norm −1, because x² ≡ −1 has no solution mod 7.
- Reg − ln(6+√35) = −3×10⁻⁷⁷, which is 0 to working precision. Exactly, Reg = ln ε by definition, given ε fundamental.
- Λ₀ = Reg/√10 = 0.78357721761742351…. Compared with OW 45aeba5f's 0.783577: they agree to 6 decimals (difference 2.18×10⁻⁷). They differ at the 7th digit (…7217 against …7000) because 0.783577 is a truncation.

## R2: Λ₀ = √(7/8)·L(1,χ₁₄₀). **PROVED. Upgrade MR1's label.**
- **h = 2 exactly.** qfbclassno(140) = 2, quadclassunit(140).no = 2, and bnfinit .no = 2 with cyc [2]. bnfcertify = 1, so h = 2 is certified.
- **Dirichlet's class number formula** (a standard theorem) gives L(1,χ_D) = 2h·ln ε/√D for real quadratic K. With D = 140 and h = 2 this is L(1,χ₁₄₀) = 4 ln ε/√140 = 2 ln ε/√35.
- **The identity is exact algebra.** √(7/8)·2 ln ε/√35 = 2 ln ε/√40 = ln ε/√10 = Λ₀.
- **Independent numerical check.** lfun(lfuncreate(140), 1) = 0.83767928125885852589… Both 2hReg/√140 − L and √(7/8)L − Λ₀ come out at −8.6×10⁻⁷⁸.
- Since ζ_K = ζ·L(s,χ₁₄₀), Res ζ_K = L(1,χ₁₄₀) = 0.837679. This agrees with MR1's "Prop. 41.5 residue".
- **Correction to MR1.** The partial sum Σ_{n≤2·10⁶}χ(n)/n with "h ≈ 1.999995" is not a proof, because no bound on the tail is given. MR1's label "PROVED (class number cited, numerically confirmed)" should become **PROVED (h = 2 certified by bnfcertify; class number formula)**.

## S3b: 1.59543 against κ
- **Arithmetic: PROVED and correct.** κ = 1.5976222400652488…
  - κ − 1.59543 = +0.00219224, matching MR1's +0.0021922.
  - κ − √(2/0.7858) = +0.00226119, where √(2/0.7858) = 1.5953611. MR1's +0.0022612 is the correct rounding.
- **Where 1.59543 comes from.** B l.31–32: "…parameter-free boundary scale R_c ≈ 1.5954 was tied back to … Λ_0 ≈ 0.7858 (√(2/Λ_0) ≈ 1.595361) … The explicit evaluation yields: R_c = 1.59543..."
  - B gives no computation behind it and names no Appell–Lerch object (MR1 S2b, agreed).
  - 1.59543 implies Λ₀ = 2/1.59543² = 0.7857321. That matches neither 0.7858 nor the adopted 0.7835772.
  - It agrees with Pack H's 1.59543590 to the 5 digits B prints (9ea1a7ad, l.22).
  - So it is a third, unsourced value, distinct from 1.595361, which 45aeba5f superseded.
- **Label verdict: partly correct. I recommend a relabel.**
  - "1.59543 ≠ κ" is a **PROVED** arithmetic fact, with Δ = 2.19×10⁻³, about 1400 times the rounding scale of a 5-digit value.
  - Under OW 45aeba5f and OW 5a6e7177, κ, and so R_c/ℓ_P, is an Owner **definition**. B's "R_c = 1.59543" is therefore not a competing proof that someone could refute. It is an unsourced value that is **inconsistent with the adopted definition**, so it is superseded, in the same way 45aeba5f handled 1.595361.
  - "REFUTED" requires a proof or counterexample against the claim's own content. B's own content ("evaluation of a normalized Appell–Lerch boundary sum") is undefined, so it is **OPEN**, not REFUTED.
  - Suggested wording: **S3b: PROVED 1.59543 ≠ κ. B's value is SUPERSEDED by Owner definition (not adopted). B's Appell–Lerch evaluation is OPEN (undefined object).**
  - MR1's conditional REFUTED is not wrong as logic: if B's number is read as κ, the statement is false. But it mis-frames a definitional supersession as a refutation.

## Scan of MR1's other labels
| MR1 item | MR1 label | PP audit |
|---|---|---|
| R1 | PROVED | **Agree.** Now certified (bnfcertify). |
| R2 | PROVED (cited + numerical) | **Agree on the claim. Fix the basis** to h certified; the partial sum is not a proof. |
| l.26 "ties Λ₀ to the Weil(140) side" | unlabeled | An interpretive remark, not a result. Should be labeled OPEN or "remark". |
| S2a | PROVED (definitional) | **Relabel** to "CLOSED by Owner definition (not a proof)". The phrase "nothing downstream depends on it" is not shown. |
| S2b | OPEN | **Agree.** The literature remark (Hurwitz/Zagier mock class numbers) should be marked CONDITIONAL (literature). |
| S2c | OPEN | **Agree.** For the 4-regular tree (PGL₂(ℚ₃)), the spectral radius is 2√3 = 3.4641016 and the growth rate is 3. Both values are correct, and neither equals κ. |
| S3a | PROVED | **Agree.** The value matches to 60 digits. |
| S3b | REFUTED (conditional) | **Relabel** as above. |
| S3c | FLAG | **Agree.** |
| S3d | PROVED (units) | **Agree.** |
| S4a | PROVED (conditional on adoption) | **Agree on the content.** This is a statement about the form of the definition and is true by inspection. Use one label: PROVED (about the definition). |
| S4b, S4c | OPEN | **Agree.** For S4c, √(7/8) = √35/(2√10) is exact (R2). |

No numerical errors were found in MR1's file.

## Rollup (PP audit items)
- **PROVED 5:** R1, R2, S3b arithmetic and source, S2c values, and the "no numerical errors" check.
- **CONDITIONAL 1:** the S2b literature remark.
- **OPEN 3:** S2b link, S4b, S4c, as MR1 has them.
- **REFUTED 0.**
- **Relabels recommended 4:** R2 basis, S2a, S3b, S4a single label. Also the l.26 remark and B's provenance note.

## Verdict
MR1's mathematics is correct.
- R1 and R2 hold and are now unconditionally certified, with h(140) = 2 and ε = 6+√35 of norm +1.
- Λ₀ = Reg(ℚ(√35))/√10 = √(7/8)·L(1,χ₁₄₀) holds exactly.
- B's 1.59543 is an unsourced third value, with implied Λ₀ = 0.785732. It differs from κ = 1.5976222 by a proven 2.19×10⁻³ and should be recorded as superseded by the Owner definition, not "refuted".
- Four labels need tightening; none of them changes a conclusion.
