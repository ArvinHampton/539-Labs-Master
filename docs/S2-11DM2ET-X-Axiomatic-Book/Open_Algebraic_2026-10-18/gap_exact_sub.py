# (b) Exact subspace test at odd m: each half-cone kernel vector k (rational, label basis) satisfies
#   k = delta_iso ⊗ c exactly (rank-1 with m-side = indicator of mZ/m^2), and on the complement N c = c, g c = -c exactly
#   (monomial maps with exact Fraction phases).  With dim X = m(m-1) (gap_exact, exact) and dim K = m(m-1): K = delta ⊗ X.
#   Also: exact traces tr(g h), h in {1, N, gamma, N gamma} (sum of phases over fixed labels, exact in Q(zeta)).
import sys, json, numpy as np, cmath, math
from fractions import Fraction as Fr
import n9h
from even_exact import red
src=open('gap_g.py').read(); exec(src.split("out=[]")[0])
res=[]
for m in map(int,sys.argv[1].split(',')):
    s=2*m*m; info=n9h.run(s); reps=n9h.run.reps; M=n9h.run.M; F=n9h.run.F; D=F.D
    X_,nul=M.transpose().nullspace(); K=[[int(X_[i,j]) for i in range(X_.nrows())] for j in range(nul)]
    dm=mpart(D,m); dc=D//dm; ec=(pow(dm,-1,dc)*dm)%D; em=(1-ec)%D
    key=[(tuple((em*np.array(al))%D),(tuple((ec*np.array(al))%D),tuple((ec*np.array(be))%D))) for al,be in F.LABELS]
    Ms=sorted({k[0] for k in key}); Cs=sorted({k[1] for k in key}); mi={x:i for i,x in enumerate(Ms)}; ci={x:i for i,x in enumerate(Cs)}
    idx={}
    for i,(al,be) in enumerate(F.LABELS): idx.setdefault((al[0]%D,al[1]%D),[]).append((i,be))
    b0=tuple(F.BES[0])
    delta=[1 if all((m*np.array(x))%D==0) else 0 for x in Ms]
    minv=pow(m,-1,dc)
    def lift(Mc): return np.array([[ (Mc[i][j]*ec + (1 if i==j else 0)*(1-ec))%D for j in range(2)] for i in range(2)],dtype=object)
    z=mi[(0,0)]
    def mp(A):
        o={}
        for i,(al,be) in enumerate(F.LABELS):
            if key[i][0]!=Ms[z]: continue
            j,ph=red(F,np.array([int(v) for v in A.dot(np.array(al,dtype=object))%D]),np.array([int(v) for v in A.dot(np.array(be,dtype=object))]))
            o[ci[key[i][1]]]=(ci[key[j][1]],Fr(ph)%1)
        return o
    g=mp(lift([[0,-m],[minv,2*m]])); N=mp(lift([[-1,0],[0,-1]])); Gm=mp(lift([[-1,-s],[2,2*s-1]]))
    ok_rank1=ok_N=ok_g=True
    for k in K:
        v={}
        for c,O in zip(k,reps):
            if c==0: continue
            for x in O:
                for i,be in idx[x]:
                    if tuple(be)==b0: v[i]=v.get(i,0)+c
        T=np.zeros((len(Ms),len(Cs)),dtype=object)
        for i,c in v.items(): T[mi[key[i][0]],ci[key[i][1]]]+=c
        # rank-1 with m-side delta: rows where delta=1 equal, others zero
        rows=[r for r in range(len(Ms)) if delta[r]]
        cvec=T[rows[0]]
        if any(any(T[r]!=cvec) for r in rows) or any(any(T[r]!=0) for r in range(len(Ms)) if not delta[r]): ok_rank1=False
        for mapx,sgn,flag in ((N,1,'N'),(g,-1,'g')):
            # (map c)_j = e(ph) c_i must equal sgn*c_j : exact requires ph in {0,1/2} wherever c_i != 0
            img={}
            for i_,(j_,ph) in mapx.items():
                if cvec[i_]!=0:
                    if ph not in (0,Fr(1,2)): 
                        if flag=='N': ok_N=False
                        else: ok_g=False
                    img[j_]=cvec[i_]*(1 if ph==0 else -1)
            good=all(img.get(j_,0)==sgn*cvec[j_] for j_ in range(len(Cs)))
            if not good:
                if flag=='N': ok_N=False
                else: ok_g=False
    # exact traces (as sums of roots of unity; report as multiset of phases -> evaluate exactly when phases in {0,1/2,1/4,3/4})
    def compose(a,b):  # a after b
        return {i:(a[b[i][0]][0],(b[i][1]+a[b[i][0]][1])%1) for i in b}
    I={i:(i,Fr(0)) for i in range(len(Cs))}
    traces={}
    for nm,h in (("g",I),("gN",N),("g gamma",Gm),("gN gamma",compose(N,Gm))):
        gh=compose(g,h); ph=[p for i,(j,p) in gh.items() if i==j]
        val=sum(cmath.exp(2j*math.pi*float(p)) for p in ph)
        traces[nm]={"fixed_labels":len(ph),"value":[round(val.real,9),round(val.imag,9)],"phases":sorted({str(p) for p in ph})}
    r=dict(m=m,kernel_dim=len(K),rank1_delta_exact=ok_rank1,Nc_eq_c_exact=ok_N,gc_eq_minus_c_exact=ok_g,traces=traces,
           trace_sum_over_4=round(sum(t["value"][0] for t in traces.values())/4,9))
    print(json.dumps(r),flush=True); res.append(r)
json.dump(res,open("gap_exact_sub.json","w"),indent=1)
