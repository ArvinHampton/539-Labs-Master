# FINDINGS — MR1 Mesh N>18 + W₇/slash-uniqueness determination premise (Rec A AUTO CLOSED) — 2026-10-26
Executor: Math Research 1 · Soft-SF Write-only · tip_touched NO · mathematical proof standard (proof OR named gap) · Cat A invent: NONE

## 1. STATUS
**PARTIAL.** Part A: Written mesh extension WRITTEN; all 6 ν are ON-MESH-by-Write (definitional, PROOF of membership = the Write itself under OW 5a766b35…); all 6 coefficients remain OPEN (no determination proved). Part B: Determination Lemma D1 (linear-algebra, finite-dim) PROVED; its application to residual-C/ρ̄ on Γ₀(49) UNPROVEN — gaps G1 (char-0 injectivity of on-mesh truncation, N36 503-block not certified; N6 89-block MATCH only mod p / CF(49) holomorphy uncertified), G2 (ρ(W₇) does not exist on V₄₂ — R26 rank-9 sole intertwiner — so a W₇-slash uniqueness route is unavailable on the current carrier), G3 (Sturm L1–L3 single-cusp Γ₀(49) lemma GAP-ABSENT). No CSV edited. No coefficient invented. 7 FILLED-MODP exact cells HELD for in-set ζ₄₉ CRT CERT.

## 2. Authority (live sha256, verified 2026-10-26 ~17:40 CDT America/Chicago)
| Item | sha256 | Result |
|---|---|---|
| OW Rec A AUTO | 5a766b35a6342ca1c86f74bbd866990d3a98e6902e0aa50fcb0e6015615184ef | OK |
| ASSIGN | 0606c31c6de6b388b9648de9a4d1e723a5497670a9fe98ad1059f36a5e62fabb | OK |
| Source FINDINGS three-track | dac489f2fedf0cbf109fbd22a74593740dce13ad406983061c0fbb136e2f87b9 | OK |
| SCOPE EIGHT | 203676c9e6118a5e19e843182940b1f94db873c7579510222f92c298eeb86187 | OK |
| Policy invent→proof | ef6da7e7d6d97e115cabf7fa661fbc262180cdde9de39b41a123da2347076192 | OK |
| Free-pursue | 687b27f5ba8fab6a847563069f66bbb4b9511cf36d14df3e7143a83db335eecd | OK |
| Schedule CSV TE-SIMPSON-FILL-SCHEDULE_TORD_N18 (read-only) | d3f12c981ec72b901ae7e97b76ac4a70c9cdd356ddda2eb5a721453d656f56f9 | OK, unchanged |
| R36 W₇ FINDINGS (cite) | 98a09683d2036d570824ce62b165b94a9c3a31fa1e31fddc187a894bc765b1f5 | OK |
| RHO-W7 Author-Write (cite) | ad3829c6cca3e2790f742f4898289026e87880072d8aed5972219489ac9bb2ce | OK |
| Tip residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | tip_pre = tip_end; READ ONLY |

## 3. Part A — Written mesh premise (N>18)
**Premise M-ext (Written, this FINDINGS, under OW 5a766b35…):** The residual-C TORD schedule mesh, currently {ν : on_mesh_N18 = YES} in CSV d3f12c98…, is extended by exactly the six exponents
- N36 lane: ν ∈ {21, 25}
- N6 lane: ν ∈ {29, 81, 109, 121}
No other ν is added. Lane classification is taken verbatim from CSV d3f12c98… rows (family column), unchanged from source FINDINGS §5.

**Membership.** Mesh membership is a schedule convention, not a property of the form; under the OW it is established by this Write. Stamp: ON-MESH-by-Write = YES (PROOF: definitional, cite OW 5a766b35…). No classical Γ₀(49)/Fricke statement is needed or claimed for membership.

**Named gaps for the extended rows (why coefficients stay OPEN):**
- GA1 — row semantics: CSV columns simpson_weight / fill_tier (1-odd-w4, 2-even-w2, 3-endpoint) are defined only for the N≤18 Simpson mesh; no Owner Write defines weights/tier for ν>18 (nor whether the extended mesh is Simpson-composite at all; ν-gaps 21→25 and 29→81→109→121 are non-uniform). Weights left "–".
- GA2 — coefficient: membership does not determine the coefficient; the existing mod-p fills come from the q^18-truncated ν-row solve (rows csv 5e3c3155…), which has no rows for ν>18. Filling needs either a new row solve past q^18 (compute, not invent) or Part B determination.
- CSV NOT edited (no proved determination). Proposed future row form, for the Owner only: `N36,21,YES(Write-ext),?,?,OPEN-ON-MESH,OPEN` etc.

## 4. Part B — W₇ / slash-uniqueness determination premise
**Lemma D1 (PROVED).** Let K be a field, M a finite-dim K-space of formal q-expansions (vector-valued, components indexed by cusp/ν-lane), and π_S : M → K^S the restriction to a finite index set S of Fourier coefficients (the on-mesh data). If π_S is injective, then for every ν (on- or off-mesh) the coefficient functional c_ν : M → K factors uniquely as c_ν = λ_ν ∘ π_S with λ_ν linear on im π_S.
*Proof.* π_S injective ⇒ π_S : M → im π_S is an isomorphism; set λ_ν = c_ν ∘ (π_S)⁻¹ on im π_S. Uniqueness: two such λ agree on im π_S by construction. ∎
Corollary: off-mesh c_ν is *determined* (as a K-linear function of on-mesh data) whenever (i) the residual-C/ρ̄ object lies in a certified finite-dim space M over K, and (ii) π_S is injective over K. Note D1 gives determination, not a value; values still require the explicit on-mesh vector over K (char 0 for exact cells).

**Lemma D2 (route via slash/W₇, status UNPROVEN).** Intended: if f is fixed (up to sign ε) by a slash operator |W, then c_ν(f) relates to coefficients at the image cusp, enlarging S effectively. On disk:
- R26/R36 (98a09683…, ad3829c6…): dim Hom(ρ, ρ∘Ad W₇) = 1, sole intertwiner rank 9 < 42 ⇒ **no ρ(W₇) on V₄₂** (PROVED in corpus, numerical SVD 7.4e-14 gap, Auditor MATCH-with-SF). Hence a W₇-slash uniqueness identity on the current carrier cannot exist; D2 on V₄₂ is **refuted as a route**, not merely unproven.
- Part B of RHO-W7 (V₈₄ = Ind ρ, forced block swap) gives ρ̃(W₇) but requires tip P1 change 42→84 (tip fold — BANNED here). On V₈₄ the slash relation only exchanges the ρ and ρ∘Ad W₇ blocks; it pairs ∞ with cusp 0 and imposes no relation among ν within one block, so it does not reduce off-mesh ν to on-mesh ν without an additional eigen-condition. GAP G2.
- Normalization flag (for Auditor, not corrected here): corpus writes W₇ = (1/√7)[[0,−1],[49,0]]; det = 49, so the SL₂(ℝ)-normalized Fricke involution is (1/7)[[0,−1],[49,0]] = W₄₉. The element is the level-49 Fricke W₄₉ (no 7‖49 Atkin–Lehner W₇ exists since gcd(7,49/7)≠1). W² = −I conclusion unaffected.

**Application status of D1 to residual-C/ρ̄ on Γ₀(49):**
- N6 lane (89-block): Card1F Step3 (88911d8c…) MATCH dim 89 + q^18 injectivity — over F_p (p=1027606441) only; char-0 holomorphy at 8 cusps NOT CERTIFIED (Q89 exact-lift 40c2810d… PARTIAL). D1 over F_p ⇒ ν ∈ {29,81,109,121} are determined **mod p** by q^18 data, conditional on the F_p space being the reduction of the true space (gap G1). Values not computed here → OPEN.
- N36 lane (503-block): no on-disk injectivity CERT of q^18 truncation (fill rows nz pattern only). GAP G1 + G3 (Sturm L1–L3 single-cusp lemma GAP-ABSENT; Magnusson–Raum Prop 1.1 bound conditional).
- **Explicit:** this premise does NOT by itself fill the 7 FILLED-MODP exact cells; those wait for an in-set ζ₄₉ CRT CERT only.

## 5. Per-ν table
| ν | Lane | ON-MESH-by-Write? | Coeff status | Proof-or-gap |
|---|---|---|---|---|
| 21 | N36 | YES (OW 5a766b35…) | OPEN | Membership PROOF (definitional). Determination UNPROVEN: G1 (503-block q^18 injectivity uncertified), G3 (Sturm L1–L3), GA1/GA2 |
| 25 | N36 | YES | OPEN | same as ν=21 |
| 29 | N6 | YES | OPEN | D1 ⇒ determined mod p conditional on G1 (F_p→char-0 space identification); value not computed; char-0 needs CF(49) holomorphy + ζ₄₉ CRT |
| 81 | N6 | YES | OPEN | same as ν=29 |
| 109 | N6 | YES | OPEN | same as ν=29 |
| 121 | N6 | YES | OPEN | same as ν=29 |
Count: 6 ON-MESH-by-Write / 6 coefficient still gap (0 filled). W₇-slash route on V₄₂: refuted (G2).

## 6. Posture
Soft-SF Write-only. tip_pre = tip_end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, tip_touched NO, no tip fold. No CSV edits. No Eigen contact; Eigen FINDINGS cite-only. Kerr/Path4 BLOCKED stands. Eight-agent scope. No Cat A coefficient invented. 7 MODP exact HELD.

## 7. Rec A
Compute (not invent) the N6 89-block ν-rows past q^18 to q^121 mod p=1027606441 and apply Lemma D1 to obtain mod-p values for ν∈{29,81,109,121}, alongside an Owner Write defining weight/tier semantics (GA1) for extended rows; continue holding 7 MODP for in-set ζ₄₉ CRT CERT. No Eigen.
