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

def Psi_low(alpha, ulo=0.5, uhi=0.75, H=0.0005):
    """rev2: lower bound of inf_{u in [ulo,uhi]} F(alpha,u) (interval arithmetic, u-boxes of width H).
    Only u in [0.5,0.75] is needed: the central odd term's own saddle u* is certified to lie there
    (M_lo(0.5) >= rho*_max, M_hi(0.75) <= rho*_min, IVT), and log o* >= sqrt(d) F(alpha*,u*) - C*.
    No claim about u outside [ulo,uhi] is made or used."""
    best = None
    u = ulo
    while u < uhi - 1e-12:
        ub = min(u + H, uhi)
        val = F(alpha, I([u, ub])).a
        best = val if best is None else min(best, val)
        u = ub
    return best

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
    # rev2: every rigorous quantity below is an mpmath interval; decisions use the conservative endpoint.
    N1 = int(sys.argv[1]); UA = float(sys.argv[2]); UB = float(sys.argv[3]); delta = I(sys.argv[4])
    eta_t = I(sys.argv[5]) if len(sys.argv) > 5 else I('1e-6')
    CA = constants(UA, UA, N1, 0.5); CB = constants(UB, UB, N1, 0.5)
    alpha1 = (ONE/iv.sqrt(ONE+7*I(CA['M_lo']))).b    # conservative (upper) end, exact mpf
    alpha2 = (ONE/iv.sqrt(ONE+7*I(CB['M_hi']))).a    # conservative (lower) end, exact mpf
    D0 = int(mp.ceil(((I(N1)/alpha1)**2).b))
    sD = iv.sqrt(I(D0))                              # interval
    print('alpha1 =', alpha1, ' alpha2 =', alpha2, ' D0 = ceil((N1/alpha1)^2) =', D0)
    # central odd: alpha* in [0.438, 0.438+14/sqrt(D0)]  (upper end rounded outward)
    a_star = I([I('0.438').a, (I('0.438') + 14/sD).b])
    rho = (ONE/a_star**2 - 1)/7
    Cs1 = constants(0.5, 0.5, N1, 0.5); Cs2 = constants(0.75, 0.75, N1, 0.5)
    assert Cs1['M_lo'] >= rho.b and Cs2['M_hi'] <= rho.a, 'u* not in [0.5,0.75]'
    Shi = constants(0.5, 0.75, N1, 0.5)['S_hi']
    PsiL = Psi_low(a_star)
    print('Psi_low(alpha*) over u in [0.5,0.75] >=', PsiL, ' (closed-form c = 0.3985400286...)')
    def Cstar(sd):   # sd interval; n* <= 0.45 sqrt(d)
        nstar = I('0.45')*sd
        return (iv.log(I(2))/2 + g(I('0.5')) + iv.log(2*iv.pi)/2 + 1.5*iv.log(nstar) + iv.log(I(Shi))/2 - iv.log(ONE-delta))
    # tail alpha-boxes (edges exact mpf/float; first range covers [0.005, top], top rounded up)
    boxes = []
    top = (alpha1 + 7/sD).b
    a = I('0.005').a
    while a < top:
        b = min((a + I('0.0025')).b, top); boxes.append((a, b)); a = b      # exact point edges, contiguous
    a = alpha2
    while a < 1:
        b = min((a + I('0.0025')).b, I(1).a); boxes.append((a, b)); a = b
    assert all(boxes[i][1] == boxes[i+1][0] for i in range(len(boxes)-1) if boxes[i][1] != top)
    assert boxes[0][0] == I('0.005').a and any(bx[1] == top for bx in boxes) and boxes[-1][1] == 1
    worst = None; worst_box = None; max_gap = None
    for (a, b) in boxes:
        uc = argmin_u((float(I(a).a)+float(I(b).a))/2)   # float only picks u_c
        Fu = F(I([a, b]), I(uc))
        gap = (Fu - PsiL)                      # interval; upper end used
        max_gap = gap.b if max_gap is None else max(max_gap, gap.b)
        val = (sD*gap + g(I(uc))).b
        if worst is None or val > worst: worst, worst_box = val, (str(a), str(b), uc, str(Fu.b))
    # tiny alpha (0, 0.005]: F <= (alpha/2)(c0 - 2 log alpha + 5.25 alpha^2), c0 = 2 - log 2 - log 3.5 <= 0.0541;
    # increasing on (0,0.005], so F <= Ftiny := value at 0.005 <= 0.0267 ; g(u) <= log(d/3.5) + 1
    c0 = 2 - iv.log(I(2)) - iv.log(I('3.5')); assert c0.b <= 0.0541
    at = I('0.005'); Ftiny = (at/2)*(I('0.0541') - 2*iv.log(at) + I('5.25')*at**2)
    assert Ftiny.b <= 0.0267
    tiny_gap = (I('0.0267') - PsiL).b
    tiny_val = (sD*(I('0.0267') - PsiL) + iv.log(I(D0)/I('3.5')) + 1).b
    T = (iv.log(sD) + iv.log(I(2)) + I(max(worst, tiny_val)) + Cstar(sD) - iv.log(eta_t)).b
    thr = (-I('2.5')/sD).a; thr_tiny = (-I('4.5')/sD).a
    print('max tail gap (F_up - Psi_low) =', max_gap, ' must be <=', thr)
    print('tiny-alpha gap', tiny_gap, ' must be <=', thr_tiny)
    print('worst tail box', worst_box, ' T(D0) =', T, '(must be <= 0)')
    ok = bool(max_gap <= thr and tiny_gap <= thr_tiny and T <= 0)
    print('R4 verified:', ok)
    up = lambda x: math.nextafter(float(x), math.inf) if float(x) < x else float(x)
    dn = lambda x: math.nextafter(float(x), -math.inf) if float(x) > x else float(x)
    json.dump(dict(N1=N1, UA=UA, UB=UB, alpha1_up=up(alpha1), alpha2_down=dn(alpha2), D0=D0, PsiL_down=dn(PsiL),
                   max_gap_up=up(max_gap), T_up=up(T), ok=ok, worst_box=worst_box,
                   note='rev2: computed in mpf intervals; JSON floats rounded outward'),
              open(f'tails_N{N1}_{UA}_{UB}.json', 'w'), indent=1)
