# A33 exact (Fractions): the automorph gamma=[[-1,-7],[2,13]] of A acts on D=A^{-1}Z^2/Z^2 as the local reflection Z7
# (identity on D5, -1 on D7) and fixes the characteristic a mod Z^2 and a mod A^{-1}Z^2-twists with trivial phase.
# Since G_{al,be}=G_{g^-1 al, g^-1 be} (change of variables), every candidate law vector is Z7-even exactly.
import json
from fractions import Fraction as Fr
from law import MU, R, a, Z, CANDS, b
A=[[2,7],[7,7]]; g=[[-1,-7],[2,13]]; gi=[[13,7],[-2,-1]]
mat=lambda M,v:(M[0][0]*v[0]+M[0][1]*v[1], M[1][0]*v[0]+M[1][1]*v[1])
gT=[[g[0][0],g[1][0]],[g[0][1],g[1][1]]]
GtAG=[[sum(gT[i][k]*A[k][l]*g[l][j] for k in range(2) for l in range(2)) for j in range(2)] for i in range(2)]
assert GtAG==A and g[0][0]*g[1][1]-g[0][1]*g[1][0]==1
B=lambda u,v: sum(u[i]*A[i][j]*v[j] for i in range(2) for j in range(2))
modZ=lambda v:(v[0]%1,v[1]%1)
def z7(mu):   # local reflection on D: CRT -1 on 7-part, +1 on 5-part ; mu = r/(-35)
    r=R[MU.index(mu)]; y=tuple((-x*15 + x*21)%35 for x in r)   # 15=1 mod7,0 mod5 ; 21=1 mod5,0 mod7
    return MU[R.index(y)]
res={'gamma^T A gamma = A':True}
okD=all(modZ(mat(gi,mu))==z7(mu) for mu in MU); res['gamma^-1 acts on D as Z7']=okD
# characteristic: gamma^-1 a - a
d=(mat(gi,a)[0]-a[0], mat(gi,a)[1]-a[1]); res['gamma^-1 a - a']=[str(x) for x in d]
# for each candidate, check G_{al(mu),be} = G_{al(z7 mu),be}: after change of variables, (g^-1 al, g^-1 be) vs (al', be):
# first slots must agree mod Z^2; second slots differ by lam in A^{-1}Z^2 with phase e(B(al',lam)) == 1
allok={}
for c,f in CANDS.items():
    ok=True
    for mu in MU:
        al,be=f(mu); al2,be2=f(z7(mu)); ga,gb=mat(gi,al),mat(gi,be)
        if modZ(ga)!=modZ(al2): ok=False; break
        lam=(gb[0]-be2[0],gb[1]-be2[1]); Al=mat(A,lam)
        if not all(x.denominator==1 for x in Al): ok=False; break
        # G_{ga,gb}=G_{al2+n, be2+lam} = e(B(al2+n, lam)) G_{al2,be2}; n=ga-al2 integral
        if B(ga,lam)%1!=0: ok=False; break
    allok[c]=ok
res['candidate g_mu = g_{Z7 mu} exactly']=allok
print(res); json.dump(res,open('exact_z7.json','w'),indent=1)
# K1 detail: phases e(B(g^-1 al, lam)) per mu ; value 1/2 => G_mu = -G_{Z7 mu}
ph=set()
for mu in MU:
    al,be=CANDS['K1'](mu); al2,be2=CANDS['K1'](z7(mu)); ga,gb=mat(gi,al),mat(gi,be)
    assert modZ(ga)==modZ(al2); lam=(gb[0]-be2[0],gb[1]-be2[1]); ph.add(str(B(ga,lam)%1))
res['K1 phases B(g^-1 al,lam) mod 1']=sorted(ph); print(res['K1 phases B(g^-1 al,lam) mod 1'])
json.dump(res,open('exact_z7.json','w'),indent=1)
# K1 under nu -> -nu and under -gamma: phase of G_{a+mu,a} vs G_{a+mu',a}
def relation(M):
    out=set()
    for mu in MU:
        al,be=CANDS['K1'](mu); ga,gb=mat(M,al),mat(M,be)
        for mu2 in MU:
            al2,be2=CANDS['K1'](mu2)
            if modZ(ga)==modZ(al2):
                lam=(gb[0]-be2[0],gb[1]-be2[1]); assert all(x.denominator==1 for x in mat(A,lam))
                out.add((mu==mu2, str(B(ga,lam)%1)))
    return sorted(out)
res['K1 under -1']=relation([[-1,0],[0,-1]]); res['K1 under -gamma^-1']=relation([[-13,-7],[2,1]])
print(res['K1 under -1'],res['K1 under -gamma^-1']); json.dump(res,open('exact_z7.json','w'),indent=1)
