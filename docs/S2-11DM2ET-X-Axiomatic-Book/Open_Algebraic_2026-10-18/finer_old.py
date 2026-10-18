# (c) Finer sectors at p^2 | s(s-2): old/new split via the isotropic subgroup <t> (order p) of the p-part of Delta.
# Pi f(x) = 1_{t-perp}(x) * (1/p) sum_j f(x + j t) commutes with rho, -1, gamma, Z_q -> acts on orbit functions.
# For each eps-sector and each piece (old = im Pi, new = im (1-Pi)): exact rank of the piece vs rank of its lift.
import sys, json, itertools, numpy as np, flint, sympy
from fractions import Fraction as Fr
from sympy.ntheory.modular import crt
from item1_lead import data
res=[]
for s in map(int,sys.argv[1].split(',')):
    orb,counts,modes,mod,D,Mx,no=data(s,float(sys.argv[2]))
    els=list(orb); reps={}
    for x,o in orb.items(): reps.setdefault(o,x)
    osize=[0]*no
    for x,o in orb.items(): osize[o]+=1
    Qi=lambda x: 2*x[0]*x[0]+2*s*x[0]*x[1]+s*x[1]*x[1]
    fac=sympy.factorint(s*(s-2)); ps=[p for p in fac if p!=2]; M=2*D
    Zs={}
    for p in ps:
        pe=p**sympy.multiplicity(p,M); u=int(crt([pe,M//pe],[pe-1,1])[0])
        Zs[p]=[orb[(u*reps[o][0]%mod[0],u*reps[o][1]%mod[1])] for o in range(no)]
    out={"s":s,"pieces":[]}
    for p in [p for p in ps if fac[p]>=2]:
        # t: order p element in Delta, isotropic
        cand=[x for x in els if x!=(0,0) and (p*x[0])%mod[0]==0 and (p*x[1])%mod[1]==0 and Qi(x)%(2*D*D)==0]
        t=cand[0]
        B=lambda x,y: Fr(Qi(((x[0]+y[0]),(x[1]+y[1])))-Qi(x)-Qi(y),2*D*D)
        add=lambda x,y:((x[0]+y[0])%mod[0],(x[1]+y[1])%mod[1])
        # Pi on orbit functions (scaled by p): (Pi f)(x0) for each orbit rep
        Pi=np.zeros((no,no),dtype=object)
        for o in range(no):
            x0=reps[o]
            if B(x0,t).denominator!=1: continue
            y=x0
            for j in range(p): Pi[o,orb[y]]+=1; y=add(y,t)
        # Pi acts on f (column = orbit values); lift of f = sum_O f_O N_O(q) /|O| *|O| ... use f_O * N_O(q)/|O| with per-element counts
        import math as _m
        Lc=1
        for z_ in osize: Lc=Lc*z_//_m.gcd(Lc,z_)
        Npe=np.array([[Mx[o][j] for j in range(len(Mx[0]))] for o in range(no)],dtype=object)
        qcol=[j for j,qq in enumerate(modes) if qq==-2*s*(s-2)]
        PiF=flint.fmpz_mat([[int(v) for v in row] for row in Pi.tolist()]); pI=flint.fmpz_mat([[p if i==j else 0 for j in range(no)] for i in range(no)])
        NpeF=flint.fmpz_mat([[int(v) for v in row] for row in Npe.tolist()])
        for eps in itertools.product((1,-1),repeat=len(ps)):
            P=np.zeros((no,no),dtype=object)
            for S in itertools.product((0,1),repeat=len(ps)):
                sg=1; img=list(range(no))
                for b,q_,e in zip(S,ps,eps):
                    if b: sg*=e; img=[Zs[q_][i] for i in img]
                for o in range(no): P[img[o],o]+=sg     # (P f) as function: f -> sum eps_S f∘Z_S
            Pf=flint.fmpz_mat([[int(v) for v in row] for row in P.tolist()])
            for nm,Proj in (("old",PiF),):
                Bm=Proj*Pf
                rk=Bm.rank()
                if rk==0: continue
                L=Bm.transpose()*NpeF
                rl=L.rank()
                nu0=any(L[r_,qcol[0]]!=0 for r_ in range(L.nrows())) if qcol else None
                out["pieces"].append(dict(p=p,eps=list(eps),piece=nm,dim=rk,lift_rank=rl,injective=rk==rl,nu0_coefficient_nonzero=bool(nu0)))
    out["total_rank"]=None
    out["all_injective"]=all(x["injective"] for x in out["pieces"])
    print(json.dumps(out),flush=True); res.append(out)
json.dump(res,open(f"finerOld_{sys.argv[1].replace(',','_')}.json","w"),indent=1)
