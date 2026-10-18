# Lemma: for z in H and T_n(w)=sqrt(y)K_0(2pi|n|y)e(nx),  int_{z}^{z+i inf} [T_n, R_z^{1/2}] = c1 * e(nz) (n>0), 0 (n<0);
# for the constant term sqrt(y) the integral is 1/2 (proved in closed form in the report).
# Green's form [u,v] = u_w v dw + u v_wbar dwbar ; R_z(w)=Im w/((w-z)(wbar-z)); v_wbar = (1/2)R^{-1/2} * i/(2(wbar-z)^2).
import mpmath as mp
mp.mp.dps=30
def integ(n,z):
    x,y=z.real,z.imag
    def f(s):
        Y=y+s; X=x
        R=Y/((1j*s)*(-1j*(2*y+s)))   # real positive
        v=mp.sqrt(R); vwb=0.5/mp.sqrt(R)*1j/(2*(-1j*(2*y+s))**2)
        if n==0:
            T=mp.sqrt(Y); Tx=0; Ty=1/(2*mp.sqrt(Y))
        else:
            a=2*mp.pi*abs(n)
            e=mp.expjpi(2*n*X)
            T=mp.sqrt(Y)*mp.besselk(0,a*Y)*e
            Tx=2j*mp.pi*n*T
            Ty=e*(mp.besselk(0,a*Y)/(2*mp.sqrt(Y))-mp.sqrt(Y)*a*mp.besselk(1,a*Y))
        Tw=0.5*(Tx-1j*Ty)
        return 1j*(Tw*v - T*vwb)
    return mp.quad(f,[0,0.01,0.1,1,mp.inf])
out=[]
for n in [0,1,2,3,-1,-2]:
    for z in [mp.mpc(0.3,0.5),mp.mpc(-1.1,0.2)]:
        I=integ(n,z)
        ratio = I/mp.exp(2j*mp.pi*n*z) if n>0 else I
        out.append(f"n={n:2d} z={complex(z)}: integral={mp.nstr(I,15)}   {'integral/e(nz)' if n>0 else 'value'}={mp.nstr(ratio,15)}")
out.append(f"compare -1/4 = -0.25, -1/2, pi... ; 1/2 for n=0")
print("\n".join(out)); open("lemma_c1.txt","w").write("\n".join(out)+"\n")
