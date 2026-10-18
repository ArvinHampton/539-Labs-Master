# Radial expansion coefficients of every f-component at rational x (exact integer phases, EM per class mod 4m):
#   f_{al,be}(e(x) e^{-t}) = s(x)/t + h(x)/sqrt(t) + kappa(x) + O(t)
#   f_{al,be} = (1/k) sum_{i<k} [E^F_{g^-i(al,be)} + E^F_{-g^-i(al,be)}],  F = C0 u rho2C0.
import numpy as np, math
from fractions import Fraction as Fr
from family import D, GI, LABELS
from uvec import K
SP=math.sqrt(math.pi)
def Icone(A11,A12,A22):
    # (1/2) int_0^inf dmu/(A11+2A12 mu+A22 mu^2)
    d=math.sqrt(A12*A12-A11*A22) if A12*A12>A11*A22 else None
    import mpmath as mp
    return float(mp.quad(lambda m: 1/(A11+2*A12*m+A22*m*m),[0,1,mp.inf]))/2
IC=[Icone(1,3.5,3.5),Icone(3.5,3.5,1)]
def EF(al70,be70,x):
    x=Fr(x); h,m=x.numerator,x.denominator; L=4*m
    i=np.arange(L,dtype=np.int64)[:,None]; j=np.arange(L,dtype=np.int64)[None,:]
    s=0j; hh=0j; c=0j
    for which in (0,1):
        if which==0:
            u0=al70[0]%D or D; w0=al70[1]%D
            A11,A12,A22=1.0,3.5,3.5
        else:
            u0=(al70[1]+2*al70[0])%D or D; w0=(-al70[0])%D
            A11,A12,A22=3.5,3.5,1.0
        U=np.broadcast_to(u0+D*i,(L,L)).astype(np.int64); W=np.broadcast_to(w0+D*j,(L,L)).astype(np.int64)
        if which==0: N1,N2=U,W
        else: N1,N2=-W,U+2*W
        q=2*N1*N1+14*N1*N2+7*N2*N2                       # 9800*Q
        bb=N1*(2*be70[0]+7*be70[1])+N2*(7*be70[0]+7*be70[1])   # 4900*B
        den=9800*m
        P=(h*q+2*m*bb)%den
        ph=np.exp(2j*np.pi*P/den)
        su=U/(D*L); sw=W/(D*L)
        s+=IC[which]*ph.sum()/L**2
        hh+=np.sum(ph*(-(sw-0.5)*SP/(2*math.sqrt(A11))-(su-0.5)*SP/(2*math.sqrt(A22))))/L
        c+=np.sum(ph*((sw*sw-sw+1/6)*A12/(2*A11)+(su*su-su+1/6)*A12/(2*A22)+(su-0.5)*(sw-0.5)))
    return np.array([s,hh,c])
def fcoef(lab,x):
    al,be=np.array(lab[0]),np.array(lab[1]); tot=np.zeros(3,complex)
    for _ in range(K):
        tot+=EF(al,be,x)+EF(-al,-be,x)
        al=GI@al; be=GI@be
    return tot/K
def allcoef(x):
    return np.array([fcoef(l,x) for l in LABELS])     # (140,3)
