# Independent implementation (double precision) of the (I3) split-path period formula
#   Psi(z) = -(1/pi) [ (z/sqrt35)(log eps/2 - J_R(z)) + J_L(-1/z) ],  J_u(z) = int_{i}^{i inf} [u, R_z^{1/2}],
# with u_L, u_R built from scratch over all four regions F, -F, T, -T (gamma-fundamental cones [e1,g e1), [f,g f)).
import numpy as np, math, cmath
from scipy.special import k0, k1
from scipy.integrate import quad
LOGEPS = math.log(6+math.sqrt(35))
def regions_mask(n1, n2):
    """n = nu scaled by an integer; returns masks for F, -F, T, -T (half-open cones)."""
    F  = (2*n1+n2 > 0) & (n2 >= 0)
    T  = (11*n1+6*n2 > 0) & (n1+n2 <= 0)
    mF = (-2*n1-n2 > 0) & (-n2 >= 0)
    mT = (-11*n1-6*n2 > 0) & (-n1-n2 <= 0)
    return F | mF | T | mT
def fourier_L(Qmax=8.0, B=40):
    i, j = np.meshgrid(np.arange(-B, B+1), np.arange(-B, B+1), indexing='ij')
    X = 7+10*i.ravel(); Y = -2+10*j.ravel()            # 10 nu
    m = regions_mask(X, Y)
    X, Y = X[m], Y[m]
    q = (2*X*X+14*X*Y+7*Y*Y)/200.0
    k = np.abs(q) <= Qmax
    return agg(q[k], np.ones(k.sum(), complex)), 0.0
def fourier_R(Qmax=8.0, B=420):
    i, j = np.meshgrid(np.arange(-B, B+1), np.arange(-B, B+1), indexing='ij')
    m1 = i.ravel(); m2 = j.ravel()
    X = -7*m1+7*m2; Y = 7*m1-2*m2                      # 35 nu
    msk = regions_mask(X, Y) & ~((m1 == 0) & (m2 == 0))
    m1, m2 = m1[msk], m2[msk]
    q = 2*(-7*m1*m1+14*m1*m2-2*m2*m2)/140.0
    k = np.abs(q) <= Qmax
    ph = np.exp(-2j*np.pi*((7*m1[k]-2*m2[k]) % 10)/10)
    return agg(q[k], ph), LOGEPS
def agg(q, c):
    key = np.round(q*140).astype(np.int64)
    u, inv = np.unique(key, return_inverse=True)
    cs = np.zeros(len(u), complex); np.add.at(cs, inv, c)
    return u/140.0, cs
def u_data(F, t):
    (q, c), c0 = F
    a = 2*np.pi*np.abs(q); K0 = k0(a*t); K1 = k1(a*t); st = math.sqrt(t)
    u = st*(c0+np.sum(c*K0))
    ux = st*np.sum(c*2j*np.pi*q*K0)
    uy = c0/(2*st)+np.sum(c*(K0/(2*st)-st*a*K1))
    return u, 0.5*(ux-1j*uy)
def J(F, z, tmax=400.0):
    def integrand(t):
        u, uw = u_data(F, t)
        R = t/(t*t+z*z); v = np.sqrt(complex(R))
        vwb = 0.5/v*1j/(2*(-1j*t-z)**2)
        return 1j*(uw*v-u*vwb)
    # split [1,tmax] adaptively + analytic-ish tail for the constant term (only c0 survives for t>tmax)
    pts = sorted({1.0, tmax} | ({abs(z.imag)} if 1 < abs(z.imag) < tmax else set()))
    tot = 0j
    for lo, hi in zip(pts[:-1], pts[1:]):
        re = quad(lambda t: integrand(t).real, lo, hi, limit=400, epsabs=1e-15, epsrel=1e-14)[0]
        im = quad(lambda t: integrand(t).imag, lo, hi, limit=400, epsabs=1e-15, epsrel=1e-14)[0]
        tot += re+1j*im
    c0 = F[1]
    if c0:
        Fc = ((np.zeros(0), np.zeros(0, complex)), c0)      # constant term only (K0 terms < e^-100 beyond tmax)
        def ig(t):
            u, uw = u_data(Fc, t); R = t/(t*t+z*z); v = np.sqrt(complex(R)); vwb = 0.5/v*1j/(2*(-1j*t-z)**2)
            return 1j*(uw*v-u*vwb)
        gs = lambda s: ig(1/s)/s**2
        re = quad(lambda s: gs(s).real, 1e-300, 1/tmax, epsabs=1e-16, limit=200)[0]
        im = quad(lambda s: gs(s).imag, 1e-300, 1/tmax, epsabs=1e-16, limit=200)[0]
        tot += re+1j*im
    return tot
FL = FR = None
def Psi_period(z):
    global FL, FR
    if FL is None: FL, FR = fourier_L(), fourier_R()
    z = complex(z)
    return -(1/math.pi)*((z/math.sqrt(35))*(LOGEPS/2-J(FR, z))+J(FL, -1/z))
