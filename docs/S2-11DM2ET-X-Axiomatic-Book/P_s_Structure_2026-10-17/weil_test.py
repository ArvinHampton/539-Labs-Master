# Vector-valued route: leading radial profiles G_{al,be}(x) = mean over nu in al+Z^2 of e(x Q2(nu) + B(nu,be)).
# For the cone sums P_{al,be} := sum_{nu in C0 cap (al+Z^2)} e(B(nu,be)) q^{Q2(nu)}, t*P -> I*G_{al,be}(x) (same argument as Lemma 3).
# Test the weight-1 law predicted by Zwegers Cor. 2.9(4)-(5) (r=2, det A=-35) at the level of these profiles:
#   (S)  G_{a,b}(-1/x) = (1/(sqrt35 x)) e(B(a,b)) sum_{p in A^-1Z^2/Z^2} G_{b+p,-a}(x)
#   (T)  G_{a,b}(x+1)  = e(Q(a) + B(A^-1 A*, a)/2) G_{a, a+b+A^-1A*/2}(x)    [sign of exponent fixed by Cor 2.9(4) with tau->x]
import cmath, math, itertools
from fractions import Fraction as Fr
A=((2,7),(7,7))
def Bf(u,v): return sum(u[i]*A[i][j]*v[j] for i in range(2) for j in range(2))
def Qf(u): return Fr(Bf(u,u),2)
def G(al,be,x):
    x=Fr(x); m=x.denominator; L=2*m*2
    s=0
    for n in range(L):
        for k in range(L):
            nu=(al[0]+n, al[1]+k)
            ph=(x*Qf(nu)+Bf(nu,be)) % 1
            s+=cmath.exp(2j*math.pi*float(ph))
    return s/L**2
Ainv=((Fr(-1,5),Fr(1,5)),(Fr(1,5),Fr(-2,35)))
reps=set()
for u in range(35):
    for w in range(35):
        p=((Ainv[0][0]*u+Ainv[0][1]*w)%1,(Ainv[1][0]*u+Ainv[1][1]*w)%1); reps.add(p)
reps=sorted(reps); assert len(reps)==35
a=(Fr(7,10),Fr(-1,5)); zero=(Fr(0),Fr(0))
neg=lambda u:(-u[0],-u[1]); addv=lambda u,v:(u[0]+v[0],u[1]+v[1])
out=[f"discriminant group A^-1Z^2/Z^2: {len(reps)} classes"]
def testS(al,be,x):
    lhs=G(al,be,-1/Fr(x))
    rhs=cmath.exp(2j*math.pi*float(Bf(al,be)%1))/(math.sqrt(35)*float(x))*sum(G(addv(be,p),neg(al),x) for p in reps)
    return lhs,rhs
worst=0
for (al,be,lab) in [(a,zero,"(a,0)"),(reps[3],neg(a),"(p3,-a)"),(addv(a,reps[7]),reps[2],"(a+p7,p2)")]:
    for x in [Fr(1),Fr(1,3),Fr(2,3),Fr(1,7),Fr(3,7),Fr(5,7),Fr(1,2),Fr(2,5),Fr(3,4)]:
        l,r=testS(al,be,x); worst=max(worst,abs(l-r))
        out.append(f"S-law {lab:10} x={str(x):4}: LHS={l.real:+.10f}{l.imag:+.10f}i  RHS={r.real:+.10f}{r.imag:+.10f}i  |diff|={abs(l-r):.1e}")
out.append(f"max |LHS-RHS| over S-tests: {worst:.2e}")
# T-law
Astar=(2,7); hA=(Fr(1,2)*(Ainv[0][0]*2+Ainv[0][1]*7), Fr(1,2)*(Ainv[1][0]*2+Ainv[1][1]*7))   # A^-1 A*/2
worstT=0
for (al,be) in [(a,zero),(reps[5],neg(a))]:
    for x in [Fr(1,3),Fr(2,7),Fr(1,2)]:
        lhs=G(al,be,x+1)
        for sgn in (+1,-1):
            ph=sgn*(Qf(al)+Bf(addv(hA,hA),al)/2)   # Q(a) + 1/2 B(A^-1A*, a)
            rhs=cmath.exp(2j*math.pi*float(ph%1))*G(al,addv(addv(al,be),hA),x)
            if sgn==-1: dneg=abs(lhs-rhs)
            else: dpos=abs(lhs-rhs)
        out.append(f"T-law al={al},be={be}, x={x}: |diff| with phase e(+(Q(a)+B/2)) = {dpos:.1e}, e(-(...)) = {dneg:.1e}")
print("\n".join(out)); open("weil_test.txt","w").write("\n".join(out)+"\n")
