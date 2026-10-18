# For each even n, nearest odd partners above (nu) and below (nd) with partner^2 = n^2 mod 7.
# U(n,m): a_n(m) <= a_nu(m - (nu^2-n^2)/7);  Dn(n,m): a_n(m) <= a_nd(m + (n^2-nd^2)/7)
# Report: last m (<=Mmax) where U fails  -> U holds for m > that (within table);  m-set where Dn fails.
import pickle
A=pickle.load(open('a_200_6000.pkl','rb')); M=len(A[0])-1
def a(n,m): return A[n][m] if 0<=m<=M else None
def partners(n):
    up=min(x for x in range(n+1,n+15) if x%2 and (x*x-n*n)%7==0)
    dn=max([x for x in range(max(1,n-14),n) if x%2 and (n*n-x*x)%7==0],default=None)
    return up,dn
print(' n  class nu  nd | U: last fail m (rho=m/n^2) | Dn: fails at m<= (rho), first m where Dn fails above that region')
for n in range(20,150,2):
    up,dn=partners(n); sh_u=(up*up-n*n)//7
    lastU=max([m for m in range(0,M-0) if a(n,m)>(a(up,m-sh_u) or 0)],default=-1)
    if dn is None: continue
    sh_d=(n*n-dn*dn)//7
    fD=[m for m in range(0,M-sh_d) if a(n,m)>a(dn,m+sh_d)]
    # split Dn fails into low-m block and high-m block
    low=[m for m in fD if m< n*n*0.2]; high=[m for m in fD if m>=n*n*0.2]
    print(f'{n:3d} {n*n%7}  {up:3d} {dn:3d} | U last fail m={lastU} ({lastU/n/n:.3f}) | Dn low fails max m={max(low,default=-1)} ({max(low,default=-1)/n/n:.3f}), high fails min m={min(high,default=-1)} ({min(high,default=-1)/n/n:.3f})')
