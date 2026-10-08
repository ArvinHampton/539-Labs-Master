import numpy as np
phi=(1+5**.5)/2; w=np.exp(2j*np.pi/3)
base=61/1001*phi**7/539.9; S=15.24
print("base",base,"S*base",S*base, "phi^7/539.9",phi**7/539.9)
W=np.array([[1,w,w**2],[w,w**2,1],[w**2,1,w]])
D=np.diag([phi**-3/61,phi**-5/61,phi**-7/61])
print("W sv",np.round(np.linalg.svd(W,compute_uv=False),6))
K=S*np.kron(W,D); print("kron eig |.|",np.round(np.sort(abs(np.linalg.eigvals(K))),6))
print("kron sv",np.round(np.linalg.svd(K,compute_uv=False),6))
H=S*W*np.diag(D)[None,:]  # elementwise columns
for name,M in [("W*D (matmul)",S*W@D),("D*W",S*D@W),("hadamard col",H),("S*base*W",S*base*W)]:
    print(name,"eig|.|",np.round(np.sort(abs(np.linalg.eigvals(M))),6),"sv",np.round(np.linalg.svd(M,compute_uv=False),6))
for nm,t in [("A",[0.0086,0.0098,0.050]),("B",[0.001,0.009,0.050])]:
    t=np.array(t);print(nm,"sum",t.sum(),"dm21",t[1]**2-t[0]**2,"dm31",t[2]**2-t[0]**2,"dm32",t[2]**2-t[1]**2)
# NOvA-based NO spectrum for reference (m1=0, dm21 7.5e-5 public, dm32 2.431e-3 NOvA)
m1=0;m2=np.sqrt(7.5e-5);m3=np.sqrt(m2**2+2.431e-3);print("NO m1=0 ref",m2,m3,m1+m2+m3)
# Omega checks
print(0.068/93.14,0.0684/93.14,0.06/93.14,3/4880,3/4880*93.14,0.059/93.14/0.120,0.120/(0.068/93.14))
print("ratio",0.050/0.003,0.050/base)
print("znr",base/(3*1.68e-4),3*1.68e-4*21)
def U(t12,t23,t13,d):
    import numpy as np
    s12,c12=np.sin(t12),np.cos(t12);s23,c23=np.sin(t23),np.cos(t23);s13,c13=np.sin(t13),np.cos(t13);e=np.exp(1j*d)
    return np.array([[c12*c13,s12*c13,s13/e],[-s12*c23-c12*s23*s13*e,c12*c23-s12*s23*s13*e,s23*c13],[s12*s23-c12*c23*s13*e,-c12*s23-s12*c23*s13*e,c23*c13]])
r=np.radians
Ub=U(r(33),r(45),r(8.5),1.5);print("SetB PMNS |U|\n",np.round(abs(Ub),3));print("J",np.imag(Ub[0,0]*Ub[1,1]*np.conj(Ub[0,1])*np.conj(Ub[1,0])))
print("sin2",np.sin(r(33))**2,np.sin(r(45))**2,np.sin(r(8.5))**2)
Up=U(r(33.41),r(49.1),r(8.54),r(197));print("public |U|\n",np.round(abs(Up),3))
V=np.array([[0.97420,0.22466,0.00354],[0.22452,0.97343,0.04118],[0.00866,0.04030,0.99913]])
s13=V[0,2];t13=np.arcsin(s13);t12=np.arctan(V[0,1]/V[0,0]);t23=np.arctan(V[1,2]/V[2,2])
print("CKM angles",np.degrees([t12,t23,t13]),"rownorm2",(V**2).sum(1))
