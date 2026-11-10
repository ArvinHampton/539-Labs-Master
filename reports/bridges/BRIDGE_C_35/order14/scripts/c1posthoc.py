# POST-HOC (descriptive): B(c') with exact s = sqrt(35)*nu2 (removes the float rounding of 2*c'_1+7*c'_2=0) for the 3 C1-failing companions
import sys, json; sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
import mpmath as mp; from fractions import Fraction as Fr; from symbols import FAM,sym_pair
mp.mp.dps=30; pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
A=((2,7),(7,7)); Bf=lambda u,v: sum(u[i]*A[i][j]*v[j] for i in range(2) for j in range(2))
fm=lambda r: mp.mpf(r.numerator)/r.denominator; ef=lambda r: mp.expjpi(2*fm(Fr(r)%1)); res=[]
for j in (12,35,70):
    al,be=pairs[j]
    for tau in (mp.mpc(0.1,0.9),mp.mpc(-0.3,1.2),mp.mpc(0.37,0.7)):
        d=0;m=0
        for n in range(-10,11):
            for k in range(-10,11):
                nu=(al[0]+n,al[1]+k); s=mp.sqrt(35)*fm(nu[1]); sp=-fm(2*nu[0]+7*nu[1])
                t=ef(Bf(nu,be))*s*sp*mp.exp(2j*mp.pi*(sp*sp*tau/4-s*s*mp.conj(tau)/4)); d+=t; m+=abs(t)
        res.append([j,str(tau),mp.nstr(abs(d),4),mp.nstr(abs(d)/m,4)]); print(res[-1],flush=True)
json.dump(res,open('../data/c1posthoc.json','w'))
