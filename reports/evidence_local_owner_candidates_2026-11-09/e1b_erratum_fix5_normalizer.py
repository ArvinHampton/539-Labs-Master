# Local-derived. SUPERSEDES the Fix5 part of e1_erratum_pp_audit_checks.py (kept on disk), which crashed because it
# unpacked sympy.gcdex(a,b) -> (s,t,h) in the wrong order. Fixes 1 and 4 in e1's log are unaffected.
import random, sympy
from sympy import Matrix, gcd
T = Matrix([[1,1],[0,1]]); N = 980
def in_G0(M, N): return M.det() == 1 and all(x.is_integer for x in M) and M[1,0] % N == 0
def samples(N, trials=600):
    random.seed(1); out = [T, Matrix([[1,0],[N,1]]), -Matrix.eye(2)]
    for _ in range(trials):
        c = N*random.randint(-30,30); d = random.randint(-200,200)
        if d == 0 or gcd(c,d) != 1: continue
        s, t, h = sympy.gcdex(d, -c)          # s*d + t*(-c) = h = +-1
        a, b = s*h, t*h                       # a*d - b*c = 1
        out.append(Matrix([[a, b],[c, d]]))
    return out
G = samples(N); assert all(in_G0(g,N) for g in G)
def normalizes(Wm): return all(in_G0(Wm*g*Wm.inv(), N) for g in G)
W49 = Matrix([[0,-1],[49,0]]); W980 = Matrix([[0,-1],[980,0]])
AL49 = Matrix([[49, 22],[980, 441]])   # (49a, b; 980c, 49d) with a=1,b=22,c=1,d=9: det = 49
print("samples:", len(G), "; det AL49 =", AL49.det())
print("W49=(0,-1;49,0) maps sample into G0(980):", normalizes(W49))
print("W980=(0,-1;980,0) normalizes (on sample):", normalizes(W980))
print("Atkin-Lehner W_49^(980) normalizes (on sample):", normalizes(AL49))
print("note: W980 and W_Q^(N) normalizing Gamma0(N) is the standard Atkin-Lehner theorem; the sample check is illustration only")
