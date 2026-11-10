# POST-HOC (descriptive): W2d with error normalised by sum|terms|, 6 companions incl. beta != 0; dps 30
import sys, json; sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
import mpmath as mp; from fractions import Fraction as Fr; from symbols import FAM,sym_pair
mp.mp.dps=30
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
A=((2,7),(7,7)); Bf=lambda u,v: sum(u[i]*A[i][j]*v[j] for i in range(2) for j in range(2))
cp=(mp.mpf(7)/mp.sqrt(35),mp.mpf(-2)/mp.sqrt(35)); fm=lambda r: mp.mpf(r.numerator)/r.denominator
ef=lambda r: mp.expjpi(2*fm(Fr(r)%1)); res=[]
for j in (1,5,40,47,75,90):
    al,be=pairs[j]
    for tau in (mp.mpc(0.1,0.9),mp.mpc(0.37,0.7)):
        ds=0; gl=0; mag=0
        for n in range(-10,11):
            for k in range(-10,11):
                nu=(al[0]+n,al[1]+k); nm=(fm(nu[0]),fm(nu[1])); s=Bf(nm,cp); sp=-Bf(nm,(1,0))
                t=ef(Bf(nu,be))*s*sp*mp.exp(2j*mp.pi*(sp*sp*tau/4-s*s*mp.conj(tau)/4)); ds+=t; mag+=abs(t)
        for k in range(-10,11):
            n2=al[1]+k
            for n in range(-60,61):
                w=al[0]+Fr(7,2)*n2+n
                if abs(w)>30: continue
                gl+=-2*mp.sqrt(35)*fm(w)*fm(n2)*mp.exp(2j*mp.pi*(fm(w)**2*tau-35*fm(n2)**2*mp.conj(tau)/4))*ef(w*(2*be[0]+7*be[1])-Fr(35,2)*be[1]*n2)
        res.append([j,str(tau),mp.nstr(abs(ds),4),mp.nstr(abs(ds-gl)/mag,4)]); print(res[-1],flush=True)
json.dump(res,open('../data/w2d_posthoc.json','w'))
