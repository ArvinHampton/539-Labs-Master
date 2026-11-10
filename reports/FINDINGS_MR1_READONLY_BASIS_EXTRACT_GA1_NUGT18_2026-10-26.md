# FINDINGS — MR1 read-only basis header extract + GAP-GA1 ν>18 semantics (Soft SF Write-only) — 2026-10-26 ~18:00 CDT America/Chicago
Role: Math Research 1, COOK + Rec A AUTO. Proof standard. Cat-A invent: NONE. No char-0. No Eigen agent wake/contact; no eigen-* script run; CF980 runner NOT run.

## Authority (live sha256 verified, all MATCH)
- OWNER_WRITE 75c176bec2fad0beccf372a60e6285ff41cdb62e6a08b711bb70baee616e426b
- ASSIGN b679276cc45a554fafaa62084603791e55be726630d98b64a2fcaa01b66e1d35
- Source FINDINGS free-pursue e1ca9141de1b646e73aacf92b4b5a3ee7bce480527822d556186b87b19d7440b
- tip_pre = tip_end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (tip_touched NO)
- Basis N36 e707cc96b0cf9c40d671a78c164bcdff5e4f7f81915bc47782e3a909c74f984c (read-only, MATCH pre & during extract)
- Basis N6/q89 3fb6519f0bef8db0af9e85f614b9139912a3174c750b34ed7765aa1aa9fcb749 (read-only, MATCH)

## 1. Header extract (method: parse header row, exponent from `_e<p/q>` suffix, ν = e·140 exact rational)
Extractor: mr1-basis-header-extract/extract_headers.py sha 6babdde496978f2c5ec2a35516a6e9424e341fb33421b0bf4f7747a3af21ea86 (MR1-authored, not under eigen-*; asserts basis sha before parse).
| family | data rows | columns (excl. index) | e·140 ∈ ℤ | on-mesh cols | GAP-E-candidate cols |
|---|---|---|---|---|---|
| N36 (e707cc96) | 503 | 648 | 648 | 7 | 641 |
| N6 (3fb6519f; 1 `#` comment line skipped) | 89 | 6048 | 1512 | 60 | 1452 |
- N36 on-mesh: ν=1 c31_e1/140 (nz 338/503); 4 c9_e1/35 (1); 9 c34_e9/140 (327); 14 c20_e1/10 (1); 16 c6_e4/35 (1); 21 c28_e3/20 (40); 25 c25_e5/28 (1, row 446). **ν=0: no column present (no e=0 header) — note, not a gap closed here.**
- N6 on-mesh: each ν∈{1,9,29,81,109,121} occurs across (seed comp a, cusp rep c0..c7); 60 columns total. Seed cusp-inf columns a0_c0_e1, a1_c0_e9, a2_c0_e29, a3_c0_e81, a4_c0_e109, a5_c0_e121 reproduce operative first3 in TE-SIMPSON-FILL-MODP / N6_D1_nu_columns_modp.csv exactly.
- Artifacts: HEADERS_INVENTORY_2026-10-26.csv sha 3593f1ed01ab8e68e26171792007528aaed41f525d462f6f303acc93272bf9dd (6696 rows); ONMESH_NAMED_COLUMNS_2026-10-26.csv sha 2cbb05ff2af634a0ba7d7971e932e75f048275df764a93f4fa39ef8c6920e0dc (67 rows; nz, first3, full basis_sha; no full vectors — provenance closes via basis sha + col index).

## GAP-N1 — CLOSED
N36 ν=21 (col 505 c28_e3/20, nz 40/503, first 0:1960245;1:2940368;3:4900613) and ν=25 (col 451 c25_e5/28, nz 1/503, 446:1) read directly from basis e707cc96…(full sha stamped in ONMESH CSV). Match operative TE-SIMPSON-FILL-MODP rows and candidate CSV 56e9be7d values.

## 2. GAP-GA1 — CLOSED (annotation) under OW 75c176be
- GA1_ANNOTATION_EXT_ROWS: 6 rows (N36 21,25; N6 29,81,109,121) fill_tier ext-write → `on-mesh-write`; simpson_weight → `N/A`. before a183dddd608cda1c90630fdc31e9e20806ccef1a1d2c5b0a7745c0b565d80529 → after d34051790256da244acd18f19f7af5440456dcc4725d057200a78e6931a03fbf (sidecar refreshed).
- Operative CSVs: w=4 / 1-odd-w4 LEFT; same 6 rows notes stamped `NON-SIMPSON …schedule label only…`. Status FILLED-MODP unchanged (13/13 rows still FILLED-MODP), HOLD CF980 kept.
  - TE-SIMPSON-FILL-MODP_N18: 453d3c4fc1607465ec37d67c9c13a4963256eaa84fddacee7637508ad3e6ecfd → 38534aa1102da03cf96d7d76cdd454f8ef0530c4ef12439ec0cbf3c4346010f3
  - TE-SIMPSON-FILL-SCHEDULE_TORD_N18: f7ec76eff6b8888039e65cac8babaecd47285699fedca6577ca20df3ca2a6ea5 → 4de5113b477836c6347d33d7142d4dfcdfd001fbb1b32085b62f5b2fabb6976e
  - Pre-edit copies: mr1-basis-header-extract/backup_pre_edit/. Diff = exactly the 6 ν>18 rows.

## GAP-E — OPEN (named)
Integer-ν columns outside the on-mesh residual-C set exist without residual-C Write: N36 641 cols (distinct ν starting 29,30,36,44,46,49,50,…,2520); N6 1452 cols (distinct ν 21,41,49,61,69,89,101,…,2509). Full list in HEADERS_INVENTORY (class=GAP-E-candidate). No mesh membership claimed. Plus N36 ν=0 absent from basis headers.

## STATUS: MATCH
Extract + GA1 annotate done under OW. FILLED-MODP HOLD CF980. G1 OPEN, Kerr BLOCKED unchanged. Eight-only stands.
## Rec A
(a) Owner decide whether N36 ν=0 absence is expected (constant term outside basis) or a GAP. (b) GAP-E scoping Write needed before any of the listed ν are treated on-mesh.
