# Local-derived (t4436, branch V-2). Numerical ILLUSTRATION only (the proof is in the findings file, from Poisson summation F0-5):
#  (i)  theta1(-1/(7 tau)) = -i sqrt(7) tau theta1(tau),  theta1 = sum_{x,y in Z} q^{x^2+xy+2y^2}  (norm form of Z[(1+sqrt-7)/2], disc -7)
#  (ii) g+ := theta1(tau)^2 - 7 theta1(7 tau)^2 satisfies g+|_2 W49 = +g+, i.e. 49 (49 tau)^-2 g+(-1/(49 tau)) = g+(tau).
import mpmath as mp
mp.mp.dps=40
def th(tau,R=60):
    q=mp.exp(2j*mp.pi*tau); s=mp.mpf(0)
    for x in range(-R,R+1):
        for y in range(-R,R+1):
            s+=q**(x*x+x*y+2*y*y)
    return s
g=lambda t: th(t)**2-7*th(7*t)**2
for tau in [mp.mpc(0.11,0.31), mp.mpc(-0.23,0.27), mp.mpc(0.05,0.2)]:
    lhs=th(-1/(7*tau)); rhs=-1j*mp.sqrt(7)*tau*th(tau)
    print(f"tau={tau}: |theta1(-1/(7tau)) - (-i sqrt7 tau theta1(tau))| = {mp.nstr(abs(lhs-rhs),5)}  (|lhs| = {mp.nstr(abs(lhs),8)})")
    gl=49*(49*tau)**-2*g(-1/(49*tau)); gr=g(tau)
    print(f"      |g+|W49 - g+| = {mp.nstr(abs(gl-gr),5)}  (|g+| = {mp.nstr(abs(gr),8)});  |g+|W49 + g+| = {mp.nstr(abs(gl+gr),5)}")
print("first coefficients of g+ (n=0..14):")
N=15; c=[0]*N
for x in range(-8,9):
    for y in range(-8,9):
        for u in range(-8,9):
            for v in range(-8,9):
                n=(x*x+x*y+2*y*y)+(u*u+u*v+2*v*v)
                if n<N: c[n]+=1
c7=[0]*N
for n in range(N):
    pass
t1=[0]*N
for x in range(-8,9):
    for y in range(-8,9):
        n=x*x+x*y+2*y*y
        if n<N: t1[n]+=1
sq=[sum(t1[i]*t1[n-i] for i in range(n+1)) for n in range(N)]
g7=[0]*N
for n in range(N):
    if n%7==0: g7[n]=sq[n//7]
print([sq[n]-7*g7[n] for n in range(N)])
