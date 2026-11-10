import sympy as sp
y,k,b=sp.symbols('y k b',real=True)
eta=sp.diag(-1,1,1,1)
def K4(A,s=1): q=sp.exp(-2*A)*eta; return sp.simplify(s*sp.Rational(1,2)*q.diff(y)),q
def tr(Km,q): return sp.simplify((q.inv()*Km).trace())
res={}
Km,q=K4(k*y); Kt=tr(Km,q)
res['P1']=sp.simplify(Km+k*q)==sp.zeros(4); res['P2_4D']=sp.simplify(Kt+4*k)==0
# internal block, B const: h_ab=e^{2B} ghat, d_y=0
B=sp.Symbol('B'); Kint=sp.diff(sp.exp(2*B),y)/2
res['P2_10D']=sp.simplify(Kt+6*Kint/sp.exp(2*B)+4*k)==0
res['P3']=sp.simplify(Km-Kt*q-3*k*q)==sp.zeros(4)
Kc,qc=K4(k*y**2); res['C1_fails']=sp.simplify(Kc+k*qc)!=sp.zeros(4)
Kf,qf=K4(k*y,-1); res['C2_fails']=sp.simplify(Kf+k*qf)!=sp.zeros(4) and sp.simplify(Kf-k*qf)==sp.zeros(4)
Ki=sp.diff(sp.exp(2*b*y),y)/2/sp.exp(2*b*y); res['C3_fails']=sp.simplify(Kt+6*Ki+4*k)!=0
print('K_mn =',Km.diag() if hasattr(Km,'diag') else Km,' trace K =',Kt)
for kk,v in res.items(): print(kk,v)
print('EH-JX1', 'PASS' if all(res.values()) else 'FAIL')
