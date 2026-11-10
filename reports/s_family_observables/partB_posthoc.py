# POST-HOC (not pre-registered): per-target p-values under N1/N2/N3 and a jitter null N4; global statistic excluding T15,T16
import warnings; warnings.filterwarnings('ignore')
import numpy as np, json, math, csv, runpy, sys, io
src=open('partB_match.py').read().split("Mobs,perobs,hits=count(Q,True)")[0]
g={}; exec(src,g)
Q,T,count,R=g['Q'],g['T'],g['count'],g['R']
Mobs,perobs,hits=count(Q,True)
rng=np.random.default_rng(2026)
def logu(v,n):
  pos=v[v>0]; o=np.exp(rng.uniform(math.log(pos.min()),math.log(pos.max()),n)); o[:np.sum(v<=0)]=0; return o
import cypari2,random
pari=cypari2.Pari(); pari.allocatemem(10**9); rr=random.Random(12345); pool=[]
nmin,nmax=int(R[0]['n_s']),int(R[-1]['n_s'])
while len(pool)<5000:
  d=rr.randint(nmin,nmax)
  if pari.issquarefree(d) and d>1: pool.append((d,float(pari.quadregulator(int(pari.quaddisc(d))))))
pool=np.array(pool)
nt=10000; per={k:np.zeros((nt,len(T))) for k in ('N1','N2','N3','N4')}
for t in range(nt):
  per['N1'][t]=count({k:(logu(v,len(v)) if k!='Q3' else v) for k,v in Q.items()})[1]
  idx=rng.integers(0,len(pool),496); d=pool[idx,0]; rg=pool[idx,1]
  q2=dict(Q); q2.update(Q1=2*rg,Q2=rg/(2*np.sqrt(d)),Q5=np.sqrt(d)); per['N2'][t]=count(q2)[1]
  q3=dict(Q); q3.update(Q5=np.sqrt(rng.integers(nmin,nmax+1,496)),Q1=logu(Q['Q1'],496),Q2=logu(Q['Q2'],496)); per['N3'][t]=count(q3)[1]
  q4={k:(v*np.exp(rng.normal(0,0.02,len(v))) if k!='Q3' else v) for k,v in Q.items()}; per['N4'][t]=count(q4)[1]   # 2% multiplicative jitter
names=[t[0] for t in T]; keep=[i for i,n in enumerate(names) if not n.startswith(('T15','T16'))]
out={'per_target':{},'global_excl_T15_T16':{}}
for i,n in enumerate(names):
  out['per_target'][n]={'obs':int(perobs[i]),**{k:{'mean':float(per[k][:,i].mean()),'p':float((np.sum(per[k][:,i]>=perobs[i])+1)/(nt+1))} for k in per}}
Mx=int(perobs[keep].sum())
for k in per:
  v=per[k][:,keep].sum(1); out['global_excl_T15_T16'][k]={'obs':Mx,'mean':float(v.mean()),'sd':float(v.std()),'p':float((np.sum(v>=Mx)+1)/(nt+1))}
out['hits_excl_T15_T16']=[(h[0],h[1],int(R[h[2]]['s']) if h[0]!='Q4' else sorted(g['tabS'])[h[2]],round(h[4],8),h[5]) for h in hits if not h[5].startswith(('T15','T16'))]
json.dump(out,open('partB_posthoc.json','w'),indent=1)
print(json.dumps(out['global_excl_T15_T16'],indent=1))
for n,v in out['per_target'].items(): print(n,v['obs'],{k:(round(v[k]['mean'],2),round(v[k]['p'],3)) for k in per})
print(len(out['hits_excl_T15_T16'])); [print(h) for h in out['hits_excl_T15_T16'] if h[4].startswith(('T1 ','T2','T3','T4','T5','T6','T11','T13'))]
