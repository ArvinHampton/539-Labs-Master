# order6: completed weights (overflow-safe) for H-hat, odd orthant pair, even product candidate
import sys, math, numpy as np; sys.dont_write_bytecode=True
from scipy.special import erfc, erfcx
SQ=math.sqrt(math.pi)
def _parts(z):  # z = sqrt(pi)*a : sign, |E| = 1 - ec, ec = erfcx(|z|)*exp(-z^2) (returned as (erfcx, -z^2))
    return np.sign(z), erfcx(np.abs(z)), -z*z
def odd_w(a,b,expo):
    """(E(a)+E(b))*exp(expo)"""
    sa,xa,la=_parts(SQ*a); sb,xb,lb=_parts(SQ*b); opp=(sa==-sb)&(sa!=0)
    with np.errstate(over='ignore',invalid='ignore'):
        same=(sa*(1-xa*np.exp(la))+sb*(1-xb*np.exp(lb)))*np.exp(np.where(opp,0,expo))
        o=sa*(xb*np.exp(np.where(opp,lb+expo,0))-xa*np.exp(np.where(opp,la+expo,0)))
    return np.where(opp,o,same)
def even_w(a,b,expo):
    """(1+E(a)E(b))*exp(expo)"""
    sa,xa,la=_parts(SQ*a); sb,xb,lb=_parts(SQ*b); opp=(sa==-sb)&(sa!=0)
    with np.errstate(over='ignore',invalid='ignore'):
        Ea=sa*(1-xa*np.exp(la)); Eb=sb*(1-xb*np.exp(lb))
        same=(1+Ea*Eb)*np.exp(np.where(opp,0,expo))
        o=xa*np.exp(np.where(opp,la+expo,0))+xb*np.exp(np.where(opp,lb+expo,0))-xa*xb*np.exp(np.where(opp,la+lb+expo,0))
    return np.where(opp,o,same)
def grid(al,n,k): return float(al[0])+n, float(al[1])+k
def weight(kind,n1,n2,y,expo):
    sy=math.sqrt(y)
    a1=math.sqrt(10)*n1*sy; a2=math.sqrt(35)*n2*sy; a3=(n1+21*n2)*math.sqrt(2/17)*sy
    if kind=='H': return 0.5*odd_w(a1,a3,expo)
    if kind=='O': return 0.5*odd_w(a1,a2,expo)
    if kind=='E': return 0.5*even_w(a1,a2,expo)
    if kind=='orth': return 0.5*weight('E',n1,n2,y,expo)+0.5*weight('O',n1,n2,y,expo)
    if kind=='full': return 0.5*weight('E',n1,n2,y,expo)+0.5*weight('O',n1,n2,y,expo)-weight('H',n1,n2,y,expo)
    s1,s2,s3=np.sign(n1),np.sign(n2),np.sign(n1+21*n2)
    if kind=='Hhol': p=0.5*(s1+s3)
    if kind=='fullhol': p=0.25*(1+s1)*(1+s2)-0.5*(s1+s3)
    return p*np.exp(np.where(p!=0,expo,0))
def series(al,be,tau,kind,Lb=40):
    y=tau.imag; n,k=np.meshgrid(np.arange(-Lb,Lb+1),np.arange(-Lb,Lb+1),indexing='ij')
    n1,n2=grid(al,n,k); Q=n1*n1+7*n1*n2+3.5*n2*n2
    b0,b1=float(be[0]),float(be[1]); Bb=n1*(2*b0+7*b1)+n2*(7*b0+7*b1)
    w=weight(kind,n1,n2,y,-2*np.pi*Q*y); assert np.isfinite(w).all()
    return (w*np.exp(2j*np.pi*(Q*tau.real+Bb))).sum()
