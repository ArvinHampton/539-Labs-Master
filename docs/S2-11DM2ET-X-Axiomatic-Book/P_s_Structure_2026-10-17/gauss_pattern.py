# Check of Theorem G: for gcd(h,m)=1, G(h/m) := (2m)^-2 sum_{n,k mod 2m} e(h Q_s(n,k)/m) satisfies
#   G = 0 if 2|m or 5|m;  |G| = 1/m if gcd(m,70)=1;  |G| = sqrt7/m if 7|m, gcd(m,10)=1.
import numpy as np, math
bad=[]; checked=0
for m in range(1,106):
    L=2*m; n=np.arange(L)[:,None]; k=np.arange(L)[None,:]
    Q=(n*n+7*n*k+7*k*(k+1)//2)
    for h in range(1,m+1):
        if math.gcd(h,m)!=1: continue
        G=np.exp(2j*np.pi*((h*Q)%m)/m).sum()/L**2
        if m%2==0 or m%5==0: pred=0.0
        elif m%7==0: pred=math.sqrt(7)/m
        else: pred=1.0/m
        checked+=1
        if abs(abs(G)-pred)>1e-9: bad.append((h,m,abs(G),pred))
msg=f"checked {checked} pairs (h,m), m<=105: mismatches {len(bad)} {bad[:5]}"
print(msg); open("gauss_pattern.txt","w").write(msg+"\n")
