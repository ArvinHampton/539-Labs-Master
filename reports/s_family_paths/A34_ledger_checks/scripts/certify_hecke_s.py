# Category A lower bounds via vector-valued Hecke operators T'_p (p prime, p = 1 mod Tlevel), generic odd s.
# For each P-even sector sigma: functions F0 = P_sigma u, F_p = T'_p F0 (p in PR), and if P_sigma c0 != 0, use the
# cuspidal combinations F_p - 2 F0 instead (zero constant term).  Lower bound = rank of the coefficient matrix,
# certified by an r x r minor whose Arb ball determinant excludes 0.  Cuspidality of F0 in mixed sectors: P_sigma c0 = 0 exactly.
import sys, json, time, itertools, numpy as np
from fractions import Fraction as Fr
sys.path.insert(0,'scripts'); sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A2/scripts'); sys.dont_write_bytecode=True
from coeffsS import Coeffs
from srho_data import Data
from flint import acb, acb_mat, fmpq, ctx
import sympy
ctx.prec=256
s=int(sys.argv[1]); NP=int(sys.argv[2]) if len(sys.argv)>2 else 3; KR=int(sys.argv[3]) if len(sys.argv)>3 else 16
d=Data(s); N=d.N
# exact T order (monomial tracking)
Lv=1
def Torder():
    L_=1
    for j in range(N): pass
    import math
    orders=[]
    seen=set(); res=1
    for j in range(N):
        idx,ph,c=j,Fr(0),0
        while True:
            idx,p1=d.Tm[idx]; ph+=p1; c+=1
            if idx==j: break
        res=math.lcm(res, c*Fr(ph).denominator)
    return res
Lv=Torder()
C=Coeffs(s,Lv); assert d.F.LABELS==C.F.LABELS
PR=[]; q=Lv+1
while len(PR)<NP:
    if sympy.isprime(q): PR.append(q)
    q+=Lv
def e(x): x=Fr(int(Fr(x).numerator),int(Fr(x).denominator))%1; return acb(fmpq(int(2*x.numerator),int(x.denominator))).exp_pi_i()
def compose(X,Y): return {i:(Y[X[i][0]][0], (X[i][1]+Y[X[i][0]][1])%1) for i in X}
def group(sig):
    ident={i:(i,Fr(0)) for i in range(N)}; els=[(ident,1)]
    for (X,sg) in [(d.Pm,1)]+[(d.refl[q],sg) for q,sg in sig]:
        els=els+[(compose(X,g),sg*c) for g,c in els]
    return els
def coeff_ball(k,i,sigel):
    tot=acb(0); T=C.terms(k)
    for g,c in sigel:
        j,ph=g[i]
        if j in T:
            v=acb(0)
            for q_ in T[j]: v+=e(q_)
            tot+=c*e(ph)*v/2
    return tot/len(sigel)
def b_ball(p,k,i,sigel):
    v=coeff_ball(p*k,i,sigel)
    if k%p==0: v+=coeff_ball(k//p,i,sigel)
    return v
log=open('logs/hecke_s%d.log'%s,'w')
def L(*a):
    s_=' '.join(str(x) for x in a); print(s_,flush=True); log.write(s_+'\n'); log.flush()
L('s=%d N=%d Tlevel=%d primes=%s gamma_order=%d'%(s,N,Lv,PR,d.F.gamma_order() if hasattr(d.F,'gamma_order') else -1))
c0=[i for i,(al,be) in enumerate(C.F.LABELS) if int(al[0])%C.D==0 and int(al[1])%C.D==0]
ps=sorted(d.refl); out={'s':s,'Tlevel':Lv,'primes':PR,'prec_bits':256,'sectors':{}}
t0=time.time()
ks=[k for k in range(-KR*1,KR+1) if k]
def fl(z): return complex(float(z.real.mid()),float(z.imag.mid()))
for signs in itertools.product((1,-1),repeat=len(ps)):
    sig=tuple(zip(ps,signs)); sigel=group(sig)
    # exact c0 projection
    nzc=0
    for i in range(N):
        acc={}
        for g,c in sigel:
            j,ph=g[i]
            if j in c0: acc[ph]=acc.get(ph,0)+c
        if any(v!=0 for v in acc.values()): nzc+=1
    # candidate entries
    cols=[]
    for k in ks:
        Ts=set(C.terms(k))
        for p in PR: Ts|=set(C.terms(p*k))
        cand=set()
        for g,c in sigel:
            inv={g[i][0]:i for i in g}; cand|={inv[j] for j in Ts}
        cols+= [(k,i) for i in sorted(cand)]
    if not cols: L(sig,'no coefficients'); continue
    A0=[coeff_ball(k,i,sigel) for (k,i) in cols]
    rows=[A0]+[[b_ball(p,k,i,sigel) for (k,i) in cols] for p in PR]
    names=['F0']+['T%d F0'%p for p in PR]
    if nzc:   # Eisenstein part present: use cuspidal combinations only
        rows=[[r[j]-2*A0[j] for j in range(len(cols))] for r in rows[1:]]; names=[n+' - 2F0' for n in names[1:]]
    Mf=np.array([[fl(z) for z in r] for r in rows])
    if np.abs(Mf).max()<1e-12: L(sig,'all zero (float)'); out['sectors'][str(sig)]={'lower':0,'c0_rows':nzc}; continue
    # greedy column pivoting to pick a well-conditioned minor
    sv=np.linalg.svd(Mf,compute_uv=False); rk=int(np.sum(sv>1e-8*sv[0]))
    best=None
    for r in range(rk,0,-1):
        # choose rows/cols by QR pivoting
        import scipy.linalg as sl
        _,_,pc=sl.qr(Mf,pivoting=True); cc=list(pc[:r])
        _,_,pr=sl.qr(Mf[:,cc].T,pivoting=True); rr=list(pr[:r])
        Mb=acb_mat([[rows[a][b] for b in cc] for a in rr]); dt=Mb.det()
        if not dt.contains(0): best=(r,rr,cc,dt); break
    r,rr,cc,dt=best
    L(sig,'d_c0rows=%d float sv='%nzc,np.round(sv[:6],6),'certified rank',r,'rows',[names[a] for a in rr],'cols',[cols[b] for b in cc],'det',dt,'%.0fs'%(time.time()-t0))
    out['sectors'][str(sig)]={'lower':r,'c0_rows_nonzero_exact':nzc,'rows':[names[a] for a in rr],'cols':[[int(cols[b][0]),int(cols[b][1])] for b in cc],
        'det':str(dt),'abs_det_lower':float(abs(dt).lower()),'float_singular_values':[float(x) for x in sv[:8]]}
out['secs']=time.time()-t0
json.dump(out,open('certs/hecke_lower_s%d.json'%s,'w'),indent=1)
L('done %.0fs'%(time.time()-t0))
