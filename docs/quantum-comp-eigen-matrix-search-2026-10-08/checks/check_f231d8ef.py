# Checks for chat f231d8ef "Gamma Ray Neutrino Annihilation Study"
import numpy as np
c=299792.458; H0=67.4; Om=0.315; OL=1-Om
def Dc(z,n=200000):
    zz=np.linspace(0,z,n); return c/H0*np.trapezoid(1/np.sqrt(Om*(1+zz)**3+OL),zz)
def radec(rah,ram,ras,dd,dm,ds):
    ra=np.radians(15*(rah+ram/60+ras/3600)); de=np.radians(dd+dm/60+ds/3600); return ra,de
def vec(ra,de,D): return D*np.array([np.cos(de)*np.cos(ra),np.cos(de)*np.sin(ra),np.sin(de)])
def tora(v):
    r=np.linalg.norm(v); de=np.degrees(np.arcsin(v[2]/r)); ra=np.degrees(np.arctan2(v[1],v[0]))%360
    h=ra/15; return r,h,de
def fmt(h,de):
    H=int(h); M=int((h-H)*60); S=((h-H)*60-M)*60
    sgn='+' if de>=0 else '-'; a=abs(de); d=int(a); m=(a-d)*60
    return f"{H:02d}h{M:02d}m{S:04.1f}s {sgn}{d:02d}d{m:04.1f}'"
D08=Dc(0.8); D0805=Dc(0.805); print("D_c(z=0.8)=%.1f Mpc, D_c(0.805)=%.1f"%(D08,D0805))
GA=radec(14,10,0,48,30,0); BR=radec(15,26,30,43,18,0)
cosang=np.sin(GA[1])*np.sin(BR[1])+np.cos(GA[1])*np.cos(BR[1])*np.cos(GA[0]-BR[0])
ang=np.degrees(np.arccos(cosang)); print("GA-BR angular sep = %.2f deg"%ang)
g=vec(*GA,D08); b=vec(*BR,D08); s=np.linalg.norm(b-g); print("GA-BR comoving sep at z=0.8 = %.0f Mpc (printed 1180+-40)"%s)
# Interpretation 1: third vertex on the same comoving shell (both solutions)
m=(g+b)/2; u=(b-g)/s; n=np.cross(g,b); n/=np.linalg.norm(n)  # normal to observer-GA-BR plane
w=np.cross(n,u)  # in-plane perpendicular to GA-BR
# points at distance s from both: m + h*(cos t * w + sin t * n), h = s*sqrt(3)/2
h=s*np.sqrt(3)/2
for t in np.linspace(0,2*np.pi,3600,endpoint=False):
    p=m+h*(np.cos(t)*w+np.sin(t)*n)
sol=[]
# solve |p| = D08
ts=np.linspace(0,2*np.pi,200000); P=m[None,:]+h*(np.cos(ts)[:,None]*w[None,:]+np.sin(ts)[:,None]*n[None,:])
f=np.linalg.norm(P,axis=1)-D08; idx=np.where(np.sign(f[:-1])!=np.sign(f[1:]))[0]
for i in idx:
    r,hh,de=tora(P[i]); print("same-shell vertex:",fmt(hh,de),"D=%.0f"%r)
# Interpretation 2: in observer-GA-BR plane (+-60 deg rotation about n)
for sgn in (+1,-1):
    th=np.radians(60)*sgn; V=b-g
    R=np.cos(th)*V+np.sin(th)*np.cross(n,V)+(1-np.cos(th))*np.dot(n,V)*n
    p=g+R; r,hh,de=tora(p); print("in-plane vertex (%+d):"%sgn,fmt(hh,de),"D=%.0f Mpc"%r)
# printed vertex
T=radec(14,2,12,52,44,0); t=vec(*T,D0805)
print("printed vertex: dist to GA %.0f, to BR %.0f Mpc"%(np.linalg.norm(t-g),np.linalg.norm(t-b)))
for nm,X in (("GA",GA),("BR",BR)):
    ca=np.sin(T[1])*np.sin(X[1])+np.cos(T[1])*np.cos(X[1])*np.cos(T[0]-X[0]); print(" ang sep printed-vertex to",nm,"%.2f deg"%np.degrees(np.arccos(ca)))
# DA and angular size of 1.18 Gpc
DA=D0805/1.805; print("D_A(0.805)=%.0f Mpc; 1180 Mpc comoving -> %.1f deg; 1180 Mpc proper -> %.1f deg"%(DA,np.degrees(1180/D0805),np.degrees(1180/DA)))
# turn-16 arithmetic
ly=9.4607e15; print("1.3 Gly in m = %.3e (printed 4.0e24)"%(1.3e9*ly)); print("light time 1.3 Gly = %.3e s (printed 4.23e17)"%(1.3e9*3.15576e7))
print("4.23e17/539.9=%.3e; 7.83e14*5400=%.3e"%(4.23e17/539.9,7.83e14*5400))
print("32*(360/539.9)=%.2f (printed 59.3); 1001^2-3481=%d"%(32*360/539.9,1001**2-3481))
print("(1+0.45*f*Omega)=38 needs kappa*f*Omega=37; 38*3e-26=%.2e"%(38*3e-26))
# turn-28 arithmetic
print("T28 span: 0.45*sqrt(1e-20)*3e8*1.0*0.68 = %.3e (printed '≈ 4.5 Gpc')"%(0.45*np.sqrt(1e-20)*3e8*0.68))
print("T28 delta: 9.70e-3*1 + 0.18*(1+0.05*exp(-1e-21/67.4))*0.31*exp(-1e17/(8.617e-5*2.7)) = %.4f (printed ≈1.8)"%(9.70e-3+0.18*(1+0.05*np.exp(-1e-21/67.4))*0.31*np.exp(-1e17/(8.617e-5*2.7))))
pc=3.0857e16; print("T28 light time 0.4 Gpc = %.3e s (printed 1.26e17); 1.26e17/539.9=%.3e"%(0.4e9*pc/2.998e8,1.26e17/539.9))
print("T2: 23:41 HKT = %d s after midnight (claimed 539.9 s)"%((23*60+41)*60))
print("delta m_warp 0.1 TeV/50 = %.1f GeV (claimed to match 20 GeV peak)"%(100/50))
