# Exact symbolic derivation of 7s-32 (report §2).
import sympy as sp, json
s=sp.symbols('s',integer=True,positive=True); g=sp.symbols('g',positive=True)
A=sp.Matrix([[2,s],[s,s]]); Q=lambda v:sp.expand((v.T*A*v)[0]/2); B=lambda x,y:sp.expand((x.T*A*y)[0])
c1=sp.Matrix([-1,1]); c2=sp.Matrix([-4,1]); e1=sp.Matrix([1,0]); u1=sp.Matrix([0,1]); nu0=sp.Matrix([s,-2])
J=sp.Matrix([[0,-1],[1,0]]); v=sp.Matrix([3*s,s-8])
r={}
r['detA']=str(sp.factor(A.det()))
r['Q(c1)']=str(sp.factor(Q(c1))); r['Q(c2)']=str(sp.factor(Q(c2))); r['B(c1,c2)']=str(sp.factor(B(c1,c2)))
r['c2 = c1 - 3 e1']=c2==c1-3*e1; r['B(c1,e1)']=str(B(c1,e1)); r['Q(e1)']=str(Q(e1))
r['v = J A c2 (so B(c2,x)=det(x,v), v spans c2^perp)']=sp.simplify(J*A*c2-v)==sp.zeros(2,1)
r['J^T A J = det(A) A^-1']=sp.simplify(J.T*A*J-A.det()*A.inv())==sp.zeros(2)
r['2Q(v) = detA * 2Q(c2) = s(s-2)(7s-32)']=sp.expand(2*Q(v)-A.det()*2*Q(c2))==0 and sp.factor(2*Q(v))==sp.factor(s*(s-2)*(7*s-32))
r['v = 3 nu0 + (s-2) u1']=sp.simplify(v-(3*nu0+(s-2)*u1))==sp.zeros(2,1)
G=sp.Matrix([[2*Q(c1),B(c1,c2)],[B(c1,c2),2*Q(c2)]])
r['det Gram(c1,c2) = det(c1,c2)^2 detA']=sp.expand(G.det()-sp.Matrix.hstack(c1,c2).det()**2*A.det())==0
r['Delta = 4Q(c1)Q(c2) = B(c1,c2)^2 + det Gram = 16(s-2)^2 - 9s(s-2)']=sp.expand(4*Q(c1)*Q(c2)-(B(c1,c2)**2+G.det()))==0 and sp.expand(4*Q(c1)*Q(c2)-(16*(s-2)**2-9*s*(s-2)))==0
# residual (u2-orthogonal) coefficient for any w with det(w,u2)=1, u2=v/g: detA/(4Q(u2)) = -g^2/(2(7s-32)) = Q(proj_{c2} w), proj w = g/(2Q(c2)) c2
Qu2=Q(v)/g**2
r['residual = detA/(4Q(u2))']=str(sp.factor(A.det()/(4*Qu2)))
r['Q(g c2/(2Q(c2)))']=str(sp.factor(Q(g*c2/(2*Q(c2)))))
print(json.dumps(r,indent=1)); json.dump(r,open('delta_lattice.json','w'),indent=1)
