# Item 5 (exact): a rho-invariant sector with no T-invariant vector lifts to cusp forms.
# For odd s, V = A3⊗(Z/s)^+⊗(Z/(s-2))^+ ⊕ B1⊗(Z/s)^-⊗(Z/(s-2))^-, refined by local parities Z_p (p^e || s(s-2)).
# T-invariant dimension of a sector = product of local T-invariant dims (exponents with coprime denominators add to 0 mod 1 iff each is 0).
import json, math, itertools, sys
def fac(n):
    out=[];p=2
    while p*p<=n:
        if n%p==0:
            e=0
            while n%p==0:n//=p;e+=1
            out.append((p,e))
        p+=1
    if n>1:out.append((n,1))
    return out
def local_dims(p,e):
    q=p**e; plus=(q+1)//2; minus=(q-1)//2
    # q_p(x) = -v x^2/q ≡ 0 mod 1  <=>  p^ceil(e/2) | x
    k=-(-e//2); zeros=[x for x in range(q) if x%(p**k)==0]          # includes 0
    tplus=1+(len(zeros)-1)//2; tminus=(len(zeros)-1)//2
    return {1:(plus,tplus),-1:(minus,tminus)}
res=[]
for s in [int(z) for z in sys.argv[1].split(',')]:
    n=s*(s-2); pf=fac(n); L={(p,e):local_dims(p,e) for p,e in pf}
    sides={(p,e):('s' if s%p==0 else 's-2') for p,e in pf}
    tot=0; cusp_proved=0; eis_allEven=0; mixed_unproved=0; secs=[]
    for signs in itertools.product((1,-1),repeat=len(pf)):
        sg=dict(zip(pf,signs))
        Zs=math.prod(sg[k] for k in pf if sides[k]=='s'); Zt=math.prod(sg[k] for k in pf if sides[k]=='s-2')
        if Zs!=Zt: continue
        char=(3,1) if Zs==1 else (1,0)    # (dim, T-invariant dim) of A3 resp. B1 ; A3 has one T-invariant vector (00+01), B1 none
        dim=char[0]*math.prod(L[k][sg[k]][0] for k in pf); tinv=char[1]*math.prod(L[k][sg[k]][1] for k in pf)
        tot+=dim; alleven=all(v==1 for v in signs)
        if alleven: eis_allEven+=dim
        elif tinv==0: cusp_proved+=dim
        else: mixed_unproved+=dim
        secs.append({"signs":{f"{p}^{e}":sg[(p,e)] for p,e in pf},"dim":dim,"T_invariant_dim":tinv})
    r={"s":s,"dimV_sectors":tot,"s(s-1)":s*(s-1),"d_Eis_allEven":eis_allEven,"cusp_proved_Cat_A":cusp_proved,"nonEven_with_T_invariants":mixed_unproved,
       "oddchar_dim":(s-1)*(s-3)//4,"sectors":secs}
    res.append(r); print(s,tot,s*(s-1),"allEven",eis_allEven,"cusp>=",cusp_proved,"undecided",mixed_unproved)
json.dump(res,open("cusp_sectors.json","w"),indent=1)
