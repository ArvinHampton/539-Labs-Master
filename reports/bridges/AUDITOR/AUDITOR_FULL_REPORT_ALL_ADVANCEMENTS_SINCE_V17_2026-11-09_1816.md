# AUDITOR — Full report: all advancements since RTA v17 — 2026-11-09 18:16

Role: Auditor, the audit-only keeper. Written Mon 2026-11-09 ~18:30 CST (America/Chicago). Created exclusively with noclobber, with a .sha256 sidecar and a PDF rendering.
Governing direction: OW **c7795d6e88d5da7662d3a562f2564313ad472e0cb5560ce684cb067c61acd2b7** (OWNER_WRITE_VOICE_11fd320e_AUDITOR_FULL_REPORT_ALL_ADVANCEMENTS_SINCE_V17_2026-11-09_1816.md, sidecar MATCH, 18:16 CST), plus the voice amendment relayed by Physicist that the report also be rendered as one PDF.
Scope:
- Local Path: Bridge C, A1→Ξ→RTA.
- Non Local Path: EH 11D, reverse-parity PT, non-local QM.
- The Auditor's full-corpus audit.
All three point toward RTA and the geometric bridge in S²-11DM²ET-X.
Read-only throughout. No existing file was edited, moved or deleted, and the v16 and v17 records are untouched. No CERT, no Gemini, nothing sent outside.
Labels used: **PROVED / CONDITIONAL / OPEN / REFUTED**, plus PENDING where a record says so. Owner **DEFINITIONS** and decisions are not proofs. Pasted or Gemini-style text is not an Owner decision unless the Owner adopted it in their own words.
Every file cited below was re-hashed this turn. An 8-hex prefix in the text stands for the full sha256 given in the ledger (§3) or in the earlier reports.

---

## 0. Executive summary (plain language)
- **Baseline.** The RTA v17 DRAFT (2026-11-05 20:37 CST) has 156 pages and 74 printed Theorems; both counts were verified this turn with poppler (§1). Its old sidecar still disagrees with the PDF (custody item C17-1). A new dated sidecar written at 15:14 matches the PDF, but the cause of the old value is still unexplained.
- **Vacuum: an 11D background is now adopted, as a working choice.**
  1. The first proposal (D), AdS₅×S⁴×Σ_g (7708ec5d), was shown BF-unstable and dropped (822cecb2).
  2. Three supersymmetric twisted vacua were compared: MN N=2, MN N=1 and BBBW (z = ±2, ±3).
  3. After two holds (aaadb280, 587eca0c), MR2's full-11D file and PP's gate audit (384096a8) found no mathematical blocker.
  4. At 18:06 the Owner lifted the hold and **adopted MN N=2 as CONDITIONAL** (19a88b19). It is a working vacuum, not a proved one.
  5. Γ = **Bolza** (genus 2) was adopted for Σ (7ff8299d). Its systole, 2 arccosh(1+√2), is PROVED (computer-assisted).
- **Geometry definitions now on record (Owner DEFINITIONS, not proofs):**
  - brane = a stack of wrapped M5-branes, and face = the 10D matching hypersurface (f283cffd);
  - the face is a ℤ₂ fixed plane, a Hořava–Witten-type wall (f825dfff);
  - Ξ names the curve 49a1⊗χ₁₄₀ (f283cffd, refined by 7b5a725b);
  - Λ₀ and R_c := κℓ_P (5a6e7177);
  - P_rev = T1 and G = ½T^(EH) (2d1e877e).
- **O1 (the ℤ₂ parity of G₄) is resolved as ODD by an audited derivation**, given the fixed-plane premise and premise P-b (PP 544fc7b0, 1bd92da7; OW f825dfff). Even parity on a fixed plane is REFUTED. The pasted parity-flip argument (record fe8bcb00) was **not adopted**, and its claim is REFUTED.
- **The junction is still UNSOLVED.**
  - Pure-M5 and E₈-wall sources cannot close it. The fibre-NEC no-go is PROVED at the end faces and CONDITIONAL in the interior.
  - A count gap N_req/(2N_flux) ∈ (1.255, 1.667) remains. It is CONDITIONAL, and BPS instantons leave it unchanged.
  - The HW wall's tr R² term (Y16) has the right sign, but only at O(1/N), so the leading-order verdict does not change. NL derived this; PP has not yet audited it.
  - Non-BPS E₈ existence (Y14) and the fibre equations with traceless stress (Y15) are OPEN and in progress.
- **MR2's wall curvature (bd47ff5e).** The bulk next to the wall is bounded. In the thin-wall limit the quadratic invariants diverge as 1/ε², but they stay inside the EFT for any wall at least Planck-thick (CONDITIONAL).
- **Citation scope was widened twice** (3f160803, then 36683379). Any source may now be cited, provided its math is verified. A citation alone never makes a result PROVED.
- **Still neutral by Owner order:** the joint carrier, R_c's physical role, DP-a, Layer2 and any baseline (5f59e33e, amended only by f283cffd).
- **Still OPEN:** P5a (literal text does not type-check; its reading and referent are unanswered) and b.
- **Bridge C is PARTIAL.** Local has new evidence logs, but no Local FINDINGS file has been filed since 15:20.
- **RTA v18.** A **safe outline** exists (e18d8fea, 16:52). It holds algebra and definitions only and is not a draft. Earlier blockers 1 (vacuum) is now resolved as CONDITIONAL. Blocker 2 (junction) still stands, so the geometric v18 is still blocked (§7).

## 1. Version-17 baseline (stated first)
| item | value | how verified |
|---|---|---|
| Path | reports/papers/RTA_FOUNDATION_BOUND_v17_DRAFT_2026-11-05_2037CST/RTA_FOUNDATION_BOUND_v17_DRAFT.pdf | on disk |
| Written | 2026-11-05 ~20:37 CST (NOTES_v17.md); PDF CreationDate Thu Nov 5 20:46:59 2026 CST | NOTES_v17.md; pdfinfo |
| sha256 | 9b407e1b0805b2129ce95665b8c2343f9b7ccaa564126277c41b545bfff9d285 | re-hashed |
| Pages | **156** | **VERIFIED**, pdfinfo |
| Printed Theorems | **74** | **VERIFIED**: pdftotext, distinct "Theorem N.M" labels at line start = 74. This matches audit_theorem_count_2026-11-05/AUDIT_SUMMARY.md and v17_all_printed_theorems_74.csv (74 rows). |
| Old sidecar .pdf.sha256 | ee88d1cd57892bafff707e53517df30b81192a5988938ea6159d2dd78733763a | **MISMATCH** (C17-1), unchanged |
| New sidecar .pdf.CURRENT_2026-11-09_1514.sha256 (file sha 4ccbbb56…) | content 9b407e1b… | **MATCH**. Per OW ec97f45e (t4294): "empirical update; the cause of the old ee88d1cd is UNEXPLAINED. Old sidecar and PDF unchanged." Note file SIDECAR_NOTE_C17-1_2026-11-09_1514.md has sha 5dd223cf…. |
| v17 content | v16 spine + post-v16 ledger + boundary rank G = C₂×C₄×C₆ + withdrawn appendix E | NOTES_v17.md |
| v16 (frozen) | papers/RTA_FOUNDATION_BOUND/RTA_FOUNDATION_BOUND_v16.pdf, 1fe7b8a2e245e90009c41726db13518b4c752e99ba4e08b4ffd006d8a73c3297 | **MATCH** with its sidecar |

## 2. Earlier Auditor reports this builds on (re-hashed, MATCH)
- AUDITOR_ADVANCEMENTS_SINCE_RTA_V17_REPORT_2026-11-09.md: 3c2c8fdb34f8b8cef4f133a331f60e5842c72ce65a7d9f702db752014018f811. Covers 12:30–15:05.
- AUDITOR_RTA_V18_READINESS_RECOMMENDATION_2026-11-09.md: 59da91863535b94bdcdd74b6bf103745efab15d270e4615d6e518b3bd4b4aea8 (sidecar MATCH). Covers 15:05–16:48.
- Full corpus audit (Auditor's lane): batches 01–23 (12:38–13:56 CST; 36 records with zero hash drift), errata ff9e4da9 (κ/Λ₀/3^539; 208 files, 606 line hits), crosscheck 034605bf (Artin v1 line 14b REFUTED; W₄₉(f⊗χ₋₇) = −1) and final summary 0504d5d7 (corpus of 36,250 files / 22,035 unique; no tampering).

## 3. Chronological ledger (file time CST; full sha256; SC = sidecar check)
OW = Owner write, recorded by Physicist. Owner decisions came through the Physicist relay and were not confirmed in the Auditor chat. "rec only" marks a record that was **not adopted**.

### 3a. 12:30–15:05 (details in 3c2c8fdb)
| time | record | sha256 | SC | what / status |
|---|---|---|---|---|
| 12:30–12:54 | PP / Local / NL Soft SF audits (Ξ–Fricke–Γ₀(49), SO₄₈ v=23, P_rev/T^(EH) defs), Gemini question set and Physicist's Gemini check | see 3c2c8fdb §3 | MATCH (Gemini question set: no SC) | Gemini answers are **not Owner decisions** |
| 13:00 | OW write/derive authorization | 33d25a790fb1e0da5d93dc5cfb911963fa9a9a83c6dab6dfc8326c34096d7e15 | MATCH | grant |
| 13:20 | OW B2 (B)-M + PP derive | 68a2b8e1f14e872204da8aed62f895f5bf3315ef1ccdc04d4f14c3d81c04c09e | MATCH | B2 **CONDITIONAL** on (B)-M |
| 13:23 | OW B11/B12/B13/B10 | 45aeba5fc0433c808957d1518161cb24664ac97adff112d9df2ff7249a331ab3 | MATCH | κ := √(2/Λ₀), Λ₀ = 0.783577 **DEFINITION**; P5a OPEN |
| 13:28–13:57 | PP derive R_c / 11D map / metric / Israel / AdS₅×S⁴×Σ_g params | 9ea1a7ad…, 9dde377d…, 4d07bd1b…, 52acc3d7…, 4660b73e… | MATCH | EH flux lock REFUTED; R_c OPEN |
| 13:40 | OW C15-3 | 63deb8505bb1f53b4ad04c87b5a1824afda8b7526eb3322ab9f65511432f09b1 | MATCH | κ supersedes Λ₀ ≈ 0.7858 |
| 13:41 | OW B16-1 | 0deba43db59d11d8c725eb5c643129f4be33be42d06931c3dae594abd6fc81ca | MATCH | **SUPERSEDED** by c4c0f1c0 |
| 13:42 | OW B18-1 | c4c0f1c0318691c045b136c01c4de7eb86690ae9c8db4d20b07939a6fd8b24ed | MATCH | W₇ = +1 on 7.4.a.a; **Path C stands** |
| 13:51 | OW F4 / errata / (D) | 7708ec5d1518e371540f7b37a51db1c014e36563c458181cf692b50124a0edd7 | MATCH | (D) adopted CONDITIONAL; replaced at 16:09 |
| 13:58 | Ops F4 FINDINGS | d73cc7b1b9661cc3ced4255e02aba85fad64774e29091947aabab7b644913ee7 | MATCH | parity + 3-bit status, exhaustive at 8 trits |
| 13:58 / 14:04 | Physicist Artin v1 / v2 | 65b367ef88cce23047c70ec0146bfb457c1274af2a3906f573d9a73d19b4b5b9 / ccb568287c9f08c5f976249a5ddf14b710efbeb36b7daf48ef2f9c0a01b826c0 | MATCH | v2 fixes line 14b; not adopted |
| 13:59–14:03 | Auditor errata / crosscheck / final summary | ff9e4da9… / 034605bf… / 0504d5d7… | Auditor files (no SC by rule B10-1) | see §2 |
| 14:02 | OW Ops HW sprint | adf7d966d233a74b900272bf3ff3227198945787261b66a738d4f5259b636077 | MATCH | Gemini's PCIe / dual-rail / "ALL STOPS LIFTED" **not adopted** |
| 14:05 | PP derive twist 7.4.a.a⊗χ₋₇ | 90c1e058c6c7d2051b860c8f48b60ffe44265a6d2dd75288bf22108c2a67e63f | MATCH | W₄₉ = −1, so not a P5a referent (PROVED) |
| 14:08 | OW P5a level-49 referent | e494873929ae6a499578a52e11e5c5bb18f1b40d14f7af2d9a42b9c78fe6004b | MATCH | referent g₀ (2,7,7), Fricke +1; P5a OPEN |
| 14:34 | Ops HW sprint FINDINGS | 2c3e5c18b6b48377b0f4a89a1ad77a3655411ce40d4c4215def2fceb30fe1172 | MATCH | 16-cycle design; formal only for N ≤ 32 |
| 14:54 | OW R1 overflow rule | 6b8822d2c09748f6545efbd4223de0a3e73f718c9a49907bd078103c5dfb28b7 | MATCH | R1 adopted; sprint files only |
| 15:01 | OW P5a ρ̄ | ea2cc9e6b41cde91844b4f2217d98694a8307df96a3a89bdd35d6eb291e46911 | MATCH | ρ̄ = reducible mod-7 reduction of ρ_f; P5a OPEN |

### 3b. 15:05–16:48 (details in 59da9186)
| time | record | sha256 | SC | what / status |
|---|---|---|---|---|
| 15:05 | PP record P5a referent adoption | 05e1c40c4f14e6aace7d081b5649579615388f125cdb22827e031e6f92822872 | MATCH | P5a OPEN |
| 15:07 | **PP derive P5a ρ̄** | 7929ffe6535a79dff41ef6a8f6ca106566d29256b12fc56336ca63d8507d4b1d | MATCH | 11 PROVED / 6 COND / 3 OPEN / 0 REF; e1: literal P5a text does **not type-check** (OPEN); e2/e3: vanishing REFUTED under PP readings I1/I2 (counted CONDITIONAL) |
| 15:11 | **OW blueprint (corrected)** | 5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c | MATCH | **DEFINITIONS** Λ₀ := ln(6+√35)/√10, R_c := κℓ_P; DP-Rc not adopted; Local/NL go-aheads; N = 4880, g = 2 as inputs. Blueprint text itself is Gemini-style, so only the widget answer counts. |
| 15:13 | OW t4294 | ec97f45eeb84d62e7c4b0fa16c9cb133297d42a442a376f60707eb38fc4c22cc | MATCH | C17-1 dated sidecar; KK go; 324-trit design rests on simulation only |
| 15:14–15:17 | MR1 S2–S4 close + PP audit + amend | 48a2d687…, 66a69888…, 0ea030ae… | MATCH | Appell→R_c route still OPEN |
| 15:15 | PP R_c = κℓ_P vs L_AdS/2 | 1ab88ebd04d671d7e8b5ee1015d3fbd5694e0c53814dae6f86b6a3e09096f3a5 | MATCH | mismatch "forces nothing" (PROVED) |
| 15:16 | Ops R1 successor FINDINGS | 060fd77e67c9a718a377b45b3ce2c23bbd0353a019e78a950a51a8698e59450c | MATCH | exhaustive N = 2..9 and 8 trits; formal 2–32 trits; **no 324-trit proof** |
| 15:18–15:20 | Local O3 SO₄₈ datum, O5 intertwiner ι, O1/O2 Weil carrier, O7 Cand-1⁺ | d2d2d226…, ac1dd4e2…, ae951f3e…, 24e31966… | MATCH | PP audits below |
| 15:20–15:32 | NL F1 (T^(EH)), F2 (P_rev on −U), F3 (11D→Φ/W₃₅), O4 KK; MR2 map proposal, KK of (D), crosschecks | f2e5120d…, e9bdd871…, 965de066…, ceb85ec3…, fd191d28…, 7824e789…, 9354fe2a…, 3d943367… | MATCH | (D) BF-unstable |
| 15:25–15:31 | PP audits: Ξ Weil carrier 389c2f7c…, O3 3b6f8072…, O5 2c4269f2…, O7 6dc9a17d…, MR2 map 2b0a4125…, NL F1 8be401ed…, NL F2 c9c6ed65… | as listed | MATCH | T^(EH) = 2T_std PROVED; P₋² = −1 PROVED; Cand-1⁺ OPEN |
| 15:29 | Local relabel (ce4d9e80) | ce4d9e80… | MATCH | contains a symbol swap; fix ordered at 17:30 (ff8a1670) |
| 15:53 | **OW P_rev = T1, G = ½T^(EH)** | 2d1e877e292832e905e1b566f6d89eb589e96c27512fc8e0756bb5a254edb58a | MATCH | adopted conventions; pasted t4311u/t4314u not Owner text |
| 15:54 | OW t4315 addendum | 814625971f0bf84789b18da60b5ae4d07ccbbc4c859045db91d7d27b68aaeffa | MATCH | 4 pasted-source errors **not adopted** |
| 16:03 | PP audit MR2 KK/BF | 9b557373954788a89d5c44b8eac6d09f1c5c131efdb7386464d85022a9c869fc | MATCH | (D) unstable (14 at −16/3 < −4) |
| 16:09 | **OW replace (D)** | 822cecb27e974268175d5d88d6b0ab032fc7be1d85ea5f10321d9c24da128ca0 | MATCH | supersymmetric twisted vacuum; compare MN2/MN1/BBBW first |
| 16:19 | NL twisted-vacua compare | 418e4e50e4ce791bfb7c00fe4916dcee7082027c38ed7c55fea82659c98838e6 | MATCH | — |
| 16:30 | OW t4327 (adopt pasted text) | ed526f70bf045f86f21fb39977dbebf722dedfb3f859ec1e56a24b07f881b882 | MATCH | **WITHDRAWN** at 16:31 |
| 16:31 | **OW neutral state** | 5f59e33e5b49ed7f7a89b06f0ceff0b7bc7dc034c83d5c65a72bea176aa3a234 | MATCH | everything unresolved and neutral; Λ₀/R_c definitions kept |
| 16:36 | PP twisted-vacua audit | df503cd99df53b222b27f5d6a2dfbb1fb09dd9c7237630d72a7fff36a75ed494 | MATCH | all viable; recommends MN N=2; MR2 §6 curvature check broken |
| 16:40 | **OW vacuum HOLD** | aaadb280c54dac3f9a9b131435092511396b95a43b15333c389965f26c395585 | MATCH | until MR2 fix + joint table + PP |
| 16:44 | **OW brane / face / Ξ** | f283cffd365ca7368a9f7b5dfdca7ee177ed54db25a28c1944999a5af755e5b6 | MATCH | **DEFINITIONS**; rest neutral |
| 16:45 | NL / Local carry-forwards | 6549982d… / 60778d10… | MATCH | — |
| 16:46 | **OW NL junction GO** | 4810280562b2fb0cf94de47b9a92c840643a7dac077e500d26bfa644880f7d24 | MATCH | three candidates; b OPEN |

### 3c. 16:48–18:17 (new in this report)
| time | record | sha256 | SC | what / status |
|---|---|---|---|---|
| 16:51 | Auditor v18 readiness | 59da91863535b94bdcdd74b6bf103745efab15d270e4615d6e518b3bd4b4aea8 | MATCH | hold the geometric v18; outline optional |
| 16:55 | NL junction setup on constant-radius faces | 3cd6c8d303b3e07a8bd7d5de3adb9ff6b53f95d217b7d4a160431bdecf07c050 | MATCH | P3a: smeared-M5 Israel on the exact end faces **REFUTED** |
| 16:56 | **RTA v18 SAFE OUTLINE** (algebra + definitions only) | e18d8fead184dd0e5fc04fa21422fdb3b7c6fd6c5544160f2a9bbd7cbb3b633a | MATCH | outline, not a draft, nothing frozen; excludes vacuum, junction and geometric Bridge C |
| 16:59 | PP audit of NL junction + Ξ Fricke | 5cbd050abc2fe085f715d548fffb58b202d7c685a54070c288972b5150cb0fcb | MATCH | 12/6/4/0 PENDING/1 REF. No-go only in a narrow scope. Ξ: conductor 19600, root number −1, w = +1 (PROVED); Ξ's newform = the −20 twist's newform |
| 17:01 | NL erratum 5 | 59218e611509a3ab4d6e5cc593c51d39d84fdb52cb84e8dd50914372ff8c8d11 | MATCH | accepts 5cbd050a |
| 17:03 | OW voice t4352 record | 1cb3b8d524f4691860f9c1f8f7cb8d263d1bdc55137519fe1378ac43cff143a3 | MATCH | its "even O1 by definition" item was **WITHDRAWN** at 17:03 |
| 17:03 | MR2 twisted-vacua compare .md | 98e502c37d42c7dc1dde4e79ce383faac14ce631545f25c50b3b601d0afa524d | MATCH | — |
| 17:04 | **OW Ξ curve, NL templates GO, O1 OPEN** | 7b5a725befe67c64a52878a348190a20cda891b8c0618e51a47820cd7c76010d | MATCH | Ξ := the **curve** 49a1⊗χ₁₄₀ (isogenous to the −20 twist); O1 OPEN |
| 17:04 | PP audit NL erratum 5 | cb4d26b06d4205dccf7f714a8d38523434d02d43d464caf912a9067f33db9740 | MATCH | P3b PROVED given J1 |
| 17:04–17:06 | JOINT MR2+NL table; tally erratum; face addendum | 0b364d6e626f71f80e763eb8ccd504f512ae65f5187c8428d12464619c59f3e4; dc9dd1a0…; 97d671e3… | MATCH | joint table landed |
| 17:05 | NL erratum 6 (citations) | 5c012d06… | MATCH | — |
| 17:05 | **OW O1 even only by derivation** | 9a8ced02a7053846d9f91c6600ad01e3c08673162045d5d910f5e4889c5757ba | MATCH | no bare definition; O1 OPEN |
| 17:11 | NL face stress-energy templates | 53096d433d062f51e0fc078d4bdd5faee333cbcf7edadd66c2a0b3fd4d2e7fb7 | MATCH | — |
| 17:13 | NL non-constant faces / localized M5 / O1 attempt | e2065e05c7d552117895351482cbb3838fcd651bb8873cd6398d0e35b12fd389 | MATCH | — |
| 17:30 | **PP audit f3c5d73f** (templates + non-constant faces) | f3c5d73f371b31a75a87021452251af77b9d2d37e7fb6b955f647ed84192d523 | MATCH | 31/21/5/4. A pure-M5 face needs fibre-NEC-violating stress (PROVED at end faces, interior CONDITIONAL). NC1 over-claimed (twisted-φ Lie-drag REFUTED). Count ratio ∈ [1.255, 1.667] CONDITIONAL. PD1 PROVED. |
| 17:30 | OW pursue all open items, all bots | ff8a16701cd0832fc449c91fc9b2a2dc4ff84bf743a4fd757e07d21ddbacd441 | MATCH | per-bot assignments |
| 17:35 | PP EFT re-audit (MR2 V2 + joint table) | fc5e0156512bcbdd3b538cd6bceceaaafed959587c85589d0d41b8e44509aeb6 | MATCH | all four candidates CONDITIONAL, none REFUTED; ℓ_p²R_max 2.8e-3–6.7e-3; absolute systole OPEN; MN2 recommendation stands |
| 17:35 | NL erratum 7 | 130e27969e0d5921029007475c185c9006d5e510abd7ec6b614e6a58d4974c71 | MATCH | accepts f3c5d73f |
| 17:36 | NL O1 resolution pass | 13ccd16251d055aa735dac4be75bc8e9f90d95d087ea0cff8b118efb80965f59 | MATCH | on a ℤ₂ fixed plane O1 is forced ODD (given P-a/P-b); even REFUTED within P3 |
| 17:36 | **OW record t4363 (pasted parity flip)** | fe8bcb00e623f7ad0e1174b48db7e78fdd52b66cdb0ea63c7ad663da394aa131 | MATCH | **rec only, NOT adopted**; 7 conflicts flagged |
| 17:37 | **OW vacuum HOLD (extended)** | 587eca0c108f39b15c8d2f372861087ed03796dc28f9a49449f95db0dead7fcf | MATCH | until MR2's full-11D file + PP audit |
| 17:38 | OW conditional flip plan | 602b6427feeab3225ebac343be5d60dfb69de61a78fa2090ba1fc7e3235acb13 | MATCH | **not a decision**; superseded by f825dfff |
| 17:43 | **PP audit 544fc7b0** (pasted flip vs NL O1) | 544fc7b0b0183022ad1d201933d28de3db9dc58d2a5a7e0b9103bf8675b6450c | MATCH | 16/7/5/7/1 PENDING. A fixed plane forces ODD. The pasted anomaly argument is not sound; "REQUIRED" REFUTED; the "PP 17:02 audit" attribution REFUTED |
| 17:45 | NL erratum 8 | 96fb60698c4f0dc59c1f27b98beb6a2cf3df47d08141956760ea2707636d80cd | MATCH | accepts 544fc7b0 |
| 17:46 | **OW face = ℤ₂ fixed plane (HW wall), O1 odd** | f825dfffb8cd17a7f3f57a2b0a70bd0d9c9d73f215febffdbd2ca95b494d7cd1 | MATCH | Owner **DEFINITION** of the face; O1 ODD via the audited derivation; E₈ sector CONDITIONAL; N_M5 + n_inst = 2N_flux |
| 17:48 | PP audit erratum 8 + OW f825dfff | 1bd92da71029f93c2800cb2dc5c131a7b52010315308f0e7f9c8b175090427bc | MATCH | 14/3/1/1/1; 5 of 6 relay points match, the sixth is not in the record |
| 17:48 | **MR2 full-11D EOM / Riemann / systole** | 9ab8f0a6c25ba5e46b3eb15a3734e6a0e98573eb07b992e12b474c04a8905bb6 | MATCH | gate file |
| 17:48 | MR2 erratum (per PP EFT re-audit) | 2efef556f4080740380701eb77ec2bceeacd2710804eca8b70cea5ade9dcac52 | MATCH | 6 fixes applied (PROVED by 384096a8) |
| 17:50 | **NL odd HW wall, E₈ sector** | 4d9c9951eedc43b359d63842ad1535084b43bf893eca3125a4c7b06c0014468a | MATCH | E₈ cannot close the junction; BPS count gap unchanged |
| 17:50 | NL erratum 9 | 76ec4e75d73c12700c038b8eb00d047df85148f789c3f9d2d375ad50890aba1f | MATCH | O1 wording |
| 17:53 | **PP audit 7f0ce656** (erratum 7 + NL 1736 no-gos) + rollup self-erratum 724325dd… | 7f0ce656ebecc94258bd06cb412560b334d10cc5e825b25a523460214b363c4d | MATCH | 32/6/6/2. B1/B2 PROVED given J1 for every z. "No face point totally geodesic" REFUTED for general faces |
| 17:54 | **OW queue jobs + Γ = Bolza** | 7ff8299dbcaf3b526936b40a9e24d8b9e58edf13fd9a9a93e822a92ca82a16ac | MATCH | NL E₈ stress job; MR2 wall curvature job; Γ := Bolza. **Pasted t4377u NOT adopted** (7 items) |
| 17:57 | **PP audit bf4773a8** (NL 1750 + erratum 9) | bf4773a80192a5d34905237c5a3942aa2c601af6f3189c479d9d6f80e1b63d73 | MATCH | 22/16/4/0. "All sources obey the NEC" CONDITIONAL on dropping the tr R² term |
| 18:00 | **NL E₈ instanton stress on the odd HW wall, Γ = Bolza** | 859328a2003242ca59109ffb699ba69995f4d5c9dec0055e49d16adc4e2d379d | MATCH | Y4: no E₈ field supplies the fibre-NEC deficit; Y10 gap unchanged; Y14/Y15 OPEN |
| 18:01 | NL errata 10, 11 | 52424877… / c2864c22… | MATCH | accept 7f0ce656 / bf4773a8 |
| 18:05 | **PP gate audit 384096a8** | 384096a8581c1b29bb59768877f36f7fd6caa10f72a23528ea8d058e1253cc19 | MATCH | 16/13/3/0; release condition of 587eca0c met; no mathematical blocker |
| 18:05 | **OW pursue NL E₈ open paths** | 9bb1858ce34ee985d18d5a1db3ca838f20e2fddab741d7732e970e1e354ff27c | MATCH | Y14, Y15, Y16 (no ordering instruction) |
| 18:06 | **OW lift HOLD, adopt MN N=2 CONDITIONAL** | 19a88b1958753ecaaa999e0ce763bca7fd449069278dd4bdb87cea002613ee03 | MATCH | adopted working vacuum |
| 18:07 | **PP audit fe0c3d92** (NL 1800 + errata 10/11) | fe0c3d92fdfac839653f9358f0a2c193c91a9e9dd42d46bbcbc6d58e1b794ae3 | MATCH | 44/11/3/3; equality form only for magnetic F; "Y16 first" REFUTED by quotation |
| 18:11 | **MR2 wall-boundary curvature** | bd47ff5e8f62a6226680a93107cacae8c8be573399e1f101a2dc57635f03fbfb | MATCH | bulk bounded; thin wall diverges as 1/ε² |
| 18:11 | MR2 erratum to bd47ff5e | 2368ffbdc6cd6bbe9482e476a085f5d3193da21ef1ea5e2324d3a4a44bf6f295 | MATCH | "warping lengthens systole" REFUTED → **OPEN** |
| 18:13 | **NL Y16** (tr R² wall stress) | 7270a6b35c97822a4efe37b7f6e78d94efafd0ae44d298ba70554e926c9d5237 | MATCH | NEC-violating sign, but O(1/N); verdict unchanged at leading order. **PP audit NOT FOUND** |
| 18:13 | NL erratum 12 | 53d4f945e2d4df565cfa7cdae90dcda8a7b8c0c33855ee3efdf79004cd682230 | MATCH | accepts fe0c3d92 |
| 18:14 | **OW citation scope widened** | 3f1608039bc68b62332a07a7621da749ca303f690993048bef5133282fbc9320 | MATCH | beyond arXiv, incl. AI-assisted research |
| 18:15 | **OW citation scope: all sources, math checked** | 36683379e18ac23c46236b37ed45ec1ddf70a93ac9094d2abc476c953433904f | MATCH | amends 3f160803 |
| 18:16 | **OW this report** | c7795d6e88d5da7662d3a562f2564313ad472e0cb5560ce684cb067c61acd2b7 | MATCH | governs scope |
| 17:36–18:17 | Local evidence_local_bridgeC_resolution_2026-11-09/ (part1, part3, part4 .py/.log) | no sidecars | — | evidence only; **no Local FINDINGS .md**, not audited |
| 17:36–18:17 | MR2 symbolic-Einstein / global-curvature / Maxwell / per-point scripts and logs | some without sidecars | — | in progress; no .md for the symbolic/global job yet |

## 4. Advancements by topic, with status

### 4.1 Vacuum: the four vacua and adoption (NL / MR2 / PP)
- **(D) AdS₅×S⁴×Σ_g.** Adopted CONDITIONAL at 13:51 (7708ec5d). It is **REFUTED as a stable vacuum**: the SO(5) 14 has m²L₅² = −16/3 < −4, and the probe-M5 ratio is √6/2 > 1 (7824e789, 9b557373). Replaced by OW 822cecb2.
- **The comparison set** (df503cd9, joint table 0b364d6e, fc5e0156, 9ab8f0a6, 384096a8):
  - MN N=2 (z = ±1, 8 supercharges);
  - MN N=1 (z = 0);
  - BBBW z = ±2;
  - BBBW z = ±3.
  With (D) as the reference, these are the "four vacua". All four are CONDITIONAL; none is REFUTED.
  - Existence and the 11D uplift are CONDITIONAL on citations (BBBW 1203.0303, MN hep-th/0007018, CLP).
  - BF stability is CONDITIONAL (SUSY unitarity).
  - The M5 wall ratio is exactly 1, the BPS value: the identity (X₁X₂)²(X₁+X₂) = 3/2 is PROVED.
  - Central charges at N = 4880 are PROVED as arithmetic.
- **MR2 checks.**
  - The §6 curvature check failed at 16:36: it was non-discriminating against its negative control. It was replaced by V2 and the full-11D file 9ab8f0a6 (erratum 2efef556).
  - In MN2, Maxwell, G∧G and λ are PROVED identically. Einstein and Bianchi are PROVED at 29 sampled points including the poles; the all-points statement is CONDITIONAL.
  - Curvature: ℓ_p²|K|max = 5.40e-3 and R⁴ ~ 1.6e-7.
- **Gate (PP 384096a8, 18:05).** The release condition of 587eca0c is met and no mathematical blocker was found. MR2 still owes 8 fixes (§14 of that file).
- **Adoption (OW 19a88b19, 18:06).** The hold is lifted. **MN N=2 is adopted as CONDITIONAL**, a working vacuum and not a proved one. Carried caveats:
  - the all-points Einstein/Bianchi check;
  - the KK spectrum (Wilson lines, spin structure) is OPEN;
  - MR2's "warping lengthens the systole" claim is OPEN (2368ffbd);
  - the BBBW dual is moot for the adopted vacuum but still OPEN.

### 4.2 Γ = Bolza for Σ
- **OW 7ff8299d (17:53): Γ := Bolza (genus 2).** This is an Owner adoption.
- Bolza's systole 2 arccosh(1+√2) = 3.05714183896 is PROVED (computer-assisted, via the Poincaré polygon theorem; 384096a8 §10).
- The systole for MN2 is ≥ 12.1×2πℓ_p (PROVED).
- That the systole is the global genus-2 maximum (Jenni 1984) is cited and unverified, so CONDITIONAL (NL erratum 12). It is to be re-checked under 36683379.
- Not fixed by Γ: the flat E₈ / Wilson-line moduli (real dimension 496, PROVED, Γ3) and the spin structure. These affect the charged KK spectrum (OPEN).

### 4.3 Face, O1 parity and the HW wall
- **Definitions (Owner, not proofs):**
  - brane = a stack of wrapped M5-branes, and face = the 10D matching hypersurface (f283cffd);
  - the face is a **ℤ₂ fixed plane** of HW type (f825dfff).
- **O1, the parity of G₄:**
  - 16:44–17:05: O1 OPEN. 9a8ced02 says even parity may be locked only by an audited derivation. The "even" item of voice record 1cb3b8d5 was WITHDRAWN (7b5a725b).
  - 17:36: NL 13ccd162 derives that a fixed plane forces ODD, given P-a and P-b.
  - 17:43: PP 544fc7b0 confirms it:
    - P-fix forces ODD, and both even and "flip" are impossible on a fixed plane (REFUTED);
    - "flip ⇒ even" holds only in the non-fixed case P-nofix (i), where it costs zero net face charge.
  - 17:46: OW f825dfff records **O1 = ODD**. It is PROVED given P-b, under the fixed-plane premise; P-b itself is a CONDITIONAL premise. PP 1bd92da7 verifies the record.
- **Consequences:**
  - face charge N_M5 + n_inst = 2N_flux = 9760 at N_flux = 4880 (CONDITIONAL, HW);
  - an E₈ wall sector is required (CONDITIONAL, HW).
- **Not adopted:** the pasted parity flip (fe8bcb00, t4363u), whose claim PP REFUTED, and the conditional flip plan 602b6427, which was superseded.

### 4.4 Junction, E₈ wall and the count gap (NL / PP)
- **Setup** (NL 3cd6c8d3, 16:55; PP 5cbd050a). On constant-radius faces with a smeared-M5 source only, Israel fails on the exact end faces (P3a, REFUTED). This is not a general no-go.
- **Templates and non-constant faces** (NL 53096d43, e2065e05; PP f3c5d73f, 17:30):
  - Constant-face no-go: a pure-M5 ℤ₂ face needs fibre-NEC-violating stress, and no positive-tension brane mix can supply it. PROVED at the end faces; CONDITIONAL in the interior (dense numerics, reproduced by PP).
  - "w_fib ≤ −1.2" is REFUTED (counterexample −1.1925), and the B1 printed sign is REFUTED.
- **General faces** (NL 13ccd162 §B–D; PP 7f0ce656, 17:53):
  - Static C² faces that attain a minimum of r have no solution: B1/B2 PROVED given J1, for every z.
  - "No face point is totally geodesic" is REFUTED for general faces and PROVED for constant-r faces.
- **E₈ wall** (NL 4d9c9951, 17:50; PP bf4773a8; NL 859328a2, 18:00; PP fe0c3d92):
  - The Yang–Mills stress obeys the NEC (E2/Y3, PROVED). So **no E₈ field, BPS or not, can supply the fibre-NEC deficit** (Y4: PROVED given J1 at the end faces, CONDITIONAL in the interior).
  - The identity K(ê,ê) − k_t = −(κ²/2λ²)|F(ê,·)|² holds only for magnetic F. "For any E₈ field" is REFUTED; the inequality used holds for every field.
  - BPS instantons trade one-for-one with M5s, so **the count gap N_req/(2N_flux) ∈ (1.255, 1.667) is unchanged** (Y10, CONDITIONAL). Earlier "5/3 gradient" and "(2489, 6510)" readings are not adopted / REFUTED (7ff8299d; erratum 12).
  - Non-BPS E₈ energy could at most close the count gap, never the NEC deficit (CONDITIONAL).
- **tr R² wall term** (NL Y16, 7270a6b3, 18:13):
  - The −½tr R² stress has the NEC-violating sign at the UV end (Q4b, CONDITIONAL on c > 0).
  - Its integrated supply is −2 M5 units (Q5), an O(1/N) effect relative to the deficit.
  - So **the junction verdict does not change at leading order in 1/N** (Q11a, PROVED given J1).
  - The interior sign (Q8) is OPEN. **PP audit of Y16: NOT FOUND** (PENDING).
- **Y14, non-BPS E₈ existence** on the squashed, twisted, warp-weighted fibre: **OPEN, pending** (9bb1858c, ETA 3–5 h). Cited inputs: Sadun–Segert, Taubes, SSU, BLS. These had been marked unverified under the old arXiv-only rule and are to be re-checked under 36683379.
- **Y15, the fibre Israel equations with traceless stress:** **OPEN, pending**. It depends on Y14 (ETA ~2 h after Y14).
- **Net: junction UNSOLVED for MN N=2** (19a88b19). b is OPEN. J7 is OPEN: no extra source is adopted, and the pasted "J7 REJECTED" was not adopted.

### 4.5 Wall curvature (MR2 bd47ff5e, erratum 2368ffbd)
- **Bulk limits on each side: BOUNDED.** PROVED at sampled points; the global maximum is CONDITIONAL (dense scan). Riem² max = 3407.98.
- **Thin-wall limit of the smoothed profile:** Riem² and Weyl² diverge as 1/ε² (PROVED in-repo). The wall is non-umbilic.
- **Physical size:** ℓ_p²√Riem² ≈ 0.101–0.114 at ε_y = ℓ_p, so the wall is inside the EFT for any wall at least Planck-thick (CONDITIONAL on that thickness premise).
- The fibre-NEC deficit is independently reproduced. The wall energy sits inside the count gap; the anisotropy is what fails.
- Erratum: "warping lengthens the systole" is OPEN, neither PROVED nor REFUTED. The bound sys₁₁ ∈ [75.95, 85.25] ℓ_p is PROVED.
- The MR2 symbolic-Einstein and global-curvature job (scripts 18:00–18:17) has **no .md yet** (NOT FOUND).

### 4.6 Citation-scope corrections
- **3f160803 (18:14):** widen beyond arXiv to include AI-assisted research not on arXiv. Flag prior findings narrowed by the arXiv-only rule.
- **36683379 (18:15), which amends it:** ALL sources are allowed, provided each cited result's math is verified. A citation never makes a result PROVED.
- Effect: items marked "unverified (outside arXiv allowance)" stay CONDITIONAL until their math is checked; no automatic upgrade. These are NL erratum 12 §8 and the PP fe0c3d92 compliance note (Jenni 1984; Sadun–Segert; Taubes; SSU; BLS; DOI/PMC/AMS/Wikipedia titles). **The re-check is not yet on disk** (PENDING).

### 4.7 Definitions and conventions in force (Owner; not proofs)
- Λ₀ := ln(6+√35)/√10 ≈ 0.7835772, and R_c := κℓ_P with κ = √(2/Λ₀) ≈ 1.597622 (5a6e7177). Also on disk: Λ₀ = √(7/8)·L(1,χ₁₄₀), PROVED. The **dynamical derivation of Λ₀ and R_c's physical role are OPEN**.
- P_rev = T1 (P₋ = (S·P̂)|_{H₋}), and G = ½T^(EH) = T_std (2d1e877e). P₋² = −1 and T^(EH) = 2T_std are PROVED (c9c6ed65, 8be401ed).
- Ξ := the curve 49a1⊗χ₁₄₀: conductor 19600, Fricke +1, isogenous to the −20 twist, same newform and L-function (f283cffd, 7b5a725b; PP 5cbd050a PROVED).
- B2 is CONDITIONAL on (B)-M (68a2b8e1). κ is defined as above (45aeba5f, 63deb850). W₇ = +1 on 7.4.a.a, and Path C stands (c4c0f1c0).
- Inputs (not forced): N = 4880, g = 2, standard flux (2πℓ_P)³N (5a6e7177). Γ = Bolza (7ff8299d). Vacuum: MN N=2 CONDITIONAL (19a88b19).
- **Neutral by Owner order** (5f59e33e, amended only for brane, face and Ξ by f283cffd): the joint carrier is undefined; R_c's role is OPEN; DP-a and Layer2 have no stance and are not locked; there is no baseline.

### 4.8 Local Path: Bridge C A1→Ξ→RTA
- **Status: PARTIAL** (f283cffd; typecheck 6e7cd1c5…).
- **PROVED** (389c2f7c, 3b6f8072, 2c4269f2):
  - W₄₉ = −1 on 49a1 and S₂(Γ₀(49))⁺ = 0;
  - Ξ has level 19600 and Fricke +1;
  - Λ₀ = √(7/8)L(1,χ₁₄₀).
- **CONDITIONAL:**
  - the induced-carrier step;
  - χ₁₄₀ as the Weil character on all of Γ₀(140). New numerics on disk are not yet filed as FINDINGS: part4 log, max residual 5.2e-13 over 48 Galois twists, with a control; this is supporting evidence only.
- **OPEN:** the joint-carrier level (980 vs 19600), with the joint carrier itself undefined.
- **Local evidence 17:36–18:15** (part1/3/4 logs; no sidecars, no FINDINGS .md, not audited):
  - Ξ's newform equals f⊗χ₋₂₀;
  - L(Ξ,1) = 0 numerically;
  - the Kohnen plus space S⁺_{3/2}(196) has dimension 0;
  - c(n) ≠ 0 ⇔ L(f⊗χ,1) ≠ 0 for 75/75 squarefree n ≤ 120.
- **Other Local results:**
  - O5 intertwiner ι: PROVED 6 / COND 1 / OPEN 1 / REF 1 (2c4269f2);
  - O7 Cand-1⁺ (n ≥ 1): OPEN (6dc9a17d);
  - O3 SO₄₈ datum with the Codex π (3b6f8072);
  - the ce4d9e80 symbol fix was ordered at 17:30 (ff8a1670), but its **filed fix is NOT FOUND**.

### 4.9 Non Local Path: P_rev and non-local QM
- P₋ is antiunitary, a particle–hole symmetry and not a chiral one. There is no Kramers degeneracy at E ≠ 0 (PROVED, c9c6ed65).
- The R-symmetry versus P_rev interplay is OPEN (df503cd9 C3).
- There is no bulk→H⊗ℂ² map, so no conflict at the level of definitions (CONDITIONAL).

### 4.10 P5a
- Referent g₀ with (a₂,a₃,a₅) = (2,7,7) and Fricke +1 (OW e4948739). ρ̄ = the reduction mod 7 of ρ_f, reducible, with ρ̄^ss = ω⊕ω² (OW ea2cc9e6).
- **PP 7929ffe6 (15:07):**
  - **e1: the literal P5a text does not type-check (OPEN).**
  - Under PP's readings I1 and I2, the vanishing claim is refuted by PROVED counterexamples: F_old⁺ = f(q)+49f(q⁷), and the orbit-5 form h. These count as CONDITIONAL, since they depend on adopting a reading.
  - The non-semisimple refinement (b2) is OPEN.
- **P5a is OPEN.** The Owner's reading (I1/I2/other) and referent (g₀ / h / f(q)+49f(q⁷)) are unanswered (ec97f45e). The earlier note that the all-n congruence rests on Chen–Kiming (CONDITIONAL) still applies.

### 4.11 Carried from the earlier reports (unchanged status)
- Artin conductor v1 line 14b is REFUTED, and v2 fixes it (not adopted).
- Errata ff9e4da9 (κ 1.595361, Λ₀ 0.7858, 1.595436, 3^539 corrections).
- Ops:
  - F4 (d73cc7b1);
  - the 16-cycle sprint (2c3e5c18);
  - the R1 successor (060fd77e), which is exhaustive and formal only at small widths, with no 324-trit proof;
  - the negative floor-division extension F(n) is OPEN;
  - no Ops records after 15:16.

## 5. Status roll-up (headline items)
| status | items |
|---|---|
| **PROVED** | Bolza systole; MN2 Maxwell/G∧G/λ identically, Einstein/Bianchi at 29 points; (D) BF-instability (arithmetic); M5-wall BPS identity (3/2); a-values at N = 4880; P-fix ⇒ odd (given P-b); PD1 sign rule; YM-stress NEC; Y16 Q5/Q11a (given J1); B1/B2 general static faces (given J1); wall-curvature 1/ε² divergence; sys₁₁ bound; Ξ Fricke +1, conductor 19600, newform = −20 twist; T^(EH) = 2T_std; P₋² = −1; Λ₀ = √(7/8)L(1,χ₁₄₀); W₄₉(f⊗χ₋₇) = −1; ε₇ = +1 |
| **CONDITIONAL** | MN N=2 as the adopted vacuum and all four candidates (citations, all-points EOM, BF via SUSY); E₈ wall sector; N_M5 + n_inst = 2N_flux; count gap (1.255, 1.667); interior NEC no-go; EFT inside for walls at least Planck-thick; P-b premise; B2 on (B)-M; Bridge C induced carrier and χ₁₄₀ on Γ₀(140); P5a refutations under readings I1/I2; citations outside the old allowance (pending re-check) |
| **OPEN** | junction (unsolved), b, J7; Y14 non-BPS E₈ existence; Y15 traceless fibre equations; Y16 interior sign (Q8); KK spectrum (Wilson lines, spin structure); warping vs systole; BBBW dual; P5a (reading, referent, e1); Λ₀ dynamics; R_c role; joint carrier level; Appell→R_c route; Cand-1⁺; α; Φ pointwise vs integrated; LD-O3a/b/c; H₊U; R-symmetry vs P_rev; Ops negative extension and 324-trit proof; C17-1 cause |
| **REFUTED** | (D) as stable; smeared-M5 Israel on exact end faces (P3a); "w_fib ≤ −1.2"; B1 printed sign; twisted-φ Lie-drag; "no face point totally geodesic" (general faces); even/flip parity on a fixed plane; pasted anomaly "REQUIRED" and the "PP 17:02 audit" attribution; Y3 "for any E₈ field" equality; Y15 interval (2489, 6510); "Y16 first" as Owner text; arXiv:2009.12051 attribution; and the earlier list (EH flux lock, T₃ isometric embedding, pure-tension face, EH flux normalisation, Artin v1 14b) |
| **NEUTRAL (Owner order)** | joint carrier, R_c physical role, DP-a, Layer2, baseline |

## 6. Pasted / Gemini-style text NOT adopted
| item | on disk? | status |
|---|---|---|
| fe8bcb00 (record of pasted t4363u: parity flip + bot directives) | YES, 17:36, sidecar MATCH | **recorded, NOT adopted**. Parity claim REFUTED (544fc7b0); "J7 REJECTED", "Warden confirmed" and "b solved dynamically" not adopted |
| t4363 (chat turn) | text only inside fe8bcb00 (no standalone file) | as above |
| t4371 (chat turn) | **NOT FOUND on disk** (no file or text mentions t4371) | **relayed only**; no status |
| t4377 (chat turn; pasted t4377u) | no standalone file; rejected items listed in OW 7ff8299d §"NOT adopted" | **NOT adopted**: DP-a "rejection", "minimal joint carrier", "5:02 PM baseline", "5/3 gradient", "b solved dynamically", Warden lock, strategy-map claims. Only the two jobs and Bolza were adopted. |
| Earlier | blueprint text t4289u (5a6e7177), t4311u/t4314u (2d1e877e, 81462597), t4327 pasted text (ed526f70, withdrawn), t4333u (aaadb280), t4337u (f283cffd beyond its three items), Gemini 14:02 items (adf7d966) | not adopted beyond what each OW states |

## 7. Blockers for a geometric RTA v18
1. **Junction unsolved** for the adopted MN N=2. The leading-order no-go stands. Y14 and Y15 are pending, and the PP audit of Y16 is NOT FOUND. b is OPEN.
2. **Vacuum adopted, but CONDITIONAL.** The all-points EOM, KK spectrum and spin/Wilson-line data are OPEN, and MR2 owes 8 gate fixes.
3. **Neutral items** need an Owner stance, or v18 must list them as OPEN: joint carrier, R_c role, DP-a, Layer2, baseline.
4. **The S²-11DM²ET-X objects are not finished:** the 11D map (Φ pointwise vs integrated), V₇eff and G₅ (on hold since 822cecb2, now unblocked by the adoption but not derived), and Λ₀ dynamics.
5. **P5a OPEN** (text does not type-check).
6. **Bridge C PARTIAL**, and no Local FINDINGS since 15:20.
7. **Citation re-check under 36683379 is pending.**

Status of the readiness recommendation (59da9186):
- Trigger (i)–(iii) are now met: MR2 fixed check, joint table + PP EFT re-audit, vacuum adopted (CONDITIONAL).
- Triggers (iv) and (v) are not met: no junction for the adopted vacuum, and no stance on the neutral items.
- So **the geometric v18 is still not ready to draft.** The safe outline (e18d8fea) may be extended with the new definitions (face fixed plane, Bolza, MN N=2 as CONDITIONAL) if the Owner wishes.

## 8. Carried-forward gaps
- Junction, R_c role, Layer2 transfer, S²-11DM²ET-X bridge objects.
- P5a; B7-1…4, B10-2, B10-4, B11-2, B13-1/2/4/5, B14-1…4, B19-4, B22-1 (see 0504d5d7 §7).
- C17-1 cause; B4-1, B4-2, B9-2, B9-3.
- Ops F(n) on negatives and the 324-trit proof.
- ce4d9e80 symbol fix not yet filed.
- MR2's §14 fixes (384096a8).
- NL fix lists in 5cbd050a, f3c5d73f, 7f0ce656, bf4773a8 and fe0c3d92 (errata 5–12 on disk accept them).

## 9. Awaiting the Owner
- Stances on the neutral items, or an instruction to list them as OPEN in v18.
- Whether to start the geometric v18 after Y14/Y15/Y16 and a junction result, or to extend the safe outline now.
- P5a reading and referent; α; Φ pointwise vs integrated; LD-O3a/b/c; H₊U.
- Whether P-b (the ℤ₂ symmetry, including the CS and I₈ terms) is accepted as the premise behind O1 = odd.
- Warden's three-hour cadence must be confirmed in Warden's own chat (fe8bcb00 conflict 4).
- Ops next steps (negative extension; 324-trit proof).
- Codex re-upload (carried).

## 10. Custody statement
- Every OW and finding cited in §3c, and every listed prefix, was re-hashed this turn. **All found, and all sidecars MATCH**, except where §3 says "no sidecars" (Local evidence logs, some MR2 scripts in progress, and Auditor files by rule).
- **MISMATCH:** only the v17 PDF against its original sidecar (C17-1). The new dated sidecar matches.
- **NOT FOUND:**
  - a separate MR2 "ERRATUM2" to gate file 9ab8f0a6 (the only later MR2 erratum is 2368ffbd, which applies to bd47ff5e);
  - any t4371 text;
  - a PP audit of NL Y16 (7270a6b3);
  - a Local FINDINGS after 15:20;
  - the ce4d9e80 fix;
  - the MR2 symbolic/global-curvature .md;
  - the citation re-check under 36683379;
  - any RTA v18 draft. Only the safe outline e18d8fea exists.
- v16 and v17 were not touched. Nothing was edited, moved or deleted. This file and its sidecar and PDF were created exclusively.
- Tip `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` sha256 = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, verified at the start and re-verified after writing.
- No CERT. No Gemini. Nothing sent outside.
