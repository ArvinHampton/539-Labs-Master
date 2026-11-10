# FROZEN 2026-11-09 for MR2 batch-2 candidate resolutions (OW b0b9ae7f). Read-only computation; writes nothing but stdout.
# MR2 batch2 §10 check: P-Phi-a (Phi := G.G = 144 R on-shell, K1) evaluated on MN N=2 (z=1) uplift.
# Independent sympy Ricci scalar; control = (D) product inside same ansatz (expect R = 6).
import sympy as sp, mpmath as mp, time
mp.mp.dps = 40
t,x1,x2,x3,r,x,y,al,be,p1,p2 = sp.symbols('t x1 x2 x3 r x y alpha beta phi1 phi2', real=True)
X = [t,x1,x2,x3,r,x,y,al,be,p1,p2]
X1,X2,F,Gs,a1,a2 = sp.symbols('X1 X2 F Gs a1 a2', positive=True)
X0 = (X1*X2)**-2
m0, m1, m2 = sp.cos(al), sp.sin(al)*sp.cos(be), sp.sin(al)*sp.sin(be)
Dl = X0*m0**2 + X1*m1**2 + X2*m2**2
n = 11
g = sp.zeros(n)
w = Dl**sp.Rational(1,3)
for i,c in enumerate([t,x1,x2,x3,r]):
    g[i,i] = w*F/r**2*(-1 if i==0 else 1)
g[5,5] += w*Gs/y**2; g[6,6] += w*Gs/y**2
v = sp.Rational(1,4)*Dl**sp.Rational(-2,3)
# dmu terms in (alpha,beta)
dm = [[sp.diff(m,al), sp.diff(m,be)] for m in (m0,m1,m2)]
Xs = [X0,X1,X2]
for a in range(3):
    for i in range(2):
        for j in range(2):
            g[7+i,7+j] += v*dm[a][i]*dm[a][j]/Xs[a]
# (dphi_i + a_i dx/y)^2 terms
for (idx,mu,Xi,ai) in ((9,m1,X1,a1),(10,m2,X2,a2)):
    c = v*mu**2/Xi
    g[idx,idx] += c; g[idx,5] += c*ai/y; g[5,idx] += c*ai/y; g[5,5] += c*ai**2/y**2
def ricci_scalar_at(gm, subs, ptsubs):
    gm = gm.subs(subs)
    dep = [4,6,7,8]
    G0 = sp.Matrix(gm).subs(ptsubs)
    G0 = mp.matrix([[mp.mpf(sp.N(G0[i,j],45)) for j in range(n)] for i in range(n)])
    D1 = {c: mp.matrix([[mp.mpf(sp.N(sp.diff(gm[i,j],X[c]).subs(ptsubs),45)) for j in range(n)] for i in range(n)]) for c in dep}
    D2 = {(c,d): mp.matrix([[mp.mpf(sp.N(sp.diff(gm[i,j],X[c],X[d]).subs(ptsubs),45)) for j in range(n)] for i in range(n)]) for c in dep for d in dep}
    gi = G0**-1
    def dg(c,a,b): return D1[c][a,b] if c in dep else 0
    def ddg(c,d,a,b): return D2[(c,d)][a,b] if (c in dep and d in dep) else 0
    # Gamma_{m a b} (lowered) and derivatives
    Gl = [[[ (dg(b,m,a)+dg(a,m,b)-dg(m,a,b))/2 for b in range(n)] for a in range(n)] for m in range(n)]
    dGl = {c: [[[ (ddg(c,b,m,a)+ddg(c,a,m,b)-ddg(c,m,a,b))/2 for b in range(n)] for a in range(n)] for m in range(n)] for c in dep}
    dgi = {c: -gi*D1[c]*gi for c in dep}
    Gam = [[[ mp.fsum(gi[l,m]*Gl[m][a][b] for m in range(n)) for b in range(n)] for a in range(n)] for l in range(n)]
    def dGam(c,l,a,b):
        if c not in dep: return 0
        return mp.fsum(dgi[c][l,m]*Gl[m][a][b] + gi[l,m]*dGl[c][m][a][b] for m in range(n))
    R = 0
    for a in range(n):
        for b in range(n):
            if abs(gi[a,b]) < mp.mpf(10)**-35: continue
            Rab = mp.fsum(dGam(c,c,a,b) for c in dep) - mp.fsum(dGam(b,c,a,c) for c in range(n))
            Rab += mp.fsum(Gam[c][c][d]*Gam[d][a][b] - Gam[c][b][d]*Gam[d][a][c] for c in range(n) for d in range(n))
            R += gi[a,b]*Rab
    return R
pts = [(sp.Rational(1,3),sp.Rational(2,7)),(sp.Rational(7,10),sp.Rational(11,10)),(sp.Rational(3,2),sp.Rational(1,5)),(sp.Rational(1,100000),sp.Rational(3,4)),(sp.pi/2-sp.Rational(1,100000),sp.Rational(1,100000)),(sp.pi/2-sp.Rational(1,100000),sp.pi/2-sp.Rational(1,100000))]
def run(name, subs):
    vals=[]
    for (A,B) in pts:
        val = ricci_scalar_at(g, subs, {r:sp.Rational(13,10), y:sp.Rational(17,10), al:A, be:B})
        Dv = sp.N(Dl.subs(subs).subs({al:A,be:B}),30)
        vals.append((A,B,val,Dv))
        print(f"  alpha={sp.N(A,8)} beta={sp.N(B,8)}  R={mp.nstr(val,25)}  Delta={Dv}  R*Delta^(2/3)={mp.nstr(val*mp.mpf(Dv)**(mp.mpf(2)/3),25)}", flush=True)
    return vals
print("== control: (D) product in-ansatz X1=X2=1, a=0, F=4/9, Gs=1/6 (expect R=6) ==")
run("D", {X1:1,X2:1,a1:0,a2:0,F:sp.Rational(4,9),Gs:sp.Rational(1,6)})
print("== MN N=2: X1=2^(-3/5), X2=2^(2/5), F=e^{2f0}=2^(-4/5), Gs=2^(1/5)/4, a1=1, a2=0 ==")
run("MN2", {X1:2**sp.Rational(-3,5),X2:2**sp.Rational(2,5),a1:1,a2:0,F:2**sp.Rational(-4,5),Gs:2**sp.Rational(1,5)/4})
ell2 = (2*(sp.pi*4880)**sp.Rational(1,3))**2
print("ell^2/l_p^2 =", sp.N(ell2,15), " ; Phi_phys = 144 R_uplift / ell^2 (l_p units)")
L5 = sp.N(2**sp.Rational(-2,5),20)
print("MN2 L5 (uplift)=e^{f0}*Delta^{1/6}? -> constant-frame L5 = e^{f0} =", L5, "; 1728/L5^2 =", sp.N(1728/L5**2,15), "; 576/L5^2 =", sp.N(576/L5**2,15))
print("== cross-check vs MR2 V2/global-curvature log: BBBW z=2 at (alpha,beta)=(2/9,7/5), expect R = 5.920430303374412362900232 ==")
zz = sp.Integer(2)
X1z = ((1+7*zz+7*zz**2+33*zz**3-(1+4*zz+19*zz**2)*sp.sqrt(1+3*zz**2))/(4*zz*(1-zz)**2))**sp.Rational(1,5)
X2z = X1z*(2*zz+sp.sqrt(1+3*zz**2))/(1+zz)
X0z = (X1z*X2z)**-2
subz = {X1:X1z, X2:X2z, a1:(1+zz)/2, a2:(1-zz)/2, F:X0z**-2, Gs:(X1z*X2z/8)*((1-zz)*X1z+(1+zz)*X2z)}
print("  X1(z=2) =", sp.N(X1z,12), " X2 =", sp.N(X2z,12))
for (rr,yy) in ((sp.Rational(13,10),sp.Rational(17,10)),(sp.Rational(1,3),sp.Rational(5,1))):
    val = ricci_scalar_at(g, subz, {r:rr, y:yy, al:sp.Rational(2,9), be:sp.Rational(7,5)})
    print(f"  r={rr} y={yy}: R = {mp.nstr(val,25)}")
print("== MN2: AdS/H2 point independence at (alpha,beta)=(1/3,2/7) ==")
subm = {X1:2**sp.Rational(-3,5),X2:2**sp.Rational(2,5),a1:1,a2:0,F:2**sp.Rational(-4,5),Gs:2**sp.Rational(1,5)/4}
for (rr,yy) in ((sp.Rational(1,3),sp.Rational(5,1)),(sp.Rational(9,2),sp.Rational(1,7))):
    val = ricci_scalar_at(g, subm, {r:rr, y:yy, al:sp.Rational(1,3), be:sp.Rational(2,7)})
    print(f"  r={rr} y={yy}: R = {mp.nstr(val,25)}")
print("== MN2 scan of Phi_uplift = 144 R over (alpha,beta) grid (9x9, offsets 1e-6 from poles) ==")
import itertools
lo = mp.mpf('1e-6'); vals=[]
for i,j in itertools.product(range(9),range(9)):
    A = sp.Rational(1,10**6) + (sp.pi/2*0 + sp.pi - sp.Rational(2,10**6))*sp.Rational(i,8) if False else sp.Rational(1,10**6)+(sp.pi-sp.Rational(2,10**6))*sp.Rational(i,8)
    B = sp.Rational(1,10**6)+(sp.pi/2-sp.Rational(2,10**6))*sp.Rational(j,8)
    vals.append((ricci_scalar_at(g, subm, {r:1, y:1, al:A, be:B}), i, j))
Rmin = min(vals); Rmax = max(vals)
e2 = mp.mpf(sp.N(ell2,40))
print(f"  R_uplift min = {mp.nstr(Rmin[0],15)} at grid {Rmin[1:]}, max = {mp.nstr(Rmax[0],15)} at grid {Rmax[1:]}")
print(f"  Phi_phys = 144 R/ell^2: min = {mp.nstr(144*Rmin[0]/e2,12)}  max = {mp.nstr(144*Rmax[0]/e2,12)}  ratio max/min = {mp.nstr(Rmax[0]/Rmin[0],12)}  (l_p^-2)")
k2 = 1/(mp.mpf(sp.N(ell2,40))*mp.mpf(2)**(mp.mpf(-4)/5))
print(f"  k^2 := 1/L5^2 (L5 = ell e^(f0)) = {mp.nstr(k2,12)} ; EH-lock Phi/1728 range = [{mp.nstr(144*Rmin[0]/e2/1728,12)}, {mp.nstr(144*Rmax[0]/e2/1728,12)}]")
print("  Phi not constant on MN2 => 'k^2 = Phi/1728' with one constant k cannot hold pointwise; ratio k^2/(Phi/1728) range:",
      mp.nstr(k2/(144*Rmax[0]/e2/1728),10), "to", mp.nstr(k2/(144*Rmin[0]/e2/1728),10))
print("== cross-check (corrected coordinates: s_a = tan(alpha/2), s_b = tan(beta/2), per MR2 symbolic script header) ==")
Az = 2*sp.atan(sp.Rational(2,9)); Bz = 2*sp.atan(sp.Rational(7,5))
val = ricci_scalar_at(g, subz, {r:1, y:1, al:Az, be:Bz})
Dz = mp.mpf(sp.N(Dl.subs(subz).subs({al:Az,be:Bz}),40))
print(f"  z=2 at s_a=2/9, s_b=7/5: R = {mp.nstr(val,25)} ; Delta = {mp.nstr(Dz,25)} ; expected (MR2 V2 log) R = 5.920430303374412362900232, Delta = 1.370287024671496606663092")
print("  |difference| =", mp.nstr(abs(val-mp.mpf('5.920430303374412362900232')),5))
