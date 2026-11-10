import sympy as s
k2,K,P=s.symbols('k2 K Phi')
def L(fw):
    so=s.solve([6*k2-3*K+P/96,10*k2-2*K-fw],[k2,K],dict=True)
    return so,len(so)==1 and s.simplify(so[0][k2]-P/576)==0 and s.simplify(so[0][K]-4*so[0][k2])==0
so,P1=L(P/288); _,c=L(-P/288)
print("sol",so,"P1",P1,"P2_ctrl_fails",not c,"P3_sign_required",not c,"RESULT","PASS" if P1 and not c else "FAIL","WRITTEN-CHAT")
