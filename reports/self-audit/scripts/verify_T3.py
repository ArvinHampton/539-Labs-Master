# README.md canonical T3; measure non-injectivity / image shrinkage of T3^L on [0,N)
def T3(n):
  r=n%3
  return n//3 if r==0 else ((4*n+2)//3 if r==1 else (2*n+1)//3)
o=[]
N=3**12
xs=list(range(N))
for L in [1,2,5,10,20,50]:
  ys=xs
  for _ in range(L): ys=[T3(y) for y in ys]
  o.append(f"L={L}: |image of T3^L on [0,{N})| = {len(set(ys))}  ({len(set(ys))/N:.3f} of domain)")
o.append("Example collision: T3(9)=3, T3(5)=3 -> T3 not injective")
o.append(f"check T3(9)={T3(9)} T3(5)={T3(5)}")
import random
def steps(n):
  i=0
  while n>3 and i<10000: n=T3(n); i+=1
  return i
random.seed(1); s=[steps(random.getrandbits(60)) for _ in range(2000)]
o.append(f"steps to <=3 for 2000 random 60-bit seeds: min {min(s)} max {max(s)} mean {sum(s)/len(s):.1f} (README says ~90-120 for 1e18; Zenodo 18603243 says 539±1)")
open('scripts/verify_T3.out','w').write("\n".join(o)); print("\n".join(o))
