#!/usr/bin/env python3
"""NL1_OMEGA_FTOTAL_20261024 — structural (symbolic) check only. No numerics."""
import sympy as sp
k,K,b,Phi,g11,gs=sp.symbols('k K b Phi g11 g_s')
O0=sp.Symbol('Omega_0')
fw,fc,fb,Pf=[sp.Function(n) for n in ('f_warp','f_curv','f_b','Phi_flux')]
NAMES=['F_Coulomb_rel','F_SO','F_torsion','F_flux','F_leak']
C=sp.symbols(' '.join(NAMES))
OMEGA=O0*fw(k)*fc(K)*fb(b)*Pf(Phi)               # locked (pin)
FT=sp.Add(*C)*OMEGA                               # locked (pin)
def same(a,b): return sp.simplify(a-b)==0
r={}
r['P1']=same(OMEGA,O0*fw(k)*fc(K)*fb(b)*Pf(Phi)) and OMEGA.free_symbols>={k,K,b,Phi}
r['P2']=same(FT,(C[0]+C[1]+C[2]+C[3]+C[4])*OMEGA) and len(C)==5
r['P3']=OMEGA.has(fw(k)) and OMEGA.has(Pf(Phi)) and [str(c) for c in C]==NAMES
ctrl={
 'C1_wrong_args': O0*fw(g11)*Pf(gs),
 'C2a_no_Omega': sp.Add(*C),
 'C2b_four_comp': sp.Add(*C[:4])*OMEGA,
 'C2c_six_comp': (sp.Add(*C)+sp.Symbol('F_extra'))*OMEGA,
 'C3_catB_nearmiss': 1/sp.sqrt(1+g11**2+gs**2),
}
tgt={'C1_wrong_args':OMEGA,'C2a_no_Omega':FT,'C2b_four_comp':FT,'C2c_six_comp':FT,'C3_catB_nearmiss':OMEGA}
cf={n:not same(e,tgt[n]) for n,e in ctrl.items()}
for n,v in r.items(): print(f"T1 {n}: {'HOLD' if v else 'FAIL'}")
for n,v in cf.items(): print(f"CONTROL {n}: {'FAILS (as required)' if v else 'MATCHES (BAD)'}")
ok=all(r.values()) and all(cf.values())
print("CATEGORY: Cat B continuum (structural lock; not paper Cat A; no numerics; maps separate)")
print(f"RESULT {'PASS' if ok else 'FAIL'}")
