# Item 1: sector-by-sector nonvanishing via local involutions Z_p : x -> u_p x (u_p = -1 at p, +1 elsewhere, CRT).
# Z_p are isometries of Delta commuting with <gamma,-1> => permute orbits, commute with rho.  Sector eps: P_eps = prod (1+eps_p Z_p).
# Exact integer data: N_O(q) (vrank counts).  c_eps(O,q) = sum_S eps_S N_{Z_S O}(q).
#   dim_in_U = rank(P_eps) (exact) ; lift_rank = rank(P_eps N) (exact) ; injective iff equal.
#   leading coefficient: smallest |q| with some c != 0; cancellation_free if a single nonzero term.
import sys, json, itertools, numpy as np, flint, sympy
from sympy.ntheory.modular import crt
def data(s,Q):
    src=open('vrank_src.py').read()
    ns={}; exec(src.split('if __name__')[0].replace("    rk = flint.fmpz_mat(Mx).rank()\n","    run.store=(orb,counts,modes,mod,D,Mx,no)\n    rk=0\n"),ns)
    ns['run'](s,Q); return ns['run'].store
def run(s,Q):
    orb,counts,modes,mod,D,Mx,no=data(s,Q)
    M=2*D if s%2 else D
    ps=[p for p in sorted(sympy.factorint(s*(s-2))) if p!=2]
    reps={}
    for x,o in orb.items(): reps.setdefault(o,x)
    Zs={}
    for p in ps:
        pe=p**sympy.multiplicity(p,M); rest=M//pe
        u=int(crt([pe,rest],[pe-1,1])[0])
        Zs[p]=[orb[(u*reps[o][0]%mod[0],u*reps[o][1]%mod[1])] for o in range(no)]
    Mx=np.array(Mx,dtype=object)
    out={"s":s,"Qmax":Q,"n_orbits":no,"primes":ps,"sectors":[]}
    td=tl=0
    order=sorted(range(len(modes)),key=lambda i:(abs(modes[i]),modes[i]))
    for eps in itertools.product((1,-1),repeat=len(ps)):
        P=np.zeros((no,no),dtype=object)
        for S in itertools.product((0,1),repeat=len(ps)):
            sg=1; img=list(range(no))
            for b,p,e in zip(S,ps,eps):
                if b: sg*=e; img=[Zs[p][i] for i in img]
            for o in range(no): P[o,img[o]]+=sg
        dimU=flint.fmpz_mat(P.tolist()).rank()
        if dimU==0: continue
        C=P.dot(Mx); rl=flint.fmpz_mat(C.tolist()).rank()
        lead=None
        for i in order:
            nz=[o for o in range(no) if C[o,i]!=0]
            if nz:
                o=nz[0]; terms=[Mx[j,i]*P[o,j] for j in range(no) if P[o,j]!=0]
                k=sum(1 for t in terms if t!=0)
                lead={"q_scaled":int(modes[i]),"orbit":o,"coef":int(C[o,i]),"nonzero_terms":k,"cancellation_free":k==1}
                break
        out["sectors"].append({"eps":dict(zip(map(str,ps),eps)),"dim_in_U":dimU,"lift_rank":rl,"injective":rl==dimU,"lead":lead})
        td+=dimU; tl+=rl
    out.update(sum_dim=td,sum_lift=tl,certified_V=(tl==no))
    return out
if __name__=="__main__":
    Q=float(sys.argv[2]); res=[]
    for s in map(int,sys.argv[1].split(',')):
        r=run(s,Q); res.append(r)
        print(s,"orbits",r["n_orbits"],"sum_dim",r["sum_dim"],"sum_lift",r["sum_lift"],"cert",r["certified_V"],flush=True)
        for sec in r["sectors"]: print("   ",sec,flush=True)
    json.dump(res,open(f"item1_lead_{sys.argv[1].replace(',','_')}.json","w"),indent=1)
