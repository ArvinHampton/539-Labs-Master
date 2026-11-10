# MERGED VANISHING MAP — living stub (2026-10-26, re-merge 3)
Status: STUB / proposed only. Not an Owner Write. Bridge PARTIAL / READY NO. tip_touched NO; tip Soft SF LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` not edited. Soft SF F3 CLOSED. Soft SF invent HOLD tip fill else.

## Inputs (box-verified sha256)
- BASE: CORPUS_VANISHING_INVENTORY_2026-10-26.md `fb2983460ebadf7c8fe1d934d33ae05d57d725fcbf716933edb7780d273756c0` (31 rows)
- PRIMARY compiler: grok-batches/MR1-AUTHOR-REVERSE-ENGINEER-ALL-VANISHINGS_2026-10-26.md `1a94765c40024c290e59e6d9707e6287bbb5b159682f6976a22369a06aec15a4` (PARTIAL)
- MR2 AMENDED: MR2-FINDINGS-CORPUS-VANISHING-MAP_2026-10-26.md `b271f42ab1cf0a3407e82f47d793ac549f056226805e9e29fa942f8808f629b9` (replaces PARTIAL 28d9913c…)
- Local: grok-batches/LOCAL-VANISHING-MAP_2026-10-26.md `bb6f4011b470b231b7014ea3bf9faa759bdcac2d61d7642d38ecfd29e7d10a9f`
- PR2: FINDINGS_PR2_VANISHING_SWEEP_COSMO_BIO_NEURO_2026-10-26.md `df90a896a59e9c5103d4c8b3501fe4e83d5721e53d1612874705f3ea10efacf5` (2 rows)
- PR1: PR1-FINDINGS-CORPUS-VANISHING-MAP_2026-10-26.md `d76991c3f3ae7c8621d5c27d9556c8bafd74a307930a8e137b8320da967f6d61` — modular κ/k ABSENT
- DF: FINDINGS_DF_CORPUS_VANISHING_MAP_2026-10-26.md `2526d282246bea6de8b01019f5d415a84ab492ec3d70efdac70141c26bcc663a` — modular κ/k ABSENT; DF-1…19 NOT mapped onto R1–R6
- Prior stub (re-merge 2) `d485dd0c7c603f0fc4273fb0cb4f69f8e19e6282f0dd134b5ef6eab2a165a100` superseded.
Dedupe key: (space, κ, k, claim). CI# = CORPUS inventory row; MR1 V#; MR2 V-ID; L = Local V#. Rank: MR1 V1–V4 first, then informativeness.

## ⚠ CONFLICT FLAGS
- **C1 (P5a):** tip W-P5a-OP L410 / Local V1,V3 = **OPEN-CLAIM** ("to prove") vs MR1 `b829661e…` (+MR1 V3, MR2 V-P5a-FAIL, CI#4) **proposed FAIL dim 592**. FAIL is proposed only — not Owner-Written, not Auditor MATCH, not folded. Route to Owner/Auditor; k/route → Arvin.
- **C2 (Soft SF F3 vs R1/T-A):** MR1 V4 / CI#13 numeric ρ(−I)=S_lab⁻²=I on V₄₂ vs tip L230–231 F3 CLOSED "ρ(−I)=Id NOT confirmed; operative S_lab⁻²" (Local V15). R1/T-A needs Owner Write reconciling F3 before any use. Also R1 is vacuous.
- **C3 (V11 numerics):** κ=6..12 dims claimed but `MR1-P5A-reverse-dimcalc_2026-10-26.out` is 0 bytes — not reproduced on-box.

## Rows
| rank | space | κ | k | claim | status | source | sha | backwards |
|---|---|---|---|---|---|---|---|---|
| 1 | Fix_{Γ₀(49)}(V₄₂) for ρ, ρ̄ [MR1 V1; CI#6; MR2 V-INV0] | — (κ=0 relevant) | — | = {0} | numeric/proposed (min sv 3.67) | MR1 P5A-VANISHING §2; MR1 reverse-all | b829661e2a6b / 1a94765c4002 | No constant-vector witness; feeds R2 (nonvacuous M₀=0) |
| 2 | Soft SF F3: S_lab⁻² ≠ Id globally; ρ(W₇) ABSENT [MR1 V2] | — | — | Fricke Role A absent | Written Soft SF CLOSED | tip LOCK | 7cddb188ca34 | Path A/V₈₄ closed; no W₇ cut — do not reopen |
| 3 | S₄(Γ₀(49), ρ̄), operative P5a, no cut [MR1 V3; CI#1–5; MR2 V-P5a-FAIL≡V-THETA-SLICE; L V1,V1a,V3,V4] | 4 | −2 | = {0} | **CONFLICT C1**: tip OPEN-CLAIM (to prove) vs proposed FAIL dim 592 (ρ conv 573; leading 588) | tip L410; OWNER_WRITE_P5A_REWRITE (cite-only); MR1 FAIL; dimcalc .py | 7cddb188ca34 / 0e1c7cac9713 / b829661e2a6b / 0ecd4166edd3 | Full 42-dim ρ̄ at κ=4 fills; need cut, κ≤2, or route change; BF/KM obstruction not cleared |
| 4 | ρ(−I)=S_lab⁻²=I on V₄₂ [MR1 V4; CI#13; L V15] | — | −2 | central char trivial | numeric/proposed; **CONFLICT C2** w/ F3 | MR1 reverse-all; tip L230–231 | 1a94765c4002 / 7cddb188ca34 | Feeds R1 parity kill; Owner Write must reconcile F3 |
| 5 | S₂(Γ₀(49), W⊂V₄₂ isotypic) [R3; CI#10; MR2 V-R3] | 2 | 0 | vanish on cut | CONDITIONAL / IN FLIGHT (not computed); leading 196 pre-cut | MR2 CONNECTION; MR1 reverse-all R3 | 2b49ca25e960 / 1a94765c4002 | Only nonvacuous k≤0 route; needs isotypic decomp |
| 6 | M₀=S₀; M_κ κ<0 (Γ₀(49), ρ̄) [R2; CI#9; MR2 V-R2; T-B] | ≤0 | ≥2 | vanish | proposed Cat B; route change vs P3 k<0 | MR2 CONNECTION; MR1 reverse-all | 2b49ca25e960 / 1a94765c4002 | Fix=0 ⇒ no constants; unitarity κ<0 |
| 7 | M_κ(Γ₀(49), ρ̄) odd κ [R1; CI#8; MR2 V-R1; T-A] | odd (3) | odd (−1) | vanish | proposed, **vacuous**; blocked by C2 | MR2 CONNECTION; MR1 reverse-all | 2b49ca25e960 / 1a94765c4002 | Parity kill via ρ̄(−I)=I; Bridge close likely unacceptable |
| 8 | S_κ(Γ₀(49), ρ̄) κ=6,8,10,12 [MR1 V11; CI#12] | 6–12 | −2 | ≠0 (984, 1376, …) | proposed; **C3** not reproduced | MR1 reverse-all; script | 1a94765c4002 / bfd0141a873c | Raising κ never frees vanishing |
| 9 | Newspace / W₄₉-on-Perm cut [R4/R5; CI#11; MR2 V-R4,V-R5] | 4 | −2 | cut → 0 | FAIL diagnostic (S_new≈581; W₄₉ ~½) | MR2 CONNECTION; MR1 reverse-all | 2b49ca25e960 / 1a94765c4002 | Reduces 592 not to 0; R5 Perm-side only |
| 10 | S₄(SL₂ℤ, ρ̄) sub-witness | 4 | −2 | ≠0 dim 11 | proposed | MR1 P5A-VANISHING §4 | b829661e2a6b | Independent refutation of P5a |
| 11 | Teitelbaum/BT Steinberg-at-7 slice [R6; CI#14; MR1 V12; MR2 V-BT-SLICE,V-R6] | 4 | −2 | slice vanish | PARTIAL Cat B; no numeric dim | MR2 CONNECTION | 2b49ca25e960 | Old+supercuspidal remain |
| 12 | S₄(ρ_D) Weil dictionary [CatB-1; CI#15; MR2 V-CATB1] | 4 | −2 | = 0 | FAIL (size bound); dictionary not Written | MR2 CONNECTION / Discipline | 2b49ca25e960 / dc0420a8e09c | Weil route cannot rescue κ=4 |
| 13 | BF S_{κ,L⁻}=0 as residual-C thm / dual-cusp obstruction [MR1 V10; CI#16; MR2 V-BF-OBS; L V13] | 2−k | <0 | vanish | NOT claimed; template only (Opt 1 closed) | tip L463,L483 §8; B-DIG | 7cddb188ca34 / a3e4523992d5 | Close only if dual space vanishes — ties to rank 3 |
| 14 | Hom(V⊗χᵏ, ℂ) A35 lawspace [MR1 V5; CI#25] | — | all | = 0 | Cat A | A35_lawspace_exact/REPORT.md | 57b6f24c70d4 | Law not ρ₃₅⊗χ object |
| 15 | Hom(ρ₃₅*⊗χᵏ, ρ₇\|W*) + metaplectic Hom [MR1 V6,V7; CI#26] | half-int | listed | = 0 exc. listed | Cat A | A32_35_to_rho7/REPORT.md | fc92193b6e19 | Lattice automorph / central −1 mismatch |
| 16 | tr_C ρ(S)=0 ⇒ dim C⁺=C⁻ (s-family) [CI#27] | — | s | trace = 0 | Cat A ledger | LEDGER_CatA_clean_v8/LEDGER.md | dc060d05932a | s=10 ⇒ C=0 |
| 17 | Fix(S_lab⁻²)=0 wall / wrong-parity wall [CI#24; L V5; MR2 V-FIX0-WALL] | any | −2 | wall kills forms | non-occurring (dim Fix=42), Cat B Owner Write | tip L256,L267 | 7cddb188ca34 | R1 relies on ρ̄(−I)=I, not Fix=0 |
| 18 | Cusp constant terms at 0, a/7 [CI#21; L V6] | n/s | (−2) | vanish | Written tip (default t1688u) | tip L361 | 7cddb188ca34 | P4 c = const term at ∞ only |
| 19 | Principal parts at 0, a/7 [CI#22; L V7] | n/s | (−2) | vanish | Written tip | tip L359 | 7cddb188ca34 | supp(Q)=∞ only |
| 20 | δ_W7 h ≡ 0 residual identity [CI#28] | wt-3/2 Ξ | — | vanish | sample only; NOT proved | RESIDUAL_IDENTITY_HUNT; order76 | ee4f4fc0d55e / 49d13fd3693a | Samples at x=1/7,3/7,5/7,1 |
| 21 | L-1 δ≡0 / RG76d / μ₁₀ packaging [CI#30; L V9–V11] | — | — | δ≡0 | NOT forced / HOLD | Local; AUTHOR_ACCEPT_t1129u | bb6f4011b470 | L-1 OPEN |
| 22 | RG2 c1-end shadow pieces vanish together on ρ_u [CI#29] | — | — | vanish | prereg (Cat A lemma corollary) | order16/PREREG.md L38 | d0cafdcf6367 | — |
| 23 | Historical W₇-part of S_{2−k,L⁻} (Γ₀(49)⁺) [CI#17; L V2; MR2 V-HIST-P5a] | 2−k | <0 | = {0} | SUPERSEDED §1w | tip L100,L412 | 7cddb188ca34 | W₇∉G, P2 VACATED |
| 24 | J_{2,49}=0 / DMZ Δ=0 coeffs [CI#18,19; L V13,V14] | 2 | 2 | vanish | SUPERSEDED option menu / not claimed | tip L463,L554,L648 | 7cddb188ca34 | DMZ W₄₉ wall ruled out PF-2 |
| 25 | W₇ ±1 eigenspace cut | 4 | −2 | cut vanish | RULED OUT (PF-2 Written) | OWNER_WRITE_MR1_FIX_DEDUCE_PF1_PF2 | e990cb379d85 | W₇∉Γ₀(49) |
| 26 | 49a line under W₇ [CI#20; L V12] | 2 | 0 | vanish | NOT claimed | tip L443 | 7cddb188ca34 | — |
| 27 | Harmonic Maass/Zwegers congruence route [CI#31] | — | — | obstruction-closed | heavy-daily note | heavy-daily/2026-08-21-18-ingest.md | a6b1dc4317ae | Residue vanishing ≠ boundary limits |
| 28 | V₄₂ components of Q / P4 other T-inv comps [MR1 V8; CI#23; L V8; MR2 V-COMP] | N/A | N/A | absent | ABSENT / no claim; blank open | tip L108; B-DIG | 7cddb188ca34 / a3e4523992d5 | Components blank — Arvin |
| 29 | P2′ vacuous after P2 VACATED [MR1 V9] / Role B force of P2 [MR2 V-ROLEB-P2] | — | — | vacuous/absent | Written Soft SF / ABSENT | tip PF-1+PF-2; Role B | 7cddb188ca34 / 42cca9d08c49 | P2 VACATED stands |
| 30 | Geom→alg residual multipliers [MR2 V-GEOM-MULT; L V16] | N/A | N/A | absent | CLOSED-ABSENT (NL; not modular) | GEOM-RESIDUAL-CLOSED | 350b6229b8af | Keep NL separate |
| 31 | STREAM ABSENT hunts t808u/t809u [L V17] | — | k<0 | no Written forcing | ABSENT | STREAM L51–58 | df3d17da99d7 | — |
| 32 | scalar S₄(Γ₀(49)) dim 10; scalar S₂(Γ₀(49)) >0 [CI#7; MR2 V-SCALAR-S2] | 4 / 2 | — / 0 | baseline | numeric nonzero | MR1 §3 | b829661e2a6b | Sanity anchors |
| 33 | Hampton 9 Maths / Φ [MR2 V-9MATHS] | N/A | N/A | no modular claim | continuum Cat B | Hamptons_9_Maths… | b271f42ab1cf | Not R1–R6 |
| 34 | PR2: P5a digest tag "to prove" (Γ₀(49)⁺ wording superseded) | 4 | −2 | — | dup of rank 3 OPEN side | framework-digest-PR2.md L190 | df90a896a59e | — |
| 35 | PR2: Ω_K=0.0007±0.0019 flatness | N/A | N/A | observational zero | measured; no residual-C link | obs-data-PR2 L39 | df90a896a59e | Non-modular |
| 36 | PR1-N1/N2 no-signalling; SME κ̃ bounds (κ̃≠modular κ) | N/A | N/A | null constraints | non-modular; PR1 modular κ/k ABSENT | obs-data-PR1-HEPP-QM-GR.md | 6c680789ff64 / d76991c3f3ae | Context only |
| 37 | DF lane DF-1…19 | N/A | N/A | — | modular κ/k ABSENT; not mapped to R1–R6 | FINDINGS_DF_CORPUS_VANISHING_MAP | 2526d282246b | — |

## Gaps
R3 isotypic dims not computed; V11 .out empty (C3); no Teitelbaum numeric dim at 49; no Owned Weil ρ_D table; MR1 reverse-all still PARTIAL. Do not tip-fold R1–R6/CatB/T-A–T-D without Owner Write + Auditor. tip_touched NO.
