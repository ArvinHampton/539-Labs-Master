# Numerical 140-component lift u_{al,be}(w) (rev4 normalisation) and its w-derivative.
import sys, math, numpy as np
from fractions import Fraction as Fr
from scipy.special import k0e, k1e
sys.path.insert(0,'../2026-10-18-S-Eigenvalues'); import family as F
LABELS=F.LABELS; N=F.N; D=70
A=np.array([[2.,7.],[7.,7.]]); G=np.array([[-1,-7],[2,13]]); GI=np.array([[13,7],[-2,-1]])
EPS=6+math.sqrt(35); LE=math.log(EPS)
def Q(v): return 0.5*np.einsum('...i,ij,...j->...',v,A,v)
def cross(u,v): return u[0]*v[...,1]-u[1]*v[...,0]
def incone(u1,u2,V):
    s=np.sign(u1[0]*u2[1]-u1[1]*u2[0])
    return (s*cross(u1,V)>=-1e-12)&(s*(V[...,0]*u2[1]-V[...,1]*u2[0])>1e-12)
e1=np.array([1.,0.]); ge1=G@e1; f=np.array([1.,-1.]); gf=G@f
CONES=[(e1,ge1),(-e1,-ge1),(f,gf),(-f,-gf)]
def terms(al70,be70,Qmax,R=60):
    """list of (Q, phase) over nu in (al+Z^2) mod gamma^2, nu!=0, |Q|<=Qmax, incl. factor 1/2."""
    n=np.arange(-R,R+1); NN=np.stack(np.meshgrid(n,n,indexing='ij'),-1).reshape(-1,2)
    be=np.array(be70)/D; out_q=[]; out_p=[]
    for k in (0,1):
        a0=(np.linalg.matrix_power(GI,k)@np.array(al70))/D   # gamma^{-k} al
        V=a0+NN; q=Q(V)
        Gk=np.linalg.matrix_power(G,k)
        for (u1,u2) in CONES:
            m=incone(u1,u2,V)&(np.abs(q)<=Qmax)&(np.abs(q)>1e-12)
            W=(Gk@V[m].T).T
            ph=np.exp(2j*np.pi*(W@A@be))
            out_q.append(q[m]); out_p.append(0.5*ph)
    return np.concatenate(out_q),np.concatenate(out_p)
class U:
    def __init__(self,Qmax):
        self.T=[terms(al,be,Qmax) for (al,be) in LABELS]
        self.b=np.array([LE if (al[0]%D==0 and al[1]%D==0) else 0.0 for (al,be) in LABELS])
    def ev(self,w):
        """returns u(w), u_w(w) (140-vectors)."""
        x,y=w.real,w.imag; u=np.zeros(N,complex); uw=np.zeros(N,complex); sy=math.sqrt(y)
        for i,(q,p) in enumerate(self.T):
            aq=np.abs(q); z=2*np.pi*aq*y; ex=np.exp(-z)
            K0=k0e(z)*ex; K1=k1e(z)*ex; ph=p*np.exp(2j*np.pi*q*x)
            u[i]=sy*(self.b[i]+np.sum(ph*K0))
            ux=sy*np.sum(2j*np.pi*q*ph*K0)
            uy=self.b[i]/(2*sy)+np.sum(ph*(K0/(2*sy)-sy*2*np.pi*aq*K1))
            uw[i]=0.5*(ux-1j*uy)
        return u,uw
