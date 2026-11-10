# Cat B: map variants into Bauer pseudospin formalism (Ridley & Cohen arXiv:2509.22264, Eqs. 16,41-50)
import sympy as sp
t,E,g=sp.symbols('t E g',real=True)
Q=sp.diag(1,-1); I2=sp.eye(2); sx=sp.Matrix([[0,1],[1,0]])
# Locked/separable: H' = diag(H,H) (Eq.41) -> [Q,H']=0, <Q> const, dt_f=+dt, dt_b=-dt (Eqs.46-50)
Hp=E*I2; print('[Q,H\'] =',(Q*Hp-Hp*Q).T)
# D2-coupled: H' + g sigma_x (brane transfer between f and b)
H=E*I2+g*sx; U=sp.simplify((-sp.I*H*t).exp())
psi=U*sp.Matrix([1,0]); Qt=sp.simplify((psi.H*Q*psi)[0])
print('<Q>(t) =',sp.simplify(sp.re(sp.expand_complex(Qt))))   # d<t>/dt = <Q> (Eq.46)
print('eigs',(H).eigenvals(),' unitary:',sp.simplify(U.H*U)==I2)
# Same coupling in tilde-frame H~ = HQ = diag(E,-E) (Eq.16) + g sx: eigenvalues
print('H~ eigs',(E*Q+g*sx).eigenvals())
# Period of arrow reversal if 2g = 2pi/539.9
print('g for G4 arrow-mixing [rad/s]', float(sp.pi/539.9))
