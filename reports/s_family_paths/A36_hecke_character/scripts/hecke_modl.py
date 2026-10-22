# T1-T3: exact mod-l Hecke data of the lift-derived forms in each P-even sector, and the dihedral eigen-search.
# Coefficients come from A34/scripts/coeffsS.py (read-only import; exact phase lists).  e(q) -> w^(qL) mod l,
# w of exact order L in F_l, L = lcm(all phase denominators, E_bound).  Everything below is exact in F_l.
import sys, json, time, itertools, math
from fractions import Fraction as Fr
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A34_ledger_checks/scripts')
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A2/scripts')
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A36_hecke_character/scripts')
from coeffsS import Coeffs
from srho_data import Data
from classdata import data as cdata, Cl
import sympy
s=int(sys.argv[1]); NP=int(sys.argv[2]); KR=int(sys.argv[3]) if len(sys.argv)>3 else 16
cd=cdata(s); E=cd['E_bound']; n=s*(s-2)
d=Data(s); N=d.N
def Torder():
    res=1
    for j in range(N):
        idx,ph,c=j,Fr(0),0
        while True:
            idx,p1=d.Tm[idx]; ph+=p1; c+=1
            if idx==j: break
        res=math.lcm(res,c*Fr(ph).denominator)
    return res
Lv=Torder(); C=Coeffs(s,Lv); assert d.F.LABELS==C.F.LABELS
PR=[];q=Lv+1
while len(PR)<NP:
    if sympy.isprime(q): PR.append(q)
    q+=Lv
Dd=C.D
L=math.lcm(Dd*Dd,d.M,E,4)
k=max(1,10**12//L)
while not sympy.isprime(k*L+1): k+=1
ell=k*L+1
g=sympy.primitive_root(ell); w=pow(g,(ell-1)//L,ell)
def e(q):
    q=Fr(q)%1; assert L%q.denominator==0, q; return pow(w,q.numerator*(L//q.denominator),ell)
inv2=pow(2,ell-2,ell)
def compose(X,Y): return {i:(Y[X[i][0]][0],(X[i][1]+Y[X[i][0]][1])%1) for i in X}
def group(sig):
    ident={i:(i,Fr(0)) for i in range(N)}; els=[(ident,1)]
    for (X,sg) in [(d.Pm,1)]+[(d.refl[q_],sg) for q_,sg in sig]:
        els=els+[(compose(X,g_),sg*c) for g_,c in els]
    return els
def coeff(k_,i,sigel):
    tot=0; T=C.terms(k_)
    for g_,c in sigel:
        j,ph=g_[i]
        if j in T:
            v=sum(e(q_) for q_ in T[j])%ell
            tot+=c*e(ph)*v*inv2
    return tot*pow(len(sigel),ell-2,ell)%ell
def bcoef(p,k_,i,sigel):
    v=coeff(p*k_,i,sigel)
    if k_%p==0: v+=coeff(k_//p,i,sigel)
    return v%ell
def rank(rows):
    M=[r[:] for r in rows]; r=0; ncol=len(M[0]) if M else 0
    for c in range(ncol):
        piv=next((i for i in range(r,len(M)) if M[i][c]%ell),None)
        if piv is None: continue
        M[r],M[piv]=M[piv],M[r]; iv=pow(M[r][c],ell-2,ell); M[r]=[x*iv%ell for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]%ell:
                f=M[i][c]; M[i]=[(a-f*b)%ell for a,b in zip(M[i],M[r])]
        r+=1
    return r
def solve(basis,v):
    # v = sum x_j basis_j exactly; least-structured: Gaussian elimination on augmented transposed system
    m=len(basis); cols=len(v)
    A=[[basis[j][c] for j in range(m)]+[v[c]] for c in range(cols)]
    piv=[];r=0
    for c in range(m):
        pr=next((i for i in range(r,cols) if A[i][c]%ell),None)
        if pr is None: return None
        A[r],A[pr]=A[pr],A[r]; iv=pow(A[r][c],ell-2,ell); A[r]=[x*iv%ell for x in A[r]]
        for i in range(cols):
            if i!=r and A[i][c]%ell:
                f=A[i][c]; A[i]=[(a-f*b)%ell for a,b in zip(A[i],A[r])]
        r+=1
    if any(A[i][m]%ell for i in range(m,cols)): return None   # inconsistent
    return [A[i][m] for i in range(m)]
# candidate set Lambda_E = {z+1/z : z^E=1}
gE=pow(g,(ell-1)//E,ell); LAM={}
z=1
for j in range(E):
    lam=(z+pow(z,ell-2,ell))%ell; LAM.setdefault(lam,j); z=z*gE%ell
def zorder(lam):
    j=LAM[lam]; return E//math.gcd(E,j)
# T3: class of a prime above p in Cl(O)
CL=Cl(4*n)
def pclass(p):
    for b in range(0,2*p):
        if (b*b-4*n)%(4*p)==0:
            nar=CL.cls((p,b,(b*b-4*n)//(4*p))); return nar, CL.widx[nar]
    return None
log=open('logs/hecke_modl_s%d.log'%s,'w')
def P(*a):
    t=' '.join(str(x) for x in a); print(t,flush=True); log.write(t+'\n'); log.flush()
P('s=%d N=%d Tlevel=%d primes=%s ell=%d L=%d E=%d'%(s,N,Lv,PR,ell,L,E))
pcl={p:pclass(p) for p in PR}
P('class of p-ideal (narrow idx, wide idx):',pcl, 'principal narrow idx', CL.cls(CL._principal()))
c0=[i for i,(al,be) in enumerate(C.F.LABELS) if int(al[0])%C.D==0 and int(al[1])%C.D==0]
ks=[k_ for k_ in range(-KR,KR+1) if k_]
out={'s':s,'Tlevel':Lv,'primes':PR,'ell':ell,'E':E,'p_class':{str(p):pcl[p] for p in PR},'sectors':{}}
for signs in itertools.product((1,-1),repeat=len(d.refl)):
    sig=tuple(zip(sorted(d.refl),signs)); sigel=group(sig)
    nzc=0
    for i in range(N):
        acc={}
        for g_,c in sigel:
            j,ph=g_[i]
            if j in c0: acc[ph]=acc.get(ph,0)+c
        if any(v for v in acc.values()): nzc+=1
    cols=[]
    for k_ in ks:
        Ts=set(C.terms(k_))
        for p in PR: Ts|=set(C.terms(p*k_))
        cand=set()
        for g_,c in sigel:
            inv={g_[i][0]:i for i in g_}; cand|={inv[j] for j in Ts}
        cols+=[(k_,i) for i in sorted(cand)]
    if not cols: P(sig,'no coefficients'); continue
    F0=[coeff(k_,i,sigel) for (k_,i) in cols]
    W={p:[bcoef(p,k_,i,sigel) for (k_,i) in cols] for p in PR}
    res={'c0_rows':nzc}
    if nzc:
        G={p:[(a-2*b)%ell for a,b in zip(W[p],F0)] for p in PR}; r=rank(list(G.values())); res['cusp_rank_modl']=r
        if r==0: P(sig,'cusp rank 0'); out['sectors'][str(sig)]=res; continue
        if r==1:
            p0=next(p for p in PR if any(G[p])); rat={p:solve([G[p0]],G[p]) for p in PR}
            assert all(rat[p] is not None for p in PR)
            rat={p:rat[p][0] for p in PR}
            # second order: exact lambda_{p0} from one column: (T'_{p0} g_{p0})(m) = a(p0^2 m) + a(m) - 2 a(p0 m)
            jbest=min((j for j in range(len(cols)) if G[p0][j]),key=lambda j:abs(cols[j][0]))
            k_,i=cols[jbest]; t0=time.time()
            h=(coeff(p0*p0*k_,i,sigel)+coeff(k_,i,sigel)-2*coeff(p0*k_,i,sigel))%ell
            lam0=h*pow(G[p0][jbest],ell-2,ell)%ell
            lams={p:(2+rat[p]*(lam0-2))%ell for p in PR}
            inL=all(l in LAM for l in lams.values())
            res['second_order_column']=[k_,i]; res['eigen']={str(p):(zorder(l) if l in LAM else None) for p,l in lams.items()}
            res['all_in_LambdaE']=inL; res['lam_is_2']={str(p):lams[p]==2 for p in PR}
            P(sig,'Eis present; cusp rank 1; exact lambda via a(p0^2 m), p0=%d col %s (%.0fs); all in Lambda_E:'%(p0,(k_,i),time.time()-t0),inL,
              'orders',[res['eigen'][str(p)] for p in PR],'ratios==1?',[rat[p]==1 for p in PR])
            sols=[]
            for mu in ([] if True else LAM):
                if mu==2: continue
                lams={p:(2+rat[p]*(mu-2))%ell for p in PR}
                if all(l in LAM for l in lams.values()): sols.append(lams)
            res['solutions']=[{str(p):{'zeta_order':zorder(l),'lam_is_2':l==2} for p,l in S_.items()} for S_ in sols]
        else:
            res['note']='cusp rank>1 with Eisenstein part: search not implemented'; P(sig,res)
    else:
        r=rank([F0]+list(W.values())); res['rank_modl']=r
        if r==1:
            lams={p:solve([F0],W[p]) for p in PR}; ok=all(v is not None for v in lams.values())
            lams={p:v[0] for p,v in lams.items()}
            inL=all(l in LAM for l in lams.values())
            res['eigen']={str(p):(zorder(l) if l in LAM else None) for p,l in lams.items()}; res['all_in_LambdaE']=inL
            P(sig,'rank 1: exact eigenvector; all lambda_p in Lambda_E:',inL,'orders',[res['eigen'][str(p)] for p in PR])
        elif r==2:
            p0=next(p for p in PR if rank([F0,W[p]])==2)
            xy={p:solve([F0,W[p0]],W[p]) for p in PR}; assert all(v is not None for v in xy.values())
            # second order: matrix of T'_{p0} on span{F0, w0}: T F0 = w0, T w0 = al F0 + be w0, with
            # (T w0)(m) = a(p0^2 m) + a(m) for |m| < p0.  Solve on 2 columns, verify on 2 more (exact).
            w0=W[p0]; order_=sorted(range(len(cols)),key=lambda j:(abs(cols[j][0]),j))
            pick=[]
            for j in order_:
                if not (F0[j] or w0[j]): continue
                if len(pick)==1 and (F0[pick[0]]*w0[j]-F0[j]*w0[pick[0]])%ell==0: continue
                pick.append(j)
                if len(pick)==4: break
            t0=time.time()
            Tw={j:(coeff(p0*p0*cols[j][0],cols[j][1],sigel)+coeff(cols[j][0],cols[j][1],sigel))%ell for j in pick}
            j1,j2=pick[0],pick[1]; det=(F0[j1]*w0[j2]-F0[j2]*w0[j1])%ell; idet=pow(det,ell-2,ell)
            al=(Tw[j1]*w0[j2]-Tw[j2]*w0[j1])*idet%ell; be=(F0[j1]*Tw[j2]-F0[j2]*Tw[j1])*idet%ell
            ver=[(al*F0[j]+be*w0[j]-Tw[j])%ell==0 for j in pick[2:]]
            disc=(be*be+4*al)%ell; sq=sympy.sqrt_mod(disc,ell)
            good=[]
            if sq is not None:
                i2=pow(2,ell-2,ell)
                for mu in sorted({(be+sq)*i2%ell,(be-sq)*i2%ell}):
                    lams={p:(xy[p][0]+xy[p][1]*mu)%ell for p in PR}; good.append((mu,lams))
            res['second_order']={'p0':p0,'cols':[list(cols[j]) for j in pick],'verify_extra_cols':ver,'charpoly_disc_is_square':sq is not None}
            res['systems']=[{'eigen':{str(p):(zorder(l) if l in LAM else None) for p,l in lams.items()},
                             'all_in_LambdaE':all(l in LAM for l in lams.values())} for mu,lams in good]
            P(sig,'rank 2: T_p0 on span solved from a(p0^2 m) (%.0fs); extra-column checks'%(time.time()-t0),ver)
            for mu,lams in good: P('   system: all in Lambda_E:',all(l in LAM for l in lams.values()),'orders',[zorder(lams[p]) if lams[p] in LAM else None for p in PR])
            for mu in []:
                lams={p:(xy[p][0]+xy[p][1]*mu)%ell for p in PR}
                if all(l in LAM for l in lams.values()): good.append((mu,lams))
                        # consistency: the two eigenvalues of T'_{p0} must be roots of the char poly of T'_{p0} on span{F0,W[p0]}:
            # T'_{p0}W[p0] unknown (needs a(p0^2 m)); instead check product/sum relation through another prime pair
            P(sig,'rank 2: #admissible mu =',len(good)); 
        else:
            res['note']='rank %d: search not implemented'%r; P(sig,res)
    out['sectors'][str(sig)]=res
json.dump(out,open('out/hecke_modl_s%d.json'%s,'w'),indent=1)
P('done')
