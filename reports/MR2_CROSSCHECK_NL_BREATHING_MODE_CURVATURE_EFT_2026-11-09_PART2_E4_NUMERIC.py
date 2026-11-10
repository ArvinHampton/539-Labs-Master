#!/usr/bin/env python3
# MR2 2026-11-09 cross-check PART2. The first script's (a2) step was killed (EXIT 137, out of memory) in the symbolic NumGeom build with exp(2 gamma beta(r)).
# This script redoes (a2) with a lightweight, self-contained numeric Ricci: mpmath dps 50, mp.diff derivatives of the analytic metric. It also runs (d).
# Controls: the (D) product inside the same metric function must give R = 6 (V2 log value); beta' = 0 must give R_r,chi = 0.
import mpmath as mp, time
mp.mp.dps = 50; T0 = time.time()
def P(s): print(s, flush=True)
X1 = mp.mpf(2)**(-mp.mpf(3)/5); X2 = mp.mpf(2)**(mp.mpf(2)/5)
def make_metric(X1, X2, F0, G0, a1, gam, b1, b2):
    X0 = 1/(X1*X2)**2
    def g(x):  # x = (r, v, al, be); 11 coords t,x1,x2,x3,r,u,v,al,be,p1,p2 (V2 cand_metric layout)
        r, v, al, be = x
        bet = b1*(r-1) + b2*(r-1)**2/2
        m = [mp.cos(al), mp.sin(al)*mp.cos(be), mp.sin(al)*mp.sin(be)]
        dm = [[-mp.sin(al), 0], [mp.cos(al)*mp.cos(be), -mp.sin(al)*mp.sin(be)], [mp.cos(al)*mp.sin(be), mp.sin(al)*mp.cos(be)]]
        Xs = [X0, X1, X2]
        D = sum(Xs[k]*m[k]**2 for k in range(3))
        G = mp.zeros(11, 11); w7 = mp.cbrt(D)*mp.exp(2*gam*bet)
        for i, s_ in enumerate([-1,1,1,1,1]): G[i,i] = w7*F0*s_/r**2
        G[5,5] = w7*G0/v**2; G[6,6] = w7*G0/v**2
        c = mp.exp(2*bet)*D**(-mp.mpf(2)/3)/4
        for i in range(2):
            for j in range(2):
                G[7+i,7+j] += c*sum(dm[k][i]*dm[k][j]/Xs[k] for k in range(3))
        for k,(ph,ai) in enumerate([(9,a1),(10,0)]):
            fac = c*m[k+1]**2/Xs[k+1]
            G[ph,ph] += fac; G[ph,5] += fac*ai/v; G[5,ph] += fac*ai/v; G[5,5] += fac*ai**2/v**2
        return G
    return g
DEP = [4, 6, 7, 8]
def ricci(gf, x):
    n = 11; x = [mp.mpf(z) for z in x]
    g = gf(x); gi = g**-1
    dg = {}; ddg = {}
    for a in range(4):
        def fa(z, a=a):
            y = list(x); y[a] = z; return gf(y)
        h = mp.mpf(10)**-12
        dg[DEP[a]] = (fa(x[a]+h) - fa(x[a]-h))/(2*h)  # O(h^2) ~1e-24, fine at dps 50
    for a in range(4):
        for b in range(a, 4):
            h = mp.mpf(10)**-8
            def gab(sa, sb):
                y = list(x); y[a] += sa*h; y[b] += sb*h; return gf(y)
            if a == b:
                val = (gf([x[i] + (h if i == a else 0) for i in range(4)]) - 2*g + gf([x[i] - (h if i == a else 0) for i in range(4)]))/h**2
            else:
                val = (gab(1,1) - gab(1,-1) - gab(-1,1) + gab(-1,-1))/(4*h**2)
            ddg[(DEP[a],DEP[b])] = val; ddg[(DEP[b],DEP[a])] = val
    Z = mp.zeros(n, n)
    d = lambda c: dg.get(c, Z)
    dd = lambda c, e: ddg.get((c, e), Z)
    # Christoffel of first kind Gam_{e b c} = 1/2 (d_b g_ec + d_c g_eb - d_e g_bc); derivative d_f Gam_{ebc}
    def G1(e, b, c_): return (d(b)[e,c_] + d(c_)[e,b] - d(e)[b,c_])/2
    def dG1(f, e, b, c_): return (dd(f,b)[e,c_] + dd(f,c_)[e,b] - dd(f,e)[b,c_])/2
    Gam = [[[sum(gi[a,e]*G1(e,b,c_) for e in range(n)) for c_ in range(n)] for b in range(n)] for a in range(n)]
    # d_f g^{ae} = -g^{ap} d_f g_pq g^{qe}
    dgi = {f: -gi*d(f)*gi for f in DEP}
    def dGam(f, a, b, c_):
        if f not in DEP: return 0
        return sum(dgi[f][a,e]*G1(e,b,c_) + gi[a,e]*dG1(f,e,b,c_) for e in range(n))
    def Ric(b, c_):
        s = 0
        for a in range(n):
            s += dGam(a, a, b, c_) - dGam(c_, a, b, a)
            for e in range(n):
                s += Gam[a][a][e]*Gam[e][b][c_] - Gam[a][c_][e]*Gam[e][b][a]
        return s
    return Ric, gi
# control: (D) product
gD = make_metric(mp.mpf(1), mp.mpf(1), mp.mpf(2)/3, mp.mpf(1)/6, 0, 0, 0, 0)
Ric, gi = ricci(gD, ['1', '1', '0.7', '0.4'])
Rs = sum(gi[i,j]*Ric(i,j) for i in range(11) for j in range(11) if gi[i,j] != 0)
P(f"control (D) product X=1,a=0,F0=2/3,G0=1/6 at (1,1,0.7,0.4): R = {mp.nstr(Rs,20)} (V2 log: 6)")
P("\n== (a2) NL E4 on V2 MN2 metric: 7D block x e^{2 gamma beta(r)}, S4 block (all c-terms incl. twist a1=1) x e^{2 beta(r)} ==")
F0 = X2**-2*0 + (X1*X2)**4  # X0^-2 with X0 = (X1 X2)^-2
G0 = X1*X2/8*(2*X2)        # z = 1: X1 X2/8 ((1-z)X1 + (1+z)X2)
P(f"MN2 params X1={mp.nstr(X1,12)} X2={mp.nstr(X2,12)} F0={mp.nstr(F0,12)} G0={mp.nstr(G0,12)} a1=1 a2=0")
X0 = 1/(X1*X2)**2
def dlnD(a_, b_):
    D = X0*mp.cos(a_)**2 + X1*(mp.sin(a_)*mp.cos(b_))**2 + X2*(mp.sin(a_)*mp.sin(b_))**2
    return (2*mp.sin(a_)*mp.cos(a_)*(-X0 + X1*mp.cos(b_)**2 + X2*mp.sin(b_)**2)/D,
            2*mp.sin(a_)**2*mp.sin(b_)*mp.cos(b_)*(X2 - X1)/D)
worst = 0
for (a_, b_) in [(mp.mpf('0.7'), mp.mpf('0.4')), (mp.mpf('2.01'), mp.mpf('1.1'))]:
    la, lb = dlnD(a_, b_)
    for gm in ['-1', '-0.5', '0', '0.5']:
        for (b1, b2) in [('0.5', '0.1'), ('-0.3', '0.7')]:
            gm_, b1_, b2_ = mp.mpf(gm), mp.mpf(b1), mp.mpf(b2)
            Ric, gi = ricci(make_metric(X1, X2, F0, G0, 1, gm_, b1_, b2_), [1, 1, a_, b_])
            ra = Ric(4,7)/(mp.mpf(3)/2*b1_*la); rb = Ric(4,8)/(mp.mpf(3)/2*b1_*lb)
            worst = max(worst, abs(ra-1), abs(rb-1))
            P(f"  (al,be)=({mp.nstr(a_,3)},{mp.nstr(b_,3)}) gamma={gm} beta'={b1} beta''={b2}: R_r,al/(1.5 beta' d_al lnD) = {mp.nstr(ra,15)} ; R_r,be/(1.5 beta' d_be lnD) = {mp.nstr(rb,15)}")
    Ric, gi = ricci(make_metric(X1, X2, F0, G0, 1, mp.mpf('0.5'), 0, mp.mpf('0.7')), [1, 1, a_, b_])
    P(f"  control beta'=0 (beta''=0.7) at ({mp.nstr(a_,3)},{mp.nstr(b_,3)}): R_r,al = {mp.nstr(Ric(4,7),3)}, R_r,be = {mp.nstr(Ric(4,8),3)}")
P(f"  max |ratio - 1| over all cases = {mp.nstr(worst,3)}")
P("\n== (d) EFT numbers at N=4880 (l_p = 1) ==")
N = 4880; ell = 2*(mp.pi*N)**(mp.mpf(1)/3)
P(f"  l = {mp.nstr(ell,10)}; L5 = l sqrt(F0) = {mp.nstr(ell*mp.sqrt(F0),10)}; l_p^2 R_max = 12/l^2 = {mp.nstr(12/ell**2,6)}; l_p^2 sqrt(Riem^2)_sup = sqrt(3408)/l^2 = {mp.nstr(mp.sqrt(3408)/ell**2,6)}")
P(f"  (l_p^2 sqrt Riem^2)^3 (R^4-vs-R relative size) = {mp.nstr((mp.sqrt(3408)/ell**2)**3,4)}")
P(f"  wall: k in [0.025358, 0.028464]/l_p => l_p k <= 0.0285 ; (l_p k)^2 = {mp.nstr(mp.mpf('0.028464')**2,4)}")
P(f"\nDONE {time.time()-T0:.0f}s")
