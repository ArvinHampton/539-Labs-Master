# order17: K1 gate (Cor. R1 + line terms + P), C0 control, T1/T2 fixed-M laws. See PREREG.md (sha d3938e1c...).
import sys, json, math, numpy as np
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import XS, phase_ints, Fr
from symbols import FAM, sym_pair, S_rows, reduce, L
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
SQ=math.sqrt(math.pi)
def sg(r): return (r>0)-(r<0)
def B1b(u):
    u=Fr(u)%1; return 0.0 if u==0 else float(u)-0.5
def ph(al,be,x,pts):
    k,M=phase_ints(al,be,x,pts); return np.exp(2j*np.pi*k/M)
def period(al,be,x,base,u):
    N=2*Fr(x).denominator
    for mult in (1,2,5,7,10,14,35,70):
        P=N*mult; j=np.arange(P); pts=base[None,:]+j[:,None]*np.array(u)[None,:]
        k1,_=phase_ints(al,be,x,pts); k2,_=phase_ints(al,be,x,pts+P*np.array(u))
        if (k1==k2).all(): return P
    raise RuntimeError('period')
WALLS=[(-0.25,(0,1),(1,0),Fr(7,2),lambda al:al[0]),     # c1: a=nu1
       ( 0.25,(1,0),(0,1),Fr(1),  lambda al:al[1]),     # c': a=nu2
       (-0.5,(21,-1),(1,0),Fr(595,2),lambda al:al[0]+21*al[1])]  # c2: a=nu1+21nu2
def pred_odd(al,be,x):
    tot=0j
    for kap,d,e,Qd,aa in WALLS:
        d=np.array(d); e=np.array(e)
        N=max(period(al,be,x,np.zeros(2,int),tuple(d)),period(al,be,x,np.zeros(2,int),tuple(e)))
        i=np.arange(N); j=np.arange(N)
        pts=i[:,None,None]*e[None,None,:]+j[None,:,None]*d[None,None,:]
        f=ph(al,be,x,pts.reshape(-1,2)).reshape(N,N); phi=f.mean(1)
        a0=Fr(aa(al)); b=np.array([B1b((a0+int(ii))/N) for ii in i])
        tot+= -2*kap*math.sqrt(math.pi/float(Qd))*np.sum(phi*b)
    return tot
def lines(al,be,x):
    a1,a2=Fr(al[0]),Fr(al[1]); sig=a1+21*a2; tot=0j; R=range(-40,41)
    h1=lambda n:(1 if n>=0 else 0)-0.5*(1+sg(n+a1)); h2=lambda k:(1 if k>=0 else 0)-0.5*(1+sg(k+a2))
    g1=lambda n:sg(n)-sg(n+a1); g3=lambda m:sg(m)-sg(m+sig)
    def mean(base,u):
        P=period(al,be,x,np.array(base),u); j=np.arange(P)
        return ph(al,be,x,np.array(base)[None,:]+j[:,None]*np.array(u)[None,:]).mean()
    for k in R:
        if h2(k): tot+=(SQ/2)*mean((0,k),(1,0))*h2(k)
    for n in R:
        w=h1(n)-g1(n)
        if w: tot+=(SQ/2)/math.sqrt(3.5)*mean((n,0),(0,1))*w
    for m in R:
        if g3(m): tot+=(SQ/2)/math.sqrt(297.5)*mean((m,0),(21,-1))*(-g3(m))
    return tot
P=np.zeros((105,105),complex)
for j,(al,be) in enumerate(pairs):
    k,e=reduce((-al[0],-al[1]),(-be[0],-be[1])); P[j,k]=np.exp(2j*np.pi*e/L)
M=np.zeros((105,105),complex)
for j,dct in enumerate(S_rows()):
    for k,es in dct.items():
        for e in es: M[j,k]+=np.exp(2j*np.pi*e/L)
D=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order3/data/parts.npz')
out={}
LN=np.zeros((216,105),complex); PO=np.zeros((216,105),complex); SLN=LN.copy(); SPO=PO.copy()
for ix,x in enumerate(XS):
    for j,(al,be) in enumerate(pairs):
        LN[ix,j]=lines(al,be,x); PO[ix,j]=pred_odd(al,be,x)
        SLN[ix,j]=lines(al,be,-1/x); SPO[ix,j]=pred_odd(al,be,-1/x)
    if ix%20==0: print('pt',ix,x,flush=True)
np.savez('../data/k1t1_arrays.npz',LN=LN,PO=PO,SLN=SLN,SPO=SPO)
odd=lambda A: 0.5*(A-A@P.T); even=lambda A: 0.5*(A+A@P.T)
def k1(A1,LNx,POx):
    e=0
    for r in range(216):
        num=np.linalg.norm(odd((A1-LNx)[r:r+1])-POx[r]); den=max(np.linalg.norm(odd(A1[r:r+1])),1e-3); e=max(e,num/den)
    return e
eK1=max(k1(D['A1'],LN,PO),k1(D['S_A1'],SLN,SPO))
out['K1']=dict(e=eK1,verdict='PASS' if eK1<=1e-9 else ('FAIL' if eK1>1e-6 else 'inconclusive'))
xs=np.array([float(x) for x in XS])
r0=np.linalg.norm(D['S_A0']-(1/(xs*math.sqrt(35)))[:,None]*(D['A0']@M.T))/np.linalg.norm(D['S_A0'])
out['C0']=dict(r0=r0,verdict='PASS' if r0<=1e-10 else 'VOID')
print(out,flush=True)
A1c=D['A1']-LN-PO; SA1c=D['S_A1']-SLN-SPO
def law(A,S,w):
    Y=(xs**-w)[:,None]*(A@M.T)/math.sqrt(35); den=np.vdot(Y,Y)
    if abs(den)<1e-300: return dict(r=None,note='zero')
    k=np.vdot(Y,S)/den; r=np.linalg.norm(S-k*Y)/max(np.linalg.norm(S),1e-300)
    return dict(r=float(r),kappa=[k.real,k.imag],normS=float(np.linalg.norm(S)),verdict='PASS' if r<=1e-8 else ('FAIL' if r>=1e-3 else 'inconclusive'))
for name,f in (('full',lambda A:A),('even',even),('odd',odd)):
    for w in (0.5,0.0,1.0):
        out[f'T_{name}_w{w}']=law(f(A1c),f(SA1c),w); print(name,w,out[f'T_{name}_w{w}'],flush=True)
out['norm_odd_A1c']=float(np.linalg.norm(odd(A1c))); out['norm_even_A1c']=float(np.linalg.norm(even(A1c)))
json.dump(out,open('../data/k1t1.json','w'),indent=1,default=float)
print('done',flush=True)
