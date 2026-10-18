"""Independent numerical check of Lemma 6.1 (Green-form lemma), mpmath quadrature written from scratch.
F_n(z) = int_z^{z+i oo} [T_n, R_z^{1/2}],  [u,v] = u_w v dw + u v_wbar dwbar,  T_n = sqrt(y) K0(2 pi |n| y) e(nx).
Also checks the closedness identity d[u,v] = (u_{w wbar} v - u v_{w wbar}) dwbar^dw numerically via the Laplacian."""
import mpmath as mp
mp.mp.dps = 30
def e(x): return mp.exp(2j*mp.pi*x)
def F(n, z):
    x0, y0 = mp.re(z), mp.im(z); a = 2*mp.pi*abs(n)
    def integrand(s):
        X, Y = x0, y0 + s; w = mp.mpc(X, Y)
        if n == 0:
            T = mp.sqrt(Y); TX = 0; TY = 1/(2*mp.sqrt(Y))
        else:
            k0 = mp.besselk(0, a*Y); k1 = mp.besselk(1, a*Y)
            T = mp.sqrt(Y)*k0*e(n*X); TX = 2j*mp.pi*n*T; TY = (k0/(2*mp.sqrt(Y)) - mp.sqrt(Y)*a*k1)*e(n*X)
        Tw = (TX - 1j*TY)/2
        # on the ray w = z + i s:  w - z = i s,  wbar - z = -i(2 y0 + s)  (written exactly to avoid cancellation)
        R = (y0 + s)/(s*(2*y0 + s))                # = Im w / ((w-z)(wbar-z)), real positive
        wbz = -1j*(2*y0 + s)
        v = mp.sqrt(R); vwb = mp.mpf(1)/2/mp.sqrt(R) * 1j/(2*wbz**2)
        return Tw*v*1j + T*vwb*(-1j)              # dw = i ds, dwbar = -i ds
    return mp.quad(integrand, [0, mp.mpf('1e-6'), 0.01, 0.1, 1, 10, mp.inf])
rows=[]
for z in [mp.mpc(0.3,0.8), mp.mpc(-0.17,0.45), mp.mpc(1.1,1.3)]:
    for n in [1, 2, 3, -1, -2]:
        val = F(n, z); ref = -mp.pi/2*e(n*z) if n > 0 else 0
        rows.append(f"z={mp.nstr(z,4)} n={n:+d}: F_n = {mp.nstr(val,18)}   expected {mp.nstr(ref,18)}   |diff| = {mp.nstr(abs(val-ref),3)}")
    val = F(0, z); rows.append(f"z={mp.nstr(z,4)} n= 0: int[sqrt y, R^1/2] = {mp.nstr(val,18)}  expected 1/2  |diff| = {mp.nstr(abs(val-0.5),3)}")
# Laplace eigenvalue of R_z^{1/2}: Delta = -y^2 (d_xx + d_yy), expect 1/4
z = mp.mpc(0.2, 0.7)
f = lambda X, Y: mp.sqrt(Y/((mp.mpc(X,Y)-z)*(mp.mpc(X,-Y)-z)))
X0, Y0 = mp.mpf('0.9'), mp.mpf('1.6')
lap = -Y0**2*(mp.diff(lambda X: f(X,Y0), X0, 2) + mp.diff(lambda Y: f(X0,Y), Y0, 2))
rows.append(f"Delta R_z^(1/2) / R_z^(1/2) at w=0.9+1.6i, z=0.2+0.7i: {mp.nstr(lap/f(X0,Y0),20)} (expected 1/4)")
print("\n".join(rows)); open("green_lemma_check.txt","w").write("\n".join(rows)+"\n")
