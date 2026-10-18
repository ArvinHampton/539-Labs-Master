# (B) Cusp rows at x = +-1 from Hecke L-values at s=0:
#   kappa_c(h) = sum_chi Fhat_c(chi) * sum_{a coprime to m} chi(a) e(h N a/140) N a^{-s} |_{s=0}
#             = (1/48) sum_{psi mod 140} tau(psi^-) psi(h) sum_chi Fhat_c(chi) L_m(0, chi * psi o N)
#   Phi_c(x) = kappa_c(-1/x) - |x| sum_{c' cusp} S[c,c'] kappa_{c'}(x)
import numpy as np, pickle, itertools, cmath, math, sys
from fractions import Fraction as fr
import cypari2; pari=cypari2.Pari(); pari.allocatemem(10**9); gp=lambda s: pari(s)
sys.path.insert(0,'.')
from family import LABELS
import kappa_all
F=pickle.load(open("fitF.pkl","rb")); pc=F['per_comp']; cyc=F['cyc']
import json; CS=json.load(open('component_split.json'))
LV=pickle.load(open("lvalues.pkl","rb"))['res']
chars=list(itertools.product(*[range(c) for c in cyc])); ncl=96
C=sorted({i for i,rec in pc.items() for s,r in rec.items() if r and r['cusp']>1e-12})
gp('bnf=bnfinit(y^2-35,1); P2=idealprimedec(bnf,2)[1]; P5=idealprimedec(bnf,5)[1]; P7=idealprimedec(bnf,7)[1]')
gp('m=idealmul(bnf,idealmul(bnf,idealpow(bnf,P2,3),P5),P7); bnr=bnrinit(bnf,[m,[1,1]],1); Li=ideallist(bnf,3000)')
# norm mod 140 as class function
normcls={}
for n in range(1,3001):
    if math.gcd(n,70)!=1: continue
    for c in gp(f'apply(I->bnrisprincipal(bnr,I,0),Li[{n}])'):
        c=tuple(int(t) for t in c)
        if c in normcls: assert normcls[c]==n%140, "norm mod 140 not a class function"
        normcls[c]=n%140
assert len(normcls)==96
def ev(chi,c): return cmath.exp(2j*math.pi*float(sum(fr(chi[i]*c[i],cyc[i]) for i in range(3))))
L0={chi:LV[chi]['L0'] for chi in chars}
zeta0={c:sum(ev(chi,c).conjugate()*L0[chi] for chi in chars)/ncl for c in chars}
def kappaL(i,h):
    Fh={tuple(e['chi']):float(fr(e['abs']))*cmath.exp(2j*math.pi*float(fr(e['phase_turns']))) for e in CS[str(i)]['data']['1']['cusp_coeffs']}
    return sum(sum(Fh[chi]*ev(chi,c) for chi in Fh)*cmath.exp(2j*math.pi*normcls[c]*h/140)*zeta0[c] for c in chars)
S=np.load("../2026-10-17-psi-conditions/S_matrix.npy"); ph=np.load("../2026-10-17-psi-conditions/phi_rows.npy")
out=[]
for h in (1,-1):
    kL=np.array([kappaL(i,h) for i in C]); kE=np.array([kappa_all.fcoef(LABELS[i],fr(h))[2] for i in C])
    out.append(f"kappa_c({h:+d}) over the 24 cusp rows: max |L-value formula - exact Bernoulli kappa| = {np.abs(kL-kE).max():.2e}  (max |kappa| = {np.abs(kE).max():.3f})")
    if h==1: k1=kL
    else: km1=kL
Sc=S[np.ix_(C,C)]
for x,k_in,k_out,idx in ((1,km1,k1,0),(-1,k1,km1,5)):
    Phi=k_in - abs(x)*Sc@k_out
    out.append(f"Phi_c({x:+d}) from L(0)-values vs phi_rows: max dev = {np.abs(Phi-ph[idx,C]).max():.2e};  Phi_73({x:+d}) = {Phi[C.index(73)]:.12f}")
# Dirichlet-twist form check: chi*psi o N in terms of Cl_m chars; psi mod 140 -> character of Cl_m via norm
# central-value replacement test
Lh={chi:LV[chi].get('Lhalf_prim') for chi in chars}
# FE check for totally odd cusp chars: L(0,chi) = W*140*L(1,conj chi)/pi^2
fe=[]
for chi in chars:
    r=LV[chi]
    if 'Lone' in r and r['cond_inf']==[1,1]:
        cc=tuple((-chi[i])%cyc[i] for i in range(3))
        fe.append(abs(r['L0prim']-r['rootno']*140*LV[cc]['Lone']/math.pi**2))
out.append(f"functional equation L(0,chi)=W(chi)*140*L(1,chi^-)/pi^2 for the 12 totally odd cusp chars: max dev {max(fe):.2e}")
# Central-value hypothesis: same linear functional with L_m(0,.) replaced by L(1/2,.) (cusp chars only, others set to their values?) 
open("cusp_rows_L.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
pickle.dump(dict(C=C,normcls=normcls,k1=k1,km1=km1),open("cusp_rows_L.pkl","wb"))
