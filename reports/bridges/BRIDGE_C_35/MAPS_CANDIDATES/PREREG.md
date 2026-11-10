# PREREG: MAPS_CANDIDATES — Residual↔Resonant candidate maps for Bridge C
Written 2026-10-24 ~5:05 PM CDT, before any test in this folder. Owner: Arvin Hampton. Parent folders (order2–order12, REVIEW_PARALLEL) read-only; new files only; CORE_FREEZE. All maps are **Category B** until proved. A pass is a *survived prediction*, never a proved Residual–Resonant bridge. Numerical near-miss ≠ pass. Runs: nice, OMP_NUM_THREADS=1, ulimit -v 3000000.

Sources for the residual side (verbatim facts only): oct17-master/README.md (T3 map; |O_res| = B′ = 539), grok-chats/02-pure-math-status.md (N_tow=243, N_flux=4880, f_max=21, Q=9, B′=floor((4880−21)/9)=539; 56 same-tower faces), grok-chats/13-t3-vs-hqcc.md (K⁺: V=539, E=594, F=56, β=(1,0,0) over F2; fibre blocks 68/67; L=18+521), task brief (fibre partition 3×68+5×67). Modular side: BRIDGE_C_35 REPORT/order11 (dim V=36, 105 components, M²=35P, Lemma O, three unary thetas, I=½log(6+√35)).

## Map-C1 (fundamental unit → packaging length)
Source: ε = 6+√35 (orthant angle I = ½ log ε). Target: L = 18+521 = 539 packaging.
Prediction (NEW): the multiplicative order of ε in (Z[√35]/539Z[√35])^× lies in {18, 521, 539}.
PASS iff the exact order (integer arithmetic) is one of these three; else FAIL.

## Map-C2 (three unary thetas → three T3 branches)
Source: the three weight-3/2 unary thetas with exponents 5n²/2, R²/34, 35m²/4 (n,R,m ∈ Z, as written). Target: T3 branches n mod 3 ∈ {0,1,2}.
Prediction (NEW): with exponents scaled to integers by 68 (170n², 2R², 595m²), each theta's exponents mod 3 put ≥ 2/3 of mass (|index| ≤ 10⁴) on a single residue, and the three dominant residues are pairwise distinct (a bijection theta ↔ branch).
PASS iff both hold; else FAIL.

## Map-C3 (P-parity on the 105 companions → K⁺ F2 cell counts)
Source: P (M²=35P) acting on V (dim 36). Target: K⁺ counts {V=539, E=594, F=56} / β over F2.
Prediction: dim V^{P=−1} − dim V^{P=+1} ≡ χ(K⁺)=1 (mod 2), and dim V^{P=−1} ∈ {1, 18, 21, 56 mod 36 = 20}.
PASS iff both. Test requires the exact P on V (SF/A35_lawspace_exact). If not cheaply available → OPEN.

## Map-C4 (Kronecker character of Q(√35) → eight fibre blocks)
Source: χ_D, D=140 (discriminant of Q(√35)); the Lemma-O sector sign is a quadratic character. Target: O_res indexed 1..539 in order, cut consecutively into blocks of sizes 68,68,68,67,67,67,67,67 (interpretation fixed now).
Prediction (NEW): every block sum S_b = Σ_{n∈b} χ_140(n) satisfies |S_b| ≤ 1, and the 68-blocks and 67-blocks have opposite sums' sign pattern (all 68-block sums ≥0, all 67-block sums ≤0 or vice versa).
PASS iff both; else FAIL.

## Map-C5 (wall Q → T3 free orbit of N_flux)
Source: walls Q ∈ {1, 7/2, 595/2}. Target: free T3 orbit of 4880 (14 steps, known).
Prediction (NEW): the orbit of 4880 contains an element n with 2n ∈ {2, 7, 595} other than the attractor 1, i.e. it passes through 595 (=2·595/2) or hits a value ≡ 595 mod 539·? — fixed sharp form: **595 ∈ orbit(4880)**.
PASS iff 595 occurs in the free T3 orbit of 4880; else FAIL.

## Map-C6 (resonant path Π → modular S-law)
Source: S-law matrix M_S (order 4). Target: resonant path Π, length 539.
Prediction: the 539-step resonant word, read mod 4, has M_S-order profile 539 ≡ 3 (mod 4) ⇒ the path's end-state is S³-related to start. Requires a written Π trajectory (not in repo) → OPEN unless found.
