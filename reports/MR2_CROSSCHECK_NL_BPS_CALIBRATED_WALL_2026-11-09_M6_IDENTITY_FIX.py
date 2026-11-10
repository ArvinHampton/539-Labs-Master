#!/usr/bin/env python3
# MR2 2026-11-09 addendum to MR2_CROSSCHECK_NL_BPS_CALIBRATED_WALL_2026-11-09.py (sha 11fdb72d...). In that run the [M6] identity check printed None
# (sympy is_zero_matrix undecided on unexpanded entries). Here: the same identity, entrywise expand to 0, several random G; plus B3 eigenvectors with g > 0.
import sympy as sp, random
def P(s): print(s, flush=True)
s0 = sp.Matrix([[1,0],[0,1]]); sx = sp.Matrix([[0,1],[1,0]]); sy = sp.Matrix([[0,-sp.I],[sp.I,0]]); sz = sp.Matrix([[1,0],[0,-1]])
def kron(*ms):
    out = ms[0]
    for m_ in ms[1:]: out = sp.kronecker_product(out, m_)
    return out
E = []
for k in range(5):
    E.append(kron(*([sz]*k + [sx] + [s0]*(4-k)))); E.append(kron(*([sz]*k + [sy] + [s0]*(4-k))))
E.append(kron(*[sz]*5)); Gam = [sp.I*E[0]] + E[1:]; eta = [-1] + [1]*10
up = lambda a: eta[a]*Gam[a]
def prod(idx):
    out = sp.eye(32)
    for i in idx: out = out*up(i)
    return out
def Gslash(Gc):
    out = sp.zeros(32)
    for idx, val in Gc.items(): out += 24*val*prod(idx)
    return out
def Gthree(Gc, a):
    out = sp.zeros(32)
    for idx, val in Gc.items():
        if a in idx:
            pos = idx.index(a); rest = idx[:pos] + idx[pos+1:]
            out += 6*((-1)**pos)*val*prod(rest)
    return out
import itertools
subs4 = list(itertools.combinations(range(4, 10), 4)); random.seed(11)
for trial in range(4):
    Gc = {c: random.randint(-5, 5) for c in subs4}; Gs = Gslash(Gc)
    lhs = sp.zeros(32)
    for a in range(4, 10): lhs += up(a)*(Gam[a]*Gs - 12*Gthree(Gc, a))
    D = (lhs + 6*Gs).applyfunc(sp.expand)
    P(f"  [M6] trial {trial}: max entry |sum_int Gamma^a(Gamma_a Gslash - 12 Gamma^cde G_acde) + 6 Gslash| = {max(abs(x) for x in D)} ; Gslash nonzero: {any(x != 0 for x in Gs.applyfunc(sp.expand))}")
# x-row check: for a in x directions (no x-legs in G), Gamma^{cde}G_{acde} = 0, so row is k_x Gamma_a eps = -sigma/144 Gamma_a Gslash eps
P("  [M6] x-row: G has no x-legs => Gthree(G, a in x) = 0:", all(Gthree({c: 1 for c in subs4}, a).is_zero_matrix for a in range(4)))
ph, la = sp.symbols('phi lambda', real=True); g = sp.symbols('g', positive=True); l = -1
W = g/2*(sp.exp(-2*ph)*(2*sp.exp(-6*la) + 3*sp.exp(4*la)) + l*sp.exp(-8*ph+6*la))
sub = {ph: sp.log(2)/30, la: sp.log(2)/10}
Lval = 3/sp.simplify(W.subs(sub))
HW = sp.Matrix([[sp.diff(W, a, b).subs(sub) for b in (ph, la)] for a in (ph, la)])
Ex = (HW*2/60*Lval).applyfunc(sp.simplify)
for e, m, v in Ex.eigenvects():
    P(f"  [M3] exponent x L = {sp.nsimplify(e)}, eigvec (dphi : dlam) = {[sp.nsimplify(sp.simplify(x/v[0][1])) for x in v[0]]}")
