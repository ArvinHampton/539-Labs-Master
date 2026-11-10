# U1/U2/U3 coefficient identities for H(Phi_0) on the unit arc [c1, gamma c1]
import sys, json; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
import mpmath as mp
from fractions import Fraction as Fr
from symbols import FAM, sym_pair
mp.mp.dps=25
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
A=((2,7),(7,7)); Bf=lambda u,v: sum(u[i]*A[i][j]*v[j] for i in range(2) for j in range(2))
G=((-1,-7),(2,13)); Gi=((13,7),(-2,-1))
ap=lambda Mx,v:(Mx[0][0]*v[0]+Mx[0][1]*v[1],Mx[1][0]*v[0]+Mx[1][1]*v[1])
c1=(mp.mpf(-1),mp.mpf(1)); gc1=ap(G,c1)
h1=tuple(v/mp.sqrt(mp.mpf(5)/2) for v in c1); hg=tuple(v/mp.sqrt(mp.mpf(5)/2) for v in gc1)
Lg=mp.acosh(-Bf(h1,hg)/2)
res={'L_arc':mp.nstr(Lg,22),'log_eps':mp.nstr(mp.log(6+mp.sqrt(35)),22)}
# angle checks (Category A geometry of PREREG s0)
ang=lambda u,v: mp.acosh(Bf(u,v)/(2*mp.sqrt(Fr(Bf(u,u),2)*Fr(Bf(v,v),2))))
e1=(1,0); e2=(0,1)
res['angles']={k:mp.nstr(ang(*v),15) for k,v in {'e1e2':(e1,e2),'e2_ge1':(e2,ap(G,e1)),'ge1_ge2':(ap(G,e1),ap(G,e2)),'e2_ge2':(e2,ap(G,e2))}.items()}
sgn=lambda v:(v>0)-(v<0)
def weight(nu,N,y):
    b1=Bf(nu,h1); b2=Bf(nu,hg)
    zh=lambda m: tuple((mp.sinh(Lg-m)*h1[i]+mp.sinh(m)*hg[i])/mp.sinh(Lg) for i in range(2))
    f=lambda m: mp.exp(-mp.pi*y*Bf(nu,zh(m))**2)
    den=b2-b1*mp.cosh(Lg); pts=[mp.mpf(0),Lg]
    if den!=0:
        th=-b1*mp.sinh(Lg)/den
        if abs(th)<1:
            mu=mp.atanh(th)
            if 0<=mu<=Lg:
                d=10/mp.sqrt(N*y); pts=sorted(set([mp.mpf(0),Lg]+[p for p in (mu-d,mu,mu+d) if 0<p<Lg]))
    if len(pts)==2 and mp.pi*y*min(b1*b1,b2*b2)>200: return mp.mpf(0)
    return 2*mp.sqrt(N*y)*mp.quad(f,pts)
def wC(nu):  # cone(e2, gamma e2): nu = a e2 + b (-7,13)
    b=-nu[0]/7; a=nu[1]+Fr(13,7)*nu[0]
    if a>=0 and b>=0: return Fr(1,2) if (a==0 or b==0) else Fr(1)
    if a<=0 and b<=0: return Fr(1,2) if (a==0 or b==0) else Fr(1)
    return Fr(0)
def in_fund(nu):  # half-open fundamental cone [e2, gamma e2) and its negative
    b=-nu[0]/7; a=nu[1]+Fr(13,7)*nu[0]
    return (a>0 and b>=0) or (a<0 and b<=0)
def ph(nu,be): v=Fr(Bf(nu,be)); return mp.expjpi(2*mp.mpf(v.numerator)/v.denominator)
mx={'U1':0,'U2':0,'U3':0}; per=[]; inv=[]
for j,(al,be) in enumerate(pairs):
    cE={};cG={};cC={};cF={};nus={}
    for n in range(-60,61):
        for k in range(-60,61):
            nu=(al[0]+n,al[1]+k); Q=Fr(Bf(nu,nu),2)
            if not (0<Q<=8): continue
            p=ph(nu,be); nus.setdefault(Q,[]).append(nu)
            ev=Fr(1+sgn(nu[0])*sgn(nu[1]),2)
            if ev: cE[Q]=cE.get(Q,0)+ev*p
            g=ap(Gi,nu); evg=Fr(1+sgn(g[0])*sgn(g[1]),2)
            if evg: cG[Q]=cG.get(Q,0)+evg*p
            w=wC(nu)
            if w: cC[Q]=cC.get(Q,0)+w*p
            nm=tuple(mp.mpf(c.numerator)/c.denominator for c in nu); Nm=mp.mpf(Q.numerator)/Q.denominator
            w1=weight(nm,Nm,mp.mpf(10)**4)
            if w1==0: continue
            w2=weight(nm,Nm,2*mp.mpf(10)**4); cF[Q]=cF.get(Q,0)+(2*w2-w1)*p
    K=set(cE)|set(cG)|set(cC)|set(cF)
    d1=max([abs(cF.get(q,0)-cE.get(q,0)-cG.get(q,0)) for q in K]+[mp.mpf(0)])
    d2=max([abs(cF.get(q,0)-cC.get(q,0)) for q in K]+[mp.mpf(0)])
    mx['U1']=max(mx['U1'],d1); mx['U2']=max(mx['U2'],d2)
    # gamma invariance of companion
    ga=ap(G,al); ok=all((ga[i]-al[i]).denominator==1 for i in range(2))
    if ok:
        for base in (al,(al[0]+1,al[1]),(al[0],al[1]+1)):
            if (Fr(Bf(ap(G,base),be))-Fr(Bf(base,be))).denominator!=1: ok=False
    d3=None
    if ok:
        inv.append(j); d3=mp.mpf(0)
        for Q,L in nus.items():
            reps=set()
            for nu in L:
                v=nu
                for _ in range(40):
                    if in_fund(v): break
                    b=-v[0]/7; a=v[1]+Fr(13,7)*v[0]
                    # move toward the cone: use gamma or gamma^-1 by hyperbolic position
                    v2=ap(G,v); v3=ap(Gi,v)
                    v=v2 if abs(Fr(Bf(v2,(0,1))))<abs(Fr(Bf(v3,(0,1)))) else v3
                if in_fund(v): reps.add(v)
            so=sum([ph(r,be) for r in reps],mp.mpc(0))
            d3=max(d3,abs(so-cC.get(Q,0)))
        mx['U3']=max(mx['U3'],d3)
    per.append(dict(j=j,U1=mp.nstr(d1,4),U2=mp.nstr(d2,4),U3=None if d3 is None else mp.nstr(d3,4)))
    print(j,mp.nstr(d1,4),mp.nstr(d2,4),d3 and mp.nstr(d3,4),flush=True)
v=lambda d,lo,hi:'pass' if d<=lo else ('FAIL' if d>hi else 'inconclusive')
res.update(U1_max=mp.nstr(mx['U1'],5),U1=v(mx['U1'],1e-7,1e-4),U2_max=mp.nstr(mx['U2'],5),U2=v(mx['U2'],1e-7,1e-4),
           U3_max=mp.nstr(mx['U3'],5),U3=(v(mx['U3'],1e-10,1e-4) if inv else 'no gamma-invariant companions'),gamma_invariant=inv,per=per)
json.dump(res,open('../data/u.json','w'),indent=1); print({k:res[k] for k in res if k!='per'})
