# PP exact checker for MR2 wall Bianchi / J_M5 filing 79795981 (2026-11-10). Exact sympy only: expand/cancel == 0 on
# polynomial/rational identities, exact Rational comparisons, exact definite integrals. No floats used as grounds.
import sympy as sp, itertools, hashlib
V2='/workspace/quantum-comp/reports/MR2_TWISTED_VACUA_ADOPTION_BLOCKERS_RIEMANN_SYSTOLE_FULL_EOM_2026-11-09_V2.py'
raw=open(V2,'rb').read(); h=hashlib.sha256(raw).hexdigest(); assert h=='ad134752da79e3064e209cd840b0aec53e004e3fa0fec8bbc9299eb12940eb85'
import contextlib, io
with contextlib.redirect_stdout(io.StringIO()):
    exec(raw.decode().split('# ======================= MAIN =======================')[0])
def P(*a): print(*a, flush=True)
P("V2 sha", h)
# ---- C1: MN2 fixed point exact: X1^5 = 1/8, X2 = 2 X1, hence X0 = (X1 X2)^-2 = X2 = 2^(2/5)
fp=FP["MN2(z=1)"]; X1e,X2e=fp['X1'],fp['X2']
x15=sp.nsimplify(sp.limit(X1_5,zs,1)); P("C1 limit X1^5 =",x15, "| equals 1/8:", x15==sp.Rational(1,8))
P("C1 ratio(z=1) =", sp.nsimplify(ratio.subs(zs,1)), "| X2/X1 == 2:", sp.nsimplify(X2e/X1e)==2)
# with X1^5=1/8: X0 = (X1*2X1)^-2 = X1^-4/4 ; X0 - X2 = X1^-4/4 - 2X1 = (1 - 8 X1^5)/(4 X1^4) = 0
q=sp.symbols('q',positive=True); P("C1 X0-X2 numerator (1-8q^5)/(4q^4):", sp.cancel((q**-4/4-2*q) - (1-8*q**5)/(4*q**4))==0)
P("C1 a1,a2 =", fp['a1'], fp['a2'])
# ---- C2: U = p^2 (s-4) exactly at X0=X2=p, X1=p/2, s=mu1^2, mu0^2 = 1 - s - mu2^2
p,s,M2=sp.symbols('p s M2',positive=True)
Xa=[p,p/2,p]; mu2sq=[1-s-M2,s,M2]
D=sum(Xa[k]*mu2sq[k] for k in range(3))
U=4*sum(Xa[k]**2*mu2sq[k]-D*Xa[k] for k in range(3))+2*D*Xa[0]
P("C2 expand(U - p^2(s-4)) == 0:", sp.expand(U-p**2*(s-4))==0, "| expand(D - p(1-s/2)) == 0:", sp.expand(D-p*(1-s/2))==0)
# ---- C3: generic block structure -> (*Omega)_{alpha beta phi1 phi2}
A=sp.symbols('A0:5'); S,w=sp.symbols('S w',positive=True); h11,h12,h22,f1,f2,b1,b2=sp.symbols('h11 h12 h22 f1 f2 b1 b2')
G=sp.zeros(11)
for i in range(5): G[i,i]=A[i]
G[5,5]=S+f1*b1**2+f2*b2**2; G[6,6]=S
G[7,7]=h11;G[7,8]=G[8,7]=h12;G[8,8]=h22
G[9,9]=f1;G[10,10]=f2;G[9,5]=G[5,9]=f1*b1;G[10,5]=G[5,10]=f2*b2
Gi=G.inv(method='LU').applyfunc(sp.cancel)
Bfib=sp.Matrix([[h11,h12,0,0],[h12,h22,0,0],[0,0,f1,0],[0,0,0,f2]])
P("C3 det G == prod(A) S^2 det(fib):", sp.cancel(G.det()-sp.prod(A)*S**2*Bfib.det())==0)
P("C3 row v of G^-1 only (v,v):", all(Gi[6,j]==0 for j in range(11) if j!=6), "| G^vv = 1/S:", sp.cancel(Gi[6,6]-1/S)==0, "| G^uu = 1/S:", sp.cancel(Gi[5,5]-1/S)==0)
B=tuple(range(7)); detBB=sp.cancel(sp.Matrix([[Gi[b,c] for c in B] for b in B]).det())
P("C3 det(G^{B,B}), B=(0..6) == 1/(prod A S^2):", sp.cancel(detBB-1/(sp.prod(A)*S**2))==0)
# any C != B with 6 not in C gives a zero row (row 6) -> zero minor; all non-eps7 Omega comps in V2 omit index 6:
P("C3 V2 Omega comps other than (0..6) contain index 6:", any(6 in k for k in Omega_sym()[0] if k!=tuple(range(7))))
# ---- C4: V2 cand_metric structure: g_(phi_k,u) = g_(phi_k phi_k) a_k/v ; g_(phi2, *) = 0 off-diagonal at a2=0 ; phi-independence
GC=cand_metric()
P("C4 g(phi1,u) - g(phi1,phi1) a1/v == 0:", sp.expand(GC[9,5]*v-GC[9,9]*a1s)==0)
P("C4 g(phi2,u) == g(phi2,phi2) a2/v:", sp.expand(GC[10,5]*v-GC[10,10]*a2s)==0, "| at a2=0:", GC[10,5].subs(a2s,0)==0)
P("C4 nonzero pattern:", sorted((i,j) for i in range(11) for j in range(i,11) if GC[i,j]!=0))
P("C4 metric independent of phi1, phi2, u:", all(sp.diff(GC[i,j],x)==0 for i in range(11) for j in range(11) for x in (p1,p2,u)))
# ---- C5: sqrt det g_fib exactly. g_fib = c h, c = D^(-2/3)/4 ; check det h = D sin^2(a) mu1^2 mu2^2 /(X0 X1^2 X2^2) for GENERIC X0,X1,X2
ca,sa,cb,sb=sp.symbols('ca sa cb sb'); Y0,Y1,Y2=sp.symbols('Y0 Y1 Y2',positive=True)
mm=[ca,sa*cb,sa*sb]; dmm=[[-sa,0],[ca*cb,-sa*sb],[ca*sb,sa*cb]]; Ys=[Y0,Y1,Y2]
H=sp.zeros(4)
for i in range(2):
    for j in range(2): H[i,j]=sum(dmm[k][i]*dmm[k][j]/Ys[k] for k in range(3))
H[2,2]=mm[1]**2/Y1; H[3,3]=mm[2]**2/Y2
Dg=sum(Ys[k]*mm[k]**2 for k in range(3))
expr=sp.expand((H.det()-Dg*sa**2*mm[1]**2*mm[2]**2/(Y0*Y1**2*Y2**2))*Y0**2*Y1**3*Y2**3)
red=sp.expand(expr.subs(ca**2,1-sa**2).subs(cb**2,1-sb**2))
red=sp.expand(sp.expand(red).subs({ca**4:(1-sa**2)**2,cb**4:(1-sb**2)**2}))
P("C5 det h identity (poly reduction mod ca^2+sa^2=1, cb^2+sb^2=1) == 0:", sp.expand(sp.Poly(red,ca,cb).as_expr().subs({ca**2:1-sa**2,cb**2:1-sb**2}))==0)
P("C5 V2 fibre block equals c*h with c=D^(-2/3)/4 (by construction, V2 lines 236-243); X0*X1^2*X2^2 = 1 since X0=(X1X2)^-2")
# hence sqrt det g_fib = (1/16) D^(-5/6) sin(a)|mu1 mu2| = (1/16) D^(-5/6) sin^3(a) cos(b) sin(b) on the chart
# ---- C6: exact integral of G4_fib (kappa=1) = U D^(-7/6) sqrt det g_fib = (1/16) U D^-2 sin^3 a cos b sin b
x,t=sp.symbols('x t',real=True); a_=1-x**2   # x = cos(alpha), a_ = sin^2 alpha ; t = cos^2 beta
inner=sp.integrate(4*(a_*t-4)/(2-a_*t)**2,(t,0,1))/2      # U/D^2 = 4(s-4)/(2-s)^2, s = a_ t ; d(beta) measure -> dt/2
outer=sp.simplify(sp.integrate(sp.simplify(a_*inner),(x,-1,1)))
P("C6 int_alpha int_beta (U/D^2) sin^3 cos sin =", outer)
tot=sp.simplify(4*sp.pi**2/16*outer); P("C6 int G4_fib (kappa=1) over fibre =", tot, "| == -pi^2:", sp.simplify(tot+sp.pi**2)==0)
# ---- C7: p1(Lambda2 +/-) = p1 +/- 2e at form level, generic curvature (36 symbols), script fibre4 conventions
Rh={}
pairs4=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
for (i,j) in pairs4:
    M=sp.zeros(4)
    for a in range(4):
        for b in range(a+1,4):
            z=sp.Symbol(f'R{i}{j}_{a}{b}'); M[a,b]=z; M[b,a]=-z
    Rh[(i,j)]=M
comb=[((0,1),(2,3),1),((0,2),(1,3),-1),((0,3),(1,2),1),((1,2),(0,3),1),((1,3),(0,2),-1),((2,3),(0,1),1)]
PI2=sp.pi**2
def psign(seq):
    seq=list(seq); s_=1
    for i in range(len(seq)):
        for j in range(i+1,len(seq)):
            if seq[i]>seq[j]: s_=-s_
    return s_
eu=0
for a,b,c,d in itertools.permutations(range(4)):
    for (Aa,Bb,s_) in comb: eu+=psign((a,b,c,d))*s_*Rh[Aa][a,b]*Rh[Bb][c,d]
eu=eu/(32*PI2)
star={(0,1):((2,3),1),(0,2):((1,3),-1),(0,3):((1,2),1),(1,2):((0,3),1),(1,3):((0,2),-1),(2,3):((0,1),1)}
Sm=sp.zeros(6)
for k,pk in enumerate(pairs4):
    qq,s_=star[pk]; Sm[pairs4.index(qq),k]=s_
def ad(M):
    out=sp.zeros(6)
    for k,(a,b) in enumerate(pairs4):
        for c in range(4):
            for (xx,yy,ww) in ((c,b,M[c,a]),(a,c,M[c,b])):
                if xx==yy or ww==0: continue
                if xx<yy: out[pairs4.index((xx,yy)),k]+=ww
                else: out[pairs4.index((yy,xx)),k]-=ww
    return out
adR={k:ad(Rh[k]) for k in Rh}
TT=lambda X_,Y_: (X_*Y_).trace()
p1f=-(2*(TT(Rh[(0,1)],Rh[(2,3)])-TT(Rh[(0,2)],Rh[(1,3)])+TT(Rh[(0,3)],Rh[(1,2)])))/(8*PI2)
P("C7 star^2 == +1 on Lambda^2:", Sm*Sm==sp.eye(6))
for sg in (1,-1):
    Pm=(sp.eye(6)+sg*Sm)/2
    t_=lambda X_,Y_: (Pm*adR[X_]*adR[Y_]).trace()
    res=-(2*(t_((0,1),(2,3))-t_((0,2),(1,3))+t_((0,3),(1,2))))/(8*PI2)
    P(f"C7 sigma={sg:+d}: expand(p1(L2) - (p1 {'+' if sg>0 else '-'} 2e)) == 0:", sp.expand((res-(p1f+sg*2*eu))*PI2)==0)
P("done")
