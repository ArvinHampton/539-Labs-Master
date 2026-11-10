from sympy import *
X,Y,n,k=symbols('X Y n k')
s=sqrt(35); eps=6+s
out=[]
def chk(name,cond): out.append(f"{'PASS' if cond else 'FAIL'}  {name}"); 
q=lambda a,b: a**2+7*a*b+Rational(7,2)*b**2
Q7=n**2+7*n*k+Rational(7,2)*k*(k+1)
beta_norm=(2*X+7*Y)**2-35*Y**2
chk("N(beta)/400 == q(X/10,Y/10)", simplify(beta_norm/400-q(X/10,Y/10))==0)
# nu=v+a with 10a=(7,-2)
nu1,nu2=n+Rational(7,10),k-Rational(2,10)
chk("q(v+a) == Q7(v) - 7/20", simplify(expand(q(nu1,nu2)-(Q7-Rational(7,20))))==0)
chk("Nm a = Nm(beta)/Nm(d')=20*Q7-7 (Nm d'=4*5)", simplify(expand(400*q(nu1,nu2)/20-(20*Q7-7)))==0)
chk("Nm eps=1", expand((6+s)*(6-s))==1)
chk("disc of quadratic part 7^2-4*1*(7/2)=35", 49-4*Rational(7,2)==35)
I=log(eps)/(2*s); out.append(f"I = {N(I,25)} (paper 0.209419820314714631473)")
out.append(f"2 log eps = {N(2*log(eps),15)}  (task 4.9558)")
aC=sqrt(pi)*(833+204*sqrt(14)-14*sqrt(1190))/2380; out.append(f"a_C = {N(aC,15)} (paper 0.8291426171)")
g=Matrix([[-1,-7],[2,13]]); out.append(f"gamma eigen {g.eigenvals()} det {g.det()}")
r1=Matrix([[1,7],[0,-1]]); r2=Matrix([[-1,0],[2,1]]); G=Matrix([[2,7],[7,7]])
chk("rho1,rho2 preserve Gram [[2,7],[7,7]]", r1.T*G*r1==G and r2.T*G*r2==G)
out.append(f"rho2*rho1 = {list(r2*r1)} (paper gamma {list(g)})")
# beta(gamma nu)= eps beta(nu): beta linear in nu: beta=10*((2nu1+7nu2)+nu2 s)
a,b=symbols('a b'); B=lambda v:(2*v[0]+7*v[1])+v[1]*s
for M,nm in [(g,'gamma'),(r2*r1,'rho2rho1'),(g.inv(),'gamma^-1')]:
  v=M*Matrix([a,b]); r=simplify(expand(B(v)-eps*B([a,b]))); r2_=simplify(expand(B(v)-(6-s)*B([a,b])))
  out.append(f"beta({nm} nu) - eps*beta = {r}; - eps^-1*beta = {r2_}")
# first norms 20Q7-7 over cone ... just list small values of 20Q7-7 positive
vals=sorted({20*(n_**2+7*n_*k_)+70*k_*(k_+1)-7 for n_ in range(-60,60) for k_ in range(-60,60)})
out.append("small positive values 20Q7-7: "+str([v for v in vals if v>0][:8]))
# eps congruences: eps mod p2: eps=6+s, p2=(2,1+s): s≡-1 -> eps≡5≡1 mod p2. p5=(5,s): eps≡6≡1
chk("eps ≡1 mod p2 (s≡-1, 6-1=5≡1 mod 2)", (6-1)%2==1)
chk("eps ≡1 mod p5 (s≡0 → 6≡1 mod 5)", 6%5==1)
# Gram diag(2,-70): |D|=140, sig 0; Fix(P) dim = #orbits of ± on Z/2 x Z/70
D=[(x,y) for x in range(2) for y in range(70)]
orb={min((x,y),((-x)%2,(-y)%70)) for x,y in D}
out.append(f"|disc grp|={len(D)}, #(+-)orbits = {len(orb)} (paper Fix(P) dim 72)")
out.append(f"Minkowski bound sqrt(140)/2 = {N(sqrt(140)/2,4)}")
open('verify_bridgeC.out','w').write("\n".join(map(str,out))); print("\n".join(map(str,out)))
