import numpy as np, math
from fractions import Fraction as Fr
from sympy import Matrix
out=[]
# 1. residual_factor is a 4-parameter interpolant through 4 data points (audit of Master 2026-08-25 'recovery')
ratios=[19.801180,3.160700,20.665180,55.302065]; ts=[-2,0,2,4]
A=np.array([[1,t,t*t,1/(1+t*t)] for t in ts]); sol=np.linalg.solve(A,ratios)
out.append(f"residual_factor fit through the 4 locked ratios: a,b,c,d = {sol.round(4)}; det = {np.linalg.det(A):.5f}")
out.append("=> 'recovers the ratios to machine precision' is automatic: 4 unknowns, 4 equations, det != 0 (interpolation, not a test).")
mags=[abs(-18.2+7.8j),abs(0.3-1.8j),abs(2.1-9.0j),abs(20.7+2.9j)]; xs=[1/7,3/7,5/7,1]
out.append("ratios |sample|/|7x|^{-1/2} recomputed from the complex markers: "+str([round(m*math.sqrt(7*x),3) for m,x in zip(mags,xs)]))
# 2. lattice level / discriminant group of A=[[2,7],[7,7]]
Am=Matrix([[2,7],[7,7]]); Ai=Am.inv()
N=next(N for N in range(1,1000) if all((N*Ai)[i,j].q==1 for i in range(2) for j in range(2)) and all((N*Ai)[i,i]%2==0 for i in range(2)))
out.append(f"A^-1 = {Ai.tolist()}; |det A| = {abs(Am.det())}; level N (N A^-1 even integral) = {N}")
# 3. first coefficients of C exceeding 1.5 (Master: value set {0,1,1.5} through degree 100)
src=open('identities.py').read().split('Cmixed =')[0].replace("int(sys.argv[1]) if len(sys.argv) > 1 else 3000","400")
g={}; exec(src,g); C=g['C']
out.append("first degrees with C-coefficient not in {0,1,3/2}: "+str([(i,str(C[i])) for i in range(401) if C[i] not in (0,1,Fr(3,2))][:8]))
print("\n".join(out)); open('audit_misc.txt','w').write("\n".join(out)+"\n")
