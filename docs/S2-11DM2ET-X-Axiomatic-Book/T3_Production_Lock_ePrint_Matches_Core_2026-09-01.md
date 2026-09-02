T3 production lock
ePrint matches core
2026-09-01

Pack+(S). Residual-flux provenance mandatory. RESIDUAL_CORE_FREEZE holds.
Twin Prime and RH unclaimed. HQH-539 hardness Category B.


1. Question

Does the IACR ePrint manuscript use the correct T3 map.


2. Answer

Yes.

The submitted map in IACR_ePrint_128_LQH_HQH539512_2026-09-01 is the production map. It matches hqh539_core.py version 1.2. It matches ePrint Table 1 orbits. It is the three-branch rule.

T3(0) = 0.
For n > 0 let r = n mod 3.
If r = 0 then T3(n) = n // 3.
If r = 1 then T3(n) = (4n + 2) // 3.
If r = 2 then T3(n) = (2n + 1) // 3.
On residue 2, (2n + 1) // 3 equals (2n − 1)/3.

Closed form after the residue is known:
T3(3k) = k
T3(3k + 1) = 4k + 2
T3(3k + 2) = 2k + 1

Last-bit table under this map:
classes 0, 1, 4 modulo 6 give Bit_next = 0
classes 2, 3, 5 modulo 6 give Bit_next = 1
This is a 3+3 split. H(Bit_next | Class_6) = 0. H(Bit_next) = 1. I(Bit_next ; Class_6) = 1. H(Class_6 | Bit_next) = log2(3).


3. What is not Canonical T3

The single formula (4n + 2)//3 applied to every n is not the production map. It disagrees on class 3. It is a 4+2 split. It is not to be called Canonical T3.

T4121, residue-1 branch (4n+1)//3, is historical. It is not the hash map.

The style-guide HQCC writing with a 3^k charge fix on residue 2 is not the HQH-539 production map.


4. What was not deleted

CORE_FREEZE, Pack+(S), Bridge C, residual series, A4+/A5+, the ePrint itself, hqh539_core.py, the 28 August wire note, and the 1 September entropy papers that already use the three-branch rule.

Those files do not present the affine-everywhere formula as production. Notes that name the affine formula only to reject it are comparison notes. They stay.

The project-memory shorthand "Canonical T3 ((4n+2)//3) is production map" is retired. That sentence names only the residue-1 branch. It is not the whole map.


5. Status

Status code:
T3_PRODUCTION_LOCK_EPRINT_MATCHES_CORE_2026-09-01
THREE_BRANCH_ONLY
AFFINE_EVERYWHERE_NOT_CANONICAL

CORE_FREEZE unchanged.
