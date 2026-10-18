"""(c) O2 Gauss input and (e) count claims. Independent code.
G(x) = (2m)^-2 sum_{(n,k) mod 2m} e(x Q7(n,k)),  Q7 = n^2+7nk+7k(k+1)/2."""
import numpy as np, math, cmath
from fractions import Fraction as Fr
from sympy import jacobi_symbol, totient
out=[]
def pr(*s): print(*s); out.append(" ".join(map(str,s)))
def G(h,m):
    n=np.arange(2*m)[:,None]; k=np.arange(2*m)[None,:]
    num=(2*n*n+14*n*k+7*k*(k+1))            # 2*Q7, integer
    ph=(h*num)%(4*m)                         # x Q7 = h*num/(2m)  -> over 4m? : h*num/(2m) = 2*h*num/(4m)
    return np.exp(2j*np.pi*(2*ph%(4*m))/(4*m)).mean()
# sanity of G with direct formula
def Gdirect(h,m):
    s=0
    for n in range(2*m):
        for k in range(2*m):
            s+=cmath.exp(2j*math.pi*h*(n*n+7*n*k+Fr(7*k*(k+1),2))/m)
    return s/(4*m*m)
pr("G implementation check (h/m=3/7, 2/9):", f"{abs(G(3,7)-Gdirect(3,7)):.1e}", f"{abs(G(2,9)-Gdirect(2,9)):.1e}")
# O2: G(1/m) = e(7/(20m)) P(m)/m for gcd(m,70)=1; test P(m) depends only on m mod 70, and the stated closed form
Pm={}; worst_cf=0; worst_per=0
for m in range(1,1200):
    if math.gcd(m,70)!=1: continue
    Pv=G(1,m)*m/cmath.exp(2j*math.pi*7/(20*m))
    r=m%70
    if r in Pm: worst_per=max(worst_per,abs(Pv-Pm[r]))
    else: Pm[r]=Pv
    inv20=pow(20,-1,m) if m>1 else 0
    cf=cmath.exp(2j*math.pi*7*inv20/m)*int(jacobi_symbol(35,m))/m
    worst_cf=max(worst_cf,abs(G(1,m)-cf))
pr(f"O2 input, all m<1200 with gcd(m,70)=1: P(m):=m G(1/m) e(-7/(20m)) depends only on m mod 70 (max spread {worst_per:.1e}); |P|=1: {max(abs(abs(v)-1) for v in Pm.values()):.1e}")
pr(f"   closed form G(1/m) = e(7*20^-1/m) (35/m)/m : max deviation {worst_cf:.1e}")
# Theorem D pattern and count of coprime pairs
cnt=0; bad=0
for m in range(1,106):
    for h in range(m):
        if math.gcd(h,m)!=1: continue
        cnt+=1; g=abs(G(h,m))
        if m%2==0 or m%5==0: ok = g<1e-9
        elif m%7==0: ok = abs(g-math.sqrt(7)/m)<1e-9
        else: ok = abs(g-1/m)<1e-9
        bad+= (not ok)
pr(f"Theorem D: coprime pairs (h mod m, m<=105) = {cnt}; pattern mismatches = {bad}")
pr("x=h/7: G = (h/7) i/sqrt7 ?", [f"{(G(h,7)/(int(jacobi_symbol(h,7))*1j/math.sqrt(7))).real:.12f}" for h in range(1,7)])
# Sum of phi counts used in the paper
S=lambda M: sum(int(totient(m)) for m in range(1,M+1))
pr("sum_{m<=105} phi(m) =",S(105), "; sum_{m<=40} phi =",S(40), "; sum_{m<=60} phi =",S(60), "; sum_{m<=29} phi =",S(29))
# Theorem E(iii): test rationals with denominator < 30: try the natural sets
def zeroG(x):
    x=Fr(x); return (x.denominator%2==0) or (x.denominator%5==0)
for name,xs in [("0<x<1, m<30",[Fr(h,m) for m in range(2,30) for h in range(1,m) if math.gcd(h,m)==1]),
                ("0<x<=1, m<30",[Fr(h,m) for m in range(1,30) for h in range(1,m+1) if math.gcd(h,m)==1]),
                ("0<=x<1, m<30",[Fr(h,m) for m in range(1,30) for h in range(0,m) if math.gcd(h,m)==1])]:
    xs=[x for x in xs if x!=0]
    one=sum(1 for x in xs if zeroG(x)!=zeroG(-1/(7*x))); both_nz=sum(1 for x in xs if not zeroG(x) and not zeroG(-1/(7*x)))
    pr(f"E(iii) candidate set {name}: size {len(xs)}, exactly one of G(x),G(-1/7x) zero: {one}, both nonzero: {both_nz}")
# numeric constants
I=math.log(6+math.sqrt(35))/(2*math.sqrt(35))
aP=math.sqrt(math.pi)*(49-2*math.sqrt(14))/140
aH=math.sqrt(math.pi)*(math.sqrt(1190)-17*math.sqrt(14))/170
aC=math.sqrt(math.pi)*(833+204*math.sqrt(14)-14*math.sqrt(1190))/2380
pr(f"I = {I:.18f}; a_P = {aP:.10f}; a_H = {aH:.10f}; a_C = {aC:.10f}; a_P - a_H = {aP-aH:.10f}; (11-7I)/20 = {(11-7*I)/20:.10f}; R t^-1/2 = a_P - sqrt(pi)/2 = {aP-math.sqrt(math.pi)/2:.10f}")
pr(f"|I G| at x=1/7: I/sqrt7 = {I/math.sqrt(7):.6f}")
open("o2_counts_check.txt","w").write("\n".join(out)+"\n")
