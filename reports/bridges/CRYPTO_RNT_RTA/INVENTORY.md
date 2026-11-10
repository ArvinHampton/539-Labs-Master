# INVENTORY: objects on each side and every existing claimed link

Paths: `R/` = `/workspace/quantum-comp/reports/`, `SF/` = `R/s_family_paths/`, `MS/` = `/workspace/quantum-comp/oct17-master/docs/S2-11DM2ET-X-Axiomatic-Book/` (local mirror of github.com/ArvinHampton/539-Labs-Master, commit 48684e3; a later mirror at `R/self-audit/repo`, cb11076). Written 2026-10-23 (CDT). Labels: **A** proved / certified (reference given); **B** stated without proof; **U** unsupported or contradicted.

## 1. Crypto side
| Object | Definition | Source (file:line) | Status |
|---|---|---|---|
| T3 | T3(3k)=k, T3(3k+1)=4k+2, T3(3k+2)=2k+1 on ℕ₀ | `R/crypto/PRESENTATION_SUPPORT/SUPPORT_DOSSIER.md:7,13`; `MS/Residual_Ternary_Algebra_Full_Manuscript_Draft_2026-08-24.md:51-57` (floor form) | A (definition) |
| Preimages | 3y always; (3y−2)/4 if y≡2 mod 4; (3y+1)/2 if y odd; one preimage iff 4∣y, never 3 | `SUPPORT_DOSSIER.md:15-25` | A (proof there) |
| Mod-3^j itinerary bijection | n mod 3^j ↦ (T3^s(n) mod 3)_{s<j} bijective | `SF/LEDGER_CatA_clean_v7/LEDGER_CatA_clean_v7.md:47` (entry 47) | A |
| T3 not defined on Z/3^j | | ledger entry 48 | A |
| σ(n), 539-step facts | σ(3^k m)=k+σ(m); T3^539 ends in {1,2} if σ≤539 | ledger entries 44–46, 53–54 | A |
| HQH-539-512 (STD-v1) | H(m)=SHA3-512(enc(T3^539(X))‖S‖":HQH-539-RESONANT:"), X=int_BE(SHA3-512(m‖S)) | `R/crypto/RPP_spec_v2_drafts/PI_AMENDMENT_DRAFT.md:9` | A (definition) |
| 18+521 split | loop split with no computational effect | `R/crypto/RPP_formal_statement/RPP_formal_statement.md:116`; `RPP_spec_v1/PI_SPEC_v1_candidate.md:47` | A (code reading) |
| Free Π | solved by x=3^L·z | `R/crypto/RPP_spec_v1/REDUCTIONS_B_what_can_be_proved.md:42-44` | A |
| Digest-target Π | ≡ preimage of outer SHA3-512 | same file, Theorem 4 | A (reduction) |
| Residual predicate R | undefined; Options W/S are drafts | `RPP_formal_statement.md:196,222-226`; `PI_AMENDMENT_DRAFT.md:64,210-211` | undefined |
| O_res | {21+9j : j=0..538} ⊂ Ω={0..4879} | `R/crypto/RPP_spec_v1/PREREG.md:11`; `MS/Object539_NonCircular_Construction.md` | A (definition) |
| Fibre blocks | 8 blocks 68,68,68,67,67,67,67,67 | `RPP_formal_statement.md:176`; `RESIDUAL_PREDICATE_C.md:38` | A (definition), see §5 |
| Permanent class [α⊗δf] | not defined on a path | `RPP_formal_statement.md:226`; `PI_AMENDMENT_DRAFT.md:210` | undefined |
| A0 emptiness | no two consecutive T3 values both in O_res | `RPP_spec_v1/RESIDUAL_T3_family_results.md:52` | A (script `x_ores_successor.py`) |

## 2. RTA side
| Object | Source | Status |
|---|---|---|
| T3 (same map) | `MS/Residual_Ternary_Algebra_Full_Manuscript_Draft_2026-08-24.md:51-73` (Def 2.1, Props 2.2–2.5) | A |
| B′ = ⌊(4880−21)/9⌋ = 539; 18+521; 17+521 | same file :83-95 | A (arithmetic) |
| Equitable 8-partition 3·68+5·67, uniqueness | same file :101-111 (Def 4.1, Props 4.2–4.3) | A (proof given there) |
| Linking series Λ_B | :115-119 | A (definition, closed form) |
| g_s, residue congruence of g_7 | :131-137 | A |
| Bridge Series C | :180 (Def 9.1) | A (definition) |
| "Axioms" of RTA | none algebraic; "six rules" are process rules | `SF/A18_RTA_foundation/REPORT.md` §1 | A (reading of sources) |

## 3. RNT / g_k / g_s / Bridge C side
| Object | Source | Status |
|---|---|---|
| g_k, allowed d, OccFilt_k(∞), Z_k | ledger entry 73 (`LEDGER_CatA_clean_v7.md:410-421`) | definitions |
| Positivity / sign split, pairing identity | ledger entries 74–75 | A |
| Parity Dominance, odd k | `SF/A39_gk_family/REPORT.md` verdict; ledger 79, 91 | A computer-assisted; central-limit layer partly re-derived (A59); odd k=17–25 audit pending |
| Even k≡2 mod 4 | A39 verdict | A (elementary) |
| k≡0 mod 4 MIX classes | A39 verdict | open |
| Zero families, g_7(67)=+1 exception | ledger entries 89–90 | A |
| dim S(ρ_s), dihedral at s=9,11,23,25 | ledger entry 28 (`:173-183`); `SF/A48_s_dims/REPORT_v3.md` | A at those s; general "all dihedral" unproved |
| Bridge C law space dim V = 36 at s=7 | `SF/A51_bridgeC_exact/REPORT.md` §1; ledger §8 | A (exact certificate) |
| Bridge C → RTA Map 1 (Fricke closure) | `SF/A53_RTA_maps/REPORT.md` bottom line 1 | refuted (A) |
| Bridge C is "key to RTA" | Arvin's view | B (no proof) |

## 4. Existing claimed links between the crypto mathematics and RNT/RTA/g_k/g_s/Bridge C
| Claimed link | Source | Status |
|---|---|---|
| T3 is "the core dynamical object" of RTA | RTA manuscript :11 | A as a statement of shared definition; it is the same map, not a bridge |
| 539 = 7²·11, ord₅₃₉(3)=210, 18+521, 539=⌊(4880−21)/9⌋ "contribute" to the construction | `RPP_formal_statement.md:318` | A as arithmetic; the same line says none is used in the definition, so as a link: U |
| "The residual T3 is the correct resonant path" (Arvin, 23 Oct) | `RPP_spec_v1/RESIDUAL_T3_predicate_sources.md:5` | B (no predicate defined) |
| Residual constraints (O_res, fibre, permanent class) inside Π | `RPP_formal_statement.md:222` quoting [FG] l.78–85 | U (undefined; Options W/S drafts) |
| Lock "Residual is not Resonant" | `PI_AMENDMENT_DRAFT.md:34,47` | rule, in force |
| R-grading of S(ρ_s) as a foundation of RTA, "ternary" = mod-3 of T3 | `SF/A18_RTA_foundation/REPORT.md` §2a | U (refuted as foundation; analogy only) |
| T3 "bulk" 539-step count | `SF/A20_T3_bulk_vs_shadow/REPORT.md` | U (no source rule gives 539) |
| Bridge C → RTA via Fricke/dilation by 7 | `SF/A53_RTA_maps` | contradicted (A, rank 72 > 36) |
| Any statement that g_k / Bridge C structure adds security to HQH | none found | none exists; not claimed |

## 5. The fibre blocks 68/68/68/67×5 (requested focus)
- **Category A.** 3·68 + 5·67 = 539 is the balanced (equitable) partition of 539 into 8 parts: 539 = 8·67 + 3, so 3 parts of ⌈539/8⌉ = 68 and 5 of ⌊539/8⌋ = 67. It is the unique 8-part partition with max − min ≤ 1 (proof in RESULTS §Proofs, P1; also RTA Props 4.2–4.3, manuscript :103-109). Hence the block sizes are determined by 539 and the choice m = 8 alone; 67 and 68 carry no information beyond (539, 8).
- **Why 8.** No source gives a reason for m = 8 beyond the statement of the partition. `MS/Object539_NonCircular_Construction.md:218-222` records mod-8 words and "N_flux ≡ 0, N_tow ≡ 3, L_pack ≡ 3 (mod 8)" labelled "Heuristic only". Searches for '67', '68', 'fibre', 'fiber', 'O_res', 'permanent class' in R/crypto, SF/ and MS/ found no other statement about why the blocks are 67/68.
- **Incidental source occurrences of 67/68** (not links): g_7(67) = +1 (ledger entry 90, the k²+2k+4 family at k=7: 67 = 7²+2·7+4); 68 = 4·17 lies in the open class k ≡ 0 mod 4; 67 is an odd prime outside the audited Parity Dominance range (k ≤ 33). "68·7 + 67" = 543 ≠ 539, so that form is not an identity of the packaging.
