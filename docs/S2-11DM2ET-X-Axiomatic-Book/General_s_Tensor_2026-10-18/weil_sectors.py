# (i) Weil scalar gamma_n of the odd factor and the induced 2-adic scalar; exact relations of rho_2.
# (ii) local quadratic forms q_p = -v_p x^2/p^e, v_p = (n/p^e)^{-1}; gamma's local sign.
# (iii) exact sector dimensions of Fix(N) ∩ Fix(gamma) by direct counting on the explicit monomial maps, vs closed forms.
import sys, json, math, numpy as np
from fractions import Fraction as F
from gen_factor import sympy_factor
exec(open('../2026-10-18-Tensor-Pattern-Closure/local2.py').read().split("# Local Weil factors")[0])
def inv2(A):
    R={}
    for i,(j,ph) in A.items(): R[j]=(i,(-ph)%1)
    return R
# symbolic S2,T2 (same for all odd s): S2 (eps,delta)->(delta,eps) phase e(-eps*delta/2) ; T2 as in local2 (overwrite S2 to symbolic convention)
S2s={(e,d):((d,e),F(-e*d,2)%1) for e in (0,1) for d in (0,1)}
res=[]
for s in [int(z) for z in sys.argv[1].split(',')]:
    n=s*(s-2); x=np.arange(n)
    Sn=np.exp(-2j*np.pi*(-2)*np.outer(x,x)/n)/np.sqrt(n)   # S_n^{-1} = conj of e(-2xy/n)/sqrt n
    Tn=np.diag(np.exp(-2j*np.pi*x*x/n))
    ks=[k for k in range(8) if np.allclose(np.linalg.matrix_power(np.exp(2j*np.pi*k/8)*Sn@Tn,3),np.exp(2j*np.pi*2*k/8)*Sn@Sn,atol=1e-8)]
    r={"s":s,"n":n,"gamma_n_k_over_8":ks}
    rel={}
    for k in ks:
        c=F(-k,8)%1; R2=scal(inv2(S2s),c); ST=mul(R2,T2)
        rel[k]={"c":str(c),"S4":pw(R2,4)==I2,"ST3=S2":pw(ST,3)==mul(R2,R2),"S2=-I":mul(R2,R2)=={i:(i,F(1,2)) for i in I2}}
    r["rho2_relations"]=rel
    loc={}
    for p,e in sympy_factor(n):
        q=p**e; v=pow(n//q,-1,q); loc[f"{p}^{e}"]={"q_p":f"-{v}x^2/{q} = {(-v)%q}x^2/{q}","divides":"s" if s%p==0 else "s-2","gamma_sign":((s-1)%q==1)*1 or -1 if (s-1)%q in (1,q-1) else None}
    r["local"]=loc
    # exact sector count: labels (x,eps,delta); conditions v(x,e,d)=v(-x,e,d), v(x,e,d)=(-1)^{ed} v((s-1)x,e,d)
    par=list(range(4*n)); sign=[0]*(4*n)
    def key(x,e,d): return (x*2+e)*2+d
    # orbit-cocycle
    seen={}; free=0; zero=0
    for X in range(n):
        for e in (0,1):
            for d in (0,1):
                k0=(X,e,d)
                if k0 in seen: continue
                orb={k0:0}; st=[k0]; bad=False
                while st:
                    (y,ee,dd)=st.pop(); ph=orb[(y,ee,dd)]
                    for (z,p2) in (((-y)%n,0),(((s-1)*y)%n,ee*dd)):
                        t=(z,ee,dd); pv=(ph+p2)%2
                        if t in orb:
                            if orb[t]!=pv: bad=True
                        else: orb[t]=pv; st.append(t)
                for t in orb: seen[t]=1
                if bad: zero+=len(orb)
                else: free+=1
    E=lambda m:(m+1)//2; O=lambda m:(m-1)//2
    pf=sympy_factor(n); allE=math.prod((p**e+1)//2 for p,e in pf)
    r.update({"dimV_upper_exact_count":free,"zero_labels":zero,"formula_s(s-1)":s*(s-1),"formula_2s-3":2*s-3,
              "dimW_formula_2(s-1)^2":2*(s-1)**2,"Eis_allEven_3prod":3*allE,
              "cusp_oddodd":O(s)*O(s-2),"cusp_evenmixed":3*(E(s)*E(s-2)-allE),"cusp_model_total":O(s)*O(s-2)+3*(E(s)*E(s-2)-allE)})
    res.append(r); print(json.dumps(r),flush=True)
json.dump(res,open(f"weil_sectors_{sys.argv[1].replace(',','_')}.json","w"),indent=1)
