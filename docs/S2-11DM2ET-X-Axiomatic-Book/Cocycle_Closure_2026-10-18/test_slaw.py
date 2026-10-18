import numpy as np, uvec
S=uvec.F.Smatrix(); T=uvec.F.Tmatrix()
U=uvec.U(14.0)
for w in [0.31+1.13j, -0.2+0.9j]:
    u1,_=U.ev(-1/w); u0,_=U.ev(w)
    print('S-law', w, np.max(np.abs(u1-S@u0)))
    u2,_=U.ev(w+1); print('T-law', np.max(np.abs(u2-T@u0)))
# derivative check
w=0.3+1.2j; h=1e-6
u,uw=U.ev(w); up,_=U.ev(w+h); um,_=U.ev(w-h); upi,_=U.ev(w+1j*h); umi,_=U.ev(w-1j*h)
num=0.5*((up-um)/(2*h)-1j*(upi-umi)/(2*h)); print('d/dw', np.max(np.abs(num-uw)))
