# Which modulus makes the cone-E_R phase a narrow-ray-class function?  For each nu in the S+ cone [e1,gamma e1) of every coset
# p in L'/Z^2 (beta=-a), ideal (beta_X) = C*B (C supported on m), key=(C, class of B in Cl_m^+); test phase constancy per key.
import cypari2, numpy as np, math, sys, itertools
from family_s import Family
from psi_q import cone_coeffs
pari=cypari2.Pari(); pari.allocatemem(2*10**9)
s=int(sys.argv[1]); Qc=float(sys.argv[2])
CF={7:(35,1),8:(3,4),11:(11,3)}; D0,c=CF[s]; F=Family(s); D=F.D; A=F.A
K=pari(f'bnfinit(x^2-{D0},1)'); w=pari('Mod(x,x^2-%d)'%D0)
pts=[]
g=F.G; r1=np.array([1,0]); r2=g@r1
for p in F.LP:
    B=int(math.sqrt(Qc)*12)+4; n=np.arange(-4*B,4*B+1); N1,N2=np.meshgrid(n,n,indexing='ij')
    X=np.stack([p[0]+D*N1.ravel(),p[1]+D*N2.ravel()],1)
    det=r1[0]*r2[1]-r1[1]*r2[0]; sv=(X[:,0]*r2[1]-X[:,1]*r2[0])*np.sign(det); tv=(r1[0]*X[:,1]-r1[1]*X[:,0])*np.sign(det)
    X=X[(sv>0)&(tv>=0)]; Q=(X[:,0]**2+s*X[:,0]*X[:,1]+(s/2)*X[:,1]**2)/(D*D); X=X[(Q<=Qc)&(Q>0)]
    ph=np.exp(2j*np.pi*((X@A@((-F.a)%D))%(D*D))/(D*D))
    for x,v in zip(X,ph): pts.append((int(x[0]),int(x[1]),v))
print("points",len(pts))
idl=[pari.idealhnf(K,(2*x1+s*x2)+c*x2*w) for x1,x2,_ in pts]
primes={2:pari.idealprimedec(K,2),3:pari.idealprimedec(K,3),11:pari.idealprimedec(K,11),5:pari.idealprimedec(K,5),7:pari.idealprimedec(K,7)}
plist=[(2,0),(3,0)]+([(11,0)] if s==11 else [])+([(5,0),(7,0)] if s==7 else [])
for exps in itertools.product(*[range(0,4) for _ in plist]):
    if s==11 and exps[1]>2: continue
    mod=pari.idealhnf(K,1); Ps=[]
    for (p,i),e in zip(plist,exps):
        P=primes[p][i]; Ps.append(P)
        if e: mod=pari.idealmul(K,mod,pari.idealpow(K,P,e))
    bnr=pari.bnrinit(K,[mod,[1,1]],1); h=int(pari('(b)->b.no')(bnr))
    seen={}; bad=0
    for J,(x1,x2,v) in zip(idl,pts):
        Cp=[];Jp=J
        for P in Ps:
            e=int(pari.idealval(K,J,P)); Cp.append(e)
            if e: Jp=pari.idealdiv(K,Jp,pari.idealpow(K,P,e))
        key=(tuple(Cp),tuple(int(z) for z in pari.bnrisprincipal(bnr,Jp,0)))
        if key in seen and abs(seen[key]-v)>1e-9: bad+=1
        seen.setdefault(key,v)
    print(f"modulus exps {dict(zip([p for p,_ in plist],exps))}: |Cl|={h}, keys {len(seen)}, phase-inconsistent points {bad}",flush=True)
