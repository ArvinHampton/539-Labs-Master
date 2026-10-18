# Exact check of the lattice <-> ideal correspondence for all four sign regions of u_L, up to norm NMAX:
#   r_R(n) := #{nu in region R mod gamma, 20|Q2(nu)| = n}  must equal  #{ideals a in class C_R, N a = n}
# plus the character decomposition and the genus (Eisenstein) form of the full u_L coefficients.
import cypari2, numpy as np, json, sympy as sp
from collections import defaultdict
from family import G, D
pari=cypari2.Pari(); pari.allocatemem(2*10**9); gp=lambda s: pari(s)
NMAX=60000
gp('bnf=bnfinit(y^2-35,1); P2=idealprimedec(bnf,2)[1]; P5=idealprimedec(bnf,5)[1]; f=idealmul(bnf,P2,P5); bnr=bnrinit(bnf,[f,[1,1]],1)')
gp(f'L=ideallist(bnf,{NMAX})')
gp(f'C=vector({NMAX},n, if(gcd(n,10)>1, [], apply(I->bnrisprincipal(bnr,I,0), L[n])))')
cnt=np.zeros((NMAX+1,8,2),dtype=np.int64)
Cv=gp('C')
for n in range(1,NMAX+1):
    for c in Cv[n-1]:
        cnt[n,int(c[0]),int(c[1])]+=1
np.save("class_counts.npy",cnt)
def region_counts(r1,r2,sg,Qmax,Bx=200):
    m=np.arange(-Bx,Bx+1); M1,M2=np.meshgrid(m,m,indexing='ij')
    N1=49+D*M1.ravel(); N2=-14+D*M2.ravel()
    det=r1[0]*r2[1]-r1[1]*r2[0]
    s=sg*(N1*r2[1]-N2*r2[0])*np.sign(det); t=sg*(r1[0]*N2-r1[1]*N1)*np.sign(det)
    ok=(s>0)&(t>=0); N1=N1[ok];N2=N2[ok]
    q=(2*N1*N1+14*N1*N2+7*N2*N2)/(2*D*D)
    n=np.rint(20*np.abs(q)).astype(np.int64); n=n[n<=NMAX]
    return np.bincount(n,minlength=NMAX+1)
e1=(1,0); f=(1,-1)
R={'S+':(e1,tuple(G@np.array(e1)),1,(5,0)),'S-':(e1,tuple(G@np.array(e1)),-1,(1,0)),
   'T+':(f,tuple(G@np.array(f)),1,(1,1)),'T-':(f,tuple(G@np.array(f)),-1,(5,1))}
out=[]
rc={}
for k,(r1,r2,sg,cls) in R.items():
    rc[k]=region_counts(r1,r2,sg,NMAX/20,Bx=900)
    d=np.abs(rc[k]-cnt[:,cls[0],cls[1]]).max()
    out.append(f"region {k} <-> ray class {cls}: max_n<={NMAX} |lattice count - ideal count| = {d}  (total ideals {cnt[:,cls[0],cls[1]].sum()})")
Apos=rc['S+']+rc['S-']; Bneg=rc['T+']+rc['T-']
# genus test on the FULL coefficients (both signs), n coprime to 70
from sympy import jacobi_symbol, divisors
for name,arr in (("positive (S+ + S-)",Apos),("negative (T+ + T-)",Bneg),("T+ alone (previous report's test)",rc['T+'])):
    h=defaultdict(set)
    for n in range(1,NMAX+1):
        if np.gcd(n,70)!=1: continue
        RO=sum(jacobi_symbol(35,dd) for dd in divisors(n))
        if RO==0:
            if arr[n]: h['bad'].add(n)
            continue
        h[n%280].add(sp.Rational(int(arr[n]),RO))
    bad=[k for k,v in h.items() if len(v)>1]
    out.append(f"genus test {name}: residue classes mod 280 with non-constant coeff/R_O: {len(bad)} of {len(h)}")
np.save("region_counts.npy",np.array([rc[k] for k in R]))
print("\n".join(out)); open("ideal_counts.txt","w").write("\n".join(out)+"\n")
