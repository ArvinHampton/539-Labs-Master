# A3 (Category B): literal S = S^nu + L at 2 tau, 3 companions, dps 25, box 40 (L via the closed form D)
import sys, json; sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
import mpmath as mp; from fractions import Fraction as Fr; from symbols import sym_pair
mp.mp.dps=25; sgn=lambda v:(v>0)-(v<0); ind=lambda b:1 if b else 0
A=((2,7),(7,7)); Bf=lambda u,v: sum(u[i]*A[i][j]*v[j] for i in range(2) for j in range(2))
fm=lambda r: mp.mpf(r.numerator)/r.denominator; ef=lambda r: mp.expjpi(2*fm(Fr(r)%1)); res=[]
for f,i in (('K2',0),('K3',5),('K4',12)):
    al,be=sym_pair(f,i); s_=al[0]+21*al[1]
    for tau in (mp.mpc(0.1,0.9),mp.mpc(-0.2,1.05)):
        S=0; Sn=0; Lt=0
        for n in range(-40,41):
            for k in range(-40,41):
                nu=(al[0]+n,al[1]+k); s1,s2,s3=sgn(nu[0]),sgn(nu[1]),sgn(nu[0]+21*nu[1])
                W=ind(n>=0 and k>=0)-Fr(sgn(n)+sgn(n+21*k),2); p=Fr((1+s1)*(1+s2),4)-Fr(s1+s3,2)
                h1=ind(n>=0)-Fr(1+s1,2); h2=ind(k>=0)-Fr(1+s2,2)
                D=Fr(1+s1,2)*h2+Fr(1+s2,2)*h1+h1*h2-Fr(sgn(n)-s1,2)-Fr(sgn(n+21*k)-sgn(n+21*k+s_),2)
                if not (W or p or D): continue
                Q=Fr(Bf(nu,nu),2); e=ef(Bf(nu,be))*mp.exp(2j*mp.pi*fm(Q)*tau)
                S+=W*e; Sn+=p*e; Lt+=D*e
        d=abs(S-Sn-Lt)/max(1,abs(S)); res.append([f,i,str(tau),mp.nstr(d,4)]); print(res[-1],flush=True)
json.dump(dict(rows=res,verdict='pass' if max(float(r[3]) for r in res)<=1e-18 else 'FAIL'),open('../data/a3.json','w'),indent=1)
