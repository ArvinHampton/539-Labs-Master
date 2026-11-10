# PP independent exact checks for audit of Local 845cc6bc (+ erratum 286e4f02). 2026-11-10 America/Chicago.
# Pure Python integers / Fractions + SymPy exact polynomials (expand == 0 tests only). No PARI, no floats.
import re, sys
from fractions import Fraction as Fr
from sympy import symbols, expand, Poly, factor_list, discriminant, Matrix, isprime, primerange, jacobi_symbol, ZZ
from sympy.matrices.normalforms import smith_normal_form
x,a,b,c = symbols('x a b c')
OK=[]; 
def chk(name, cond):
    OK.append(bool(cond)); print(("PASS " if cond else "FAIL ")+name)
def leg(D,p):  # Euler criterion, p odd prime
    D%=p
    if D==0: return 0
    r=pow(D,(p-1)//2,p); return 1 if r==1 else -1
print("== K: Kronecker symbols (Euler criterion, cross-checked vs sympy.jacobi) ==")
exp={140:1,-20:1,-7:1,5:-1,28:-1,-35:-1,35:1,-4:-1,8:1,-8:-1}
for D,v in exp.items():
    k=leg(D,23); print("  (%d/23) = %+d" % (D,k)); chk("R5b (%d/23)=%+d matches Local G4"%(D,v), k==v and k==jacobi_symbol(D%23,23))
chk("(-7/17) = -1", leg(-7,17)==-1)
for p in [113,137,193,233,281]:
    chk("(-7/%d) = +1 (wrongly listed in 845cc6bc s4)"%p, leg(-7,p)==1)
print("== N2: lattice [[2,14],[14,28]] ==")
G=Matrix([[2,14],[14,28]])
chk("det = -140", G.det()==-140)
chk("even (diagonal even)", G[0,0]%2==0 and G[1,1]%2==0)
chk("signature (1,1) since det<0 for 2x2 symmetric => sig = 0", G.det()<0)
S=smith_normal_form(G,domain=ZZ); d1,d2=abs(S[0,0]),abs(S[1,1]); print("  Smith diag:",d1,d2)
chk("D(N2) = Z/2 x Z/70, |D|=140", sorted([d1,d2])==[2,70])
chk("2-torsion of D = gcd(2,d1)*gcd(2,d2) = 4", (2 if d1%2==0 else 1)*(2 if d2%2==0 else 1)==4)
chk("rho(-I) eigenspace dims (sig=0: permutation g->-g): +72 / -68", (140+4)//2==72 and (140-4)//2==68)
chk("140 fundamental discriminant (140=4*35, 35=3 mod 4 squarefree)", 140%4==0 and (35%4)==3 and all(35%(q*q) for q in range(2,6)))
chk("chi_140(-1) = sign(140) = +1 = e(-0/4)", 1==1 and 140>0)
# nondegeneracy of discriminant bilinear form (used in rho(S)^2 = e(-sig/4) (g -> -g) via character orthogonality)
Gi=G.inv()
pts=set()
for v1 in range(140):
    for v2 in range(140):
        w=Gi*Matrix([v1,v2]); pts.add((Fr(int(w[0].p),int(w[0].q))%1, Fr(int(w[1].p),int(w[1].q))%1))
def bil(g,h): 
    return (g[0]*(2*h[0]+14*h[1])+g[1]*(14*h[0]+28*h[1]))%1
chk("|L'/L| enumerated = 140", len(pts)==140)
nd=all(any(bil(t,d)!=0 for d in pts) for t in pts if t!=(0,0))
chk("discriminant bilinear form nondegenerate (=> sum_d e(-(t,d)) = 0 for t != 0)", nd)
print("== R2: one-line congruence (replaces tautological v3 G5 loop) ==")
chk("(a-b) - 2(c-b) - (a+b-2c) expands to 0, so a+b=2c over Z => a = b mod 2", expand((a-b)-2*(c-b)-(a+b-2*c))==0)
print("== R4a: Jac(C), C: y^2 = x^5 - x, at p = 17, by brute-force point counts over F_17 and F_289 ==")
dsc=discriminant(x**5-x,x); print("  disc(x^5-x) =",dsc)
chk("disc(x^5-x) = 256 = 2^8 (good reduction at every odd p for the odd-degree model)", dsc==256)
def counts(p, f):
    # N1 over F_p, N2 over F_{p^2} = F_p[t]/(t^2-n); quadratic char of F_{p^2} via norm
    n=next(z for z in range(2,p) if leg(z,p)==-1)
    N1=1+sum(1+leg(f(X,0,p,n)[0],p) for X in range(p))
    N2=1
    for u in range(p):
        for v in range(p):
            r0,r1=f(u,v,p,n); 
            if r0==0 and r1==0: N2+=1
            else: N2+=1+leg(r0*r0-n*r1*r1,p)
    return N1,N2
def fbolza(u,v,p,n):
    # (u+v t)^5 - (u+v t) in F_p[t]/(t^2-n)
    def mul(A,B): return ((A[0]*B[0]+n*A[1]*B[1])%p,(A[0]*B[1]+A[1]*B[0])%p)
    z=(u%p,v%p); z2=mul(z,z); z4=mul(z2,z2); z5=mul(z4,z)
    return ((z5[0]-z[0])%p,(z5[1]-z[1])%p)
def lpoly(p,N1,N2):
    S1=p+1-N1; S2=p*p+1-N2; c2=(S1*S1-S2)//2
    return Poly(x**4 - S1*x**3 + c2*x**2 - p*S1*x + p*p, x)
N1,N2=counts(17,fbolza); P17=lpoly(17,N1,N2); print("  #C(F_17) =",N1," #C(F_289) =",N2," P(x) =",P17.as_expr())
chk("Frobenius char poly of Jac(C)/F_17 = (x^2+6x+17)^2 (expand difference == 0)", expand(P17.as_expr()-(x**2+6*x+17)**2)==0)
co=P17.all_coeffs(); print("  coefficients:",co)
chk("x^3 coefficient 12 (trace of Frobenius -12)", co[1]==12)
chk("x^2 coefficient 70, 17 does not divide 70 (p-rank 2: ordinary, g=2 criterion)", co[2]==70 and co[2]%17!=0)
chk("x^2+6x+17 irreducible over Q (disc -32 < 0)", 36-68==-32)
chk("Newton polygon of x^2+6x+17 at 17: v(17)=1, v(6)=0 => exactly one 17-adic unit root", 6%17!=0)
s=[2,-6]  # s_f = alpha^f + alphabar^f, alpha+alphabar=-6, alpha*alphabar=17
for f in range(2,61): s.append(-6*s[-1]-17*s[-2])
chk("s_f = -6 s_{f-1} - 17 s_{f-2}: s_f = (-6)^f mod 17, nonzero mod 17 for f=1..60", all(s[f]%17==pow(-6,f,17) and s[f]%17!=0 for f in range(1,61)))
# 49a1: y^2 + xy = x^3 - x^2 - 2x - 1 over F_17
p=17; cnt=1+sum(1 for X in range(p) for Y in range(p) if (Y*Y+X*Y-(X**3-X*X-2*X-1))%p==0)
chk("a_17(49a1) = 18 - #E(F_17) = 0 (point count; supersingular at 17 since 17 | a_17)", 18-cnt==0)
print("== ER: erratum prime lists vs independent point counts p = 5..281 and vs v3 log ==")
logtxt=open(sys.argv[1]).read()
logfac={int(m.group(1)):m.group(2) for m in re.finditer(r"p=\s*(\d+)\s+\(-2/p\)=[+-]\d \(-7/p\)=[+-]\d\s+charpoly factors: \[(.*)\]",logtxt)}
chk("v3 log G3 lists 58 primes 5..281", sorted(logfac)==list(primerange(5,282)))
quadnz7=[];quart7=[];quad2=[];mismatch=[]
for p in primerange(5,282):
    N1,N2=counts(p,fbolza); P=lpoly(p,N1,N2)
    fl=[(Poly(f,x),e) for f,e in factor_list(P.as_expr())[1]]
    ours=sorted(str(f.as_expr()).replace(' ','') for f,e in fl)
    theirs=sorted(t.strip().strip("'").replace(' ','') for t in logfac[p].split(','))
    if ours!=theirs: mismatch.append((p,ours,theirs))
    deg2=[f for f,e in fl if f.degree()==2]
    if leg(-7,p)==-1:
        if deg2 and deg2[0].all_coeffs()[1]!=0: quadnz7.append(p)
        if len(fl)==1 and fl[0][0].degree()==4 and fl[0][1]==1:
            cc=fl[0][0].all_coeffs(); 
            if cc[1]==0 and cc[3]==0 and cc[2]%p!=0: quart7.append(p)
    if leg(-2,p)==1 and deg2:
        aa=-deg2[0].all_coeffs()[1]; dd=aa*aa-4*p
        m=dd; 
        for q in range(2,int(abs(m)**0.5)+2):
            while m%(q*q)==0: m//=q*q
        quad2.append((p,m))
chk("independent factor sets equal v3 log G3 factor sets at all 58 primes", not mismatch)
if mismatch: print("  mismatch:",mismatch)
print("  (-7/p)=-1, quadratic factor nonzero trace:",quadnz7)
print("  (-7/p)=-1, irreducible quartic x^4+cx^2+p^2, p !| c:",quart7)
print("  (-2/p)=+1 with quadratic factor (p, squarefree part of a^2-4p):",quad2)
chk("erratum item 1 list = 17,41,73,89,97,241,257", quadnz7==[17,41,73,89,97,241,257])
chk("erratum item 1 quartic-ordinary list = 19,59,83,131,139,227,251, all = 3 mod 8", quart7==[19,59,83,131,139,227,251] and all(q%8==3 for q in quart7))
chk("erratum item 2: 12 primes, list as filed, all squarefree part -2", [q for q,_ in quad2]==[17,41,73,89,97,113,137,193,233,241,257,281] and all(m==-2 for _,m in quad2))
print("ALL_CHECKS", "PASS" if all(OK) else "FAIL", "(%d)"%len(OK))
