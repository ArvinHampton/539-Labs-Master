# DERIVE EH FIELD VARIABLES — 2026-10-25 (America/Chicago)

**OWNER JOB (supersedes PURSUE_THREE_NEEDS).** Invent-ban is HELD. **residual-C NOT edited**: draft sha256 ea85cbbc239d2e050e2b639908ae70dc850090270f08081662e26606036a7feb is unchanged.
Needs (2) and (3) are OUT OF SCOPE here. No d=2, k=−2 or ρ was inserted anywhere. Context: NL FINDINGS 4f84ffa282061a36ba9af3bd52842757d188b0960d872a7253b4a3f15ab08469.

## Sources (sha256 checked with sha256sum this run)
| ID | Path | sha256 |
|---|---|---|
| E1 | quantum-comp/nonlocal/Einstein_Hampton_Equation_Rewrite_Appendix_2026-09-28.txt (EH, Zenodo 23010998 extract) | 08b8541a1b40e16961984833915437aa4a96b680fe1404ad3e722191308ede39 |
| LN | /tmp/repo539/lean/EinsteinHamptonCurvature.lean (canonical; 0 `sorry`) | 53f9a4a81c3b05a3e3eb5cedf396a67ec4e6ba3bee0485e020d95f6c4d5b7aa6 |
| LN' | /tmp/repo539/docs/S2-11DM2ET-X-Axiomatic-Book/Einstein-Hampton-2026-09-2{8,9}/EinsteinHamptonCurvature.lean (older copy, differs) | ef6e7ed35c78f46c9b1fda344a9e0965152b9e05787c77b0e251eedb82d7c9a5 |
| M9 | quantum-comp/maths/theorem-lemma-chain-9-maths.txt | 904104d26c0c029df9a9e39f7ef5235f4b3a2f7befb0349e7bdf0187a6df5a0a |
| R1 | quantum-comp/reports/self-audit/zenodo/RTA_v12.txt (Zenodo 23644022) | f837aa377f0d57d1822d5d3243509f4a4a8c77a3aeaec7bf55e885de12303bcb |

## What "establish a field" means here (E1 Written)
A field is a solution of (EH) G_MN = 8πG11·T(EH)_MN on the ansatz (EH-ds): ds² = e^{−2A(y)}η dx² + dy² + e^{2B} ĝ dz².
- B is constant.
- R̂_ab = κ_int ĝ_ab.
- T(EH) = T(G4) + T(M2) + T(m) + T(−) + T(PBH).
- G4 = G11/V7eff.
- There is no Λ11.

The required variables are therefore:
- metric data: A (giving k), B (giving K);
- coupling: G11 (giving ℓ₁₁);
- source data: the five stress pieces, with the four-form entering L7 as Φ;
- reduction data: warp and V7eff.

## Algebra re-checked this run (DERIVED)
- From (alg), 6k²−3K = −Φ/96 and 4k²+K = Φ/144:
  - multiply the second by 3 and add: 18k² = Φ/48 − Φ/96 = Φ/96, so **k² = Φ/1728**;
  - then K = Φ/144 − 4Φ/1728 = 8Φ/1728, so **K = 8k² = Φ/216**.
- This matches LN `L7_fibre_lock` and E1 App C SymPy ("K:Φ/216").
- On the lock: G_ext/g = 6k²−24k² = −18k² and G_fib/g = 10k²−16k² = −6k². This matches LN `L6_lock_Einstein_blocks`.

## Per-variable status
| Variable | Status | Result / quote | Source |
|---|---|---|---|
| A | **WRITTEN ANSATZ** (input, not derived) | A = ky is the hypothesis of L5. From it, A' = k and A'' = 0 are DERIVED (LN `deriv_A_of_lin`, `deriv2_A_of_lin`). L4 then gives R_μyνy = −k² g (L5). | E1, LN |
| k | **DERIVED given Φ** (L7, Lean-proved) | k² = Φ/1728. Numeric: kℓ₁₁ = 0.02531377 (EH-k). E1 §7 lists (EH-k) as "Derived … given N", with N = 4880 inserted. The N→Φ step is garbled in the extract and is NOT reproduced here. | E1, LN |
| K | **DERIVED** (L7, Lean-proved) | K = 8k² = Φ/216. K is the fibre curvature in warp units, κ_int e^{−2B}. | E1, LN |
| Φ | **NOT derived by L1–L7** (source input); expression OPEN | Φ is the RHS of (alg), i.e. the four-form block weight. E1 App D: "Next check that can move L7: four-form weights Tμν/g=−G²/96 vs Tab/g=−G²/288". The Φ↔G² identification is therefore Author-flagged as unchecked. **AUTHOR-PROPOSED:** Φ := 8πG11·G² (four-form), normalised so that (alg) holds. Owner must WRITE this. | E1 |
| ℓ₁₁ | **WRITTEN convention** (not derived) | "16π G11 = (2π)^8 ℓ11^9". ℓ₁₁ is the unit in which kℓ₁₁ and T₂ℓ₁₁³ are stated. | E1 |
| T(G4) four-form | **WRITTEN; flux integer inserted** | "N = 4880 on equatorial S4 of unit S6". E1 l.101: 4880 is Inserted. "Match wants N = 4870.45. Miss 9.55 units." | E1 |
| T(M2) | **WRITTEN numeric** | T₂ℓ₁₁³ = 0.02533030 (EH-T2). Enters via the valve "(Δσ')² ≥ T2 k*". Not derived from L1–L7. | E1 |
| T(m) visible matter | **WRITTEN placement, not derived** | Sources the Plus-U face (Isr+) [K−Kq]₀ = −8πG11(τ+q+T(m)+T(H)). L1–L7 do not touch it. | E1 |
| T(−) hidden plasma | **WRITTEN form; params inserted** | T(−) = (ρp+ρd)uu + pp(q+uu), with fu ≈ 3×10⁻⁴. Sources (Isr−) at y = b. | E1 |
| T(PBH) negative-PBH dust | **WRITTEN; param inserted** | "bulk dust, βPBH=0.181 input". | E1 |
| warp e^{−4A} | **DERIVED** (from L1 + EH-ds) | The 4D block is g_μν = e^{−2A}η_μν, so √−g₄ = e^{−4A} (= e^{−4ky} on the lock). Cross-check: E1 App D "Warp 0.45" and "kb≈0.80" give e^{−kb} = e^{−0.80} = 0.449. These are consistent, but b itself is not derived. | E1, LN L1 |
| 11D / V7eff volume | **ABSENT as formula** | E1 Written only "G4 = G11/V7eff". No expression for V7eff. **AUTHOR-PROPOSED:** V7eff = ∫₀ᵇ dy e^{−4A}·e^{6B}Vol(ĝ), using the standard warped reduction. Owner must WRITE the measure and b. Not adopted. | E1 |

## 9 Maths and RTA v12 contribution
- **M9:** contains no Einstein–Hampton, 1728, k, K or Φ content. The "Frobenius warp operator" hits (l.121, 885ff) are a name collision with the metric warp.
- **R1:** its only link is the programme reference "Bridge Series C of the author's S2-11DM2ET-X programme" (l.2372). It contains no 11D field variable.
- **Neither source derives any variable above.**

## Caveats
- LN (53f9…) and LN' (ef6e…) differ; only the canonical LN was inspected.
- LN states: "Not an 11D Riemann API … does not emit n_2, Gamma, G4, or J_feed".
- R = 28k² on the lock is Written in E1 and is not proved in LN.
- residual-C OPEN / Bridge PARTIAL / READY NO, all unchanged.

## What does NOT follow
- No Cat A claim for Φ, V7eff, N_flux or the face sources.
- Proved L7 does not fix Φ (and hence k) without an Author-Written Φ(N).
- Nothing here closes residual-C or feeds needs (2)/(3).
