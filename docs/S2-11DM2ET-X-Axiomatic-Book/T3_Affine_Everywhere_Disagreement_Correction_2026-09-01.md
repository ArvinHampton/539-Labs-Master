T3 affine-everywhere disagreement correction
2026-09-01

Pack+(S). Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds.
Twin Prime and RH unclaimed. HQH-539 hardness Category B.


1. Production map

Canonical production T3 is the three-branch rule in the IACR ePrint manuscript and in hqh539.py:
residue 0: n // 3
residue 1: (4n + 2) // 3
residue 2: (2n + 1) // 3

The IACR ePrint uses this map. The answer to the user question is yes.


2. What affine-everywhere is

The single formula T_aff(n) = (4n + 2) // 3 applied to every n is not Canonical T3.

Closed-form comparison after writing n = 3k + r:
T3(3k) = k.          T_aff(3k) = 4k.         Disagree for every k ≠ 0.
T3(3k + 1) = 4k + 2. T_aff(3k + 1) = 4k + 2. Agree.
T3(3k + 2) = 2k + 1. T_aff(3k + 2) = 4k + 3. Disagree for every k ≥ 0.

Affine-everywhere therefore agrees only on residue 1. It disagrees on residue 0 and on residue 2. That is two of the three residue classes, not one class modulo 6.

On 0 through 59 there are 39 disagreements. Examples:
T3(2) = 1, T_aff(2) = 3.
T3(3) = 1, T_aff(3) = 4.
T3(5) = 3, T_aff(5) = 7.
T3(6) = 2, T_aff(6) = 8.

The earlier lock sentence that affine-everywhere "disagrees on class 3" is too narrow. Class 3 modulo 6 is only one slice of residue 0. Residue 0 also contains class 0. Residue 2 contains classes 2 and 5.

Shannon leftover numbers that belong to affine-everywhere, including 5/3, are retired from the production ledger. Production leftover numbers are the 3+3 table only.


3. What was not deleted

No production file was deleted.
No CORE_FREEZE file was deleted.
Comparison notes that name T_aff only in order to reject it stay.

Historical June 2026 Drive files that define Canonical T3 correctly and then call T4121 "superior production" were not deleted. They are labeling history, not an affine-everywhere production error. Inventory:
Drive 1A6Jxy0DVzObo8yvtuqJ7qnxozB8LspFSGnOyM-0GknI, title New and superior Primitive; T3 is canonical, T4121 is superior.
Drive 1SlfZICrE31HmOUM4ynP_07kaIXy2tEcE and 1pWEULB-vJRhJCJc4AjXkdlWZ-jut4Dnh, proprietary statements that use the same historical label.
Those files keep T4121 as a named variant. They do not replace the ePrint map.

T4121 itself, residue-1 branch (4n + 1) // 3, remains a historical comparison object. It is not the hash map.


4. Status

Status code:
AFFINE_EVERYWHERE_DISAGREES_RESIDUE_0_AND_2_2026-09-01
EPRINT_T3_IS_PRODUCTION_THREE_BRANCH
NO_MASS_DELETE

CORE_FREEZE unchanged.
