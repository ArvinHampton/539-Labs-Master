# Analytic Euler-Maclaurin coefficients (t^-1, t^-1/2, t^0) for shifted quadrant sums
#   S(t) = sum_{i,j>=0} exp(-t*Q(i+al, j+be)),  Q(x,y) = A11 x^2 + 2 A12 xy + A22 y^2 + l1 x + l2 y + c0.
import mpmath as mp
mp.mp.dps = 30
def B1(x): return x - mp.mpf(1)/2
def B2(x): return x*x - x + mp.mpf(1)/6
def M(A11,A12,A22,p,r):
    w = mp.mpf(p+r+2)/2
    return mp.gamma(w)/2*mp.quad(lambda u: u**r/(A11+2*A12*u+A22*u*u)**w, [0,1,10,mp.inf])
def em(A11,A12,A22,l1,l2,c0,al,be):
    A11,A12,A22,l1,l2,c0,al,be = map(mp.mpf,(A11,A12,A22,l1,l2,c0,al,be))
    M00=M(A11,A12,A22,0,0)
    ML = l1*M(A11,A12,A22,1,0)+l2*M(A11,A12,A22,0,1)
    ML2 = l1**2*M(A11,A12,A22,2,0)+2*l1*l2*M(A11,A12,A22,1,1)+l2**2*M(A11,A12,A22,0,2)
    gx = mp.sqrt(mp.pi)/(2*mp.sqrt(A11)); gy = mp.sqrt(mp.pi)/(2*mp.sqrt(A22))
    cm2 = M00
    cm1 = -ML - B1(be)*gx - B1(al)*gy
    c0_ = ML2/2 - c0*M00 + B1(be)*l1/(2*A11) + B2(be)*A12/(2*A11) + B1(al)*l2/(2*A22) + B2(al)*A12/(2*A22) + B1(al)*B1(be)
    return [cm2,cm1,c0_]
def em1(a,b,c=0,al=0):   # sum_{j>=0} exp(-t(a(j+al)^2 + b(j+al) + c))
    a,b,c,al=map(mp.mpf,(a,b,c,al))
    return [mp.mpf(0), mp.sqrt(mp.pi)/(2*mp.sqrt(a)), -b/(2*a) - B1(al)]
def add(*terms):
    out=[mp.mpf(0)]*3
    for c,v in terms:
        for i in range(3): out[i]+=c*v[i]
    return out
h = mp.mpf(7)/2
# Q_s: A11=1, A12=7/2, A22=7/2, l=(0,7/2);   Q_-: l=(0,-7/2)
Ps  = em(1,h,h,0, h,0, 0,0)
R   = em(1,h,h,0, h,0, 0,1)          # n>=0,k>=1
Mm  = em(1,h,h,0,-h,0, 1,0)          # n>=1,k>=0 of Q_-  (= C_third + sum_{n>=1} q^{n^2})
Ct  = em(1,h,h,0,-h,0, 1,1)          # C_third
E   = add((1,R),(1,Mm))
# H_s via K+- decomposition: v = x v1 + y v2, v1=(0,1), v2=(21,-1); quad 3.5x^2+140xy+297.5y^2
Kp = add(*[(1,em(h,70,mp.mpf(595)/2, h,-h,0, mp.mpf(s)/21, mp.mpf(s)/21)) for s in range(21)])
Km = add(*[(1,em(h,70,mp.mpf(595)/2,-h, h,0, mp.mpf(s)/21, mp.mpf(s)/21)) for s in range(21)])
W1p=em1(h,h); W2p=em1(mp.mpf(595)/2,-h); W1m=em1(h,-h); W2m=em1(mp.mpf(595)/2,h)
H = add((1,Kp),(-0.5,W1p),(-0.5,W2p),(-1,Km),(0.5,W1m),(0.5,W2m))
C = add((1,Ps),(-1,H))
res = {"P_s":Ps,"R":R,"Mm":Mm,"C_third":Ct,"E":E,"H_s":H,"C":C}
if __name__=="__main__":
    I = mp.log(6+mp.sqrt(35))/(2*mp.sqrt(35))
    for kname,v in res.items():
        print(f"{kname:8} t^-1: {mp.nstr(v[0],22):>26}   t^-1/2: {mp.nstr(v[1],22):>26}   t^0: {mp.nstr(v[2],22):>26}")
    print("I =", I)
