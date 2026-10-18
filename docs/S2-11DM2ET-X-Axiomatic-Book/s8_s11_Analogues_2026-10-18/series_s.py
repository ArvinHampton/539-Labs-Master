# Step (1): exact series identities for s in {7,8,11} to q^N (integer bincounts).
#  Q_s(n,k) = n^2 + s n k + (s/2) k(k+1);  nu = (n,k) + a,  a = (s/(2(s-2)), -1/(s-2));  Q_s = Q2(nu) + c0, c0 = s/(4(s-2)).
#  R = sum_{n>=0,k>=1}, Mm = sum_{n<=-1,k<=0} (= C_third + sum_{n>=1} q^{n^2}),  E := R + Mm,  Theta_hol := Mm - R
#  (= sum_{n>=1,k>=0} q^{Q_-} - sum_{n<=0,k<=-1} q^{Q_-}, Q_-(n,k) = Q_s(-n,-k), the Zwegers form of the levers report).
#  Checks: 2P_s = E + 1 + theta_3 - Theta_hol;  E == sum over gamma-fundamental cones [r, gamma r) for several r;  E_{-a} == E_a.
import sys, numpy as np
from fractions import Fraction as Fr
N=int(sys.argv[1]) if len(sys.argv)>1 else 3000
out=[]
for s in (7,8,11):
    d=2*(s-2)                          # X = d*nu integer
    a=(Fr(s,2*(s-2)),Fr(-1,s-2)); c0=Fr(s,4*(s-2))
    Bn=int(2.2*np.sqrt(N))+40; Bk=int(2.2*np.sqrt(N))+40
    n=np.arange(-6*Bn,6*Bn+1)[:,None]; k=np.arange(-6*Bk,6*Bk+1)[None,:]
    Qs=n*n+s*n*k+(s*k*(k+1))//2
    def cnt(mask,Q=Qs):
        m=mask&(Q<=N)&(Q>=0)
        assert not(m[0,:].any() or m[-1,:].any() or m[:,0].any() or m[:,-1].any()), "box"
        return np.bincount(Q[m].astype(np.int64),minlength=N+1)[:N+1]
    R=cnt((n>=0)&(k>=1)); Mm=cnt((n<=-1)&(k<=0)); P=cnt((n>=0)&(k>=0))
    Qm=n*n+s*n*k+(s*k*(k-1))//2
    Th=cnt((n>=1)&(k>=0),Qm)-cnt((n<=0)&(k<=-1),Qm)
    th3=np.zeros(N+1,np.int64)
    for t in range(-200,201):
        if t*t<=N: th3[t*t]+=1
    one=np.zeros(N+1,np.int64); one[0]=1
    E=R+Mm
    out.append(f"s={s}: a={a}, c0={c0}, Theta_hol(Q_- form) == Mm - R: {(Th==Mm-R).all()};  2P_s == E + 1 + theta3 - Theta_hol (to q^{N}): {(2*P==E+one+th3-Th).all()}")
    # gamma cones in nu coords: nu = ((n,k)+a); X = d*nu
    X1=d*n+int(d*a[0]); X2=d*k+int(d*a[1])
    g=np.array([[-1,-s],[2,2*s-1]])
    for r in [(1,0),(1,1),(2,1),(1,2),(3,-1)]:
        if r[0]**2+s*r[0]*r[1]+Fr(s,2)*r[1]**2<=0: continue
        gr=g@np.array(r); det=r[0]*gr[1]-r[1]*gr[0]
        assert det>0
        mask=((X1*gr[1]-X2*gr[0])>0)&((r[0]*X2-r[1]*X1)>=0)
        Er=cnt(mask)
        out.append(f"   E == sum over gamma-cone [r,gamma r), r={r}: {(Er==E).all()}")
    # E_{-a}: coset -a, same cone r=(1,0); Q2(nu)+c0 with nu=(n,k)-a  -> Q = Q2(-( (-n,-k)+a ))+c0 = Q_s(-n,-k)
    X1m=d*n-int(d*a[0]); X2m=d*k-int(d*a[1])
    gr=g@np.array((1,0))
    mask=((X1m*gr[1]-X2m*gr[0])>0)&((1*X2m-0*X1m)>=0)
    Em=cnt(mask,Qm)
    out.append(f"   E_(-a) == E_a: {(Em==E).all()};  first E coefficients (q^0..q^40): {E[:41].tolist()}")
print("\n".join(out)); open("series_s.txt","w").write("\n".join(out)+"\n")
