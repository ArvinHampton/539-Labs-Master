# FINDINGS — MR1 FILL-FIRST mod-p Simpson/4Q cells (2026-10-26)
STATUS: PARTIAL

## Authority (sha256 verified at start)
- RHOS mod-p MATCH a8788e5c63c9f84d6bed66c808db5831ab751d9d0d930b8603fa7e25fedf2efd
- Exact-lift CLOSED_A 3cf5735ca0c2a61a0aeb5e7ed62de00cea47395ece07e4ed18b3330dfe2f2057 (Eigen owns exact lift; Rec A LOCKED; Eigen LIVE path (b))
- ASSIGN lift BEGIN 29ede292036d155f1eede8913609ba6a0b91ff5aa7daa956ee848bd117aec463
- 4Q OPERATIVE 11f104c7361970a2dc02b3f6300071a20d32cad76f0055a616ebded1974ebff2
- Dual OW 538a02d9…1436; Simpson mesh 98f996ae…2784 (N=18); prior absorb PARTIAL d2ce6132…8576 (cited, not re-hashed)
- Basis csv 3fb6519f0bef8db0af9e85f614b9139912a3174c750b34ed7765aa1aa9fcb749; m6.sobj 4183e07e7707fbf9cccc6f90db5323c18c7d66a2834f65fd55e805c963d617c0
- Schedule csv before: ad0a0ff3ce4150f746d7787ebc983129a39598048164331c0fec3e7beaf6e757

## Tip Soft SF
start = end = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91; tip_touched NO.

## invent HOLD
All filled values are mod p (p=1027606441), FILLED-MODP only. NOT exact / NOT char-0. No interpolation, no tip fold, no invented mapping. Exact char-0 cells remain OPEN pending Eigen exact FINDINGS under CLOSED_A.

## Cells
| family | ν | mesh | w | status | coefficient (mod p) | source |
|---|---|---|---|---|---|---|
| N6 | 1 | YES | 4 | FILLED-MODP | nz=1/89; form0=1 | a0_c0_e1/140 |
| N6 | 9 | YES | 4 | FILLED-MODP | nz=89/89; f0=854531552,f1=997863718,f2=809587200,… | a1_c0_e9/140 |
| N6 | 29,81,109,121 | NO | - | OPEN-OFF-MESH | - | - |
| N36 | 0 | YES | 1 | VACUOUS | n=0 cusp-form, 4Q §(d) | - |
| N36 | 1,4,9,14,16 | YES | 4/2/4/2/2 | OPEN-MAPPING-GAP | OPEN | no Written map |
| N36 | 21,25 | NO | - | OPEN-OFF-MESH | - | - |

Counts: FILLED-MODP 2 / VACUOUS 1 / OPEN-MAPPING-GAP 5 / OPEN-OFF-MESH 6.

## GAP
CSV columns are seed spectrum /140 (seeds a0..a5 ↔ {1,9,29,81,109,121}/140, cusps c0..c7). No Written mapping from N36 integer T-ord {1,4,9,14,16} to these columns exists; not invented.

## RECOMMEND-FIRST (N36)
- A = Owner/Eigen Written map N36 T-ord ↔ CSV /140 columns (recommended)
- B = leave N36 OPEN
- C = other

## Outputs
- /workspace/grok-batches/TE-SIMPSON-FILL-MODP_N18_2026-10-26.csv b869010b22f931e15fc3c80d43f4a9b504641dc40211a9adeaf85eb1c2b1e9dd
- schedule csv (in place) after: 3f8343336d668738e41dcf9808826329008811fa9be64b8d8f1c8abcc5186238
