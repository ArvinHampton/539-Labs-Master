# FINDINGS: PP audit of MR2 KK Group A spin-2, stage 1 (8ca7b93a) and stage 2 (7491cdb8)
Auditor: PP (Professor Proof), Soft SF audit agent. Written 20:18 CST (America/Chicago). Scope: OW d5eaeef3 under OW 8b26c786 (Group A KK).
- Labels: PROVED / CONDITIONAL / OPEN / REFUTED / PENDING. Float-only = COND. A citation alone never makes PROVED. A claim with a stated premise is graded as an implication.
- Additive new file; nothing edited; nothing sent; no CERT; no Gemini; nothing adopted. Naming: "resonant algebra" (RA-n labels are MR2's).
- Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, unchanged.

## 1. Provenance
| file | sha256 (recomputed) | sidecar | mtime CST |
|---|---|---|---|
| MR2_MN2_KK_A_S4_DEPENDENT_SPIN2_AUT48_2026-11-09.py | 17f821d25491ea072cd574238f052b30d8c7dcc8e5681ae2b44e5e642d5c977a | MATCH | 20:03:25.9 (r--r--r--) |
| …S4_DEPENDENT….log | c4fc9660c92edc2c8824e21b2758087c5ff750848aedb4c708fdd771708bccef | MATCH | 20:03:40.3 |
| …S4_DEPENDENT….md | 8ca7b93a1f011b19a1e2f29e9fe5e5ce3a4b6edff6bbd373305a80c7696cd24d | MATCH | 20:04:13.3 |
| MR2_MN2_KK_A_CHARGED_S4_TOWERS_AUT48_2026-11-09.py | 92fe47d02c3c2295ea81780fc49c0726670116a855350b22244b063afee256fb | MATCH | 20:08:32.0 (r--r--r--) |
| …CHARGED….log | 5d0d3b76e4ffc171d6f05ecbff28e6eba547cf04f154dbe221991265b6340362 | MATCH | 20:08:45.8 |
| …CHARGED….md | 7491cdb8492de4948ffdee830e3bc39634ca2db5ee34f5823775a9a060d36545 | MATCH | 20:09:35.4 |
- .py before log: confirmed for both (gaps 14.4 s and 13.8 s match the logged 14.0 s / 13.2 s runtimes).
- Reruns on copies (/workspace/pp_kkA_2015/s1.py, s2.py; same shas): exit 0, 14.0 s and 13.9 s. Output **byte-identical** to MR2's logs except the runtime line (s1_rerun.log 9b9b030e…, s2_rerun.log 7d5654f7…).
- PP independent scripts (exact sympy): pp_indep.py d67e3880… / .log 17d0f1db…; pp_indep2.py 82036844… / .log 8b547502…; pp_indep3.py 5c563e00… / .log 1c683be8…. An exact symbolic (non-point) version of the RA-4 11D check was started and was interrupted before finishing, so it gives no result. RA-4 stays COND.

## 2. Independent checks
**Identity (RA-1x): exact, PROVED.** By hand and in sympy (pp_indep [1]):
- s = X₂ = 2^{2/5} and t = X₁ = 2^{−3/5}, with F₀ = X₀^{−2} = 2^{−4/5}. Then 4F₀st = 2, 4F₀s² = 4 and 4F₀t² = 1 exactly, and Hst − D ≡ 0.
- So ρ = (st)^{−1/2}cos²θ sinθ and the kinetic coefficient is 4√(st)cos²θ sinθ. The kinetic part is therefore 4F₀st = 2 times the round one.
- Potential: 4F₀D[j(j+1)s/cos² + q²t/sin²] = j(j+1)(4 + 2tan²) + q²(2cot² + 1) = 2[j(j+1)/cos² + q²/sin²] + 2j(j+1) − q².
- The identity is exact **for the reduced radial operator as written** (ansatz ψ = f(Σ)Θ(θ)Y_j(μ̂)e^{iqφ₁}, metric normalisation c = D^{−2/3}/4 with e^{2A} absorbed, so the round control gives 4ℓ(ℓ+3)). That reduced operator equals the 11D Bachas–Estes operator only up to float point checks (RA-1 / RA-4, COND).

**Round S⁴ spectrum and selection rule: PROVED.** The round radial operator with weight cos²θ sinθ maps cos^j sin^|q| X^N (X = cos 2θ) to cos^j sin^|q|[ℓ(ℓ+3)X^N + lower], with ℓ = j + |q| + 2N. This was checked exactly for j, q, N ∈ {0..3}, and the general-N symbolic form was printed (pp_indep [2]; the one "FAIL" line is the j = q = N = 0 zero polynomial, eigenvalue 0 = ℓ(ℓ+3), a test artefact).
- The operator is triangular with strictly increasing diagonal, so each eigenfunction is a Jacobi-type polynomial.
- The functions cos^j sin^|q|·poly(X) are dense in the weighted L² (Weierstrass on [−1,1] after the unitary change to a Jacobi weight).
- Hence the spectrum is exactly {ℓ(ℓ+3) : ℓ = j + |q| + 2n}. The selection rule ℓ = j + |q| + 2n is correct.

**Masses (exact arithmetic; pp_indep [3]):**
| m²L₅² | λ_Σ | ℓ | j | q | Δ = 2+√(4+m²) |
|---|---|---|---|---|---|
| 12 = 2·0 + 2·1·4 + 2·1·2 − 0 | 0 | 1 | 1 | 0 | 6 (exact) |
| 20 = 2·2·5 | 0 | 2 | 0 | 0 | 2+2√6 |
| 32 = 2·2·5 + 2·2·3 | 0 | 2 | 2 | 0 | 8 |
| 40 = 2·3·6 + 4 | 0 | 3 | 1 | 0 | 2+2√11 |
| 55.157117 = 2(1+23.0785585) + 8 − 1 | raised λ₁ᴵ | 1 | 0 | ±1 | 9.69137 |
| 84 = 2·6 + (2·6·9 − 36) | LLL of K⁶ (H = 36 + 6(1−6) = 6) | 6 | 0 | ±6 | 2+√88 = 11.38083 |
- **λ_Σ = 0 is allowed.** The constant on Σ is Aut⁺-invariant. The 12-mode is f = const times the ℓ = 1 harmonics m₀, m₂cosφ₂, m₂sinφ₂, i.e. the R³ coordinates: an SO(3)_R triplet.
- **Δ = 6.** Δ(Δ−4) = 12 has roots 6 and −2; the transverse-traceless spin-2 in AdS₅ obeys m²L² = Δ(Δ−4) with the root Δ ≥ 4, so Δ = 6 exactly. PROVED as arithmetic. The mode's existence is COND (RA-1, Bachas–Estes, MN2, HW).
- All other rows of both tables (56, 58.157, 60, 66.157; 70.157 … 120) were recomputed and agree.

**H⁰(K^m)^{Aut⁺}: PROVED by PP exact recomputation** (pp_indep2 [G]/[RA-6], pp_indep3 [CH]):
- Automorphisms of y² = x⁵ − x: A = (x→ix, y→ζ₈y), B = (x→(x+1)/(1−x), y→2√2·i·y/(1−x)³) (exact: (Bx⁵−Bx)(1−x)⁶ = −8(x⁵−x)), and J = (y→−y).
- The exact closure on H⁰(K) has order **48**.
- Basis x^aω^m (a ≤ m), y·x^bω^m (b ≤ m−3), with dimension 2m−1 (2 at m = 1). Pullbacks were asserted to stay in the span.
- Exact common fixed space of A, B, J over ℚ(ζ₈): **0,0,0,0,0,1,0,1** for m = 1..8.
- The exact character average over all 48 elements gives the same row. The decomposition tr|H⁰(K^m) = χ_{Sym^m ρ} + det·χ_{Sym^{m−3}ρ} holds exactly for all 48 elements and m ≤ 8.
- **Orbifold control (exact integers).** dim = −(2m−1) + ⌊m/2⌋ + ⌊2m/3⌋ + ⌊7m/8⌋ gives 0,0,0,0,1,0,1 for m = 2..8, and m = 1 gives g₀ = 0.
- **Signature (2,3,8).** Riemann–Hurwitz forces it: 48(−2 + 1/2 + 2/3 + 7/8) = 2, and among genus-0 signatures with periods dividing 48 only (2,3,8) has area 1/24.
- **MR2's own basis is float, not exact.** It uses np.linalg.eigvals on complex-float matrices, then int(round(mean)), and the η = dx³/y² det check is also float, with no error bound. On its own that would be COND. The grade PROVED stands **on PP's exact recomputation**.
- Group identification: the result is PROVED for the order-48 group ⟨A,B,J⟩. Identifying it with all of Aut⁺ inherits the ecee2668 §1 status.

**Landau ladder (pp_indep2 [L]):**
- Exact: H_b = Δ_{2b} + b², Δ_{k+2}R_k = R_kΔ_k and L_{k+2}R_k = Δ_k + (k/2)(1+k/2).
- PP also checked a general holomorphic factor: v^{k/2}g(u+iv) has Δ_k-eigenvalue (k/2)(1−k/2) and L_k = 0. The sympy printout is unsimplified; it simplifies to 0 by hand. The anti-holomorphic version does not.
- On K^n (b = n, weight 2n): H = n² + m(1−m), m = 1..n, with multiplicity h⁰(K^m). It equals n(2k+1) − k(k+1) with k = n−m. The LLL is m = n, at H = n.
- Raised scalars: H = n² + λ, λ > 0. Constants are killed by R₀.
- Sign convention: s = +1 (∂_u − iq/v) matches, and s = −1 fails in all 4 controls. ±q give conjugate representations with equal invariant counts, so the holomorphic/anti-holomorphic choice does not affect the tables.
- deg = q·Area/2π = 2q, consistent with K^q at a₁ = 1.
- The m range 1..n and the sign are correct. Completeness of the list (L² = ker L ⊕ closure of the image of R) is a citation: COND.

**Completeness below 120 (given RA-5).**
- PP's wider enumeration (q ≤ 12, j ≤ 9, n ≤ 5, three invariant λ) reproduces MR2's list exactly up to 120. The next entries are 127.157 (×2), 128 (q = 8 LLL) and 129 (q = 7, m = 6).
- H ≥ |q| always holds, so m²L₅² ≥ q² + 8|q|. That gives 105 at q = 7 (not enough by itself; MR2 handles q = 7 explicitly at 129), 128 at q = 8, and 153 at q = 9.
- So the q = 8 omission in the log does not leave a logical gap: the general bound already gives 128.

## 3. Stage 1 per-claim table (8ca7b93a)
| # | claim | MR2 | PP | reason |
|---|---|---|---|---|
| 1 | RA-1 reduction to 2(−Δ_Σ) + L_θ | COND | **COND** | Float point check at 15 points. Note: run at a₁ = 7/10, not MN2's a₁ = 1; harmless at q = 0 since ∂_{φ₁}ψ = 0. The product f(Σ)·S⁴ separability is covered only by the stage-2 RA-4 float check. |
| 2 | RA-1x shift identity μ = 2ℓ(ℓ+3) + 2j(j+1) − q² | PROVED | **PROVED** | Exact sympy; PP hand derivation and independent sympy agree. |
| 3 | RA-2 spectrum of the reduced L_θ | PROVED | **PROVED** | Round ℓ(ℓ+3) and the selection rule were proved by PP (triangular + density), so this is not citation-only. The controls are float and do not count. It is a statement about the reduced operator; the physical masses carry RA-1. |
| 4 | RA-3 selection | COND | **COND** | Canonical lift (ecee2668 §6, 3rd bullet), HW premise. |
| 5 | headline 12 (Δ 6, triplet), 20 (singlet), 32, 40 < 46.157 | COND | **COND** | Arithmetic and Δ exact (PROVED as arithmetic). Premises: Bachas–Estes, MN2, RA-1. The 46.157 comparison uses float λ₁ᴵ. |
| 6 | controls | COND | **COND** | float |
| 7 | q ≠ 0; rigorous Σ bounds | OPEN | **OPEN** | — |
**Stage 1: PROVED 2 · COND 4 · OPEN 1 · REF 0 = 7. CONFIRMED.**

## 4. Stage 2 per-claim table (7491cdb8)
| # | claim | MR2 | PP | reason |
|---|---|---|---|---|
| 1 | RA-4 charged reduction 2H_q + μ | COND | **COND** | Float, 4 modes × 3 points, rerun identical. The s = −1 control discriminates. The exact symbolic attempt was interrupted. |
| 2 | μ for q ≠ 0 | PROVED | **PROVED** | RA-1x is symbolic in q. |
| 3 | RA-5 ladder identities | PROVED | **PROVED** | Exact; PP re-derived them and added the holomorphic-factor check. |
| 4 | RA-5 completeness | COND | **COND** | Citation (Maass theory). |
| 5 | RA-6 invariant dims 0,0,0,0,0,1,0,1 | PROVED (computer-assisted) | **PROVED (on PP exact recomputation)** | MR2's own computation is float with rounding and no error bound, so on its own it would be COND. PP's exact ℚ(ζ₈) fixed-space and character computation and the exact orbifold integers agree. Valid for ⟨A,B,J⟩ of order 48. |
| 6 | RA-7 masses: 55.157 (q = ±1), 84 (q = ±6), complete below 120 | COND | **COND** | Arithmetic exact. Enumeration complete given RA-5. Premises: Bachas–Estes, MN2, RA-4, RA-5, float λ, canonical lift on K^q. |
| 7 | controls | COND | **COND** | float |
| 8 | scalars/vectors, rigorous bounds, > 120 | OPEN | **OPEN** | — |
**Stage 2: PROVED 3 · COND 4 · OPEN 1 · REF 0 = 8. CONFIRMED** (no grade changes; the basis for #5 is corrected).

Combined: 5 / 8 / 2 / 0 = 15.

## 5. Self-disclosures
1. The stage-1 log lists 46.157 as an S⁴ row: **CONFIRMED.** It is log line 27, with μ = 0, n = 0, j = 0 at λ = 23.07856, and is not skipped because only λ = 0 rows are excluded. The "above" tag is the `m2<2*lam[0]` test failing on equality.
2. 'ecee2668 §A' should be §6: **CONFIRMED.** ecee2668 has no §A. The lift text is §6 "Which are kept", which is the 3rd bullet of §6, so "§6 item 3" is correct.
3. Four 'does not match' lines in the stage-2 log: **CONFIRMED.** These are log lines 5, 7, 9 and 11, all with s = −1 (rel diff 0.5–3.5), i.e. the rejected control.
4. The stage-2 log's completeness line omits q = 8: **CONFIRMED.** It is a cosmetic slip, not a gap, because H ≥ |q| gives ≥ 128 at q = 8.

## 6. Fixes (for MR2's next erratum)
1. **Header times.** The stage-1 md says "~20:25 CST", but the file mtime is 20:04:13. The stage-2 md says "~20:45 CST", but its mtime is 20:09:35. The stated times are later than when the files were written; correct them.
2. **Stage-1 RA-1 a₁ value.** State that the check ran at a₁ = 7/10, not MN2's a₁ = 1, and why this is harmless at q = 0.
3. **Running max.** The stage-1 log's per-test "max rel diff over 3 random points" is a cumulative running max (`worst` is never reset). Cosmetic.
4. **RA-6 basis.** Replace "computer-assisted, exact group" with: the float character average (rounded) plus PP's exact recomputation in this file. The η det check was float.
5. **RA-6 scope.** Say "for ⟨A,B,J⟩ (order 48); identification with Aut⁺ per ecee2668 §1".
6. **Canonical-lift premise on K^q (RA-3/RA-7).** Lifts are unique only up to a character of Aut⁺ ≅ GL(2,3), and nontrivial characters exist, e.g. det. A twisted lift would change the invariant counts. Keep "canonical lift (ecee2668 §6)" as an explicit premise on every charged headline.
7. **Completeness wording.** Replace the log's "|q| ≥ 7 … ≥ 105" with the md version: H ≥ |q| gives q² + 8|q|, with q = 7 explicit at 129, q = 8 at 128 and q ≥ 9 at ≥ 153.
8. **RA-5 holomorphic sections.** The e4 identity was tested only on v^{k/2}. Add the general v^{k/2}g(u+iv) check, which PP verified.
9. **"Exact" wording.** The stage-1 headline "All are exact closed-form values given the operator" is fine. Keep "exact" off any comparison with 46.157, which uses float λ₁ᴵ.
10. Fold in self-disclosures 1–4 as stated.

No REFUTED items. Nothing adopted.
