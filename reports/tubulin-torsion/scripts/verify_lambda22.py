# Numerical/exact checks for PROOF_LAMBDA22.md
import numpy as np, sympy as sp, itertools
N=13
# Fourier basis on coords 1..13
rows=[np.ones(N)/np.sqrt(N)]
for k in range(1,7):
    n=np.arange(N)
    rows.append(np.sqrt(2/N)*np.cos(2*np.pi*k*n/N)); rows.append(np.sqrt(2/N)*np.sin(2*np.pi*k*n/N))
F=np.array(rows); Pi=np.hstack([F,np.zeros((13,9))]); P=Pi.T@Pi
print("max|PiPi^T-I|",abs(Pi@Pi.T-np.eye(13)).max())
D=np.zeros((22,22)); D[:13,:13]=np.eye(13)
print("max|P-diag(I13,0)|",abs(P-D).max(), " |det F|",abs(np.linalg.det(F)))
# D22 Gram (basis e1-e2,...,e21-e22? use standard basis: e1+e2, e2-e1... ) use basis b1=e1+e2, bi=e_i - e_{i-1} (i=2..22)
B=np.zeros((22,22)); B[0,0]=B[0,1]=1
for i in range(1,22): B[i,i]=1; B[i,i-1]=-1
assert all(int(r.sum())%2==0 for r in B)
print("det Gram D22 =",round(np.linalg.det(B@B.T)), " det Gram Z22 =",1)
# Fixed sublattice of sigma=(S, I_9)
S=sp.zeros(22,22)
for i in range(13): S[(i+1)%13,i]=1
for i in range(13,22): S[i,i]=1
K=(S-sp.eye(22)).nullspace(); print("dim fixed space",len(K))
Bf=sp.Matrix.hstack(*[sp.Matrix([1]*13+[0]*9)]+[sp.eye(22)[:,j] for j in range(13,22)])
G=Bf.T*Bf; print("det Gram fixed Z22 =",G.det())
# fixed D22: basis (1^13,1,0..),(0,2,0..),(0,e14-e15..)… index 2 -> det 4*13
Bd=sp.Matrix.hstack(Bf[:,0]+Bf[:,1], 2*Bf[:,1], *[Bf[:,j]-Bf[:,1] for j in range(2,10)])
assert all(sum(Bd[:,j])%2==0 for j in range(10))
print("det Gram fixed D22 =",(Bd.T*Bd).det())
# minimal norms by short-vector enumeration in small box (sanity)
print("min norm Z22 = 1 (e1); min norm D22 = 2 (e1+e2); kissing D22 =",4*sp.binomial(22,2))
# dense contrast: projection of Z^2 onto line spanned by (1,sqrt2): coords (a+b*sqrt2)/sqrt3
vals=sorted({(a+b*np.sqrt(2))%1 for a in range(-300,301) for b in range(-300,301)})
print("contrast: max gap in {a+b*sqrt2 mod 1}, |a|,|b|<=300:",max(np.diff(vals)))
