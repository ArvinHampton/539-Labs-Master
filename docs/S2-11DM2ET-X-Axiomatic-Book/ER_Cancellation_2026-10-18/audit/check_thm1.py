# Audit check 3: Theorem 1.  Herglotz side (from-scratch mpmath R_chi, 36 digits) against
#  (a) z in H: q-series E_L(-1/z) - (z/sqrt35) E_R(z) from from-scratch lattice enumeration (36 digits);
#  (b) Re z > 0, Im z <= 0: from-scratch split-path period formula (period.py, double precision);
#  (c) rationals x: exact Bernoulli/kappa value from the audited folder's predecessor code hp_check.psi_exact (34 digits; NOT independent code)
#      and the from-scratch period formula (double).
import sys, math, mpmath as mp, common as C
from fractions import Fraction as Fr
from multiprocessing import Pool
sys.dont_write_bytecode = True
mp.mp.dps = 36
def herg(z):
    return 2*mp.fsum(c.w*c.R(z) for c in C.chars().values())
def qseries(z):
    z = mp.mpc(z); tau = -1/z
    QL = 80/(2*math.pi*float(tau.imag))+1; QR = 80/(2*math.pi*float(z.imag))+1
    el = C.EL_coeffs(QL); er = C.ER_coeffs(QR)
    EL = mp.fsum(cnt*C.ee(mp.mpf(N)*tau/20) for N, cnt in el.items())
    ER = mp.fsum(mp.fsum(cnt[p]*C.ee(mp.mpf(p)/10) for p in range(10) if cnt[p])*C.ee(mp.mpf(N)*z/140) for N, cnt in er.items())
    return EL - z/mp.sqrt(35)*ER
H_PTS = ['1+0.6j', '0.5+0.4j', '2+1j', '0.8+1.5j', '1.3+0.25j', '-0.5+0.8j']
LOW = ['1-0.3j', '2-1j', '0.5-0.2j', '5-3j', '1.4142135623730951+0j']
RAT = [Fr(1), Fr(1,3), Fr(2), Fr(3,5), Fr(7,4), Fr(5,2), Fr(13,8), Fr(11,7)]
def job(item):
    mp.mp.dps = 36
    kind, v = item
    if kind == 'H':
        z = mp.mpc(complex(v)); h = herg(z); q = qseries(z)
        return f"[H]   z={v:12s} Herglotz={mp.nstr(h,22)}  q-series={mp.nstr(q,22)}  |diff|={mp.nstr(abs(h-q),3)}"
    if kind == 'L':
        import warnings; warnings.filterwarnings('ignore'); import period as P
        z = complex(v); h = herg(mp.mpc(z)); p = P.Psi_period(z)
        return f"[off-H] z={v:22s} Herglotz={mp.nstr(h,18)}  period(double)={p:.15f}  |diff|={abs(complex(h)-p):.1e}"
    if kind == 'R':
        import warnings, os; warnings.filterwarnings('ignore'); import period as P
        x = v; h = herg(mp.mpf(x.numerator)/x.denominator)
        here = os.getcwd(); os.chdir('../2026-10-18-ER-cancellation'); sys.path.insert(0, '.')
        import hp_check; mp.mp.dps = 36
        ex = hp_check.psi_exact(x); os.chdir(here)
        p = P.Psi_period(float(x))
        return f"[rat] x={str(x):5s} Herglotz={mp.nstr(h,25)}  exact-kappa={mp.nstr(ex,25)}  |diff|={mp.nstr(abs(h-ex),3)}  |period(double)-Herglotz|={abs(complex(h)-p):.1e}"
if __name__ == "__main__":
    items = [('H', v) for v in H_PTS] + [('L', v) for v in LOW] + [('R', x) for x in RAT]
    with Pool(7) as pool: out = pool.map(job, items)
    print("\n".join(out)); open("check_thm1.txt", "w").write("\n".join(out)+"\n")
