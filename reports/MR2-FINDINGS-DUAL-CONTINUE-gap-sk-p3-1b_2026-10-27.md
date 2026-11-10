# MR2 FINDINGS — DUAL-CONTINUE — GAP-SK-p3-1b (2026-10-27)
STATUS: PARTIAL | NOT OPERATIVE | tip_touched NO (sha 7cddb188…dfc91 before+after) | Kerr BLOCKED | REPORTS ONLY, no RECS | no new invented values
Parent: MR2-FINDINGS-DUAL-CONTINUE-gap-sk-p3-1a_2026-10-27.md sha bf07abbfcc1b64ebeff3965cab08e4f06186d20c011283eddf945cf908302b40

## (a) Corpus search (rg -i "brauer|p-regular|simple modules|number of irreducible" lit/bm/*.txt)
- bm02_multiplicite.txt L1202 "(Brauer-Nesbitt)" — sha aa4893cf…a264a22d. Brauer–Nesbitt (semisimplification determined by char poly), NOT Brauer's count.
- breuil_GL2Qp_II.txt L943 "preuve de Brauer-Nesbitt …" — sha 245f62ee…0362b273. Same; NOT the count.
- breuil_paskunas_supersingular.txt L1853, 1005.2008.txt L1089/L7488: "number of irreducible subquotients" (induction length), irrelevant.
- No on-disk statement of #irreducibles over F̄p = #p-regular classes. RESULT: MISS.
- breuil_GL2Qp_I.txt (sha 3b5f0a8e…3f154518) L389–392: "A torsion près par les caractères, les σ_r donnent toutes les représentations lisses irréductibles de dimension finie de KZ sur F̄p ([2])." Completeness is CITED to [2] Barthel–Livné, not proved. BL94/BL95 PDFs: MISS (no barthel/livne/BL9* file on disk). RESULT: MISS.

## (b) Path A: NOT available (only citation; BL MISS).
Path B (elementary, done): p-regular elements of GL2(Fp) = semisimple elements (order coprime to p ⇔ diagonalizable over F̄p). Classes determined by char poly:
1. scalar a·I, a∈Fp^×: p−1 classes;
2. split non-scalar diag(a,b), {a,b}⊂Fp^×, a≠b, unordered: (p−1)(p−2)/2;
3. anisotropic (irreducible char poly), eigenvalues {λ,λ^p}, λ∈F_{p^2}^×∖Fp^×, up to Frobenius: (p²−p)/2.
Sum = (p−1)[1+(p−2)/2+p/2] = p(p−1). Labels Sym^s⊗det^a, 0≤s≤p−1, a∈Z/(p−1): p(p−1). Equal. Machine check p=2,3,5,7,11,13: both sides agree (/tmp check: 2,6,20,42,110,156).
Combined with 1a (pairwise non-isomorphic, irreducible), completeness follows IF Brauer's theorem (#irr = #p-regular classes) is granted.

## Residual (why PARTIAL, not CLOSED)
The count equality is now proved; Brauer's theorem itself remains UNQUOTED on disk (corpus MISS; BL94/BL95 MISS). A Brauer-free route (V^U≠0 for unipotent p-Sylow U, T-eigenline, embed V into Ind_B^G χ, read off JH factors) is standard but not written/verified here; not claimed.
24h retry rule: re-attempt on acquisition of BL94/BL95 or a text containing Brauer's count (e.g. Serre, Linear Representations §18). Dated 2026-10-27.
