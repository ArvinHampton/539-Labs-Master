# Exact (symbolic) evaluation of the EM coefficients of em.py.
import sympy as sp
u=sp.symbols('u',positive=True)
def B1(x): return x-sp.Rational(1,2)
def B2(x): return x*x-x+sp.Rational(1,6)
def M(A11,A12,A22,p,r):
    w=sp.Rational(p+r+2,2)
    return sp.gamma(w)/2*sp.integrate(u**r/(A11+2*A12*u+A22*u**2)**w,(u,0,sp.oo))
def em(A11,A12,A22,l1,l2,c0,al,be):
    M00=M(A11,A12,A22,0,0)
    ML=l1*M(A11,A12,A22,1,0)+l2*M(A11,A12,A22,0,1)
    ML2=l1**2*M(A11,A12,A22,2,0)+2*l1*l2*M(A11,A12,A22,1,1)+l2**2*M(A11,A12,A22,0,2)
    gx=sp.sqrt(sp.pi)/(2*sp.sqrt(A11)); gy=sp.sqrt(sp.pi)/(2*sp.sqrt(A22))
    return [sp.simplify(M00), sp.simplify(-ML-B1(be)*gx-B1(al)*gy),
            sp.simplify(ML2/2-c0*M00+B1(be)*l1/(2*A11)+B2(be)*A12/(2*A11)+B1(al)*l2/(2*A22)+B2(al)*A12/(2*A22)+B1(al)*B1(be))]
h=sp.Rational(7,2)
I=sp.log(6+sp.sqrt(35))/(2*sp.sqrt(35))
Ps=em(1,h,h,0,h,0,0,0); R=em(1,h,h,0,h,0,0,1); Mm=em(1,h,h,0,-h,0,1,0)
out=[]
def show(nm,v):
    vv=[sp.nsimplify(sp.simplify(sp.expand_log(x,force=True)),[sp.log(6+sp.sqrt(35)),sp.sqrt(sp.pi),sp.sqrt(14),sp.sqrt(35)]) for x in v]
    out.append(f"{nm}: t^-1: {sp.simplify(v[0])}   t^-1/2: {sp.simplify(v[1])}   t^0: {sp.simplify(v[2])}")
    out.append(f"      numeric: {[sp.N(x,20) for x in v]}")
show("P_s",Ps); show("R",R); show("Mm",Mm)
E=[sp.simplify(R[i]+Mm[i]) for i in range(3)]
show("E",E)
out.append(f"check t^-1 of P_s - I = {sp.N(Ps[0]-I,30)}")
out.append(f"check const(P_s) - (11-7I)/20 = {sp.N(Ps[2]-(11-7*I)/20,30)} ;  simplify: {sp.simplify(sp.expand_log(Ps[2]-(11-7*I)/20,force=True))}")
out.append(f"check const(E) - (1-7I)/10 = {sp.N(E[2]-(1-7*I)/10,30)} ;  simplify: {sp.simplify(sp.expand_log(E[2]-(1-7*I)/10,force=True))}")
out.append(f"check t^-1/2(E) = {sp.simplify(E[1])}")
out.append(f"check a_P - sqrt(pi)(49-2sqrt14)/140 = {sp.simplify(Ps[1]-sp.sqrt(sp.pi)*(49-2*sp.sqrt(14))/140)}")
print("\n".join(out)); open("em_exact.txt","w").write("\n".join(out)+"\n")
