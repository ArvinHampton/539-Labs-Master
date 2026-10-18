# Identify each sigma-invariant ray class character chi_{j,l} (j even) as psi o N for a Dirichlet character psi,
# by its values on prime ideals; also confirm the odd-j characters are NOT of this form.
import cypari2, cmath, itertools
from sympy import primerange, jacobi_symbol
pari=cypari2.Pari(); pari.allocatemem(10**9); gp=lambda s: pari(s)
gp('bnf=bnfinit(y^2-35,1); P2=idealprimedec(bnf,2)[1]; P5=idealprimedec(bnf,5)[1]; f=idealmul(bnf,P2,P5); bnr=bnrinit(bnf,[f,[1,1]],1)')
def chi(j,l,c): return cmath.exp(2j*cmath.pi*(j*c[0]/8+l*c[1]/2))
data=[]
for p in primerange(3,3000):
    if p in (5,): continue
    dec=gp(f'idealprimedec(bnf,{p})')
    cls=[tuple(int(x) for x in gp(f'bnrisprincipal(bnr,idealprimedec(bnf,{p})[{i+1}],0)')) for i in range(len(dec))]
    data.append((p,len(dec),int(gp(f'idealprimedec(bnf,{p})[1].f')),cls))
# candidate psi: products of kronecker characters (-4/.),(8/.),(-8/.),(5/.),(-7/.) etc.  basis of real chars mod 280,
# plus quartic chars mod 5 (chi5 with chi5(2)=i).
def k(d,n): return int(jacobi_symbol(d% (4*abs(d)) if False else d, n)) if False else __import__('sympy').ntheory.residue_ntheory.jacobi_symbol(d,n) if n%2 else None
from sympy.ntheory import legendre_symbol
def kron(d,n):
    return int(pari(f'kronecker({d},{n})'))
def chi5(n,e):  # character mod 5 with chi(2)=i^e
    if n%5==0: return 0
    lg={1:0,2:1,4:2,3:3}[n%5]; return 1j**(e*lg)
basis=[(-4,),(8,),(-7,)]
cands=[]
for e5 in range(4):
    for s4 in (0,1):
        for s8 in (0,1):
            for s7 in (0,1):
                def psi(n,e5=e5,s4=s4,s8=s8,s7=s7):
                    return chi5(n,e5)*(kron(-4,n) if s4 else 1)*(kron(8,n) if s8 else 1)*(kron(-7,n) if s7 else 1)
                cands.append(((e5,s4,s8,s7),psi))
lines=[]
for j in range(8):
    for l in range(2):
        hits=[]
        for name,psi in cands:
            ok=True
            for (p,g,fdeg,cls) in data:
                if p==7:
                    continue
                v=psi(p)**fdeg
                if any(abs(chi(j,l,c)-v)>1e-9 for c in cls): ok=False;break
            if ok: hits.append(name)
        lines.append(f"chi_{j},{l}: psi o N candidates (e5: chi5(2)=i^e5, (-4/.),(8/.),(-7/.) exponents): {hits}")
print("\n".join(lines)); open("genus_chars.txt","w").write("\n".join(lines)+"\n")
