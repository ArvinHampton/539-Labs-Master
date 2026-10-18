# E-vector (gamma-fundamental-domain sums) radial expansions at rationals, exact finite EM formulas:
#   E_{al,be}(e(x)e^{-t}) = 2I*G_{al,be}(x)/t + a(x)/sqrt t + kappa(x) + O(sqrt t)
# F = C0 u rho2(C0):  C0 = {nu1>0, nu2>=0} (coords u=nu1 open, w=nu2 closed; Q2 = u^2+7uw+3.5w^2)
#                     rho2C0 = {nu = X(0,1)+Y(-1,2): X>0, Y>=0}  (Q2 = 3.5X^2+7XY+Y^2), X = nu2+2nu1, Y = -nu1.
# Then test the weight-1 S-cocycle at order t^0:  psi(x) = kappa_{a,b}(-1/x) - (x/sqrt35) e(B(a,b)) sum_p kappa_{b+p,-a}(x).
import cmath, math
from fractions import Fraction as Fr
exec(open('weil_test.py').read().split("out=[")[0])
def B1(u): return u-0.5
def B2(u): return u*u-u+1.0/6
SP=math.sqrt(math.pi)
def cone_terms(al,be,x,which):
    x=Fr(x); L=4*x.denominator
    if which==0: A11,A12,A22=1.0,3.5,3.5
    else:        A11,A12,A22=3.5,3.5,1.0
    s1=0; s0=0
    for i in range(L):
        for j in range(L):
            if which==0:
                u=(Fr(al[0])%1)+i; w=(Fr(al[1])%1)+j          # nu1=u, nu2=w
                if u==0: u=Fr(L)                                # u in (0,L]
                nu=(u,w)
            else:
                X0=(Fr(al[1])+2*Fr(al[0]))%1+i; Y0=(-Fr(al[0]))%1+j
                if X0==0: X0=Fr(L)
                u,w=X0,Y0; nu=(-Y0, X0+2*Y0)
            ph=cmath.exp(2j*math.pi*float((x*Qf(nu)+Bf(nu,be))%1))
            su=float(u)/L; sw=float(w)/L
            s1+=ph*(-B1(sw)*SP/(2*math.sqrt(A11)) - B1(su)*SP/(2*math.sqrt(A22)))/L
            s0+=ph*(B2(sw)*A12/(2*A11) + B2(su)*A12/(2*A22) + B1(su)*B1(sw))
    return s1,s0
def Eexp(al,be,x):
    a0,k0=cone_terms(al,be,x,0); a1,k1=cone_terms(al,be,x,1)
    return a0+a1, k0+k1
a=(Fr(7,10),Fr(-1,5)); zero=(Fr(0),Fr(0))
out=[]
# sanity at x=0 against em.py: E (with q^{7/20} shift removed) const = zeta(0) = 1/10, t^-1/2 = 0
aa,kk=Eexp(a,zero,Fr(0)) if False else Eexp(a,zero,Fr(1))
out.append(f"x=1 (trivial phase e(-7/20)): a = {aa:.3e}, kappa = {kk:.12f}  (expect a=0, kappa = e(-7/20)*1/10 = {0.1*cmath.exp(-2j*math.pi*0.35):.12f})")
# gamma-invariance of components
g=((-1,-7),(2,13))
def ginv(al,be):
    ga=(g[0][0]*al[0]+g[0][1]*al[1], g[1][0]*al[0]+g[1][1]*al[1]); ok1=all((ga[i]-al[i]).denominator==1 for i in range(2))
    # B(g nu, be) - B(nu, be) integral for nu in al+Z^2 : check on al and al+e_i
    ok2=True
    for d in [(0,0),(1,0),(0,1)]:
        nu=(al[0]+d[0],al[1]+d[1]); gn=(g[0][0]*nu[0]+g[0][1]*nu[1], g[1][0]*nu[0]+g[1][1]*nu[1])
        ok2 &= ((Bf(gn,be)-Bf(nu,be)).denominator==1)
    return ok1 and ok2
ninv=sum(1 for p in reps if ginv(p,neg(a)))
out.append(f"components (p,-a) that are gamma-invariant: {ninv}/35 ; (a,0) gamma-invariant: {ginv(a,zero)}")
for x in [Fr(1),Fr(1,3),Fr(2,3),Fr(1,7),Fr(1,2),Fr(2,5),Fr(3,4),Fr(3,7)]:
    aL,kL=Eexp(a,zero,-1/x)
    sa=0; sk=0
    for p in reps:
        ap,kp=Eexp(p,neg(a),x); sa+=ap; sk+=kp
    rhs_k=float(x)/math.sqrt(35)*sk
    out.append(f"x={str(x):4}: t^-1/2 coeff of E_(a,0) at -1/x: {abs(aL):.2e};  sum_p |.| at x: {abs(sa):.2e};   kappa_(a,0)(-1/x) = {kL.real:+.8f}{kL.imag:+.8f}i ;  (x/sqrt35) sum_p kappa_(p,-a)(x) = {rhs_k.real:+.8f}{rhs_k.imag:+.8f}i ;  psi = {(kL-rhs_k).real:+.8f}{(kL-rhs_k).imag:+.8f}i")
print("\n".join(out)); open("evector.txt","w").write("\n".join(out)+"\n")
