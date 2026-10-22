# A35: explicit intertwiner X: V -> E, verified exactly in Q(zeta_N), N=58800 (cyclotomic polynomial reduction).
# Common factor 1/sqrt35 (positive root on both sides) cancels in S-equations.
import sys, json, numpy as np, flint, math
from fractions import Fraction as Fr
sys.dont_write_bytecode=True
from symbols import *
from orbits import orbits
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A/scripts')
from weil_family import WFam
N=58800; fV=N//L; fE=N//29400
# ---- cyclotomic elements: dict exp->Fraction ----
def cadd(a,b,s=1):
    d=dict(a)
    for e,c in b.items(): d[e%N]=d.get(e%N,0)+s*c
    return {e:c for e,c in d.items() if c}
def cmul(a,b):
    d={}
    for e1,c1 in a.items():
        for e2,c2 in b.items(): e=(e1+e2)%N; d[e]=d.get(e,0)+c1*c2
    return {e:c for e,c in d.items() if c}
PHI=flint.fmpz_poly.cyclotomic(N) if hasattr(flint.fmpz_poly,'cyclotomic') else None
PHIq=flint.fmpq_poly([int(c) for c in PHI.coeffs()])
def iszero(a):
    if not a: return True
    co=[0]*N
    for e,c in a.items(): co[e]+=c
    den=1
    for c in co:
        if c: den=den*Fr(c).denominator//math.gcd(den,Fr(c).denominator)
    P=flint.fmpz_poly([int(Fr(c)*den) for c in co])
    return (P % PHI)==0
def cval(a): return sum(float(c)*np.exp(2j*np.pi*e/N) for e,c in a.items())
z=lambda e,c=1:{e%N:Fr(c)}
# ---- V side: orbit basis ----
rep,zero,roots,_=orbits(); assert not zero and len(roots)==36
ridx={r:i for i,r in enumerate(roots)}
def orbit_matrix(rows):
    M=[[{} for _ in range(36)] for _ in range(36)]
    for i,r in enumerate(roots):
        for k,es in rows[r].items():
            rt,ph=rep[k]
            for e in es: M[i][ridx[rt]]=cadd(M[i][ridx[rt]], z((e+ph)*fV))
    return M
SV=orbit_matrix(S_rows()); TV=orbit_matrix(T_rows())
# ---- E side (A32 restrict construction, unnormalised orbit basis) ----
F=WFam(7); F.build_W(); good=np.nonzero(F.good)[0]
def restrict(rowfun):
    M={}
    for o in good:
        i0=F.rep[o]; J,PH=rowfun(i0)
        for j,ph in zip(J,PH):
            c=F.widx[F.orb[j]]
            if c<0: continue
            e=(3*int(ph)+3*int(F.ph[j])-3*int(F.ph[i0]))%29400
            key=(int(F.widx[o]),int(c)); M[key]=cadd(M.get(key,{}),z(e*fE))
    return M
S7=restrict(F.S_row); J,PH=F.T_mono(); T7=restrict(lambda i:(J[i:i+1],PH[i:i+1]))
Cidx=[26,28,30,32,34,36]; Eidx=[i for i in range(42) if i not in Cidx]
res={}
res['E_C_block_zero_exact']=all(iszero(v) for (r,c),v in list(S7.items())+list(T7.items()) if (r in Cidx)!=(c in Cidx))
SE=[[S7.get((r,c),{}) for c in Eidx] for r in Eidx]; TE=[[T7.get((r,c),{}) for c in Eidx] for r in Eidx]
res['T_E_diagonal']=all(iszero(TE[i][j]) for i in range(36) for j in range(36) if i!=j)
def eigbasis(TM):
    """T monomial with 1- and 2-cycles, unit coefficients: returns P (columns = eigenvectors), Pinv, eigenvalue exps"""
    n=len(TM); P=[[{} for _ in range(n)] for _ in range(n)]; Pinv=[[{} for _ in range(n)] for _ in range(n)]; lam=[None]*n; done=set()
    for i in range(n):
        if i in done: continue
        nz=[j for j in range(n) if TM[i][j]]; assert len(nz)==1 and len(TM[i][nz[0]])==1
        j=nz[0]; (ea,ca),=TM[i][j].items(); assert ca==1
        if j==i: P[i][i]=z(0); Pinv[i][i]=z(0); lam[i]=ea; done.add(i); continue
        nz2=[k for k in range(n) if TM[j][k]]; assert nz2==[i]; (eb,cb),=TM[j][i].items(); assert cb==1
        s=ea+eb; assert s%2==0
        lp=(s//2)%N; lm=(s//2+N//2)%N
        # column eigenvector v=(1 at i, c at j), (M v)_i = z^ea c = lam ; c = z^(lam-ea)
        cp=(lp-ea)%N; cm=(lm-ea)%N        # cm = cp + N/2  (= -c+)
        P[i][i]=z(0); P[j][i]=z(cp); P[i][j]=z(0); P[j][j]=z(cm); lam[i]=lp; lam[j]=lm
        # inverse of [[1,1],[c,-c]] = 1/(2c) [[c,1],[c,-1]]
        Pinv[i][i]=z(0,Fr(1,2)); Pinv[i][j]=z(-cp,Fr(1,2)); Pinv[j][i]=z(0,Fr(1,2)); Pinv[j][j]=z(-cp,Fr(-1,2))
        done.update({i,j})
    return P,Pinv,lam
PV,PVinv,lamV=eigbasis(TV); PE,PEinv,lamE=eigbasis(TE)
assert len(set(lamV))==36 and len(set(lamE))==36
pi={}
for col in range(36):
    m=[k for k in range(36) if lamE[k]==lamV[col]]; assert len(m)==1, (col,lamV[col]); pi[col]=m[0]
res['T_spectra_equal_exact']=sorted(lamV)==sorted(lamE)
def mm(Aa,Bb):
    n=len(Aa); m=len(Bb[0]); out=[[{} for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for k in range(len(Bb)):
            if not Aa[i][k]: continue
            for j in range(m):
                if Bb[k][j]: out[i][j]=cadd(out[i][j],cmul(Aa[i][k],Bb[k][j]))
    return out
I36=mm(PVinv,PV); J36=mm(PEinv,PE)
res['P^-1 P = I exact (V and E)']=all(iszero(cadd(M_[i][j], z(0) if i==j else {}, -1)) for M_ in (I36,J36) for i in range(36) for j in range(36))
SVp=mm(mm(PVinv,SV),PV); SEp=mm(mm(PEinv,SE),PE)
SE=SEp
# float solve for diagonal scalars c_col with c_i SVp[i][j] = SE[pi i][pi j] c_j
fS=np.array([[cval(SVp[i][j]) for j in range(36)] for i in range(36)]); fE_=np.array([[cval(SE[pi[i]][pi[j]]) for j in range(36)] for i in range(36)])
c=np.zeros(36,complex); c[0]=1; known={0}
while len(known)<36:
    for i in range(36):
        if i in known: continue
        for j in known:
            if abs(fS[i][j])>1e-9: c[i]=fE_[i][j]*c[j]/fS[i][j]; known.add(i); break
resid=max(abs(c[i]*fS[i][j]-fE_[i][j]*c[j]) for i in range(36) for j in range(36)); res['float_residual']=float(resid)
# identify c_i = 2^(k/2) * zeta^e  (sqrt2 = z^(N/8)+z^(-N/8))
sq2={N//8:Fr(1),(-N//8)%N:Fr(1)}
cex=[]; guesses=[]
for i in range(36):
    mag=abs(c[i]); k=round(2*math.log2(mag)); assert abs(mag-2**(k/2))<1e-9, mag
    ph=np.angle(c[i]/2**(k/2))/(2*np.pi)*N; e=round(ph); assert abs(ph-e)<1e-6
    el=z(e,Fr(2)**(k//2) if k>=0 else Fr(1,2**((-k+1)//2)) if k%2 else Fr(1,2**(-k//2)))
    if k%2: el=cmul(el,sq2)
    cex.append(el); guesses.append((k,int(e)%N))
bad=0
for i in range(36):
    for j in range(36):
        d=cadd(cmul(cex[i],SVp[i][j]), cmul(SE[pi[i]][pi[j]],cex[j]),-1)
        if not iszero(d): bad+=1
res['S equation entries failing (of 1296)']=bad
res['T eigenvalues matched exactly']=all(lamV[i]==lamE[pi[i]] for i in range(36))
res['X form']='X = P_E * Perm * diag(c) * P_V^-1 (orbit bases)'
res['X = Perm * diag(c) * P^-1 ; c_i = 2^(k/2) zeta_N^e (k,e)']=guesses
res['orbit_roots']=[f"{FAM[r//35]}[{r%35}]" for r in roots]; res['perm V-eigvec -> E index (0-based in E)']=[pi[i] for i in range(36)]
res['V T-eigenvalues (exp mod 58800)']=lamV
print({k:v for k,v in res.items() if not isinstance(v,list)}); json.dump(res,open('exact_intertwiner.json','w'),indent=1)
