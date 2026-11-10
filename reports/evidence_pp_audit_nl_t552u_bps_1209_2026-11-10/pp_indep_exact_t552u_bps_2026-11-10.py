# PP independent exact checks for the NL t552u BPS-cluster filings 617bc443 (FX) and 6ccc9ef4 (NEC). 2026-11-10.
# Exact sympy only: exact matrix equality, exact nullspace rank over Q(i), expand(...)==0, exact Rational / integer.
# No simplify, no nsimplify, no float, no numpy, no allclose. Own Clifford build, both inequivalent representations.
import itertools, sys
import sympy as sp
I=sp.I; NP=[0]; FAIL=[]
def test(name,ok):
    ok=bool(ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if ok: NP[0]+=1
    else: FAIL.append(name)
# ---------------- PART A: Clifford(1,10), own build, both representations ----------------
s0=sp.eye(2); sx=sp.Matrix([[0,1],[1,0]]); sy=sp.Matrix([[0,-I],[I,0]]); sz=sp.Matrix([[1,0],[0,-1]])
def kron(ms):
    out=ms[0]
    for m in ms[1:]: out=sp.kronecker_product(out,m)
    return out
# Euclidean Cl(10) generators with the Pauli chain REVERSED relative to NL (identities on the left, sz on the right)
Ee=[]
for k in range(5):
    Ee.append(kron([s0]*(4-k)+[sx]+[sz]*k)); Ee.append(kron([s0]*(4-k)+[sy]+[sz]*k))
Id=sp.eye(32)
c11=Id
for e in Ee: c11=c11*e
# frame labels: 0,1,2,3 | r | S1,S2 | m1,m2 | t,f ; spatial labels 1..10 get Euclidean generators by a fixed shuffle
shuffle=[3,7,0,9,5,1,8,2,6,4]
def build(sign):
    G=[None]*11
    for lab in range(1,11): G[lab]=Ee[shuffle[lab-1]]
    # Gamma^0 with (Gamma^0)^2=-1: proportional to the product of the ten Euclidean ones
    G0=I*c11*(I**5)
    G[0]=sign*G0
    return G
R,S1,S2,M1,M2,T,F=4,5,6,7,8,9,10
reps={}
for sign in (1,-1):
    G=build(sign)
    ok=all(G[a]*G[b]+G[b]*G[a]==((-2 if a==0 else 2)*Id if a==b else sp.zeros(32)) for a in range(11) for b in range(11))
    vol=Id
    for a in range(11): vol=vol*G[a]
    c=int(vol[0,0])
    test(f"A0 rep(sign={sign:+d}): Clifford(1,10) exact; Gamma^(0..10) = c*Id with c={c}",ok and vol==c*Id and c in (1,-1))
    reps[c]=G
test("A0b both inequivalent representations realised (c=+1 and c=-1)",set(reps)=={1,-1})
def P(G,*ix):
    m=Id
    for i in ix: m=m*G[i]
    return m
def nullsp(conds):
    A=sp.Matrix.vstack(*[op-val*Id for op,val in conds]); return A.nullspace()
def single_eig(op,B):
    vals=[v for v in (1,-1,I,-I) if all(sp.expand(x)==0 for b in B for x in (op*b-v*b))]
    return vals
for c,G in sorted(reps.items()):
    G0123=P(G,0,1,2,3); G12=P(G,1,2)
    # A1: operator identities behind FX step 3 (representation-independent: only Gamma^(0..10)=c is used)
    for lab,Fidx,nu in (("F4",(S1,S2,M1,M2),(T,F)),("C4",(S1,S2,T,F),(M1,M2))):
        lhs=G0123*G[R]*P(G,*Fidx)*P(G,*nu)
        perm=list(range(4))+[R]+list(Fidx)+list(nu)
        sgn=sp.combinatorics.Permutation([perm.index(i) for i in range(11)]).signature()
        test(f"A1 c={c:+d} {lab}: Gamma^0123 Gamma^r vol_F Gamma^nu = (perm sign {sgn})*c*Id exactly",lhs==sgn*c*Id)
        # FX-1 analogue: with chi4, Gamma^n=+1 (n=+-e_r), Gamma^nu = i s: dim 4, vol_F single eigenvalue; + Gamma^12: dim 2
        okall=True
        for chi4,s,ns in itertools.product((I,-I),(1,-1),(1,-1)):
            B=nullsp([(G0123,chi4),(ns*G[R],1),(P(G,*nu),I*s)])
            vs=single_eig(P(G,*Fidx),B)
            B2=nullsp([(G0123,chi4),(ns*G[R],1),(P(G,*nu),I*s),(G12,I)])
            okall=okall and len(B)==4 and len(vs)==1 and vs[0] in (1,-1) and len(B2)==2
        test(f"A2 c={c:+d} {lab}: all 16 (chi4,s,n) cases: dim 4, vol_F single real eigenvalue, rank 2 with Gamma^12=i",okall)
    # A3: two-pole statement T1, BOTH lock orientations, o_p rule (n=+e_r -> (t,f); n=-e_r -> (f,t))
    for lsign in (1,-1):
        lock=P(G,S1,S2)+lsign*P(G,M1,M2)
        okT=True; star={}
        for chi4 in (I,-I):
            for ns in (1,-1):
                GP=P(G,T,F) if ns==1 else P(G,F,T)
                B=sp.Matrix.vstack(lock,G0123-chi4*Id,ns*G[R]-Id).nullspace()
                vals=[s for s in (1,-1) if all(sp.expand(x)==0 for b in B for x in (GP*b-I*s*b))]
                okT=okT and len(B)==4 and len(vals)==1
                if len(vals)==1: star[(chi4,ns)]=vals[0]
            okT=okT and star.get((chi4,1))==star.get((chi4,-1)) and star.get((chi4,1)) is not None
        okT=okT and star[(I,1)]==-star[(-I,1)]
        test(f"A3 c={c:+d} lock sign {lsign:+d}: locked&Gamma^n=+1 dim 4, single s3* w.r.t. o_p, equal for n=+-e_r, opposite for opposite chi4 (s3*(i)={star.get((I,1))})",okT)
    # A4: CH (D-1a analogue): given chi4, s2', s3, Gamma^r=+1 exactly one s1, and s1(chi4,s2,-s3) = -s1(chi4,s2,s3)
    okCH=True; tab={}
    for chi4,s2,s3 in itertools.product((I,-I),(1,-1),(1,-1)):
        occ=[s1 for s1 in (1,-1) if nullsp([(G0123,chi4),(G[R],1),(P(G,S1,S2),I*s1),(P(G,M1,M2),I*s2),(P(G,T,F),I*s3)])]
        okCH=okCH and len(occ)==1; tab[(chi4,s2,s3)]=occ[0] if occ else None
    okFlip=okCH and all(tab[(chi4,s2,-s3)]==-tab[(chi4,s2,s3)] for chi4,s2,s3 in tab)
    test(f"A4 c={c:+d}: CH unique s1, and flipping s3 at fixed (chi4,s2') flips s1 (all 8 cases)",okFlip)
    # lock-label logic: for either lock sign L (locked <=> s1 = -L*s2'), exactly one of (s1, -s1) is locked at fixed s2'
    okL=all(((tab[(chi4,s2,s3)]==-L*s2)!=(tab[(chi4,s2,-s3)]==-L*s2)) for L in (1,-1) for chi4,s2,s3 in tab)
    test(f"A5 c={c:+d}: for either lock sign, exactly one of the two pole sections is unlocked when s2' agrees and s3 flips",okL)
# ---------------- PART B: topology (rational cohomology, splitting principle) ----------------
g,k,j=sp.symbols('g k j',integer=True); al,be=sp.symbols('alpha beta')
def red(e):  # ring Q[alpha,beta]/(alpha^2, beta^2), [alpha*beta] = 1
    e=sp.expand(e); e=sp.expand(e.subs({al**2:0,be**2:0})); return sp.expand(e.subs(al*be,1))
# own convention: S^+(Sigma_g) = K^{1/2} (deg g-1), S^-(Sigma_g)=K^{-1/2}; S^+(S^2)=O(-1), S^-(S^2)=O(+1)
SpS=[(g-1)*al,-(g-1)*al]; Ssph_p=-be; Ssph_m=be
Wp=[SpS[0]+Ssph_p, SpS[1]+Ssph_m]   # S+ x S+  (+)  S- x S-
Wm=[SpS[0]+Ssph_m, SpS[1]+Ssph_p]   # S+ x S-  (+)  S- x S+
def c2tw(roots,lam): return red((roots[0]+lam)*(roots[1]+lam))
cp=c2tw(Wp,k*al); cm=c2tw(Wm,k*al)
test(f"B1 c2(S^+ (x) lambda), c1(lambda)=k*alpha: {cp}; expand(c2-(2g-2))==0",sp.expand(cp-(2*g-2))==0)
test(f"B2 c2(S^- (x) lambda), c1(lambda)=k*alpha: {cm}; expand(c2+(2g-2))==0",sp.expand(cm+(2*g-2))==0)
test(f"B3 Bolza g=2: (+2,-2); torus control g=1: (0,0)",cp.subs(g,2)==2 and cm.subs(g,2)==-2 and cp.subs(g,1)==0 and cm.subs(g,1)==0)
cpj=c2tw(Wp,k*al+j*be); cmj=c2tw(Wm,k*al+j*be)
test(f"B4 premise-necessity: with a fibre component c1(lambda)=k*alpha+j*beta, c2 = {cpj}, {cmj} (depends on k*j; vanishes e.g. g=2,k=1,j=-1)",
     sp.expand(cpj-(2*g-2+2*k*j))==0 and sp.expand(cmj-(2-2*g+2*k*j))==0 and cpj.subs({g:2,k:1,j:-1})==0)
# correct spin^c formula c2(W^+-) = (c1^2 -+ 2chi - 3sigma)/4 versus the filing's text form (c1^2 - 2chi -+ 3sigma)/4
chiS=4-4*g; c1sq=red((Wp[0]+Wp[1]+2*k*al)**2)
test("B5 Sigma_g x S^2: correct form (c1^2 -+ 2chi - 3sigma)/4 reproduces (+(2g-2), -(2g-2)) at sigma=0",
     sp.expand(cp-(c1sq-2*chiS)/4)==0 and sp.expand(cm-(c1sq+2*chiS)/4)==0)
test("B6 filing text form (c1^2 - 2chi -+ 3sigma)/4 gives +(2g-2) for BOTH at sigma=0, contradicting FX-2b (transcription error, W^- line)",
     sp.expand((c1sq-2*chiS+3*0)/4-(2*g-2))==0 and sp.expand(cm-(c1sq-2*chiS+3*0)/4)!=0)
# controls of the correct form on spaces with sigma != 0 or chi != genus-type: S^2 x S^2 (spin) and CP^2 (canonical spin^c)
a2,b2=sp.symbols('a2 b2')
def red22(e):
    e=sp.expand(e); e=sp.expand(e.subs({a2**2:0,b2**2:0})); return sp.expand(e.subs(a2*b2,1))
c2p=red22((-a2-b2)*(a2+b2)); c2m=red22((-a2+b2)*(a2-b2))
test(f"B7 S^2xS^2 control: c2(S^+)={c2p}, c2(S^-)={c2m}; (0 -+ 2*4 - 0)/4 = (-2, +2)",c2p==-2 and c2m==2)
h=sp.symbols('h')  # CP^2: h^2=1 (h^3=0); W^+ = O (+) K^{-1} (c1=3h), W^- = T CP^2 with c(T)=(1+h)^3
c1W=3; c2Wp=0; c2Wm=sp.expand((1+h)**3).coeff(h,2)
test(f"B8 CP^2 control: c2(W^+)={c2Wp}=(9-6-3)/4, c2(W^-)={c2Wm}=(9+6-3)/4 (chi=3, sigma=1)",
     sp.Rational(c1W**2-2*3-3*1,4)==c2Wp and sp.Rational(c1W**2+2*3-3*1,4)==c2Wm)
e_=sp.symbols('e',integer=True); Q=sp.Matrix([[0,1],[1,e_]])
cp_=sp.expand(Q.charpoly(sp.Symbol('x')).as_expr())
test("B9 S^2-bundle intersection form [[0,1],[1,e]]: det=-1 for all e (eigenvalues of opposite sign: sigma=0); chi(Sigma_2 x S^2)=-4",
     sp.expand(Q.det()+1)==0 and chiS.subs(g,2)==-4)
# ---------------- PART C: two-pole weights and the diagonal sign table (symbolic a, b) ----------------
m3,m4,m5,wgt=sp.symbols('mu3 mu4 mu5 w')
xi=wgt*sp.Matrix([-m4,m3,0]); J=xi.jacobian([m3,m4,m5])
def lin_at(p):  # oriented basis (b1,b2) of T_pS^2 with (outward normal, b1, b2) positive in R^3
    nu=sp.Matrix(p); b1=sp.Matrix([1,0,0]); b2=nu.cross(b1)
    assert sp.Matrix.hstack(nu,b1,b2).det()==1
    Jp=J.subs({m3:p[0],m4:p[1],m5:p[2]})
    return sp.Matrix([[b1.dot(Jp*b1),b1.dot(Jp*b2)],[b2.dot(Jp*b1),b2.dot(Jp*b2)]])
LN=lin_at([0,0,1]); LS=lin_at([0,0,-1])
test(f"C1 rotation weight w.r.t. one global orientation of S^2: north {LN.tolist()}, south {LS.tolist()} (weights +w, -w)",
     LN==sp.Matrix([[0,-wgt],[wgt,0]]) and LS==sp.Matrix([[0,wgt],[-wgt,0]]))
sst=sp.symbols('sstar')
qN=wgt*sst/2; qS=-wgt*sst/2
test("C2 two-pole charges q_N - q_S = w*s3* (nonzero for w != 0, s3* = +-1) => no common charge",sp.expand(qN-qS-wgt*sst)==0)
a,b=sp.symbols('a b')
signs=list(itertools.product((1,-1),repeat=2))
vals={s:a*s[0]+b*s[1] for s in signs}
test("C3 S-pole equation a s2 - b s3 = 2q is the N-pole equation under (s2,s3)->(s2,-s3): bijection of solution sets (expand==0)",
     all(sp.expand((a*s2-b*(-s3))-vals[(s2,s3)])==0 for s2,s3 in signs))
diffs=[sp.factor(vals[s]-vals[t]) for s,t in itertools.combinations(signs,2)]
prod_d=sp.factor(sp.Mul(*diffs))
test(f"C4 product of the 6 pairwise differences = {prod_d}: a coincidence occurs iff a=0, b=0 or a=+-b",
     sp.expand(prod_d-sp.expand(sp.Mul(*[vals[s]-vals[t] for s,t in itertools.combinations(signs,2)])))==0
     and set(sp.factor_list(prod_d)[1][i][0] for i in range(len(sp.factor_list(prod_d)[1])))=={a,b,a+b,a-b})
# coincident value is 0 whenever a=b or a=-b (q=0)
ok5=(sp.expand(vals[(1,-1)].subs(a,b))==0 and sp.expand(vals[(-1,1)].subs(a,b))==0 and
     sp.expand(vals[(1,1)].subs(a,-b))==0 and sp.expand(vals[(-1,-1)].subs(a,-b))==0)
test("C5 for a=b the coincident pair (+,-),(-,+) has value 0; for a=-b the pair (+,+),(-,-) has value 0 => residual exactly |a|=|b|, q=0",ok5)
# exhaustive integer sweep |a|,|b|<=6 (corroboration only; C3-C5 are the general proof)
resid=set(); okU=True
for A_ in range(-6,7):
    for B_ in range(-6,7):
        if A_==0 or B_==0: continue
        for q2 in range(-13,14):
            nN=[s for s in signs if A_*s[0]+B_*s[1]==q2]; nS=[s for s in signs if A_*s[0]-B_*s[1]==q2]
            okU=okU and (len(nN)==len(nS))
            if len(nN)>1: resid.add((abs(A_)==abs(B_),q2))
test(f"C6 sweep |a|,|b|<=6 (a,b != 0): N and S solution counts equal; non-unique only with |a|=|b| and 2q=0: {sorted(resid)}",okU and resid=={(True,0)})
# cohomogeneity counting (A12): rank of Killing fields of SO(3)_R x U(1)_R on R^5 at a generic S^4 point
mu=sp.Matrix([1,2,3,5,7])
gens=[]
def rot(i,jj):
    Mx=sp.zeros(5); Mx[i,jj]=-1; Mx[jj,i]=1; return Mx
for (i,jj) in [(0,1)]: gens.append(rot(i,jj)*mu)          # U(1)_R on (mu1,mu2)
for (i,jj) in [(2,3),(2,4),(3,4)]: gens.append(rot(i,jj)*mu)  # SO(3)_R on (mu3,mu4,mu5)
rk_full=sp.Matrix.hstack(*gens).rank(); rk_so3=sp.Matrix.hstack(*gens[1:]).rank()
rk_T2=sp.Matrix.hstack(gens[0],gens[1]).rank(); rk_diag=sp.Matrix.hstack(gens[0]+gens[1]).rank()
coh=lambda r: 7-2-r
test(f"C7 orbit dims on S^4: full {rk_full}, SO(3)_R {rk_so3}, T^2 {rk_T2}, diagonal {rk_diag}; cohomogeneity with H_Sigma: {coh(rk_full)},{coh(rk_so3)},{coh(rk_T2)},{coh(rk_diag)}, none {coh(0)}",
     (rk_full,rk_so3,rk_T2,rk_diag)==(3,2,2,1) and (coh(rk_full),coh(rk_so3),coh(rk_T2),coh(rk_diag),coh(0))==(2,3,3,4,5))
test("C8 counterexample to A12's residual sentence: the E4-6 main case (H_Sigma x SO(3)_R x U(1)_R, singular on C4) is in A10 and has cohomogeneity 2 < 4",coh(rk_full)==2)
# ---------------- PART D: filing 2 (NEC necessary conditions) ----------------
r=sp.symbols('r'); pp,lp,wp,Ap=sp.symbols('phi_p lam_p w_p A_p')
tf=[sp.Function(f't{i}')(r) for i in range(5)]
taus=[-6*lp,-6*lp,4*lp+wp,4*lp+wp,4*lp-2*wp]   # (ln T_aa)' for T=diag(e^-6lam,e^-6lam,e^{4lam+w},e^{4lam+w},e^{4lam-2w})
def margins_axis(i):
    ys=sp.symbols('y0:4'); others=[jj for jj in range(5) if jj!=i]
    muv=[0]*5
    for kk,jj in enumerate(others): muv[jj]=ys[kk]
    muv[i]=sp.sqrt(1-sum(y**2 for y in ys)); muv=sp.Matrix(muv)
    Del=sum(tf[aa]*muv[aa]**2 for aa in range(5))
    Jm=muv.jacobian(ys)
    gm=Del**sp.Rational(-2,3)*(Jm.T*sp.diag(*[1/t for t in tf])*Jm)
    at0={y:0 for y in ys}
    g0=gm.subs(at0); dg0=sp.diff(gm,r).subs(at0)
    D0=Del.subs(at0); dD0=sp.diff(Del,r).subs(at0)
    sub={sp.Derivative(tf[aa],r):tf[aa]*taus[aa] for aa in range(5)}
    Kf=(g0.inv()*dg0/2).subs(sub)
    kx=Ap-2*pp+(dD0/D0).subs(sub)/6
    offd=all(sp.expand(sp.together(Kf[x,y]).as_numer_denom()[0])==0 for x in range(4) for y in range(4) if x!=y)
    out={}
    for kk,jj in enumerate(others):
        out[jj]=sp.together(Kf[kk,kk]-kx)
    return offd,out
closed={(0,1):6*lp,(0,2):lp-wp/2,(0,3):lp-wp/2,(0,4):lp+wp,
        (2,0):lp-wp/2,(2,1):lp-wp/2,(2,3):-4*lp-wp,(2,4):-4*lp+wp/2,
        (4,0):lp+wp,(4,1):lp+wp,(4,2):-4*lp+wp/2,(4,3):-4*lp+wp/2}
MM={}
for i in (0,2,4):
    offd,out=margins_axis(i); MM[i]=out
    okm=all(sp.expand(sp.together(out[jj]-(2*pp-Ap+closed[(i,jj)])).as_numer_denom()[0])==0 for jj in out)
    test(f"D1 axis mu=e{i+1} (own normal chart, t_a(r) generic, then (ln t_a)'=tau_a): shape operator diagonal and all 4 margins = (2phi'-A') + closed form",offd and okm)
comb=sp.expand(sp.together(MM[0][1]+2*MM[2][3]+2*MM[4][0]).as_numer_denom()[0])
test("D2 Z-N3 re-derived: m(e1;e2)+2m(e3;e4)+2m(e5;e1) - 5(2phi'-A') == 0 (expand), weights (1,2,2) >= 0",sp.expand(sp.together(MM[0][1]+2*MM[2][3]+2*MM[4][0]-5*(2*pp-Ap)).as_numer_denom()[0])==0)
test("D3 Sigma margin (k_S-k_x)/eps = 5phi'-A' (frozen k_S, k_x; D' cancels)",sp.expand((3*pp+sp.Symbol('Dp')/6)-(Ap-2*pp+sp.Symbol('Dp')/6)-(5*pp-Ap))==0)
V=sp.symbols('V')
Vc=30*pp**2+30*lp**2+sp.Rational(3,2)*wp**2-12*Ap**2      # frozen constraint solved for V
test("D4 Z-N5 chain: -V - [(9/2)A'^2 - 30lam'^2 - (3/2)w'^2] = -30(phi'-A'/2)(phi'+A'/2) on the constraint (expand==0)",
     sp.expand(-Vc-(sp.Rational(9,2)*Ap**2-30*lp**2-sp.Rational(3,2)*wp**2)+30*(pp-Ap/2)*(pp+Ap/2))==0)
# premise necessity: A' <= 0 is needed (A'=1, phi'=0 satisfies 2phi'<=A' but (phi'-A'/2)(phi'+A'/2) = -1/4 < 0)
test("D5 A'<=0 is a needed premise: (A',phi')=(1,0) has 2phi'<=A' but (phi'-A'/2)(phi'+A'/2) = -1/4",((0-sp.Rational(1,2))*(0+sp.Rational(1,2)))==sp.Rational(-1,4))
# |V| form needs V<=0: A'=-1, phi'=-1, lam'=w'=0: all axis margins and Sigma margin <= 0, but V=+18 > (3/8)*12*A'^2 = 9/2
ptc={pp:-1,lp:0,wp:0,Ap:-1}
allm=[sp.expand((2*pp-Ap+v).subs(ptc)) for v in closed.values()]+[sp.expand((5*pp-Ap).subs(ptc))]
Vval=Vc.subs(ptc)
test(f"D6 '|V| <= (3/8)*12A'^2' is not implied when V>0: at (A',phi',lam',w')=(-1,-1,0,0) all axis/Sigma margins {sorted(set(allm))} <= 0, V={Vval} > 9/2; the -V form holds",
     all(x<=0 for x in allm) and Vval==18 and -Vval<=sp.Rational(9,2))
test("D7 Z-N6: at zero scalar velocity comb = -5A' (expand==0)",sp.expand(sp.together(MM[0][1]+2*MM[2][3]+2*MM[4][0]).subs({pp:0,lp:0,wp:0})+5*Ap)==0)
# MN2 vacuum value of the frozen potential, exact (g=1, l=-1, phi=ln2/30, lam=ln2/10, w=0)
ph,la,w=sp.symbols('phi lambda w',real=True); gg=1; l=-1
S=sp.exp(-(ph+3*la)); O=sp.exp(3*ph-la-w); vp=la-3*ph-w/2
Vpot=-(gg**2*O**-2*S**-2*(2*l*sp.exp(2*vp)*O*S**3-sp.Rational(1,2)*sp.exp(4*vp)*l**2-sp.Rational(1,2)*sp.exp(4*vp)*O**4+4*O*S**3+2*sp.exp(2*vp)*O**2+2*sp.exp(2*vp)*O**3*S**3))
V0=sp.expand(sp.powsimp(sp.expand(Vpot.subs({ph:sp.log(2)/30,la:sp.log(2)/10,w:0})),force=True))
test(f"D8 frozen V at the MN2 point = {V0} = -3*2^(2/3) < 0 (exact), so A'(MN2) = -sqrt(-V0/12) = -2^(-2/3) != 0",
     sp.expand(V0+3*2**sp.Rational(2,3))==0)
# fidelity of NL's re-typing against the frozen face file (read-only text check)
src=open('/workspace/nl-bps-d6-2057/z2_centre_flow_faces.py').read()
needles=["eps=D**(-1/6)*np.exp(2*p)","kx=eps*(Ap-2*dp+dD/6); kS=eps*(3*dp+dD/6)","Kf=0.5*eps*np.linalg.solve(gm,dg)",
         "Tdiag=[sp.exp(-6*la)]*2+[sp.exp(4*la+w)]*2+[sp.exp(4*la-2*w)]","Gd=np.array([60.,60.,3.])","Ap=-np.sqrt(max(K,0)/12)",
         "K=0.5*np.dot(Gd,dX**2)-Vf(*Xv)","np.linspace(0.05,np.pi/2-0.05,9)"]
test("D9 NL's re-typed face formulas, T, constraint, A'=-sqrt branch occur verbatim in frozen 21bcbc3f (grid excludes the axis points)",all(n in src for n in needles))
print(f"SUMMARY: {NP[0]} passed, {len(FAIL)} failed")
sys.exit(0 if not FAIL else 1)
