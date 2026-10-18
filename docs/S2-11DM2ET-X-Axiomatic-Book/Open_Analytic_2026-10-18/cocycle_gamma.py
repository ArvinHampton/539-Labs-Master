# Item (5): numerical test of the E-part cocycle at gamma' with c != 0 (s = 7 data of the 2026-10-17 psi-cocycle report).
#   gamma'_{j,k} = T^{-k} [[1,0],[140 j,1]] T^k   (trivial multiplier on u_L; c = 140 j, d = 1 + 140 j k, cusp r = -k - 1/(140 j)).
#   Claim (Lewis-Zagier/Stokes, see report sec. 4):  kappa_L(x) - |cx+d|^{-1} kappa_L(gamma' x) = -(1/pi) * Jfull(x),
#   Jfull(x) = int_r^{i inf} [u_L, R_x^{1/2}].  For k = 0 the path is split at 0 and mapped by S (u_L o S = u_R/sqrt35, u_R(w+70) = u_R(w)):
#   int_0^{i inf}[u_L,R_x] = J_L(x) - J_R(-1/x)/(sqrt35|x|);  int_{-1/140j}^0 [u_L,R_x] = (1/(sqrt35|x|)) int_0^{i inf}[u_R, R_{-1/x-140j}],
#   int_0^{i inf}[u_R,R_z] = J_R(z) - (sqrt35/|z|) J_L(-1/z);  J(z) = int_i^{i inf} (tabulated Bessel series, as in psi_period.py).
#   For k != 0: Jfull_{j,k}(x) = e(-13k/20) Jfull_{j,0}(x+k)  (u_L(w-k) = e(-13k/20) u_L(w)).
import sys, math, cmath, json
sys.path.insert(0, '../2026-10-17-psi-cocycle')
from fractions import Fraction as Fr
import psi_period as PP
from fastkappa import cone_terms, a, zero
S35 = math.sqrt(35)
D = PP.D2
def JL(z): return PP.J(D[2], D[0], D[1], z)
def JR(z): return PP.J(D[3], D[0], D[1], z)
def I0R(z): return JR(z) - S35/abs(z)*JL(-1/z)
def Jfull(x, j, k=0):
    if k: return cmath.exp(-2j*math.pi*13*k/20)*Jfull(x + k, j, 0)
    A = JL(x) - JR(-1/x)/(S35*abs(x))
    B = I0R(-1/x - 140*j)/(S35*abs(x))
    return A + B
def kL(x): return cone_terms(a, zero, Fr(x))[1]
def lhs(x, j, k=0):
    c = 140*j; d = 1 + 140*j*k; aa = 1 - 140*j*k; bb = -140*j*k*k
    gx = (aa*x + bb)/(c*x + d)
    return kL(x) - kL(gx)/abs(float(c*x + d)), float(c*x + d)
if __name__ == "__main__":
    xs = [Fr(1), Fr(1, 2), Fr(1, 3), Fr(2, 3), Fr(3, 7), Fr(5, 4), Fr(-1, 3), Fr(-2, 5), Fr(-1, 100), Fr(-1, 200), Fr(-3, 500), Fr(-1, 7)]
    out = []
    for (j, k) in ((1, 0), (-1, 0), (2, 0), (1, 1)):
        for x in xs:
            if (140*j*x + 1 + 140*j*k) == 0: continue
            c_ = 140*j; d_ = 1 + 140*j*k; gx_ = ((1 - 140*j*k)*x - 140*j*k*k)/(c_*x + d_)
            if Fr(gx_).denominator > 4000: continue   # memory limit of the exact kappa code
            L, cxd = lhs(x, j, k)
            R = -Jfull(float(x), j, k)/math.pi
            row = dict(j=j, k=k, x=str(x), cx_d=cxd, lhs=[L.real, L.imag], pred=[R.real, R.imag], diff=abs(L - R),
                       diff_conj=abs(L - R.conjugate()))
            out.append(row); print(json.dumps(row), flush=True)
    json.dump(out, open('cocycle_gamma.json', 'w'), indent=0)
