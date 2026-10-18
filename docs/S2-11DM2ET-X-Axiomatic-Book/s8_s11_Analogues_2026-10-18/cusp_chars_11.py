# s=11: character content of u_L at the minimal modulus m = p2*(9)*oo1*oo2 (Cl_m^+ = Z/24 x Z/2): the sigma-symmetrised
# indicator of S+ u S- is 2*(1_C + 1_{C+d}); content F^(chi) = conj(chi(C))(1+conj(chi(d)))/24 ... list the cusp characters.
import cypari2, itertools, numpy as np, math, cmath
from fractions import Fraction as Fr
pari=cypari2.Pari(); pari.allocatemem(10**9)
K=pari('bnfinit(x^2-11,1)'); w=pari('Mod(x,x^2-11)')
sig=[g for g in pari.nfgaloisconj(K) if str(g)!='x'][0]
P2=pari.idealprimedec(K,2)[0]; P3=pari.idealprimedec(K,3)[0]
mod=pari.idealmul(K,P2,pari.idealpow(K,P3,2))
bnr=pari.bnrinit(K,[mod,[1,1]],1); cyc=[int(z) for z in pari('(b)->b.cyc')(bnr)]
cl=lambda J: np.array([int(z) for z in pari.bnrisprincipal(bnr,J,0)])
Nm=int(pari.idealnorm(K,mod))
d=cl(pari.idealhnf(K,1-1000*Nm)); dpm=cl(pari.idealhnf(K,1+1000*Nm*w))
gens=pari('(b)->b.gen')(bnr)
Sg=np.array([cl(pari.nfgaloisapply(K,sig,g)) for g in gens]).T
C=np.array([22,0])
ev=lambda ch,x: cmath.exp(2j*math.pi*sum(c*v/m for c,v,m in zip(ch,x,cyc)))
print("Cl_m^+ =",cyc,"d =",d,"C =",C,"sigma(C) =",(Sg@C)%np.array(cyc), "d_{+-} =",dpm)
rows=[]
for ch in itertools.product(*[range(m) for m in cyc]):
    pure=abs(ev(ch,d)-1)<1e-9
    if not pure: continue
    inv=all(abs(ev(ch,(Sg@np.eye(len(cyc),dtype=int)[:,i])%np.array(cyc))-ev(ch,np.eye(len(cyc),dtype=int)[:,i]))<1e-9 for i in range(len(cyc)))
    typ='(1,1)' if abs(ev(ch,dpm)+1)<1e-9 else '(0,0)'
    f=pari.bnrconductor(bnr,list(ch))
    Fh=ev(ch,-C)*2/24*2/2   # content of 2(1_C+1_{C+d}) / |G| = (2/48)*conj chi(C)*(1+1)
    order=math.lcm(*[m//math.gcd(c,m) for c,m in zip(ch,cyc)]) if any(ch) else 1
    rows.append((ch,'Eis' if inv else 'cusp',typ,str(pari.idealfactor(K,f[0])).replace('\n',''),int(pari.idealnorm(K,f[0])),order,Fh))
for r in rows: print(f"  chi={r[0]} {r[1]:4s} type {r[2]} cond N={r[4]:4d} order {r[5]:2d}  content {r[6]:.4f}   cond={r[3]}")
cus=[r for r in rows if r[1]=='cusp']
print(f"pure-type characters: {len(rows)}; Eisenstein (sigma-inv) {len(rows)-len(cus)}; cusp {len(cus)} -> {len(cus)//2} dihedral Maass forms (sigma-pairs)")
