# Item 2(b): action of g=(gamma+I)/(2m) on the complement factor (all labels with zero m-part), joint eigen-dims.
import sys, json, math, cmath, numpy as np
from family_s import Family
from even_exact import red
def mpart(D,m):
    a=1
    for p in set(f for f in range(2,m+1) if m%f==0 and all(f%q for q in range(2,int(f**.5)+1))):
        while D%(a*p)==0: a*=p
    return a
out=[]
for m in map(int,sys.argv[1].split(',')):
    s=2*m*m; F=Family(s); D=F.D; dm=mpart(D,m); dc=D//dm
    ec=(pow(dm,-1,dc)*dm)%D     # ≡1 mod dc, 0 mod dm
    lab=[i for i,(al,be) in enumerate(F.LABELS) if all((ec*np.array(al)-np.array(al))%D==0) and all((ec*np.array(be)-np.array(be))%D==0)]
    li={i:k for k,i in enumerate(lab)}; n=len(lab)
    minv=pow(m,-1,dc)
    def lift(Mc):  # integer matrix ≡ Mc mod dc, ≡ I mod dm
        return np.array([[ (Mc[i][j]*ec + (1 if i==j else 0)*(1-ec))%D for j in range(2)] for i in range(2)],dtype=object)
    G=lift([[0,-m],[minv,2*m]]); Gm=lift([[-1,-s],[2,2*s-1]]); Nm=lift([[-1,0],[0,-1]])
    def mat(A):
        X=np.zeros((n,n),complex)
        for i in lab:
            al,be=F.LABELS[i]; al=np.array(al,dtype=object); be=np.array(be,dtype=object)
            a2=np.array([int(v) for v in (A.dot(al))%D]); 
            # beta is in Q^2 with denominator D: apply A
            b2=np.array([int(v) for v in A.dot(be)])
            j,ph=red(F,a2,b2); assert j in li
            X[li[j],li[i]]=cmath.exp(2j*math.pi*float(ph))
        return X
    Xg,Xga,Xn=mat(G),mat(Gm),mat(Nm)
    def jd(pairs):
        A=np.vstack([M-l*np.eye(n) for M,l in pairs]); return n-np.linalg.matrix_rank(A,tol=1e-7)
    r={"m":m,"s":s,"|complement labels|":n,"g^2=gamma":bool(np.allclose(Xg@Xg,Xga)),
       "Fix(N,gamma)":jd([(Xn,1),(Xga,1)]),"N=1,g=+1":jd([(Xn,1),(Xg,1)]),"N=1,g=-1":jd([(Xn,1),(Xg,-1)]),
       "N=-1,g=+1":jd([(Xn,-1),(Xg,1)]),"N=-1,g=-1":jd([(Xn,-1),(Xg,-1)]),"m(m-1)":m*(m-1),"m(m+1)":m*(m+1)}
    print(json.dumps(r,default=int),flush=True); out.append(r)
json.dump(out,open("gap_g.json","w"),indent=1,default=int)
