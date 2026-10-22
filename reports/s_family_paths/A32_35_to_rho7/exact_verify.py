# Exact verification in Z[zeta_L] (L=29400) that the numerically found Y intertwines rho35(x)chi^3 and rho_7|W.
import sys,json,numpy as np
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A/scripts')
from weil_family import WFam
from fractions import Fraction as Fr
import flint
L=29400
F=WFam(7); F.build_W(); w=F.w
good=np.nonzero(F.good)[0]; sizes=sorted(set(int(F.size[o]) for o in good))
# unnormalised orbit basis: rho' = Delta^-1 rho Delta, Delta=diag(sqrt size); Y'=Delta^-1 Y
wsize={int(F.widx[o]):int(F.size[o]) for o in good}
# exact S7W, T7W as dicts {(row,col): {exp:coef}} ; value = (1/sqrt35) * sum coef*zeta^exp  (S) ; T has no 1/sqrt35
def restrict(rowfun):
    M={}
    for o in good:
        i0=F.rep[o]; J,PH=rowfun(i0)
        for j,ph in zip(J,PH):
            c=F.widx[F.orb[j]]
            if c<0: continue
            e=(3*int(ph)+3*int(F.ph[j])-3*int(F.ph[i0]))%L
            d=M.setdefault((int(F.widx[o]),int(c)),{}); d[e]=d.get(e,0)+1
    return M
S7=restrict(F.S_row); J,PH=F.T_mono(); T7=restrict(lambda i:(J[i:i+1],PH[i:i+1]))
# rho35: same construction as RTA_prereg weil_odd; S = eps/sqrt35 * zeta^{-L b}, eps = i (numerically fixed there; recorded)
A=np.array([[2,7],[7,7]],dtype=object); det=-35; n=35
adj=np.array([[7,-7],[-7,2]],dtype=object)
reps=sorted({tuple((adj.dot(np.array([x,y],dtype=object)))%n) for x in range(n) for y in range(n)})
reps=[np.array(r,dtype=object) for r in reps]
b=lambda r1,r2: Fr(int(r1.dot(A.dot(r2))),det*det)%1
q=[Fr((pow(2,-1,n)*int(b(r,r)*n))%n,n) for r in reps]
k=3; eps_e=L//4; chiS=(3*L//4*k)%L; chiT=(k*L//12)%L      # eps=i ; chi(S)=(-i)^k ; chi(T)=e(k/12)
S35={(a,c):{(eps_e+chiS-int(b(reps[a],reps[c])*L))%L:1} for a in range(n) for c in range(n)}
T35={(a,a):{(int(q[a]*L)+chiT)%L:1} for a in range(n)}
X=np.load('X_chi3.npy'); nz=np.argwhere(np.abs(X)>1e-9); i0,j0=nz[0]
Y={}
for (r,c) in nz:
    ph=np.angle(X[r,c]/X[i0,j0])/(2*np.pi)*L; e=int(round(ph))%L; assert abs(ph-round(ph))<1e-6; Y[(int(r),int(c))]={e:1}
def mul(A_,B_):
    out={}
    bi={}
    for (r,c),v in B_.items(): bi.setdefault(r,[]).append((c,v))
    for (r,m),v in A_.items():
        for c,u in bi.get(m,[]):
            d=out.setdefault((r,c),{})
            for e1,c1 in v.items():
                for e2,c2 in u.items():
                    e=(e1+e2)%L; d[e]=d.get(e,0)+c1*c2
    return out
Phi=flint.fmpz_poly.cyclotomic(L) if hasattr(flint.fmpz_poly,'cyclotomic') else None
def iszero(d):
    coeffs=[0]*L
    for e,c in d.items(): coeffs[e]+=c
    P=flint.fmpz_poly(coeffs)
    return (P % Phi)==0
def check(Mleft,Mright):
    keys=set(Mleft)|set(Mright); bad=0
    for kk in keys:
        d=dict(Mleft.get(kk,{}))
        for e,c in Mright.get(kk,{}).items(): d[e]=d.get(e,0)-c
        if any(d.values()) and not iszero(d): bad+=1
    return bad,len(keys)
rowsz=sorted(set(wsize[r] for (r,c) in Y)); assert len(rowsz)==1, rowsz
res={'orbit_sizes':sizes,'support_row_sizes':rowsz,'nonzero_entries':len(Y)}
res['S: Y*S35 - S7*Y nonzero entries']=check(mul(Y,S35),mul(S7,Y))
res['T: Y*T35 - T7*Y nonzero entries']=check(mul(Y,T35),mul(T7,Y))
res['Y_exponents_mod_L']={f"{r},{c}":list(v)[0] for (r,c),v in Y.items()}
res['support_labels']=sorted(set(c for (r,c) in Y)); res['zero_labels']=[a for a in range(n) if a not in res['support_labels']]
res['q_of_labels']=[str(x) for x in q]; res['reps_mu_times_minus35']=[list(map(int,r)) for r in reps]
print({k:v for k,v in res.items() if 'expo' not in k and 'q_of' not in k and 'reps' not in k}); json.dump(res,open('exact_verify.json','w'),indent=1)
