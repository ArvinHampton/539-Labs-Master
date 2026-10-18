"""Independent re-derivation of the function-space dimension of the 140 lift functions (input to the 42=36+6 erratum).
Fourier coefficients from the explicit lift formula of Section 5.3:
  u_{al,be}(w) = sqrt(y)[ log(eps) [al in Z^2] + 1/2 sum_{nu in (al+Z^2) mod gamma^2, nu != 0} e(B(nu,be)) K0(2pi|Q(nu)|y) e(Q(nu)x) ]
gamma^2-fundamental cones: [e1, g^2 e1), [f, g^2 f) (f=(1,-1)) and their negatives.
Distinct frequencies give linearly independent mode functions, so dim span{u} = rank of the label x mode matrix C.
Written from scratch (no reuse of cusp-part/uvec.py)."""
import numpy as np, math, sys
sys.path.insert(0,'.')
import thmF_exact as F   # labels, S, T, P (rebuilt independently)
D=70; A=np.array([[2,7],[7,7]])
g=np.array([[-1,-7],[2,13]]); g2=g@g
X=float(sys.argv[1]) if len(sys.argv)>1 else 25.0
def cone_pts(al70, r, sgn):
    r=np.array(r); r2=g2@r; det=int(r[0]*r2[1]-r[1]*r2[0])
    # bound: |Q(s r + t r2)| <= X  => s,t <= sqrt(X/|Q(r)|) (both terms same sign, cross term same sign)
    Qr=abs(r@A@r)/2; smax=math.sqrt(X/Qr)+1
    Bx=int(math.ceil(smax*(abs(r).max()+abs(r2).max())))+2
    n=np.arange(-Bx,Bx+1)
    N1,N2=np.meshgrid(n,n,indexing='ij')
    v1=sgn*(al70[0]+D*N1.ravel()); v2=sgn*(al70[1]+D*N2.ravel())   # 70*nu  (sgn=-1: negatives of the cone)
    # nu in sgn*cone  <=> sgn*nu in cone ; we enumerate mu = al+n and test sgn*mu in cone, i.e. v = sgn*70*mu
    s_num=v1*r2[1]-v2*r2[0]; t_num=r[0]*v2-r[1]*v1      # s = s_num/(70 det), t = t_num/(70 det)
    if det<0: s_num,t_num=-s_num,-t_num
    m=(s_num>0)&(t_num>=0)
    v1=v1[m]; v2=v2[m]; mu1=sgn*v1; mu2=sgn*v2           # 70*mu, mu in al+Z^2
    q=(2*mu1*mu1+14*mu1*mu2+7*mu2*mu2)                    # = 2*4900*Q(mu)
    k=np.abs(q)<=X*9800
    return mu1[k],mu2[k],q[k]
labels=F.LAB
cols={}
rows=[]
for i,(al,be) in enumerate(labels):
    al70=np.array([int(c*D) for c in al]); be70=np.array([int(c*D) for c in be])
    acc={}
    for r in [(1,0),(1,-1)]:
        for sgn in (1,-1):
            m1,m2,q=cone_pts(al70,r,sgn)
            ph=np.exp(2j*np.pi*((m1*(A@be70)[0]+m2*(A@be70)[1])%4900)/4900)
            for qq,pp in zip(q.tolist(),ph.tolist()):
                acc[qq]=acc.get(qq,0)+0.5*pp
    if all(c.denominator==1 for c in al): acc['const']=acc.get('const',0)+math.log(6+math.sqrt(35))
    rows.append(acc)
keys=sorted({k for r in rows for k in r}, key=lambda k:(k=='const', k if k!='const' else 0))
C=np.array([[r.get(k,0) for k in keys] for r in rows])
C=C[:, np.abs(C).max(0)>1e-12]
sv=np.linalg.svd(C,compute_uv=False)
rk=int((sv>1e-8*sv[0]).sum())
out=[]
def pr(*s): print(*s); out.append(" ".join(map(str,s)))
pr(f"|Q|<={X}: {C.shape[1]} nonzero modes; singular values around the gap: {sv[rk-2]:.3e}, {sv[rk-1]:.3e} | {sv[rk]:.3e}; rank = {rk}")
S,T,P=F.S,F.T,F.P
def rank(M): s=np.linalg.svd(M,compute_uv=False); return int((s>1e-8*s[0]).sum())
pr("S-invariance: rank[C|SC] =",rank(np.hstack([C,S@C])), "; T-invariance: rank[C|TC] =",rank(np.hstack([C,T@C])), "; P C = C:",f"{np.abs(P@C-C).max():.1e}")
# cusp labels per Section 7.2: beta=-a, 70*alpha_1 in {7,21,49,63}
cusp=[i for i,(al,be) in enumerate(labels) if be!=F.zero and int(al[0]*70) in (7,21,49,63)]
pr("cusp labels by the Section 7.2 description:",len(cusp))
CE=C.copy(); CE[cusp,:]=0; CC=C-CE
pr("rank V_Eis (cusp rows zeroed) =",rank(CE), "; rank V_cusp =",rank(CC), "; S-inv:",rank(np.hstack([CE,S@CE])),rank(np.hstack([CC,S@CC])), "; T-inv:",rank(np.hstack([CE,T@CE])),rank(np.hstack([CC,T@CC])))
def trS(M):
    U,s,_=np.linalg.svd(M); B=U[:,:rank(M)]; return np.trace(B.conj().T@S@B)
pr(f"tr S on V = {trS(C).real:+.2e}, on V_Eis = {trS(CE).real:+.2e}, on V_cusp = {trS(CC).real:+.2e}  (S^2=I there, so n+ = n- = dim/2)")
open(f"vspace_check_X{int(X)}.txt","w").write("\n".join(out)+"\n")
# precise cusp list of [S5, 3.3]: beta=-a, 70*al1 in {7,21,49,63} and 70*al2 NOT a multiple of 14 (i.e. 7 | den(al2))
cusp24=[i for i in cusp if int(labels[i][0][1]*70)%14!=0]
extra=[i for i in cusp if i not in cusp24]
pr("precise cusp labels:",len(cusp24), "; the 4 extra labels of the loose description:", [(tuple(int(c*70) for c in labels[i][0])) for i in extra], "; their row norms in C:", [f"{np.abs(C[i]).max():.2e}" for i in extra])
CE=C.copy(); CE[cusp24,:]=0; CC=C-CE
pr("with the precise 24: rank V_Eis =",rank(CE), "; rank V_cusp =",rank(CC), "; S-inv:",rank(np.hstack([CE,S@CE])),rank(np.hstack([CC,S@CC])), "; T-inv:",rank(np.hstack([CE,T@CE])),rank(np.hstack([CC,T@CC])))
open(f"vspace_check_X{int(X)}.txt","w").write("\n".join(out)+"\n")
zr=[i for i in range(len(labels)) if np.abs(C[i]).max()<1e-12]
pr("labels whose lift function vanishes identically (all modes |Q|<=X zero):",len(zr), [(tuple(str(c) for c in labels[i][0]), 'be=0' if labels[i][1]==F.zero else 'be=-a') for i in zr])
open(f"vspace_check_X{int(X)}.txt","w").write("\n".join(out)+"\n")
from fractions import Fraction as Fq
def Tspec(M):
    U,sv_,_=np.linalg.svd(M); B=U[:,:rank(M)]; ev=np.linalg.eigvals(B.conj().T@T@B)
    return sorted(Fq(int(round((np.angle(z)/(2*np.pi))%1*840))%840,840) for z in ev)
sc=Tspec(CC); se=Tspec(CE)
pr("T spectrum on V_cusp (r with eigenvalue e(r)):", [str(r) for r in sc])
pr("T spectrum on V_Eis: distinct =", len(set(se)), "of", len(se), "; contains the 6 cusp values:", all(r in se for r in sc))
open(f"vspace_check_X{int(X)}.txt","w").write("\n".join(out)+"\n")
