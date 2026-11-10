# Local-derived (PP fix CNF). Elementary, GRH-free check of h(Q(sqrt35)) = 2 (disc 140) and fundamental unit 6+sqrt35.
# Pure integer arithmetic; no quadclassunit, no PARI.
from math import isqrt
D=140; d=35
# 1. reduced indefinite forms (a,b,c), b^2-4ac=140, Gauss-reduced: 0<b<sqrt(D), sqrt(D)-b<2|a|<sqrt(D)+b
r=D**0.5
red=[(a,b,(b*b-D)//(4*a)) for b in range(1,isqrt(D)+1) for a in range(-12,13) if a and (b*b-D)%(4*a)==0 and r-b<2*abs(a)<r+b]
print('reduced forms of disc 140:',red)
def rho(f):
    a,b,c=f; # Gauss reduction operator
    cc=abs(c); t=None
    for bb in range(-2*cc+1,2*cc+1):
        if (bb+b)%(2*c)==0 and ((cc<r and r-2*cc<bb<r) or (cc>r and -cc<bb<=cc)): t=bb;break
    return (c,t,(t*t-D)//(4*c))
cycles=[]; seen=set()
for f in red:
    if f in seen: continue
    cyc=[f]; g=rho(f)
    while g!=f: cyc.append(g); g=rho(g)
    seen|=set(cyc); cycles.append(cyc)
print('cycles (narrow classes):',len(cycles)); [print('  ',c) for c in cycles]
# 2. small norms: x^2-35y^2 in {+-2,+-5} impossible mod 5 / mod 7
print('x^2 mod 5 in', sorted({x*x%5 for x in range(5)}), '-> x^2-35y^2 = x^2 mod 5 is never +-2 mod 5')
print('x^2-35y^2=+-5 => 5|x, x=5u, 5u^2-7y^2=+-1; mod 5: -7y^2=2y^2 in', sorted({2*y*y%5 for y in range(5)}), ', +-1 = {1,4} not hit')
print('N(5+sqrt35) =',25-35)
print('-1 mod 7 square?', any(x*x%7==6 for x in range(7)), '-> norm -1 impossible (x^2-35y^2 = x^2 mod 7)')
# 3. Pell: least y>=1 with 35y^2+1 or 35y^2-1 square
for y in range(1,50):
    for s in (1,-1):
        x2=d*y*y+s; x=isqrt(x2)
        if x*x==x2: print('first Pell hit: y=%d, x=%d, norm %+d'%(y,x,s)); break
    else: continue
    break
# continued fraction of sqrt35
m,dd,a0=0,1,isqrt(d); a=a0; cf=[a0]
while a!=2*a0: m=dd*a-m; dd=(d-m*m)//dd; a=(a0+m)//dd; cf.append(a)
print('sqrt35 = [%d; %s]'%(cf[0],', '.join(map(str,cf[1:]))))
