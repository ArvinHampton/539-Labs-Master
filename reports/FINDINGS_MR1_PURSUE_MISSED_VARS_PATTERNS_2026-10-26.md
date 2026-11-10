# FINDINGS — MR1 Pursue missed variables / patterns / correlations (residual-C) — 2026-10-26 ~17:45 CDT (America/Chicago)
Executor: Math Research 1 · Soft-SF Write-only · tip_touched NO · Kerr BLOCKED · eight-only · no Eigen contact

ACK: policy ADD (free pursue, no pre-approval; proof OR named gap; invent ban LIFTED; Cat-A gate DROPPED) + DIRECT acknowledged.

## STATUS
**PARTIAL.** 5 pursuits. PROVEN: P1 (q^18 = classical Sturm index bound for Γ₀(49), wt 4), P2 (Atkin–Lehner set at level 49 = {1, W₄₉}; "W₇" is not an AL involution — ν-cell↔AL-sign correlation VACUOUS), P3-existence (off-mesh ν uniquely determined by on-mesh data *inside the 89-dim module*), P5 (parity/P-even projector from ρ̄(−I)). UNPROVEN+gap: P3 values/identification, P4 coefficient field (ζ₄₉ vs CF(980)), L3 single-cusp lemma. No CSV edited, no cell filled, no mesh N>18 asserted.

## Authority (live sha256, verified 2026-10-26 ~17:40 CDT)
| Item | sha256 | Result |
|---|---|---|
| OW free-pursue | 687b27f5ba8fab6a847563069f66bbb4b9511cf36d14df3e7143a83db335eecd | OK |
| ASSIGN eight pursue | d763ac36900df1f0bb55e0ce8d7f72e96aa29e1b1e44af7269ce0d892dc73bba | OK |
| Policy invent→proof | ef6da7e7d6d97e115cabf7fa661fbc262180cdde9de39b41a123da2347076192 | OK |
| SCOPE EIGHT | 203676c9e6118a5e19e843182940b1f94db873c7579510222f92c298eeb86187 | OK |
| Tip residual-c-field-WRITTEN_PREMISES_DRAFT.md (pre=end) | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | OK, untouched |
| Prior FINDINGS_MR1_FILLFIRST_DEEPEN_ONMESH_GAPS (background) | live **dac489f2fedf0cbf109fbd22a74593740dce13ad406983061c0fbb136e2f87b9** (sidecar agrees) | **MISMATCH vs brief 66b1bc0a…** — cited by live sha; not rewritten |
| Sturm Prop 1.1 bound | b3172d39… | GAP-ABSENT (cite) |
| ζ₄₉ CRT | 92e15d32703a1ec8… | GAP (cite) |
| PR2 Rank25 W₇ cut | 4bd66bc17cc9855e… | MATCH (cite) |

## (a) What pursuing
1. **P1 — Mesh N=18 ↔ Sturm index bound** (variable: [SL₂ℤ:Γ₀(49)]).
2. **P2 — ν-cell ↔ Atkin–Lehner/Fricke sign correlation at level 49.**
3. **P3 — Slash/truncation uniqueness ⇒ determination of off-mesh ν (21,25,29,81,109,121).**
4. **P4 — Coefficient field for N6 exact lift: ζ₄₉ vs CF(140)·CF(49) = CF(980).**
5. **P5 — P-even (Ramanujan–Hampton) selection via ρ̄(−I) on V₄₂.**
(Dropped as weak: mock vs quantum-modular cusp mismatch — no corpus traction, no on-disk shadow/Eichler data; UNPROVEN, gap = no mock completion written for any residual-C object.)

## (b) First findings
**P1 — PROOF.** [SL₂ℤ:Γ₀(N)] = N∏_{p|N}(1+1/p); N=49 ⇒ 49·8/7 = 56. Classical Sturm: f ∈ M_k(Γ₀(N)) with a_n=0 for n ≤ k·m/12 ⇒ f=0. k=4: 4·56/12 = 18.67, so coefficients n=0..18 suffice. **Pattern: the TORD mesh N=18 coincides exactly with the scalar Sturm bound for weight 4 on Γ₀(49).** Relation: explains why q^18 injectivity on dim 89 (Step3 MATCH, 88911d8c…) holds naturally; supplies a candidate route around L3 (single-cusp lemma) **only for scalar components**. UNPROVEN gap: applicability to vector-valued ρ̄|cusp6 components (need each component to be a scalar form on a congruence group of index ≤ 56 — false in general, Ind type is 336-dim; Prop 1.1 B=1/3 route remains conditional on L1–L3 per b3172d39…).

**P2 — PROOF (negative).** Atkin–Lehner involutions W_Q of Γ₀(N) exist for Hall divisors Q‖N (gcd(Q,N/Q)=1). For N=49 = 7²: Q ∈ {1,49}; Q=7 fails since gcd(7,7)=7. So the only AL/Fricke involution is W₄₉. Hence "W₇" is not an Atkin–Lehner element of Γ₀(49)'s normalizer of that form; together with Path C (tip L247/L309: W₇ ∉ G, ρ(W₇) CLOSED ABSENT on V₄₂) there is **no W₇ eigenvalue attached to any FILLED-MODP ν-cell: correlation VACUOUS**. W₄₉-sign correlation: UNPROVEN, gap = no Written ρ̄(W₄₉) on V₄₂ (DMZ W₄₉ scalar wall ruled out per PF-2 e990cb37…); not reopened. Consistent with PR2 Rank25 (4bd66bc1…).

**P3 — PROOF (existence) / UNPROVEN (values).** Lemma: let V be finite-dim, T: V→C^m linear injective (truncation at q^18). If f ∈ V and T(f) known, f is unique, hence every Fourier coefficient a_ν(f), ν>18, is a fixed linear functional of T(f). Proof: f=T⁻¹(T f) on im T. Step3 MATCH gives injectivity on the 89-dim module. ⇒ **if** the off-mesh cells ν∈{21,25,29,81,109,121} are Fourier coefficients of one element of that module, they are determined by on-mesh data. Gaps: (G3a) Written identification ν-cell ↔ coefficient of a single module element (TORD map EIGEN-TE-RHOBAR-N36-TORD-CSV-MAP is for N36 on-mesh only); (G3b) explicit basis (char-0 ABSENT; mod-p only, so determination holds mod p only where reduction stays injective — unproven per prime). No values computed; cells stay OPEN-OFF-MESH.

**P4 — PROOF (field arithmetic) / UNPROVEN (containment).** [Q(ζ₄₉):Q]=φ(49)=42. Card1D: ρ̄|cusp6 ≅ ρ₄⊗ρ₅⊗ρ₇ over CF(140). Q(ζ₁₄₀)∩Q(ζ₄₉)=Q(ζ_{gcd})=Q(ζ₇); compositum Q(ζ₉₈₀), degree φ(980)=2·4·42=336. Primes p≡1 (mod 980) split completely in Q(ζ₉₈₀), so mod-p data at such p embeds; CRT + rational reconstruction over enough such p recovers Z[ζ₉₈₀] coefficients given a height bound. **Finding: a ζ₄₉-only CRT (92e15d32…) may be insufficient — the natural field is CF(980) unless the ν-cells are proven to lie in Q(ζ₄₉).** Gaps: (G4a) containment in Q(ζ₄₉) (Galois-invariance under Gal(Q(ζ₉₈₀)/Q(ζ₄₉)) unproven); (G4b) coefficient height bound; (G4c) whether existing mod-p primes are ≡1 mod 980.

**P5 — PROOF (conditional on Cat B operative premise).** With F(γτ)=(cτ+d)^k ρ̄(γ)F(τ) and γ=−I (acts trivially on H, cτ+d=−1): F = (−1)^k ρ̄(−I)F. k=4 ⇒ F ∈ ker(ρ̄(−I)−1). Under operative ρ̄(−I)=ρ(S)² (tip L231, R19 77643e84…), nonzero forms lie in the +1 eigenspace of ρ(S)²: the P-even projector (1+ρ(S)²)/2 kills the odd part identically. Consequence: any ν-cell supported on the ρ(S)²=−1 part is forced 0 (provable vanishing source). Gap: eigenspace dims of ρ(S)² on V₄₂ not Written; ρ(−I)=Id NOT confirmed (F3 CLOSED) — no claim outside V₄₂.

## Posture
Soft-SF Write-only. tip_pre = tip_end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91; tip_touched NO; no fold. Kerr/Path4 C2–C3 BLOCKED. Eight-only; no Eigen/Ops/out-of-set contact (Eigen files cite-only). No CSV edits; no mesh N>18; no invented coefficients. Soft SF → Auditor.

## Rec A
Owner Write (in-set, MR1/Auditor) to settle P4/G4a: declare the exact-lift coefficient field (Q(ζ₄₉) vs CF(980)) for the 7 FILLED-MODP cells and require CRT primes ≡1 mod 980 — prerequisite for both N6 exact lift and P3 off-mesh determination.
