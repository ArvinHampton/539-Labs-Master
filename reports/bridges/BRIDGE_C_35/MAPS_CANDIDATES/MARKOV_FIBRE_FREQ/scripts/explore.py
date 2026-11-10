# Pre-PREREG exploration: lifted Markov chain of T3 on u mod M=2^k*9*... ; fibre j=((u-21)/9) mod 8 needs u mod 72.
import sys, json, hashlib, numpy as np
def T3(n): return n//3 if n%3==0 else ((4*n+2)//3 if n%3==1 else (2*n+1)//3)
def chain(M):
    src=np.arange(3*M)%M; dst=np.array([T3(r)%M for r in range(3*M)])  # uniform over 3 lifts mod 3M
    pi=np.ones(M)/M
    for _ in range(4000):
        nx=np.bincount(dst,weights=pi[src]/3,minlength=M)
        if abs(nx-pi).sum()<1e-14: pi=nx; break
        pi=nx
    hit=[0.]*8
    for r in range(M):
        if r%9==3: hit[((r-21)//9)%8]+=pi[r]
    s=sum(hit); return [h/s for h in hit], s
out={}
for k in [3,5,7,9,11]:
    M=(2**k)*27; f,s=chain(M); out[k]=dict(M=M,hitfrac=s,fib=[round(x,6) for x in f])
fib=[0]*8;h=0
for sd in range(300):
    u=int.from_bytes(hashlib.sha3_512(b'mfexplore-%d'%sd).digest(),'big')
    for i in range(539):
        u=T3(u)
        if u%9==3: h+=1; fib[((u-21)//9)%8]+=1
out['empirical']=[round(c/h,6) for c in fib]
print(json.dumps(out,indent=0))
