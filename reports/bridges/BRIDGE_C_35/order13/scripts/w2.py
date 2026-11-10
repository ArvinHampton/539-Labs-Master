# W2a parity algebra; W2c Laplacian defect of Phi_orth on [c', c1]; W2d glued factorisation at c'
import sys, json; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
import mpmath as mp
from fractions import Fraction as Fr
from symbols import FAM, sym_pair
mp.mp.dps=30
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
A=((2,7),(7,7)); Bf=lambda u,v: sum(u[i]*A[i][j]*v[j] for i in range(2) for j in range(2))
sgn=lambda v:(v>0)-(v<0); out={}
# W2a
bad=0
for al,be in pairs:
    for n in range(-12,13):
        for k in range(-12,13):
            nu=(al[0]+n,al[1]+k); s1,s2,s3=sgn(nu[0]),sgn(nu[1]),sgn(nu[0]+21*nu[1])
            p=Fr((1+s1)*(1+s2),4)-Fr(s1+s3,2); pm=Fr((1-s1)*(1-s2),4)-Fr(-s1-s3,2)
            if (p+pm)/2!=Fr(1+s1*s2,4): bad+=1
out['W2a_mismatches']=bad; print(out,flush=True)
Lh=mp.log(6+mp.sqrt(35))/2
cp=(mp.mpf(7)/mp.sqrt(35),mp.mpf(-2)/mp.sqrt(35)); e1=(mp.mpf(1),mp.mpf(0)); ch=(mp.mpf(-1)/mp.sqrt(2.5),1/mp.sqrt(mp.mpf(2.5)))
sg=None
for s0 in (1,-1):
    for flip in (1,-1):
        zz=tuple(mp.cosh(Lh)*cp[i]+s0*mp.sinh(Lh)*e1[i] for i in range(2))
        if max(abs(zz[i]-flip*ch[i]) for i in range(2))<1e-20: sg=(s0,flip)
assert sg is not None; out['orientation']=sg; s0=sg[0]
zf=lambda m: tuple(mp.cosh(m)*cp[i]+s0*mp.sinh(m)*e1[i] for i in range(2))
zp=lambda m: tuple(mp.sinh(m)*cp[i]+s0*mp.cosh(m)*e1[i] for i in range(2))
def ph(nu,be): v=Fr(Bf(nu,be)); return mp.expjpi(2*mp.mpf(v.numerator)/v.denominator)
def lhs(nm,y):
    f=lambda m:(lambda s,sp: mp.sqrt(y)*mp.exp(-mp.pi*y*(s*s+sp*sp)/2)*(mp.pi*y*(s*s+sp*sp)/2-mp.pi**2*y*y*s*s*sp*sp))(Bf(nm,zf(m)),Bf(nm,zp(m)))
    return mp.quad(f,mp.linspace(0,Lh,7))
def bnd(nm,y,m):
    s=Bf(nm,zf(m)); sp=Bf(nm,zp(m)); return s*sp*mp.exp(-mp.pi*y*(s*s+sp*sp)/2)
D=0; per=[]
for j in range(0,105,7):
    al,be=pairs[j]; cL={}; cR={}
    for n in range(-14,15):
        for k in range(-14,15):
            nu=(al[0]+n,al[1]+k); Q=Fr(Bf(nu,nu),2)
            if abs(Q)>8: continue
            nm=tuple(mp.mpf(c.numerator)/c.denominator for c in nu); p=ph(nu,be)
            for y in (mp.mpf(1)/2,mp.mpf(1),mp.mpf(2)):
                bl=bnd(nm,y,Lh); b_=bnd(nm,y,0)
                if abs(bl)+abs(b_)<mp.mpf(10)**-40 and abs(Bf(nm,zf(Lh/2)))>3: continue
                key=(Q,y); cL[key]=cL.get(key,0)+p*lhs(nm,y); cR[key]=cR.get(key,0)+p*mp.pi/2*y**1.5*(bl-b_)
    d=max([abs(cL[k]-cR[k])/max(1,abs(cR[k])) for k in cL]+[mp.mpf(0)]); D=max(D,d); per.append([j,mp.nstr(d,4)]); print(j,mp.nstr(d,4),flush=True)
out['W2c_max']=mp.nstr(D,4); out['W2c']='pass' if D<=1e-15 else ('FAIL' if D>1e-6 else 'inconclusive'); out['W2c_per']=per
# W2d at c': direct vs glued (nu2, w) with twist w(2b0+7b1) - (35/2) b1 nu2
al,be=pairs[1]; D2=0
fm=lambda r: mp.mpf(r.numerator)/r.denominator
for tau in (mp.mpc(0.1,0.9),mp.mpc(-0.3,1.2),mp.mpc(0.37,0.7)):
    ds=0; gl=0
    for n in range(-25,26):
        for k in range(-25,26):
            nu=(al[0]+n,al[1]+k); nm=(fm(nu[0]),fm(nu[1])); s=Bf(nm,cp); sp=Bf(nm,tuple(s0*v for v in e1))
            ds+=ph(nu,be)*s*sp*mp.exp(2j*mp.pi*(sp*sp*tau/4-s*s*mp.conj(tau)/4))
    for k in range(-25,26):
        n2=al[1]+k
        for n in range(-60,61):
            w=al[0]+Fr(7,2)*n2+n
            if abs(w)>30: continue
            tw=Fr(w*(2*be[0]+7*be[1])-Fr(35,2)*be[1]*n2)
            gl+=2*s0*mp.sqrt(35)*fm(w)*fm(n2)*mp.exp(2j*mp.pi*(fm(w)**2*tau-35*fm(n2)**2*mp.conj(tau)/4))*mp.expjpi(2*fm(tw%1))
    D2=max(D2,abs(ds-gl)/abs(gl))
out['W2d']=mp.nstr(D2,4); out['W2d_verdict']='pass' if D2<=1e-20 else 'FAIL'
print({k:v for k,v in out.items() if k!='W2c_per'}); json.dump(out,open('../data/w2.json','w'),indent=1,default=str)
