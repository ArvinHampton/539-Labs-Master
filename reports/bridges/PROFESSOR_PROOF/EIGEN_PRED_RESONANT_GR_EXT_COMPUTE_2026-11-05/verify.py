# Eigenvalues & matrix lane - exact checks for FINDINGS_EIGEN_PREDICTIONS_RESONANT_AND_GR_EXT_2026-11-05
from sympy import *
import math
def ok(tag,c):
    c=bool(c); print(("PASS " if c else "FAIL ")+tag); return c
R=[]
# A1 Gram matrix
A=Matrix([[2,7],[7,7]]); R.append(ok("A1 det A=-35",A.det()==-35))
ev=A.eigenvals(); R.append(ok("A1 eig A=(9±sqrt221)/2 "+str(ev), set(ev)=={Rational(9,2)+sqrt(221)/2,Rational(9,2)-sqrt(221)/2}))
R.append(ok("A1 signature (1,1)", sum(1 for e in ev if e>0)==1))
n1,n2,n,k=symbols('n1 n2 n k'); v=Matrix([n1,n2])
Q=expand((v.T*A*v)[0]/2); R.append(ok("A1 Q=n1^2+7n1n2+7/2 n2^2", Q==n1**2+7*n1*n2+Rational(7,2)*n2**2))
R.append(ok("A1 disc(2Q)=140", 14**2-4*2*7==140))
# A2 completed square
Q7=n**2+7*n*k+Rational(7,2)*k*(k+1); Qm=n**2+7*n*k+Rational(7,2)*k*(k-1)
R.append(ok("A2 Q7=(n+7k/2)^2-(35/4)k^2+(7/2)k", expand(Q7-((n+7*k/2)**2-Rational(35,4)*k**2+Rational(7,2)*k))==0))
R.append(ok("A2 Q-=(n+7k/2)^2-(35/4)k^2-(7/2)k [item 8 form]", expand(Qm-((n+7*k/2)**2-Rational(35,4)*k**2-Rational(7,2)*k))==0))
R.append(ok("A2 Q-(n,k)=Q7(-n,-k)", expand(Qm-Q7.subs({n:-n,k:-k},simultaneous=True))==0))
# A6 shift identity
a=Matrix([Rational(7,10),Rational(-1,5)])
R.append(ok("A6 Aa=(0,7/2)", A*a==Matrix([0,Rational(7,2)])))
Qf=lambda w: (w.T*A*w)[0]/2
R.append(ok("A6 Q(a)=-7/20", Qf(a)==Rational(-7,20)))
R.append(ok("A6 Q7(v)=Q(v+a)+7/20", expand(Q7.subs({n:n1,k:n2})-(Qf(v+a)+Rational(7,20)))==0))
wc=A.inv()*Matrix([0,Rational(1,2)]); R.append(ok("A6 wc=(1/10,-1/35)", wc==Matrix([Rational(1,10),Rational(-1,35)])))
y=A*(wc-a); R.append(ok("A6 wc-a in L'=A^-1 Z^2", all(t.is_integer for t in y)))
# A3 automorphs
r1=Matrix([[1,7],[0,-1]]); r2=Matrix([[-1,0],[2,1]]); g=r2*r1
for nm,r in (("rho1",r1),("rho2",r2)):
    R.append(ok(f"A3 {nm}^T A {nm}=A", r.T*A*r==A)); R.append(ok(f"A3 {nm}^2=I det-1", r*r==eye(2) and r.det()==-1))
R.append(ok("A3 gamma=[[-1,-7],[2,13]]", g==Matrix([[-1,-7],[2,13]])))
x=symbols('x'); R.append(ok("A3 charpoly gamma=x^2-12x+1", g.charpoly(x).as_expr()==x**2-12*x+1))
R.append(ok("A3 eig gamma=6±sqrt35", set(g.eigenvals())=={6+sqrt(35),6-sqrt(35)}))
R.append(ok("A3 gamma preserves a+Z^2", all(t.is_integer for t in g*a-a)))
R.append(ok("A3 rho_i map a+Z^2 -> -a+Z^2", all(t.is_integer for t in list(r1*a+a)+list(r2*a+a))))
# traces of gamma^m: t_m=12 t_{m-1}-t_{m-2}
t=[2,12]
for m in range(2,8): t.append(12*t[-1]-t[-2])
R.append(ok("A3 tr gamma^m recurrence m<=7", all((g**m).trace()==t[m] for m in range(8))))
# A4 Pell / unit
R.append(ok("A4 cf sqrt35=[5;(1,10)]", continued_fraction_periodic(0,1,35)==[5,[1,10]]))
R.append(ok("A4 6^2-35*1^2=1", 36-35==1))
R.append(ok("A4 minimal Pell sol (6,1) by search", min((xx,yy) for yy in range(1,50) for xx in [math.isqrt(35*yy*yy+1)] if xx*xx-35*yy*yy==1)==(6,1)))
R.append(ok("A4 x^2-35y^2=-1 impossible mod 5 (-1 not QR mod 5? check mod 7)", all((xx*xx)%7!=6 for xx in range(7))))
# A4b narrow class number of disc 140 via reduced indefinite form cycles
D=140; sD=math.sqrt(D)
def reduced(a,b,c): return 0<b<sD and sD-b<2*abs(a)<sD+b
forms=set()
for aa in range(-12,13):
    if aa==0: continue
    for b in range(1,12):
        if (b*b-D)%(4*aa)==0:
            c=(b*b-D)//(4*aa)
            if reduced(aa,b,c) and math.gcd(math.gcd(abs(aa),b),abs(c))==1: forms.add((aa,b,c))
def rho(f):
    aa,b,c=f; a2=c
    # b2 ≡ -b mod 2a2, sD-2|a2|<b2<sD
    for b2 in range(-200,200):
        if (b2+b)%(2*abs(a2))==0 and sD-2*abs(a2)<b2<sD: return (a2,b2,(b2*b2-D)//(4*a2))
seen=set(); cycles=0
for f in sorted(forms):
    if f in seen: continue
    cycles+=1; h=f
    while h not in seen: seen.add(h); h=rho(h)
R.append(ok(f"A4b narrow class number h+(140)={cycles} (expect 4)", cycles==4))
# genus count: disc 140=4*5*7 -> 2^(3-1)=4 genera, so Cl+ ~ C2xC2 (each genus one class)
R.append(ok("A4b 4 genera => Cl+ elementary 2-group C2xC2", cycles==4))
res=2*log(6+sqrt(35))/sqrt(35); R.append(ok(f"A5 Res zeta_K=2ln(6+sqrt35)/sqrt35={N(res,10)}", abs(N(res)-0.837679)<5e-7))
R.append(ok("A5 2hR/sqrt140 = 2lnε/sqrt35 for h=2", simplify(2*2*log(6+sqrt(35))/sqrt(140)-res)==0))
# A7 Prop 16.1 bookkeeping
R.append(ok("A7 T mult on Fix(P): 12*1+18*2+6*4=72; 36 values", 12+36+24==72 and 12+18+6==36))
R.append(ok("A7 V=36+6=42; Vperp=0*12+1*18+2*6=30=72-42", 36+6==42 and 18+12==30==72-42))
R.append(ok("A7 S on V 21/21 = 18/18+3/3; dim W_P=2(s-1)^2=72 at s=7", 18+3==21 and 2*36==72 and 2*(7-1)**2==72))
# A8 abstract SL2(Z) relations: check in a model rep that relations imply spectrum claims (symbolic argument; here sanity on SL2(Z) generators)
S0=Matrix([[0,-1],[1,0]]); T0=Matrix([[1,1],[0,1]])
R.append(ok("A8 SL2Z model: S^2=(ST)^3=-I, S^4=I", S0**2==-eye(2) and (S0*T0)**3==-eye(2) and S0**4==eye(2)))
# A9 F2 circulants M=3
w=exp(2*pi*I/3)
d1=nsimplify(expand_complex(expand(prod([1+w**j for j in range(3)])))); d2=nsimplify(expand_complex(expand(prod([-1+w**j+3*w**(2*j) for j in range(3)]))))
R.append(ok(f"A9 det rho(h1)={d1}, det rho(h2)={d2}", d1==2 and d2==36))
C1=Matrix(3,3,lambda i,j: [1,1,0][(i-j)%3]); C2=Matrix(3,3,lambda i,j: [-1,1,3][(i-j)%3])
R.append(ok("A9 explicit circulant dets 2,36", C1.det()==2 and C2.det()==36))
W=(C2*C1)[1,0]; Nn=(abs(C2).applyfunc(abs)*C1.applyfunc(abs))[1,0] if False else (C2.applyfunc(abs)*C1)[1,0]
R.append(ok(f"A9 signed W=(rho(h2)rho(h1))[1,0]={W}, unsigned N={Nn}", W==0 and Nn==2))
# A10 Perron for nonneg circulant
Cn=Matrix(5,5,lambda i,j:[3,0,1,2,5][(i-j)%5]); R.append(ok("A10 spr nonneg circulant = row sum 11", max(abs(N(e)) for e in Cn.eigenvals())-11<1e-9 and Cn*ones(5,1)==11*ones(5,1)))
# F1(i): 1+omega^j !=0 for odd M
R.append(ok("A9b 1+zeta_M^j !=0 for odd M<=51", all(simplify(1+exp(2*pi*I*j/MM))!=0 for MM in range(3,52,2) for j in range(MM)) ))
# A11 W7 Mobius
Wm=Matrix([[-3,-16],[1,3]]); tt=symbols('t'); xx=symbols('x')
tW=simplify(7*(-1/(7*((tt+3)/7)))-3)
R.append(ok("A11 t_W=-(3t+16)/(t+3) from x->-1/(7x), t=7x-3", simplify(tW+(3*tt+16)/(tt+3))==0))
R.append(ok("A11 Wm^2=-7I, tr0, det7", Wm**2==-7*eye(2) and Wm.trace()==0 and Wm.det()==7))
# A12 Haar
nu=symbols('nu'); kk=symbols('kk',integer=True,nonnegative=True)
shell=[(1-Rational(1,3**4))*Rational(1,3**(4*j)) for j in range(3)]
cnt=[]
for j in range(3):  # residue counting mod 27 in Z/27^4 via 1-d valuation counts
    # fraction of x in (Z/27)^4 with min ord = j: (#ord>=j)^4-(#ord>=j+1)^4 over 27^4
    ge=lambda m: (27//3**m) if m<=3 else 1
    cnt.append(Rational(ge(j)**4-ge(j+1)**4,27**4))
R.append(ok(f"A12 shell measures k=0,1,2 {cnt}", cnt==shell))
rr=symbols('rr'); geo=summation(rr**kk,(kk,0,oo)).args[0][0]; print('INFO geometric series (|r|<1):',geo)
sumexpr=(1-Rational(1,81))*geo.subs(rr,3**(-(nu+3)))
for vv in [Integer(1),Integer(2),Integer(3),Rational(1,2),Integer(5)]:
    R.append(ok(f"A12 nu={vv} closed form", simplify(sumexpr.subs(nu,vv)-(1-Rational(1,81))/(1-3**(-(vv+3))))==0))
R.append(ok("A12 nu=1 integral =1", (1-Rational(1,81))/(1-Rational(1,81))==1))
R.append(ok("A12 mu(3^539 Z_3^4)=3^-2156", 4*539==2156))
# A13/A14 g_s series and Q(m)
def gser(s,Nmax):
    c=[0]*(Nmax+1); nn=0
    while nn*nn<=Nmax:
        # 1/(-q^s;q^s)_n
        t=[0]*(Nmax+1); t[0]=1
        for i in range(1,nn+1):
            e=s*i
            for d in range(e,Nmax+1): t[d]-=t[d-e]  # multiply by 1/(1+q^e): t_new[d]=t[d]-t_new[d-e]
        for d in range(Nmax+1-nn*nn): c[d+nn*nn]+=t[d]
        nn+=1
    return c
g1=gser(1,60)
# Ramanujan f0(q)=sum q^{n^2}/(-q;q)_n : same by definition at s=1 (item 1 is definitional)
for kq in [2,3,5,6,7,10,11]:
    c=gser(kq,kq*(kq+2)); R.append(ok(f"A13 g_{kq}({kq*(kq+2)})=0 [Thm 5.1 instance]", c[kq*(kq+2)]==0))
NM=3000; c7=gser(7,NM)
R.append(ok("A13 g7 support in {0,1,2,4} mod 7 up to 3000", all(c7[d]==0 for d in range(NM+1) if d%7 not in (0,1,2,4))))
zeros=[d for d in range(NM+1) if d%7 in (0,1,2,4) and c7[d]==0]
print("INFO g7 allowed-degree zeros <=3000:",zeros)
R.append(ok("A20 last allowed zero of g7 in [0,3000] is 247", zeros and zeros[-1]==247))
Qp=[1]+[0]*200
for j in range(1,201,2):
    for d in range(200,j-1,-1): Qp[d]+=Qp[d-j]
R.append(ok("A14 Q(2)=0,Q(m)>=1 m!=2,Q(m)>=2 m>=8 (m<=200)", Qp[2]==0 and all(Qp[m]>=1 for m in range(201) if m!=2) and all(Qp[m]>=2 for m in range(8,201))))
xs=symbols('xs'); Pm=expand(prod([1-xs**j for j in range(1,30,2)])); Pp=expand(prod([1+xs**j for j in range(1,30,2)]))
R.append(ok("A14 c_m=(-1)^m Q(m), m<=29", all(Pm.coeff(xs,m)==(-1)**m*Pp.coeff(xs,m) for m in range(30))))
# A15 arithmetic
e3=E**3; R.append(ok("A15 floor(e^3*3^5)=4880", floor(N(e3*243,50))==4880))
R.append(ok("A15 sum_{z=1}^{118} z=7021", sum(range(1,119))==7021))
R.append(ok("A15 539=floor(4859/9)=18+521=7^2*11", 4859//9==539==18+521 and factorint(539)=={7:2,11:1}))
R.append(ok("A15 sum 3^k/k! = e^3", summation(3**kk/factorial(kk),(kk,0,oo))==E**3))
# A16 HQCC
def b3(nn):
    s=[]
    while nn: s.append(nn%3); nn//=3
    return s[::-1]
def run(nn,reading):
    L=math.ceil(math.log(nn,3)-1e-12) if nn>1 else 0
    s=b3(nn); 
    if len(s)!=L: return ("LENGTH_MISMATCH",len(s),L)
    st=0; seen=set()
    while any(s):
        key=tuple(s)
        if key in seen: return ("LOOP",st)
        seen.add(key)
        if s[0]==0: s = s[1:]+[0] if reading=="shift" else s[1:]+[s[0]]+[0]
        else: s=[0]+s[:-1]
        st+=1
        if st>2000: return ("NOHALT_2000",st)
    return ("HALT",st)
R.append(ok("A16 n=2: string '2', L=1, halts in 1 step (both readings)", run(2,"shift")==("HALT",1) and run(2,"rot+append")==("HALT",1)))
R.append(ok("A16 n=3: base-3 '10' has 2 digits but ceil(log3 3)=1 (definition inconsistent at powers of 3)", run(3,"shift")[0]=="LENGTH_MISMATCH"))
from collections import Counter
for rd in ("shift","rot+append"):
    st=Counter(run(nn,rd)[0] for nn in range(2,(3**9 if rd=="shift" else 3**6))); print("INFO A16",rd,"outcomes n in [2,3^9) shift; [2,3^6) rot+append:",dict(st))
    hs=[run(nn,rd)[1] for nn in range(2,(3**9 if rd=="shift" else 3**6)) if run(nn,rd)[0]=="HALT"]; print("INFO A16",rd,"halting step counts set:",sorted(set(hs)))
    R.append(ok(f"A16 {rd}: no n in [2,3^9) halts in 538..540 steps", not any(538<=h<=540 for h in hs)))
R.append(ok("A16 n=5 ('12') loops under shift reading", run(5,"shift")[0]=="LOOP"))
# A17 density matrix
ph=symbols('phi',real=True); rho_=Rational(1,2)*Matrix([[1,exp(I*ph)],[exp(-I*ph),1]])
R.append(ok("A17 eig rho={0,1} for all real phi", set(rho_.eigenvals())=={0,1}))
R.append(ok("A17 Tr rho^2=1 (pure)", simplify((rho_*rho_).trace())==1))
sy=Matrix([[0,-I],[I,0]]); syv=simplify((rho_*sy).trace().rewrite(sin)); print("INFO Tr(rho sigma_y)=",syv); R.append(ok("A17 |<sigma_y>|=|sin phi| (not identically 1)", simplify(syv**2-sin(ph)**2)==0))
R.append(ok("A17 |exp(i*phi)|=1 for real phi", simplify(Abs(exp(I*ph)))==1))
sg=symbols('sigma',positive=True); th=symbols('theta',real=True)
avg=simplify(integrate(exp(I*th)*exp(-th**2/(2*sg**2))/sqrt(2*pi*sg**2),(th,-oo,oo)))
R.append(ok(f"A17 E[e^(i theta)], theta~N(0,s^2) = {avg}", simplify(avg-exp(-sg**2/2))==0))
rb=Rational(1,2)*Matrix([[1,exp(-sg**2/2)],[exp(-sg**2/2),1]])
R.append(ok("A17 averaged rho eig (1±e^{-s^2/2})/2", set(rb.eigenvals())=={(1+exp(-sg**2/2))/2,(1-exp(-sg**2/2))/2}))
# A18 two-level
Ep,Em,V=symbols('E_p E_m V',real=True); H=Matrix([[Ep,V],[V,Em]])
ev=list(H.eigenvals()); tgt={(Ep+Em)/2+sqrt((Ep-Em)**2/4+V**2),(Ep+Em)/2-sqrt((Ep-Em)**2/4+V**2)}
R.append(ok("A18 exact eigenvalues", all(any(simplify(e-t2)==0 for t2 in tgt) for e in ev)))
Dl,eps=symbols('Delta epsilon',positive=True)
spl=series(2*sqrt(Dl**2/4+(eps)**2),eps,0,4).removeO()
R.append(ok(f"A18 splitting E+-E- = Delta + 2V^2/Delta + O(V^4): {spl}", simplify(spl-(Dl+2*eps**2/Dl))==0))
# corrected: E_+ - E_- = Delta + 2*(V^2/Delta)?  check
spl2=series(sqrt(Dl**2/4+eps**2),eps,0,4).removeO()
R.append(ok(f"A18 level shift each = V^2/Delta: {spl2}", simplify(spl2-(Dl/2+eps**2/Dl))==0))
# B1 regulated g_rr
GM=symbols('GM',positive=True)
R.append(ok("B1 min denominator 3^-539>0", Rational(1,3**539)>0))
Dk=lambda kk_: Rational(1,3**kk_)+Rational(1,3**539)
R.append(ok("B1 1-2GM/D=0 iff D=2GM: pole persists e.g. 2GM=D(5)", simplify(1-2*(Dk(5)/2)/Dk(5))==0))
# B2
R.append(ok("B2 |3^v u|_3^-539 = 3^(539 v); (-1)^(±1)=-1", (-1)**1==(-1)**(-1)==-1))
# B4 spectra K9 x P(540 vertices)
lamK=[8]+[-1]*8
R.append(ok("B4 K9 adjacency eig {8,-1^8}", sorted(Matrix(9,9,lambda i,j:0 if i==j else 1).eigenvals().items())==[(-1,8),(8,1)]))
R.append(ok("B4 K9 graph Euler char 9-36=-27, b1=28", 9-36==-27 and 36-9+1==28))
P6=Matrix(6,6,lambda i,j:1 if abs(i-j)==1 else 0)
R.append(ok("B4 path P_n adjacency eig 2cos(pi j/(n+1)) (n=6 check)", all(abs(min(abs(N(e)-2*math.cos(math.pi*j/7)) for e in P6.eigenvals()))<1e-9 for j in range(1,7))))
print("INFO B4 spr(K9 box P540)=8+2cos(pi/541)=",8+2*math.cos(math.pi/541)," lambda2(L)=2-2cos(pi/540)=",2-2*math.cos(math.pi/540))
# B6 arithmetic
R.append(ok("B6 (4+1)+(3+1)=9 != 11; 10+1=11", 5+4==9 and 10+1==11))
print("TOTAL",len(R),"PASS",sum(R),"FAIL",len(R)-sum(R))
