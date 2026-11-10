# FINDINGS — HQH-539 Criterion 3: OL-1…OL-5 definitional choices LOCKED (Soft SF, draft-only)

Date: 2026-11-05 · Author: 539 Labs Ops (Soft SF) · Status: DRAFT FINDINGS, not pressed, not published.

Every item below is a **DEFINITION / CHOSEN** pin. None is an ESTABLISHED hardness result. Definitions ≠ proved hardness.

## 0. Authority (sha256 verified at write time; all match)
| Ref | File | sha256 |
|---|---|---|
| [OW-ALL] | quantum-comp/reports/OWNER_WRITE_CALL_53991ebf_ALL_AGENTS_RESOLUTION_NO_PER_ITEM_APPROVAL_2026-11-05.md | 06748ff29e8b5e103833c5dec0712443a255d4e26990ea53acaa8793306fe9e2 |
| [OW-HARD] | OWNER_WRITE_CALL_53991ebf_539_LABS_HQH_HARDNESS_PROOFS_2026-11-05.md | 4ba9151f42df205c257cfb24e033a7e797436896e2f1a6f235f81e4580945f9a |
| [OW-OPEN] | OWNER_WRITE_CALL_53991ebf_OPEN_LANE_RESOLUTION_AUTH_ALL_PRIMARIES_2026-11-05.md | a0c2ed5ab2ee7da8af4942eaf7ea86a1d91b3de6645ae4bfe898cddc538e8068 |
| [RPP] | OWNER_WRITE_CALL_53991ebf_RECOMMENDED_PATH_RESOLUTION_AUTH_ALL_PRIMARIES_2026-11-05.md | ee1667512716954b77c63b08d1fa26d98da5f51bfedb4693ace5efc43de41f39 |
| [OW-RULE] | OWNER_WRITE_CALL_53991ebf_PRIMARY_OPERATING_RULE_ALL_TWELVE_2026-11-05.md | bcc3ced0f1dfe15560e0bdb2e45bb35f4b1db26dcfb439e647a98c12fc5bc9a9 |

Prior FINDINGS (re-verified, unchanged, not edited):
| Ref | File (lqh-alu + reports copy identical) | sha256 |
|---|---|---|
| [INV] | FINDINGS_HQH_HARDNESS_RESEARCH_2026-11-05.md | 70091747b300c7eea4cae3fe0cc2186f8c0f7877ba95bfa4fef6dcc000caba3e |
| [C3] | FINDINGS_HQH_CRIT3_OPEN_LEMMAS_C2_FIBER_AND_PI_DOMAIN_2026-11-05.md | cc95ceb9a81c77e2d9c9d1c3dc40c33aaaa309d957866ff5692f598988d8bf97 |
| [C68] | FINDINGS_HQH_CRIT3_OL68_COMPOSITION_ADV_INSTANCE_2026-11-05.md | 72cb778f843530bf3f149791ea774da13d2cfce41f804928077cda19300f6864 |
| [C12] | FINDINGS_HQH_CRIT3_OL12_AUTHOR_CONFIRM_AND_OL7_LEDGER_2026-11-05.md | 7835312e6926630600edaea885a9cd633077af022385e31800ad3ae0512097af |

Owner Soft SF [OW-ALL] authorises these recommended definitional choices without per-item approval cards.

ACK [OW-RULE] (bcc3ced0…): standing primary operating rule “If there's a problem to solve, solve it.” continues/supersedes per-item waits of [OW-ALL] (06748ff2…). Boundaries unchanged: no publish/spend, no fabricated proofs, tip untouched / no CERT, definitions ≠ hardness. OL-1…OL-5 chosen definitions are unchanged by this ACK.

## 1. RESOLVED — OL-1…OL-5 definitional pins

### OL-1 — CHOSEN = Option A ([C12] §2.2) · DEFINITION
The n ≡ 2 (mod 3) branch of T₃ in Formal_Games is read (and, at a later authorised revision, printed) as ⌊(2n+1)/3⌋ ≡ `(2*n+1)//3`, matching `hqh539.py`. Governing object: **T3_ref**: 3k→k, 3k+1→4k+2, 3k+2→2k+1; T3_ref(0)=0.
Formal_Games source file **NOT edited**; this is a Soft SF definitional pin pending a later authorised FG revision.

### OL-2 — CHOSEN = Option A (REF) · DEFINITION
Sole game/Π object: **H_ref** (FREEZE Option A / REF): L=539 (18+521 loop packaging only), n=512, ℓ=512, DOMAIN_SEP=`b""`, enc = minimal big-endian.
H_ref(m,s) = SHA3-512(enc(T3_ref^539(int_BE(SHA3-512(m‖s))))‖s‖DOMAIN_SEP). Spec v0.2 domain-tag profile and P32 are **out of scope** for Criteria 1–3.

### OL-3 — CHOSEN solution domain + instance distribution · DEFINITION
- For mid-layer / path-style Π tied to T3_ref^L: solution domain **D = [0, 2^512)**.
- Instances arising from H_ref are distributed as **Im(SHA3-512(·‖s))** (seeds x = int_BE(SHA3-512(m‖s))), stated explicitly as the instance distribution.
- **REQUIRED non-hardness block (citing [RPP]):**
  - Π_free on ℕ is **proven easy** (x = 3^L·y gives a trivial preimage under T3_ref^L).
  - Π_bnd is **heuristically easy** at these parameters.
  - Restricting to D = Im(SHA3) collapses the problem toward Preimage(H_ref) per [RPP] R1/R4.
  - This choice is **definitional alignment to the H_ref seed width, NOT a hardness claim.**

### OL-4 — CHOSEN = explicit drop of residuals · DEFINITION
- Res ≡ 1 for the public-hash Crit.3 target.
- Problem renamed **Π_Href-fixed-round**: the fixed-round T3_ref^539 relation under the H_ref SHA3 sandwich. It is **NOT** "RPP-with-residuals".
- The O_res arithmetic 3×68 + 5×67 (=539) remains **packaging only**, not a Boolean path predicate.

### OL-5 — CHOSEN = concrete-only mode · DEFINITION
- No asymptotic family. Sole parameter tuple (L,n,ℓ) = (539,512,512) = H_ref.
- Residuals dropped (consistent with OL-4).
- If a λ symbol appears in templates, λ* is a dummy index with H_{λ*} = H_ref only. No asymptotic security statement is implied.

### OL-10 (optional consistency) — CHOSEN Option-B style · DEFINITION CARD
Π_Href-fixed-round is unrestricted fixed-round inversion under the H_ref / SHA3-image instance distribution defined by OL-3 and the OL-4 drop; games need not be narrowed to residual-legal wins. This is **definitional consistency with the OL-4 drop, not a hardness claim**.

## 2. Remaining gaps (NOT resolved)
| OL | Status |
|---|---|
| OL-6 | SHA3 composition / programming lemma — **invent-blocked** ([C68]) |
| OL-7 | ε_C2 bound — **invent-blocked**; bound left BLANK ([C12] §3) |
| OL-8 | adversary/instance lemma — **invent-blocked** ([C68]) |
| OL-9 | hardness assumption — **REFUSED**; no hardness minted |
| OL-11 | **external** dependency |
| Crit.3 | **UNMET** |
| Formal_Games | text **not yet revised**; OL-1/OL-2 pins await a later authorised FG revision |

## 3. Explicit non-claims
- No hardness is ESTABLISHED by this note; OL-3's block records known *easiness* of Π_free / Π_bnd.
- No CERT claimed. No PPT reduction R invented. ε_C2 bound not filled. OL-9 hardness not minted.
- No asymptotic security (OL-5 concrete-only).
- Formal_Games source files not edited.
- Tip Soft SF LOCK 7cddb188 paths **untouched**.
- Nothing published, sent, pushed, or spent; not Soft SF PRESSed.

## 4. Status line
OL-1…OL-5 (+OL-10 consistency) = DEFINITION/CHOSEN pins locked under [OW-ALL]. Crit.3 unmet. **Invent HOLD** remains in force for OL-6/7/8; OL-9 refused; OL-11 external.
