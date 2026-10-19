# Exact side checks for 2026-10-19-Implications-Unification-RTA-multik-K3.md (read-only w.r.t. all existing files)
import cypari2, json, itertools
from fractions import Fraction as Fr
import sympy as sp
pari=cypari2.Pari(); gp=lambda s: pari(s)
out={}
# (1) multi-k Theorem 3.1 symbolic
m,k,x=sp.symbols('m k x')
al=256*m**2-sp.Rational(3125,256)*k**4; be=k*al
d=sp.discriminant(x**5+al*x+be,x)
out['multik_thm31']=bool(sp.simplify(d-(256*al**2*m)**2)==0)
seeds={'x^5-55*x+88':None,'x^5-100*x+400':None,'x^5+20*x+16':None,'x^5+20*x-32':None}
for f in seeds:
    D=int(gp(f'poldisc({f})')); sq=bool(gp(f'issquare({D})'))
    G=str(gp(f'polgalois({f})'))
    seeds[f]={'disc':D,'square':sq,'polgalois':G}
out['seeds']=seeds
# (2) the two 'P_s' of the RTA manuscript (s=7): §7 P_s=(-q^s;q^s)_inf g_s vs §9 orthant path count
N=60; s=7
q=sp.symbols('q')
def trunc(e): return sp.series(e,q,0,N).removeO()
orth=sum(q**(n*n+s*n*kk+s*kk*(kk+1)//2) for n in range(N) for kk in range(N) if n*n+s*n*kk+s*kk*(kk+1)//2<N)
gs=0
for n in range(8):
    den=1
    for j in range(1,n+1): den*= (1+q**(s*j))
    gs+= q**(n*n)/den
prod=1
for j in range(1,N//s+1): prod*=(1+q**(s*j))
p7=sp.Poly(trunc(sp.expand(prod)*trunc(gs)),q)
po=sp.Poly(orth,q)
diff=[ (i, p7.coeff_monomial(q**i), po.coeff_monomial(q**i)) for i in range(N) if p7.coeff_monomial(q**i)!=po.coeff_monomial(q**i)]
out['RTA_two_Ps_first_diffs_s7']=[(i,int(a),int(b)) for i,a,b in diff[:6]]
# (3) K3-relevant lattice facts
def latinfo(G,name):
    G=sp.Matrix(G); det=G.det()
    a,b,c=G[0,0],G[0,1],G[1,1]
    disc=b*b-a*c
    iso=sp.sqrt(disc).is_integer
    # (-2)-vectors: a x^2+2b xy + c y^2 = -2 ; binary indefinite: check via pari qfbsolve on form (a,2b,c)
    r=str(gp(f'qfbsolve(Qfb({a},{2*b},{c}),-2)'))
    return {'name':name,'gram':[[int(a),int(b)],[int(b),int(c)]],'det':int(det),'even':(a%2==0 and c%2==0),'isotropic':bool(iso),'minus2_solution':r}
out['lattices']=[latinfo([[2,14],[14,28]],'s=7 even sublattice {x2 even} of (Z^2,A)'),
                 latinfo([[4,14],[14,14]],'s=7 lattice (Z^2,2A)')]
for kk in [2,3,4]:
    mm=2*kk*kk-1
    out['lattices'].append(latinfo([[2,2*mm],[2*mm,2]],f'M_t at k={kk}, m={mm}'))
# action of automorph on discriminant group: for even lattice Gram G and isometry g, check g = +-1 on G^{-1}Z^2/Z^2
def disc_action(G,g):
    G=sp.Matrix(G); g=sp.Matrix(g)
    assert g.T*G*g==G
    Gi=G.inv(); gens=[Gi[:,0],Gi[:,1]]
    res=[]
    for sign in (1,-1):
        ok=all(all(((g*v - sign*v)[i]).is_integer for i in range(2)) for v in gens)
        res.append(ok)
    return {'plus1':res[0],'minus1':res[1]}
gam=[[-1,-7],[2,13]]  # rev6 automorph on (Z^2,A)
A=sp.Matrix([[2,7],[7,7]]); g=sp.Matrix(gam); assert g.T*A*g==A
# on (Z^2,2A)
acts={}
P=sp.eye(2)
for e in range(1,13):
    P=P*g
    acts[e]=disc_action([[4,14],[14,14]],P)
out['gamma_powers_on_disc(Z^2,2A)']={e:v for e,v in acts.items() if v['plus1'] or v['minus1']} or 'none up to 12'
# even sublattice basis (1,0),(0,2): change of basis
Bm=sp.Matrix([[1,0],[0,2]]); acts2={}
P=sp.eye(2)
for e in range(1,13):
    P=P*g
    h=Bm.inv()*P*Bm
    if all(v.is_integer for v in h):
        acts2[e]=disc_action([[2,14],[14,28]],h)
out['gamma_powers_on_disc(even sublattice)']=acts2
for kk in [2,3,4]:
    mm=2*kk*kk-1
    gg=sp.Matrix([[0,-1],[1,2*mm]])  # g e1=f, g f=-e1+2m f
    G=[[2,2*mm],[2*mm,2]]
    out[f'M_t k={kk}: g on disc']=disc_action(G,gg); out[f'M_t k={kk}: g^2 on disc']=disc_action(G,gg*gg)
# (4) Weil rep of Z/5, Q(x)=2x^2/5 (s=7 factor): image orders of even/odd parts (exact, in Q(zeta_20))
z=sp.exp(2*sp.pi*sp.I/5)
def weil(p,a):
    # rho(T) e_x = e(a x^2/p) e_x ; rho(S) e_x = c/sqrt(p) sum_y e(-2a x y/p) e_y  (scalar c irrelevant for projective image)
    T=sp.diag(*[sp.exp(2*sp.pi*sp.I*sp.Rational(a*xx*xx%p,p)) for xx in range(p)])
    S=sp.Matrix(p,p,lambda i,j: sp.exp(-2*sp.pi*sp.I*sp.Rational((2*a*i*j)%p,p)))/sp.sqrt(p)
    return S,T
import numpy as np
def numgroup(mats,maxn=2000):
    mats=[np.array(sp.N(M,30).tolist(),dtype=complex) for M in mats]
    I=np.eye(mats[0].shape[0]); els=[I]; keys={tuple(np.round(I,8).flatten())}
    frontier=[I]
    while frontier and len(els)<maxn:
        nf=[]
        for X in frontier:
            for M in mats:
                Y=M@X; kk=tuple(np.round(Y,8).flatten())
                if kk not in keys: keys.add(kk); els.append(Y); nf.append(Y)
        frontier=nf
    return els
S,T=weil(5,2)
ev=sp.Matrix([[1 if (j==0 and i==0) else 0 for j in range(5)] for i in range(1)])
# even basis e0, e1+e4, e2+e3 ; odd basis e1-e4, e2-e3
Be=sp.Matrix([[1,0,0],[0,1,0],[0,0,1],[0,0,1],[0,1,0]])
Bo=sp.Matrix([[0,0],[1,0],[0,1],[0,-1],[-1,0]])
def restrict(M,B): return (B.T*B).inv()*B.T*M*B
Se,Te=restrict(S,Be),restrict(T,Be); So,To=restrict(S,Bo),restrict(T,Bo)
ge=numgroup([Se,Te]); go=numgroup([So,To])
def proj_order(els):
    # order modulo scalars
    keys=set()
    for X in els:
        i=np.argmax(abs(X.flatten())); Y=X/ (X.flatten()[i]/abs(X.flatten()[i]))
        keys.add(tuple(np.round(Y,6).flatten()))
    return len(keys)
out['Weil_Z5_even_dim3']={'group_order(numerical closure)':len(ge),'order_mod_scalars':proj_order(ge)}
out['Weil_Z5_odd_dim2']={'group_order(numerical closure)':len(go),'order_mod_scalars':proj_order(go)}
# (5) 5399
out['5399_isprime']=bool(gp('isprime(5399)'))
out['2cos(2pi*10/5399) degree']=int(gp('eulerphi(5399)'))//2
json.dump(out,open('checks.json','w'),indent=1,default=str)
print(json.dumps(out,indent=1,default=str))
