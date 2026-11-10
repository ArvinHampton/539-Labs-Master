import json
sizes=[68,68,68,67,67,67,67,67]; blk=[]
for b,s in enumerate(sizes): blk+= [b]*s
def T3(n):
    k,r=divmod(n,3); return (k,4*k+2,2*k+1)[r]
D0=sum(s*s for s in sizes)/539**2; out={'D0':D0}
for L in (1,2,3):
    P=3**L*539; C=[[0]*8 for _ in range(8)]; img=[0]*539
    for n in range(P):
        u=n
        for _ in range(L): u=T3(u)
        C[blk[n%539]][blk[u%539]]+=1; img[u%539]+=1
    D=sum(C[b][b] for b in range(8))/P
    out[L]=dict(D=D,ratio=D/D0,PASS=D>=1.5*D0,uniform_image=len(set(img))==1,C=C)
print(json.dumps(out))
