# Audit check 4 (double precision): growth of the Herglotz side and of the period-formula continuation in the
# Lemma-8 strip S = {1 <= Re z <= 141, Im z <= -1}; and period formula vs Herglotz far into S.
import numpy as np, math, cmath, warnings, common as C, mpmath as mp
from scipy.special import psi as dig, zeta as hz
warnings.filterwarnings('ignore')
import period as P
CH = C.chars()
DAT = {}
for k, c in CH.items():
    DAT[k] = dict(a=np.array([complex(x) for x in c.a]), rho=np.array([complex(x) for x in c.rho]),
                  beta=[None]+[complex(c.beta(j)) for j in range(1, 16)], w=complex(c.w), mean=complex(c.mean))
def Rnp(d, z, K=15):
    M = 20*int(math.ceil(30*abs(z))); m = np.arange(1, M+1); am = d['a'][m % 20]; keep = am != 0
    m = m[keep]; am = am[keep]; X = m/(20*z)
    s = np.arange(1, 141); rho = d['rho'][s % 140]
    val = 0j
    for i0 in range(0, len(m), 4000):
        Xb = X[i0:i0+4000]
        val += np.sum(am[i0:i0+4000]*(dig(s[None, :]/140+Xb[:, None])*rho[None, :]).sum(1))
    r = np.arange(1, 21)
    for k in range(1, K+1):
        bk = d['beta'][k]
        if abs(bk) < 1e-14: continue
        if k == 1: tail = -np.sum(d['a'][r % 20]*dig((M+r)/20))/20
        else: tail = np.sum(d['a'][r % 20]*hz(k, (M+r)/20))/20**k
        val += (-1)**(k+1)*bk/k*(20*z)**k*tail
    return val
def herg(z): return 2*sum(d['w']*Rnp(d, z) for d in DAT.values())
out = []
for z in [3-3j, 10-10j, 20-40j]:
    h = herg(z); p = P.Psi_period(z)
    out.append(f"z={z}: Herglotz(double)={h:.13f}  period={p:.13f}  |diff|={abs(h-p):.1e}")
    print(out[-1], flush=True)
out.append("growth on S (|Psi| via Herglotz form; Lemma 8 claims <= C(1+|z|)^2):")
for x in (1.0, 71.0, 141.0):
    for Y in (1, 10, 100, 1000):
        z = complex(x, -Y); h = herg(z)
        Rmax = max(abs(Rnp(d, z)) for d in DAT.values())
        out.append(f"  z={x:5.0f}-{Y:4d}i |z|={abs(z):8.1f}  |Psi|={abs(h):.4e}  |Psi|/|z|={abs(h)/abs(z):.4e}  max_chi|R_chi|/|z|={Rmax/abs(z):.4e}")
        print(out[-1], flush=True)
open("growth.txt", "w").write("\n".join(out)+"\n")
