# Exact (unconditional) class numbers of discriminant D>0 (non-square) by Gauss reduction cycles of primitive
# indefinite forms. Narrow h+ = number of cycles of reduced forms under rho (each rho step is a proper equivalence;
# two reduced forms are properly equivalent iff they lie on the same cycle). Wide h = number of orbits of cycles
# under (a,b,c) -> (-a,b,-c) (improper-sign twist = equivalence by the unit of norm -1 when it exists).
import math, json, sys
from sympy import factorint
def isqrt(n): return math.isqrt(n)
def reduced_forms(D):
    r=isqrt(D); out=[]
    for b in range(1,r+1):
        if (b*b-D)%4: continue
        ac=(b*b-D)//4   # negative
        for a in range(1,2*r+2):
            if ac%a: continue
            c=ac//a
            for A,C in ((a,c),(-a,-c)):
                if math.gcd(math.gcd(abs(A),b),abs(C))!=1: continue
                # reduced: 0 < b < sqrt D and sqrt D - b < 2|a| < sqrt D + b
                if r - b < 2*abs(A) - (0) and (2*abs(A))**2 > 0:
                    sq=math.sqrt(D)
                    if sq-b < 2*abs(A) < sq+b: out.append((A,b,C))
    return sorted(set(out))
def rho(f,D):
    a,b,c=f; sq=math.sqrt(D); cc=abs(c)
    # b' = -b mod 2c with sqrt D - 2|c| < b' < sqrt D
    bp=(-b)%(2*cc)
    while bp<=sq-2*cc: bp+=2*cc
    while bp>sq: bp-=2*cc
    return (c,bp,(bp*bp-D)//(4*c))
def classnos(D):
    R=reduced_forms(D); S=set(R); seen=set(); cycles=[]
    for f in R:
        if f in seen: continue
        cyc=[];g=f
        while g not in seen:
            assert g in S,(g,D); seen.add(g); cyc.append(g); g=rho(g,D)
        cycles.append(frozenset(cyc))
    idx={g:i for i,c in enumerate(cycles) for g in c}
    neg=[idx[(-c0[0],c0[1],-c0[2])] for c0 in [next(iter(c)) for c in cycles]]
    orbits=len({frozenset((i,neg[i])) for i in range(len(cycles))})
    return len(cycles),orbits
def fund(n):
    f=factorint(n); d=1
    for p,e in f.items():
        if e%2: d*=p
    return d if d%4==1 else 4*d
res=[]
for s in (5,7,9,11,13,15,17,19,21,23,25,27,29,31):
    n=s*(s-2)
    for name,D in (('K_s',fund(n)),('4n',4*n)):
        hp,h=classnos(D); res.append({'s':s,'disc':name,'D':D,'h_narrow':hp,'h_wide':h})
        print(s,name,D,'h+',hp,'h',h)
json.dump(res,open(sys.argv[1] if len(sys.argv)>1 else 'classno_exact.json','w'),indent=1)
