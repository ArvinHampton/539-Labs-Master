# order-2 library: piece decomposition of S_{al,be} and the order-2 (t^{-1/2}) formula. Read-only import of A35 symbols.py.
import sys, numpy as np, math
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from symbols import A, MU, a, FAM, sym_pair, B, Q
from fractions import Fraction as Fr
from math import gcd
XS=sorted({Fr(h,m) for m in range(1,16) for h in range(1,3*m+1) if gcd(h,m)==1}); assert len(XS)==216
u1=(21,-1); u2=(0,1)
def Bi(u,v): return u[0]*(2*v[0]+7*v[1])+u[1]*(7*v[0]+7*v[1])
def Qi(u): return Fr(Bi(u,u),2)
# pieces: (sign, offset c, basis U=(e1,e2)) ; walls: (sign, offset c, direction u) with weight already included in sign
PIECES=[(Fr(1),(0,0),((1,0),(0,1)))]                       # orthant, weight +1 (closed)
for r in range(21):
    PIECES.append((Fr(-1),(r,0),(u1,u2)))                   # -K+ pieces (C = P_orth - H)
    PIECES.append((Fr(1),(-r,0),((-21,1),(0,-1))))          # -(-K-) pieces
WALLS=[(Fr(1,2),(0,0),u2),(Fr(1,2),(0,0),u1),               # H subtracts 1/2 on K+ walls -> C gets +1/2
       (Fr(-1,2),(0,0),(0,-1)),(Fr(-1,2),(0,0),(-21,1))]    # K- walls (weight -1/2 in H) -> C gets -1/2
def phase_ints(al,be,x,pts):
    """pts: integer array (...,2) of v; returns integer phase k mod M=9800*m with value e(k/M) = e(x Q(al+v) + B(al+v,be))"""
    x=Fr(x); h,m=x.numerator,x.denominator; M=9800*m
    a0,a1=int(al[0]*70),int(al[1]*70); assert Fr(a0,70)==al[0] and Fr(a1,70)==al[1]
    b0,b1=int(be[0]*70),int(be[1]*70); assert Fr(b0,70)==be[0] and Fr(b1,70)==be[1]
    V0=a0+70*pts[...,0].astype(np.int64); V1=a1+70*pts[...,1].astype(np.int64)
    Q2=2*V0*V0+14*V0*V1+7*V1*V1; Bn=V0*(2*b0+7*b1)+V1*(7*b0+7*b1)
    return ((h%M)*(Q2%M)+2*m*(Bn%M))%M, M
def piece_data(al,be,x,c,U):
    """exact rational data: dict phase->coef for mean f, for sum f*B1(z1/N)/N, for sum f*B1(z2/N)/N; plus l1,l2,p,q,r"""
    m=Fr(x).denominator; N=2*m
    z1,z2=np.meshgrid(np.arange(N),np.arange(N),indexing='ij')
    pts=np.stack([c[0]+z1*U[0][0]+z2*U[1][0], c[1]+z1*U[0][1]+z2*U[1][1]],-1)
    k,M=phase_ints(al,be,x,pts)
    # periodicity check (exactness requirement): shifting z by N in either direction leaves phases unchanged
    for d in (U[0],U[1]):
        k2,_=phase_ints(al,be,x,pts+N*np.array(d)); assert (k2==k).all(), 'period'
    ac=(al[0]+c[0],al[1]+c[1])
    l1=Fr(Bi(U[0],ac)); l2=Fr(Bi(U[1],ac))
    p=Qi(U[0]); r=Qi(U[1]); q=Fr(Bi(U[0],U[1]))
    return dict(k=k.ravel(),z1=z1.ravel(),z2=z2.ravel(),N=N,M=M,l1=l1,l2=l2,p=p,q=q,r=r)
def wall_data(al,be,x,c,u):
    m=Fr(x).denominator; N=2*m; b=np.arange(N)
    pts=np.stack([c[0]+b*u[0],c[1]+b*u[1]],-1); k,M=phase_ints(al,be,x,pts)
    k2,_=phase_ints(al,be,x,pts+N*np.array(u)); assert (k2==k).all()
    return dict(k=k,N=N,M=M,Qu=Qi(u))
# ---------- float evaluation ----------
SQPI=math.sqrt(math.pi)
def J(p,q,r):
    p,q,r=float(p),float(q),float(r); den=4*p*r-q*q
    return (SQPI/4)*(2/den)*(2*math.sqrt(r)-q/math.sqrt(p)), (SQPI/4)*(2/den)*(2*math.sqrt(p)-q/math.sqrt(r))
def area(p,q,r):
    p,q,r=float(p),float(q),float(r); D=q*q-4*p*r; s=math.sqrt(D); assert q>s
    return math.log((q+s)/(q-s))/(2*s)
def A01_float(al,be,x):
    A0=0j; A1=0j
    for sg,c,U in PIECES:
        d=piece_data(al,be,x,c,U); N=d['N']
        f=np.exp(2j*np.pi*d['k']/d['M'])
        mf=f.mean(); w1=(f*(d['z1']/N-0.5)).sum()/N; w2=(f*(d['z2']/N-0.5)).sum()/N
        Ja,Jb=J(d['p'],d['q'],d['r'])
        A0+=float(sg)*mf*area(d['p'],d['q'],d['r'])
        A1+=float(sg)*(-mf*(float(d['l1'])*Ja+float(d['l2'])*Jb)-(SQPI/2)*(w1/math.sqrt(float(d['r']))+w2/math.sqrt(float(d['p']))))
    for sg,c,u in WALLS:
        d=wall_data(al,be,x,c,u); f=np.exp(2j*np.pi*d['k']/d['M'])
        A1+=float(sg)*(SQPI/2)*f.mean()/math.sqrt(float(d['Qu']))
    return A0,A1
