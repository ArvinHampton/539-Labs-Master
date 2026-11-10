# CX2: Ad-type model. V=M_2(C) (vectorized), M = projection onto span(I) (trace part, analog of time-mean),
# P0 = Id - M, A = Ad_g, g=diag(1,-1). Ad_g preserves I and traceless, so commutes with P0 (S1 case).
import numpy as np
E=[np.array(m,float) for m in ([[1,0],[0,0]],[[0,1],[0,0]],[[0,0],[1,0]],[[0,0],[0,1]])]
vec=lambda X: X.reshape(-1); g=np.diag([1.,-1.])
A=np.column_stack([vec(g@e@np.linalg.inv(g)) for e in E])
Iv=vec(np.eye(2))/np.sqrt(2); Mp=np.outer(Iv,Iv); P0=np.eye(4)-Mp
Q=P0@A
print("CX1 (A=2Id):", np.allclose((np.diag([0,1.])@(2*np.eye(2)))@(np.diag([0,1.])@(2*np.eye(2))), np.diag([0,1.])@(2*np.eye(2))))
print("CX2 commute:",np.allclose(P0@A,A@P0),"idempotent:",np.allclose(Q@Q,Q),"eig:",np.round(np.linalg.eigvals(Q),6))
