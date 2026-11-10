# NL derived proposal (resonant algebra). t552u pursuit, 2026-11-10. Exact checks for the fixed-set Euler obstruction (FX),
# the two-pole argument (T1) and the diagonal-U(1) sign table (D-1). Independent Clifford(1,10) build (Gaussian integers);
# exact matrix equality / exact rank / expand(...)==0 only. No simplify(...)==0, no allclose. Exit 0 iff every test passes.
# Frame order: 0,1,2,3 | r | S1,S2 | m1,m2 | t,f  (indices 0..10).
import itertools, sys
import sympy as sp
I=sp.I; FAIL=[]; NPASS=[0]
def test(name,ok):
    print(f"[{'PASS' if ok else 'FAIL'}] {name}")
    if ok: NPASS[0]+=1
    else: FAIL.append(name)
s0=sp.eye(2); sx=sp.Matrix([[0,1],[1,0]]); sy=sp.Matrix([[0,-I],[I,0]]); sz=sp.Matrix([[1,0],[0,-1]])
def kron(*ms):
    out=ms[0]
    for m in ms[1:]: out=sp.kronecker_product(out,m)
    return out
E=[]
for k in range(5):
    E.append(kron(*([sz]*k+[sx]+[s0]*(4-k)))); E.append(kron(*([sz]*k+[sy]+[s0]*(4-k))))
chir=sp.eye(32)
for e in E: chir=chir*e
chir=I**5*chir
Gam=[I*chir]+E; Id=sp.eye(32)
ok=True
for a in range(11):
    for b in range(11):
        eta=(-2 if a==0 else 2) if a==b else 0
        ok = ok and (Gam[a]*Gam[b]+Gam[b]*Gam[a]==eta*Id)
test("C0 Clifford(1,10) relations exact",ok)
def prod(*ix):
    m=Id
    for i in ix: m=m*Gam[i]
    return m
R,S1,S2,M1,M2,T,F=4,5,6,7,8,9,10
vol=prod(*range(11)); test("C1 Gamma^{0..10} = +Id (NL representation)",vol==Id)
G0123=prod(0,1,2,3); G12=prod(1,2)
def space(conds):
    A=sp.Matrix.vstack(*[op-val*Id for op,val in conds]); return A.nullspace()
def acts_as(op,B,val):
    return all(sp.expand(x)==0 for v in B for x in (op*v-val*v))
# ---------- T1: pole argument (H_Sigma lock + HW projection + chirality) ----------
# o_p(P) rule: (x, W, n, P) positively oriented. For n=+e_r take P-frame (t,f); for n=-e_r the P-orientation reverses: (f,t).
lock=prod(S1,S2)+prod(M1,M2)
sstar={}
for chi4 in (I,-I):
    for nsign in (1,-1):
        Gn=nsign*Gam[R]; GP=prod(T,F) if nsign==1 else prod(F,T)
        B=space([(G0123,chi4),(Gn,1)]); 
        A=sp.Matrix.vstack(lock,G0123-chi4*Id,Gn-Id); B=A.nullspace()
        vals=[s for s in (1,-1) if acts_as(GP,B,I*s)]
        test(f"T1-a chi4={chi4} n={'+' if nsign==1 else '-'}e_r: locked & Gamma^n=+1 space dim={len(B)}, o_p-oriented Gamma^P acts as a single i*s3 (s3={vals})",len(B)==4 and len(vals)==1)
        if len(vals)==1: sstar[(chi4,nsign)]=vals[0]
for chi4 in (I,-I):
    test(f"T1-b chi4={chi4}: s3* w.r.t. o_p(P) is the same for n=+e_r and n=-e_r (orientation-invariant statement)",sstar[(chi4,1)]==sstar[(chi4,-1)])
# S^2 rotation weights at the two fixed points w.r.t. one global orientation (outward-normal-first in R^3(mu3,mu4,mu5)).
m3,m4,m5=sp.symbols('mu3 mu4 mu5',real=True)
xi=sp.Matrix([-m4,m3,0]); J=xi.jacobian([m3,m4,m5])
def weight(p):
    nu=sp.Matrix(p)
    for b1,b2 in itertools.permutations([sp.Matrix([1,0,0]),sp.Matrix([0,1,0])],2):
        if sp.Matrix.hstack(nu,b1,b2).det()==1:
            Mx=sp.Matrix([[b1.dot(J*b1),b1.dot(J*b2)],[b2.dot(J*b1),b2.dot(J*b2)]])
            return Mx
Mn=weight([0,0,1]); Ms=weight([0,0,-1])
test(f"T1-c rotation of (mu3,mu4): linearisation at N in oriented basis = {Mn.tolist()} (weight +1)",Mn==sp.Matrix([[0,-1],[1,0]]))
test(f"T1-c rotation of (mu3,mu4): linearisation at S in oriented basis = {Ms.tolist()} (weight -1)",Ms==sp.Matrix([[0,1],[-1,0]]))
wN=Mn[1,0]; wS=Ms[1,0]
# Kosmann at a zero: (1/4)(nabla xi)_{ab}Gamma^{ab} = (1/2) w Gamma^P. On the locked space: i q = (1/2) w i s3*  => q = w s3*/2.
for chi4 in (I,-I):
    qN=sp.Rational(wN*sstar[(chi4,1)],2); qS=sp.Rational(wS*sstar[(chi4,1)],2)
    test(f"T1-d chi4={chi4}: SO(2) charge from N = {qN}, from S = {qS}; unequal => no Killing spinor regular at both poles",qN!=qS)
# ---------- FX: chirality on the fixed 4-manifold ----------
# Case F4(xi): normal P=(t,f) weight fixed (s3), F=(S1,S2,m1,m2). Case C4 (U(1)_R): normal (m1,m2) weight fixed (s2'), F=(S1,S2,t,f).
for label,GP,Fidx in (("F4(xi): P=(t,f), F=(S1,S2,m1,m2)",prod(T,F),(S1,S2,M1,M2)),("C4: P=(m1,m2), F=(S1,S2,t,f)",prod(M1,M2),(S1,S2,T,F))):
    volF=prod(*Fidx)
    test(f"FX-0 {label}: vol_F^2 = +Id",volF*volF==Id)
    for chi4 in (I,-I):
        for s in (1,-1):
            for nsign in (1,-1):
                B=space([(G0123,chi4),(nsign*Gam[R],1),(GP,I*s)])
                vs=[v for v in (1,-1) if acts_as(volF,B,v)]
                B2=space([(G0123,chi4),(nsign*Gam[R],1),(GP,I*s),(G12,I)])
                test(f"FX-1 {label} chi4={chi4} s={s:+d} n={'+' if nsign==1 else '-'}e_r: dim={len(B)}, vol_F single eigenvalue {vs}; with Gamma^12=i dim={len(B2)}",
                     len(B)==4 and len(vs)==1 and len(B2)==2)
# ---------- FX-2: c2 of the rank-2 chiral spin^c bundles on Sigma_g x S^2 ----------
g,k,al,be=sp.symbols('g k alpha beta')
def red(e):
    e=sp.expand(e); return sp.expand(e.subs({al**2:0,be**2:0}).subs(al*be,1))
def c2(x1,x2): return red(x1*x2)
# S(Sigma)=K^{1/2}+K^{-1/2} (degrees +-(g-1)); S(S^2)=O(-1)+O(1). Twist lambda with c1 = k*alpha (pulled back from Sigma).
Sp=[(g-1)*al-be+k*al, -(g-1)*al+be+k*al]; Sm=[(g-1)*al+be+k*al, -(g-1)*al-be+k*al]
cp=c2(*Sp); cm=c2(*Sm)
test(f"FX-2a c2(S^+ (x) lambda) = {cp} ; expand(c2-(2g-2))==0",sp.expand(cp-(2*g-2))==0)
test(f"FX-2b c2(S^- (x) lambda) = {cm} ; expand(c2+(2g-2))==0",sp.expand(cm+(2*g-2))==0)
test("FX-2c independent of the twist k (any degree of the normal line)",sp.diff(cp,k)==0 and sp.diff(cm,k)==0)
chiX=(2-2*g)*2; sig=0
cdet=red((Sp[0]+Sp[1])**2)
test(f"FX-2d agrees with (c1^2 - 2chi -/+ 3sigma)/4 (c1^2={cdet}, chi={chiX}, sigma=0)",
     sp.expand(cp-(cdet-2*chiX-3*sig)/4)==0 and sp.expand(cm-(cdet+2*chiX-3*sig)/4)==0)
test(f"FX-2e Bolza g=2: c2 = {cp.subs(g,2)}, {cm.subs(g,2)} (both nonzero)",cp.subs(g,2)==2 and cm.subs(g,2)==-2)
test(f"FX-2f control torus g=1: c2 = {cp.subs(g,1)}, {cm.subs(g,1)} (obstruction disappears)",cp.subs(g,1)==0 and cm.subs(g,1)==0)
# sigma(F)=0 for any S^2-bundle over a surface: rank-2 unimodular form with isotropic primitive fibre class f (f.f=0, f.s=1).
s2sq=sp.symbols('e',integer=True); Q=sp.Matrix([[0,1],[1,s2sq]])
test(f"FX-2g intersection form [[0,1],[1,e]]: det=-1, eigenvalue product <0 => signature 0 for every e",sp.expand(Q.det()+1)==0)
# ---------- D-1: diagonal U(1)_{a,b} sign table ----------
# weights (a on m with K/U(1)_R orientation, b on P with o_p orientation) at N; (a,-b) at S. CH fixes s1 given (chi4,s2',s3), Gamma^n=+1.
def s1_of(chi4,s2,s3):
    occ=[s1 for s1 in (1,-1) if space([(G0123,chi4),(Gam[R],1),(prod(S1,S2),I*s1),(prod(M1,M2),I*s2),(prod(T,F),I*s3)])]
    return occ
s1tab={}
okCH=True
for chi4 in (I,-I):
    for s2,s3 in itertools.product((1,-1),repeat=2):
        o=s1_of(chi4,s2,s3); okCH=okCH and len(o)==1; s1tab[(chi4,s2,s3)]=o[0] if o else None
test("D-1a CH: given chi4, s2', s3 and Gamma^r=+1 exactly one s1 occurs",okCH)
okD=True; resid=set()
for a,b in [(1,1),(1,-1),(1,2),(2,1),(1,3),(3,-2),(2,-1)]:
    for chi4 in (I,-I):
        for q2 in range(-(abs(a)+abs(b)),abs(a)+abs(b)+1):   # 2q
            solN=[(s2,s3) for s2,s3 in itertools.product((1,-1),repeat=2) if a*s2+b*s3==q2]
            solS=[(s2,s3) for s2,s3 in itertools.product((1,-1),repeat=2) if a*s2-b*s3==q2]
            if len(solN)==1 and len(solS)==1:
                (n2,n3),(t2,t3)=solN[0],solS[0]
                s1N=s1tab[(chi4,n2,n3)]; s1S=s1tab[(chi4,t2,t3)]
                unlockedN=(s1N==n2); unlockedS=(s1S==t2)
                okD = okD and (n2==t2) and (n3==-t3) and (s1N==-s1S) and (unlockedN!=unlockedS)
            elif solN or solS:
                resid.add((a,b,sp.Rational(q2,2)))
test("D-1b whenever the weight equation has a unique solution at N and at S: same s2', opposite s3 and s1, exactly one pole section unlocked",okD)
test(f"D-1c residual (non-unique) cases are exactly |a|=|b| with q=0: {sorted(resid)}",all(abs(a)==abs(b) and q==0 for a,b,q in resid) and len(resid)>0)
print(f"SUMMARY: {NPASS[0]} passed, {len(FAIL)} failed")
sys.exit(0 if not FAIL else 1)
