# FINDINGS — HQH-539 Criterion 3 open lemmas: Π domain, residual predicate, λ-family, C2 mid-fiber (definitional pinboard)

**Date:** 2026-11-05 (America/Chicago) · **Status:** DRAFT-ONLY · Soft SF follow-on · **No CERT** · not peer reviewed
**Scope:** definitions and blanks only. No proofs, no hardness, no probability bounds asserted as theorems. No Shor/Grover/post-quantum claims.

## 1. ACK / lineage

- Continues **OW 4ba9151f…** (hardness research). Draft-only; nothing published, sent, pushed, or spent.
- Prior FINDINGS (not edited): `/workspace/539-labs/lqh-alu/FINDINGS_HQH_HARDNESS_RESEARCH_2026-11-05.md`, sha256 `70091747b300c7eea4cae3fe0cc2186f8c0f7877ba95bfa4fef6dcc000caba3e` (re-verified at write time). OL numbering (OL-1…OL-11) is taken from its §4.2; this note executes its §"next" items 1–3.
- **Tip 7cddb188 untouched.** No git operations performed.

### Sources read (sha256 at write time)

| Short | Path | sha256 |
|---|---|---|
| [SW] | `quantum-comp/oct17-master/docs/hqh539-verification/Architecture_SHA3_Sandwich.md` | `fdad074d…a09d49ab` |
| [FG] | `quantum-comp/oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/HQH539_Formal_Games_and_Hard_Problem_Pi.md` | `03865621…3a64dde8` |
| [FG-A] | same dir, `HQH539_Formal_Games_Addendum_2026-09-14.md` | `4d3a168d…b2f9860c` |
| [SR] | same dir, `HQH539_Security_Reductions_Exploration.md` (+ Addendum 2026-09-14) | `9f3a6a74…5ab05b` |
| [RPP] | `quantum-comp/reports/crypto/RPP_formal_statement/RPP_formal_statement.md` | `173c2c66…77dac` |
| [REF] | `quantum-comp/oct17-master/docs/hqh539-verification/hqh539.py` | `fef5fce5…8115dd` |
| [FREEZE] | same dir, `FREEZE_LOCK_Canonical_4q2_SHA3_2026-08-02.md` | `3d60ee3c…1022` |

## 2. Pinned primary object for all Criterion-3 work (OL-1 / OL-2 pin, as read from FREEZE + REF)

This is a **pin of what the code computes**, not a rewrite of [FG]. All cards below use only this object; spec v0.2 domain-tag and P32 profiles are **out of scope** for Crit. 3 primary work.

**T3_ref : ℕ → ℕ** ([REF] `T3`, [FREEZE] §2, [RPP] §1.3):
- n = 3q → q
- n = 3q+1 → (4n+2)/3 = 4q+2 (exact)  — Canonical "4q+2" branch
- n = 3q+2 → ⌊(2n+1)/3⌋ = 2q+1

**H_ref (Option A / REF, ACCEPTED in FREEZE):** for message m, salt s (bytes):
1. x := int_be(SHA3-512(m ‖ s)) ∈ [0, 2^512)
2. z := T3_ref^L(x), L = 539 (loop packaged 18 + 521; packaging only, same map 539 times)
3. d := SHA3-512(enc(z) ‖ s ‖ DOMAIN_SEP), enc = minimal big-endian bytes, DOMAIN_SEP = b"" ([REF] line 16)

Constants: L = 539, seed width n = 512, digest width 512. [FG] text for T3 differs from T3_ref on residue 2 (RPP §1.2–1.5); OL-1 author confirmation remains open — this pin does not close it, it only fixes the object Soft SF uses.

## 3. NEEDS-DEFINITION cards

Notation: `⟦BLANK: …⟧` = author must supply; nothing in a blank is asserted. "On-disk" = existing sketch cited, not imported as proof.

### Card OL-3 — Solution domain of Π

**Proposed statement template.**
> Π_⟦D⟧(inst): Instance ⟦BLANK: y ∈ ℕ | digest d ∈ {0,1}^512 with salt s⟧. Solution x ∈ **D** with ⟦BLANK: T3_ref^L(x) = y | SHA3-512(enc(T3_ref^L(x))‖s) = d⟧ ∧ ⟦BLANK: residual predicate Res, see OL-4, or "none"⟧.
> D ∈ { ℕ (free) | [0, 2^n) (bounded) | Im(SHA3-512 ∘ (·‖s)) (SHA3-image) } — ⟦BLANK: author choice⟧.

**On-disk consequences per candidate (cited, not new):**
| D | Recorded status | Source |
|---|---|---|
| ℕ | trivially solvable: x = 3^L·y (proven on disk) | [RPP] §2.4(1); [FG-A] |
| [0,2^512) | heuristic/empirical easiness at hash parameters (best-first 100/100); no proof either way | [RPP] §2.4(6) — labeled heuristic |
| Im(SHA3) | equals Preimage(H_ref) itself; no content beyond the game | [RPP] R1, R4 |
| Π_dig, D = ℕ | equivalent to SHA3-512 preimage on enc(z)‖s; T3 layer adds nothing | [RPP] R2 |

**Status:** NEEDS-DEFINITION. No candidate is asserted hard here.

### Card OL-4 — Residual path predicate

**Proposed statement template.**
> Res : (u_0,…,u_L; P) → {0,1}, where P = (O_res, block partition 3×68 + 5×67, ⟦BLANK: permanent class [α⊗δf] or none⟧, ⟦BLANK: activity flag⟧).
> Required sub-definitions: (a) ⟦BLANK: map ι from step index i and/or value u_i to O_res label⟧; (b) ⟦BLANK: fiber-membership rule, map to block id ∈ {0..7}⟧; (c) ⟦BLANK: permanent-class evaluation as a Boolean of the path⟧; (d) ⟦BLANK: who sets "active" — public param / per instance⟧; (e) ⟦BLANK: does Res restrict seeds, orbits, or digests⟧.
> **Alternative (explicit drop):** declare Res ≡ 1 for the public-hash reduction target and rename the problem ⟦BLANK: name⟧ so it is not called RPP-with-residuals.

**On-disk:** [FG] §Π search task (residual constraints "when active"); [RPP] §2.5 items 1–4 (none defined); U1 I10: H_ref does not evaluate residuals; [SR] §7 residual-only tracks. Arithmetic 3·68+5·67 = 539 fixes block sizes only.
**Status:** NEEDS-DEFINITION. Until filled, Π_res is not statable; no sparsity/density statement is made.

### Card OL-5 — λ-family

**Proposed statement template.**
> Family {H_λ}_{λ∈ℕ}: L(λ) = ⟦BLANK⟧, seed width n(λ) = ⟦BLANK⟧, digest width ℓ(λ) = ⟦BLANK⟧, salt length bound ⟦BLANK⟧, inner/outer hash H_in(λ), H_out(λ) = ⟦BLANK: SHA3 variant or RO of output ℓ(λ)⟧, residual parameters P(λ) = ⟦BLANK: how 539 / 68 / 67 scale, or "fixed, residuals dropped"⟧.
> Consistency requirement: H_{λ*} = H_ref at ⟦BLANK: λ*⟧ with (L, n, ℓ) = (539, 512, 512).

**On-disk:** [RPP] §2.2 item 6, §3.2(1); [RPP] §3.3(4) records (heuristic) that L has quantitative effect on state size — so L(λ) is not a free label.
**Status:** NEEDS-DEFINITION. Without it, "poly" and "negl" in §4 are not well-typed; only a concrete (fixed-parameter) table form could be used.

### Card OL-7 — C2 mid-fiber collision under Im(SHA3)

**Definition (random variable only; no bound asserted).**
> Let U, U′ be ⟦BLANK: independent uniform on {0,1}^512 | RO outputs on distinct inputs (m‖s) ≠ (m′‖s′)⟧, viewed as integers. Define the event
> C2 := [ U ≠ U′ ∧ T3_ref^L(U) = T3_ref^L(U′) ], and ε_C2(L, n) := Pr[C2].
> Equivalently ε_C2 = Σ_z p_z² − 2^{-n}, with p_z := Pr_U[T3_ref^L(U) = z] (collision probability of the 539-step state minus the trivial diagonal term).
> Multi-query form for a q-query adversary: ε_C2^{(q)} := Pr[∃ i<j ≤ q: C2 for (U_i, U_j)] ≤ ⟦BLANK: bound, e.g. C(q,2)·ε_C2 by union — only valid once ε_C2 is defined/bounded⟧.
> Target lemma (OPEN): ε_C2(539, 512) ≤ ⟦BLANK: function, with proof⟧.

**On-disk:** [SW] §5 (C2 attack surface), §9 item 2 ("bound on probability that two independent RO outputs fall in the same T^539 fiber"); [RPP] R6 (proven: any state collision ⇒ H collision, same s); [RPP] §3.3(3) Rényi model R₂ — **heuristic, model-extrapolated from n ≤ 48; not imported**. Constructive fibers: `Architecture_Collision_4q2.md` §3.
**Status:** invent-pending. The blank is not filled. Note for the author: by R6 any mid-fiber term enters a CR reduction as an *additive loss*, so the direction of the needed lemma is an **upper** bound on ε_C2.

### (Context, no new card) OL-6, OL-8, OL-9, OL-10
Remain invent-pending exactly as in prior FINDINGS §4.2. OL-6 (SHA3 programming/composition lemma) is referenced as a blank in §4. Not addressed further here.

## 4. Criterion-3 Adv relation skeleton (template only)

What would **count** as a Crit. 3 relation — a shape, not a claim that any R exists:

> For each game G ∈ {Pre, SPR, Col} on H_λ and every adversary A running in time t_A with q oracle queries, there exists an algorithm R = R^A (explicitly given) with running time t_R ≤ ⟦BLANK: poly(λ)·t_A or concrete⟧ such that
> **Adv_G^{H_λ}(A) ≤ ⟦BLANK: poly(λ) or concrete factor k(q)⟧ · Adv_{Π_λ}(R^A) + ⟦BLANK: ε_hash (SHA3/RO term, OL-6)⟧ + ⟦BLANK: ε_C2^{(q)} for Col/SPR (OL-7)⟧ + negl(λ).**

Mandatory components before the template is non-vacuous:
1. Π_λ fully defined (OL-3, OL-4) with a separately stated assumption (OL-9) not already trivial on disk.
2. λ-family (OL-5).
3. SHA3 model and planting/extraction lemma (OL-6): how R embeds a Π instance into A's view and extracts a Π witness from A's output.
4. Instance-space agreement (OL-10).
5. Explicit R: inputs, oracle simulation, extraction, running time.

Known obstruction on disk: [FG-A] "No Pack+(S) algorithm R and no explicit advantage relation are constructible from the written games and written Pi"; [RPP] R3–R5. **This note does not assert that any concrete R exists.**

## 5. Explicit non-claims

- No hardness of any Π variant is claimed; no proof of any OL is supplied.
- No value or bound for ε_C2 is claimed; heuristic Rényi figures (≈2^70 / 2^140) are **not** imported as results.
- No reduction R and no advantage relation is claimed to exist.
- No security level for HQH-539-512; no collision/preimage-resistance claim beyond what SHA3 alone is generally assumed to give.
- No Shor, Grover, or post-quantum claims of any kind.
- 539 is packaging depth, not a mixing-time or clock theorem.
- The §2 pin does not edit [FG]; OL-1/OL-2 author confirmation remains open.
- Not peer reviewed (Criterion 4 unmet).

## 6. Status line

Tip 7cddb188 untouched · No CERT · draft-only · nothing pushed, sent, published, or spent.

**Cards issued:** OL-3 (Π domain), OL-4 (residual predicate), OL-5 (λ-family), OL-7 (C2 mid-fiber under Im(SHA3)); §2 pins the OL-1/OL-2 working object; §4 template touches OL-6/OL-8 only as blanks.
