# Local-derived (t4436, Oc-2). Cusp-space dimensions dim S_{3/2}(Gamma0(784), chi_D) (PARI mfdim, space flag 1 = cuspidal, the same space
# s1e's mfinit([784,3/2,D],1) builds), for all 8 admissible quadratic D. Cheap (no mfinit, 300 MB stack), run alongside s1e without touching it.
# dim 0 => no Oc-2 vector at level 784 for that character. Cross-check: s1e already reports dim 36 (D=1) and dim 0 (D=-4).
import cypari2; pari=cypari2.Pari(); pari.allocatemem(3*10**8)
for D in [1,-4,8,-8,-7,28,-56,56]:
    print(f"level 784, char {D}: dim S_3/2 = {pari(f'mfdim([784,3/2,{D}],1)')}", flush=True)
