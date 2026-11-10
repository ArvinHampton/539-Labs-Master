# Local-derived. Quick exact checks for ERRATUM_LOCAL_t4407_CANDIDATES_PP_AUDIT_FIXES (fixes 1, 4, 5).
from sympy import Matrix, Rational, gcd
import cypari2; pari = cypari2.Pari()
S = Matrix([[0,-1],[1,0]]); T = Matrix([[1,1],[0,1]]); W = Matrix([[0,-1],[49,0]])
print("Fix1: W T W^-1 =", (W*T*W.inv()).tolist(), "; S T^49 S^-1 =", (S*T**49*S.inv()).tolist(), "; equal:", W*T*W.inv() == S*T**49*S.inv())
E = pari.ellinit([1,-1,0,-2,-1])
print("Fix4: a_11(49a1) =", pari.ellap(E,11), "; chi140(11) = (140/11) =", pari.kronecker(140,11), "; (-7/11) =", pari.kronecker(-7,11))
ps = [int(p) for p in pari.primes(200) if int(pari.kronecker(140,p)) == -1 and int(pari.ellap(E,p)) != 0]
print("Fix4: primes p<1229 with chi140(p)=-1 and a_p(f)!=0 (first 10):", ps[:10], " count:", len(ps))
# Fix5: does a matrix normalize Gamma0(980)? test conjugation of generators-ish sample: T, -I, and random elements
import random
def in_G0(M, N): return M.det() == 1 and all(x.is_integer for x in M) and M[1,0] % N == 0
def normalizes(Wm, N, trials=400):
    random.seed(1); ok = True
    samples = [T, Matrix([[1,0],[N,1]])]
    for _ in range(trials):
        c = N*random.randint(-30,30); d = random.randint(-200,200)
        if gcd(c,d) != 1: continue
        # solve a d - b c = 1
        import sympy; g, x, y = sympy.gcdex(d, -c)  # x*d + y*(-c) = 1
        samples.append(Matrix([[x, y],[c, d]]))
    for g in samples:
        assert in_G0(g, N), g
        h = Wm*g*Wm.inv()
        if not in_G0(h, N): ok = False; break
    return ok
N = 980
W980 = Matrix([[0,-1],[980,0]])
# Atkin-Lehner W_49 at level 980: (49a, b; 980c, 49d), det 49 -> 49ad - 20bc... choose a=1,d? need 49*49ad - 980bc = 49 -> 49ad - 20bc = 1: a=1,d=1,b=... 49 - 20bc = 1 -> bc = 12/5 no; a=1,d=9: 441-20bc=1 -> bc=22: b=22,c=1
AL49 = Matrix([[49*1, 22],[980*1, 49*9]])
print("Fix5: det AL49 =", AL49.det(), "; W49=(0,-1;49,0) normalizes G0(980):", normalizes(W, N), "; W980 normalizes:", normalizes(W980, N), "; AL W_49^(980) normalizes:", normalizes(AL49, N))
