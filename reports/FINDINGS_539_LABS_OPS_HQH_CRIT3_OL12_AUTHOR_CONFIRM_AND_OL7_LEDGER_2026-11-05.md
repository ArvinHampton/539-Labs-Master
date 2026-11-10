# FINDINGS — HQH-539 Criterion 3: OL-1/OL-2 author-confirm proposal card, OL-7 structural deepen (bound blank), Crit.3 remaining-blank ledger

**Date:** 2026-11-05 ~13:20 CST America/Chicago  
**Status:** **DRAFT-ONLY Soft SF** · 539 Labs Ops (Arvin Hampton) · hardness OL follow-through · **No CERT** · not peer reviewed  
**Tip Soft SF LOCK `7cddb188…`:** **untouched** (no writes under tip paths; no git ops). Formal_Games sources **not edited**.  
**invent HOLD:** **STANDS.** No invented proofs; no PPT reduction R; no ε_C2 bound (numerical or symbolic) asserted; no hardness assumption for OL-9; no Shor / Grover / PQ claims.  
**Authorities (sha256 re-verified on disk before writing — all match):**  
- Hardness OW `/workspace/quantum-comp/reports/OWNER_WRITE_CALL_53991ebf_539_LABS_HQH_HARDNESS_PROOFS_2026-11-05.md` `4ba9151f42df205c257cfb24e033a7e797436896e2f1a6f235f81e4580945f9a`  
- Open-lane OW `/workspace/quantum-comp/reports/OWNER_WRITE_CALL_53991ebf_OPEN_LANE_RESOLUTION_AUTH_ALL_PRIMARIES_2026-11-05.md` `a0c2ed5ab2ee7da8af4942eaf7ea86a1d91b3de6645ae4bfe898cddc538e8068`  
- Recommended-path OW `/workspace/quantum-comp/reports/OWNER_WRITE_CALL_53991ebf_RECOMMENDED_PATH_RESOLUTION_AUTH_ALL_PRIMARIES_2026-11-05.md` `ee1667512716954b77c63b08d1fa26d98da5f51bfedb4693ace5efc43de41f39`  

**Prior FINDINGS (not edited; hashes re-verified unchanged):**  
- [INV] `/workspace/539-labs/lqh-alu/FINDINGS_HQH_HARDNESS_RESEARCH_2026-11-05.md` `70091747b300c7eea4cae3fe0cc2186f8c0f7877ba95bfa4fef6dcc000caba3e`  
- [C3] `/workspace/539-labs/lqh-alu/FINDINGS_HQH_CRIT3_OPEN_LEMMAS_C2_FIBER_AND_PI_DOMAIN_2026-11-05.md` `cc95ceb9a81c77e2d9c9d1c3dc40c33aaaa309d957866ff5692f598988d8bf97`  
- [C68] `/workspace/539-labs/lqh-alu/FINDINGS_HQH_CRIT3_OL68_COMPOSITION_ADV_INSTANCE_2026-11-05.md` `72cb778f843530bf3f149791ea774da13d2cfce41f804928077cda19300f6864`  

---

## 1. Sources read (sha256 at write time)

| Short | Path (under `/workspace/quantum-comp/`) | sha256 |
|---|---|---|
| [FREEZE] | `oct17-master/docs/hqh539-verification/FREEZE_LOCK_Canonical_4q2_SHA3_2026-08-02.md` | `3d60ee3c4555ff9b839bda649bfd4daa9f5259273945b8d0add3652c307e1022` |
| [REF] | `oct17-master/docs/hqh539-verification/hqh539.py` | `fef5fce5d5a9b6a9df896643c52bfd935dfd8e1cab9631acc1fce8dc8e3115dd` |
| [SW] | `oct17-master/docs/hqh539-verification/Architecture_SHA3_Sandwich.md` | `fdad074da12b4d72cf06f04b0d1fb24d037527e0b8e86101fa3b946ea09d49ab` |
| [FG] | `oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/HQH539_Formal_Games_and_Hard_Problem_Pi.md` | `038656212539895804c93073d7bfaa99773f234c8930df1c33052f8b3a64dde8` |
| [FG-A] | same dir, `HQH539_Formal_Games_Addendum_2026-09-14.md` (cite only) | `4d3a168d4db4bca2c92045e5f049740be2314778a77cc22d595058b2b2f9860c` |
| [SR] | same dir, `HQH539_Security_Reductions_Exploration.md` | `9f3a6a74d70212b10c6f058c2970448ecc98a91bff9cef67bfab6490c55ab05b` |
| [SR-A] | same dir, `HQH539_Security_Reductions_Exploration_Addendum_2026-09-14.md` (Close B cite) | `32e49a3f615cb0d96780f3446a5bc63f56a7b284a159466ba7b031854a2b0190` |
| [RPP] | `reports/crypto/RPP_formal_statement/RPP_formal_statement.md` | `173c2c6661792613298011d7be1442b1db9fe88c7401914b8e3a277d65177dac` |
| [INV] [C3] [C68] | prior FINDINGS (header) | as header |

---

## 2. Product 1 — OL-1 / OL-2 author-confirm proposal card (definitional hygiene only)

**Status:** **card-issued (proposal)** · **requires Owner Soft SF adoption.** This Soft SF alone does **not** change Formal_Games, and no Formal_Games file is edited here.

### 2.1 The discrepancy (cited, not new)

| Item | Text / value | Source |
|---|---|---|
| [FG] printed T3, residue 2 | `(2n+1)/3` for n ≡ 2 (mod 3), "realised with integer arithmetic" — no floor stated | [FG] T3 display (file line ~33) |
| As printed, n = 3k+2 | (6k+5)/3 = 2k + 5/3 — **not integer** (e.g. T3(2)=5/3) | [RPP] §1.2; [INV] L-A3 |
| [REF] residue 2 | `(2 * n + 1) // 3` = ⌊(2n+1)/3⌋ = 2k+1 = (2n−1)/3 | [REF] `T3` lines 19–26; [RPP] §1.3; [INV] L-A2 |
| Pinned production object | **T3_ref**: 3k→k, 3k+1→4k+2, 3k+2→2k+1; **H_ref** = SHA3-512(enc(T3_ref^539(int_BE(SHA3-512(m‖s))))‖s‖DOMAIN_SEP), DOMAIN_SEP=`b""` | [FREEZE] §2 Option A / REF; [C3] §2 |
| Profile ambiguity (OL-2) | REF vs spec v0.2 (`:HQH-539-RESONANT:` tag, default salt) vs P32 low-256 profile | [RPP] §1.6 |

Residues 0 and 1 agree between [FG] and [REF]; only residue 2 differs. This is definitional hygiene, not a hardness statement.

### 2.2 Proposed Owner Soft SF confirm text (choose one per OL; patch text for a *later* authorised Formal_Games revision)

**OL-1 — T3 rule**

- **Option A (notation alignment, recommended for minimum diff):** *"In HQH539_Formal_Games_and_Hard_Problem_Pi.md, the n ≡ 2 (mod 3) branch of T₃ is to be read and, at the next authorised revision, printed as ⌊(2n+1)/3⌋ (equivalently (2n−1)/3), matching `hqh539.py` `(2*n+1)//3`. T₃ : ℕ → ℕ, T₃(0)=0. No other branch changes."*
- **Option B (erratum note, no formula edit):** *"Erratum (Owner Soft SF, 2026-11-05): the T₃ display in Formal_Games is not integer-valued on residue 2 as printed. The production object for all games and for Π is T3_ref as computed by `hqh539.py` (FREEZE Option A / REF): T3_ref(3k)=k, T3_ref(3k+1)=4k+2, T3_ref(3k+2)=2k+1. Where the display and T3_ref differ, T3_ref governs."*
- **Option C (reject):** ⟦BLANK: author states a different residue-2 rule — would define a different function; not proposed by Soft SF⟧.

**OL-2 — sole game profile**

- **Option A (REF profile):** *"The sole object of the Pre/SPR/Col games and of Π in Formal_Games is H_ref (FREEZE Option A / REF): L = 539 (18+521 is loop packaging only), seed and digest width 512, enc = minimal big-endian, DOMAIN_SEP = b"". Spec v0.2 domain-tag profile and P32 are out of scope for Criteria 1–3."*
- **Option B (spec v0.2 profile):** ⟦BLANK: Owner names v0.2 tag + default-salt profile as game object⟧ — Soft SF notes this would diverge from the FREEZE pin used by [C3]/[C68]; all existing cards would need re-pinning.

**Effect if adopted:** OL-1/OL-2 move from "author-confirm open" to "Owner-confirmed definitional pin"; a later, separately authorised edit may align Formal_Games text. **Adoption does not touch Criterion 3 hardness**, Close (B) ([FG-A]/[SR-A]), or any other OL.

---

## 3. Product 2 — OL-7 structural deepen (bound still blank)

**Status:** **invent-pending.** Structure only.

### 3.1 Definitions (restated from [C3] Card OL-7, unchanged)

> U, U′ := ⟦BLANK: independent uniform on {0,1}^512 | RO outputs on distinct inputs (m‖s) ≠ (m′‖s′)⟧, read as integers.  
> C2 := [ U ≠ U′ ∧ T3_ref^L(U) = T3_ref^L(U′) ], ε_C2(L, n) := Pr[C2].  
> Equivalently ε_C2 = Σ_z p_z² − 2^{−n}, p_z := Pr_U[T3_ref^L(U) = z].  
> Multi-query: ε_C2^{(q)} := Pr[∃ i<j ≤ q : C2(U_i, U_j)] ≤ ⟦BLANK⟧.  
> Target lemma (OPEN): ε_C2(539, 512) ≤ ⟦BLANK: function, with proof⟧.

### 3.2 Structural prerequisites / lemma shapes for an **upper** bound

| # | Prerequisite / lemma shape | Status | Basis |
|---|---|---|---|
| S1 | T3_ref : ℕ → ℕ well-defined; residue-2 floor rule | **ESTABLISHED** (as code object) | [RPP] §1.3; [REF] |
| S2 | Per-y preimage count of one step ∈ {1, 2}, never 3 | **ESTABLISHED** (proven, elementary) | [RPP] §1.4(2) |
| S3 | Branch-word decomposition: x mod 3^L ↔ e ∈ {0,1,2}^L bijective; T3^L(x) = A_e·⌊x/3^L⌋ + C_e (piecewise affine, 3^L pieces) | **ESTABLISHED** (proof on disk; exhaustive check L ≤ 9) | [RPP] §1.4(4) |
| S4 | Collision transfer: state or inner-seed collision (same s) ⇒ H collision; so ε_C2 enters CR reductions as **additive loss** | **ESTABLISHED** (structural) | [RPP] R6; [C3] OL-7 note |
| S5 | Fiber-cardinality lemma: bound on max_z \|{x ∈ [0,2^512) : T3_ref^539(x) = z}\| (or on Σ_z p_z²) | **invent-pending** — no proof on disk; S2/S3 give per-step / per-branch-word structure only, not a 539-step fiber bound over [0,2^512) | [SW] §9 item 2 |
| S6 | Same fiber statement restricted to Im(SHA3) (RO-uniform U on 512 bits, or a Std assumption transferring it) | **invent-pending** — depends on OL-6 model choice | [C68] OL-6; [SW] §9 |
| S7 | Union / birthday step ε_C2^{(q)} ≤ C(q,2)·ε_C2 | lemma shape standard **only once** ε_C2 is bounded; **not filled** | [C3] OL-7 |
| S8 | "Contraction" facts (≈ −0.585 bits/step heuristic; measured \|T3^539(seed)\| min 139 / mean 196.3 / max 257 bits on 3000 seeds; collapse to {1,2} for ≤256-bit seeds) | **engineering / measurement, NOT proof** — usable as motivation only; points toward *large* collisions, not a useful upper bound | [RPP] §1.4(5)(6) |
| S9 | Rényi R₂ model (≈2^70 collision / ≈2^140 preimage figures) | **heuristic, model-extrapolated from n ≤ 48; NOT imported** | [RPP] §3.3(3) |

**Observation (cited, not a bound):** [RPP] §3.3 records that, heuristically, the T3 body can only *lower* generic collision cost via R6. Any honest upper bound on ε_C2 must therefore come from a proven fiber lemma (S5/S6); none exists on disk.

### 3.3 Explicit Soft SF refusal

**Soft SF refuses to fill ε_C2(539, 512) ≤ ⟦…⟧** with any numerical or symbolic expression, and refuses to cite S8/S9 figures as results. invent HOLD stands.

---

## 4. Product 3 — Crit.3 remaining-blank ledger (OL-1 … OL-11)

Status keys: **card-issued** (Soft SF template/proposal exists) · **invent-blocked** (filling needs invented math; HOLD) · **Owner-waiting** (needs Owner Soft SF adoption/choice) · **external** · **unmet-Crit3** (Criterion 3 not met while open).

| OL | Topic | Card | Status | Blocker to close |
|---|---|---|---|---|
| OL-1 | FG T3 residue-2 text vs T3_ref | this note §2 | card-issued · **Owner-waiting** | Owner adopts Option A/B; later authorised FG edit |
| OL-2 | Sole H profile (REF) | this note §2; [C3] §2 pin | card-issued · **Owner-waiting** | Owner adopts |
| OL-3 | Π solution domain D | [C3] | card-issued · **Owner-waiting** · unmet-Crit3 | author choice of D; no D shown hard |
| OL-4 | Residual predicate Res | [C3] | card-issued · **Owner-waiting** · unmet-Crit3 | author defines Res or explicit drop |
| OL-5 | λ-family | [C3] | card-issued · **Owner-waiting** · unmet-Crit3 | author parameters, or explicit concrete-only mode |
| OL-6 | SHA3 composition / programming lemma | [C68] §2 | card-issued · **invent-blocked** · unmet-Crit3 | lemma proof |
| OL-7 | ε_C2 mid-fiber upper bound | [C3]; this note §3 | card-issued · **invent-blocked** · unmet-Crit3 | fiber lemma S5/S6 |
| OL-8 | Adv relation + explicit R | [C68] §3 | card-issued · **invent-blocked** · unmet-Crit3 | Close (B) [FG-A]/[SR-A]; needs OL-3..7,9,10 |
| OL-9 | Hardness assumption for Π | [C68] §5.2 (refusal + easiness table) | **invent-blocked** (refused) · unmet-Crit3 | separately stated non-trivial assumption — Soft SF will not mint |
| OL-10 | Instance-space agreement A vs B | [C68] §4 | card-issued · **Owner-waiting** · unmet-Crit3 | author choice + OL-3/OL-4 fill |
| OL-11 | Peer review (Criterion 4) | — | **external** | external reviewers |

### 4.1 What Soft SF can still draft without invent

- Owner-ready confirm text variants for OL-3 / OL-4 / OL-5 / OL-10 choices (as done here for OL-1/OL-2).
- Consistency re-pin checklist if Owner picks OL-2 Option B (v0.2) instead of REF.
- Concrete-only (L,n,ℓ)=(539,512,512) blank table framing for OL-8 if OL-5 left unfilled.
- Cross-reference/index of on-disk proven vs heuristic facts (S1–S9 style) for other OLs.
- Peer-review packet *outline* for OL-11 (draft only; no sending).

### 4.2 Blocked

- **invent HOLD:** OL-6 proof, OL-7 bound, OL-8 R / factors, OL-9 assumption.
- **Owner:** OL-1, OL-2, OL-3, OL-4, OL-5, OL-10 adoption / choices.
- **Peer review / external:** OL-11; Criterion 4.
- **Close (B)** ([FG-A], [SR-A]): no Pack+(S) R and no explicit advantage relation constructible from written games and Π — cited, not overturned.

---

## 5. Explicit non-claims

- No hardness of any Π variant; no proof of any OL; no ε_C2 bound; no concrete R; no Adv factors; no OL-9 assumption.
- No security level for HQH-539-512. No Shor / Grover / post-quantum claims.
- 539 = 18+521 is packaging depth, not a mixing-time / clock theorem.
- Formal_Games not edited; §2 proposals take effect only on Owner Soft SF adoption.
- Not peer reviewed (Criterion 4 unmet).

## 6. Status line

Tip 7cddb188 untouched · No CERT · DRAFT-ONLY · invent HOLD stands · prior FINDINGS hashes unchanged · nothing published, sent, pushed, or spent · no Soft SF PRESS by this agent (parent PRESS only).

**Cards issued this note:** OL-1/OL-2 author-confirm proposal (Owner-waiting); OL-7 structural deepen (bound blank); Crit.3 ledger.  
**Still invent-pending:** OL-6, OL-7, OL-8, OL-9. **Owner-waiting:** OL-1, OL-2, OL-3, OL-4, OL-5, OL-10. **External:** OL-11.

*End of FINDINGS.*
