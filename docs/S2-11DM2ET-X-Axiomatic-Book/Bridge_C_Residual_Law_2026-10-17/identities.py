# Exact integer-series verification of the Bridge-C decomposition identities.
# All series are truncated at q^N (exponents 0..N); coefficients exact (Fractions for the 1/2's).
import sys, math
from fractions import Fraction as Fr
N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000

def zero(): return [Fr(0)]*(N+1)
def add(s, e, c=1):
    if 0 <= e <= N: s[e] += c
def sgn(x): return (x > 0) - (x < 0)
def sg(r): return 1 if r >= 0 else -1          # HM sg
Qs = lambda n,k: n*n + 7*n*k + Fr(7,2)*k*(k+1)  # Master Q_s = Q_plus
Qm = lambda n,k: n*n + 7*n*k + Fr(7,2)*k*(k-1)  # Q_minus = Q_plus(-n,-k)
B = int(4*math.isqrt(N) + 40)                   # box; enlarged-box rerun below confirms stability

def series_H(Bx):
    # Master: w(v) = 1/2(sgn B(c1,v) - sgn B(c2,v)), c1=(-1,1), c2=(-4,1), M=[[2,7],[7,7]]
    # B(c1,v) = 5n, B(c2,v) = -n-21k
    H = zero()
    for n in range(-Bx, Bx+1):
        for k in range(-Bx, Bx+1):
            w = Fr(sgn(5*n) - sgn(-n-21*k), 2)
            if w:
                e = Qs(n,k); assert e.denominator == 1
                if e <= N: H[int(e)] += w
    return H

P = zero()   # P_s = sum_{n,k>=0} q^{Q_s}
for n in range(0, B): 
    for k in range(0, B): add(P, int(Qs(n,k)))
H = series_H(B)
H2 = series_H(B+30)
assert H == H2, "box not large enough"
C = [P[i]-H[i] for i in range(N+1)]

Ct = zero()  # C_third = sum_{n,k>=1} q^{Q_minus}
for n in range(1,B):
    for k in range(1,B): add(Ct, int(Qm(n,k)))
R = zero()   # R = sum_{n>=0,k>=1} q^{Q_s}
for n in range(0,B):
    for k in range(1,B): add(R, int(Qs(n,k)))
th3 = zero(); 
for n in range(-B,B+1): add(th3, n*n)
psi7 = zero()  # sum_{k in Z} q^{7k(k+1)/2}
for k in range(-B,B+1): add(psi7, 7*k*(k+1)//2)
sq1 = zero()
for n in range(1,B): add(sq1, n*n)
tri1 = zero()
for k in range(1,B): add(tri1, 7*k*(k+1)//2)
# HM f_{2,7,7}(-q^10,-q^14,q) times q^8
F = zero()
for r in range(-B,B):
    for s in range(-B,B):
        if sg(r) == sg(s):
            e = 8 + r*(r-1) + 7*r*s + Fr(7,2)*s*(s-1) + 10*r + 14*s
            assert e.denominator == 1
            if e <= N: F[int(e)] += sg(r)
            # (-1)^{r+s} x^r y^s with x=-q^10,y=-q^14 gives q^{10r+14s} exactly
ThetaHol = zero()  # sum_{n>=1,k>=0} q^{Qm} - sum_{n<=0,k<=-1} q^{Qm}
for n in range(-B,B):
    for k in range(-B,B):
        if n>=1 and k>=0: add(ThetaHol, int(Qm(n,k)), 1)
        if n<=0 and k<=-1: add(ThetaHol, int(Qm(n,k)), -1)

one = zero(); one[0] = Fr(1)
def lin(*terms):
    out = zero()
    for c, s in terms:
        for i in range(N+1): out[i] += c*s[i]
    return out
Cmixed = [C[i]-lin((Fr(3,2),one),(1,sq1),(1,tri1),(1,Ct))[i] for i in range(N+1)]
checks = {
 "I1  C_mixed := C - C_axis - C_third vanishes through q^293 (Master claim)":
     all(Cmixed[i]==0 for i in range(294)),
 "I1b C_mixed is NOT identically zero: first nonzero coefficient is at q^294":
     Cmixed[294] != 0,
 "I2  C_third = q^8 f_{2,7,7}(-q^10,-q^14,q) + P_s":
     Ct == lin((1,F),(1,P)),
 "I3  Theta_hol = q^8 f_{2,7,7}(-q^10,-q^14,q) + theta_3":
     ThetaHol == lin((1,F),(1,th3)),
 "I4  C_third = Theta_hol - sum_{n>=1} q^{n^2} + R":
     Ct == lin((1,ThetaHol),(-1,sq1),(1,R)),
 "I5  C - C_third = -H_s - q^8 f_{2,7,7}(-q^10,-q^14,q)   (both residuals are the SAME P_s)":
     lin((1,C),(-1,Ct)) == lin((-1,H),(-1,F)),
 "I6  C_mixed = -H_s - q^8 f - 3/2 - sum_{n>=1}q^{n^2} - sum_{k>=1}q^{7k(k+1)/2}  (mock + unary only)":
     Cmixed == lin((-1,H),(-1,F),(Fr(-3,2),one),(-1,sq1),(-1,tri1)),
 "I7  C = P_s - H_s and P_s = R + (1+theta_3)/2":
     P == lin((1,R),(Fr(1,2),one),(Fr(1,2),th3)),
}
print(f"N = {N}, box B = {B} (rerun at B+30 identical for H_s)")
for k,v in checks.items(): print(("PASS " if v else "FAIL ")+k)
print("C coefficient value set through q^N:", sorted(set(C)))
print("C coefficient value set through q^293:", sorted(set(C[:294])))
print("first nonzero C_mixed (deg, coeff):", [(i,str(Cmixed[i])) for i in range(N+1) if Cmixed[i]][:12])
print("first C_third exponents:", [i for i in range(N+1) if Ct[i]][:14])
print("C_third coefficient max to N:", max(Ct))
