# MR2 — Erratum to f4ee61f2 (HW fixed-plane boundary Ricci² / Weyl²) per PP audit 976e5621
2026-11-10, written 11:59:12 CST (America/Chicago), by MR2. This is an additive erratum only. Nothing was edited: not the parent f4ee61f2, not QC note 66f04088, not the parent's frozen script cd289c73 or log d5396417. The later filing 9811de14 and its script/log are also untouched and are **not** part of this erratum. PP did not audit them in this pass, and none of their grades are mixed in here. **Nothing adopted.** No CERT. No Gemini. Nothing sent. Junction **UNSOLVED**. Wording: resonant algebra.

## 0. Audit accepted
- **PP audit:** FINDINGS_PP_AUDIT_MR2_HW_PLANE_RICCI2_WEYL2_f4ee61f2_2026-11-10_1140.md, sha 976e56211308cf68e8ad80df063f99e08826d441e0f4d8a45242ad6fad01031c = sidecar, written 11:40:51 CST = mtime, mode 444. Accepted in full.
- **Ruled tally (stands):** PROVED 12 / CONDITIONAL 3 (10b, 13, 3G) / OPEN 2 (14, 16) / REFUTED 1 (10) = 18 + 1 bookkeeping.
  - The only grade move is row 3's general-D rider, PROVED-as-implication → CONDITIONAL on L-GN (3G).
  - Row 3's D = 4 instance stays PROVED. Its scope is one background jet (h0, h1, h2 at u = ½), with a 5-parameter κ in which κ_tv = 0. That scope is disclosed here.
- **Unchanged this write, re-hashed from reports/:**
  - parent f4ee61f26ad536800792b510f29f714c9c622fd11a8c378e545a8a38976c330d
  - QC 66f040887ebe660a6d540963b76f005ccd504e9d3e0f1a96b9b842b50f16e2bc
  - script cd289c73043595e303fc5f2d5a0c2e7ba0b2fa5b5cdef33489dcf0231a9c695d
  - log d5396417b7d3c3ad1212bb8748abe90b26910c89a448081334801038e10b6f23
  - 9811de14… (not in scope)

## 1. New files (reports/, sha = sidecar, relative names)
| file | sha256 | time (CST) |
|---|---|---|
| mr2_lgn_gaussian_normal_lemma_2026-11-10.py | 1728d877918a96c8d91862483ade6b376ce6d91fdd531b1bb6881d138a3d0a50 | frozen (sidecar + chmod a-w) 11:57:34 |
| mr2_lgn_gaussian_normal_lemma_2026-11-10.log | 20f66fe318da09fcbaf192a923291fe31e1dbe9ca03de0dac59ffcff32a09177 | 11:57:44 (sidecar 11:57:44) |
| this erratum | see .md.sha256 | header = mtime |

- **Freeze vs run.** Freeze at 11:57:34, then a deliberate 2 s wait. The log begins `RUN_START_WALLCLOCK 2026-11-10 11:57:36 CST` and `SCRIPT_SHA256 1728d877…` (= sidecar). The two times do not coincide. Exit 0, `ALL_CHECKS PASS` (21 checks), end 11:57:44.
- Originals are in /workspace/mr2-hw-curv-1110/, copied with `cp -p`.
- **Disclosure: pre-freeze scratch runs, none cited.**
  - /tmp/scratch_pretest3.py (585c778c…) was killed at a 700 s timeout. Its slow full-expansion Weyl step was then replaced by the exact affine-coefficient method (GK0–GK0b). Its L-GN and GK1–GK3 lines had passed.
  - /tmp/scratch_pretest3b.py (6850e132…) passed. It differs from the frozen script only in one zero test: `nsimplify` was replaced by `cancel` in C2d.
- **Method.** Exact SymPy throughout. Zero tests use `Poly.is_zero`, `expand(...)==0`, `diff(...)==0` or rational equality. No `simplify`, `nsimplify`, floats or allclose.

## 2. F-1 — L-GN stated and proved (proposed for PP regrade of 3G; no self-upgrade)
**Lemma L-GN.** Take any dimension D = n + 1, any signature of the tangent metric h, and no diagonality or x-independence assumption. In coordinates g = dy² + h_ab(y, x) dx^a dx^b, with K_ab := ½∂_y h_ab:
- (a) Gauss components R_abcd contain at most first y-derivatives of h.
- (b) Codazzi components R_yabc contain at most first y-derivatives of h (including mixed ∂_x∂_y h).
- (c) R_yayb = −∂_yK_ab + K_acK^c_b.
- (d) The second y-derivative ∂_y²h enters the Riemann tensor only through (c).

**Proof (index-generic).**
1. Since g_yy = 1 and g_ya = 0, the only nonzero Christoffel symbols are Γ^y_ab = −K_ab, Γ^a_yb = K^a_b and Γ^a_bc = γ^a_bc[h]. Here γ contains only x-derivatives of h. Γ^y_yy, Γ^y_ya and Γ^a_yy all vanish.
2. Every Γ therefore contains at most first derivatives of h, and y-derivatives appear only through K.
3. In R^ρ_σμν = ∂_μΓ^ρ_νσ − ∂_νΓ^ρ_μσ + Γ^ρ_μλΓ^λ_νσ − Γ^ρ_νλΓ^λ_μσ, a second y-derivative of h can appear only through ∂_y acting on K. That requires μ = y or ν = y.
4. (a): μ and ν are tangent, so only ∂_x acts. The products carry at most K (first y-derivative).
5. (b): R^y_abc = ∂_bΓ^y_ca − ∂_cΓ^y_ba + ΓΓ involves only ∂_xK.
6. (c): R^y_ayb = ∂_yΓ^y_ba − ∂_bΓ^y_ya + Γ^y_yλΓ^λ_ba − Γ^y_bλΓ^λ_ya.
   - ∂_yΓ^y_ba = −∂_yK_ab.
   - ∂_bΓ^y_ya = 0 and Γ^y_yλ = 0.
   - Γ^y_bλΓ^λ_ya = Γ^y_bcΓ^c_ya = −K_bcK^c_a.
   - Hence R^y_ayb = −∂_yK_ab + K_acK^c_b. Lower the index with g_yy = 1.
7. (d): a pair (y, y) vanishes by antisymmetry. Every other index placement is related to (a)–(c) by the Riemann symmetries. ∎

No step uses D, the signature or the form of h. Sign conventions K → −K leave (a)–(d) unchanged, because (c) is quadratic in K except for the ∂_yK term, whose sign follows K.

**Machine check [log L-GN(a,b,c), D = 4, 5, 6] — PROVED (exact).**
- The 2-jets at a point are fully general, with 84, 200 and 405 free symbols. All entries of ∂_yh, ∂_y²h, ∂_xh, ∂_x∂_yh and ∂_x²h are symbolic, non-diagonal and x-dependent.
- h(0) = η without loss of generality: a constant linear change of x preserves the Gaussian-normal form and acts tensorially.
- The validation (unit S² gives R_1212 = 1) fixes the sign convention.
- (a), (b) and (c) hold exactly in each of D = 4, 5 and 6.

**Consequence for 3G — proposed PROVED as implication of {P-reg, L-GN}.**
- Under a thin-wall smoothing, ∂_yK = [K]φ_ε + bounded (P-reg). By L-GN, every Riemann component is affine in 1/ε, and its δ part is −[K]_ab, carried by R_yayb alone.
- Elementary index algebra then gives, in every D and for every symmetric [K] with M := h⁻¹[K] (mixed):
  - Riem² δ²-coefficient: 4 tr M²
  - Ric_MN Ric^MN: tr M² + (tr M)²
  - R: δ-coefficient −2 tr M
  - Weyl²: 4(D−3)/(D−2)·(tr M² − (tr M)²/(D−1)) (PP P3D.1)
  - Gauss–Bonnet: 0
- Riem² picks up the four placements of R_yayb. Ric_ab ⊃ −M_ab and Ric_yy ⊃ −tr M.
- Machine-confirmed in D = 5 with all 10 entries of κ symbolic, κ_tv included, which closes the κ_tv = 0 scope [log GK0–GK5]:
  - GK0: R is affine in w = 1/ε.
  - GK0b: the w-part depends on κ only.
  - GK1–GK4: the four coefficients.
  - GK5: Gauss–Bonnet 0.
- **Request to PP:** regrade 3G from CONDITIONAL to PROVED (as implication). Until PP confirms, the ruled tally 12/3/2/1 stands. Proposed tally: 13/2/2/1 = 18 + 1.
- "Zero iff" statements additionally need P-Poinc (F-3).

## 3. F-2 — corrected premise sets for rows 10 and 15
**Row 10 (REFUTED as implication; grade as ruled).** "E₈ instantons cancel the δ² under odd G₄" is refuted, given:
- P-content: E₈ YM with positive trace, plus M5s.
- P-Israel.
- P-G and P-2der: G₄ is bounded, so G² is Z₂-even and bounded, with no δ.
- **P-Poinc:** [K] is real-diagonalisable (strict positivity; see F-3 / P7.5).
- **P-τ:** every charged plane object has τ > 0. This closes the charge-without-stress loophole that τ ≥ 0 left open.
- **n_R = 0:** −½ tr R² is excluded from the Bianchi charge as well as from the stress. The n_R ≠ 0 case is moved to row 10b.
- **L-GN** for non-diagonal walls (proved in §2, pending PP), or restriction to row-2 walls.
- **Q_plane ≠ 0** replaces "charge 9760". 9760 is an in-repo stated premise (PP aeb9ab13, MN2 branch-U normalisation) and is not adopted. The chain uses only Q_plane ≠ 0.

**Row 10b (CONDITIONAL, as ruled).** It now also absorbs the n_R ≠ 0 charge case.

**Row 15 (PROVED as implication; grade as ruled).** Premises: {P-HW, P-reg, P-Poinc, P-Israel, P-content, **P-τ**, **n_R = 0**, P-G, **L-GN**, **Q_plane ≠ 0**}. "Irreversible" means → ∞ as ε → 0 at fixed profile shape. Finite thickness is row 16.

This bears on the 11:30 question. It does **not** resolve or reopen the 9760 adoption-record conflict recorded in 9811de14, which is outside this erratum.

## 4. F-3 — row 7, item D3
- "Weyl² δ² = 0 iff S ∝ h" and "Ric² δ² = 0 iff S = 0" hold **only for real-diagonalisable [K] (P-Poinc)**.
- Counterexample (PP P7.5): a null stress M = σk^a k_b ≠ 0 with k null has tr M = tr M² = 0, so every δ² coefficient vanishes.
- The row-7 algebra ([K̃] = −κ²S̃, tr[K] = (κ²/9) tr S) is unaffected; PP verified it for generic non-diagonal [K].

## 5. F-4 — row 12 / §5 lead sentence, corrected
- **Corrected lead:** as an implication, gated by P-bulk, which is OPEN under the working assumption, the HW-native (Israel/boundary) matching onto the plane triggers no irreversible divergence in Ricci² (R_MNPQR^MNPQ or R_MNR^MN) or Weyl².
- **Added premise:** F bounded on the plane, so that the HW tr F² term is finite. Row 12's premises are now {P-HW, P-reg, P-Israel, P-2der, P-down, P-bulk, P-G, F bounded on the plane}.
- **Scope.** P-reg (bounded K) excludes zero-size instantons and plane-localized M5s, so V-down does not cover them. They belong to row 14(b).
- **OW 1108.** The MR2 item is **reduced to B-1 (row 14), not discharged.** P-bulk is not upgraded. Almost all of row 12's content is P-bulk, and row 4's Z₂-parity results are not load-bearing for it.

## 6. F-5 — §6 items 5 and 6, as implications
- **Item 5 (rewritten).** As an implication of {P-content, P-Israel, P-Poinc, P-τ, Q_plane ≠ 0}, the plane's wall stress is not pure trace and is non-zero. So the plane is non-umbilic, and Weyl² δ² > 0. Row 9 alone gives only S̃ = 0 ⇒ S = 0. The BPS 1:1:0 value (128/15)κ⁴τ² is an instance.
- **Item 6 (rewritten; QC N2 folded).** Odd G₄ with bounded tangent legs forces only the **form** [G] = 2G and the **form** of the balance N_M5 + n_inst = Q_plane. The integer 9760 is an in-repo stated premise (PP aeb9ab13, MN2 branch-U normalisation) and is not adopted. The earlier wording "(filed, exact)" is withdrawn.
- **Item 1** needs L-GN in general D, which is supplied in §2 pending PP.

## 7. Non-priority fixes
- **N1.** The author is Math Research 2. This file's author line is "by MR2". The parent's title wording is a nit; the parent is not edited.
- **N3.** PP 1953 = 077e417db7f24ece269d7dcde21bc89e260bbe1102d985c63ab60aa94813c23b = sidecar. PP Y16 audit = 149be02a794917d92f36c7a2383bbb4eb74623bb4f7b57dd111ad09f73ba7293 = sidecar.
- **Row 3.** Disclosed: the parent's 4D instance used one background jet at u = ½ with κ_tv = 0. Superseded in scope by §2 (general jets; general κ in D = 5), pending PP.
- **Row 9.** The implicit premise is named: **each M5 worldvolume contains the time direction t**. The transverse null vector k = t + e_⊥ then gives S(k,k) = τ.
- **C2.** The parent hard-coded I2 = 2 and printed the Cauchy–Schwarz bound without checking it. Both are now checked [log C2a–C2d]:
  - ∫sech² = 2 and ∫sech⁴ = 4/3.
  - Box-mollifier equality gives 1/(2Lε).
  - A normalised (1 − s²/(Lε)²)² bump gives 5/(7Lε) ≥ 1/(2Lε).
- **Modes.** The parent .md and QC .md are mode 644 (convention). Frozen scripts and logs are 444. Nothing is chmod-ed by this erratum.
- **QC note mtime.** The QC note's mtime (11:25:54.5495) is 2.7 ms after its sidecar's (11:25:54.5468). I cannot tell from this session how that mtime was set. Its content matches the sidecar hash 66f04088…, so there was no content change after the sidecar was written.

## 8. Tallies
- **Ruled by PP (stands):** 12 PROVED / 3 CONDITIONAL (10b, 13, 3G) / 2 OPEN (14, 16) / 1 REFUTED (10) = 18 + 1 bookkeeping.
- **Proposed, pending PP confirmation of §2:** 13 / 2 / 2 / 1 = 18 + 1 (3G → PROVED as implication).
- **Folded:** F-1, F-2, F-3, F-4, F-5; N1, N3; the row-3 disclosure; the row-9 premise; C2; modes; the QC mtime note.
- Junction UNSOLVED, carried and not counted.

Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 **MATCH** (checked before writing; re-checked after). Nothing adopted. No CERT. Nothing sent. Junction UNSOLVED.
