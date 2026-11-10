import math,json
def T3(n):
    k,r=divmod(n,3); return (k,4*k+2,2*k+1)[r]
out={}
for K in (7,11,17,67):
    sq={x*x%K for x in range(K)}; null=len(sq)/K; f=[]
    for j in range(2000):
        u=10**12+7919*j; c=t=0
        while u!=1:
            c+= (u%K in sq); t+=1; u=T3(u)
        f.append(c/t)
    m=sum(f)/len(f); sd=(sum((x-m)**2 for x in f)/(len(f)-1))**.5
    z=(m-null)/(sd/len(f)**.5); p=0.5*math.erfc(z/2**.5)
    out[K]=dict(null=null,mean=m,sd=sd,z=z,p=p,excess=m-null)
ps=sorted(out,key=lambda k:out[k]['p']); adj=0
for i,k in enumerate(ps):
    adj=max(adj,min(1,(4-i)*out[k]['p'])); out[k]['p_holm']=adj
    out[k]['PASS']=adj<0.01 and out[k]['excess']>=0.02
print(json.dumps(out,indent=1))
