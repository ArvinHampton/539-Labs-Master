# order58 RG48b: A is odd (Q(e2)=7/2); use even rescaling A(2)=[[4,14],[14,14]] (det -140). Milgram check + all definite even binary det 140.
import json,cmath,math
exec(open('rg48.py').read().split('A=[[2,7]')[0])
out={}
for name,G in (('A(2)',[[4,14],[14,14]]),):
    v,g=dform(G); out[name]=dict(n=len(v),milgram=[g.real,g.imag]); vA=v
forms=[]
for a in range(1,80):
  for c in range(a,80):
    for b in range(-2*a,2*a+1):
      if 4*a*c-b*b==140: forms.append([[2*a,b],[b,2*c]])
L=[]
for G in forms:
    v,g=dform(G); L.append(dict(gram=G,n=len(v),milgram=[round(g.real,12),round(g.imag,12)],same_qvals=v==vA,same_minus=v==sorted((-x)%1 for x in vA)))
out['definite_det140']=L; out['any_match']=any(f['same_qvals'] for f in L); out['any_match_minus']=any(f['same_minus'] for f in L)
print(json.dumps(out,indent=1)); json.dump(out,open('../data/rg48b.json','w'),indent=1)
