import sys, math, numpy as np; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order6/scripts')
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from lib6 import weight as w6, grid
from symbols import FAM, sym_pair, S_rows, L as LL, reduce
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
M=np.zeros((105,105),complex)
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for e in es: M[j,kk]+=np.exp(2j*np.pi*e/LL)
neg=lambda v:(-v[0],-v[1])
P=np.zeros((105,105),complex)
for j,(al,be) in enumerate(pairs):
    k,e=reduce(neg(al),neg(be)); P[j,k]=np.exp(2j*np.pi*e/LL)
def taus(N,seed):
    rng=np.random.default_rng(seed); T=[]
    while len(T)<N:
        t=complex(rng.uniform(-0.45,0.45),rng.uniform(0.55,1.3))
        if 0.8<=abs(t)<=1.25: T.append(t)
    return T
GAM=np.array([[-1,-7],[2,13]]); A=np.array([[2,7],[7,7]])
c1=np.array([-1.,1.]); gc1=GAM@c1
Bf=lambda u,v: u@A@v
def arc_nodes(nn=24):
    x,wq=np.polynomial.legendre.leggauss(nn); s=(x+1)/2; wq=wq/2
    zh=lambda s: ((1-s)*c1+s*gc1)/math.sqrt(-0.5*Bf((1-s)*c1+s*gc1,(1-s)*c1+s*gc1))
    z0=zh(0.0); mu=lambda s: math.acosh(max(1.0,-Bf(z0,zh(s))/2))
    h=1e-6; out=[]
    for si,wi in zip(s,wq):
        dmu=(mu(min(1,si+h))-mu(max(0,si-h)))/(min(1,si+h)-max(0,si-h))
        out.append((zh(si),wi*dmu,mu(si)))
    return out, mu(1.0)
def weight(kind,n1,n2,y,expo,z=None):
    if kind=='G':
        return np.exp(-np.pi*y*(10*n1*n1+35*n2*n2)+expo)
    if kind=='ThE':
        p=0.5*(1+np.sign(n1)*np.sign(n2)); return p*np.exp(np.where(p!=0,expo,0))
    if kind=='siegel':
        Bz=n1*(A[0]@z)+n2*(A[1]@z); Qz=Bz*Bz/(4*(0.5*Bf(z,z)))
        Q=-expo/(2*np.pi*y)
        return math.sqrt(y)*np.exp(-2*np.pi*y*(Q-2*Qz))
    return w6(kind,n1,n2,y,expo)
def series(al,be,tau,kind,Lb=40,z=None):
    y=tau.imag; n,k=np.meshgrid(np.arange(-Lb,Lb+1),np.arange(-Lb,Lb+1),indexing='ij')
    n1,n2=grid(al,n,k); Q=n1*n1+7*n1*n2+3.5*n2*n2
    b0,b1=float(be[0]),float(be[1]); Bb=n1*(2*b0+7*b1)+n2*(7*b0+7*b1)
    w=weight(kind,n1,n2,y,-2*np.pi*Q*y,z); assert np.isfinite(w).all()
    return (w*np.exp(2j*np.pi*(Q*tau.real+Bb))).sum()
