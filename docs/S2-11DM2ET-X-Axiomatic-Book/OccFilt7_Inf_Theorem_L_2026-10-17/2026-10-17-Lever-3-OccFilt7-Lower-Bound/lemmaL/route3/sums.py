"""
Rigorous sum enclosures (Lemma S):
 (odd)  sum_{odd j<=n} f(j)        = (1/2) int_0^n f  + e,  |e| <= TV_{[0,n+1]} f + (1/2) sup_{[0,n+1]}|f|
 (int)  sum_{k=floor(n/2)+1}^{n} f(k) = int_{n/2}^{n} f + e, |e| <= TV_{[n/2,n+1]} f + sup_{[n/2,n+1]}|f|
Proof: each odd j is the midpoint of [j-1,j+1]; these tile [0,2N], 2N in {n,n+1}; |f(j)-(1/2)int_{j-1}^{j+1}f| <= TV on that
interval. Integers k in [K1,n] are midpoints of [k-1/2,k+1/2] tiling [K1-1/2,n+1/2]; K1-1/2-n/2 in {0,1/2}.
With f(x) = x^p F(c u x / n), x = n y:  sum = n^{p+1}[ J + e'/n ],  J = (1/2)int_0^1 y^p F(cuy)dy  resp. int_{1/2}^1,
|e'| <= TV_y + (1/2 or 1) sup_y   (TV, sup over y in [0,1+1/n1] resp. [1/2, 1+1/n1]).
TV_y <= sum_i Delta_i * sup|f'| on subinterval (f' enclosed by interval arithmetic).
"""
from mpmath import iv
iv.prec = 100
I = iv.mpf; ONE = I(1)

def p_(z): return ONE/(ONE+iv.exp(z))
# (F, F') pairs as functions of z
def Fv(z):
    p = p_(z); v = p*(ONE-p); return v, -v*(ONE-2*p)
def Fp(z):
    p = p_(z); v = p*(ONE-p); return p, -v
def F3(z):
    p = p_(z); v = p*(ONE-p); return v*(ONE-2*p), -v*((ONE-2*p)**2 - 2*v)
def F4(z):
    p = p_(z); v = p*(ONE-p); return p*p*(ONE-p), -(2*p-3*p*p)*v
def Gh(z):
    w = iv.exp(-z); return w/(ONE-w)**2, -w*(ONE+w)/(ONE-w)**3
def G3(z):
    w = iv.exp(-z); return w*(ONE+w)/(ONE-w)**3, -w*(ONE+4*w+w*w)/(ONE-w)**4
def Gm(z):
    w = iv.exp(-z); return w/(ONE-w), -w/(ONE-w)**2

def enclose(F, p, c, u, ya, yb, n1, Q=300, half=True):
    """enclosure of (1/n^{p+1}) * sum, for all n>=n1, u in interval u.
       half=True: odd-j sum over y in (0,1]; half=False: integer-k sum over y in (1/2,1]."""
    J = I(0); TV = I(0); SUP = I(0)
    yend = I(yb) + ONE/I(n1)
    # integral part over [ya,yb]
    for i in range(Q):
        y = I(ya) + (I(yb)-I(ya))*I([i, i+1])/Q
        f, fp = F(c*u*y)
        val = y**p*f
        J += val*(I(yb)-I(ya))/Q
    # TV and sup over [ya, yb+1/n1]
    for i in range(Q):
        y = I(ya) + (yend-I(ya))*I([i, i+1])/Q
        f, fp = F(c*u*y)
        val = y**p*f
        der = (p*y**(p-1)*f if p > 0 else I(0)) + y**p*c*u*fp
        dy = (yend-I(ya))/Q
        TV += dy*I(max(abs(der.a), abs(der.b)))
        SUP = I(max(SUP.b, abs(val.a), abs(val.b)))
    if half:
        J = J/2; err = TV + SUP/2
    else:
        err = TV + SUP
    e = err/I(n1)
    return I([(J-e).a, (J+e).b])
