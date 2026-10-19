# O(N2) elements (N2 = <2>+<-70>) mod the action on A_{N2}: which preserve the positive cone and act as +-1 on A?
import sympy as sp, json
G=sp.diag(2,-70)
# gamma in this basis: N2 basis (1,0),(0,2) of Z^2, then P=[[1,-7],[0,1]]
A=sp.Matrix([[2,7],[7,7]]); Bm=sp.Matrix([[1,0],[0,2]]); P=sp.Matrix([[1,-7],[0,1]]); C=Bm*P   # columns: diag basis in Z^2 coords
assert C.T*A*C==G
g=C.inv()*sp.Matrix([[-1,-7],[2,13]])*C; assert g.T*G*g==G
r=sp.diag(1,-1); assert r.T*G*r==G
Gi=G.inv()
gens=[sp.Matrix([sp.Rational(1,2),0]),sp.Matrix([0,sp.Rational(1,70)])]
def act(M):   # +1 / -1 / other on A
    plus=all(all((M*v-v)[i].is_integer for i in range(2)) for v in gens)   # G-dual coordinates: A = G^{-1}Z^2/Z^2
    minus=all(all((M*v+v)[i].is_integer for i in range(2)) for v in gens)
    return '+1' if plus else ('-1' if minus else 'other')
h=sp.Matrix([1,0])   # positive class, norm 2
res={}
for name,M0 in (('g^k',sp.eye(2)),('r g^k',r)):
    for sgn in (1,-1):
        for k in range(4):
            M=sgn*M0*g**k
            res[f"{'-' if sgn<0 else ''}{name}, k={k}"]={'on_A':act(M),'preserves_positive_cone':bool(((h.T*G*(M*h))[0])>0)}
print(json.dumps(res,indent=1)); json.dump({'g_in_diag_basis':str(g),'table':res},open('aut.json','w'),indent=1)
