# Hecke-correspondence reformulation of rank_h (exact). See report §1.
import sys, json, math, sympy as sp, flint
sys.path.insert(0,'../2026-10-18-Open-Algebraic')
from hcount import lat, inlat
def run(k):
    m=2*k*k-1; s=2*m*m; r=2*k
    A=sp.Matrix([[2,s],[s,s]]); G=sp.Matrix([[-1,-s],[2,2*s-1]]); g=(G+sp.eye(2))/(2*m); h=(g+sp.eye(2))/r
    assert h*h==g and h.T*A*h==A and g*g==G
    t0=sp.Matrix([0,sp.Rational(1,m)])
    Mt=lat([sp.Matrix([1,0]),sp.Matrix([0,1]),t0])
    D_=lat([(((h**i*Mt).T).inv())[:,j] for i in range(4) for j in range(2)])
    M=lat([((D_.T).inv())[:,j] for j in range(2)])
    GM=M.T*A*M; L=int(abs(GM.det()))
    Ginv=(GM.inv()*L).applyfunc(int)
    c1=[int(x) for x in Ginv[:,0]]; c2=[int(x) for x in Ginv[:,1]]
    els=set()
    for a in range(L):
        x=((a*c1[0])%L,(a*c1[1])%L)
        if a>0 and x==(0,0): break
        for b in range(L):
            y=((x[0]+b*c2[0])%L,(x[1]+b*c2[1])%L)
            if b>0 and y==x: break
            els.add(y)
    assert len(els)==L
    mat=lambda Y:(M.inv()*Y*M).applyfunc(int)
    H=mat(h); Hi=mat(h.inv()); Gg=mat(g)
    ap=lambda T,y:((int(T[0,0])*y[0]+int(T[0,1])*y[1])%L,(int(T[1,0])*y[0]+int(T[1,1])*y[1])%L)
    Pm=M.T*A*Mt; W=Mt.inv()*M
    P00,P10,P01,P11=[int(Pm[i,j]) for i,j in((0,0),(1,0),(0,1),(1,1))]
    inMts=lambda y:(y[0]*P00+y[1]*P10)%L==0 and (y[0]*P01+y[1]*P11)%L==0
    key=lambda y:tuple(sp.Rational(W[i,0]*y[0]+W[i,1]*y[1],L)%1 for i in range(2))
    old=[y for y in els if inMts(y)]; ek={y:key(y) for y in old}
    C=sorted(set(ek.values())); ci={c:i for i,c in enumerate(C)}; n=len(C)
    csize=len(old)//n
    # <g,-1> orbits on C
    rep={}
    for y in old: rep.setdefault(ek[y],y)
    lab={};no=0
    for c in C:
        if c in lab: continue
        st=[c];lab[c]=no
        while st:
            a=st.pop(); y=rep[a]
            for z in (ap(Gg,y),((-y[0])%L,(-y[1])%L)):
                b=ek[z]
                if b not in lab: lab[b]=no; st.append(b)
        no+=1
    # T_{c,c'} = #{y in c : h^{-1} y in M_t# , class c'} ; tau = T/csize, then on orbit basis
    T=[[0]*no for _ in range(no)]
    for y in old:
        z=ap(Hi,y)
        if inMts(z): T[lab[ek[y]]][lab[ek[z]]]+=1
    osz=[0]*no
    for c in C: osz[lab[c]]+=1
    # operator on V0 (orbit-indicator basis): (tau f)(O) = sum_{O'} T[O][O']/(|O| csize) f(O')
    Tq=sp.Matrix(no,no,lambda i,j:sp.Rational(T[i][j],osz[i]*csize))
    I=sp.eye(no)
    res=dict(k=k,m=m,n_classes=n,class_size=csize,V0=no,rank_I_plus_tau=(I+Tq).rank(),rank_I_minus_tau=(I-Tq).rank(),
             trace_tau=str(Tq.trace()))
    # minimal polynomial search deg<=3
    P=[I,Tq,Tq*Tq,Tq*Tq*Tq]
    for d in (1,2,3):
        Mx=sp.Matrix([list(Pi) for Pi in P[:d+1]]).T
        ns=Mx.nullspace()
        if ns: res['minpoly_coeffs_low_to_high']=[str(x) for x in (ns[0]/ns[0][-1])]; break
    res['charpoly_factored']=str(sp.factor(Tq.charpoly().as_expr()))
    return res
if __name__=="__main__":
    out=[run(int(k)) for k in sys.argv[1].split(',')]
    for o in out: print(json.dumps(o))
    json.dump(out,open(f"tau_{sys.argv[1].replace(',','_')}.json","w"),indent=1)
