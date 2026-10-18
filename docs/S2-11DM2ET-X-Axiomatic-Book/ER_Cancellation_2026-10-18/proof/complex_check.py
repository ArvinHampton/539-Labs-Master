# (A) identity as holomorphic functions on Re z>0: Psi(z) = E_L(-1/z) - (z/sqrt35) E_R(z)  vs  (1/8) sum e(-j/8) R_{j,l}(z), z complex
# + 40 random rationals (denominators<=60, both signs; x<0 via psi(-x)=conj psi(x)) in double precision.
import numpy as np, math, cmath, random
from fractions import Fraction as Fr
import uvec, fastkappa
from herglotz import Herg, GEN
from family import G
e1=(1,0); ge1=tuple(G@np.array(e1))
def Evec(al70,be70,tau,Qmax):
    q,ph=uvec.cone_pts(np.array(al70),np.array(be70),e1,ge1,1,Qmax,Bx=120)
    return np.sum(ph*np.exp(2j*np.pi*q*tau))
a70=(49,-14); ma70=(-49,14)
reps=sorted({((-14*u+14*w)%70,(14*u-4*w)%70) for u in range(35) for w in range(35)})
def Psi(z):
    EL=Evec(a70,(0,0),-1/z,Qmax=60/(-1/z).imag)
    ER=sum(Evec(p,ma70,z,Qmax=60/z.imag) for p in reps)
    return EL-z/math.sqrt(35)*ER
H={k:Herg(k) for k in GEN}; w={k:cmath.exp(-2j*math.pi*k[0]/8)/8 for k in GEN}
def RR(z): return sum(w[k]*H[k].R(z) for k in GEN)
if __name__=="__main__":
  out=[]
  for z in [1+0.6j,0.5+0.4j,2+1j,1.3+0.25j,0.8+1.5j]:
      p=Psi(z); r=RR(z); out.append(f"z={z}: Psi(q-series)={p:.13f}  Herglotz={r:.13f}  |diff|={abs(p-r):.1e}")
      print(out[-1],flush=True)
  random.seed(1); rs=set()
  while len(rs)<40:
      q=random.randint(2,60); p=random.randint(-3*q,3*q)
      if p: rs.add(Fr(p,q))
  worst=0
  for x in sorted(rs):
      ex=fastkappa.psi(x) if x>0 else None
      if x<0:
          # psi_minus(x) = conj psi(|x|) (Cat A in the psi-cocycle report); compare Herglotz at |x| conjugated with exact negative-side kappa formula
          from fastkappa import cone_terms,a,zero,REPS,ma
          ex=cone_terms(a,zero,-1/x)[1]-abs(float(x))/math.sqrt(35)*sum(cone_terms(pp,ma,x)[1] for pp in REPS)
          r=RR(abs(float(x))).conjugate()
      else: r=RR(float(x))
      worst=max(worst,abs(ex-r))
  out.append(f"40 random rationals (denominators<=60, both signs): max |exact Bernoulli psi - Herglotz formula| = {worst:.2e}")
  print(out[-1]); open("complex_check.txt","w").write("\n".join(out)+"\n")
