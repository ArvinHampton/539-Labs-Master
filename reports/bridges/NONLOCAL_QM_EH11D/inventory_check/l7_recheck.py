# Category A re-derivation of written EH L6->L7 algebra (23010998 Sec.3). Not a link test.
import sympy as s
k2,K,P=s.symbols('k2 K Phi')
sol=s.solve([6*k2-3*K+P/96, 4*k2+K-P/144],[k2,K],dict=True)[0]
print(sol, "K/k2 =", s.simplify(sol[K]/sol[k2]))
assert sol=={k2:P/1728,K:P/216}
print("on lock G_ext/g =", s.simplify((6*k2-3*K).subs(sol)), " -18k2 =", -18*sol[k2])
print("on lock G_fib/g (10k2-2K) =", s.simplify((10*k2-2*K).subs(sol)), " written -6k2 =", -6*sol[k2])
