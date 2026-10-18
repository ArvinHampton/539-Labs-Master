# Audit check 2: Theorem 2, E_R lattice coefficients from scratch vs (sqrt35/140) sum_chi w_chi sum_{nk=N} bhat(n) acheck(k).
# Also: exact recognition of every coefficient as A + B*phi (phi = golden ratio), A,B integers, on both sides.
import math, cmath, numpy as np, common as C, mpmath as mp
mp.mp.dps = 20
QMAX = 100; NMAX = 140*QMAX
lat = C.ER_coeffs(QMAX)
cR = np.zeros(NMAX+1, complex)
z10 = [cmath.exp(-2j*math.pi*k/10) for k in range(10)]      # phase stored as (-(m.a)*10) mod 10 -> e(ph/10)
for N, cnt in lat.items():
    cR[N] = sum(cnt[p]*cmath.exp(2j*math.pi*p/10) for p in range(10))
form = np.zeros(NMAX+1, complex)
for key, c in C.chars().items():
    bh = np.array([complex(x) for x in c.bh]); ah = np.array([complex(x) for x in c.ach]); w = complex(c.w)
    for n in range(1, NMAX+1):
        if abs(bh[n % 140]) < 1e-12: continue
        k = np.arange(1, NMAX//n+1)
        form[n*k] += w*bh[n % 140]*ah[k % 20]
form *= math.sqrt(35)/140
dev = np.abs(cR-form)[1:].max()
odd = [N for N in range(1, NMAX+1) if N % 2 and abs(cR[N]) > 1e-9]
phi = (1+math.sqrt(5))/2
def recog(v):
    # v real in Z[phi]? solve v = A + B phi using conjugate unknown -> brute over small B
    for B in range(-400, 401):
        A = v - B*phi
        if abs(A-round(A)) < 1e-7: return (round(A), B)
    return None
bad = 0; nz = 0; maxim = 0
for N in range(1, NMAX+1):
    if abs(cR[N]) < 1e-9 and abs(form[N]) < 1e-9: continue
    nz += 1; maxim = max(maxim, abs(cR[N].imag), abs(form[N].imag))
    r1 = recog(cR[N].real); r2 = recog(form[N].real)
    if r1 is None or r1 != r2: bad += 1
out = [f"Theorem 2 vs lattice (from-scratch enumeration of nu in F cap A^-1 Z^2), N <= {NMAX} (Q <= {QMAX}):",
       f"  max_N |c_R(N/140) - formula(N)| = {dev:.2e}; nonzero coefficients: {nz}; max |Im| either side: {maxim:.1e}",
       f"  odd N with nonzero coefficient: {len(odd)} (all frequencies lie in (2/140)Z, consistent with 140Q = 2(-7m1^2+14m1m2-2m2^2))",
       f"  coefficients recognised as A+B*phi with identical (A,B) on both sides: {nz-bad}/{nz}",
       "  first 12 (N: lattice | formula): " + "; ".join(f"{N}: {cR[N].real:+.10f} | {form[N].real:+.10f}" for N in [n for n in range(1,NMAX+1) if abs(cR[n])>1e-9][:12])]
# I1 check: E_L(tau) = sum_chi w_chi G_chi(tau/20): coefficientwise, lattice count at 20Q=n vs sum_chi w_chi lambda_chi(n)
el = C.EL_coeffs(QMAX)
NL = 20*QMAX
lamtot = np.zeros(NL+1, complex)
for key, c in C.chars().items():
    a = np.array([complex(x) for x in c.a]); b = np.array([complex(x) for x in c.b]); w = complex(c.w)
    for m in range(1, NL+1):
        if a[m % 20] == 0: continue
        k = np.arange(1, NL//m+1); lamtot[m*k] += w*a[m % 20]*b[k % 140]
devL = max(abs(el.get(n, 0)-lamtot[n]) for n in range(1, NL+1))
out.append(f"I1 check: lattice E_L coefficients (nu in F cap (a+Z^2), 20Q=n<= {NL}) vs sum_chi w_chi (a*b)(n): max dev {devL:.2e}; nonzero: {sum(1 for n in el if el[n])}")
print("\n".join(out)); open("check_thm2.txt", "w").write("\n".join(out)+"\n")
