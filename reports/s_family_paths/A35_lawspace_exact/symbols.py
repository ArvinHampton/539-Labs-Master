# A35: exact symbol calculus for the 35-component law vector components G_{al,be}.
# Symbols: K2_mu=G_{a+mu,0}, K3_mu=G_{mu,a}, K4_mu=G_{mu,0}, (K1_mu=G_{a+mu,a}), mu in D=A^{-1}Z^2/Z^2 (A32 label order).
# Proven rules (see REPORT): G_{al+n,be}=G_{al,be} (n in Z^2); G_{al,be+lam}=e(B(al,lam))G_{al,be} (A lam in Z^2);
#   S: G_{al,be}(-1/x) = (1/(|x| sqrt35)) e(B(al,be)) sum_p G_{be+p,-al}(x);  T: G_{al,be}(x+1)=e(-Q(al)-B(al,hA)) G_{al,be+al+hA}(x).
# Phases are stored as exponents mod L=9800 (value e(k/L)).
import json
from fractions import Fraction as Fr
A=((2,7),(7,7)); L=9800
A32='/workspace/quantum-comp/reports/s_family_paths/A32_35_to_rho7/'
R=[tuple(r) for r in json.load(open(A32+'exact_verify.json'))['reps_mu_times_minus35']]
MU=[(Fr(-r[0],35)%1,Fr(-r[1],35)%1) for r in R]
a=(Fr(7,10),Fr(-1,5)); Z=(Fr(0),Fr(0)); hA=(Fr(1,2),Fr(0))
B=lambda u,v: sum(u[i]*A[i][j]*v[j] for i in range(2) for j in range(2))
Q=lambda u: B(u,u)/2
add=lambda u,v:(u[0]+v[0],u[1]+v[1]); neg=lambda u:(-u[0],-u[1]); sub=lambda u,v:add(u,neg(v))
Av=lambda v:(A[0][0]*v[0]+A[0][1]*v[1],A[1][0]*v[0]+A[1][1]*v[1])
isZ=lambda v: all(Fr(x).denominator==1 for x in v)
inAinv=lambda v: isZ(Av(v))
modZ=lambda v:(v[0]%1,v[1]%1)
FAM=['K2','K3','K4']; FAM1=FAM+['K1']
def sym_pair(f,i):
    mu=MU[i]; return {'K2':(add(a,mu),Z),'K3':(mu,a),'K4':(mu,Z),'K1':(add(a,mu),a)}[f]
def ex(fr):  # Fraction mod 1 -> exponent mod L
    fr=Fr(fr)%1; k=fr*L; assert k.denominator==1, fr; return int(k)
def reduce(al,be,fams=FAM):
    """return (index in fams*35, phase exponent) with G_{al,be} = e(k/L) * symbol"""
    for fi,f in enumerate(fams):
        for i in range(35):
            al2,be2=sym_pair(f,i)
            if modZ(al)==modZ(al2):
                lam=sub(be,be2)
                if inAinv(lam):
                    n=sub(al,al2)   # integral
                    # G_{al,be}=G_{al2,be} (shift) = G_{al2,be2+lam} = e(B(al2,lam)) G_{al2,be2}
                    return fi*35+i, ex(B(al2,lam))
    raise ValueError((al,be))
def S_rows(fams=FAM):   # row j: G_j(-1/x) = (1/(|x|sqrt35)) sum_k e(S[j][k]/L)... as dict k->list of exponents
    rows=[]
    for f in fams:
        for i in range(35):
            al,be=sym_pair(f,i); d={}
            for p in MU:
                k,e=reduce(add(be,p),neg(al),fams); d.setdefault(k,[]).append((e+ex(B(al,be)))%L)
            rows.append(d)
    return rows
def T_rows(fams=FAM):
    rows=[]
    for f in fams:
        for i in range(35):
            al,be=sym_pair(f,i); k,e=reduce(al,add(add(be,al),hA),fams)
            rows.append({k:[(e+ex(-Q(al)-B(al,hA)))%L]})
    return rows
