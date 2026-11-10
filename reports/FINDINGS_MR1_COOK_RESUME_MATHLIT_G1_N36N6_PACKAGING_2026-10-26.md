# FINDINGS — MR1 COOK RESUME: math-lit G1 (N36 503 injectivity) + N36–N6 FILLED-MODP packaging hygiene — 2026-10-26 (America/Chicago)
Soft-SF Write-only. Cat-A invent NONE. No ν/CERT coefficients invented. Exact ν fill NOT started. path-(a) OPEN (no ρ̄ matrices). GAP-E off-mesh (OW b33a5e85…) not promoted. Kerr BLOCKED. Mesh CANCELLED. Alt B CERT fa47db06e268a6f73579c547af25851ba267720f8259cf281e76a9614ff46b32 cite-only, not re-run, no Card-1A ID.

## Authority / hashes verified (sha256sum, this run)
| Item | sha256 | |
|---|---|---|
| RESUME OW | fe0d3543028b801643d342466853d85bdce2f1bb47295e936a5c2bd7a3373d1b | ✔ |
| Tip LOCK pre | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | ✔ |
| Operative MODP CSV TE-SIMPSON-FILL-MODP_N18 | 38534aa1102da03cf96d7d76cdd454f8ef0530c4ef12439ec0cbf3c4346010f3 | ✔ |
| W1 seeds (Eigen) | ee9c36f9e5a23f3147bdbd104a4ba648cf8e9e2f3f22c750c0d143459364da96 | cite |
| N36 EXACT-CRT (Eigen) | 8061c7b2072537e2755e6d799883b2c093f5d221b3e4dff36df73194d6159d92 | cite |
| N36 503-BASIS (Eigen, earlier GAP-ABSENT) | a8547419cc5f0f041b29a57d36f00e3279a63e9d2bbbb89c69dbfc0c83bc8349 | cite (superseded by W1) |
| Q18 Sturm/Prop1.1 (89-dim) | b3172d3972bc113e870449096afc655d497513cecaa607169033953e7dc0f4d5 | cite |
| Prior lit deepen | 91ee45e532b1dd26c39f37d982c80235b4322f84709938fa9ce0f02498974ddb | cite |
| Prior freepursue (C6 GAP G1) | e1ca9141de1b646e73aacf92b4b5a3ee7bce480527822d556186b87b19d7440b | cite |
| N6 promote + N36 /140 check | 27b1c5e82aa8d3720767cd1eb4296aeb3eef93cbd434287e16ad3c821b797460 | cite |
| N36 ν21/25 promote | f57ea4b5e120e4aa1c5b686c5959a2a34f5e0a03a7a0e52e63c27be3603eb06f | cite |
| OW basis-ID confirm (TEN slot 10) | 4103ea927c9907709721e19f6935f7db3fa2ce54b4ed0465dce909b63ad8c8db | cite |
| N36 side CSV TE-SIMPSON-FILL-MODP-N36_N18 | 0e17098c61b5ee7823dad690fa998389a84e504055e599ca31c36a423deacbf2 | read |

## 1. G1 — injectivity of ∞-cusp q^18 truncation on S₄(Γ₀(49), ρ̄₃₆), dim 503
**Lemma (proved, elementary).** Let V = S₄(Γ₀(49),ρ̄₃₆) with dim_C V = 503 (Written, reverse-dimcalc e2b26038…). Let T: V → C^648 be truncation at ∞ through q^18 in the c*_e* seed coordinates. If f₁..f₅₀₃ ∈ V have q-coefficients in Z_(p) and the reduction mod p of the 503×648 matrix M = [T f_i] has rank 503, then T is injective.
*Proof.* rank_Q M ≥ rank_{F_p}(M mod p) = 503 (a non-vanishing 503-minor mod p is non-zero in Z_(p)). So T(f_i) are independent, hence f_i independent, hence a basis of V (dim 503). Then T(V) has dim 503 = dim V, so ker T = 0. ∎
**Corpus facts:** W1 (ee9c36f9…) §4: rank 503 at p=7840981, 7946821; EXACT-CRT (8061c7b2…): rank 503 at 6 primes p≡1 mod 980, rational RREF 503×648 (sobj 74d8eb15…), held-out verified.
**Remaining premise (named gap G1-mem):** that the 503 kernel vectors of the polar system (solve36w.sage, Φ⊗h/Δ^m Ind construction) are q-expansions of genuine elements of V in char 0 with p-integral coefficients at a used prime. EXACT-CRT itself caveats "standard multi-prime modular certificate … not an independent char-0 lin[ear algebra]". Rank-equals-dim at good primes does not by itself certify membership/good-prime status.
**Why Sturm route does not close it:** Q18 Sturm (b3172d39…) applies Magnusson–Raum Prop 1.1 to the 89-dim cusp6 block only and requires all Ind components (all 56 cosets / cusps of Γ₀(49)); an ∞-only truncation is explicitly NOT covered. No on-disk Written premise transfers this to the 503-block.
**G1 STATUS: PARTIAL** — injectivity is proved conditional on G1-mem; G1-mem is a named gap (no invent). Refines, does not contradict, e1ca9141… C6 "GAP G1 unchanged" and OW 4103ea92… "G1/G4a remain OPEN for char-0". The earlier 503-BASIS GAP-ABSENT note "No a_ν mod p rows exist for N36" (a8547419…) is superseded by W1 (Written seed D₆⊕A₄⊕A₆ theta, Borcherds 1998 §4) — chronological, not a Soft SF inconsistency.

## 2. Packaging hygiene — N36–N6 FILLED-MODP under HOLD
Arithmetic (exact): 21/140 = 3/20 (gcd 7); 25/140 = 5/28 (gcd 5). So c28_e3/20 ≡ ν=21 and c25_e5/28 ≡ ν=25 under the /140 reading; matches OW 4103ea92… item 2 (reduced-fraction labels OK). Existing rows use mixed forms too (c9_e1/35 = 4/140, c20_e1/10 = 14/140, c6_e4/35 = 16/140) — so reduced labels are the house convention in basis column names; no new denominators.
Operative CSV (38534aa1…) N36 rows: ν∈{0 VACUOUS; 1,4,9,14,16,21,25 FILLED-MODP p=7840981}. All HOLD CF980 CERT-under-H_work.

Soft SF inconsistencies (list only; no edit made):
| ID | Issue | Severity |
|---|---|---|
| H1 | ν=21,25 rows' notes cite candidate 56e9be7d / FINDINGS 27b1c5e8 / OW fe16077f but do **not** carry the stamp `basis sha e707cc96` that OW 4103ea92… item 1 directs ("Stamp W1/basis for these rows = that basis under HOLD"); also not W1 ee9c36f9. Ν=1..16 rows carry it. | packaging, stamp-only |
| H2 | ν=21,25 source_cols use reduced label (c28_e3/20, c25_e5/28) while ν=1..16 source_cols use "seed comp N eν/140" form. Values equal; format non-uniform. | cosmetic |
| H3 | ν=21,25 notes say "nu>18 on-mesh-write" while on_mesh_N18=YES and ν/140<1 lies inside q^18 truncation (consistent with OW N6 correction of off-mesh label). The "nu>18" phrase refers to the schedule index, not exponent — ambiguous wording. | wording |
| H4 | GA1: operative CSV keeps simpson_weight=4 / fill_tier=1-odd-w4 for ext rows with NON-SIMPSON note, while GA1 annotation CSV has fill_tier=ext-write, simpson_weight blank (e1ca9141… C3 GAP-GA1). Still open. | semantic, carried |
| H5 | N36 side CSV (0e17098c…) w1_sha/basis_sha=NA-HOLD for ν21,25 (e1ca9141… C2 GAP-N1) — superseded in substance by OW 4103ea92… but not re-stamped. | stamp-only |
No value inconsistency found: all filled residues trace to e707cc96 basis columns via unique-match (27b1c5e8…). N6 rows (p=1027606441, basis 3fb6519f) not affected.
**Packaging STATUS: MATCH (values) / PARTIAL (stamps H1,H5; format H2,H3; GA1 H4).**

## 3. Rec A (recommend-first; not self-authorized)
Rec A-1 (Owner Write needed): authorize a stamp-only edit of operative MODP CSV and N36 side CSV for ν=21,25 adding `basis sha e707cc96; W1 sha ee9c36f9` (per OW 4103ea92… item 1), and optionally normalizing source_cols to "seed comp 28 e21/140" / "seed comp 25 e25/140" form. No residue change. HOLD CF980 kept.
Rec A-2 (Eigen, for G1-mem): either an independent char-0 check that kernel vectors lie in S₄ (e.g. verify modularity on generators S,T with the Written ρ̄ data already in W1 — only if Written; else stays gap), or a Written all-cusp Prop 1.1 extension to the 503-block. Not started; exact ν fill waits Eigen Soft SF FINDINGS + Owner Write.

## STATUS
Overall: **PARTIAL** — G1 PARTIAL (conditional proof; named gap G1-mem); packaging MATCH on values, PARTIAL on stamps/format. tip_pre = tip_end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91.
