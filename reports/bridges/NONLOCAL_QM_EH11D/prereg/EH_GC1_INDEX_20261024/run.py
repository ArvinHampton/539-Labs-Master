import sympy as s
k2,K,GG,G11=s.symbols('k2 K GG G11',positive=True)
ext=6*k2-3*K; fib=10*k2-2*K; c=8*s.pi*G11
def lock(G2,Phi,fw=s.Rational(-1,288)):
    so=s.solve([ext-c*(-G2/96), fib-c*fw*G2],[k2,K],dict=True)
    return len(so)==1 and s.simplify(so[0][k2]-Phi/1728)==0 and s.simplify(so[0][K]-8*so[0][k2])==0
T1=lock(GG,c*GG)
C=[not lock(GG,GG), not lock(GG/24,c*GG), not lock(GG,c*GG,s.Rational(-1,144))]
print("T1",T1,"controls_fail",C,"RESULT","PASS" if T1 and all(C) else "FAIL","Cat A-conditional WRITTEN-CHAT")
