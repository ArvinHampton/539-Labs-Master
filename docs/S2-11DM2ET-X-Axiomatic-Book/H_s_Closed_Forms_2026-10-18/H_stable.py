# Path B: s-stable two-variable form.  For s -> oo the cone boundary k > (s-8)n/(3s) becomes k >= ceil(n/3) and wall terms move to infinity:
#   Hcal(x, y) = sum_{n>=1} sum_{k>=ceil(n/3)} x^{n^2} (y^{nk + k(k+1)/2} - y^{nk + k(k-1)/2}) + 1/2 sum_{k>=1} (y^{k(k+1)/2} - y^{k(k-1)/2}).
# Claim (case analysis): H_s(q) = Hcal(q, q^s) up to (excluding) the first exponent where
#   (i) a boundary term differs: n with s(n - 3j) < 8n, j = ceil(n/3) - 1 (extra k = j), or 3 | n ... (handled exactly below), or
#   (ii) a wall term appears: n = m * 3s/g.
import math, sys
from fractions import Fraction as Fr
from collections import defaultdict
sys.path.insert(0, '.')
from H_zwegers import H_closed, Qs
def H_stab(s, N):
    h = defaultdict(Fr)
    n = 1
    while n*n <= N + 10*s:
        k = -(-n//3)
        while True:
            e1 = Qs(s, n, k); e2 = e1 - s*k
            if min(e1, e2) > N: break
            if e1 <= N: h[e1] += 1
            if e2 <= N: h[e2] -= 1
            k += 1
        n += 1
    for k in range(1, 10*int(math.sqrt(N)) + 5):
        if s*k*(k+1)//2 <= N: h[s*k*(k+1)//2] += Fr(1, 2)
        if s*k*(k-1)//2 <= N: h[s*k*(k-1)//2] -= Fr(1, 2)
    return {e: v for e, v in h.items() if v != 0}
def predicted_first(s):
    g = math.gcd(24, s-8); best = None
    for n in range(1, 400):
        j = -(-n//3) - 1
        # extra boundary point k = j present in H_s but not in Hcal iff 3sj > (s-8)n
        if 3*s*j > (s-8)*n and j >= 1 and not (3*s*j == (s-8)*n):
            e = min(Qs(s, n, j), Qs(s, n, j) - s*j); best = e if best is None else min(best, e)
        # Hcal includes k = ceil(n/3) but H_s requires 3sk > (s-8)n (always true for k >= n/3 when s > 0 since 3sk >= sn > (s-8)n) -> no missing points
        if ((s-8)*n) % (3*s) == 0 and (s-8)*n != 0:
            kn = (s-8)*n//(3*s); e = min(Qs(s, n, kn), Qs(s, n, kn) - s*kn); best = e if best is None else min(best, e)
    return best
if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
    out = []
    for s in list(range(9, 41)) + [41, 50, 64, 80, 100]:
        a = H_closed(s, N); b = H_stab(s, N)
        diff = sorted(set(a) ^ set(b) | {e for e in set(a) & set(b) if a[e] != b[e]})
        first = diff[0] if diff else None; pf = predicted_first(s)
        ok = (first == pf) or (first is None and (pf is None or pf > N))
        out.append(f"s={s}: first exponent where H_s != Hcal(q,q^s): {first}; predicted {pf}; agree {ok}")
    out.append("(s = 5..8 excluded: for s < 8 the cone admits k <= 0 rows and the stable form is not the right comparison; the exact cone closed form H_closed covers them.)")
    out.append("first terms of Hcal(q, y=q^s): " + str(sorted(H_stab(1000, 4500).items())[:14]) + "   (s=1000: exponents a*s + b)")
    open('H_stable.txt', 'w').write("\n".join(out) + "\n"); print("\n".join(out))
