# Step (4): Zwegers admissibility of H_s (Master definition: M=[[2,s],[s,s]], c1=(-1,1), c2=(-4,1)) as a function of s.
import sympy as sp
s = sp.symbols('s'); M = sp.Matrix([[2, s], [s, s]]); c1 = sp.Matrix([-1, 1]); c2 = sp.Matrix([-4, 1])
Qn = lambda c: sp.expand((c.T*M*c)[0]/2); B = lambda a, b: sp.expand((a.T*M*b)[0])
L = [f"Q(c1) = {Qn(c1)}  (<0 iff s>2)", f"Q(c2) = {Qn(c2)}  (<0 iff s>32/7, i.e. integer s>=5)", f"B(c1,c2) = {sp.factor(B(c1,c2))}",
     f"det M = {sp.factor(M.det())} (indefinite iff s>2)", f"c2^T M = {list(c2.T*M)}"]
for sv in range(3, 13):
    L.append(f"  s={sv}: Q(c1)={Qn(c1).subs(s,sv)}, Q(c2)={Qn(c2).subs(s,sv)}, B(c1,c2)={B(c1,c2).subs(s,sv)} -> Zwegers-admissible (both negative, same cone component since B<0): {Qn(c1).subs(s,sv)<0 and Qn(c2).subs(s,sv)<0}")
open('Hs_conditions.txt', 'w').write("\n".join(L)+"\n"); print("\n".join(L))
