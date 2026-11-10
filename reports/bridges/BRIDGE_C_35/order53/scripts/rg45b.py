import sys,json,math,numpy as np
src=open('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order18/scripts/a2.py').read().split('\n')
exec('\n'.join(src[:30]))
r={}
c1=lambda v:v[0]; c2=lambda v:v[0]+21*v[1]
r['T1']=bool(c1((0,1))==0 and c2((21,-1))==0)
G=[(a,b) for a in range(-30,31) for b in range(-30,31)]
def cover(f):
    seen={}
    for v in G: seen[f(v)]=seen.get(f(v),0)+1
    return all(c==1 for c in seen.values())
r['T2']=cover(lambda v:(v[0],v[1])) and cover(lambda v:(v[0]+21*v[1],-v[1]))  # (ℓ,b) for u2
def mean_line(al,be,x,v0,u):
    P=period(al,be,x,u); b=np.arange(P)
    return ph(al,be,x,np.array(v0)[None,:]+b[:,None]*np.array(u)[None,:]).mean(),P
t3=0;t4=0;tab=[]
for x in XS:
  for j,(al,be) in enumerate(pairs):
    for (u,base) in (((0,1),lambda l:(l,0)),((21,-1),lambda l:(l,0))):
      Nt=period(al,be,x,(1,0)); ms=[mean_line(al,be,x,base(l),u)[0] for l in range(2*Nt)]
      t3=max(t3,max(abs(ms[l+Nt]-ms[l]) for l in range(Nt)))
      t4=max(t4,abs(mean_line(al,be,x,(u[0],u[1]),u)[0]-ms[0]))
      if j<3 and x==XS[0]: tab.append(dict(j=j,u=u,theta=str(Fr(al[0]) if u==(0,1) else Fr(al[0])+21*Fr(al[1])),N=Nt,m=[complex(round(m.real,12),round(m.imag,12)).__repr__() for m in ms[:Nt]]))
r['T3_max']=t3;r['T4_max']=t4;r["T3"]=bool(t3<=1e-12);r["T4"]=bool(t4<=1e-12);r["T3_max"]=float(t3);r["T4_max"]=float(t4)
r['PASS']=bool(all(r[k] for k in ('T1','T2','T3','T4')))
print(json.dumps(r));json.dump(dict(r=r,sample=tab),open('../data/rg45b.json','w'),indent=1)
