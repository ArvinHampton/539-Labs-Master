# (2) Exact joint-eigenspace dimensions of <N,g> on the complement factor (monomial maps with exact Fraction phases),
# via stabiliser characters (orbit method).  Also exact trace tr(g | Fix(N,gamma)).
import sys, json, numpy as np
from fractions import Fraction as Fr
from family_s import Family
from even_exact import red
src=open('gap_g.py').read()
exec(src.split("out=[]")[0])
def run(m):
    s=2*m*m; F=Family(s); D=F.D; dm=mpart(D,m); dc=D//dm
    ec=(pow(dm,-1,dc)*dm)%D
    lab=[i for i,(al,be) in enumerate(F.LABELS) if all((ec*np.array(al)-np.array(al))%D==0) and all((ec*np.array(be)-np.array(be))%D==0)]
    S_=set(lab); minv=pow(m,-1,dc)
    def lift(Mc): return np.array([[ (Mc[i][j]*ec + (1 if i==j else 0)*(1-ec))%D for j in range(2)] for i in range(2)],dtype=object)
    G=lift([[0,-m],[minv,2*m]]); Nm=lift([[-1,0],[0,-1]])
    def mp(A):
        out={}
        for i in lab:
            al,be=F.LABELS[i]; al=np.array(al,dtype=object); be=np.array(be,dtype=object)
            j,ph=red(F,np.array([int(v) for v in A.dot(al)%D]),np.array([int(v) for v in A.dot(be)]))
            out[i]=(j,Fr(ph)%1)
        return out
    g=mp(G); N=mp(Nm)
    dims={}
    for sig in (1,-1):
        for tau in (1,-1):
            ch=lambda a,b: Fr(0 if sig==1 else a,2)+Fr(0 if tau==1 else b,2)   # chi(N^a g^b) in Q/Z
            seen=set(); cnt=0
            for x0 in lab:
                if x0 in seen: continue
                # g-cycle with phases
                cyc={x0:Fr(0)}; x=x0; ph=Fr(0); L=0
                while True:
                    j,p=g[x]; ph=(ph+p)%1; L+=1; x=j
                    if x==x0: break
                    cyc[x]=ph
                phL=ph
                # N-image
                j,p=N[x0]
                okN=True
                if j in cyc:
                    # N x0 = phase p * e_j ; e_j = g^c e_x0 / e(cyc[j]) -> N g^{-c} stabilises with phase p - cyc[j]
                    c=list(cyc).index(j)
                    okN=((p-cyc[j])-ch(1,-c))%1==0
                    orbit=set(cyc)
                else:
                    orbit=set(cyc)
                    y=j; 
                    while True:
                        orbit.add(y); y=g[y][0]
                        if y==j: break
                ok=okN and (phL-ch(0,L))%1==0
                seen|=orbit; cnt+=ok
            dims[(sig,tau)]=cnt
    return dict(m=m,s=s,n=len(lab),**{f"N={a},g={b}":v for (a,b),v in dims.items()},trace_g_on_FixNgamma=dims[(1,1)]-dims[(1,-1)],
                **{"2m":2*m,"m(m-1)":m*(m-1)})
if __name__=="__main__":
    out=[run(int(m)) for m in sys.argv[1].split(',')]
    for r in out: print(json.dumps(r))
    json.dump(out,open("gap_exact.json","w"),indent=1)
