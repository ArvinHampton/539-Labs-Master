# Canonical E-vector: average over gamma^k-fundamental domain so that every component is gamma^k-invariant.
#   Et_{al,be} := (1/k) sum_{i<k} E^F_{g^-i al, g^-i be}   (F = C0 u rho2C0 = [e1, g e1))
exec(open('evector.py').read().split("a=(Fr(7,10)")[0])
import itertools
g=((-1,-7),(2,13)); gi=((13,7),(-2,-1))
def act(M,v): return (M[0][0]*v[0]+M[0][1]*v[1], M[1][0]*v[0]+M[1][1]*v[1])
def equiv(al,be,al2,be2):
    # same function on the coset: al2-al in Z^2 and B(nu,be2-be) in Z for nu in al+Z^2
    if not all((al2[i]-al[i]).denominator==1 for i in range(2)): return False
    d=(be2[0]-be[0],be2[1]-be[1])
    return all((Bf((al[0]+e[0],al[1]+e[1]),d)).denominator==1 for e in [(0,0),(1,0),(0,1)])
a=(Fr(7,10),Fr(-1,5)); zero=(Fr(0),Fr(0))
comps=[(a,zero)]+[(p,neg(a)) for p in reps]
k=1
while True:
    M=((1,0),(0,1))
    for _ in range(k): M=((M[0][0]*gi[0][0]+M[0][1]*gi[1][0], M[0][0]*gi[0][1]+M[0][1]*gi[1][1]),(M[1][0]*gi[0][0]+M[1][1]*gi[1][0], M[1][0]*gi[0][1]+M[1][1]*gi[1][1]))
    if all(equiv(al,be,act(M,al),act(M,be)) for al,be in comps): break
    k+=1
out=[f"order k of gamma on all 36 component data: k = {k}"]
def Et(al,be,x):
    sa=0; sk=0; al_,be_=al,be
    for i in range(k):
        aa,kk=Eexp(al_,be_,x); sa+=aa; sk+=kk
        al_,be_=act(gi,al_),act(gi,be_)
    return sa/k, sk/k
for x in [Fr(1),Fr(1,3),Fr(2,3),Fr(1,7),Fr(1,2),Fr(2,5),Fr(3,4),Fr(3,7),Fr(5,3),Fr(1,9)]:
    aL,kL=Et(a,zero,-1/x)
    sk=0
    for p in reps: sk+=Et(p,neg(a),x)[1]
    rhs=float(x)/math.sqrt(35)*sk
    psi=kL-rhs
    out.append(f"x={str(x):4}: kappa_(a,0)(-1/x) = {kL.real:+.10f}{kL.imag:+.10f}i   (x/sqrt35)Sum_p kappa_(p,-a)(x) = {rhs.real:+.10f}{rhs.imag:+.10f}i   psi = {psi.real:+.3e}{psi.imag:+.3e}i")
print("\n".join(out)); open("evector2.txt","w").write("\n".join(out)+"\n")
