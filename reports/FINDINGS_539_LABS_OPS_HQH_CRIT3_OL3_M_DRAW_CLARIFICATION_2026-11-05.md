# FINDINGS AMEND — HQH Crit.3 OL-3 m-draw / D vs Im(SHA3) clarification (Soft SF, draft-only)

Date: 2026-11-05 ~13:36 CST America/Chicago · Author: 539 Labs Ops (Soft SF) · Status: DRAFT FINDINGS — **executor Soft SF not PRESSed** (this draft agent did not PRESS); parent Soft SF PRESS may occur separately. Not published. (Edited in place ~13:36 CST to absorb PP OL-8 CONFIRM N1.)

**AMENDS (does not edit)** prior [C15] `FINDINGS_HQH_CRIT3_OL15_DEFINITIONAL_CHOICES_2026-11-05.md` sha `85ef70db16dad3b005b4a50f2ebbfe90122566c7e6f05c46e766831549ec410f` (lqh-alu + reports copy identical; re-hashed this turn). Responds to Professor Proof Soft SF CONFIRM `4c8a378a2a9aeb3c44488266139a829f1d9ce4943404e22ac650db57e1c2cd12` notes N1/N2 on [C15], and absorbs PP Soft SF OL-8 CONFIRM `1a2d914af4f9858d50f17d12c6c940f5af8da05442a8cd2f63f164a93b330ed8` note N1 (near-circular Pre→Π). **OL-1…OL-5 CHOSEN pins unchanged.** Definitional clarification only. Definitions ≠ proved hardness.

## 0. Authority (sha256 verified at write time; all MATCH)
| Ref | File | sha256 |
|---|---|---|
| [OW-ALL] | OWNER_WRITE_CALL_53991ebf_ALL_AGENTS_RESOLUTION_NO_PER_ITEM_APPROVAL_2026-11-05.md | 06748ff29e8b5e103833c5dec0712443a255d4e26990ea53acaa8793306fe9e2 |
| [OW-RULE] | OWNER_WRITE_CALL_53991ebf_PRIMARY_OPERATING_RULE_ALL_TWELVE_2026-11-05.md | bcc3ced0f1dfe15560e0bdb2e45bb35f4b1db26dcfb439e647a98c12fc5bc9a9 |
| [OW-HARD] | OWNER_WRITE_CALL_53991ebf_539_LABS_HQH_HARDNESS_PROOFS_2026-11-05.md | 4ba9151f42df205c257cfb24e033a7e797436896e2f1a6f235f81e4580945f9a |
| [C15] | FINDINGS_HQH_CRIT3_OL15_DEFINITIONAL_CHOICES_2026-11-05.md | 85ef70db16dad3b005b4a50f2ebbfe90122566c7e6f05c46e766831549ec410f |
| [PP-OL15] | FINDINGS_PP_SOFTSF_AUDIT_539_OL15_DEFINITIONAL_CHOICES_85ef70db_2026-11-05.md | 4c8a378a2a9aeb3c44488266139a829f1d9ce4943404e22ac650db57e1c2cd12 |
| [PP-OL8] | FINDINGS_PP_SOFTSF_AUDIT_539_OL8_FRAMING_OL11_OUTLINE_07521fa9_2026-11-05.md | 1a2d914af4f9858d50f17d12c6c940f5af8da05442a8cd2f63f164a93b330ed8 |

tip Soft SF LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` — tip_touched **NO**. Formal_Games **not edited**. No CERT. No R / ε / hardness invented.

## 1. OL-3 / H_ref — m-draw and D vs Im(SHA3) (DEFINITION only; pins unchanged)

1. **Message draw.** Message `m` is drawn from the **public message space of the games** (byte-strings). Salt `s` is drawn / fixed **per game rules** (unchanged from Formal_Games / H_ref game statements).
2. **Seed.** Seed `x := int_BE(SHA3-512(m ‖ s)) ∈ Im(SHA3-512(·‖s)) ⊆ [0, 2^512)`.
3. **CHOSEN solution domain.** `D = [0, 2^512)` remains the ambient search space for mid-layer / fixed-round `Π_Href-fixed-round` solutions and is **strictly larger** than `Im(SHA3-512)`. Legal H_ref seeds live in the image.
4. **Instance distribution vs search.** For H_ref-originated instances, the instance distribution is the image `Im(SHA3-512(·‖s))` (push-forward of the public `(m,s)` draw through SHA3-512 ‖ int_BE). Searching `D \ Im(SHA3)` is allowed by the CHOSEN ambient `D` but is **outside the H_ref seed support**. This is **not a hardness claim either way** (easiness of Π_free / Π_bnd and the non-hardness block of [C15] §OL-3 stand unchanged).

OL-1, OL-2, OL-3 CHOSEN `D`, OL-4, OL-5, OL-10 consistency pins of [C15] are **not revised** — only clarified as above.

## 1b. DEFINITION / NON-HARDNESS — OL-3 collapse ⇒ Pre→Π near-circular ([PP-OL8] N1)

**Explicit statement (definitional / non-hardness only; no R filled):** If the solution domain and/or instance support for `Π_Href-fixed-round` is restricted to `Im(SHA3-512(·‖s))`, then — citing [C15] §OL-3 non-hardness block and [RPP] R1/R4 — that Π **collapses toward Preimage(H_ref)** (equivalently, toward the Pre game on H_ref). Therefore a reduction from Pre (or the Pre game) to that Im-restricted Π is **near-circular** (Pre → essentially-Pre) and **must not be read as hardness evidence**. Any later filled Adv / R / ε bound that depends on such a reduction is likewise **not** hardness evidence under that restriction. Adv blanks on the OL-8 concrete-only template remain ⟦BLANK⟧ under invent HOLD; this note fills none of them and invents no R, ε, or OL-9 hardness.

## 2. N2 hygiene — Soft SF draft headers

Prior [C15] header said "not pressed" while a parent Soft SF PRESS of that draft later occurred. Clarification for Soft SF draft headers going forward:

- **"executor Soft SF not PRESSed"** / **"this draft agent did not PRESS"** means only that the drafting Soft SF agent did not Soft SF PRESS the note.
- A **parent Soft SF PRESS** (e.g. Ops parent → Physicist / PP / Auditor) may occur separately and does not contradict the executor draft-header.
- Prefer that wording over bare "not pressed" when the parent may PRESS.

This note: **executor Soft SF not PRESSed**; parent Soft SF PRESS not performed by this agent and not requested here.

## 3. Explicit non-claims
- No hardness ESTABLISHED; no PPT reduction R; no ε bound filled; OL-9 still refused; Crit.3 still UNMET.
- OL-1…OL-5 CHOSEN pins of [C15] unchanged; Formal_Games source **not edited**.
- Tip Soft SF LOCK `7cddb188…` **untouched**. No CERT.
- Nothing published, sent, pushed, or spent. Soft SF PRESS **not** performed by this executor.
- Near-circular Pre→Π under Im(SHA3) restriction is recorded as a **non-hardness** hygiene note, not a proved easiness theorem beyond [C15]'s existing Π_free / Π_bnd / collapse block.

## 4. Status line
[C15] CONFIRM with N1/N2 notes absorbed as definitional clarification; [PP-OL8] N1 absorbed as explicit Pre→Π near-circular NON-HARDNESS under OL-3 collapse. OL-3 pins stand; m-draw and D ⊃ Im(SHA3) stated explicitly. Adv blanks remain blank. Invent HOLD for OL-6/7/8 remains.
