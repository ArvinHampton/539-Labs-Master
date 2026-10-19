import math
from latt import lat, Qp
def Hv(s,a,N):
    g,m,b,nw,kw=lat(s); P=2*N
    return tuple(tuple(sorted([(a*Qp(s,c*nw+y*m,c*kw+y*b))%N for y in range(P)])) for c in range(P))
for N,a in [(2,1),(4,1),(4,3),(8,1),(8,3),(16,1)]:
    L=24*2*N
    per=min(d for d in range(1,L+1) if L%d==0 and all(Hv(s,a,N)==Hv(s+d,a,N) for s in range(5,5+2*L)))
    print(N,a,'period',per)
