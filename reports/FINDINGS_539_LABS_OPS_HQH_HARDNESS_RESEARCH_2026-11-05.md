# FINDINGS — Soft SF hardness research (HQH-539-512 sandwich) — draft-only — 2026-11-05

**Date:** 2026-11-05 ~12:52 CST America/Chicago  
**Mode:** Soft SF draft FINDINGS only. **Do not publish, send, push, or spend.**  
**Tip Soft SF LOCK `7cddb188…`:** **untouched** (this file does not write under tip/`7cddb188` paths).  
**CERT:** **None.** No CERT claimed or requested.  
**Proofs:** **None invented.** No PPT reduction R constructed. No claim of proven PQ / Shor–Grover immunity / BQP⊂C⊂NP.

---

## 1) Authority ACK

| Field | Value |
|-------|--------|
| Owner Write Call | `/workspace/quantum-comp/reports/OWNER_WRITE_CALL_53991ebf_539_LABS_HQH_HARDNESS_PROOFS_2026-11-05.md` |
| Verified sha256 | `4ba9151f42df205c257cfb24e033a7e797436896e2f1a6f235f81e4580945f9a` (**matches** required) |
| Prior inventory | `/workspace/539-labs/lqh-alu/STATUS_HQH539512_2026-11-05.md` sha256 `2ca44213de3024ff600e943012a796fcee897142c73765111d1c5928f548b0bf` |
| OW decision (as filed) | Soft SF lift from FULL STOP **for this task only**: begin hardness research grounded in pure math of HQH-539-512; Draft FINDINGS → PP Soft SF audit → Keeper; **No invented proofs**; **No CERT unless Owner names one**; nothing published/spent without Owner approval |

**This FINDINGS is the first Soft SF research product under that OW.** It inventories lemmas and Criterion-3 gaps from on-disk sources. It does **not** complete Criterion 3 or 4.

**Locked profile (brief):** FREEZE `FREEZE_LOCK_Canonical_4q2_SHA3_2026-08-02.md` + `HQH539_Verification_Status.md` — Option A / REF **ACCEPTED**; Canonical T3 with r0=`n//3`, r1=`(4n+2)//3` (=`4q+2`), r2=`(2n+1)//3`; depth **exactly 539 = 18+521**; public API = SHA3-512 seed → T^539 → SHA3-512 finalize (REF `DOMAIN_SEP=b""`).

---

## 2) Pure-math / structural lemma inventory (sandwich)

Construction (Option A / REF), cited from `Architecture_SHA3_Sandwich.md` and FREEZE:

```text
seed = int(SHA3-512(message ‖ salt))
fp   = T_3^{539}(seed)     # Canonical T3; packaged 18+521
digest = SHA3-512( encode_minBE(fp) ‖ salt ‖ DOMAIN_SEP )   # DOMAIN_SEP = b""
```

Classification key used below:

- **ESTABLISHED** — elementary algebra / packaging identities / structural facts already written on disk (Cat A hygiene or structural analysis). **Not** hardness.
- **ENGINEERING** — KAT / census / stress / avalanche / RTL vector facts. Implementation identity only.
- **INVENT-PENDING / NEEDS-DEFINITION** — named but undefined, or needed for a reduction, or hardness language without a proof.

### 2.1 ESTABLISHED (algebra / packaging / structure — not hardness)

| ID | Lemma / fact (as on disk) | Source |
|----|---------------------------|--------|
| L-A1 | On \(n=3q\): \(T_3(n)=q\) (exact). On \(n=3q+1\): \(T_3(n)=(4n+2)/3=4q+2\) exact (integrality \(4n+2\equiv0\pmod3\)). | FREEZE §2; `Architecture_Residue1_4q2_Map.md` §1; REF `hqh539.py` |
| L-A2 | On \(n=3q+2\): **as implemented**, \(T_3(n)=(2n+1)//3=2q+1\) (= \((2n-1)/3\)). | FREEZE; REF code; RPP §1.3 (labels this \(T3_{\mathrm{ref}}\)) |
| L-A3 | As **printed** in Formal_Games without floor: \((2n+1)/3\) is **not** integer-valued on all residue-2 inputs — domain/codomain of \(T_3\) as FG text alone are incomplete; production object is \(T3_{\mathrm{ref}}\). | RPP §1.2–1.3 (**definitional hygiene**, not a hardness claim) |
| L-A4 | r1 branch \(q\mapsto4q+2\) is injective on \(\mathbb{N}\); image always \(\equiv2\pmod4\); \(T_{\mathrm{Canonical}}(n)=T_{\mathrm{T4121}}(n)+1\) on every residue-1 input. | Residue1 map §1–2; FREEZE §2 |
| L-A5 | Full one-step \(T_3\) is **not** injective: constructive cross-branch collisions (Family A r0–r1: \(T(3(4q+2))=T(3q+1)\); Family B r0–r2); r1–r2 one-step collisions impossible (parity). Collisions **lift** under iteration. | `Architecture_Collision_4q2.md` §3 |
| L-A6 | Formal one-step preimages of \(y\): always \(3y\); plus \((3y-2)/4\) when \(y\equiv2\pmod4\); plus odd-branch candidate when \(y\) odd — typically **1 or 2** preimages (never three under mutual exclusion of even/odd cases as in RPP §1.4). | Residue1 §3; Collision; RPP §1.4 item 2 |
| L-A7 | Packaging identity: round budget \(L=539=18+521\) (Principle (S) packaging / FREEZE depth). Games stated for full \(L=539\). Split is loop packaging; REF applies the same \(T_3\) 539 times. | Formal_Games; FREEZE; Security_Reductions §2.1; RPP §1.6 |
| L-A8 | Sandwich CR path partition (structural): collision \(H(m,s)=H(m',s)\) implies one of **C1** (inner SHA3 collision), **C2** (mid \(T^{539}\) fiber collision on distinct seeds in Im(SHA3)), **C3** (encode alias — should not occur for distinct \(\mathbb{Z}_{\ge0}\) under min-BE), **C4** (outer SHA3 collision). | `Architecture_SHA3_Sandwich.md` §2.1 |
| L-A9 | Bare \(T\) / bare \(T^{539}\) is **not** a CR compression function (constructive collisions + contraction). Public API is the **full sandwich**. | Sandwich §1; FREEZE §3; Collision §1 |
| L-A10 | Min-BE `encode(fp)` injective on \(\mathbb{Z}_{\ge1}\) (unique width). Fixed-salt finalize payload \(fp\mapsto\mathrm{encode}(fp)\|s\) injective → outer distinct-payload CR reduces cleanly to SHA3-CR on those payloads (**structural**, not a completed HQH reduction). | Sandwich §4.1–4.2 |
| L-A11 | Cycle \(\{1\leftrightarrow2\}\); fixed point \(0\). 539 is **hash packaging depth**, not a measured pure-map stopping time for free seeds. | FREEZE §2, §6 non-claims; Verification_Status |
| L-A12 | Piecewise-affine itinerary fact (RPP): \(x\mapsto e(x)\in\{0,1,2\}^L\) bijective on \(x\bmod 3^L\); \(T_3^L\) has exactly \(3^L\) affine pieces (induction; verified small \(L\)). | RPP §1.4 item 4 (**algebra of the map**, not hardness of H) |

### 2.2 ENGINEERING (not security proofs)

| ID | Fact | Source |
|----|------|--------|
| E1 | Residue-1 algebra explore PASS; unit tests REF/P32 PASS; goldens match. | Verification_Status; FREEZE §4 |
| E2 | Long-orbit census 1..50k: max 55 steps to 1; mean ≈21.91. Large-seed \(T^{539}\): strong contraction (2 unique endpoints / 2000 samples). | Verification_Status |
| E3 | Sandwich probe 5k msgs: unique seeds/fps/digests 5000/5000 — **not** a CR proof. | Sandwich §7 |
| E4 | Avalanche mean bit-flip ≈0.500; JSON marks `not_a_security_proof: true`. | STATUS inventory; Security_Reductions §2.5 |
| E5 | RTL vector cross-check Canonical recorded PASS; Vivado PnR/xsim = PENDING_LAB. | STATUS |
| E6 | Measured residual fingerprint bit-length after 539 steps from 512-bit SHA3 seeds ≈196±19 bits (RPP scripts) — **heuristic/engineering**, used only as structural entropy note in Sandwich §5. | RPP §1.4 item 5; Sandwich §5 |

### 2.3 INVENT-PENDING / NEEDS-DEFINITION (do not fill in Soft SF)

| ID | Gap | Source |
|----|-----|--------|
| N1 | PPT reduction \(R\) + advantage relation (Criterion 3). | Formal_Games Crit. 3; U1_LEDGER Close (B) |
| N2 | Independent peer review / external cryptanalysis (Criterion 4). | Formal_Games Crit. 4 |
| N3 | Residual predicate \(R\) on a path (O_res-indexing, fiber membership, permanent-class evaluation) — **undefined** for a Boolean/path predicate; arithmetic \(3\cdot68+5\cdot67=539\) only. | RPP §2.5; U1 I10 |
| N4 | Security-parameter family \(\lambda\mapsto(L(\lambda),n(\lambda),\ldots)\) for asymptotic Adv statements. | RPP §3.2 item 1; Formal_Games Crit. 3 template uses \(\lambda\) without a family |
| N5 | Random-oracle / programming / indifferentiability / collision-transfer **composition lemmas** for the SHA3 sandwich wrapper. | U1 C2; Sandwich §9; RPP R5 |
| N6 | Hardness of Π (any fully defined variant) — **not established**; RPP records Π_free easy (proven \(x=3^L y\)); Π_bnd empirically easy at stated params (**heuristic**). | Formal_Games Crit. 2 notes; RPP §2.4 |
| N7 | Codex / corpus Shor–Grover immunity; \(BQP\subset C_{\mathrm{HQH}}\subset\mathrm{NP}\)-Complete; proven PQ for HQH-539-512. | STATUS invent-pending fences; Sandwich §3 “Quantum security — Not analyzed” |
| N8 | Retracted / uncapped figures \(3^{539}\) / \(3^{270}\) as security levels — fail against 512-bit output generic bounds (RPP §4.2); **must not** be reasserted. | RPP §4 |

---

## 3) Games Pre / SPR / Col and hard problem Π (restated from Formal_Games)

**On-disk status line (Formal_Games header):**  
> “Exploration note meeting reduction criteria 1 and 2 where feasible. **Criteria 3 and 4 remain unmet.** Hardness language: Category B only.”

### 3.1 Criterion 1 — games (SUPPLIED)

Public \(\mathcal{H}\): \(u_0=\mathrm{SHA3\text{-}512}(m\|s)\) as integer; \(u_{i+1}=T_3(u_i)\) for exactly \(L=539\); \(H(m,s)=\mathrm{SHA3\text{-}512}(\mathrm{bytes}(u_{539})\|s)\).

| Game | Win condition (on-disk wording condensed) | Advantage |
|------|-------------------------------------------|-----------|
| **Preimage** | Challenger issues digest \(y\); \(\mathcal{A}\) outputs \((m,s)\) with \(H(m,s)=y\) | \(\mathrm{Adv}^{\mathrm{pre}}_{\mathcal{H}}(\mathcal{A})\) |
| **Second-Preimage** | Challenger issues \((m^*,s^*)\) and \(y=H(m^*,s^*)\); \(\mathcal{A}\) outputs distinct pair with same digest | \(\mathrm{Adv}^{\mathrm{spr}}_{\mathcal{H}}(\mathcal{A})\) |
| **Collision** | \(\mathcal{A}\) outputs two distinct pairs with \(H(m,s)=H(m',s')\) | \(\mathrm{Adv}^{\mathrm{col}}_{\mathcal{H}}(\mathcal{A})\) |

Formal_Games: “These are the standard cryptographic games adapted to the published HQH-539 API. **They do not constitute a hardness proof.**”

### 3.2 Criterion 2 — Π Resonant Path (SUPPLIED as statement; difficulty not proven)

**Instance:** target integer \(y\) (or digest derived from it) + public residual parameters (\(|\mathcal{O}_{\mathrm{res}}|=539\); fiber blocks 3×68 + 5×67; optional permanent class; \(L=18+521=539\)).

**Search:** recover seed \(x\) s.t. length-\(L\) Canonical-\(T_3\) trajectory lands on \(y\) (or yields given digest after final SHA3) **and** respects declared residual constraints when active.

**Decision:** given \((x,y)\) and residual parameters, decide whether the unique length-\(L\) path lands on \(y\) and satisfies constraints.

Formal_Games notes (cite): combinatorial objects are Cat A; “**The computational difficulty of Π is not established by those pure-math facts alone.**”; “**No asymptotic or concrete hardness proof for Π is claimed.**”

Addendum 2026-09-14 (Formal_Games): Close (B); “No Pack+(S) algorithm R and no explicit advantage relation are constructible from the written games and written Pi”; PR1–PR10 / OBR1–OBR4 lock Criterion 3 unmet; “does not invent hardness from free Canonical T3”.

### 3.3 Criteria 3–4 (UNMET — cite, do not invent)

**Criterion 3** (Formal_Games, quote shape): no PPT \(R\) with
\[
\mathrm{Adv}^{\mathrm{game}}_{\mathcal{H}}(\mathcal{A})
\le
\mathrm{poly}(\lambda)\cdot\mathrm{Adv}^{\Pi}(R^{\mathcal{A}})
+ \mathrm{negl}(\lambda)
\]
(or concrete analogue) is supplied. “**This criterion remains unmet.**”

**Criterion 4:** “No independent external cryptanalysis or peer-reviewed validation of a reduction for HQH-539 exists. **This criterion remains unmet** and cannot be satisfied internally.”

Security_Reductions_Exploration + Addendum 2026-09-14: **no completed security reduction**; forbidden “provably secure / unbreakable / information-theoretic”; packaging COUNT 539 is not a clock.

U1_LEDGER_PPT_R (companion): Close (B) from written Master data — no algorithm R; no SHA3 composition lemma; games vs Π instance-space mismatch; no written hardness source for R to carry; engineering substitutes are not R.

---

## 4) First research product — open-lemma list toward Criterion 3

**Product of this FINDINGS:** a precise checklist of what a future PPT reduction would need, plus structural lemmas that **can** be stated from Architecture_SHA3_Sandwich **without** claiming hardness. Soft SF **does not** invent the missing lemmas’ proofs.

### 4.1 Structural lemmas stateable carefully (no hardness claim)

These are restatements of Sandwich / Collision / Residue notes — **ESTABLISHED as structure**, not as “H is secure”:

1. **Bare-\(T\) non-CR:** Explicit infinite one-step collision families + lift ⇒ bare \(T^k\) not CR as a free map on \(\mathbb{Z}\).
2. **Sandwich necessity:** Inner SHA3 commits seeds; outer SHA3 randomizes variable-width \(fp\); without both faces, marketing \(T^{539}\) as general-purpose CR is unjustified on present structure (Sandwich §1).
3. **C1–C4 partition:** Any fixed-salt message collision factors through C1/C2/C3/C4 as above; C3 ruled out for distinct nonnegative ints under min-BE; C1/C4 are SHA3-CR problems; **C2 is the sandwich-specific hinge** — “**no claim that C2 is computationally hard — only that it is not free**” (Sandwich §2.1, on-disk wording).
4. **Non-transfer of bare collisions:** Constructive pairs such as \(T(6)=T(1)\) do **not** automatically yield HQH message collisions; both seeds must lie in \(\mathrm{Im}(\mathrm{SHA3})\) (Sandwich §2.1 implication).
5. **Encode / salt framing hygiene:** min-BE injectivity; fixed-salt outer injectivity; variable-salt concat ambiguity without length framing (Sandwich §4) — protocol hygiene, not a reduction.
6. **Future reduction must-handle list (Sandwich §9, already written):** (i) SHA3 model (RO or standard assumption); (ii) bound on Pr[two independent RO outputs in same \(T^{539}\) fiber]; (iii) encode + salt framing; (iv) exclude free integer-seed games (API is message-based).

### 4.2 Open lemmas for Criterion 3 (NEEDS-DEFINITION / invent-pending — do not invent here)

Toward a relation \(\mathrm{Adv}_{\mathrm{Game}}\leftrightarrow\mathrm{Adv}_{\Pi}\) (or a corrected hard problem), Soft SF records **gaps**, not proofs:

| Gap ID | What would be needed (from on-disk obstruction + RPP §3.2 / Sandwich §9) | Status |
|--------|--------------------------------------------------------------------------|--------|
| OL-1 | **Fix \(T_3\) text** to \(T3_{\mathrm{ref}}\) (domain \(\mathbb{N}\), residue-2 floor rule) in the games/Π parent note so Crit. 1–2 objects are single-valued. | NEEDS-DEFINITION (RPP §1.5) — author confirm; Soft SF does not rewrite Formal_Games here |
| OL-2 | **Pin one profile** of H (REF vs spec v0.2 domain tag vs P32) as the sole game object. | NEEDS-DEFINITION (RPP §1.6) |
| OL-3 | **Define Π’s solution domain:** free \(\mathbb{N}\) vs bound \(<2^n\) vs restricted to \(\mathrm{Im}(\mathrm{SHA3})\). Note on disk: Π_free trivial via \(x=3^L y\); SHA3-restricted Π collapses toward the preimage game itself (RPP R1–R4). | NEEDS-DEFINITION; invent-pending hardness |
| OL-4 | **Define residual path predicate** (or explicitly drop residual-only constraints from the public-hash reduction target and rename the problem). U1 C3: games and Π are not the same instance space. | NEEDS-DEFINITION (RPP §2.5; U1 I10/C3) |
| OL-5 | **Parameter family** \(\lambda\) with \(L(\lambda)\), seed width, digest width — else poly/negl Adv template is not well-typed. | NEEDS-DEFINITION |
| OL-6 | **Composition / programming lemma** for outer (and inner) SHA3: plant Π target into digest / extract inner endpoint from digest win (RO programming or stated standard assumption). U1 C2: none written. | invent-pending lemma |
| OL-7 | **C2 fiber-collision probability bound** under RO seeds: \(\Pr[T^{539}(U)=T^{539}(U')]\) for independent uniform 512-bit (or RO) seeds — quantitative mid-collision term in any CR reduction. Sandwich §9 item 2 names this; no proven bound claimed here. | invent-pending (heuristic Rényi/collision models in RPP §3.3 are **not** imported as proofs) |
| OL-8 | **Advantage relation + algorithm \(R\)**: inputs of \(R\), how \(R\) wraps \(\mathcal{A}\), simulation of SHA3, extraction of Π witness, poly/negl or concrete table. | invent-pending (Formal_Games Crit. 3; U1 C1) |
| OL-9 | **Hardness assumption** for the fully defined Π (or replacement assumption, e.g. SHA3-CR + mid-fiber bound) stated **separately** from the construction — with basis that is not already trivial on disk. | invent-pending; do **not** invent from free T3 (Addendum / U1 I8) |
| OL-10 | **Instance-space agreement:** either change games to residual-legal wins, or change Π to unrestricted fixed-round inversion under SHA3 image restriction — without claiming the changed problem hard from present data. | invent-pending design choice |
| OL-11 | **Peer review path** (Criterion 4) — external; Soft SF cannot close. | unmet / external |

**Explicit Soft SF refusal:** this section does **not** supply proofs of OL-6–OL-9, does **not** redefine Π to dodge RPP easiness results, and does **not** treat packaging 539 as a mixing-time or clock theorem.

---

## 5) Explicit non-claims (mandatory)

| Non-claim | Basis on disk |
|-----------|----------------|
| **No Shor / Grover immunity** | Sandwich §3: quantum security **not analyzed**; STATUS invent-pending fence; Codex language REPORTS ONLY |
| **No \(BQP\subset C\subset\mathrm{NP}\) (or \(C_{\mathrm{HQH}}\)) membership as fact** | STATUS / INTAKE invent-pending |
| **No proven post-quantum security** for HQH-539-512 | FREEZE / Verification_Status non-claims; Formal_Games Crit. 3–4 unmet |
| **Bare \(T_3\) is not collision-resistant** | Collision + Sandwich §1 |
| **Avalanche ≈½ and KATs ≠ security proof** | Security_Reductions §2.5; avalanche JSON flag; U1 C5 |
| **No completed PPT reduction \(R\)** | Formal_Games Crit. 3; U1 Close (B) |
| **No CERT** | This FINDINGS; OW |
| **Tip `7cddb188…` untouched** | This FINDINGS |
| **Do not reassert \(3^{539}/3^{270}\) security levels** | RPP §4 (retracted / arithmetically impossible as uncapped levels for 512-bit digests) |
| **Do not claim HQH-CR ⇔ SHA3-CR or HQH-CR ⇔ \(T\) CR** | Sandwich §3 non-implications |
| **Π statement ≠ Π hardness** | Formal_Games Crit. 2 notes; PR2 |

Locked Category B marketing sentence (only allowed hardness **language**, not a completed proof) remains as filed — Soft SF does not elevate it to CERT.

---

## 6) Next Soft SF unpaid step (one concrete pure-math draft target)

**Follow-on file target (still draft-only; still no invented proof; still no tip touch):**

`FINDINGS_HQH_CRIT3_OPEN_LEMMAS_C2_FIBER_AND_PI_DOMAIN_2026-11-05.md`  
(under `/workspace/539-labs/lqh-alu/`, with optional ops copy under `/workspace/quantum-comp/reports/`)

**Concrete pure-math draft contents for that follow-on (definitional / inventory only):**

1. **OL-3 pinboard:** three candidate solution domains for Π (free / bit-bounded / SHA3-image) with on-disk consequences already recorded in RPP R1–R4 and §2.4 — labeled CANDIDATE / author-confirm, **no new hardness**.  
2. **OL-7 statement skeleton:** formalize the **mid-fiber collision random variable** \(C_2\) for independent seeds in \(\{0,1\}^{512}\) under \(T3_{\mathrm{ref}}^{539}\) as a **definition** toward Sandwich §9 item 2 — mark any numerical bound **heuristic/engineering** unless a proof is later Owner-authorized.  
3. **OL-4 status line:** residual predicate = NEEDS-DEFINITION; public REF H does not evaluate it (U1 I10) — reduction target for public API must say so explicitly.

**Out of scope for that follow-on (and for this FINDINGS):** writing algorithm \(R\), claiming Adv inequalities, CERT, publish/push/spend, tip/`7cddb188` edits, Shor/Grover/PQ proofs.

---

## Document control

| Field | Value |
|-------|--------|
| Primary path | `/workspace/539-labs/lqh-alu/FINDINGS_HQH_HARDNESS_RESEARCH_2026-11-05.md` |
| Ops copy | `/workspace/quantum-comp/reports/FINDINGS_539_LABS_OPS_HQH_HARDNESS_RESEARCH_2026-11-05.md` |
| Method | Read OW + STATUS + Architecture_SHA3_Sandwich + Formal_Games (+Addendum) + Security_Reductions (+Addendum) + U1_LEDGER + RPP_formal_statement + FREEZE + Verification_Status + Residue1/Collision architecture notes; draft-only write |
| Tip | `7cddb188…` untouched |
| CERT | None |
| Invented proofs | None |

*End of FINDINGS.*
