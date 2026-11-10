# PP independent exact checks for NL 79ad0c64 (E8 instanton stress vs geometric delta).
# Zero tests: sympy Poly(...).is_zero (exact polynomial arithmetic) or exact Rational/Fraction equality.
# No simplify()==0, no allclose, no float in any test (float() appears only in one printed label, P8f).
import sympy as sp, re
from fractions import Fraction as Fr
res=[]
def chk(name, ok):
    res.append(bool(ok)); print(f"[{'PASS' if ok else 'FAIL'}] {name}")
def pz(e, gens):
    e=sp.expand(e)
    return e==0 if not e.free_symbols else sp.Poly(e,*gens).is_zero

D=10; eta=sp.diag(-1,*([1]*9)); T,X,SIG,FIB=[0],[1,2,3],[4,5],[6,7,8,9]; Y6=SIG+FIB
# ---------- P1 Israel inversion on a 10D wall ----------
kap2=sp.Symbol('kappa2',positive=True)
Kd=sp.symbols('K0:10'); Kab=sp.diag(*Kd); Kmix=sp.Matrix(D,D,lambda a,b:(eta[a,a]*Kab[a,b]))  # K^a_b
Ktr=sum(Kd[a]*eta[a,a] for a in range(D))  # K = h^ab K_ab
S=-(2/kap2)*(Kab-eta*Ktr)
Str=sum(eta[a,a]*S[a,a] for a in range(D))
chk("P1a trace: K = kappa^2 S/18", pz(Ktr-kap2*Str/18, Kd))
chk("P1b K_ab = -(kappa^2/2)(S_ab - h_ab S/9)", all(pz(Kab[a,b]+(kap2/2)*(S[a,b]-eta[a,b]*Str/9),Kd) for a in range(D) for b in range(D)))
for j in X+SIG+FIB:
    k=sp.zeros(D,1); k[0]=1; k[j]=1
    if not pz((k.T*S*k)[0,0]+(2/kap2)*(k.T*Kab*k)[0,0],Kd): chk("P1c null",False); break
else: chk("P1c S(k,k) = -(2/kappa^2) K(k,k) for k = t+e_j, every j", True)
# ---------- P2 T0 end faces (J1 values as premise), Poincare-invariant face ----------
kx=sp.Symbol('kx',nonzero=True)
def face(kS,kF):
    # K_tt = -kx (k_t := -K(t,t) = kx), K_xx = kx, Sigma kS, fibre kF
    Kd_=[-kx,kx,kx,kx,kS,kS,kF,kF,kF,kF]; K_=sp.diag(*Kd_); tr=sum(Kd_[a]*eta[a,a] for a in range(D))
    S_=-(2/kap2)*(K_-eta*tr); rho=S_[0,0]
    return S_,rho,tr
for lab,(kS,kF),Ktar,wF,wS in [("IR",(0,0),4,Fr(-4,3),Fr(-4,3)),("UV",(kx,0),6,Fr(-6,5),Fr(-1))]:
    S_,rho,tr=face(kS,kF)
    chk(f"P2 {lab}: K = {Ktar} k_x", sp.expand(tr-Ktar*kx)==0)
    chk(f"P2 {lab}: w_fib = {wF}, w_Sigma = {wS} exactly", sp.Rational(wF.numerator,wF.denominator)==sp.cancel(S_[6,6]/rho) and sp.Rational(wS.numerator,wS.denominator)==sp.cancel(S_[4,4]/rho))
    Skk=S_[0,0]+S_[6,6]
    chk(f"P2 {lab}: S(t+e_fib,t+e_fib) = (2/kappa^2) k_x", sp.expand(Skk-2*kx/kap2)==0)
    chk(f"P2 {lab}: S(k,k)*rho = -c k_x^2 with c>0 (sign(S(k,k)) = -sign(rho), both pairings)", sp.cancel(Skk*rho/kx**2*kap2**2) in (-12,-20))
chk("P2 w_fib(UV)=-6/5 < -1 and w_fib(IR)=-4/3 < -1", Fr(-6,5)< -1 and Fr(-4,3)< -1)
# ---------- P3 YM stress, general field (electric legs included), one generator ----------
Fs={}; F=sp.zeros(D,D)
for a in range(D):
    for b in range(a+1,D):
        s=sp.Symbol(f"f{a}_{b}",real=True); Fs[(a,b)]=s; F[a,b]=s; F[b,a]=-s
g=list(Fs.values())
F2=sum(F[a,b]*F[c,d]*eta[a,c]*eta[b,d] for a in range(D) for b in range(D) for c in [a] for d in [b])
def YM(F,F2): return F*eta*F.T - sp.Rational(1,4)*eta*F2      # S_ab = F_ac F_b^c - 1/4 h F^2
Sg=YM(F,F2)
kk=sp.symbols('k0:10'); kv=sp.Matrix(kk)
v=sp.Matrix([sum(kv[a]*F[a,b] for a in range(D)) for b in range(D)])   # v_b = F(k,e_b)
lhs=(kv.T*Sg*kv)[0,0]; vv=(v.T*eta*v)[0,0]; kk2=(kv.T*eta*kv)[0,0]
chk("P3a S(k,k) = <F(k,.),F(k,.)>_eta - 1/4 eta(k,k) F^2 for arbitrary k (exact poly)", pz(lhs-vv+sp.Rational(1,4)*kk2*F2, g+list(kk)))
chk("P3b F(k,k) = v_b k^b = 0 (antisymmetry) for arbitrary k; with k=(1,n): v_0 = -n.v_s", pz((v.T*kv)[0,0], g+list(kk)))
# for null k=(1,n), |n|=1: v0 = -(n.v_s)*... -> <v,v> = -v0^2+|v_s|^2 >= 0 by Cauchy-Schwarz; check Lagrange identity form
n=sp.symbols('n1:10'); vs=sp.symbols('w1:10')
lag=(sum(x**2 for x in n))*(sum(y**2 for y in vs))-(sum(x*y for x,y in zip(n,vs)))**2 - sum((n[i]*vs[j]-n[j]*vs[i])**2 for i in range(9) for j in range(i+1,9))
chk("P3c Lagrange identity |n|^2|w|^2-(n.w)^2 = sum (n_i w_j - n_j w_i)^2 (so S(k,k)>=0 for every null k)", pz(lag,list(n)+list(vs)))
okC3=True
for j in range(1,D):
    k=sp.zeros(D,1); k[0]=1; k[j]=1; vj=[sum(k[a]*F[a,b] for a in range(D)) for b in range(D)]
    okC3 &= pz((k.T*Sg*k)[0,0]-sum(vj[c]**2 for c in range(1,D) if c!=j), g)
chk("P3d C3 exact: S(t+e_j,t+e_j) = sum_{c not in {t,j}} F(k,e_c)^2, all j=1..9", okC3)
# magnetic-on-Y6 sub-case: C1a-C1g re-derived
Fm=F.subs({s:0 for (a,b),s in Fs.items() if not (a in Y6 and b in Y6)}); F2m=F2.subs({s:0 for (a,b),s in Fs.items() if not (a in Y6 and b in Y6)})
Sm=YM(Fm,F2m); rho=Sm[0,0]; gm=[s for (a,b),s in Fs.items() if a in Y6 and b in Y6]
chk("P3e C1a x-block = -rho eta", all(pz(Sm[m,nn]+rho*eta[m,nn],gm) for m in T+X for nn in T+X))
chk("P3e C1b trace = -6 rho", pz(sum(eta[a,a]*Sm[a,a] for a in range(D))+6*rho,gm))
chk("P3e C1c rho = 1/2 sum F_ab^2", pz(rho-sp.Rational(1,2)*sum(s**2 for s in gm),gm))
chk("P3e C1d/e blocks; mixed x/t-Y6 = 0", all(pz(Sm[m,a],gm) for m in T+X for a in Y6) and all(pz(Sm[a,b]-(sum(Fm[a,c]*Fm[b,c] for c in Y6)-(rho if a==b else 0)),gm) for a in Y6 for b in Y6))
chk("P3e C1f S_aa + rho = |F(e_a,.)|^2 on Y6", all(pz(Sm[a,a]+rho-sum(Fm[a,c]**2 for c in Y6),gm) for a in Y6))
chk("P3e C1g S_ss - S_xx = |F(e_s,.)|^2", all(pz(Sm[s,s]-Sm[1,1]-sum(Fm[s,c]**2 for c in Y6),gm) for s in SIG))
# two generators with orthonormal positive Killing form: stress is the sum
G2={}; Fb=sp.zeros(D,D)
for a in range(D):
    for b in range(a+1,D):
        s=sp.Symbol(f"h{a}_{b}",real=True); G2[(a,b)]=s; Fb[a,b]=s; Fb[b,a]=-s
F2b=sum(Fb[a,b]**2*eta[a,a]*eta[b,b] for a in range(D) for b in range(D))
Stot=F*eta*F.T+Fb*eta*Fb.T-sp.Rational(1,4)*eta*(F2+F2b)
chk("P3f two-generator tr stress = S[F^1]+S[F^2] (one-generator reduction is exact)", all(pz(Stot[a,b]-Sg[a,b]-YM(Fb,F2b)[a,b],g+list(G2.values())) for a in range(D) for b in range(a,D)))
# ---------- P4 fibre 4D: Hodge star from epsilon, SD blocks, Bogomolny ----------
f=FIB; Gf={}
F4=sp.zeros(D,D)
for i in range(4):
    for j in range(i+1,4):
        s=sp.Symbol(f"q{i}{j}",real=True); Gf[(i,j)]=s; F4[f[i],f[j]]=s; F4[f[j],f[i]]=-s
gq=list(Gf.values())
def star(M):
    St=sp.zeros(D,D)
    for i in range(4):
        for j in range(4):
            St[f[i],f[j]]=sum(sp.Rational(1,2)*sp.LeviCivita(i,j,k_,l)*M[f[k_],f[l]] for k_ in range(4) for l in range(4))
    return St
F4s=star(F4); F24=sum(F4[a,b]**2 for a in f for b in f)/1
rho4=sp.Rational(1,4)*F24
q=sum(sp.Rational(1,4)*sp.LeviCivita(i,j,k_,l)*F4[f[i],f[j]]*F4[f[k_],f[l]] for i in range(4) for j in range(4) for k_ in range(4) for l in range(4))  # F^F / vol
asd=sum(((F4-F4s)[a,b])**2 for a in f for b in f)   # sum over ordered pairs = 2*sum_{a<b}
chk("P4a star^2 = 1 on fibre 2-forms", all(pz(star(F4s)[a,b]-F4[a,b],gq) for a in f for b in f))
chk("P4b Bogomolny: rho - q/2 = (1/8) sum_{ordered}(F-*F)^2 = 1/2 sum_{3 pairs}(F-*F)^2", pz(rho4-q/2-sp.Rational(1,8)*asd,gq))
sd={Gf[(0,1)]:sp.Symbol('a'),Gf[(2,3)]:sp.Symbol('a'),Gf[(0,2)]:sp.Symbol('b'),Gf[(1,3)]:-sp.Symbol('b'),Gf[(0,3)]:sp.Symbol('c'),Gf[(1,2)]:sp.Symbol('c')}
Fsd=F4.subs(sd); chk("P4c chosen SD parametrisation is *-self-dual", all(sp.expand(star(Fsd)[a,b]-Fsd[a,b])==0 for a in f for b in f))
Ssd=YM(Fsd,sum(Fsd[a,b]**2 for a in f for b in f)); rsd=Ssd[0,0]; abc=sp.symbols('a b c')
chk("P4d SD: fibre block 0, mixed 0, worldvolume -rho h", all(pz(Ssd[a,b],abc) for a in f for b in range(D)) and all(pz(Ssd[m,nn]+rsd*eta[m,nn],abc) for m in T+X+SIG for nn in T+X+SIG))
chk("P4e SD: rho = q/2", pz(rsd-q.subs(sd)/2,abc))
S4g=YM(F4,F24); chk("P4f general fibre field: fibre block traceless", pz(sum(S4g[a,a] for a in f),gq))
# Israel response to SD smeared stress
rS=sp.Symbol('rho',positive=True); Sw=sp.diag(*([rS]+[-rS]*5+[0]*4)); Swtr=sum(eta[a,a]*Sw[a,a] for a in range(D))
Kw=-(kap2/2)*(Sw-eta*Swtr/9)
chk("P4g S1/Y5: K^wv = kappa^2 rho/6 h, K^fib = -kappa^2 rho/3, ratio -2", sp.expand(Kw[1,1]-kap2*rS/6)==0 and sp.expand(Kw[6,6]+kap2*rS/3)==0 and sp.cancel(Kw[6,6]/Kw[1,1])==-2)
# ---------- P5 GA7a: v ^ F = 0 with F SD forces F = 0 for v != 0 ----------
vv4=sp.symbols('v0:4')
def wedge_vF(vv,a,b,c):
    Fm_=sp.zeros(4,4); 
    for (i,j),val in {(0,1):a,(2,3):a,(0,2):b,(1,3):-b,(0,3):c,(1,2):c}.items(): Fm_[i,j]=val; Fm_[j,i]=-val
    # (v^F)_{ijk} = v_i F_jk + v_j F_ki + v_k F_ij, components i<j<k
    return [vv[i]*Fm_[j,k_]+vv[j]*Fm_[k_,i]+vv[k_]*Fm_[i,j] for (i,j,k_) in [(0,1,2),(0,1,3),(0,2,3),(1,2,3)]]
w=wedge_vF(vv4,*abc); M=sp.Matrix([[sp.diff(e,x) for x in abc] for e in w])
MtM=M.T*M
chk("P5 M(v)^T M(v) = |v|^2 I_3 (so v^F=0, v!=0, F SD => F=0)", all(pz(MtM[i,j]-(sum(x**2 for x in vv4) if i==j else 0),vv4) for i in range(3) for j in range(3)))
# ---------- P6 branes: S(k,k) >= 0 for positive tension, any worldvolume containing t ----------
Tt=sp.Symbol('T',nonnegative=True); okb=True
import itertools
for Wv in [T+X+SIG, T+X+[6,7], T+X+FIB[:1]+SIG, T+[1,6]]:
    P=sp.zeros(D,D)
    for a in Wv: P[a,a]=eta[a,a]
    Sb=-Tt*P
    for j in range(1,D):
        k=sp.zeros(D,1); k[0]=1; k[j]=1
        val=(k.T*Sb*k)[0,0]; okb &= (val==Tt*(0 if j in Wv else 1))
chk("P6 brane S(k,k) = T*[j not in worldvolume] >= 0 for T >= 0", okb)
# ---------- P7 normalisations C4a, PP-1, and the factor-2 charge convention ----------
pi=sp.pi; TM5=(2*pi)**-5; kap2_11=(2*pi)**8/2   # 2 kappa^2 = (2 pi)^8 l_P^9, l_P=1
lam2_HW=2*pi*(4*pi*kap2_11)**sp.Rational(2,3); lam2_CL=2*(2*pi)**7
chk("P7a HW printed lambda^2 = 2pi(4pi kappa^2)^(2/3) = (2pi)^7 (convention 2k^2=(2pi)^8)", sp.expand(sp.powsimp(lam2_HW-(2*pi)**7,force=True))==0)
chk("P7b u := 8pi^2/(lambda^2 T_M5): HW -> 2, Conrad/Lu -> 1 (exact)", sp.cancel(8*pi**2/((2*pi)**7*TM5))==2 and sp.cancel(8*pi**2/(lam2_CL*TM5))==1)
chk("P7c Conrad/Lu lambda^6/kappa^4 = (4pi)^5 with lambda^2 = 2(2pi)^7", sp.cancel(lam2_CL**3/kap2_11**2-(4*pi)**5)==0)
chk("P7d convention-free: [(4pi)^5 / (HW lambda^6/kappa^4 = 128 pi^5)]^(1/3) = 2 = lambda^2 ratio", sp.cancel((4*pi)**5/(128*pi**5))==8)
# BPS energy per generator: E = int rho = (1/2) int F^F  (P4e).  With tr-normalisation c: n = (1/c) int tr F^F
lam2=sp.Symbol('lambda2',positive=True)
E_per_unit=lambda c: sp.Rational(1,2)*c/lam2
chk("P7e energy per unit charge = 8pi^2/lambda^2 iff unit charge is int trF^F = 16pi^2 (GA3 I_4 normalisation)", sp.cancel(E_per_unit(16*pi**2)-8*pi**2/lam2)==0)
chk("P7f with Sec.2's n_inst = (1/8pi^2) int trF^F, energy per unit = 4pi^2/lambda^2 = u/2 (factor-2 mismatch)", sp.cancel(E_per_unit(8*pi**2)/(8*pi**2/lam2))==sp.Rational(1,2))
# ---------- P8 C4b, C4c, D-B2, C4e ----------
N_,n_,u_,e_=sp.symbols('N n u eps')
Tn=(2*N_-n_)+u_*n_+e_
chk("P8a C4b tension = 2N+(u-1)n+eps", pz(Tn-(2*N_+(u_-1)*n_+e_),[N_,n_,u_,e_]))
chk("P8b C4c d/dn at u=1 is 0", sp.diff(Tn.subs(u_,1),n_)==0)
Q=9760; UV=Fr(10*4880,3)
chk("P8c 10N/3 at N=4880 is 48800/3 (not 16266.7): 16266.7 is a 1-decimal print", UV==Fr(48800,3) and UV!=Fr("16266.7"))
chk("P8d UV N_req/(2N) = 5/3 exactly IF N_req^UV = 10N/3 exactly (identity of the on-record formula; C4e is by construction)", UV/Q==Fr(5,3))
chk("P8e printed 16266.7/9760 != 5/3 (so any 5/3 'exactness' is from the formula, not the print)", Fr("16266.7")/Q!=Fr(5,3))
for lab,s in [("MN2","12568.6"),("MN1","12252.1"),("z=2","12812.2"),("z=3","12942.4")]:
    r=Fr(s)/Q; chk(f"P8f {lab}: printed N_req/9760 = {r} (exact rational of a print; ratio {float(r):.4f})", r>1)
# ---------- P9 D-A side sentence: R^2 energy (Y16 Q5, -8pi^2/lambda^2) vs one unit BPS charge ----------
chk("P9 Y16 Q5 (-8pi^2/lambda^2) + one I_4-unit BPS energy (+8pi^2/lambda^2) = 0: a >=0 energy CAN cancel it", sp.cancel(-8*pi**2/lam2+E_per_unit(16*pi**2))==0)
# ---------- P10 tally and log count ----------
txt=open('/workspace/quantum-comp/reports/NL_DERIVED_E8_INSTANTON_GEOMETRIC_DELTA_ODD_G4_2026-11-10_1120.md',encoding='utf-8').read()
rows={}
for lab in ["PROVED","CONDITIONAL","OPEN","REFUTED"]:
    m=re.search(r"^\| "+lab+r" \| (\d+) \| (.*?) \|$",txt,re.M); items=[x.strip() for x in m.group(2).split(",")]; rows[lab]=(int(m.group(1)),items)
allitems=sum((v[1] for v in rows.values()),[])
chk("P10a §7 counts equal list lengths 22/16/5/2", all(v[0]==len(v[1]) for v in rows.values()) and [v[0] for v in rows.values()]==[22,16,5,2])
chk("P10b no item double-counted; 45 distinct", len(allitems)==len(set(allitems))==45)
log=open('/workspace/nl-e8-delta-1110/e8delta_run.log').read()
npass=len(re.findall(r"^\[PASS\]",log,re.M)); nfail=len(re.findall(r"^\[FAIL\]",log,re.M))
print(f"   NL log: {npass} [PASS] lines, {nfail} [FAIL] lines")
chk("P10c NL log has 23 checks (not 26 as filed): 23 PASS, 0 FAIL", npass==23 and nfail==0)
print(f"TOTAL {sum(res)}/{len(res)} PASS"); print("ALL PASS" if all(res) else "SOME FAIL")
