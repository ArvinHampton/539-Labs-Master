# FINDINGS — MR1 N6 mod-p "q^121" + Lemma D1 + GA1 annotate (Rec A AUTO) — 2026-10-26
Executor: Math Research 1 · Soft-SF Write-only · tip_touched NO · proof standard (proof OR named gap) · Cat A invent: NONE · No Eigen contact (Eigen on-disk artifacts read-only, cited)

## 1. STATUS
**MATCH (mod p) for all four N6 ν ∈ {29,81,109,121}; char-0 OPEN (G1 stands).**
Key structural finding (PROOF, on-disk): in the N6 lane, ν is the **T-exponent numerator over 140** of seed component a (ν = 1,9,29,81,109,121 ↔ a = 0..5; seed T-exponents {1,9,29,81,109,121}/140 per RHOS-SOLVE). The existing FILLED-MODP cells N6 ν=1,9 are exactly the basis-csv columns `a0_c0_e1/140`, `a1_c0_e9/140`. Hence the ν∈{29,81,109,121} cells are the columns `a2_c0_e29/140`, `a3_c0_e81/140`, `a4_c0_e109/140`, `a5_c0_e121/140`. Their q-exponents (29/140 … 121/140 < 1) already lie **inside** the q^18 truncation. The "ν>18 / off-mesh" label in the schedule CSV conflates ν with an integer q-power. So **no compute past q^18 (no literal q^121 run) is needed**: the values are read from the on-disk 89×6048 mod-p basis. D1 applies trivially (c_ν is a coordinate of π_S).
GA1 annotation: written to a separate artifact (FINDINGS-only pattern). Operative CSVs are **not mutated**.

## 2. Authority (live sha256 verified 2026-10-26 ~17:45 CDT America/Chicago)
| Item | sha256 | Result |
|---|---|---|
| OW GA1+N6 mod-p | 8690275accfb1f67fb1b8fea12d312bc0f53ba3abb323e9f2d733474e342f50a | OK |
| ASSIGN | 261c9cb297967e4a812a4221501ab2e2eb5ed84a4e904c1ba705a794b600b061 | OK |
| Source mesh FINDINGS (D1 PROVED) | 143080bc81786e8037965fef5deba53f45061e86f644780624c60f3a1410b749 | OK |
| CF980 OW hold | ee3260468b890c8922274c1aa3bb4eec14c806032fc8814291b5061fce7bbb86 | OK |
| Schedule CSV (read-only) | d3f12c981ec72b901ae7e97b76ac4a70c9cdd356ddda2eb5a721453d656f56f9 | unchanged |
| Mod-p CSV (read-only) | 9df646a935931fb70a523edf4e52190bbb08381fd24b51d8c4441873d827ccf3 | unchanged |
| Step3 MATCH (dim 89, q^18 injective) | 88911d8c71ae8e4fd791b944227aaa116c12241365ca985d4376341dfb32959a | cited |
| RHOS-SOLVE MATCH mod p | basis csv 3fb6519f0bef8db0af9e85f614b9139912a3174c750b34ed7765aa1aa9fcb749 (re-hashed live OK); q89_modp_m6.sobj 4183e07e… | cited |
| Tip residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | tip_pre = tip_end; READ ONLY |

## 3. GA1 table (fill_tier / simpson_weight semantics per OW 8690275a)
| family | ν | on_mesh | fill_tier | simpson_weight | coeff this run |
|---|---|---|---|---|---|
| N36 | 21 | YES (Write-ext OW 5a766b35) | ext-write | (blank, N/A) | OPEN (out of scope; 503-block G1) |
| N36 | 25 | YES | ext-write | (blank, N/A) | OPEN (same) |
| N6 | 29 | YES | ext-write | (blank, N/A) | MODP-D1 (§5) |
| N6 | 81 | YES | ext-write | (blank, N/A) | MODP-D1 (§5) |
| N6 | 109 | YES | ext-write | (blank, N/A) | MODP-D1 (§5) |
| N6 | 121 | YES | ext-write | (blank, N/A) | MODP-D1 (§5) |
Artifact: `grok-batches/mr1-n6-modp-q121-d1/GA1_ANNOTATION_EXT_ROWS_2026-10-26.csv` sha a183dddd608cda1c90630fdc31e9e20806ccef1a1d2c5b0a7745c0b565d80529. No operative CSV mutated: no before/after needed.
Note for Owner: since N6 ν are /140 exponents inside q^18, the "ext-write" tier for the N6 rows is a label of convenience only. A future Owner Write may reclassify N6 ν∈{29,81,109,121} as on-mesh-N18 (they are columns of the q^18 data). The same /140 reading likely applies to N36 ν=21,25 (CSV `seed comp … e{ν}/140` pattern). Not asserted here: the 503-block is out of scope.

## 4. Compute method + cites
- Script `mr1-n6-modp-q121-d1/extract_d1.py` (sha 2e2a67c29407918aa89eb6c34eb7de94411d7e0f347588d40341ffbdc5c3d976). It is a pure read of the on-disk basis csv 3fb6519f… (89 forms × 6048 slots over GF(1027606441), Eigen RHOS-SOLVE m=6, 8-cusp truncated holomorphic). It does: (i) assert p from the header; (ii) Gaussian elimination mod p gives **rank 89** (re-verified live); (iii) extract column `a{a}_c0_e{ν}/140` for each ν.
- Log `extract_d1.log` sha 1f13f4af556ce323be615318368ec8b7608d5501f91ab51217c5b38cb0ba72a7.
- Output `N6_D1_nu_columns_modp.csv` sha 9b9b73c04564f257bc2a7da9a57efb696e69e550e2a66a4da842ba9cacb26429 holds the full 89-vectors.
- **Convention check (PROOF of the ν↔column identification):** the script reproduces the existing FILLED-MODP cells bit-for-bit: ν=1 → nz=1/89, first=0:1; ν=9 → nz=89/89, first=0:854531552;1:997863718;2:809587200. Both equal mod-p CSV 9df646a9….
- No new Sage solve was run. No literal integer q^121 truncation was computed, and none is required (§1).

## 5. Per-ν results (D1 over F_p, p = 1027606441)
Value format = same as the FILLED-MODP cells: the leading cusp-∞ coefficient of seed component a, as an 89-vector over the echelon basis (full vector in the output csv).
| ν | column | nz | first 3 (row:value mod p) | Status |
|---|---|---|---|---|
| 29 | a2_c0_e29/140 | 89/89 | 0:225650609; 1:522387538; 2:367160988 | **PROOF (mod p)** |
| 81 | a3_c0_e81/140 | 89/89 | 0:200307986; 1:78319815; 2:139970354 | **PROOF (mod p)** |
| 109 | a4_c0_e109/140 | 89/89 | 0:6839830; 1:583863915; 2:778245974 | **PROOF (mod p)** |
| 121 | a5_c0_e121/140 | 89/89 | 0:754394536; 1:881713098; 2:82808653 | **PROOF (mod p)** |

**D1 application (PROOF over F_p):**
- K = F_p and M = the row space of the on-disk basis (dim 89, rank re-verified).
- π_S = restriction to the 6048 slots through q^18. It is injective on M because rank = 89 = dim M.
- Each c_ν is itself a coordinate of π_S, so λ_ν = coordinate projection, and the value is the column above.

**Scope of the proof:**
- The statement is about the F_p space computed on disk.
- Identifying it with the reduction of the true char-0 M₄(ρ̄|cusp6⊗Ind) is **G1 (OPEN)**. Mod-p rank 89 counts as evidence only, per RHOS-SOLVE's own caveat. The ansatz is not full (zeta49-CRT FINDINGS).
- Values depend on the z49 choice in the original run (uncoordinated q89_modp_m6.sobj, same as the ν=1,9 fills). They are consistent with the existing FILLED-MODP convention.
- No char-0 values are claimed.

## 6. Hold / Posture
- The 7 FILLED-MODP exact cells stay **HELD** pending in-set CERT under CF(980) + CRT p≡1 mod 980 (OW ee326046…). G4a ℚ(ζ₄₉) containment OPEN.
- The 4 new N6 mod-p values are **not** written into the operative CSVs. They join the HOLD queue as MODP-D1 candidates; promotion requires an Owner Write.
- W₇-slash on V₄₂ REFUTED (G2), not reopened.
- No Eigen contact. No tip fold. tip_pre = tip_end = 7cddb188…, tip_touched NO. Kerr BLOCKED. SCOPE EIGHT. No char-0 invent.

## 7. Rec A
Owner Write: (a) adopt the ν=/140-exponent reading and promote N6 ν∈{29,81,109,121} to FILLED-MODP (MODP-D1, artifact 9b9b73c0…) under HOLD, correcting the "ν>18 off-mesh" label; (b) check the same /140 reading for N36 ν=21,25 against the 503-block columns; (c) keep all MODP cells HELD for the CF(980)/ζ₄₉ CRT CERT (G1/G4a). No Eigen.
