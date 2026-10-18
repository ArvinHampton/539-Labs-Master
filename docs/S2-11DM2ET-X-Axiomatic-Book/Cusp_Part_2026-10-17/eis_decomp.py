# Exact Eisenstein decomposition of u_L, checked for every n <= 60000 (both frequency signs):
#   A(n) = #{nu in S+ u S-: 20Q2=n},  B(n) = #{nu in T+ u T-: -20Q2=n}
#   A(n) = (1/8) sum_{j even,l} conj chi_{j,l}(g1) * lam_{j,l}(n),  B(n) = (1/8) sum (-1)^l conj chi_{j,l}(g1) lam_{j,l}(n)
#   lam_{j,l}(n) = 1_{(n,10)=1} * sum_{d|n} psi(d) psi'(n/d)   (psi' = psi*chi_140)
import numpy as np, cmath, cypari2
pari=cypari2.Pari()
NMAX=60000
rc=np.load("region_counts.npy"); A=rc[0]+rc[1]; B=rc[2]+rc[3]
kr={d:np.array([0]+[int(pari(f'kronecker({d},{n})')) for n in range(1,NMAX+1)]) for d in (-4,-7)}
def chi5(e):
    v=np.zeros(NMAX+1,complex); lg={1:0,2:1,4:2,3:3}
    for n in range(1,NMAX+1):
        if n%5: v[n]=1j**(e*lg[n%5])
    return v
def psi(e5,s4,s7):
    v=chi5(e5).copy()
    if s4: v*=kr[-4]
    if s7: v*=kr[-7]
    return v
PSI={(0,0):(0,0,0),(0,1):(0,1,0),(2,0):(3,1,0),(2,1):(3,0,0),(4,0):(2,0,0),(4,1):(2,1,0),(6,0):(1,1,0),(6,1):(1,0,0)}  # psi has conductor | 20; chosen so psi(7)=chi(p7)
chi140=psi(2,1,1)
def conv(a,b):
    out=np.zeros(NMAX+1,complex)
    for d in range(1,NMAX+1):
        if a[d]==0: continue
        out[d::d]+=a[d]*b[1:NMAX//d+1]
    return out
cop=np.array([1 if np.gcd(n,10)==1 else 0 for n in range(NMAX+1)])
Ahat=np.zeros(NMAX+1,complex); Bhat=np.zeros(NMAX+1,complex); lam={}
for (j,l),(e5,s4,s7) in PSI.items():
    p=psi(e5,s4,s7); lam[(j,l)]=cop*conv(p,p*chi140)
    w=cmath.exp(-2j*cmath.pi*j/8)/8
    Ahat+=w*lam[(j,l)]; Bhat+=w*(-1)**l*lam[(j,l)]
r=[f"max_n<=60000 |A(n) - Eisenstein formula| = {np.abs(A[1:]-Ahat[1:]).max():.2e}",
   f"max_n<=60000 |B(n) - Eisenstein formula| = {np.abs(B[1:]-Bhat[1:]).max():.2e}",
   f"sum A = {A.sum()}, sum B = {B.sum()}"]
np.save("lam.npy",np.array([lam[k] for k in PSI]))
print("\n".join(r)); open("eis_decomp.txt","w").write("\n".join(r)+"\n")
bad=np.nonzero(np.abs(A-Ahat)>1e-6)[0]; print("bad A n:",bad[:20],len(bad), "all div by 7:",all(n%7==0 for n in bad))
print([(n,A[n],Ahat[n].round(6)) for n in bad[:6]])
