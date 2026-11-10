# shared: exact-s boundary terms at c' and c1 for a companion list; argv: mode
import sys, json; sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
import mpmath as mp; from fractions import Fraction as Fr; from symbols import sym_pair, MU, a, hA, add
mp.mp.dps=30
A=((2,7),(7,7)); Bf=lambda u,v: sum(u[i]*A[i][j]*v[j] for i in range(2) for j in range(2))
fm=lambda r: mp.mpf(r.numerator)/r.denominator; ef=lambda r: mp.expjpi(2*fm(Fr(r)%1))
TAUS=(mp.mpc(0.1,0.9),mp.mpc(-0.3,1.2),mp.mpc(0.37,0.7))
def bterm(al,be,end):
    out=[]
    for tau in TAUS:
        d=0;m=0
        for n in range(-10,11):
            for k in range(-10,11):
                nu=(al[0]+n,al[1]+k)
                if end=='cp': s=mp.sqrt(35)*fm(nu[1]); sp=-fm(2*nu[0]+7*nu[1])
                else: s=mp.sqrt(10)*fm(nu[0]); sp=mp.sqrt(14)*fm(nu[0]+nu[1])
                t=ef(Bf(nu,be))*s*sp*mp.exp(2j*mp.pi*(sp*sp*tau/4-s*s*mp.conj(tau)/4)); d+=t; m+=abs(t)
        out.append(abs(d)/m if m else mp.mpf(0))
    return out
isZ=lambda r: Fr(r).denominator==1
def rg1p(al,be): return (isZ(2*(al[0]+al[1])) and isZ(14*(be[0]+be[1])) and isZ(14*(be[0]+be[1])*(al[0]+al[1]))) or (isZ(2*al[0]) and isZ(10*be[0]) and isZ(10*be[0]*al[0]))
mode=sys.argv[1]
if mode=='C1p':
    K1=[sym_pair('K1',i) for i in range(35)]; cpm=0; c1m=0; per=[]
    for j,(al,be) in enumerate(K1):
        x=max(bterm(al,be,'cp')); y=max(bterm(al,be,'c1')); cpm=max(cpm,x); c1m=max(c1m,y); per.append([j,mp.nstr(x,3),mp.nstr(y,3)]); print(per[-1],flush=True)
    res=dict(C1p_max=mp.nstr(cpm,4),verdict='pass' if cpm<=1e-25 else ('FAIL' if cpm>1e-12 else 'inconclusive'),control=('pass' if c1m>1e-6 else 'FAIL'),per=per)
else:
    H=[(mu,hA) for mu in MU]+[(add(a,mu),add(a,hA)) for mu in MU]; pred=set(); Z=set(); gap=1.0; per=[]
    for j,(al,be) in enumerate(H):
        v=bterm(al,be,'c1'); x=max(v); p=rg1p(al,be)
        if p: pred.add(j)
        if x<=1e-25: Z.add(j)
        else: gap=min(gap,float(min(v)))
        per.append([j,str(al),str(be),mp.nstr(x,3),p]); print(per[-1],flush=True)
    res=dict(pred=sorted(pred),zero=sorted(Z),min_nonzero=gap,verdict='pass' if (Z==pred and pred and gap>1e-6) else 'FAIL',per=per)
print({k:v for k,v in res.items() if k!='per'}); json.dump(res,open('../data/%s.json'%mode,'w'),indent=1,default=str)
