"""R4: rigorous tail bound.  For d >= D0, every even term not covered by a good block satisfies
   log e_n <= sqrt(d) F(alpha,u_c) + log 2 + g(u_c)        (Chernoff + Lemma T1, any u_c>0)
and a central odd term satisfies
   log o*  >= sqrt(d) Psi_low - C*(d)                      (local CLT at its saddle + Lemma T2)
 F(alpha,u) = alpha*Phi1(u) + (1-alpha^2) u/(7 alpha),   Phi1(u) = (1/2)[int_0^1 log(1+e^{-uy})dy + int_1^2 -log(1-e^{-uy})dy]
 g(u) = -log(1-e^{-u}).
Lemma T1 (upper): log A_n(e^{-u/n}) <= n Phi1(u) + log 2 + g(u).
Lemma T2 (lower): log A_n(e^{-u/n}) >= n Phi1(u) - (1/2)log 2 - g(u).
"""
import sys, json, math
from mpmath import iv, mp
iv.prec = 60
I = iv.mpf; ONE = I(1)
from clt import constants

def Phi1(u, Q=250):
    """enclosure of Phi1 over interval u (integrands monotone in y; interval evaluation per y-cell)."""
    A = I(0); B = I(0)
    for i in range(Q):
        y = I([i, i+1])/Q
        A += iv.log(ONE+iv.exp(-u*y))/Q
        y2 = ONE + I([i, i+1])/Q
        B += -iv.log(ONE-iv.exp(-u*y2))/Q
    return (A+B)/2

def F(alpha, u):
    return alpha*Phi1(u) + (ONE-alpha**2)*u/(7*alpha)

def g(u): return -iv.log(ONE-iv.exp(-u))

def Psi_low(alpha):
    """lower bound of inf_{u>0} F(alpha,u) for alpha interval within [0.3,0.6]"""
    assert alpha.a >= 0.3 and alpha.b <= 0.6
    best = None
    u = 0.02
    while u < 10:
        ub = u*1.004 if u > 0.1 else u+0.0005
        val = F(alpha, I([u, ub])).a
        best = val if best is None else min(best, val)
        u = ub
    # u<=0.02: F >= (alpha/2) log(1/(2u)) >= 0.15*log(25) = 0.48 ; u>=10: F >= (1-0.36)*10/(7*0.6) = 1.52
    return min(best, 0.48)

def _phi1f(u, Q=200):
    A=sum(math.log1p(math.exp(-u*(i+.5)/Q)) for i in range(Q))/Q
    B=sum(-math.log1p(-math.exp(-u*(1+(i+.5)/Q))) for i in range(Q))/Q
    return (A+B)/2
def argmin_u(alpha):
    f = lambda u: alpha*_phi1f(u)+(1-alpha**2)*u/(7*alpha)   # float search only picks u_c; bound is rigorous for any u_c
    lo, hi = 1e-4, 30.0
    for _ in range(60):
        m1 = lo+(hi-lo)*0.382; m2 = lo+(hi-lo)*0.618
        if f(m1) < f(m2): hi = m2
        else: lo = m1
    return lo

if __name__ == '__main__':
    N1 = int(sys.argv[1]); UA = float(sys.argv[2]); UB = float(sys.argv[3]); delta = float(sys.argv[4])
    log_eta_t = math.log(float(sys.argv[5])) if len(sys.argv) > 5 else math.log(1e-6)
    CA = constants(UA, UA, N1, 0.5); CB = constants(UB, UB, N1, 0.5)
    alpha1 = 1/math.sqrt(1+7*float(CA['M_lo'])); alpha1 = float((ONE/iv.sqrt(ONE+7*I(CA['M_lo']))).b)  # conservative (upper) end
    alpha2 = float((ONE/iv.sqrt(ONE+7*I(CB['M_hi']))).a)  # conservative (lower) end
    D0 = math.ceil((N1/alpha1)**2)
    sD = math.sqrt(D0)
    print('alpha1 (good-base lower edge)=', alpha1, ' alpha2=', alpha2, ' D0=(N1/alpha1)^2 =', D0)
    # central odd: alpha* in [0.438, 0.438+14/sqrt(D0)]
    a_star = I([0.438, 0.438+14/sD])
    rho = (ONE/a_star**2 - 1)/7
    Cs1 = constants(0.5, 0.5, N1, 0.5); Cs2 = constants(0.75, 0.75, N1, 0.5)
    assert Cs1['M_lo'] >= rho.b and Cs2['M_hi'] <= rho.a, 'u* not in [0.5,0.75]'
    Shi = constants(0.5, 0.75, N1, 0.5)['S_hi']
    PsiL = Psi_low(a_star)
    print('Psi_low(alpha*) >=', PsiL, ' (closed-form c = 0.3985400286...)')
    def Cstar(sd):
        nstar = 0.45*sd
        return float((iv.log(I(2))/2 + g(I(0.5)) + iv.log(2*iv.pi)/2 + 1.5*iv.log(I(nstar)) + iv.log(I(Shi))/2 - iv.log(ONE-I(delta))).b)
    # tail alpha-boxes
    boxes = []
    a = 0.005; top = alpha1 + 7/sD
    while a < top - 1e-12:
        b = min(a+0.0025, top); boxes.append((a, b)); a = b
    a = alpha2
    while a < 1 - 1e-12:
        b = min(a+0.0025, 1.0); boxes.append((a, b)); a = b
    worst = -1e9; worst_box = None; max_gap = -1e9
    for (a, b) in boxes:
        uc = argmin_u((a+b)/2)
        Fu = F(I([a, b]), I(uc)).b
        gap = float(Fu) - PsiL
        max_gap = max(max_gap, gap)
        val = sD*gap + float(g(I(uc)).b)
        if val > worst: worst, worst_box = val, (a, b, uc, float(Fu))
    # tiny alpha (0, 0.005]: F <= (alpha/2)(0.0541 - 2 log alpha + 5.25 alpha^2) <= 0.0267 ; g <= log(d/3.5)+1
    tiny_gap = 0.0267 - PsiL
    T = math.log(sD) + math.log(2) + max(worst, sD*tiny_gap + math.log(D0/3.5) + 1) + Cstar(sD) - log_eta_t
    print('max tail gap (F_up - Psi_low) =', max_gap, ' must be <= -2.5/sqrt(D0) =', -2.5/sD)
    print('worst tail box', worst_box, ' T(D0) =', T, '(must be <= 0)')
    ok = (max_gap <= -2.5/sD) and (tiny_gap <= -2.5/sD - 2/sD) and T <= 0
    print('R4 verified:', ok)
    fl=lambda x: float(x.b) if hasattr(x,'b') else float(x)
    json.dump(dict(N1=N1, UA=UA, UB=UB, alpha1=alpha1, alpha2=alpha2, D0=D0, PsiL=float(PsiL.a) if hasattr(PsiL,'a') else float(PsiL), max_gap=fl(max_gap), T=fl(T), ok=bool(ok),
                   worst_box=worst_box), open(f'tails_N{N1}_{UA}_{UB}.json', 'w'), indent=1)
