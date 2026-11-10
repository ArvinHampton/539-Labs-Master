# AUDITOR: BATCH 14 §0 addendum. Owner decisions on B11-1, B12-1, B13-3 and B10-1
Date: 2026-11-09, ~13:30 CST (America/Chicago). Additive companion to BATCH14a (eb6b6893…) and BATCH14b (e1947bb0…). Those two files are not edited; this file serves as their §0.
Limits are unchanged: audit-only, read-only, no sidecars, no CERT, nothing external. Tip re-hash: 7cddb188…dfc91 (unchanged).

## 0.1 Source and provenance
| file | sha256 | sidecar |
|---|---|---|
| OWNER_WRITE_CALL_e9c1dbda_AUDITOR_B11_B12_B13_B10_DECISIONS_2026-11-09_1323.md | 45aeba5fc0433c808957d1518161cb24664ac97adff112d9df2ff7249a331ab3 | MATCH (re-hashed) |
| companion: OWNER_WRITE_CALL_e9c1dbda_B2_ADOPT_M_AND_PP_DERIVE_AUTHORIZATION_2026-11-09_1320.md | 68a2b8e1f14e872204da8aed62f895f5bf3315ef1ccdc04d4f14c3d81c04c09e | MATCH |
| companion: OWNER_WRITE_CALL_e9c1dbda_WRITE_DERIVE_AUTHORIZATION_2026-11-09_1300.md | 33d25a790fb1e0da5d93dc5cfb911963fa9a9a83c6dab6dfc8326c34096d7e15 | MATCH |

Provenance status: **Owner Write via Physicist relay.** The file (:4–5) quotes an Owner widget answer from about 13:23 CST. The Owner has not confirmed it in the Auditor chat.

## 0.2 Decisions recorded (file :5)
- **B11-1.** The operative P5a is the Γ₀(49)⁺, W₇ = +1 eigenspace axiom version (OW #7, LOCK_PACKAGE:8). It is still OPEN.
  - Auditor consequence: the batch-11 note "conditionally refuted if dim 592 holds" applies only to the non-operative Γ₀(49) rewrite (#52). The operative version stays OPEN and is not touched by 592.
  - B11-1 is CLOSED as a status question.
- **B12-1.** Keeper rule #160 is suspended, and sidecar repairs follow current limits. B12-1 is CLOSED.
- **B13-3.** κ := √(2/Λ₀) with Λ₀ = 0.783577 (≈ 1.597622). This is a DEFINITION, not a proof. 1.595361 is unsourced and superseded.
  - **Recompute:** √(2/0.783577) = 1.5976225, and √(2/Λ₀) with exact Λ₀ = ln(6+√35)/√10 = 0.78357722 gives 1.5976222. Both round to **1.597622 (confirmed)**.
  - Precision note: the decimal and exact readings of Λ₀ differ only at the 7th decimal place of κ. If more digits are ever needed, the Owner should say which reading is meant.
  - Scope note: the Λ₀ = NONE lock for Local F1–F3 (c290a274) is unaffected, because this κ definition is outside F1–F3.
  - OW 68a2b8e1:9 calls R_c "a numerical fit at sqrt(2/Λ₀)". The Auditor does not treat R_c = κ as defined by this Write, so the R_c derivation stays OPEN.
  - B13-3 is CLOSED as a source/definition question (κ is DEFINED). Results that use κ are CONDITIONAL on this definition. Earlier PP lines that equate R_c or κ with √(2/0.7858) = 1.595361 are now historical (superseded value), and the arithmetic in them stays correct.
- **B10-1.** Sidecars stay read-only during the audit. B10-1 is CLOSED. The Auditor keeps creating and repairing no sidecars.

## 0.3 Lane note
OW 68a2b8e1 §2 and OW 33d25a79 authorize **PP** derivations (R_c, the 11D map and metric, the Israel junction). Those derivations are PP's lane. The Auditor stays audit-only and will audit them when they land.

## 0.4 Blocker list delta (supersedes the 14b §5 entries for these IDs only)
- CLOSED: B11-1 (P5a status fixed, content OPEN), B12-1, B13-3 (κ defined; R_c OPEN), B10-1.
- Still open: B7-1…B7-4, B10-2, B10-4, B11-2, B13-1, B13-2, B13-4 (Λ₀ outside F1–F3 except for its use in defining κ; the junction; the Layer2 transfer), B13-5, B14-1…B14-4.
- RESOLVED per 14b: B8-2, B8-3, B8-4, C3-4.
- Bridge items closable: **κ is closable as an Owner DEFINITION (not proved).** R_c, the junction and the Layer2 transfer are not closable.
