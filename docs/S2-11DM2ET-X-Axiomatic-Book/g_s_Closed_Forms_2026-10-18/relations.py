# Step (4): exact linear-algebra test: is g_s in span_Q{1, theta3, R, Mm} (hence span of {1, theta3, P_s, E_s, Theta_hol, C_third, q^8 f})?
from fractions import Fraction as Fr
import json
N = 400
def gser(s):
    tot = [0]*N; cur = [1] + [0]*(N-1); n = 0
    while n*n < N:
        for i in range(N - n*n): tot[i + n*n] += cur[i]
        n += 1; m = s*n
        if m >= N:   # further divisions by 1+q^m with m>=N do nothing mod q^N
            pass
        else:
            for i in range(m, N): cur[i] -= cur[i-m]
    return tot
def Qs(s, n, k): return n*n + s*n*k + Fr(s, 2)*k*(k+1)
def lattice(s, region):
    c = [0]*N
    for n in range(-60, 61):
        for k in range(-60, 61):
            if region(n, k):
                e = Qs(s, n, k)
                if e.denominator == 1 and 0 <= e < N: c[int(e)] += 1
                elif e.denominator != 1: return None
    return c
def rank(rows):
    M = [[Fr(x) for x in r] for r in rows]; r = 0
    for col in range(len(M[0])):
        piv = next((i for i in range(r, len(M)) if M[i][col] != 0), None)
        if piv is None: continue
        M[r], M[piv] = M[piv], M[r]
        for i in range(len(M)):
            if i != r and M[i][col] != 0:
                f = M[i][col]/M[r][col]; M[i] = [a - f*b for a, b in zip(M[i], M[r])]
        r += 1
        if r == len(M): break
    return r
S = list(range(3, 21)) + [25, 30, 41]; res = []
for s in S:
    g = gser(s)
    R = lattice(s, lambda n, k: n >= 0 and k >= 1); Mm = lattice(s, lambda n, k: n <= -1 and k <= 0)
    th = [0]*N
    for m in range(-30, 31):
        if m*m < N: th[m*m] += 1
    one = [1] + [0]*(N-1)
    base = [one, th, R, Mm]; r0 = rank(base); r1 = rank(base + [g])
    res.append(dict(s=s, rank_base=r0, rank_with_g=r1, g_in_span=(r1 == r0), g_prefix=g[:16]))
    print(f"s={s:2d} rank{{1,theta3,R,Mm}}={r0}  with g_s: {r1}  -> g_s in span: {r1 == r0};  g_s = {g[:16]}...", flush=True)
json.dump(res, open('relations.json', 'w'), indent=1)
