# For every component u_c and sign: fit c(g*n) = sum_{N a = n} F(class_m(a)),  n coprime to 70, m = p2^3 p5 p7 oo1 oo2,
# then expand F in ray class characters and split: sigma-invariant (Eisenstein/genus) | non-invariant pure type (Maass cusp) | mixed (must vanish)
import numpy as np, cypari2, itertools, math, json, uvec, sys
from collections import defaultdict
from uvec import vectors
from family import LABELS
pari=cypari2.Pari(); pari.allocatemem(2*10**9); gp=lambda s: pari(s)
QMAX=400; BX=420
_o=uvec.cone_pts; uvec.cone_pts=lambda a,b,r1,r2,s,Q,Bx=40:_o(a,b,r1,r2,s,Q,Bx=BX)
gp('bnf=bnfinit(y^2-35,1); P2=idealprimedec(bnf,2)[1]; P5=idealprimedec(bnf,5)[1]; P7=idealprimedec(bnf,7)[1]')
gp('m=idealmul(bnf,idealmul(bnf,idealpow(bnf,P2,3),P5),P7); bnr=bnrinit(bnf,[m,[1,1]],1); gens=bnr.gen')
cyc=[int(c) for c in gp('bnr.cyc')]; ncl=int(np.prod(cyc))
allc=list(itertools.product(*[range(c) for c in cyc])); cidx={c:i for i,c in enumerate(allc)}
NM=int(19600*QMAX*0.98)//140
gp(f'L=ideallist(bnf,{NM})')
Mx=np.zeros((NM+1,ncl))
for n in range(1,NM+1):
    if math.gcd(n,70)!=1: continue
    for c in gp(f'apply(I->bnrisprincipal(bnr,I,0),L[{n}])'):
        Mx[n,cidx[tuple(int(t) for t in c)]]+=1
# sign classes & sigma action for typing
gp('mm=idealhnf(bnf,m); e=nfbasistoalg(bnf,mm[,1]); e2=nfbasistoalg(bnf,mm[,2])')
gp('findsig(s1,s2)=for(a=-80,80,for(b=-80,80, my(x=1+a*e+b*e2, v=nfeltembed(bnf,x)); if(sign(v[1])==s1 && sign(v[2])==s2, return(bnrisprincipal(bnr,idealhnf(bnf,x),0))))); error("nf")')
cpm=[int(t) for t in gp('findsig(1,-1)')]; cmp_=[int(t) for t in gp('findsig(-1,1)')]
sg=[[int(t) for t in gp(f'bnrisprincipal(bnr,nfgaloisapply(bnf,-y,gens[{i+1}]),0)')] for i in range(len(cyc))]
def ev(chi,c): return np.exp(2j*np.pi*sum(chi[i]*c[i]/cyc[i] for i in range(len(cyc))))
chars=allc
def sigc(c): return tuple(sum(c[i]*sg[i][k] for i in range(len(cyc)))%cyc[k] for k in range(len(cyc)))
info=[]
for chi in chars:
    t=(int(round(np.angle(ev(chi,cmp_))/np.pi))%2, int(round(np.angle(ev(chi,cpm))/np.pi))%2)
    inv=all(abs(ev(chi,sigc(c))-ev(chi,c))<1e-9 for c in [tuple(1 if k==i else 0 for k in range(len(cyc))) for i in range(len(cyc))])
    info.append((t,inv))
X=np.array([[ev(chi,c) for c in allc] for chi in chars])  # X[chi,c]
Mrows=np.arange(1,NM+1); Mrows=Mrows[[math.gcd(int(n),70)==1 for n in Mrows]]
A=Mx[Mrows]
res=[]; per_comp={}
for idx,(al,be) in enumerate(LABELS):
    q,ph,c0=vectors(al,be,Qmax=QMAX)
    rec={}
    for sgn in (1,-1):
        sel=np.sign(q)==sgn
        N=np.rint(19600*np.abs(q[sel])).astype(np.int64); P=ph[sel]
        coef=defaultdict(complex)
        for n,v in zip(N,P): coef[int(n)]+=v
        coef={n:v for n,v in coef.items() if abs(v)>1e-9}
        if not coef: rec[sgn]=None; continue
        g=0
        for n in coef: g=math.gcd(g,n)
        rows=Mrows[Mrows<=int(19600*QMAX*0.98)//g]
        b=np.array([coef.get(g*int(n),0) for n in rows]); Ar=Mx[rows]
        Fv,*_=np.linalg.lstsq(Ar,b,rcond=None)
        resid=np.abs(Ar@Fv-b).max()
        Fs=(Fv+np.array([Fv[cidx[sigc(c)]] for c in allc]))/2   # sigma-symmetrised (the determined part)
        Fh=X.conj()@Fs/ncl     # F = sum_chi Fh[chi] chi
        eis=sum(abs(Fh[i])**2 for i in range(ncl) if info[i][1])
        cusp=sum(abs(Fh[i])**2 for i in range(ncl) if (not info[i][1]) and info[i][0][0]==info[i][0][1])
        mix=sum(abs(Fh[i])**2 for i in range(ncl) if (not info[i][1]) and info[i][0][0]!=info[i][0][1])
        rec[sgn]=dict(g=g,resid=float(resid),eis=float(eis),cusp=float(cusp),mixed=float(mix),
                      cusp_chars=[(chars[i],complex(np.round(Fh[i],8))) for i in range(ncl) if (not info[i][1]) and abs(Fh[i])>1e-8])
    per_comp[idx]=rec
    if idx%10==0: print(idx,{s:(r and {k:r[k] for k in ('g','resid','eis','cusp','mixed')}) for s,r in rec.items()},flush=True)
import pickle; pickle.dump(dict(cyc=cyc,info=info,per_comp=per_comp,cpm=cpm,cmp=cmp_,sg=sg),open("fitF.pkl","wb"))
lines=[f"m = p2^3 p5 p7 oo1 oo2, Cl_m^+ = {cyc}"]
for idx,rec in per_comp.items():
    s=[]
    for sgn,r in rec.items():
        s.append("empty" if r is None else f"sgn{sgn:+d} g={r['g']} resid={r['resid']:.1e} |Eis|^2={r['eis']:.4f} |cusp|^2={r['cusp']:.4f} |mixed|^2={r['mixed']:.1e}")
    lines.append(f"{idx:3d} {LABELS[idx]}  "+" ; ".join(s))
open("fitF.txt","w").write("\n".join(lines)+"\n"); print("done")
