# RG1' fresh test on K1 family
import sys, json; sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
import mpmath as mp; from fractions import Fraction as Fr; from symbols import sym_pair
mp.mp.dps=30; pairs=[sym_pair('K1',i) for i in range(35)]; isZ=lambda r: Fr(r).denominator==1
A=((2,7),(7,7)); Bf=lambda u,v: sum(u[i]*A[i][j]*v[j] for i in range(2) for j in range(2))
fm=lambda r: mp.mpf(r.numerator)/r.denominator; ef=lambda r: mp.expjpi(2*fm(Fr(r)%1))
pred={j for j,(al,be) in enumerate(pairs) if (isZ(2*(al[0]+al[1])) and isZ(14*(be[0]+be[1])) and isZ(14*(be[0]+be[1])*(al[0]+al[1]))) or (isZ(2*al[0]) and isZ(10*be[0]) and isZ(10*be[0]*al[0]))}
meas={}; 
for j,(al,be) in enumerate(pairs):
    v=[]
    for tau in (mp.mpc(0.1,0.9),mp.mpc(-0.3,1.2),mp.mpc(0.37,0.7)):
        d=0;m=0
        for n in range(-10,11):
            for k in range(-10,11):
                nu=(al[0]+n,al[1]+k); s=mp.sqrt(10)*fm(nu[0]); sp=mp.sqrt(14)*fm(nu[0]+nu[1])
                t=ef(Bf(nu,be))*s*sp*mp.exp(2j*mp.pi*(sp*sp*tau/4-s*s*mp.conj(tau)/4)); d+=t; m+=abs(t)
        v.append(abs(d)/m if m else mp.mpf(0))
    meas[j]=max(v); print(j,mp.nstr(meas[j],3),j in pred,flush=True)
Z={j for j,v in meas.items() if v<=1e-25}; gap=min([float(v) for j,v in meas.items() if j not in Z]+[1.0])
res=dict(pred=sorted(pred),meas_zero=sorted(Z),min_nonzero=gap,verdict='pass' if (Z==pred and gap>1e-6) else 'FAIL')
print(res); json.dump(res,open('../data/rg1k1.json','w'),indent=1)
