import numpy as np
M=3; h1=[1,1,0]; h2=[-1,1,3]
circ=lambda h: np.array([[h[(i-j)%M] for j in range(M)] for i in range(M)],float)
print("det", round(np.linalg.det(circ(h1))), round(np.linalg.det(circ(h2))))
W=sum(h1[a]*h2[b] for a in range(M) for b in range(M) if (a+b)%M==1)
N=sum(abs(h1[a]*h2[b]) for a in range(M) for b in range(M) if (a+b)%M==1)
print("W",W,"N",N,"h1*h2",[sum(h1[a]*h2[b] for a in range(M) for b in range(M) if (a+b)%M==r) for r in range(M)])
