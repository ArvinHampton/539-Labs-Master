# PARI-free control: E_s coefficient at prime norms. For a pure genus (Eisenstein) theta series the count of cone points with
# N(a)=kappa*Q2 = p (p prime) depends only on p modulo the genus conductor; a cusp component makes it vary within residue classes.
from fractions import Fraction as Fr
import math, sympy
from collections import defaultdict
for s,kappa,mod in ((7,20,280*3),(8,3,48*5),(11,36,396*5)):
    a=(Fr(s,2*(s-2)),Fr(-1,s-2)); d=2*(s-2)
    Pmax=60000
    cnt=defaultdict(int)
    # nu = a + (n,k); cone [e1, gamma e1): nu2>=0 and 2 nu1 + nu2 > 0 ; Q2 = nu1^2 + s nu1 nu2 + s/2 nu2^2
    Qmax=Fr(Pmax,kappa)
    for k in range(0,400):
        nu2=a[1]+k
        if nu2<0: continue
        for n in range(-400,400):
            nu1=a[0]+n
            if not (2*nu1+nu2>0): continue
            Q=nu1*nu1+s*nu1*nu2+Fr(s,2)*nu2*nu2
            if Q>Qmax or Q<=0: continue
            N=kappa*Q
            if N.denominator==1 and sympy.isprime(int(N)): cnt[int(N)]+=1
    byres=defaultdict(set)
    for p in sympy.primerange(2,Pmax):
        if cnt.get(p,0) or True: byres[p%mod].add(cnt.get(p,0))
    mixed={r:v for r,v in byres.items() if len(v)>1}
    hit={r for r,v in byres.items() if max(v)>0}
    print(f"s={s}: primes p<{Pmax}; residues mod {mod} containing represented primes: {len(hit)}; residues with varying counts: {len(mixed)} e.g. {list(mixed.items())[:4]}")
