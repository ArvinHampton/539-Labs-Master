# Exact structure of P_s via the automorph group of Q2 (nu-coordinates nu = v + a, a = (7/10,-1/5)).
# Q_s(v) = Q2(v+a) + 7/20,  Q2(x,y) = x^2 + 7xy + (7/2)y^2.
import sys, math
import numpy as np, sympy as sp
N = int(sys.argv[1]) if len(sys.argv)>1 else 3000
out=[]
n,k,x,y = sp.symbols('n k x y')
R72 = sp.Rational(7,2)
Q2s = x**2+7*x*y+R72*y**2
assert sp.expand(Q2s.subs({x:n+sp.Rational(7,10), y:k-sp.Rational(1,5)},simultaneous=True) + sp.Rational(7,20) - (n**2+7*n*k+R72*k*(k+1))) == 0
out.append("PASS Q_s(v) = Q2(v+a) + 7/20, a = (7/10,-1/5)   [symbolic]")
r1 = sp.Matrix([[1,7],[0,-1]]); r2 = sp.Matrix([[-1,0],[2,1]]); g = r2*r1
for Mx in (r1,r2,g):
    Xv = Mx*sp.Matrix([x,y]); assert sp.expand(Q2s.subs({x:Xv[0],y:Xv[1]},simultaneous=True)-Q2s)==0
out.append(f"PASS rho1=[[1,7],[0,-1]], rho2=[[-1,0],[2,1]] (reflections, det -1, fixing the rays nu2=0 resp. nu1=0), gamma=rho2*rho1={g.tolist()} preserve Q2  [symbolic]")
out.append(f"     gamma eigenvalues {list(g.eigenvals())}  (6 +- sqrt35; eps = 6+sqrt35 is the fundamental unit, N(eps)=+1)")
av = sp.Matrix([sp.Rational(7,10),sp.Rational(-1,5)])
for nm,Mx in (("rho1",r1),("rho2",r2),("gamma",g)):
    d = Mx*av - av; d2 = Mx*av + av
    tgt = 'a' if all(t.q==1 for t in d) else ('-a' if all(t.q==1 for t in d2) else '?')
    out.append(f"     {nm} maps the coset a+Z^2 to {tgt}+Z^2")
# integer model: X = 10*nu1, Y = 10*nu2 ; 200*Q_s = 2X^2+14XY+7Y^2+70
NN, KK = 700, 450
nn = np.arange(-NN,NN+1)[:,None]; kk = np.arange(-KK,KK+1)[None,:]
def S_region(pred, sgn=+1):
    X = 10*nn + sgn*7; Y = 10*kk - sgn*2
    e200 = 2*X*X + 14*X*Y + 7*Y*Y + 70
    m = pred(X,Y) & (e200 <= 200*N)
    assert (e200[m] % 200 == 0).all()
    assert not (m[0,:].any() or m[-1,:].any() or m[:,0].any() or m[:,-1].any()), "box too small"
    return np.bincount((e200[m]//200).astype(np.int64), minlength=N+1)[:N+1]
def quad_pred(c1,c2):  # nu1 c1 0, nu2 c2 0
    return lambda X,Y: (c1(X)) & (c2(Y))
R   = S_region(lambda X,Y: (X>0)&(Y>0))            # n>=0, k>=1   (Q_s)
Mm  = S_region(lambda X,Y: (X<0)&(Y<0))            # n<=-1,k<=0  = C_third + sum_{n>=1} q^{n^2}
P   = S_region(lambda X,Y: (X>=7)&(Y>=-2))         # n>=0, k>=0  = P_s
th3 = np.zeros(N+1,dtype=np.int64)
for t in range(-100,101):
    if t*t<=N: th3[t*t]+=1
one = np.zeros(N+1,dtype=np.int64); one[0]=1
E = R + Mm
Theta_hol = Mm - R
def cone_pred(r):
    gr = (-r[0]-7*r[1], 2*r[0]+13*r[1]); assert r[0]*gr[1]-r[1]*gr[0] > 0
    return lambda X,Y: ((X*gr[1]-Y*gr[0])>0) & ((r[0]*Y-r[1]*X)>=0)
for r in [(1,0),(1,1),(7,-1),(1,2)]:
    Er = S_region(cone_pred(r))
    out.append(f"{'PASS' if (Er==E).all() else 'FAIL'} E := R + C_third + sum_(n>=1)q^(n^2)  ==  sum over the gamma-fundamental cone [r, gamma r) in S+, r = {r}   (to q^{N})")
out.append(f"{'PASS' if (2*P == E + one + th3 - Theta_hol).all() else 'FAIL'} 2 P_s = E + 1 + theta_3 - Theta_hol   (to q^{N})")
Em = S_region(cone_pred((1,0)), sgn=-1)
out.append(f"{'PASS' if (Em==E).all() else 'FAIL'} E_(-a) == E_a   (so the Hecke sign-twisted combination E_a - E_(-a) vanishes identically)")
out.append(f"E first coefficients: {list(E[:40])}")
# ray-class form
X,Y = sp.symbols('X Y'); s35=sp.sqrt(35)
beta = (2*X+7*Y) + Y*s35; betac = (2*X+7*Y) - Y*s35
assert sp.expand(beta*betac/400 - Q2s.subs({x:X/10,y:Y/10},simultaneous=True))==0
gX = g*sp.Matrix([X,Y]); bg = sp.expand((2*gX[0]+7*gX[1]) + gX[1]*s35)
out.append(f"PASS Q2(nu) = N(beta)/400 with beta = (2X+7Y)+Y*sqrt35, (X,Y)=10*nu;  beta(gamma nu) = eps*beta(nu): {sp.expand(bg-(6+s35)*beta)==0}")
# lattice of beta's
out.append("     (X,Y) in (7,-2)+10Z^2  <=>  beta in beta0 + 10*b,  b := Z*2 + Z*(7+sqrt35) (ideal of Z[sqrt35], index 2)")
b0 = sp.expand((2*7+7*(-2)) + (-2)*s35); out.append(f"     beta0 = beta(7,-2) = {b0}")
ok=True
for (Xs,Ys) in [(7,8),(17,-2),(-3,18),(27,-12)]:
    if 2*Xs*Xs+14*Xs*Ys+7*Ys*Ys>0:
        b1=(2*Xs+7*Ys)+Ys*math.sqrt(35); b2=(2*Xs+7*Ys)-Ys*math.sqrt(35); ok &= (b1>0 and b2>0)
out.append(f"{'PASS' if ok else 'FAIL'} sample points of S+ have beta totally positive")
print("\n".join(out)); open('structure.txt','w').write("\n".join(out)+"\n")
