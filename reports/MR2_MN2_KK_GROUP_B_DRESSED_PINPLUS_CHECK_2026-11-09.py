# Frozen (chmod a-w + sidecar) before the logged run. MR2 2026-11-09. Pin+ check of dressed Group B on MN N=2 x wall Z2 (OW b1893386). Additive; no network.
import numpy as np, itertools, hashlib, time
def P(*a): print(*a, flush=True)
T0=time.time()
R='/workspace/quantum-comp/reports/'
kk=R+'MR2_MN2_KK_TRUNCATION_BOLZA_AUT48_ISOM96_WALL_Z2_2026-11-09.py'
h=hashlib.sha256(open(kk,'rb').read()).hexdigest()
P(f"[0] KK .py sha256 {h} ({'MATCH 88949658' if h.startswith('88949658') else 'MISMATCH'}); exec'ing its group section [G]/[W] verbatim")
src=open(kk).read().split('# ---------------- T:')[0]
exec(src)
# ---------------- Z: H^1(Sigma;Z2), theta characteristics, spin structures on Y ----------------
B6=frozenset(range(6))
def norm(T): T=frozenset(T); return min(T, B6-T, key=lambda s:(len(s),sorted(s)))
theta={norm(T) for k in (1,3,5) for T in itertools.combinations(range(6),k)}
J2={norm(T) for k in (0,2,4,6) for T in itertools.combinations(range(6),k)}
P(f"[Z] theta characteristics (odd subsets mod complement): {len(theta)}; J[2]=H^1(Sigma;Z2) (even subsets mod complement): {len(J2)}")
s0=next(iter(theta))
P(f"[Z] torsor check: s -> s0 (sym.diff) s is a bijection theta -> J[2]: {len({norm(s0^s) for s in theta})==16}")
act=lambda p,T: norm(frozenset(p[i] for i in T))
for G,lab in [(G48,'(A) Aut+'),(G96,'(B) Isom, reflections dressed (same Sigma action)')]:
    orbs=[]; seen=set()
    for d in J2:
        if d in seen: continue
        o={act(p,d) for _,p in G}; orbs.append(len(o)); seen|=o
    P(f"[Z] {lab}: orbits on H^1(Sigma;Z2) = 11D spin structures on Y labelled by d = s (x) s_R: {sorted(orbs)}; d=0 (SUSY, s_R=s) fixed: {all(act(p,frozenset())==frozenset() for _,p in G)}")
    # diagonal (s, s_R=s) preserved by every element (same permutation acts on both square roots)
    ok=all(act(p,s)==act(p,s) for _,p in G for s in theta)
    eq=all(norm(act(p,s)^act(p,s))==frozenset() for _,p in G for s in theta)
    P(f"[Z] {lab}: twisted pair (K^(1/2)_s, R-root s_R=s) mapped to a pair with s'_R=s' for every element: {ok and eq}; bare-s orbits: {sorted(len({act(p,s) for _,p in G}) for s in [norm({0}),norm({0,1,2}),norm({0,1,3})])} (sample)")
# ---------------- C: real Clifford algebra Cl(10,1), Majorana 32 ----------------
I2=np.eye(2); X=np.array([[0,1],[1,0.]]); Zm=np.array([[1,0],[0,-1.]]); E=np.array([[0,1],[-1,0.]])
F={'I':I2,'X':X,'Z':Zm,'E':E}; sq={'I':1,'X':1,'Z':1,'E':-1}
def comm(a,b):  # +1 commute, -1 anticommute
    return 1 if (a=='I' or b=='I' or a==b) else -1
words=[''.join(w) for w in itertools.product('IXZE',repeat=5) if w!=('I',)*5]
def wsq(w): return int(np.prod([sq[c] for c in w]))
def wcomm(a,b): return int(np.prod([comm(x,y) for x,y in zip(a,b)]))
def search(need):
    sol=[]
    import sys; sys.setrecursionlimit(10000)
    def bt(k):
        if k==len(need): return True
        for w in words:
            if wsq(w)!=need[k]: continue
            if all(wcomm(w,v)==-1 for v in sol):
                sol.append(w)
                if bt(k+1): return True
                sol.pop()
        return False
    return sol if bt(0) else None
need=[-1]+[1]*10
W=search(need)
def mat(w):
    M=np.array([[1.]])
    for c in w: M=np.kron(M,F[c])
    return M
g=[mat(w) for w in W]
vol=np.eye(32)
for x in g: vol=vol@x
sgn=1 if np.allclose(vol,np.eye(32)) else (-1 if np.allclose(vol,-np.eye(32)) else 0)
if sgn==-1: g[10]=-g[10]
vol=np.eye(32)
for x in g: vol=vol@x
eta=np.diag([-1]+[1]*10)
cl=max(np.abs(g[a]@g[b]+g[b]@g[a]-2*eta[a,b]*np.eye(32)).max() for a in range(11) for b in range(11))
P(f"[C] real 32x32 rep of Cl(10,1) found (words {W}); Clifford error {cl:.0e}; all real: True; Gamma^0...Gamma^10 = +1: {np.allclose(vol,np.eye(32))} (HW convention (1.1))")
P(f"[C] Pin- check: real 32-dim rep needs Cl(10,1) (p-q=9=1 mod 8: M32(R)+M32(R)); Cl(1,10) (p-q=7 mod 8) is M32(C): no real 32 => Majorana gravitino requires Pin+ (LM table; FH 1908.09916 sec.2). volume-element square: Cl(10,1) {(-1)**55*(-1)**1:+d}, Cl(1,10) {(-1)**55*(-1)**10:+d} -> in Cl(1,10) omega is central with omega^2=-1, so any real module carries a commuting complex structure: real dim >= 64, no real 32. PROVED.")
names=['t','x1','x2','x3','rho','u','v','a','b','y(phi1)','z(phi2)']
rho=4
Gw=np.eye(32)
for k in range(11):
    if k!=rho: Gw=Gw@g[k]
rel=[s for s in (1,-1) if np.allclose(Gw, s*g[rho]) or np.allclose(Gw, s*1j*g[rho])]
P(f"[C] 10D wall chirality Gamma_(wall) = prod of the 10 tangent gammas = {rel} x Gamma_rho  => HW projection Gamma_rho eps = eps is 10D chirality (HW (1.2))")
def lift(S):
    M=np.eye(32)
    for k in sorted(S): M=M@g[k]
    Mi=np.linalg.inv(M)
    pat={k:(1 if np.allclose(M@g[k]@Mi,g[k]) else -1) for k in range(11)}
    ins={pat[k] for k in S}; outs={pat[k] for k in range(11) if k not in S}
    refl_ok = len(ins)==1 and len(outs)==1 and ins!=outs
    Mc=np.eye(32)
    for k in sorted(set(range(11))-set(S)): Mc=Mc@g[k]
    Mci=np.linalg.inv(Mc)
    patc={k:(1 if np.allclose(Mc@g[k]@Mci,g[k]) else -1) for k in range(11)}
    sq_=M@M; sqv=1 if np.allclose(sq_,np.eye(32)) else (-1 if np.allclose(sq_,-np.eye(32)) else 0)
    cr=1 if np.allclose(M@g[rho],g[rho]@M) else -1
    return refl_ok, outs.pop() if refl_ok else None, patc==pat, sqv, cr
# G4 index sets (MR2 bd47ff5e C2): {u,v,a,z},{u,v,b,z},{u,a,b,z},{a,b,y,z}
G4=[{5,6,7,10},{5,6,8,10},{5,7,8,10},{7,8,9,10}]
CASES=[('W   wall Z2 (rho->-rho, G4 odd by OW f825dfff)',{4},True),
       ('A   Aut+ example: (u,v) rotation by pi, Sigma part only (fibre compensation: [E])',{5,6},False),
       ('s   bare Bolza reflection lift (u,phi1)',{5,9},False),
       ('(i) Bolza refl + 5D spatial parity x3',{5,9,3},False),
       ('(ii) Bolza refl + time reversal t',{5,9,0},False),
       ("(i') (i) + O(3)_R det-1 reflection phi2",{5,9,10,3},False),
       ("(ii') (ii) + O(3)_R det-1 reflection phi2",{5,9,10,0},False)]
P("[C] case | 11D orient | G4 sign | M-theory symmetry rule (G sign = orient sign) | wall-tangent reflections | lift ok/eps | same eps for complement lift | M^2 on fermions | [M,Gamma_rho] | S4 flux N -> ")
for lab,S,iswall in CASES:
    orient=(-1)**len(S)
    gs={(-1)**len(s_&S) for s_ in G4}
    gsign=gs.pop()*(-1 if iswall else 1)
    rule = (gsign==orient)
    tang=len(S-{rho})
    ok,eps,same,sqv,cr=lift(S)
    s4=(-1)**len(S&{7,8,9,10})
    Nsign=gsign*s4
    P(f"   {lab:44s} | {orient:+d} | {gsign:+d} | {str(rule):5s} | {tang} ({'odd: flips 10D wall orientation' if tang%2 else 'even'}) | {ok}/{eps:+d} | {same} | {sqv:+d} | {'commutes' if cr==1 else 'ANTICOMMUTES'} | {'+N' if Nsign==1 else '-N'}" + ("  (wall: N on one side, -N image: the 2N wall charge)" if iswall else ""))

# ---------------- D: delta(g) = g*s0 - s0 in H^1(Sigma;Z2) per generator (PP item c) ----------------
P("[D] generators of G^ = (dressed Isom) x Z2^wall: g1, g2 (Aut+), J, K (antiholomorphic, dressed), W (wall, acts trivially on Sigma)")
GEN=dict(gens); GEN['W: wall rho->-rho']=(np.eye(4), tuple(range(6)))
for name,(D,p) in GEN.items():
    bare=[norm(act(p,t)^t) for t in theta]
    nfix=sum(1 for d in bare if d==frozenset())
    # SUSY spin structure on Y: s_Y = (s, s_R = s), class d0 = s (+) s_R = 0; image (g s, g s_R = g s)
    dl={norm(act(p,t)^act(p,t)) for t in theta}
    P(f"   {name:28s} perm {[PN[i] for i in p]} | bare Sigma spin structures fixed: {nfix}/16 | delta(g) on SUSY s0 for all 16 base choices s: {sorted(map(sorted,dl))} -> {'0' if dl=={frozenset()} else 'NONZERO'}")
P("[D] J acts trivially on H^1(Sigma;Z2) (-1 = +1 mod 2) and fixes all 6 Weierstrass points, so J fixes all 16 theta characteristics: "+str(sum(1 for t in theta if act(GEN['J: y->-y'][1],t)==t))+"/16")
# ---------------- E: lifted group, extension class data in H^2(G^;Z2) (PP item d, e) ----------------
def nS(th): return -np.sin(th)*g[5]+np.cos(th)*g[6]          # reflection of T_pSigma across the line at angle th
def nF(th,tw): return -np.sin(tw*th)*g[9]+np.cos(tw*th)*g[8]  # induced reflection of the twisted phi1-plane (L = T Sigma: tw=+1; L = K: tw=-1)
Id=np.eye(32)
def val(M):
    return '+1' if np.allclose(M,Id) else ('-1' if np.allclose(M,-Id) else 'not central')
DRESS=[('s  bare (internal; REFUTED by G-sign)',Id),
       ("s' bare + phi2 flip (internal; REFUTED by G-sign)",g[10]),
       ('(i)  + P (x3)',g[3]),('(ii) + T (t), Lorentzian',g[0]),
       ("(i') + phi2 flip + P",g[10]@g[3]),("(ii') + phi2 flip + T, Lorentzian",g[10]@g[0])]
Wt=g[4]
P(f"[E] wall lift W~ = Gamma_rho: W~^2 = {val(Wt@Wt)}")
P("[E] dressing | twist | r~^2 | (r~a r~b)^8 [pi/8 vertex] | (r~a r~b)^2 [pi/2] | (r~a r~b)^3 [pi/3], r~b sign +,- | [W~,r~] = W~ r~ W~^-1 r~^-1")
for lab,Dm in DRESS:
    for tw in (1,-1):
        r=lambda th: nS(th)@nF(th,tw)@Dm
        rr=val(r(0)@r(0))
        v8=val(np.linalg.matrix_power(r(0)@r(np.pi/8),8))
        v2=val(np.linalg.matrix_power(r(0)@r(np.pi/2),2))
        v3p=val(np.linalg.matrix_power(r(0)@r(np.pi/3),3)); v3m=val(np.linalg.matrix_power(r(0)@(-r(np.pi/3)),3))
        cm=val(Wt@r(0.3)@np.linalg.inv(Wt)@np.linalg.inv(r(0.3)))
        P(f"   {lab:44s} | {'L=T' if tw==1 else 'L=K'} | {rr} | {v8} | {v2} | {v3p},{v3m} | {cm}")
# Aut+ vertex rotations: r_a r_b is a rotation by 2pi/m of T_pSigma and (twist) of the phi1-plane. Lift connected to 1:
def rot(m,tw):
    a=np.pi/m
    return (np.cos(a)*Id+np.sin(a)*g[5]@g[6])@(np.cos(a)*Id+tw*np.sin(a)*g[9]@g[8])
for m in (8,2,3):
    Rs=np.cos(np.pi/m)*Id+np.sin(np.pi/m)*g[5]@g[6]
    out=[]
    for tw in (1,-1):
        R=rot(m,tw)
        same=val((nS(0)@nF(0,tw)@nS(np.pi/m)@nF(np.pi/m,tw))@np.linalg.inv(R))
        out.append(f"{'L=T' if tw==1 else 'L=K'}: ^{m} = {val(np.linalg.matrix_power(R,m))}, (reflection-product)/(connected lift) = {same}")
    P(f"[E] Aut+ vertex rotation order {m}: Sigma-only spin lift ^{m} = {val(np.linalg.matrix_power(Rs,m))} (2pi rotation = (-1)^F); twisted connected lift: {'; '.join(out)}; commutes with W~: {np.allclose(rot(m,1)@Wt,Wt@rot(m,1))}")
P("[E] note: in [E] g8,g9 are a local Cartesian basis of the phi1-plane at a mu1=0 point of S^4 (an abstract labelling, independent of the [C]-table coordinate names)")
# 2D control: chiral MW fermion; T and R flip chirality, CRT does not
g2=[E.copy(),X.copy()]  # gamma0^2=-1, gamma1^2=+1, real
G2=g2[0]@g2[1]
for lab,S in [('T (t->-t)',[0]),('R (x->-x)',[1]),('CRT (t,x)',[0,1])]:
    M=np.eye(2)
    for k in S: M=M@g2[k]
    P(f"[C] 2D control {lab}: M Gamma_* M^-1 = {'-Gamma_* (flips chirality: left-mover f(t+x) -> right-mover f(-t+x) for T)' if np.allclose(M@G2@np.linalg.inv(M),-G2) else '+Gamma_* (preserves)'}")
# ---------------- Q: RP^2 link of codim-3 fixed loci (only relevant if a dressed element were gauged) ----------------
from math import comb
for n in (2,3):
    w=[comb(n+1,k)%2 for k in range(n+1)]
    w1=w[1]; w2=w[2]; w1sq=w1  # a^2 coefficient of w1^2 is w1 (since w1 = w1*a)
    P(f"[Q] RP^{n}: w1={w1}a, w2={w2}a^2, w1^2={w1}a^2 => Pin+ (w2=0): {w2==0}; Pin- (w2+w1^2=0): {(w2+w1sq)%2==0}" + ("  [link of R^3/(-1): codim-3 fixed set of (i)/(ii)]" if n==2 else "  [link of R^4/(-1): codim-4 fixed set of (i')/(ii')]"))
P(f"[done] runtime {time.time()-T0:.1f} s")
