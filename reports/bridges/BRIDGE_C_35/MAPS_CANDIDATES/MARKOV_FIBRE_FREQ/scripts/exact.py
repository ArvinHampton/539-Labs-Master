# Exact rational stationary law of the lifted chain at M=216 (post-test, closed form check)
import sympy as sp
def T3(n): return n//3 if n%3==0 else ((4*n+2)//3 if n%3==1 else (2*n+1)//3)
M=216; P=sp.zeros(M,M)
for r in range(3*M): P[r%M,T3(r)%M]+=sp.Rational(1,3)
# stationary from limit: solve pi(P-I)=0 restricted to the closed class (u not 0 mod 4)
S=[r for r in range(M) if r%4!=0]; Q=P.extract(S,S)
A=(Q.T-sp.eye(len(S))).row_insert(0,sp.ones(1,len(S)))
b=sp.zeros(len(S)+1,1); b[0]=1
pi=A.solve_least_squares(b)
hit=[0]*8
for i,r in enumerate(S):
    if r%9==3: hit[((r-21)//9)%8]+=pi[i]
s=sum(hit); print('hitrate',s,'fib',[sp.nsimplify(h/s) for h in hit])
m8=[sum(pi[i] for i,r in enumerate(S) if r%8==c) for c in range(8)]; print('u mod 8 law',m8)
