import sympy as sp, json
s,a,n,k=sp.symbols('s a n k')
A=sp.Matrix([[2,s],[s,s]]); Qp=lambda v: sp.expand(v[0]**2+s*v[0]*v[1]+s*v[1]*(v[1]+1)/2)
B=lambda c,v: sp.expand((sp.Matrix(c).T*A*sp.Matrix(v))[0])
M=sp.Matrix([[-1,-s],[0,1]]); v=sp.Matrix([n,k]); ca=sp.Matrix([-a,1])
r={}
r['M involution, det']=[M*M==sp.eye(2), str(M.det())]
r['Q+(Mv)=Q+(v)']=sp.expand(Qp(M*v)-Qp(v))==0
r['M isometry of A']=sp.simplify(M.T*A*M-A)==sp.zeros(2)
r['M c_a = c_{s-a}']=sp.simplify(M*ca-sp.Matrix([-(s-a),1]))==sp.zeros(2,1)
r['B(c_a,v)']=str(sp.factor(B(ca,v)))
r['-2Q(c_a)']=str(sp.expand(-B(ca,ca)))
r['-2Q(c_a) invariant a->s-a']=sp.expand(B(ca,ca)-B(sp.Matrix([-(s-a),1]),sp.Matrix([-(s-a),1])))==0
r['-2Q(c_4)']=str(sp.factor(-B(ca,ca).subs(a,4)))
r['Delta(a)=4Q(c1)Q(c_a)']=str(sp.factor(B([-1,1],[-1,1])*B(ca,ca)))
r['det(c1,c_a)']=str(sp.Matrix([[-1,-a],[1,1]]).det())
r['orthant strictly inside cone iff']='B(c_a,(1,0))=s-2a<0 and B(c_a,(0,1))=s(1-a)<0, i.e. a>s/2'
r['Q(c_a)<0 iff']=str(sp.solve(sp.Eq(2*a**2-2*s*a+s,0),a))
print(json.dumps(r,indent=1)); json.dump(r,open('c2_symbolic.json','w'),indent=1)
