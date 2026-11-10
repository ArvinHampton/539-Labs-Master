import sys; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
import mpmath as mp
from fractions import Fraction as Fr
from symbols import FAM, sym_pair, S_rows, L as LL
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
def Mmat():
    M=mp.matrix(105,105)
    for j,d in enumerate(S_rows()):
        for kk,es in d.items():
            for e in es: M[j,kk]+=mp.expjpi(mp.mpf(2*e)/LL)
    return M
fm=lambda r: mp.mpf(r.numerator)/r.denominator
_E={}
def ef(r):
    r=Fr(r)%1
    if r not in _E: _E[r]=mp.expjpi(2*fm(r))
    return _E[r]
T4=[mp.mpc(0.1,0.95),mp.mpc(-0.2,1.05),mp.mpc(0.3,0.9),mp.mpc(-0.05,1.15)]
HO=[mp.mpc(0.15,1.0),mp.mpc(-0.25,0.92)]
def tables(Amat,al,be,Qcut,B=12,cone=None):
    """dict Q -> summed phase, for nu in alpha+Z^2 with Q=1/2 nu^T A nu <= Qcut (and weight from cone)"""
    (a,b),(_,c)=Amat; D={}
    for n in range(-B,B+1):
        for k in range(-B,B+1):
            nu=(al[0]+n,al[1]+k); Q=Fr(a*nu[0]**2+2*b*nu[0]*nu[1]+c*nu[1]**2,2)
            if Q>Qcut: continue
            w=1 if cone is None else cone(nu)
            if not w: continue
            ph=nu[0]*(a*be[0]+b*be[1])+nu[1]*(b*be[0]+c*be[1])
            D[Q]=D.get(Q,0)+w*ef(ph)
    return D
def evalt(D,tau): return sum((v*mp.exp(2j*mp.pi*fm(Q)*tau) for Q,v in D.items()),mp.mpc(0))
