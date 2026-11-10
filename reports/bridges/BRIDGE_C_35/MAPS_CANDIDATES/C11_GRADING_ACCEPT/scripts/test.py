import json
tau=lambda x: x//21 if x<420 else 20+(x-420)//20
O=[21+9*j for j in range(539)]; g=[(-1)**tau(x) for x in O]
size=[sum(1 for j in range(539) if j%8==r) for r in range(8)]
S=[sum(g[j] for j in range(539) if j%8==r) for r in range(8)]
cond=[S[r]==0 if size[r]==68 else abs(S[r])==1 for r in range(8)]
r=dict(block_sizes=size,S=S,conditions=cond,nonconstant=len(set(g))==2,total=sum(g),
 prefix18=sum(g[:18]),body521=sum(g[18:]),n_plus=g.count(1),n_minus=g.count(-1),
 verdict='PASS' if all(cond) else 'FAIL',category='A')
print(json.dumps(r)); json.dump(r,open('data/test.json','w'),indent=1)
