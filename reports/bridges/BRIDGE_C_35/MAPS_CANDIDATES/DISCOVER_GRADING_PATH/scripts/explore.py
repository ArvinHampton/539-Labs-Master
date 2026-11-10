# Exploration only (pre-PREREG). Exact structure of T3 on charge classes mod 9, and tower-parity grading.
import json, hashlib
from fractions import Fraction
def T3(n): return n//3 if n%3==0 else ((4*n+2)//3 if n%3==1 else (2*n+1)//3)
# T3(n) mod 9 is determined by n mod 27
tr={}
for r in range(27):
    s={T3(r+27*t)%9 for t in range(50)}; tr[r]=sorted(s)
det=all(len(v)==1 for v in tr.values())
# transition counts mod 9 (uniform over lifts mod 27)
M=[[0]*9 for _ in range(9)]
for r in range(27): M[r%9][tr[r][0]]+=1
# sample 539-step paths from SHA3 seeds: fraction of u_i ≡ 3 mod 9; and does q_i depend on q_{i-1} beyond M?
def path(m):
    u=int.from_bytes(hashlib.sha3_512(m).digest(),'big'); out=[u]
    for _ in range(539): u=T3(u); out.append(u)
    return out
cnt=[0]*9; pair=[[0]*9 for _ in range(9)]
for s in range(200):
    p=path(b'explore-%d'%s)
    for a,b in zip(p,p[1:]): cnt[a%9]+=1; pair[a%9][b%9]+=1
# tower parity grading on O_res
O=[21+9*j for j in range(539)]
tau=lambda x: x//21 if x<420 else 20+(x-420)//20
g=[(-1)**tau(x) for x in O]
fib=[sum(g[j] for j in range(539) if j%8==r) for r in range(8)]
print(json.dumps(dict(det_mod27=det,M=M,visit=cnt,pair=pair,g_sum=sum(g),g_fibre_sums=fib)))
