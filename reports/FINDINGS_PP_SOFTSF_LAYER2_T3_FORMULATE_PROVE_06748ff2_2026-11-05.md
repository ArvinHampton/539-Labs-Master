# FINDINGS — PP Soft SF — Layer2 & T3 formulate-and-prove under OW 06748ff2… — 2026-11-05
REPORTS ONLY. No CERT. invent HOLD respected (definitions labeled, not results). tip untouched.
Authority: OW `06748ff29e8b5e103833c5dec0712443a255d4e26990ea53acaa8793306fe9e2` (MATCH; names PP; authorizes formulate Layer2/T3 hypotheses under D1/S_eff locks, clearly labeling proposed definitions and conditional conclusions; does NOT authorize fabricated proofs, restoring purged physical mappings, tip edits, CERT, publishing or spending).
D₁/S_eff lock: OW `96f8d42e80c1975b4390fed950a4fb4b420088e6b19b2cbef8a44bebd28ff2ba` (MATCH). Locked attach `a71f388efa35312556530d478a75fd9e54cc92a70a807d4ddda21c2b84b7543d`.
Prior gap (IDLE both): FINDINGS_PP_SOFTSF_LAYER2_T3_PROOF_RESUME_GAP_a0c2ed5a_2026-11-05.md.
Prior ABSENT Layer2 transfer: FINDINGS_LOCAL_D1_NORM_LAYER2_TRANSFER_2026-10-26.md; OWNER_CARD_LOCAL_D1_NORM_LAYER2_ABSENT_NEXT_2026-10-26.md.
RTA v16: Thm 41.10, Prop 41.11, Prop 41.12, Prop 42.6, Remark 42.7 (on-disk PDF reports/papers/RTA_FOUNDATION_BOUND/RTA_FOUNDATION_BOUND_v16.pdf).
tip Soft SF BEFORE: `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` sha `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` MATCH.
tip Soft SF AFTER: same sha MATCH (re-verified post-write). tip_touched NO.

---

## 0. Scope and honesty gate

Under OW 06748ff2… PP may choose well-typed targets and attempt proofs. PP may not invent physical/Kronecker maps (PURGED by lock 96f8d42e… / Prop 41.13(ii) / Remark 42.7). The old "D₁-norm → Kerr area" Layer2 transfer is **ill-typed** under locked D₁ (D₁ is a rank-1 class in H²(F), not a norm; Thm 41.10(ii) forbids temporal/schedule/metric arguments). This Soft SF therefore chooses **algebraic** Layer2 and **static-budget** T3 targets only.

---

## 1. Chosen targets (one line each)

- **Layer2 target (PP-CHOSEN):** Under locked D₁ / Thm 41.10, prove that any Cat-A Layer2 claim derived from D₁ is a ℚ-linear functional of the unique line ℚ·[s_αδ] ⊂ H²(F), uniquely determined up to nonzero scalar, and that any purported D₁-norm / Kerr-area transfer is ill-typed; no physical map is constructed.
- **T3 target (PP-CHOSEN):** Under S_eff (T₃=539 static cell/hash budget, Prop 41.11) and T3_ref of Prop 42.6, prove the preimage-cardinality theorem (|T3_ref⁻¹(y)| ∈ {1,2} for all y∈ℕ, never 3) and the packaging identities 539=⌊4859/9⌋=18+521=3·68+5·67; record Haar-on-ℤ₃ as already proved in Prop 42.6(iii) (re-stated, not re-invented).

---

## 2. (a) Chosen definitions / hypotheses — PP-CHOSEN DEFINITION labels

### PP-CHOSEN DEFINITION L2-D1. Layer2_D1_classifier
Let F be the thin residual form complex of Thm 41.10 (generators {1,α,ω₂,μ,f,δf}, product differential D, residual relations ω₂=d_Q α and μ=−B′ ω₂ on ordered triples, brutal truncation F³:=0). Write s_αδ := α⊗δf. By the locked computation (Thm 41.10 / Residual_Product_Cohomology / Flag 1 CLOSED in OW 96f8d42e…),
\[
H^0(F)\cong\mathbb{Q},\qquad H^1(F)=0,\qquad H^2(F)\cong\mathbb{Q}\cdot[s_{\alpha\delta}],
\]
and consequently the formality equivalence \(F\simeq\mathbb{Q}[0]\oplus\mathbb{Q}[-2]\) in D(ℚ).

**PP-CHOSEN DEFINITION.** Define the Layer2 classifier associated to locked D₁ to be any ℚ-linear functional
\[
D_1:H^2(F)\longrightarrow\mathbb{Q}
\]
that isolates the line ℚ·[s_αδ] (equivalently: the projection onto the degree-2 summand of the formal model, composed with a fixed identification ℚ·[s_αδ]≅ℚ). Domain restriction: D₁ acts only on the nine charge sectors of X_×=K₉×P_{B′} and takes **no** argument from any temporal variable, execution schedule, or metric normalisation (Thm 41.10(ii); OW lock §1).

**Hypothesis L2-H1 (locked, not invented).** H²(F)≅ℚ·[s_αδ] (rank 1 over ℚ). Source: Thm 41.10; OW 96f8d42e… Flag 1 CLOSED; Residual_Product_Cohomology boxed class.

**Hypothesis L2-H2 (locked, not invented).** No algebraic datum of D₁ is shared with any resonant counter set (Thm 41.10(iii); Prop 41.12).

**Hypothesis L2-H3 (negative / purged).** No Kronecker / four-forces / SU(3) / continuum physical mapping is part of Category A (Prop 41.13(ii); OW lock §4; Remark 42.7). Restoring such a map is out of scope.

### PP-CHOSEN DEFINITION T3-REF. T3_ref under S_eff
**PP-CHOSEN DEFINITION.** Adopt the ternary map of Prop 42.6 / RPP formal statement:
\[
T3_{\mathrm{ref}}:\mathbb{N}\to\mathbb{N},\qquad
T3_{\mathrm{ref}}(3k)=k,\quad
T3_{\mathrm{ref}}(3k+1)=4k+2,\quad
T3_{\mathrm{ref}}(3k+2)=2k+1
\]
(with ℕ including 0; T3_ref(0)=0). Under S_eff (Prop 41.11 / OW lock §2), the integer **539** is a **static cell capacity / arithmetic hash budget**, not a stopping time, not a convergence rate, and not a runtime execution length forced by residual cohomology. The resonant schedule of length 539 (when used) is an external constant-time override, disjoint from Residual₅₃₉ (Prop 41.11(iv), Prop 41.12).

**Hypothesis T3-H1 (locked).** T₃=539 is static budget under S_eff. Source: Prop 41.11; OW 96f8d42e….

**Hypothesis T3-H2 (locked arithmetic).** Packaging identities of Prop 42.6 / Remark 42.7: 539=⌊4859/9⌋=18+521 and the near-equal partition {68³,67⁵}.

**Hypothesis T3-H3 (negative / purged).** No written map from T3_ref / O_res / packaging identities to g_s, C, V₃₅, Kerr area, or stress-energy (Remark 42.7; OW lock §4). A "ternary stress-energy" reading is out of scope.

---

## 3. (b) Proved results — Tier P (complete proofs)

### Theorem PP-L2-1 (Uniqueness of D₁ up to scalar). Tier P
**Statement.** Under L2-H1, any two Layer2 classifiers D₁, D₁′ as in PP-CHOSEN DEFINITION L2-D1 differ by a nonzero rational scalar. Equivalently, the projectivized classifier ℙ(D₁) ∈ ℙ(Hom_ℚ(H²(F),ℚ)) is a single point.

**Proof.** By L2-H1, dim_ℚ H²(F)=1, with basis {[s_αδ]}. Then Hom_ℚ(H²(F),ℚ) ≅ ℚ as a 1-dimensional ℚ-vector space. Any nonzero linear functional is a nonzero multiple of any other. A classifier that "isolates the line ℚ·[s_αδ]" is nonzero on [s_αδ], hence nonzero, hence unique up to ℚˣ. Formality F≃ℚ[0]⊕ℚ[−2] has the same H², so the same uniqueness holds for the formal-model projection. ∎

**Status.** Proved from locked rank-1. No physical content. No invent.

### Theorem PP-L2-2 (Ill-typedness of D₁-norm / Kerr-area Layer2 transfer). Tier P
**Statement.** Let Φ be any purported Layer2 transfer of the form "the D₁-norm of ĝ_s (or of a Fourier index n) equals / maps to the Kerr area A (O1–O4 or SUSY-extremal)." Under locked D₁ (L2-D1, L2-H1, Thm 41.10(ii)) and L2-H3, Φ is **ill-typed**: it is not a well-formed Cat-A statement about D₁.

**Proof.** Three independent typing failures, each sufficient:
1. **D₁ is not a norm.** By PP-CHOSEN DEFINITION L2-D1 / Thm 41.10(i), D₁ is a ℚ-linear functional on H²(F). A norm on a ℚ-line (or on a residual-series coefficient space) would require a metric or absolute-value structure. Thm 41.10(ii) forbids metric normalisation as an argument of D₁. Hence "D₁-norm" has no referent under the lock.
2. **No temporal / schedule / metric argument.** Any map whose codomain is an astrophysical or SUSY horizon area A (a metric geometric quantity) necessarily feeds metric data into the claimed transfer. Thm 41.10(ii) excludes metric arguments from D₁. Hence a D₁→A transfer cannot be a Cat-A consequence of D₁.
3. **Physical maps purged.** Even granting a purely numerical coincidence n↔A, L2-H3 / Remark 42.7 / OW lock §4 state that no written Category A map from residual packaging / D₁ data to physical Kerr (or four-forces / Kronecker) exists; restoring one is invent. Prior FINDINGS (Local Layer2 transfer, 2026-10-26) already recorded links (a) n↔charge index and (b) SUSY area↔Kerr area as ABSENT.

Therefore Φ is ill-typed under the lock. This is a negative typing theorem, not a positive physical claim. ∎

**Status.** Proved. Does **not** construct a replacement Layer2 physical transfer. Thm 41.10(iv) still stands: "Layer 2 structure beyond the definition of D₁ is not constructed from D₁ in this paper."

### Theorem PP-L2-3 (Formality consequence for Layer2). Tier P
**Statement.** Under L2-H1 and formality F≃ℚ[0]⊕ℚ[−2], every Cat-A cohomology invariant of F that can enter a Layer2 classifier lives in H⁰(F)≅ℚ or H²(F)≅ℚ·[s_αδ]. In particular H¹(F)=0 contributes no Layer2 data, and no degree ≥3 data exists in the thin truncation F³=0.

**Proof.** Formality says F is quasi-isomorphic to its cohomology placed in degrees 0 and 2. The thin truncation kills F^{≥3}. H¹(F)=0 by L2-H1. Hence the only possible Cat-A cohomological inputs to a Layer2 classifier built from F are the two lines H⁰ and H²; D₁ as defined uses only H². ∎

**Status.** Proved. Purely algebraic.

---

### Theorem PP-T3-1 (Preimage cardinality of T3_ref). Tier P
**Statement.** Let T3_ref be as in PP-CHOSEN DEFINITION T3-REF. For every y∈ℕ,
\[
\bigl|T3_{\mathrm{ref}}^{-1}(\{y\})\bigr|\in\{1,2\},
\]
and the cardinality is never 3. Explicitly, the preimages are:
- always \(x_0=3y\) (residue-0 branch);
- additionally \(x_1=3k+1\) with \(k=(y-2)/4\), iff \(y\equiv 2\pmod{4}\) and \(k\in\mathbb{N}\);
- additionally \(x_2=3k+2\) with \(k=(y-1)/2\), iff \(y\) is odd and \(k\in\mathbb{N}\).

The residue-1 and residue-2 cases are mutually exclusive (y even vs odd). Moreover, for y≥1: |T3_ref⁻¹(y)|=1 iff v₂(y)≥2, and =2 otherwise. (Here v₂ is the 2-adic valuation; for y=0 the unique preimage is 0.)

**Proof.**
Write an arbitrary x∈ℕ as x=3k+r with r∈{0,1,2} and k∈ℕ.
- If r=0: T3_ref(x)=k. Setting equal to y gives k=y, so x=3y. One candidate.
- If r=1: T3_ref(x)=4k+2. Setting 4k+2=y gives y−2=4k, so y≡2 (mod 4) and k=(y−2)/4≥0. At most one candidate.
- If r=2: T3_ref(x)=2k+1. Setting 2k+1=y gives y odd and k=(y−1)/2≥0. At most one candidate.

The conditions "y≡2 (mod 4)" and "y odd" are incompatible (odd ⇒ y≢0,2 mod 4 in the even sense; specifically odd ⇒ y≢2 mod 4). Hence at most one of the r=1 and r=2 candidates exists. Together with the always-present r=0 candidate, the preimage size is 1 or 2, never 3.

For the v₂ refinement (y≥1): 
- If y odd: residue-2 candidate exists; residue-1 does not; with residue-0, size=2. And v₂(y)=0<2.
- If y≡2 (mod 4): then v₂(y)=1<2; residue-1 candidate exists; residue-2 does not; size=2.
- If v₂(y)≥2: then y≡0 (mod 4), so y even and y≢2 (mod 4); neither residue-1 nor residue-2 candidate exists; size=1.

For y=0: T3_ref(0)=0, and the formulas give only x=0 (k=0 in residue 0; residue 1 needs y≡2 mod 4, false; residue 2 needs y odd, false). ∎

**Numeric CONFIRM (not a substitute for the proof):** exhaustive check for all y∈{0,…,4999} found max preimage count 2, zero mismatches against the closed-form preimage list, and zero mismatches against the v₂ classification (Python, this Soft SF). Counts: 1250 values with 1 preimage, 3750 with 2 (among y=0..4999).

**Status.** Proved. Elementary number theory. Consistent with prior PP audit note on OL Option B (FINDINGS_PP_SOFTSF_AUDIT_539_OPS_HQH_CRIT3…): odd outputs from branch 2, outputs ≡2 mod 4 from branch 1, disjoint; every y also has preimage 3y.

### Theorem PP-T3-2 (Packaging arithmetic identities). Tier P
**Statement.** The following equalities of integers hold:
\[
539=\Bigl\lfloor\frac{4859}{9}\Bigr\rfloor=18+521=3\cdot 68+5\cdot 67=7^2\cdot 11.
\]
Moreover, if 539=a₁+⋯+a₈ with positive integers and max a_i − min a_i ≤ 1, then {a_i}={68,68,68,67,67,67,67,67} (Prop 42.6(i), re-proved below).

**Proof.**
- 4859=9·539+8, so ⌊4859/9⌋=539.
- 18+521=539.
- 3·68+5·67=204+335=539.
- 7²·11=49·11=539.

For the near-equal 8-partition: let q=min a_i and b=#{i: a_i=q+1}. Then 539=8q+b with 0≤b≤7. If b=8 then 8|539, but 539=7²·11 is not divisible by 2, contradiction. Solving 539=8q+b in the stated range gives q=67, b=3. Hence three parts equal 68 and five equal 67. ∎

**Status.** Proved. Matches Prop 42.6(i) and Remark 42.7 packaging list. Under S_eff these are **cell-count / schedule-split integers**, not dynamical parameters (Prop 41.11(i), Prop 41.12).

### Theorem PP-T3-3 (Static-budget reading of 539 under S_eff — definitional Tier P). Tier P
**Statement.** Under T3-H1 / Prop 41.11, the integer 539 appearing in PP-T3-2 is the static cell capacity (Residual₅₃₉ count) and, separately, may be used as a forced iteration count (Resonant₅₃₉). Equality of the two integer values is not a structure map of chain complexes, graded vector spaces, or sets (Prop 41.12). In particular, Theorems PP-T3-1 and PP-T3-2 do not imply that residual cohomology forces a 539-step dynamical stopping time.

**Proof.** Prop 41.11(i)–(iv) and Prop 41.12 are definitional constraints already Owner-locked (OW 96f8d42e…). PP-T3-1 concerns the set-theoretic map T3_ref:ℕ→ℕ; PP-T3-2 concerns integer identities. Neither constructs a chain map C^•(X_×)→ℤ/539 or a stopping-time structure. Thm 41.10(iii) and Prop 41.11(iv) forbid sharing D₁ algebraic data with resonant counters and keep Residual/Resonant projections disjoint. ∎

**Status.** Proved as a reading of the lock + the two arithmetic theorems. No dynamics invented.

---

## 4. (c) Conditional results

### Conditional C-T3-Haar (Prop 42.6(iii), accepted as written, not re-proved from scratch here)
**Statement (RTA v16 Prop 42.6(iii)).** Extended to ℤ₃, T3_ref preserves Haar measure μ, and the itinerary map n ↦ (T3_ref^j(n) mod 3)_{j≥0} is a homeomorphism ℤ₃ → {0,1,2}^ℕ conjugating T3_ref to the shift.

**Condition.** Accept the RTA v16 written proof of Prop 42.6(iii): each branch k↦k, 4k+2, 2k+1 is an affine bijection of ℤ₃ with unit linear coefficient; k↦3k+r maps onto r+3ℤ₃ scaling Haar by 1/3; hence μ(T3_ref⁻¹ B)=Σ_r μ(B)/3=μ(B); itinerary classes mod 3^j give the homeomorphism.

**PP status.** CONDITIONAL on the on-disk RTA proof (not independently re-derived in full 3-adic detail in this Soft SF). The elementary preimage theorem PP-T3-1 is the ℕ-shadow of the same branch analysis and is proved above unconditionally. PP does **not** claim a new Haar proof beyond Prop 42.6(iii).

### Conditional C-L2-positive-transfer
**Statement.** "There exists a well-typed Cat-A Layer2 transfer beyond the rank-1 classifier D₁ itself (e.g., a cite-grounded map from [s_αδ] to a residual-series invariant that is not a purged physical quantity)."

**Condition.** Would require either (i) an Owner-Written redefine of the Layer2 target past Thm 41.10(iv), or (ii) a new in-lane cite supplying a non-purged algebraic map. Neither is present.

**PP status.** CONDITIONAL / OPEN. PP-L2-1..3 do not discharge it. Prior Path4 C1–C3 remain BLOCKED for physical load; under the locked D₁ the old physical load is additionally ill-typed (PP-L2-2).

### Conditional C-T3-stress-energy (REJECTED as target)
A "ternary stress-energy" conditional under S_eff would reintroduce a purged physical mapping (prior gap FINDINGS a0c2ed5a…; L2-H3 / T3-H3). **Not formulated. Not proved. Out of scope.**

---

## 5. (d) Remaining gaps

1. **Positive Layer2 structure beyond D₁ definition.** Thm 41.10(iv) records that RTA does not construct Layer2 from D₁ beyond the classifier definition. PP-L2-1..3 prove uniqueness / ill-typedness / formality consequences; they do **not** supply a new positive Layer2 transfer. Gap: OPEN, pending Owner redefine or new in-lane cite (not invent).
2. **Physical / Kerr / n↔A transfer.** Still ABSENT (prior Local FINDINGS; PP-L2-2 makes it ill-typed under locked D₁). Links (a) and (b) of the 2026-10-26 ABSENT card remain missing. Kronecker/physical maps stay PURGED. Gap: OPEN by design of the lock; do not invent.
3. **Path4 C1–C3.** Remain BLOCKED for physical load. Scoped-C1 on Layer-1 SUSY-only ID was never Owner-chosen as operative for a new transfer under locked D₁.
4. **Haar-on-ℤ₃ independent writeup.** Accepted conditionally from Prop 42.6(iii); full 3-adic re-proof not duplicated here. Gap: minor / documentary only.
5. **No global Ω≡0 (mod 539).** Prop 41.11(ii) stands; PP did not attempt to prove or disprove local remainder cancellation. Gap: definitional lock, not a theorem gap.
6. **Collatz-type total orbit claim for T3_ref.** Whether every ℕ-orbit reaches {0,1,2}-cycle is explicitly not claimed (RPP formal statement §1.4 item 6). Gap: OPEN, Collatz-type; out of scope for this Soft SF.

---

## 6. Explicit non-claims

- No CERT. No tip edit/fold. No STREAM edit.
- No fabricated proof. Definitions labeled PP-CHOSEN DEFINITION; proved results separated; conditional results separated; gaps listed.
- No restoration of purged Kronecker / four-forces / SU(3) / continuum / Kerr / stress-energy maps.
- No claim that 539-as-seconds is a Cat-A prediction (seconds↔cell-capacity link not written; cf. DF Tier E hygiene).
- invent HOLD respected: chosen definitions are not results; PP-L2-1..3 and PP-T3-1..3 are theorems about locked objects, not new physical inventions.
- Thm 41.10(iv) stands: Layer2 beyond D₁ definition is not constructed here as a positive transfer.

---

## 7. Verdict

| Item | Prior (a0c2ed5a gap) | This Soft SF |
|------|---------------------|--------------|
| Layer2 | IDLE pending Owner-Written target | **STARTED+partially RESOLVED:** PP chose well-typed algebraic target; proved PP-L2-1 (uniqueness), PP-L2-2 (ill-typedness of D₁-norm→Kerr), PP-L2-3 (formality). Positive physical Layer2 transfer remains ABSENT/ill-typed. |
| T3 | IDLE pending Owner-Written conditional | **STARTED+partially RESOLVED:** PP chose preimage+packaging under S_eff; proved PP-T3-1 (preimage 1-or-2), PP-T3-2 (packaging identities), PP-T3-3 (static-budget reading). Haar conditional on Prop 42.6(iii). Stress-energy rejected. |

Soft SF → Auditor Write-only MATCH, then Keeper.
