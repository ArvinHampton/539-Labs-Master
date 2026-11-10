# D1-D4: (Delta0 - 1/4) Phi0 = (pi/2) y^{3/2} (B(gamma c1) - B(c1)); per-Fourier-mode, mpmath dps 30
import sys, json; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
import mpmath as mp
from fractions import Fraction as Fr
from symbols import FAM, sym_pair
mp.mp.dps=30
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
A=((2,7),(7,7)); Bf=lambda u,v: sum(u[i]*A[i][j]*v[j] for i in range(2) for j in range(2))
G=((-1,-7),(2,13)); Gi=((13,7),(-2,-1)); ap=lambda M,v:(M[0][0]*v[0]+M[0][1]*v[1],M[1][0]*v[0]+M[1][1]*v[1])
L2=mp.log(6+mp.sqrt(35))
ch=tuple(mp.mpf(v)/mp.sqrt(mp.mpf(5)/2) for v in (-1,1)); e2h=(mp.mpf(0),1/mp.sqrt(mp.mpf(7)/2))
gch=ap(G,ch)
sg=None
for s0 in (1,-1):
    zz=tuple(mp.cosh(L2)*ch[i]+s0*mp.sinh(L2)*e2h[i] for i in range(2))
    if max(abs(zz[i]-gch[i]) for i in range(2))<1e-20: sg=s0
assert sg is not None
zp=lambda m: tuple(mp.sinh(m)*ch[i]+sg*mp.cosh(m)*e2h[i] for i in range(2))
zf=lambda m: tuple(mp.cosh(m)*ch[i]+sg*mp.sinh(m)*e2h[i] for i in range(2))
def ph(nu,be): v=Fr(Bf(nu,be)); return mp.expjpi(2*mp.mpf(v.numerator)/v.denominator)
def lhs(nm,y):
    f=lambda m:(lambda s,sp: mp.sqrt(y)*mp.exp(-mp.pi*y*(s*s+sp*sp)/2)*(mp.pi*y*(s*s+sp*sp)/2-mp.pi**2*y*y*s*s*sp*sp))(Bf(nm,zf(m)),Bf(nm,zp(m)))
    return mp.quad(f,mp.linspace(0,L2,9))
def bnd(nm,y,m):
    s=Bf(nm,zf(m)); sp=Bf(nm,zp(m)); return s*sp*mp.exp(-mp.pi*y*(s*s+sp*sp)/2)
inv=[0,12,18,23,29,35,47,53,58,64,70,82,88,93,99]
out={'orientation_sign':sg,'D1':[], 'D3':[], 'D4':[]}; D1max=0; D4max=0
sel=list(range(0,105,7))+inv[:3]
for j in sorted(set(sel)):
    al,be=pairs[j]; cL={}; cR={}; b0={}; b1={}
    for n in range(-14,15):
        for k in range(-14,15):
            nu=(al[0]+n,al[1]+k); Q=Fr(Bf(nu,nu),2)
            if abs(Q)>8: continue
            nm=tuple(mp.mpf(c.numerator)/c.denominator for c in nu); p=ph(nu,be)
            for y in (mp.mpf(1)/2,mp.mpf(1),mp.mpf(2)):
                bl=bnd(nm,y,L2); b_=bnd(nm,y,0)
                if abs(bl)+abs(b_)<mp.mpf(10)**-40 and abs(Bf(nm,zf(L2/2)))>3: continue
                key=(Q,y); cL[key]=cL.get(key,0)+p*lhs(nm,y); cR[key]=cR.get(key,0)+p*mp.pi/2*y**1.5*(bl-b_)
                b0[key]=b0.get(key,0)+p*b_; b1[key]=b1.get(key,0)+p*bl
    d=max([abs(cL[k]-cR[k])/max(1,abs(cR[k])) for k in cL]+[mp.mpf(0)]); D1max=max(D1max,d)
    out['D1'].append([j,mp.nstr(d,4)])
    if j in inv:
        d4=max([abs(b1[k]-b0[k]) for k in b0]+[mp.mpf(0)]); D4max=max(D4max,d4); out['D4'].append([j,mp.nstr(d4,4)])
    print(j,mp.nstr(d,4),flush=True)
# D3 exact characteristics: negative factor at c1 has u in alpha1+Z, at gamma c1 in (Gi alpha)_1+Z
for j,(al,be) in enumerate(pairs):
    ga=ap(Gi,al); out['D3'].append([j,str(al[0]%1),str(ga[0]%1),str((-ga[0])%1)])
chars=sorted({r[1] for r in out['D3']}); gchars=sorted({r[2] for r in out['D3']}|{r[3] for r in out['D3']})
out['D3_summary']=dict(c1_chars=chars,gamma_chars_pm=gchars,gamma_chars_subset_of_c1_chars_pm=set(gchars)<=set(chars)|{str((-Fr(c))%1) for c in chars})
# D2 factorisation at 3 tau (companion 1)
al,be=pairs[1]; D2=0
for tau in (mp.mpc(0.1,0.9),mp.mpc(-0.3,1.2),mp.mpc(0.37,0.7)):
    dsum=0; tp=0; tm=0
    for n in range(-30,31):
        for k in range(-30,31):
            nu=(al[0]+n,al[1]+k); nm=tuple(mp.mpf(c.numerator)/c.denominator for c in nu)
            s=Bf(nm,ch); sp=Bf(nm,tuple(sg*v for v in e2h))
            dsum+=ph(nu,be)*s*sp*mp.exp(2j*mp.pi*(sp*sp*tau/4-s*s*mp.conj(tau)/4))
    for n in range(-30,31):
        m_=al[0]+al[1]+n; mm=mp.mpf(m_.numerator)/m_.denominator
        tp+=mm*mp.exp(2j*mp.pi*(7*mm*mm*tau/2))*ph2 if False else mm*mp.exp(2j*mp.pi*(7*mm*mm*tau/2+7*(float(0))))
    # twists exactly via B split: B(nu,beta) = -5 b0 u + 7(b0+b1) m
    tp=0; tm=0
    for n in range(-30,31):
        m_=al[0]+al[1]+n; u_=al[0]+n
        mm=mp.mpf(m_.numerator)/m_.denominator; uu=mp.mpf(u_.numerator)/u_.denominator
        tp+=mm*mp.exp(2j*mp.pi*(7*mm*mm*tau/2))*mp.expjpi(2*mp.mpf(Fr(7*(be[0]+be[1])*m_).numerator)/Fr(7*(be[0]+be[1])*m_).denominator)
        tm+=uu*mp.exp(2j*mp.pi*(5*uu*uu*tau/2))*mp.expjpi(2*mp.mpf(Fr(5*be[0]*u_).numerator)/Fr(5*be[0]*u_).denominator)
    pred=sg*mp.sqrt(140)*tp*mp.conj(tm); D2=max(D2,abs(dsum-pred)/abs(pred))
v=lambda d,lo,hi:'pass' if d<=lo else ('FAIL' if d>hi else 'inconclusive')
out.update(D1_max=mp.nstr(D1max,4),D1=v(D1max,1e-15,1e-6) and out['D1'],D1_verdict=v(D1max,1e-15,1e-6),D2_max=mp.nstr(D2,4),D2_verdict=v(D2,1e-20,1e-6),D4_max=mp.nstr(D4max,4),D4_verdict=v(D4max,1e-15,1e-6))
json.dump(out,open('../data/d.json','w'),indent=1,default=str)
print({k:out[k] for k in ('orientation_sign','D1_max','D1_verdict','D2_max','D2_verdict','D4_max','D4_verdict','D3_summary')})
