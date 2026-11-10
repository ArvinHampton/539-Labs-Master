# copied from order22 (functions only): RG9 (gamma transport of corner), RG9b (subdivision), C1, C2. PREREG sha f7ca8083...
import sys, math, json, numpy as np
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import XS, phase_ints, Fr
from symbols import FAM, sym_pair, reduce, L
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
A=np.array([[2,7],[7,7]]); g=np.array([[-1,-7],[2,13]]); assert (g.T@A@g==A).all()
gi=np.array([[13,7],[-2,-1]]); assert (g@gi==np.eye(2,dtype=int)).all()
def period(al,be,x,u):
    N=2*Fr(x).denominator
    for mult in (1,2,5,7,10,14,35,70):
        P=N*mult; j=np.arange(P); pts=j[:,None]*np.array(u)[None,:]
        k1,_=phase_ints(al,be,x,pts); k2,_=phase_ints(al,be,x,pts+P*np.array(u))
        if (k1==k2).all(): return P
def Bi(u,v): return int(np.array(u)@A@np.array(v))
def fracs(num,den):  # arrays of integer numerators over common den -> {.} as float, exact zero
    r=np.mod(num,den); return r/den, r==0
def corner(al,be,x,u1,u2):
    N=math.lcm(period(al,be,x,(1,0)),period(al,be,x,(0,1)))
    i=np.arange(N); V=np.stack(np.meshgrid(i,i,indexing='ij'),-1).reshape(-1,2)
    k0,Mm=phase_ints(al,be,x,V); f=np.exp(2j*np.pi*k0/Mm)
    U=np.array([u1,u2]).T; det=round(np.linalg.det(U)); assert abs(det)==1
    Ui=np.round(np.linalg.inv(U)).astype(np.int64)
    q=math.lcm(Fr(al[0]).denominator,Fr(al[1]).denominator)
    an=np.array([int(Fr(al[0])*q),int(Fr(al[1])*q)])
    W=(an[None,:]+q*V)@Ui.T          # q*(a,b) integer numerators
    out=[]
    for c in range(2):
        fr,z=fracs(W[:,c],q*N); b1=np.where(z,0.0,fr-0.5); b2=fr*fr-fr+1/6; out.append((b1,b2))
    Bu=Bi(u1,u2); Q1=Bi(u1,u1)/2; Q2=Bi(u2,u2)/2
    w=out[0][0]*out[1][0]+Bu/(4*Q2)*out[0][1]+Bu/(4*Q1)*out[1][1]
    return np.sum(f*w)
