# FINDINGS — HQH-539 Criterion 3 open lemmas: OL-6 composition, OL-8 Adv/R skeleton, OL-10 instance-space (definitional cards)

**Date:** 2026-11-05 ~13:12 CST America/Chicago  
**Status:** **DRAFT-ONLY Soft SF** · follow-on hardness research · **No CERT** · not peer reviewed  
**Tip Soft SF LOCK `7cddb188…`:** **untouched** (this file does not write under tip/`7cddb188` paths; no git ops).  
**invent HOLD:** **STANDS** (lane OW a0c2ed5a… ¶6). No invented proofs. No PPT reduction R algorithm filled. No hardness claims. No Shor / Grover / PQ claims.  
**Authorities (re-verified at write time):**  
- Hardness OW `/workspace/quantum-comp/reports/OWNER_WRITE_CALL_53991ebf_539_LABS_HQH_HARDNESS_PROOFS_2026-11-05.md` sha256 `4ba9151f42df205c257cfb24e033a7e797436896e2f1a6f235f81e4580945f9a`  
- Lane-resolution OW `/workspace/quantum-comp/reports/OWNER_WRITE_CALL_53991ebf_OPEN_LANE_RESOLUTION_AUTH_ALL_PRIMARIES_2026-11-05.md` sha256 `a0c2ed5ab2ee7da8af4942eaf7ea86a1d91b3de6645ae4bfe898cddc538e8068`  
**Prior FINDINGS (not edited; hashes unchanged):**  
- Inventory `/workspace/539-labs/lqh-alu/FINDINGS_HQH_HARDNESS_RESEARCH_2026-11-05.md` sha256 `70091747b300c7eea4cae3fe0cc2186f8c0f7877ba95bfa4fef6dcc000caba3e`  
- Crit3 pinboard `/workspace/539-labs/lqh-alu/FINDINGS_HQH_CRIT3_OPEN_LEMMAS_C2_FIBER_AND_PI_DOMAIN_2026-11-05.md` sha256 `cc95ceb9a81c77e2d9c9d1c3dc40c33aaaa309d957866ff5692f598988d8bf97`  

**Scope:** definitional / template cards for **OL-6**, **OL-8**, **OL-10** only. Context restatements for OL-7 / OL-9 / OL-1–OL-2. Nothing filled that invent HOLD forbids.

---

## 1. ACK / lineage

- Continues **OW 4ba9151f…** (hardness research) under lane-resolution **OW a0c2ed5a…**. Draft-only; nothing published, sent, pushed, or spent.
- Executes inventory FINDINGS §4.2 items OL-6, OL-8, OL-10 and Crit3 pinboard §4 blanks / §3 context note that those IDs remained invent-pending.
- Working object for all cards remains the Crit3 §2 pin: **H_ref / T3_ref** (Option A / REF; L=539, n=512, digest 512, DOMAIN_SEP=`b""`). This note does not rewrite Formal_Games; OL-1 / OL-2 author confirmation remains open (Crit3 §2, §5).
- **Tip 7cddb188 untouched.** No Soft SF PRESS by this agent (parent PRESS only).

### Sources read (sha256 at write time)

| Short | Path | sha256 |
|---|---|---|
| [SW] | `quantum-comp/oct17-master/docs/hqh539-verification/Architecture_SHA3_Sandwich.md` | `fdad074da12b4d72cf06f04b0d1fb24d037527e0b8e86101fa3b946ea09d49ab` |
| [FREEZE] | same dir, `FREEZE_LOCK_Canonical_4q2_SHA3_2026-08-02.md` | `3d60ee3c4555ff9b839bda649bfd4daa9f5259273945b8d0add3652c307e1022` |
| [VS] | same dir, `HQH539_Verification_Status.md` | `45e3cadd35bcf33b93f4b8c2cecb2e07c2f7063e38db775744d7ae9e7ebc1867` |
| [FG] | `quantum-comp/oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/HQH539_Formal_Games_and_Hard_Problem_Pi.md` | `038656212539895804c93073d7bfaa99773f234c8930df1c33052f8b3a64dde8` |
| [FG-A] | same dir, `HQH539_Formal_Games_Addendum_2026-09-14.md` | `4d3a168d4db4bca2c92045e5f049740be2314778a77cc22d595058b2b2f9860c` |
| [SR] | same dir, `HQH539_Security_Reductions_Exploration.md` | `9f3a6a74d70212b10c6f058c2970448ecc98a91bff9cef67bfab6490c55ab05b` |
| [SR-A] | same dir, `HQH539_Security_Reductions_Exploration_Addendum_2026-09-14.md` | `32e49a3f615cb0d96780f3446a5bc63f56a7b284a159466ba7b031854a2b0190` |
| [RPP] | `quantum-comp/reports/crypto/RPP_formal_statement/RPP_formal_statement.md` | `173c2c6661792613298011d7be1442b1db9fe88c7401914b8e3a277d65177dac` |
| [U1] | `quantum-comp/reports/heavy-daily/master-2026-09-14-ppt-r/U1_LEDGER_PPT_R_Obstruction_Written_Data_2026-09-14.md` | `fd8cebf1263de75f1641a67b4332a906be5aa61a4aad9691c765f972241e6578` |
| [INV] | prior inventory FINDINGS (above) | `70091747…caba3e` |
| [C3] | prior Crit3 pinboard FINDINGS (above) | `cc95ceb9…d8bf97` |

**Addendum note (cite, do not invent around):** [FG-A] states Close (B): “No Pack+(S) algorithm R and no explicit advantage relation are constructible from the written games and written Pi.” [SR-A] restates: no PPT algorithm R written; no explicit advantage relation written. This Soft SF issues **templates/blanks only** and does not claim those Close (B) obstructions are lifted.

---

## 2. Card OL-6 — Composition / programming lemma (outer and inner SHA3)

**Status:** NEEDS-DEFINITION / invent-pending lemma. **No lemma proof is supplied here.**

**Why the card exists (on-disk, cited):**  
- [U1] C2: planting a Π target as an inner endpoint requires programming or inverting the outer SHA3; extracting an inner endpoint from a digest requires opening the outer SHA3; “No random-oracle programming lemma, no indifferentiability statement for the wrapper, and no collision-transfer lemma from H to the inner map is written on Master.”  
- [SW] §9 items 1–4: future CR reduction must handle SHA3 model (RO or standard assumption); mid-fiber bound; encode + salt framing; exclusion of free integer-seed games.  
- [RPP] R5 (absent) + §3.2 item 4: treatment of both SHA3-512 layers — “either a model (random oracle for both calls, with a programming argument that plants a Π instance into a digest) or a stated standard assumption”; ledger records no such lemma written.  
- [SR] §2 structural ingredients / §3 needs: SHA3 front-end is Category A interface material, not a completed composition lemma.

**Proposed statement template (blanks only).**

> **Model choice** M ∈ {  
> &nbsp;&nbsp;**RO:** both SHA3-512 calls (seed and finalize) are independent random oracles of output length ⟦BLANK: ℓ = 512 fixed | ℓ(λ) from OL-5⟧;  
> &nbsp;&nbsp;**Std:** SHA3-512 is treated under ⟦BLANK: named standard assumption, e.g. CR / Pre / SPR of SHA3-512 on the relevant payload classes⟧  
> } — ⟦BLANK: author choice; one model per claimed lemma⟧.  
>
> **Planting (outer).** Given a Π instance ⟦BLANK: y ∈ ℕ | digest d | (d,s)⟧ under the OL-3/OL-4 definition in force, algorithm family ⟦BLANK: name⟧ produces a game view for adversary A by setting the outer-oracle answer on payload  
> `enc(⟦BLANK: z* = y | z* derived⟧) ‖ s ‖ DOMAIN_SEP`  
> to ⟦BLANK: programmed digest / Std-reduction embedding⟧ so that a Pre/SPR/Col win by A is consistent with that planting.  
>
> **Planting (inner, optional for some games).** Seed oracle answers on `m ‖ s` are programmed / simulated so that  
> `int(SHA3_in(m ‖ s)) ∈ ⟦BLANK: Im restriction / free / bound from OL-3⟧`  
> and the T3_ref^L itinerary meets the planted inner target when required.  
>
> **Extraction.** From a game win of A (Pre: (m,s); SPR: distinct pair; Col: colliding pairs), extractor E returns a Π witness  
> `x = ⟦BLANK: int(SHA3_in(m‖s)) | recovered path | residual-legal seed⟧`  
> such that ⟦BLANK: T3_ref^L(x)=y | finalize matches d | Res=1 if OL-4 active⟧.  
>
> **Simulation bookkeeping.** ⟦BLANK: how RO tables are maintained; abort / bad-event set Bad; relation of Bad to ε_hash / ε_C2^(q)⟧.  
>
> **Lemma shape (OPEN — do not fill numerically here).**  
> Under model M, for every A making ≤ q queries in time t_A,  
> `Adv_G^{H}(A) ≤ ⟦BLANK: factor⟧ · Adv_Π(E^A) + ⟦BLANK: ε_hash(M,q)⟧ + ⟦BLANK: ε_C2^(q) if G ∈ {Col,SPR} (OL-7)⟧ + ⟦BLANK: negl(λ) or concrete residual⟧`,  
> with running time of E ≤ ⟦BLANK: poly(λ)·t_A or concrete⟧.  
>
> **Encode / salt framing sub-blank (from [SW] §9 item 3).** ⟦BLANK: min-BE injectivity already structural on disk; salt length framing / DOMAIN_SEP choice — confirm DOMAIN_SEP=`b""` for H_ref or state alternate⟧.

**Explicit Soft SF refusal:** this card does **not** invent an RO programming proof, does **not** assert indifferentiability of the sandwich from a RO, and does **not** assert any collision-transfer lemma beyond what [RPP] R6 already records as structural (state/seed collision ⇒ H collision, same s). R6 is cited as structure only; it is not a completed Crit. 3 reduction.

---

## 3. Card OL-8 — Advantage relation + algorithm R skeleton

**Status:** invent-pending. Expands Crit3 pinboard §4 Adv template into explicit blank fields. **No concrete R is asserted; no factor is asserted as true.**

**On-disk obstruction (cite):** [FG] Criterion 3 unmet; [FG-A] / [SR-A] Close (B) — no Pack+(S) algorithm R and no explicit advantage relation constructible from the written games and written Π; [U1] C1 (no algorithm: inputs, wrap, plant, extract, SHA3 sim unspecified); [RPP] R5 absent.

**Expanded template (every field blank).**

> For each game G ∈ {Pre, SPR, Col} on H_λ (or H_ref if concrete-only) and every adversary A running in time t_A with q oracle queries, there exists an algorithm R = R^A (explicitly given) such that:
>
> **(1) Inputs of R**  
> - Π instance inst = ⟦BLANK: y | (d,s) | residual params P from OL-4⟧  
> - oracle access to A  
> - public parameters ⟦BLANK: λ | (L,n,ℓ)=(539,512,512) concrete⟧  
> - model handles from OL-6 (RO tables / Std reduction auxiliaries) = ⟦BLANK⟧  
>
> **(2) How R wraps A**  
> - Challenger-side setup: ⟦BLANK: sample / plant inst into digest or seed view per OL-6⟧  
> - On each A query to SHA3_in / SHA3_out: ⟦BLANK: simulate / program / forward to Std oracle; maintain consistency with T3_ref^L⟧  
> - On A output: ⟦BLANK: accept/reject as G-win; invoke extractor⟧  
>
> **(3) SHA3 simulation**  
> - Inner call `SHA3-512(m‖s)`: ⟦BLANK: RO program / lazy sample / Std⟧ → seed u_0  
> - Body: u_{i+1} = T3_ref(u_i) for i=0..L−1 with L=⟦BLANK: 539 | L(λ)⟧ (public evaluation; not a hardness step)  
> - Outer call `SHA3-512(enc(u_L)‖s‖DOMAIN_SEP)`: ⟦BLANK: RO program / Std⟧ → digest  
> - Bad events tracked: ⟦BLANK: list; tied to OL-6 Bad and OL-7 C2⟧  
>
> **(4) Extraction**  
> - From G-win of A, R outputs Π witness w = ⟦BLANK: seed x | path | residual certificate⟧  
> - Correctness condition: ⟦BLANK: formal; depends on OL-3 domain and OL-4 Res⟧  
>
> **(5) Running time**  
> - t_R ≤ ⟦BLANK: poly(λ)·(t_A + q·cost(T3_ref^L)) | concrete expression in L,n,q⟧  
>
> **(6) Advantage relation (shape only)**  
> ```
> Adv_G^{H_λ}(A)
>   ≤  ⟦BLANK: poly(λ) | concrete k(q)⟧ · Adv_{Π_λ}(R^A)
>     + ⟦BLANK: ε_hash from OL-6⟧
>     + ⟦BLANK: ε_C2^{(q)} for Col/SPR from OL-7⟧
>     + ⟦BLANK: negl(λ) | concrete residual δ⟧.
> ```  
>
> **(7) Poly/negl vs concrete table**  
> - If OL-5 λ-family is filled: use asymptotic poly/negl form.  
> - If OL-5 remains blank: only a **concrete** table at (L,n,ℓ)=(539,512,512) is well-typed — fields:  
>   | G | k(q) | ε_hash | ε_C2^(q) | δ | t_R bound | ← all ⟦BLANK⟧ |

**Mandatory prerequisites before this template is non-vacuous** (restated from Crit3 §4; still unmet):  
1. Π_λ fully defined (OL-3, OL-4) with separately stated assumption (OL-9) not already trivial on disk.  
2. λ-family (OL-5) **or** concrete-only mode chosen explicitly.  
3. SHA3 model + planting/extraction lemma (OL-6).  
4. Instance-space agreement (OL-10).  
5. Explicit filled R for (1)–(5) above.

**This note does not assert that any concrete R exists.** Filling any blank above with a claimed algorithm or numerical factor would violate invent HOLD and is refused.

---

## 4. Card OL-10 — Instance-space agreement (design-choice card)

**Status:** invent-pending **design choice**. Neither option claims hardness from present data.

**On-disk mismatch (cite):**  
- [U1] C3 / PR5: Π may demand O_res-indexing, fiber membership, or permanent-class evaluations; public games do not; an adversary that wins a public game need not return a residual-legal path.  
- [RPP] §3.2 item 5: “Agreement of instance spaces: the game adversary does not return residual-legal paths, and Π instances have residual predicates; one of the two must change.”  
- Inventory FINDINGS OL-10; Crit3 cards OL-3 / OL-4 leave domain and Res blank.

**Option (A) — Change games to residual-legal wins.**

> Redefine G ∈ {Pre, SPR, Col} so a win additionally requires that the recovered seed/path satisfies Res(·; P)=1 under the OL-4 predicate.  
> **Requires from OL-3 / OL-4:**  
> - OL-4 filled (Res fully defined: ι, fiber membership, permanent-class Boolean, activity flag, what Res restricts).  
> - OL-3 domain D chosen consistently with residual-legal seeds (typically D intersecting whatever Res admits).  
> **Consequences (definitional, not hardness):** public API H_ref does **not** evaluate residuals today ([U1] I10; Crit3 OL-4). Option (A) therefore changes the **written games** relative to Formal_Games Criterion 1, or restricts them to residual-only tracks ([SR] §7). Soft SF does not perform that rewrite here.  
> **Hardness:** **none claimed.** Filling Res does not by itself make Π hard.

**Option (B) — Change Π to unrestricted fixed-round inversion under SHA3 image restriction.**

> Replace residual-constrained Π with a problem Π^♯ whose solutions are seeds x ∈ Im(SHA3-512 ∘ (·‖s)) (or the concrete game-equivalent Π_dig^{SHA3}) with T3_ref^L(x) meeting the target / digest condition, **without** Res.  
> **Requires from OL-3 / OL-4:**  
> - OL-3: choose D = Im(SHA3) (or accept Π_dig^{SHA3}).  
> - OL-4: explicitly **drop** Res (Crit3 OL-4 “Alternative (explicit drop)”) and rename so the object is not called RPP-with-residuals.  
> **Consequences (on-disk, cited — not new):** [RPP] R1: Π_dig^{SHA3} is the preimage game itself (no content beyond the game). [U1] C3: dropping residuals “changes Π into unrestricted fixed-round inversion of Canonical T3. That changed problem is not the written Π,” and free-map easiness facts ([U1] I8/I9; [RPP] §2.4) forbid treating it as hard from present data.  
> **Hardness:** **none claimed.** Option (B) is a definitional alignment move, not a hardness source.

**Author choice blank:** ⟦BLANK: Option (A) | Option (B) | hybrid with named residual-only track⟧. Until chosen and OL-3/OL-4 filled accordingly, Crit. 3 instance spaces remain mismatched.

---

## 5. Context only (no new cards) — OL-7, OL-9, OL-1/OL-2

### 5.1 OL-7 — ε_C2 still blank

Cite Crit3 pinboard Card OL-7: random variable C2 and ε_C2(L,n) := Pr[C2] are **defined as symbols**; target lemma ε_C2(539,512) ≤ ⟦BLANK⟧ remains **OPEN / invent-pending**. Heuristic Rényi figures from [RPP] §3.3 are **not** imported. Direction note unchanged: by [RPP] R6 any mid-fiber term enters a CR reduction as an additive loss, so the needed lemma is an **upper** bound — still unfilled.

### 5.2 OL-9 — Hardness assumption: Soft SF refusal

**Explicit Soft SF refusal to invent a hardness assumption for Π.** invent HOLD stands. Soft SF will not mint an assumption that contradicts or papers over on-disk easiness.

**What on-disk already shows is easy / not established hard** (Owner: these block filling OL-9 from present data):

| Object | Status on disk | Source |
|---|---|---|
| Π_free (x ∈ ℕ, T3_ref^L(x)=y) | **easy, proven** — x = 3^L·y | [RPP] §2.4(1); Crit3 OL-3 table |
| Π_bnd (0 ≤ x < 2^n, n=512, L=539) on hash states | **heuristic/empirical easiness** — best-first 100/100; no poly proof either way | [RPP] §2.4(6) |
| Π_dig (unrestricted x, digest target) | poly-time ≡ SHA3-512 preimage on enc(z)‖s; T3 adds nothing | [RPP] R2 |
| Π_dig^{SHA3} | equals Preimage(H_ref) | [RPP] R1 |
| Π_res | **not statable** until OL-4 filled | [RPP] §2.5; Crit3 OL-4 |
| Free Canonical T3 short trajectories (e.g. 4880→1 in 14 steps) | forbidden as hardness source for Π | [U1] I8, PR7; [FG-A] |
| Packaging COUNT 539 = 18+521 | not a clock / mixing-time theorem | [FG-A]; [SR-A]; FREEZE non-claims |

Any OL-9 fill must be a **separately stated** assumption whose basis is not already trivial on the rows above ([RPP] §3.2 item 2). Soft SF does not supply one.

### 5.3 OL-1 / OL-2 — Formal_Games author confirmation still open

From Crit3 §2: working pin is T3_ref / H_ref (FREEZE Option A / REF). [FG] text for T3 differs from T3_ref on residue 2 ([RPP] §1.2–1.5). Soft SF does not rewrite Formal_Games. **OL-1** (fix T3 text to T3_ref) and **OL-2** (pin one H profile as sole game object) remain **author-confirm open**.

---

## 6. Explicit non-claims

- **No hardness** of any Π variant; no OL-6 lemma proof; no filled ε_C2 bound; no concrete R; no asserted Adv inequality factors.  
- **No security level** for HQH-539-512; no claim beyond what SHA3 alone is generally assumed to give under a still-unwritten composition lemma.  
- **No Shor, Grover, or post-quantum claims** of any kind.  
- **539** is packaging depth (18+521), not a mixing-time or clock theorem.  
- invent HOLD stands; Close (B) of [FG-A]/[SR-A]/[U1] is **cited**, not overturned.  
- Prior FINDINGS hashes unchanged; tip `7cddb188…` untouched; **No CERT**; nothing published, sent, pushed, or spent.  
- Not peer reviewed (Criterion 4 unmet / external).

---

## 7. Status line

Tip 7cddb188 untouched · No CERT · draft-only · invent HOLD stands · nothing pushed, sent, published, or spent · no Soft SF PRESS by this agent.

**Cards issued this note:** OL-6 (composition / programming template), OL-8 (expanded Adv/R blank skeleton), OL-10 (instance-space Option A vs B design card).  

**Context restated, invent-pending unchanged:** OL-7 (ε_C2 blank), OL-9 (hardness assumption refused / easiness table), OL-1/OL-2 (author confirm open).  

**Still invent-pending from prior pinboard (not re-issued):** OL-3, OL-4, OL-5 (definitions remain as in Crit3 cards). OL-11 external peer review.

*End of FINDINGS.*
