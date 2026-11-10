# NL derived proposal (resonant algebra). t552u pursuit, 2026-11-10. Exact necessary conditions for an 11D-NEC face on ANY
# 3-scalar (phi,lambda,w) truncation flow (BPS or not, any IR), using the face data of the frozen
# /workspace/nl-bps-d6-2057/z2_centre_flow_faces.py (formulas re-typed here, file not imported or edited):
#   eps = Delta^{-1/6} e^{2phi};  k_x = eps(A' - 2phi' + D'/6);  k_S = eps(3phi' + D'/6);  fibre: K = (1/2) eps g^{-1} dg/dr,
#   g = Delta^{-2/3} T^{-1}_{ij} dmu^i dmu^j on S^4,  T = diag(e^{-6lam}, e^{-6lam}, e^{4lam+w}, e^{4lam+w}, e^{4lam-2w}).
#   NEC for the required wall stress <=> k_v - k_x <= 0 for every unit internal v at every point (PP Y15).
#   Hamiltonian constraint (frozen code): 12 A'^2 = 30 phi'^2 + 30 lam'^2 + (3/2) w'^2 - V, with A' = -sqrt(...) <= 0.
# Exact sympy; tests are expand(...)==0 or exact Rational comparisons. Exit 0 iff all pass.
import sys, sympy as sp
FAIL=[]; NP=[0]
def test(n,ok):
    print(f"[{'PASS' if ok else 'FAIL'}] {n}")
    if ok: NP[0]+=1
    else: FAIL.append(n)
la,w=sp.symbols('lambda w',real=True)
p,l,u,a,eps=sp.symbols("phi_p lam_p w_p A_p eps",real=True)   # phi', lambda', w', A'
Tdiag=[sp.exp(-6*la)]*2+[sp.exp(4*la+w)]*2+[sp.exp(4*la-2*w)]
def ddr(expr): return sp.diff(expr,la)*l+sp.diff(expr,w)*u
def axis_margins(i):
    Dl=sp.log(Tdiag[i]); Dp=sp.expand(ddr(Dl))                # Delta = T_ii at mu = e_i
    kx=a-2*p+Dp/6                                              # k_x/eps
    out={}
    for j in range(5):
        if j==i: continue
        tj=sp.expand(ddr(sp.log(1/Tdiag[j]))/2)               # (1/2) d/dr ln T^{-1}_jj
        kv=-Dp/3+tj                                            # (1/2) d/dr ln( Delta^{-2/3} T^{-1}_jj )
        out[j]=sp.expand(kv-kx)
    return out,Dp
mS=sp.expand((3*p)-(a-2*p))                                    # (k_S - k_x)/eps, D' cancels
test(f"Z-N1 (k_S-k_x)/eps = {mS}",sp.expand(mS-(5*p-a))==0)
M={}
for i in (0,2,4):
    out,Dp=axis_margins(i); M[i]=out
    print(f"    mu=e{i+1}: D'={Dp}; margins (k_v-k_x)/eps:",{f'e{j+1}':v for j,v in out.items()})
exp={ (0,1):6*l+2*p-a, (0,2):l-u/2+2*p-a, (0,4):l+u+2*p-a,
      (2,0):l-u/2+2*p-a, (2,3):-4*l-u+2*p-a, (2,4):-4*l+u/2+2*p-a,
      (4,0):l+u+2*p-a, (4,2):-4*l+u/2+2*p-a }
test("Z-N2 axis-point margins equal the closed forms",all(sp.expand(M[i][j]-v)==0 for (i,j),v in exp.items()))
comb=sp.expand(M[0][1]+2*M[2][3]+2*M[4][0])
test(f"Z-N3 m(e1;e2) + 2 m(e3;e4) + 2 m(e5;e1) = {comb} ; expand(comb - 5(2phi'-A'))==0",sp.expand(comb-5*(2*p-a))==0)
# cross-check against the frozen chart (chi,theta,nu,psi) at mu=e3 (chi=pi/2, theta=pi/2), nondegenerate block (chi,theta,psi)
chi,th=sp.symbols('chi theta',real=True)
mu_s=sp.Matrix([sp.cos(chi),0,sp.sin(chi)*sp.sin(th),0,sp.sin(chi)*sp.cos(th)])
tv=[sp.diff(mu_s,chi),sp.diff(mu_s,th),sp.Matrix([0,0,0,sp.sin(chi)*sp.sin(th),0])]
Del=sum(Tdiag[k]*mu_s[k]**2 for k in range(5)); Tinv=sp.diag(*[1/t for t in Tdiag])
g3=sp.Matrix(3,3,lambda r,c: Del**sp.Rational(-2,3)*(tv[r].T*Tinv*tv[c])[0])
dg3=g3.applyfunc(ddr)
pt={chi:sp.pi/2,th:sp.pi/2}
G=g3.subs(pt); dG=dg3.subs(pt)
test("Z-N4a frozen-chart block at (chi,theta)=(pi/2,pi/2) is diagonal",all(sp.expand(G[r,c])==0 for r in range(3) for c in range(3) if r!=c) and all(sp.expand(dG[r,c])==0 for r in range(3) for c in range(3) if r!=c))
Dp3=sp.expand(ddr(sp.log(Del)).subs(pt))
kx3=a-2*p+Dp3/6
ref=[M[2][0],M[2][4],M[2][3]]
# margin_r = dG_rr/(2 G_rr) - k_x/eps  <=>  dG_rr - 2 (margin_r + k_x/eps) G_rr == 0  (polynomial identity in exponentials)
res=[sp.expand(sp.powsimp(sp.expand(dG[r,r]-2*(ref[r]+kx3)*G[r,r]),combine='exp')) for r in range(3)]
print("    residuals:",res, " G diag:",[G[r,r] for r in range(3)])
test(f"Z-N4b frozen-chart margins at mu=e3 (chi,theta,psi) equal the axis forms (expand==0)",all(x==0 for x in res) and all(G[r,r]!=0 for r in range(3)))
# constraint consequence: NEC => 2phi' <= A' (<=0) => phi'^2 >= A'^2/4 => -V <= 12A'^2 - 30 A'^2/4 - 30 lam'^2 - (3/2) w'^2
bound=sp.Rational(12)-sp.Rational(30,4)
test(f"Z-N5 12 - 30/4 = {bound} = 9/2 ; so -V <= (9/2)A'^2 - 30 lam'^2 - (3/2) w'^2, i.e. |V|/(12A'^2) <= {bound/12}",bound==sp.Rational(9,2) and bound/12==sp.Rational(3,8))
# at a potential-dominated point (velocities -> 0, 12A'^2 = -V, A'<0): comb/5 = -A' > 0 => some margin > 0 (no NEC face)
test("Z-N6 at zero scalar velocity comb = -5A' (>0 for A'<0)",sp.expand(comb.subs({p:0,l:0,u:0})+5*a)==0)
print(f"SUMMARY: {NP[0]} passed, {len(FAIL)} failed")
sys.exit(0 if not FAIL else 1)
