N=80
def mul(a,b):
    c=[0]*N
    for i,x in enumerate(a):
        if x:
            for j,y in enumerate(b[:N-i]): c[i+j]+=x*y
    return c
def inv(a):
    b=[0]*N; b[0]=1
    for n in range(1,N): b[n]=-sum(a[k]*b[n-k] for k in range(1,n+1))
    return b
def poch(fn,n):  # prod_{j=1..n} fn(j) where fn returns series
    r=[1]+[0]*(N-1)
    for j in range(1,n+1): r=mul(r,fn(j))
    return r
def mono(e,c=1):
    s=[0]*N
    if e<N: s[e]+=c
    return s
def one_plus(e,sign=1):
    s=mono(0); 
    if e<N: s[e]+=sign
    return s
def ssum(terms):
    r=[0]*N
    for t in terms: r=[x+y for x,y in zip(r,t)]
    return r
def g(s):
    return ssum(mul(mono(n*n),inv(poch(lambda j:one_plus(s*j),n))) for n in range(9))
out={}
for s in [1,2,3,4,7,8,11]: out[f"g_{s}"]=g(s)
# 7th order Ramanujan: F0=sum q^{n^2}/(q^{n+1};q)_n, F1=sum q^{n^2}/(q^n;q)_n (n>=1), F2=sum q^{n^2+n}/(q^{n+1};q)_{n+1}
def qp(a,n): return poch(lambda j:one_plus(a+j-1,-1),n)
out["F0_7th"]=ssum(mul(mono(n*n),inv(qp(n+1,n))) for n in range(9))
out["F1_7th"]=ssum(mul(mono(n*n),inv(qp(n,n))) for n in range(1,9))
out["F2_7th"]=ssum(mul(mono(n*n+n),inv(qp(n+1,n+1))) for n in range(9))
# 3rd order f, phi, psi, chi, omega
out["f_3rd"]=ssum(mul(mono(n*n),inv(mul(poch(lambda j:one_plus(j),n),poch(lambda j:one_plus(j),n)))) for n in range(9))
# 8th order Gordon-McIntosh: S0=sum q^{n^2}(-q;q^2)_n/(-q^2;q^2)_n, S1=sum q^{n(n+2)}(-q;q^2)_n/(-q^2;q^2)_n
# T0=sum q^{(n+1)(n+2)}(-q^2;q^2)_n/(-q;q^2)_{n+1}, T1=sum q^{n(n+1)}(-q^2;q^2)_n/(-q;q^2)_{n+1}
A=lambda n:poch(lambda j:one_plus(2*j-1),n); B=lambda n:poch(lambda j:one_plus(2*j),n)
out["S0_8th"]=ssum(mul(mono(n*n),mul(A(n),inv(B(n)))) for n in range(9))
out["S1_8th"]=ssum(mul(mono(n*n+2*n),mul(A(n),inv(B(n)))) for n in range(9))
out["T0_8th"]=ssum(mul(mono((n+1)*(n+2)),mul(B(n),inv(A(n+1)))) for n in range(9))
out["T1_8th"]=ssum(mul(mono(n*n+n),mul(B(n),inv(A(n+1)))) for n in range(9))
with open("coeff_table.txt","w") as f:
    for k,v in out.items(): f.write(f"{k}: {v[:61]}\n")
for k,v in out.items(): print(k,v[:40])
# check g7 sequence via d-formula
