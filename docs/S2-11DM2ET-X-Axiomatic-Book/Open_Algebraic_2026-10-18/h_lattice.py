# Item 1: explicit lattice M = ∩_{k=0..7} h^k M7, M7 = Z^2 + Z t0; prove hM = M, h preserves the discriminant form of M,
# and h(S_plus) = S_minus exactly as unions of M-cosets, for the two extra relations R1, R2 at s=98.
import json, sympy as sp, itertools
exec(open('old98_rel.py').read().split("M=flint.fmpz_mat(rows)")[0].replace("Q=float(sys.argv[1])","Q=2.0"))
R=json.load(open('old98_rel_Q40.json'))
A=sp.Matrix([[2,s],[s,s]])
g=sp.Matrix([[0,-m],[sp.Rational(1,m),2*m]]); h=(g+sp.eye(2))/4
t0=sp.Matrix([sp.Rational(t[0],D),sp.Rational(t[1],D)])
def hnf_lat(cols):  # rational generators -> basis (2x2) via scaling to integers and HNF
    den=sp.ilcm(*[c.q for v in cols for c in v]) if cols else 1
    Mi=sp.Matrix.hstack(*[v*den for v in cols])
    from sympy.matrices.normalforms import hermite_normal_form
    Mi=sp.Matrix(Mi.shape[0],Mi.shape[1],[int(x) for x in Mi]); H=hermite_normal_form(Mi)
    H=H[:, [j for j in range(H.shape[1]) if any(H[:,j])]]
    return H/den
def dual(B): return (B.T).inv()  # w.r.t. standard pairing
M7=hnf_lat([sp.Matrix([1,0]),sp.Matrix([0,1]),t0])
lats=[(h**k)*M7 for k in range(8)]
Mdual=hnf_lat([dual(L)[:,j] for L in lats for j in range(2)])
M=dual(Mdual)
M=hnf_lat([M[:,0],M[:,1]])
def inlat(B,v): c=B.inv()*v; return all(x.q==1 for x in c)
hM_eq=all(inlat(M,h*M[:,j]) for j in range(2)) and all(inlat(M,h.inv()*M[:,j]) for j in range(2))
gram=M.T*A*M
even=all(x.q==1 for x in gram) and all((gram[i,i]%2)==0 for i in range(2))
# dual lattice of M w.r.t. A: M# = A^{-1} M^{-T}
Msharp=(A.inv())*dual(M)
hMs=all(inlat(Msharp,h*Msharp[:,j]) for j in range(2))
detM=gram.det()
print("M basis",M.tolist()," index [M7:M]=",(M.det()/M7.det()), " Gram",gram.tolist()," det",detM," even",even," hM=M",hM_eq," hM#=M#",hMs)
# M7/M coset reps
def coset_reps(Big,Small):
    # enumerate Big/Small: Big basis b; small coordinates in big basis -> integer matrix; Smith-like brute force
    T=Big.inv()*Small; n=abs(T.det())
    reps=[]; keys=set()
    rng=range(int(n)+1)
    for a in rng:
        for b in rng:
            v=Big*sp.Matrix([a,b]); k=key(v,Small)
            if k not in keys: keys.add(k); reps.append(v)
            if len(reps)==n: return reps
    return reps
def key(v,B):
    c=B.inv()*v; return tuple(x-sp.floor(x) for x in c)
reps7=coset_reps(M7,M)
print("|M7/M|",len(reps7))
out=dict(M=[[str(x) for x in row] for row in M.tolist()],gram=[[str(x) for x in r] for r in gram.tolist()],det=str(detM),even=bool(even),
         hM_eq_M=bool(hM_eq),hMsharp_eq_Msharp=bool(hMs),index_M7_over_M=str(M.det()/M7.det()),relations=[])
for e in R['extra']:
    sets={}
    for sg in (1,-1):
        S=set()
        for d in e['support']:
            if (int(d['coef'])>0)==(sg>0):
                for c in corep[d['class_orbit']]:
                    x=sp.Matrix([sp.Rational(c[0],D),sp.Rational(c[1],D)])
                    for r in reps7: S.add(key(x+r,M))
        sets[sg]=S
    # weights: coefficients are ±1 per class orbit; check h maps S+ onto S- bijectively as M-coset sets
    def hkey(k):
        v=M*sp.Matrix(list(k)); return key(h*v,M)
    img={hkey(k) for k in sets[1]}
    ok=img==sets[-1] and len(sets[1])==len(sets[-1])
    out["relations"].append(dict(n_plus_cosets=len(sets[1]),n_minus_cosets=len(sets[-1]),h_maps_plus_onto_minus=bool(ok)))
    print(out["relations"][-1],flush=True)
json.dump(out,open("h_lattice.json","w"),indent=1)
