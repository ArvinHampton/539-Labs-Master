# MR2 check script, 2026-11-09 (America/Chicago). Pure arithmetic/representation checks; no external I/O.
# Conventions: 11D action (1/2k^2) Int sqrt(-g) (R - (1/48) G_MNPQ G^MNPQ), 2k^2 = 16 pi G11 = (2 pi)^8 lp^9
# => Einstein eq  G_MN = (1/12)(G_MPQR G_N^PQR - (1/8) g_MN G^2).  Units lp = 1.
import sympy as sp, itertools, math
from fractions import Fraction as Fr

k, g, N = sp.symbols('k g N', positive=True)
# --- 1. Adopted vacuum (D) (PP 4660b73e): AdS5(L=1/k) x S4(r) x Sigma_g(rho), G = q0 vol(S4)
q0 = 2*sp.sqrt(6)*k; r = sp.sqrt(6)/(4*k); rho = 1/(2*k)
Ric = {'AdS5': -4*k**2, 'S4': 3/r**2, 'Sig': -1/rho**2}
dims = {'AdS5':5, 'S4':4, 'Sig':2}
R = sp.simplify(sum(dims[b]*Ric[b] for b in dims))
Ein = {b: sp.simplify(Ric[b] - R/2) for b in dims}
Phi = 24*q0**2                       # G_MNPQ G^MNPQ = 4! q0^2 for G = q0 vol4
GG = {'AdS5':0, 'S4':6*q0**2, 'Sig':0}   # G_MPQR G_N^PQR = 3! q0^2 g_MN on S4 legs
rhs = {b: sp.simplify(sp.Rational(1,12)*(GG[b] - sp.Rational(1,8)*Phi)) for b in dims}
print("R =", R, "| Einstein blocks:", Ein, "| flux rhs:", rhs)
assert all(sp.simplify(Ein[b]-rhs[b])==0 for b in dims)
print("Phi := G.G on vacuum =", sp.simplify(Phi), "; blocks/Phi:", {b: sp.simplify(rhs[b]/Phi) for b in dims})
print("k^2/Phi =", sp.simplify(k**2/Phi), " (EH lock claims 1/1728)")
print("Ric_S4/Phi =", sp.simplify(Ric['S4']/Phi), " K_Gauss(Sigma)/Phi =", sp.simplify(-1/rho**2/Phi))
print("G_S4 - G_ext =", sp.simplify((rhs['S4']-rhs['AdS5'])/Phi), "* Phi (EH alg claims 1/144)")
# --- 2. Flux quantization  q0 Vol(S4_r) = (2 pi)^3 N
volS4 = sp.Rational(8,3)*sp.pi**2*r**4
ksol = sp.solve(sp.Eq(q0*volS4, (2*sp.pi)**3*N), k)[0]
print("k(N) =", sp.simplify(ksol), " check vs sqrt(3/8)(pi N)^(-1/3):", sp.N(ksol.subs(N,4880)), sp.N(sp.sqrt(sp.Rational(3,8))*(sp.pi*4880)**sp.Rational(-1,3)))
kN = sp.sqrt(sp.Rational(3,8))*(sp.pi*N)**sp.Rational(-1,3)
PhiN = sp.simplify(Phi.subs(k,kN)); print("Phi(N) =", PhiN)
vals = {}
for name, ex in [('k',kN),('L_AdS',1/kN),('r_S4',r.subs(k,kN)),('rho_Sigma',rho.subs(k,kN)),('Phi',PhiN),
                 ('Area_Sigma_g2', (4*sp.pi*(g-1)*rho**2).subs(k,kN)),('(lp/r)^6',(1/r.subs(k,kN))**6)]:
    v = sp.N(ex.subs({N:4880,g:2}), 12); vals[name]=v; print(f"  N=4880,g=2: {name} = {v}")
# --- 3. 5D Newton constant and holographic a=c=pi L^3/(8 G5) (Henningson-Skenderis; GM eq. 2.8 usage)
G11 = 16*sp.pi**7                       # GM: G11 = 16 pi^7 lp^9
V6 = volS4*4*sp.pi*(g-1)*rho**2
G5 = G11/V6
aD = sp.simplify((sp.pi*(1/k)**3/(8*G5)).subs(k,kN))
print("V6 =", sp.simplify(V6), "; G5(N,g) =", sp.simplify(G5.subs(k,kN)), "; a_D=c_D =", aD, "=", sp.N(aD/((g-1)*N**3)), "(g-1)N^3")
print("  a_D(g=2,N=4880) =", sp.N(aD.subs({g:2,N:4880}),12), "; G5 =", sp.N(G5.subs(k,kN).subs({g:2,N:4880}),6), "lp^3")
# calibration of the same method on AdS5xS5 (IIB): expect N^2/4
gs,al,Nn = sp.symbols('g_s alpha N', positive=True); L5 = (4*sp.pi*gs*Nn*al**2)**sp.Rational(1,4)
G10 = (2*sp.pi)**7*gs**2*al**4/(16*sp.pi); G5b = G10/(sp.pi**3*L5**5)
print("  calibration AdS5xS5: pi L^3/(8G5) =", sp.simplify(sp.pi*L5**3/(8*G5b)))
# --- 4. Class S central charges (GM eq. 2.1, 2.4, 2.5; gluing of 2g-2+n T_N and 3g-3+n SU(N))
def nvnh(Nv, gg, n):
    TNv = Fr(2,3)*Nv**3 - Fr(3,2)*Nv**2 - Fr(1,6)*Nv + 1; TNh = Fr(2,3)*Nv**3 - Fr(2,3)*Nv
    nv = (2*gg-2+n)*TNv + (3*gg-3+n)*(Nv**2-1); nh = (2*gg-2+n)*TNh
    return nv, nh
def ac(nv, nh): return Fr(5*nv+nh,24), Fr(2*nv+nh,12)
# consistency with GM (2.5) at n=0 and BBBW (E.6) T_N
for Nv in (2,3,7,4880):
    nv,nh = nvnh(Nv,2,0); assert nv == (2-1)*(Fr(4,3)*Nv**3-Fr(1,3)*Nv-1) and nh == (2-1)*(Fr(4,3)*Nv**3-Fr(4,3)*Nv)
    TNv = Fr(2,3)*Nv**3 - Fr(3,2)*Nv**2 - Fr(1,6)*Nv + 1; TNh = Fr(2,3)*Nv**3 - Fr(2,3)*Nv
    a,c = ac(TNv,TNh); assert a == Fr(Nv**3,6)-Fr(5*Nv**2,16)-Fr(Nv,16)+Fr(5,24) and c == Fr(Nv**3,6)-Fr(Nv**2,4)-Fr(Nv,12)+Fr(1,6)
print("GM(2.5) and BBBW(E.6) consistency: OK")
for n in (0,61):
    nv,nh = nvnh(4880,2,n); a,c = ac(nv,nh)
    print(f"  N=2 class S, g=2, n={n} maximal punctures: n_v={nv}, n_h={nh}, a={a} ({float(a):.6e}), c={c} ({float(c):.6e}), a/N^3={float(a)/4880**3:.6f}")
    print(f"     2g-2+n={2*2-2+n} (T_N blocks = -chi), 3g-3+n={3*2-3+n} (SU(N) gauge groups = dim_C M_{{g,n}})")
# per-puncture increments
Nv=sp.symbols('N'); print("  per max puncture: dn_v =", sp.expand(sp.Rational(2,3)*Nv**3-sp.Rational(3,2)*Nv**2-Nv/6+1+Nv**2-1), " dn_h =", sp.expand(sp.Rational(2,3)*Nv**3-sp.Rational(2,3)*Nv))
print("  large-N: N=2 MN a~(g-1)N^3/3 =", (4880**3)/3, "; N=1 MN (BBBW 2.22, z=0, kappa=-1) a~9(g-1)N^3/32 =", 9*4880**3/32)
zs = sp.symbols('z'); expr = (1-9*zs**2-(1+3*zs**2)**sp.Rational(3,2))/(48*zs**2)
print("  BBBW(2.22) kappa=-1: |z|=1 ->", sp.simplify(-expr.subs(zs,1)), "; z->0 ->", sp.limit(-expr, zs, 0))
# --- 5. Representation counts
C = math.comb
print("dim L^4(R^7) =", C(7,4), "= dim L^3(R^7); G2 split 1+7+27 =", 1+7+27, "(27 = dim S^2_0(R^7) =", 7*8//2-1, ")")
# SO(4)xSO(2)xR split of L^4 on R_y + T S4 + T Sigma  (1+4+2)
split = {}
for (a1,b4,c2) in itertools.product(range(2),range(5),range(3)):
    if a1+b4+c2==4: split[(a1,b4,c2)] = C(1,a1)*C(4,b4)*C(2,c2)
print("L^4(R^1+4+2) blocks (y,S4,Sigma degrees):", split, "sum", sum(split.values()))
print("L^4(R^6) =", C(6,4), "; L^3(R^6) =", C(6,3), "; 35-15 =", 35-15, "; dim SL(6)/SO(6) =", 35-15)
print("Lambda^4(R^8) =", C(8,4), "= L^4(R^7)+L^3(R^7) =", C(7,4)+C(7,3), "; Cremmer-Julia count 28+35+7 =", 28+35+7)
print("SL(5)/SO(5) =", 24-10, "; dim Sym^2_0(R^8) =", 36-1, "; dim SL(6) =", 35, "; dim SU(6) =", 35)
# SO(5)=Sp(4) Weyl dimension formula, Dynkin labels (a,b) (B2, a=long-root? use standard: dim=(a+1)(b+1)(a+b+2)(a+2b+3)/6)
d = lambda a,b: (a+1)*(b+1)*(a+b+2)*(a+2*b+3)//6
irr = sorted({(d(a,b),(a,b)) for a in range(8) for b in range(8) if d(a,b)<=60})
print("SO(5) irreps dim<=60 (dim,(a,b)):", irr)
print("SO(5) irreps of dim 35:", [x for x in irr if x[0]==35])
# --- 6. Arithmetic of project numbers
print("floor(e^3*3^5) =", math.floor(math.e**3*3**5), "(", math.e**3*3**5, ")")
# --- 7. Cusped option: Sigma_{g,n} = H^2/Gamma, n cusps, Gauss-Bonnet: Area = 2 pi (2g-2+n) rho^2
nn = sp.symbols('n', nonnegative=True)
AreaC = 2*sp.pi*(2*g-2+nn)*rho**2
aDc = sp.simplify((sp.pi*(1/k)**3/(8*(G11/(volS4*AreaC)))).subs(k,kN))
print("cusped: a_D = c_D =", aDc, "; at g=2,n=61,N=4880:", sp.N(aDc.subs({g:2,nn:61,N:4880}),12),
      "; Area =", sp.N(AreaC.subs(k,kN).subs({g:2,nn:61,N:4880}),10), "lp^2 ; ratio to n=0:", sp.Rational(2*2-2+61,2*2-2))
