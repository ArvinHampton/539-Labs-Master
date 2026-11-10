import sympy as s
k2,K,P=s.symbols('k2 K Phi')
ext=6*k2-3*K; fib=10*k2-2*K
sol=s.solve([ext+P/96, fib+P/288],[k2,K],dict=True)
P1=len(sol)==1 and s.simplify(sol[0][k2]-P/1728)==0 and s.simplify(sol[0][K]-8*sol[0][k2])==0
P2=s.expand((fib-ext)-(4*k2+K))==0 and s.simplify((-P/288)-(-P/96)-P/144)==0
ctrl=[]
for w in (P/144,P/96):
    so=s.solve([ext+P/96, fib+w],[k2,K],dict=True)[0]
    ctrl.append(not(s.simplify(so[k2]-P/1728)==0 and s.simplify(so[K]-8*so[k2])==0))
P3=all(ctrl)
print("sol",sol,"P1",P1,"P2",P2,"P3",P3,"RESULT","PASS" if P1 and P2 and P3 else "FAIL")
