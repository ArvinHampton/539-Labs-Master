import numpy as np, sys, time
N=int(sys.argv[1]); CH=10_000_000; CAP=2000
maxsteps=0; maxpeak=0; t0=time.time()
for lo in range(3, N+1, CH):
    hi=min(N, lo+CH-1)
    n=np.arange(lo,hi+1,dtype=np.int64)
    n=n[n%3==1]          # residues 0,2 descend in one step: T(3k)=k<3k (k>=1), T(3k+2)=2k+1<3k+2
    x=n.copy(); steps=0
    while n.size:
        r=x%3
        x=np.where(r==0,x//3,np.where(r==1,(4*x+2)//3,(2*x+1)//3))
        steps+=1
        m=int(x.max()); maxpeak=max(maxpeak,m)
        assert m < 2**61
        keep = x>=n
        n=n[keep]; x=x[keep]
        if steps>CAP: print("CAP",lo,n[:5]); sys.exit(1)
    maxsteps=max(maxsteps,steps)
print({"N":N,"all_descend":True,"max_first_descent_steps":maxsteps,"max_peak":maxpeak,"secs":round(time.time()-t0,1)})
