# Local-derived. LD-O3a/b/c candidate checks. Exact integer / rational arithmetic only.
import itertools
from fractions import Fraction
import cypari2
pari = cypari2.Pari()
print("== LD-O3a: quadratic characters chi_D with chi_D,23 trivial (unramified and chi_D(23)=+1)")
for D in [1, 140, -7, -20, 5, -4, 28, -35]:
    k = int(pari.kronecker(D, 23)); fd = int(pari.coredisc(D)) if D != 1 else 1
    print(f"D={D:5d}  fund.disc={fd:5d}  (D/23)={k:+d}  chi_D(-1)={int(pari.kronecker(D,-1)) if D!=1 else 1:+d}  ramified primes={[int(p) for p in pari.factor(abs(fd))[0]] if abs(fd)>1 else []}")
print("== LD-O3b C1 (standard): poles of Lambda(s)=xi(s)^2 prod_{i=1}^{23} xi(s-i)xi(s+i); xi has simple poles at 0,1")
shifts = [0,0] + [i for i in range(1,24)] + [-i for i in range(1,24)]   # factor xi(s - a): poles at s=a, a+1
pol = {}
for a in shifts:
    for s0 in (a, a+1): pol[s0] = pol.get(s0,0)+1
print("pole set =", min(pol), "..", max(pol), " total order =", sum(pol.values()), " orders at -23,0,1,24 =", pol[-23], pol[0], pol[1], pol[24])
print("functional eq: multiset of shifts symmetric under a -> -a (since xi(1-s)=xi(s)):", sorted(shifts)==sorted(-a for a in shifts))
print("== LD-O3b C2 (adjoint): principal SL2 in SO48 => ad = sum Sym^{2e}, e in exponents of D24")
ex = list(range(1,46,2)) + [23]
dimad = sum(2*e+1 for e in ex)
print("exponents:", ex, " sum(2e+1) =", dimad, " dim so(48) =", 48*47//2, " match:", dimad == 48*47//2)
sh2 = [j for e in ex for j in range(-e, e+1)]           # L^fin(s,1,Ad) = prod zeta(s+j)
pol2 = {}
for j in sh2:
    for s0 in (-j, 1-j): pol2[s0] = pol2.get(s0,0)+1
print("Ad: degree", len(sh2), " pole range", min(pol2), "..", max(pol2), " order at s=1:", pol2[1], " at s=0:", pol2[0], " total:", sum(pol2.values()))
print("Ad symmetric shifts:", sorted(sh2)==sorted(-j for j in sh2))
print("== LD-O3c: maximal totally singular subspaces of nH over F_q, brute force vs prod_{i=0}^{n-1}(q^i+1)")
def rref_subspaces(n_amb, k, q):
    # enumerate k-dim subspaces of F_q^{n_amb} via RREF
    for piv in itertools.combinations(range(n_amb), k):
        free = [(r,c) for r in range(k) for c in range(n_amb) if c > piv[r] and c not in piv]
        for vals in itertools.product(range(q), repeat=len(free)):
            M = [[0]*n_amb for _ in range(k)]
            for r in range(k): M[r][piv[r]] = 1
            for (r,c),v in zip(free, vals): M[r][c] = v
            yield M
def count_mts(n, q):
    N = 2*n  # coordinates (x1,y1,...,xn,yn), Q = sum x_i y_i, B(u,v)=sum u_x v_y + u_y v_x
    Q = lambda v: sum(v[2*i]*v[2*i+1] for i in range(n)) % q
    Bf = lambda u,v: sum(u[2*i]*v[2*i+1]+u[2*i+1]*v[2*i] for i in range(n)) % q
    c = 0
    for M in rref_subspaces(N, n, q):
        if all(Q(r)==0 for r in M) and all(Bf(M[a],M[b])==0 for a in range(n) for b in range(a+1,n)): c += 1
    return c
for (n,q) in [(1,3),(2,3),(2,5),(3,3),(2,7)]:
    f = 1
    for i in range(n): f *= q**i+1
    b = count_mts(n,q); print(f"n={n} q={q}: brute={b} formula={f} match={b==f}")
q = 23; tot = 1
for i in range(24): tot *= q**i+1
one = tot//2
codex = 2
for i in range(1,24): codex *= q**i+1
print("#OG(24,48)(F23) = prod_{i=0}^{23}(23^i+1): digits", len(str(tot)), " equals Codex 2*prod_{i=1}^{23}(23^i+1):", tot == codex, " one family:", one == codex//2)
vol = Fraction(1) - Fraction(1, q**24)
for i in range(1,24): vol *= (1 - Fraction(1, q**(2*i)))
print("vol(K23) (canonical, |SO(F23)| q^-dim) = (1-23^-24) prod(1-23^-2i) ~", float(vol), " 1/vol ~", float(1/vol), " ; Siegel density 2*vol ~", float(2*vol))
print("1/vol == Codex?", 1/vol == codex, " 1/(2vol) == Codex?", 1/(2*vol) == codex)
