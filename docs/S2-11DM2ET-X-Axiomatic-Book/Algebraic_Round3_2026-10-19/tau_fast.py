# Fast integer re-implementation of tau.py (original D=M#/M definition) for k=5,6; ranks mod primes.
import sys, json, numpy as np, sympy as sp, flint
sys.path.insert(0,'../2026-10-18-Open-Algebraic')
from hcount import lat
def run(k,primes=(1000003,998244353)):
    m=2*k*k-1; s=2*m*m; r=2*k
    A=sp.Matrix([[2,s],[s,s]]); G=sp.Matrix([[-1,-s],[2,2*s-1]]); g=(G+sp.eye(2))/(2*m); h=(g+sp.eye(2))/r
    Mt=lat([sp.Matrix([1,0]),sp.Matrix([0,1]),sp.Matrix([0,sp.Rational(1,m)])])
    M=lat([Mt[:,0],Mt[:,1],(h*Mt)[:,0],(h*Mt)[:,1]]); M=lat([(((lat([((Mt.T).inv())[:,0],((Mt.T).inv())[:,1],(((h*Mt).T).inv())[:,0],(((h*Mt).T).inv())[:,1]])).T).inv())[:,j] for j in range(2)])
    assert all(((M.inv()*h*M)[i]).q==1 for i in range(4))
    GM=M.T*A*M; L=int(abs(GM.det())); Gi=(GM.inv()*L).applyfunc(int)
    # M# = M GM^{-1} Z^2 ; elements: c = Gi z mod L
    from sympy.matrices.normalforms import smith_normal_decomp
    Sd,U,V=smith_normal_decomp(sp.Matrix(GM.applyfunc(int)))
    d1,d2=abs(int(Sd[0,0])),abs(int(Sd[1,1])); assert d1*d2==L
    B=(Gi*U.inv()).applyfunc(lambda z:int(z)%L)
    w1=np.repeat(np.arange(d1,dtype=np.int64),d2); w2=np.tile(np.arange(d2,dtype=np.int64),d1)
    xx=(int(B[0,0])*w1+int(B[0,1])*w2)%L; yy=(int(B[1,0])*w1+int(B[1,1])*w2)%L
    codes=np.unique(xx*L+yy); assert len(codes)==L
    x=codes//L; y=codes%L
    Hm=(M.inv()*h.inv()*M).applyfunc(int); Gm=(M.inv()*g*M).applyfunc(int)
    Pm=(M.T*A*Mt).applyfunc(int)
    old=((x*int(Pm[0,0])+y*int(Pm[1,0]))%L==0)&((x*int(Pm[0,1])+y*int(Pm[1,1]))%L==0)
    W=Mt.inv()*M; den=int(sp.ilcm(*[sp.Rational(w).q for w in W])); Wi=(W*den).applyfunc(int); Q=L*den
    def key(x,y): return (((int(Wi[0,0])*x+int(Wi[0,1])*y)%Q)*Q+((int(Wi[1,0])*x+int(Wi[1,1])*y)%Q))
    def ap(T,x,y): return ((int(T[0,0])*x+int(T[0,1])*y)%L,(int(T[1,0])*x+int(T[1,1])*y)%L)
    xo,yo=x[old],y[old]; ko=key(xo,yo); C,inv=np.unique(ko,return_inverse=True); n=len(C); cs=len(xo)//n
    # g,-1 action on classes
    gx,gy=ap(Gm,xo,yo); gi=np.searchsorted(C,key(gx,gy)); ni=np.searchsorted(C,key((-xo)%L,(-yo)%L))
    gmap=np.empty(n,int);gmap[inv]=gi; nmap=np.empty(n,int); nmap[inv]=ni
    par=np.arange(n)
    def f(i):
        while par[i]!=i: par[i]=par[par[i]]; i=par[i]
        return i
    for i in range(n):
        for j in (gmap[i],nmap[i]):
            a_,b_=f(i),f(j)
            if a_!=b_: par[a_]=b_
    roots=np.array([f(i) for i in range(n)]); R,lab=np.unique(roots,return_inverse=True); no=len(R)
    hx,hy=ap(Hm,xo,yo)
    Pmold=((hx*int(Pm[0,0])+hy*int(Pm[1,0]))%L==0)&((hx*int(Pm[0,1])+hy*int(Pm[1,1]))%L==0)
    src=lab[inv[Pmold]]; dst=lab[np.searchsorted(C,key(hx[Pmold],hy[Pmold]))]
    T=np.zeros((no,no),np.int64); np.add.at(T,(src,dst),1)
    osz=np.bincount(lab,minlength=no)*cs
    # tau = T/osz (row-scaled). I+tau ~ diag(osz)+T (row scaling preserves rank)
    res=dict(k=k,m=m,D=L,n_classes=n,class_size=cs,V0=no,expected_V0=m*(m+1))
    for p in primes:
        Mp=flint.nmod_mat([[int(v) for v in row] for row in (np.diag(osz)+T)],p)
        Tp=flint.nmod_mat([[int(v) for v in row] for row in T],p)
        res[f'rank_I_plus_tau_mod{p}']=Mp.rank(); res[f'rank_tau_mod{p}']=Tp.rank()
    res['trace_tau']=float(sum(T[i,i]/osz[i] for i in range(no)))
    res['expected_extra']=k*(k-1); res['extra_mod_first_prime']=no-res[f'rank_I_plus_tau_mod{primes[0]}']
    return res
if __name__=="__main__":
    for k in map(int,sys.argv[1].split(',')):
        o=run(k); print(json.dumps(o),flush=True); json.dump(o,open(f"tau_fast_{k}.json","w"),indent=1)
