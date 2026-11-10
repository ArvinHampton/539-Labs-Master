# Local-derived. Joint-carrier candidates: Weil restriction Res_{Q(sqrt35)/Q}(49a1) ~ 49a1 x Xi.
# PARI 2.17.2 via cypari2, local only.
import cypari2
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
E  = pari('ellinit([1,-1,0,-2,-1])')
Xi = pari('ellinit(elltwist(ellinit([1,-1,0,-2,-1]),140))')
print("Xi a-invariants:", pari('elltwist(ellinit([1,-1,0,-2,-1]),140)'))
print("cond E =", pari.ellglobalred(E)[0], " cond Xi =", pari.ellglobalred(Xi)[0])
print("rootno E =", pari.ellrootno(E), " rootno Xi =", pari.ellrootno(Xi))
# (1) E and Xi become isomorphic over K = Q(sqrt 35): c4'/c4 = u^4, c6'/c6 = u^6 with u^2 in K^x2
c4, c6 = E[9], E[10]; c4x, c6x = Xi[9], Xi[10]
r4 = c4x/c4; r6 = c6x/c6
print("c4 ratio =", r4, " c6 ratio =", r6, " r6^2/r4^3 =", r6**2/r4**3)
d = r6/r4   # = u^2
print("u^2 = c6ratio/c4ratio =", d, " core(u^2) =", pari.core(pari.numerator(d)*pari.denominator(d)), "(35 => u^2 is a square in Q(sqrt35))")
# (2) Euler factors: over K, a_P for split p equals a_p(E)=a_p(Xi); for inert p, a_P = a_p(E)^2 - 2p and a_p(Xi) = -a_p(E)
K = pari('nfinit(y^2-35)')
EK = pari.ellinit([1,-1,0,-2,-1], K)
bad = {2,5,7}
nsplit = ninert = 0; ok = True
for p in pari.primes(400):
    p = int(p)
    if p in bad: continue
    chi = int(pari.kronecker(140, p))
    ap, apx = int(pari.ellap(E, p)), int(pari.ellap(Xi, p))
    if apx != chi*ap: ok = False; print("twist law fails at", p)
    dec = pari.idealprimedec(K, p)
    if chi == 1:
        nsplit += 1
        for P in dec:
            if int(pari.ellap(EK, P)) != ap: ok = False; print("split fail", p)
    else:
        ninert += 1
        P = dec[0]
        if int(pari.ellap(EK, P)) != ap*ap - 2*p: ok = False; print("inert fail", p)
print(f"primes 3..400 (p not in 2,5,7): split {nsplit}, inert {ninert}; all Euler-factor identities L(E/K)=L(E)L(Xi): {ok}")
# (3) minimal level: f (level 49) and f_Xi (level 19600) both occur in S2(Gamma0(N)) iff lcm | N
print("lcm(49,19600) =", pari.lcm(49,19600), " 19600 % 140 =", 19600 % 140, " 19600 % 980 =", 19600 % 980)
print("conductor of Res (= N(E) N(Xi)) =", 49*19600)
