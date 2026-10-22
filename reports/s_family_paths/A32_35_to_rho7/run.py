from exact_hom import *
import time
def order(T,p):
    n=len(T); I=np.eye(n,dtype=object); P=T.copy(); k=1
    while not (P==I).all(): P=mm(P,T,p); k+=1
    return k
def tspec2(T,p,z):
    o=order(T,p); assert L%o==0; n=len(T); out={}
    for k in range(0,L,L//o):
        lam=zpow(z,p,k)
        M=flint.nmod_mat(n,n,[int((T[i][j]-(lam if i==j else 0))%p) for i in range(n) for j in range(n)],p)
        d=n-M.rank()
        if d: out[str(Fr(k,L))]=d
    return o,out
res={}
for k0 in (1,500):
    p=find_p(k0); z=setup(p); R={'p':p}
    F,G7,T7=rho7W(p,z)
    roots=sqrt35(p); ok7=[r for r in roots if rels((G7*pow(r,-1,p))%p,T7,p)]
    R['rho7_sqrt35_consistent_roots']=len(ok7); r=ok7[0]
    S7=(G7*pow(r,-1,p))%p
    G35,T35,q=weil35([[2,7],[7,7]],p,z)
    i4=zpow(z,p,L//4); eps=[e for e in (1,p-1,i4,p-i4) if rels((G35*e*pow(r,-1,p))%p,T35,p)]
    R['eps_consistent']=len(eps); S35=(G35*eps[0]*pow(r,-1,p))%p
    inv=lambda M: np.array([int(e) for e in flint.nmod_mat(len(M),len(M),[int(v) for v in M.ravel()],p).inv().entries()],dtype=object).reshape(M.shape)
    dual=lambda S,T:(inv(S).T%p, inv(T).T%p)   # contragredient
    S7d,T7d=dual(S7,T7); S35d,T35d=dual(S35,T35)
    R['T7_order'],R['T7_spec']=tspec2(T7,p,z); R['T35_order'],R['T35_spec']=tspec2(T35,p,z)
    R['T7dual_spec']=tspec2(T7d,p,z)[1]
    R['End_rho7W']=hom_dim(S7,T7,S7,T7,p); R['End_rho35']=hom_dim(S35,T35,S35,T35,p)
    # character twists chi^k: chi(T)=e(k/12), chi(S)=(-i)^k
    homs={}
    for vn,(Sv,Tv) in {'rho35':(S35,T35),'rho35*':(S35d,T35d)}.items():
        for tn,(St,Tt) in {'rho7W':(S7,T7),'rho7W*':(S7d,T7d)}.items():
            for k in range(12):
                cS=pow((p-i4)%p,k,p); cT=zpow(z,p,k*L//12)
                Sx=(Sv*cS)%p; Tx=(Tv*cT)%p
                a=hom_dim(Sx,Tx,St,Tt,p); b=hom_dim(St,Tt,Sx,Tx,p)
                homs[f"{vn}(x)chi^{k} -> {tn}"]=a; homs[f"{tn} -> {vn}(x)chi^{k}"]=b
    R['homs']=homs; R['max_hom']=max(homs.values())
    res[str(p)]=R; print(p,R['T7_order'],R['T35_order'],R['End_rho7W'],R['End_rho35'],R['max_hom'],flush=True)
json.dump(res,open('results.json','w'),indent=1)
