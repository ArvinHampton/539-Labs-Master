# Local-derived (t4436, alpha-3 audit aid). Re-examines every (support, sign) job of s4c whose Groebner basis was NOT [1] but which
# returned no real all-nonzero solution, and prints the z-free GB, all complex solutions, and why each is rejected.
import itertools, sympy as sp, importlib.util
spec=importlib.util.spec_from_file_location("s4c","s4c_alpha_support_sign_split.py"); s4c=importlib.util.module_from_spec(spec); spec.loader.exec_module(s4c)
K90=s4c.K90; inv=s4c.inv; kron=s4c.kron; Dind=s4c.Dind
surv=[T for r in range(2,12) for T in itertools.combinations(K90,r) if all(len(c)!=1 for c in s4c.monomial_eqs(T).values())]
n=0
for T in surv:
    for s in itertools.product((1,-1),repeat=4):
        r=s4c.job((T,s))
        if r[2]=='solved' and not r[3]:
            n+=1
            X=[sp.Symbol(f'a{p}') for p in T]; Ml=sp.Matrix([[kron(d,p) for p in T] for d in Dind])
            sol,params=Ml.gauss_jordan_solve(sp.Matrix(s)); y=list(params); sub=dict(zip(X,list(sol)))
            E={}
            for i,a in enumerate(T):
                for j,b in enumerate(T):
                    g=(a*inv(b))%140; E[g]=E.get(g,0)+X[i]*X[j]
            eqs=[e for e in {sp.expand((E[1]-1).subs(sub))}|{sp.expand(v.subs(sub)) for g,v in E.items() if g!=1} if e!=0]
            G=sp.groebner(eqs,*y,order='lex') if y else None
            allsol=sp.solve(G.exprs,y,dict=True) if y else []
            vals=[tuple(sp.simplify(c.subs(rr)) for c in sol) for rr in allsol]
            print(T,s,"GB(no saturation):",G.exprs if G else None,"; complex solutions:",len(vals),"; each has a zero coordinate on T:",[any(x==0 for x in v) for v in vals],"; all real:",[all(x.is_real for x in v) for v in vals])
print("re-examined jobs:",n)
