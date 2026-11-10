# order5: mpmath (dps 30) re-implementation of the order3c A0/A1/A2 formula (read-only import of lib2 geometry).
import sys; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import PIECES, WALLS, piece_data, wall_data, Bi, Qi, Fr
import numpy as np, mpmath as mp
mp.mp.dps=30
_K={}
def consts(p,q,r):
    key=(p,q,r)
    if key not in _K:
        P,Qq,R=mp.mpf(p.numerator)/p.denominator,mp.mpf(q.numerator)/q.denominator,mp.mpf(r.numerator)/r.denominator
        phi=lambda th: P*mp.cos(th)**2+Qq*mp.cos(th)*mp.sin(th)+R*mp.sin(th)**2
        K11=mp.quad(lambda th: mp.cos(th)**2/(2*phi(th)**2),[0,mp.pi/2])
        K12=mp.quad(lambda th: mp.cos(th)*mp.sin(th)/(2*phi(th)**2),[0,mp.pi/2])
        K22=mp.quad(lambda th: mp.sin(th)**2/(2*phi(th)**2),[0,mp.pi/2])
        Ar=mp.quad(lambda th: 1/(2*phi(th)),[0,mp.pi/2])
        den=4*P*R-Qq*Qq; sp=mp.sqrt(mp.pi)
        Ja=(sp/4)*(2/den)*(2*mp.sqrt(R)-Qq/mp.sqrt(P)); Jb=(sp/4)*(2/den)*(2*mp.sqrt(P)-Qq/mp.sqrt(R))
        _K[key]=(K11,K12,K22,Ar,Ja,Jb,P,Qq,R)
    return _K[key]
class Etab:
    def __init__(s,M): s.M=M; s.c={}
    def get(s,ks):
        out=[]
        for k in ks:
            k=int(k); v=s.c.get(k)
            if v is None: v=mp.expjpi(mp.mpf(2*k)/s.M); s.c[k]=v
            out.append(v)
        return out
_ET={}
def csum(k,M,gs):
    """[sum_z e(k_z/M) g_z for g in gs] exactly-weighted, mp"""
    if M not in _ET: _ET[M]=Etab(M)
    u,inv=np.unique(k,return_inverse=True); E=_ET[M].get(u)
    res=[]
    for g in gs:
        cnt=np.bincount(inv,weights=g.astype(np.float64),minlength=len(u)); assert np.all(np.abs(cnt)<2**52)
        res.append(mp.fdot(E,[int(c) for c in np.rint(cnt)]))
    return res
SQPI=mp.sqrt(mp.pi)
def mpq(fr): fr=Fr(fr); return mp.mpf(fr.numerator)/fr.denominator
def A012mp(al,be,x,pieces=None,walls=None):
    pieces=PIECES if pieces is None else pieces; walls=WALLS if walls is None else walls
    A0=A1=A2=mp.mpc(0)
    for sg,c,U in pieces:
        d=piece_data(al,be,x,c,U); N=d['N']; z1=d['z1'].astype(np.int64); z2=d['z2'].astype(np.int64)
        g1=2*z1-N; g2=2*z2-N
        S=csum(d['k'],d['M'],[np.ones_like(z1),g1,g2,6*z1*z1-6*N*z1+N*N,6*z2*z2-6*N*z2+N*N,g1*g2])
        N2=mp.mpf(N*N); mf=S[0]/N2; w1=S[1]/(2*N2); w2=S[2]/(2*N2); b2a=S[3]/(6*N2); b2b=S[4]/(6*N2); bb=S[5]/(4*N2)
        K11,K12,K22,Ar,Ja,Jb,P,Qq,R=consts(d['p'],d['q'],d['r'])
        l1,l2=mpq(d['l1']),mpq(d['l2']); ac=(al[0]+c[0],al[1]+c[1]); Q0=mpq(Fr(Bi(ac,ac),2)); s=mpq(sg)
        A0+=s*mf*Ar
        A1+=s*(-mf*(l1*Ja+l2*Jb)-(SQPI/2)*(w1/mp.sqrt(R)+w2/mp.sqrt(P)))
        A2+=s*(mf*(mp.mpf(1)/2*(l1*l1*K11+2*l1*l2*K12+l2*l2*K22)-Q0*Ar)+w1*l2/(2*R)+w2*l1/(2*P)+(Qq/4)*(b2a/R+b2b/P)+bb)
    for sg,c,u in walls:
        d=wall_data(al,be,x,c,u); N=d['N']; b=np.arange(N,dtype=np.int64)
        S=csum(d['k'],d['M'],[np.ones_like(b),2*b-N]); ac=(al[0]+c[0],al[1]+c[1]); Qu=mpq(d['Qu']); s=mpq(sg)
        mean=S[0]/N; sb1=S[1]/(2*N)
        A1+=s*(SQPI/2)*mean/mp.sqrt(Qu)
        A2+=s*(-mean*mpq(Bi(u,ac))/(2*Qu)-sb1)
    return A0,A1,A2
