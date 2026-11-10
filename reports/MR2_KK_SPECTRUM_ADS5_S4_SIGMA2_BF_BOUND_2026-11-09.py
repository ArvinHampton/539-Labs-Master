#!/usr/bin/env python3
"""MR2 KK/BF check for Owner-adopted (D): AdS5 x S4 x Sigma_g direct product (Kehagias-Russo hep-th/0003281 (vi), eqs.13-14),
G4 = q0 vol(S4) only. Conventions as PP 4660b73e: Ric_AdS5 = Ric_Sigma = -4k^2 g, L5=1/k, rho=1/(2k), r=sqrt6/(4k), q0=2 sqrt6 k.
Every input formula cited inline. Nothing here is fitted."""
import sympy as sp, mpmath as mp
mp.mp.dps = 30
out = []
def P(*a):
    s = ' '.join(str(x) for x in a); print(s); out.append(s)

k = sp.symbols('k', positive=True)
q0, r, rho, L5 = 2*sp.sqrt(6)*k, sp.sqrt(6)/(4*k), 1/(2*k), 1/k
# --- 1. vacuum check, 11D Einstein eq R_MN = 1/12 (G_M...G_N... - 1/12 g G^2), G on S4 only
G2 = 24*q0**2; GG = 6*q0**2
R_S4 = sp.simplify(GG/12 - G2/144)          # coefficient of g on S4
R_ext = sp.simplify(-G2/144)                # coefficient of g on AdS5 and Sigma
P('1. Ric_S4/g =', R_S4, ' expect 3/r^2 =', sp.simplify(3/r**2), '| Ric_ext/g =', R_ext, ' expect -4/L5^2 =', -4/L5**2, ' Sigma K=-1/rho^2 =', -1/rho**2)
# KR eq.13: L5^2 = 2R0^2/3, rho^2 = R0^2/6, r^2 = R0^2/4
R0 = sp.symbols('R0', positive=True)
P('   KR(13) ratios L5/rho, L5/r:', sp.sqrt(sp.Rational(2,3)/sp.Rational(1,6)), sp.sqrt(sp.Rational(2,3)/sp.Rational(1,4)), '| (D):', sp.simplify(L5/rho), sp.simplify(L5/r))
# 7D Einstein space M7 = AdS5 x Sigma: Ric = -6/L7^2 g  =>  L7
L7 = sp.sqrt(sp.Rational(6,4))/k
P('   L7 =', L7, ' 2r =', sp.simplify(2*r), ' (AdS7xS4 relation L7=2R holds:', sp.simplify(L7-2*r)==0, ')  (L5/L7)^2 =', sp.simplify((L5/L7)**2))

# --- 2. Freund-Rubin coupled scalars, DeWolfe et al hep-th/0105047 eq.(4.7), p=7,q=4; minus branch k>=2, plus k>=0 (sec.4 special cases)
p_, q_ = 7, 4
def m2_minus(n): return sp.Rational((p_-1)**2,(q_-1)**2)*n*(n-q_+1)
def m2_plus(n):  return sp.Rational((p_-1)**2,(q_-1)**2)*(n+2*(q_-1))*(n+q_-1)
def dimSO5(n): return sp.Rational((n+1)*(n+2)*(2*n+3),6)   # [n,0] scalar harmonics on S4
P('2. 7D masses M^2 L7^2 (DeWolfe 4.7); 7D BF = -9; 5D BF in L7 units = -4*(L7/L5)^2 =', -4*sp.Rational(3,2))
for n in range(0,6):
    mm = m2_minus(n) if n>=2 else None
    P(f'   S4 level k={n} [dim {dimSO5(n)}]: minus {mm}  plus {m2_plus(n)}')
# --- 3. reduce on Sigma: phi = psi(AdS5) Y(Sigma), -Lap_Sigma Y = lam Y, lam = lam_hyp/rho^2 = 4k^2 lam_hyp
lh = sp.symbols('lambda_hyp', nonnegative=True)
def m2L5(M2L7sq): return sp.nsimplify(M2L7sq*sp.Rational(2,3)) + 4*lh
m5 = m2L5(-8)
P('3. k=2 [14] mode: m^2 L5^2 =', m5, '; BF violated iff', sp.solve(sp.Lt(m5,-4), lh))
P('   constant mode (lam=0): m^2L^2 =', m5.subs(lh,0), '=', float(m5.subs(lh,0)), ' Delta = 2 +/- sqrt(4+m^2L^2) =', sp.simplify(2+sp.sqrt(4+m5.subs(lh,0))))
# genus-2 lambda1 pins
lam1_KMP = mp.mpf('3.8388976481')   # Kravchuk-Mazac-Pal 2111.12716 upper bound, all genus-2
lam1_Bolza = mp.mpf('3.8388872588') # Strohmaier-Uski 1110.2150 Bolza surface
for nm, v in [('KMP upper bound', lam1_KMP), ('Bolza', lam1_Bolza), ('threshold', mp.mpf(1)/3), ('Otal-Rosas 1/4', mp.mpf(1)/4)]:
    P(f'   lam1={nm} {mp.nstr(v,12)}: m^2L^2 = {mp.nstr(-mp.mpf(16)/3+4*v,12)}')
P('   other levels: k=3 minus (M2L7^2=0) -> m^2L^2 = 4 lam >= 0; plus branch k=0 -> ', m2L5(m2_plus(0)).subs(lh,0), '(PP C3 breathing 48)')
# --- 4. Sigma breathing in 7D Einstein-Lambda reduction: L=R-1/2(dphi)^2-V, 3a+2b=0, a^2=1/15
a = 1/sp.sqrt(15); b = -sp.Rational(3,2)*a; ph = sp.symbols('phi')
Lam7 = -10*k**2   # Ric = 2Lam7/5 g = -4k^2
V = 2*Lam7*sp.exp(2*a*ph) + 8*k**2*sp.exp(2*(a-b)*ph)
P('4. Sigma breathing: V(0)=', sp.simplify(V.subs(ph,0)), " V'(0)=", sp.simplify(sp.diff(V,ph).subs(ph,0)), " m^2L^2=V''(0)/k^2 =", sp.simplify(sp.diff(V,ph,2).subs(ph,0)/k**2), '(PP C3: 8)')
# Teichmueller TT on Sigma: Delta_L(Sigma) on TT = -Box + 4K ; Einstein deformations of 2D: Delta_L h = 2K h -> -Box h = -2K h ... 5D: (Delta_L7 - 2 Lam_R) h = 0 with Lam_R=-4k^2
P('   Teichmueller TT (holomorphic quadratic differentials, 6g-6 real): 5D m^2 = 0 (Einstein-deformation kernel); graviton tower m^2L^2 = 4 lam_hyp')
# --- 5. probe M5 domain wall on R^{1,3} x Sigma at point of S4: charge/tension = q0 L_d / d, general sqrt(6/d)
P('5. probe M5: q0/(4k) =', sp.simplify(q0/(4*k)), '=', float(q0/(4*k)), '; AdS7 calib q/(6k) with q=6k ->', 1, '; general AdS_{d+1}xH^{6-d}: sqrt(6/d):', [sp.sqrt(sp.Rational(6,d)) for d in (2,3,4,5,6)])
# --- 6. N, g numbers (standard (2 pi lp)^3 N; PP A1/A4)
N, g = 4880, 2
kk = mp.sqrt(mp.mpf(3)/8)*(mp.pi*N)**(-mp.mpf(1)/3)
P(f'6. k = {mp.nstr(kk,9)} lp^-1; L5 = {mp.nstr(1/kk,8)}; L7 = {mp.nstr(mp.sqrt(1.5)/kk,8)}; r = {mp.nstr(mp.sqrt(6)/(4*kk),8)} = (piN)^(1/3)={mp.nstr((mp.pi*N)**(mp.mpf(1)/3),8)}; rho = {mp.nstr(1/(2*kk),8)}')
P(f'   K_Sigma = -4k^2 = {mp.nstr(-4*kk**2,9)} lp^-2; Phi=216(piN)^(-2/3)={mp.nstr(216*(mp.pi*N)**(-mp.mpf(2)/3),9)}; -Phi/144 = {mp.nstr(-216*(mp.pi*N)**(-mp.mpf(2)/3)/144,9)}')
P(f'   Area(Sigma_2) = pi(g-1)/k^2 = {mp.nstr(mp.pi*(g-1)/kk**2,9)} lp^2; lam1 physical range (0, {mp.nstr(lam1_KMP*4*kk**2,8)}] lp^-2; BF-unstable iff lam_phys < 4k^2/3 = {mp.nstr(4*kk**2/3,8)} lp^-2')
P(f'   (lp/r)^6 = {mp.nstr((mp.pi*N)**-2,6)}  (lp/L5)^6 = {mp.nstr(kk**6,6)}')
# central charges: a = pi L^3/(8 G5); calibrations
G11 = (2*mp.pi)**8/(16*mp.pi)   # lp=1
VolS4 = lambda R: 8*mp.pi**2/3*R**4
R = (mp.pi*N)**(mp.mpf(1)/3); L7n = 2*R
P(f'   calib L7^5/G7 = {mp.nstr(L7n**5*VolS4(R)/G11,12)} vs 16N^3/(3pi^2) = {mp.nstr(16*mp.mpf(N)**3/(3*mp.pi**2),12)}')
VolSig = 4*mp.pi*(g-1)*(1/(2*kk))**2
aD = mp.pi*(1/kk)**3*VolS4(mp.sqrt(6)/(4*kk))*VolSig/(8*G11)
P(f'   a_D = c_D (2-derivative) = {mp.nstr(aD,10)}; (2/3)^(7/2)(g-1)N^3 = {mp.nstr(mp.mpf(2/3.)**3.5*(g-1)*mp.mpf(N)**3,10)} = 8sqrt6/81 = {mp.nstr(8*mp.sqrt(6)/81,10)}')
nv = (g-1)*(mp.mpf(4)*N**3/3 - mp.mpf(N)/3 - 1); nh = (g-1)*(mp.mpf(4)*N**3/3 - mp.mpf(4)*N/3)
P(f'   comparison only (not (D)): MN N=2 (GM 2.5, 2.1) a={mp.nstr((5*nv+nh)/24,10)} c={mp.nstr((2*nv+nh)/12,10)}; MN N=1 large-N 9/32(g-1)N^3 = {mp.nstr(mp.mpf(9)/32*N**3,10)}')
open(__file__.replace('.py','.log'),'w').write('\n'.join(out)+'\n')
