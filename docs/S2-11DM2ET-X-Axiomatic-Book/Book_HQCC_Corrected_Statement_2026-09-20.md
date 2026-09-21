Book HQCC corrected statement
20 September 2026

Pack+(S). CORE_FREEZE holds.
Canonical T3 is not edited.
Twin Prime and RH unclaimed.
This note replaces the book HQCC theorem, the four book proofs, and the live 4880 table.
G4 remains the stipulated Category B clock of 5 September.

0. What was broken

The book treats three different objects as one theorem.
Map A. Canonical T3, the production map used by HQH-539.
Map B. The November charge-fix rule with residue 1 sent to (n-1)/3 and residue 2 sent through a search on k.
Map C. T3 applied a fixed 539 times after SHA3-512.
The book claims every physically allowed seed reaches 1 in exactly 539 plus or minus 1 steps. That is false of Map A, undefined of Map B at seed 4880, and tautological of Map C.

1. The production map, unchanged

T3(0)=0.
If n ≡ 0 (mod 3), T3(n)=n/3.
If n ≡ 1 (mod 3), T3(n)=(4n+2)/3.
If n ≡ 2 (mod 3), T3(n)=(2n+1)/3.
Integer division. No k. No mod-9 condition.
This is hqh539_core.py. CORE_FREEZE forbids replacing residue 1 by (n-1)/3.

2. What is actually true of Map A

0 is fixed. {1,2} is a 2-cycle.
4880 reaches 1 in 14 steps: 4880, 3253, 4338, 1446, 482, 321, 107, 71, 47, 31, 42, 14, 9, 3, 1.
20 reaches 1 in 5 steps. 21 reaches 1 in 6 steps.
T3 does not preserve residue modulo 9.
No general termination proof. Exact length 539 is false of every named book seed.

3. Map B is retired as the physical rule

At n=4880, no k preserves residue modulo 9. The first step is empty.
The printed 4880 to 1629 uses k=0 and lands at 1629 ≡ 0 (mod 9). Conservation fails on its own table.
Every n that is 2 mod 3 and 2 mod 9 is dead under Map B, including 4880 and 20.
Residue 1 is already a different affine map from T3.

4. Map C is a construction

HQH-539 applies T3 exactly 539 times. 539 is an input, the packaging COUNT 18+521.
On seed 4880 the raw orbit hits 1 at step 14. The rest of the 539 applications travel the 2-cycle.

5. Four book proofs withdrawn as proofs of raw 539-step termination

Banach: four unequal tokens share one name; T3 expands on residue 1; 539 enters and exits as N.
Generating function: pole location and 3^{-539} are inserted.
512-qubit: a simulator returning 539 on seed 20 is not running Map A.
Topology: cobordism does not emit 539 from T3.

6. 223×20+20×21=4880 is addition, not a map. Under Map A those seeds finish in 5 and 6 steps.

7. Replacement theorems

Theorem HQCC-A (map). T3 is a total integral map. Termination of every seed is unproved. Length 539 under unrestricted iteration is false of the named book seeds.

Theorem HQCC-C (construction). HQH-539 applies T3 a fixed 539 times. The 539 is an input.

Theorem HQCC-B (overlay, Category B). G4=539.90 s is a stipulated clock. It is not a corollary of HQCC-A.

8. The book may still say three generations as axiom, e^3 as a named series, N_flux=4880 as locked arithmetic, 18+521=539 as locked arithmetic, and T3 as the local rule of the hash primitive.

The book may not say that T3 or the charge-fix rule terminates in 539 steps, that Banach lambda equals ln3/539 and contracts T3, that 4880 goes to 1629 under a well-defined charge-fix, that 243 towers each run 538 or 539 raw steps, or that there are zero free parameters while G4 is stipulated.

9. Status

Old book HQCC retired. Map B retired. Four proofs withdrawn.
Canonical T3 unchanged. HQH-539 loop bound unchanged, labelled construction.
G4 unchanged, labelled Category B.
CORE_FREEZE unchanged. No new residual-flux object. TPC and RH unclaimed.
