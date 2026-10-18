"""
Rigorous (interval-arithmetic) constants for the local CLT of a_n(m) = [x^m] A_n(x).
Tilted model at r = e^{-t}, t = u/n:  S = sum_{odd j<=n} B_j + sum_{k in (n/2,n]} G_k,
  B_j in {0,j}, P(B_j=j) = p_j = 1/(1+e^{jt});   G_k = 2k*Geom(w_k), w_k = e^{-2kt}.
P(S=m) = a_n(m) r^m / A_n(r)  (exact).
All bounds are uniform over u in [u_lo,u_hi] and integers n >= n1.  mpmath.iv, outward rounding.
"""
from mpmath import iv, mp
iv.prec = 100
I = iv.mpf
ONE = I(1)
PI = iv.pi

def E(z): return iv.exp(-z)
# Bernoulli functions of z = j t
def pB(z): return ONE/(ONE+iv.exp(z))
def vB(z):  # p(1-p), decreasing in z>=0
    p = pB(z); return p*(ONE-p)
def F3B(z):  # p(1-p)(1-2p), unimodal -> evaluate on interval
    p = pB(z); return p*(ONE-p)*(ONE-2*p)
def F4B(z):  # p^2(1-p), decreasing
    p = pB(z); return p*p*(ONE-p)
# geometric functions of z = 2 k t
def hG(z):   # w/(1-w)^2, decreasing
    w = E(z); return w/(ONE-w)**2
def G3(z):   # w(1+w)/(1-w)^3, decreasing
    w = E(z); return w*(ONE+w)/(ONE-w)**3
def mG(z):   # w/(1-w), decreasing
    w = E(z); return w/(ONE-w)

def hull(a, b): return I([min(a.a, b.a), max(a.b, b.b)])

def mono_dec(F, zlo, zhi):
    """enclosure of decreasing F over [zlo,zhi] (zlo,zhi point intervals)"""
    return I([F(zhi).a, F(zlo).b])

def oddsum(p, a, b, n1):
    """bounds for (1/n^{p+1}) sum_{odd j in (na,nb]} j^p, valid for all n>=n1"""
    a = I(a); b = I(b); n1 = I(n1)
    main = (b**(p+1)-a**(p+1))/(2*(p+1))
    lo = main - b**p/n1 - ONE/n1**(p+1)
    hi = main + (b+2/n1)**p/n1
    return max(lo.a, 0), hi.b

def intsum(p, a, b, n1):
    """bounds for (1/n^{p+1}) sum_{integer k in (na,nb]} k^p, valid for all n>=n1"""
    a = I(a); b = I(b); n1 = I(n1)
    main = (b**(p+1)-a**(p+1))/(p+1)
    lo = main - b**p/n1
    hi = main + (b+1/n1)**p/n1
    return max(lo.a, 0), hi.b

def constants(u_lo, u_hi, n1, tau0, P=None, Q=300):
    """rigorous bounds valid for all n>=n1, u in [u_lo,u_hi] (via Lemma S in sums.py):
       S_lo <= sigma^2/n^3 <= S_hi ; K3/n^4 <= k3 ; M_lo <= mu/n^2 <= M_hi"""
    from sums import enclose, Fv, Fp, F3, F4, Gh, G3, Gm
    u = I([u_lo, u_hi]); c3 = iv.cos(I(tau0)/2)**3
    sB = enclose(Fv, 2, 1, u, 0, 1, n1, Q, True)
    sG = 4*enclose(Gh, 2, 2, u, 0.5, 1, n1, Q, False)
    S = sB + sG
    k3B = enclose(F3, 3, 1, u, 0, 1, n1, Q, True)
    k3B4 = enclose(F4, 4, 1, u, 0, 1, n1, Q, True)
    k3G = 8*enclose(G3, 3, 2, u, 0.5, 1, n1, Q, False)
    # |F3| bound: F3>=0 for z>=0, so sum j^3 F3 <= upper enclosure
    k3 = (I(k3B.b) + I(tau0)*I(k3B4.b))/c3 + I(k3G.b)
    mB = enclose(Fp, 1, 1, u, 0, 1, n1, Q, True)
    mG = 2*enclose(Gm, 1, 2, u, 0.5, 1, n1, Q, False)
    M = mB + mG
    return dict(S_lo=S.a, S_hi=S.b, k3=k3.b, M_lo=M.a, M_hi=M.b)

def sinc_enc(z):
    """enclosure of sin(z)/z for z an interval in [0, 0.5]"""
    assert z.b <= 0.5 and z.a >= 0
    return I([(ONE - z.b**2/6).a, 1])

def minor_terms(u_lo, u_hi, n1, tau0, T, ntau=400, parity_cases=(0, 1)):
    """Bounds on the minor-arc contribution. Returns (rel1, rel2, rel3): the three regions'
       contributions to the relative error, i.e. sqrt(2 pi) sigma * (1/pi) * int e^{-B} (upper bound),
       valid for all n>=n1, u in [u_lo,u_hi]. Uses S_hi from constants."""
    ul = I(u_lo); uh = I(u_hi)
    v = vB(uh)            # v_j >= v(u) >= v(u_hi)  (j<=n => jt<=u)
    w = E(2*uh); lam = 4*w/(ONE-w)**2   # lambda_k >= lambda at w=e^{-2u}
    v = I(v.a); lam = I(lam.a)
    s = I([0, (ONE/n1).b])
    # Region 1: tau in [tau0, T]; collect (dtau, b_lower) boxes
    boxes = []
    edges = [tau0 + (T - tau0)*i/ntau for i in range(ntau+1)]
    # piecewise weights for the small-tau Taylor bound (tau <= TS)
    TS = 1.2
    Pm = 50
    pieces = []
    for i in range(1, Pm+1):
        a = I(i-1)/Pm; b = I(i)/Pm
        vlo = vB(I((uh*b).b)).a
        a2 = I(1)/2 + I(i-1)/(2*Pm); b2 = I(1)/2 + I(i)/(2*Pm)
        wl = E(I((2*uh*b2).b)); laml = (4*wl/(ONE-wl)**2).a
        pieces.append((I(vlo), oddsum(2, a, b, n1)[0], oddsum(4, a, b, n1)[1], I(laml),
                       intsum(2, a2, b2, n1)[0], intsum(4, a2, b2, n1)[1]))
    for i in range(ntau):
        tau = I([edges[i], edges[i+1]])
        if tau.b <= TS:
            # 1-cos x >= x^2/2 - x^4/24 ; sin^2 x >= x^2 - x^4/3 ; chord log(1+lam x)>= (x/X)log(1+lam X), x<=X=tau^2
            X = I(tau.b)**2
            tl = I(tau.a); th = I(tau.b)
            b = I(0)
            for (vl, o2, o4, laml, i2, i4) in pieces:
                s1 = tl**2/2*I(o2) - th**4/24*I(o4)
                s2 = tl**2*I(i2) - th**4/3*I(i4)
                b += vl*s1 + iv.log(ONE+laml*X)/X*s2/2
            boxes.append((edges[i+1]-edges[i], b.a))
            continue
        X = iv.sin(I(min(tau.b, float(PI.a)/2)))**2 if tau.b < float(PI.a)/2 else ONE
        X = I(X.b)
        chord = iv.log(ONE+lam*X)/X
        nsin = tau*sinc_enc(tau*s)
        bmin = None
        for par in parity_cases:
            if par == 0:
                Nn = I(1)/2; Ln = I(1)/2; a2N = tau; a2n1 = tau*(2+s); a2K1 = tau*(1+s)
            else:
                Nn = (1+s)/2; Ln = (1+s)/2; a2N = tau*(1+s); a2n1 = tau*(2+s); a2K1 = tau
            S1 = Nn - iv.sin(a2N)/(2*nsin)
            S2 = Ln/2 - (iv.sin(a2n1) - iv.sin(a2K1))/(4*nsin)
            b = v*S1 + chord*S2/2
            bmin = b.a if bmin is None else min(bmin, b.a)
        boxes.append((edges[i+1]-edges[i], bmin))
    # Region 2: theta in [T/n, pi - T/n]
    epsT = I(T)**2/(6*I(n1)**2)
    l1 = iv.log(ONE+lam)
    b2 = (v/2 + l1/8 - (v + l1/2)/(2*I(T)*(ONE-epsT))).a
    # Region 3: psi in [0,T] near theta=pi : B >= v*(N + sin(2N phi)/(2 sin phi))
    b3 = None
    edges3 = [T*i/ntau for i in range(ntau+1)]
    for i in range(ntau):
        psi = I([edges3[i], edges3[i+1]])
        if psi.b <= 0.5:
            val = (v*I(1)/2).a
        else:
            nsin = psi*sinc_enc(psi*s)
            val = None
            for par in parity_cases:
                Nn = I(1)/2 if par == 0 else (1+s)/2
                a2N = psi if par == 0 else psi*(1+s)
                bb = v*(Nn + iv.sin(a2N)/(2*nsin))
                val = bb.a if val is None else min(val, bb.a)
        b3 = val if b3 is None else min(b3, val)
    return boxes, b2, b3, float(v.a), float(lam.a)

def delta_bound(u_lo, u_hi, n1, tau0=None, T=12.0, P=40, verbose=False):
    """rigorous upper bound on the relative local-CLT error delta, valid for all n>=n1 and
       u in [u_lo,u_hi]:  |P(S=m) - g(x)| <= delta/(sqrt(2 pi) sigma),  g(x)=e^{-x^2/2s^2}/(sqrt(2pi)s)."""
    # choose tau0 by fixed point: need k3*tau0 <= 1.5*S_lo and tau0<=1
    tau = 1.0
    for _ in range(30):
        C = constants(u_lo, u_hi, n1, tau, P)
        tnew = min(1.0, 0.999*1.5*float(C['S_lo'])/float(C['k3']))
        if tnew >= tau*0.999 and tnew <= tau: tau = tnew; break
        tau = tnew if tnew < tau else tau
        if tnew >= tau: break
    if tau0 is not None: tau = min(tau, tau0)
    C = constants(u_lo, u_hi, n1, tau, P)
    assert float(C['k3'])*tau <= 1.5*float(C['S_lo']) and tau <= 1
    n = I(n1)
    S_lo = I(C['S_lo']); S_hi = I(C['S_hi']); k3 = I(C['k3'])
    D1 = 4*iv.sqrt(2*PI)/(3*PI) * k3/(S_lo**1.5*iv.sqrt(n))
    z = I(tau)*iv.sqrt(S_lo*n/2)
    D2 = iv.exp(-z*z)/(z*iv.sqrt(PI))      # erfc(z) <= e^{-z^2}/(z sqrt(pi))
    boxes, b2, b3, v, lam = minor_terms(u_lo, u_hi, n1, tau, T)
    pref = iv.sqrt(2*PI)*iv.sqrt(S_hi)/PI     # sqrt(2pi)*sigma/pi / n^{1.5}
    # region1: (1/n) sum dtau e^{-n b}  -> times n^{1.5}: sqrt(n) * sum dtau e^{-n b}; need n*b>=1/2 for monotonicity
    R1 = I(0); mono_ok = True
    for dt, b in boxes:
        if b*n1 < 0.5: mono_ok = False
        R1 += I(dt)*iv.sqrt(n)*iv.exp(-n*I(b))
    R2 = n**1.5*PI*iv.exp(-n*I(b2)) if b2 > 0 else I('inf')
    R3 = iv.sqrt(n)*I(T)*iv.exp(-n*I(b3))
    if b2*n1 < 1.5 or b3*n1 < 0.5: mono_ok = False
    D3 = pref*(R1+R2+R3)
    delta = D1 + D2 + D3
    out = dict(tau0=tau, S_lo=float(S_lo.a), S_hi=float(S_hi.b), k3=float(k3.b), D1=float(D1.b), D2=float(D2.b),
               D3=float(D3.b), delta=float(delta.b), mono_ok=mono_ok, b2=float(b2), b3=float(b3),
               bmin1=min(b for _, b in boxes), M_lo=float(C['M_lo']), M_hi=float(C['M_hi']))
    return out

if __name__ == '__main__':
    import sys
    for (ul, uh) in [(0.2, 0.21), (0.3, 0.31), (0.6, 0.61), (1.0, 1.01), (1.6, 1.61)]:
        for n1 in [1000, 2000]:
            r = delta_bound(ul, uh, n1); print(ul, uh, n1, {k: (round(v,5) if isinstance(v,float) else v) for k,v in r.items()})
