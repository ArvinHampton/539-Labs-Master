import warnings; warnings.filterwarnings('ignore')
# Implements PREREG.md exactly (sha256 in prereg.sha256). T15 sigma recomputed from cited inputs (see REPORT note).
import csv,math,numpy as np,cypari2,random,json
R=list(csv.DictReader(open('partA_table.csv')))
tabS=set(list(range(5,52))+[72])
Q={'Q1':np.array([float(r['two_log_eps_s']) for r in R]),'Q2':np.array([float(r['I_s']) for r in R]),
   'Q3':np.array([int(r['hplus_D'])/int(r['h_D']) for r in R]),
   'Q4':np.array([int(r['dcusp'])/int(r['dimV']) for r in R if int(r['s']) in tabS]),
   'Q5':np.array([math.sqrt(int(r['n_s'])) for r in R])}
sigT15=math.hypot(14.5,62)/116592033*1e8
T=[('T1 alpha^-1',137.035999177,2.1e-8),('T2 mmu/me',206.7682827,4.6e-6),('T3 mp/me',1836.152673426,3.2e-8),('T4 mtau/me',3477.23,0.23),
('T5 mtau/mmu',3477.23/206.7682827,0.23/206.7682827),('T6 sin2thW',0.23129,4e-5),('T7 alpha_s',0.1180,9e-4),('T8 J*1e5',3.08,0.15),
('T9 Ob h2',0.02237,1.5e-4),('T10 Oc h2',0.1200,1.2e-3),('T11 n_s',0.9649,4.2e-3),('T12 ln1e10As',3.044,0.014),
('T13 H0 ratio',73.04/67.36,(73.04/67.36)*math.hypot(1.04/73.04,0.54/67.36)),('T14 S8',0.832,0.013),
('T15 g-2 dev*1e8',(116592071.5-116592033)/116592033*1e8,sigT15),('T16 mW CDF/PDG',80.4335/80.3692,(80.4335/80.3692)*math.hypot(9.4/80433.5,13.3/80369.2))]
ops=[('x',lambda x:x),('1/x',lambda x:1/x),('2x',lambda x:2*x),('3x',lambda x:3*x),('x/2',lambda x:x/2),('x/3',lambda x:x/3)]
tol=np.array([max(s,1e-3*abs(y)) for _,y,s in T]); yv=np.array([y for _,y,_ in T])
def count(Qd,detail=False):
  M=0; per=np.zeros(len(T),int); hits=[]
  for qn,v in Qd.items():
    for on,f in ops:
      fv=f(v)
      D=np.abs(fv[:,None]-yv[None,:])<=tol[None,:]
      M+=D.sum(); per+=D.sum(0)
      if detail:
        for i,j in zip(*np.nonzero(D)): hits.append((qn,on,i,j,float(fv[i]),T[j][0],T[j][1],T[j][2]))
  return M,per,hits
Mobs,perobs,hits=count(Q,True)
Ntr=sum(len(v) for v in Q.values())*len(ops)*len(T)
rng=np.random.default_rng(539)
def logu(v,n):
  pos=v[v>0]; lo,hi=pos.min(),pos.max(); out=np.exp(rng.uniform(math.log(lo),math.log(hi),n))
  out[:np.sum(v<=0)]=0  # keep the same number of exact zeros
  return out
# N2 pool: random squarefree d in n-range, regulators via PARI
pari=cypari2.Pari(); pari.allocatemem(2*10**9)
nmin,nmax=int(R[0]['n_s']),int(R[-1]['n_s'])
pool=[]; rr=random.Random(12345)
while len(pool)<5000:
  d=rr.randint(nmin,nmax)
  if pari.issquarefree(d) and d>1:
    reg=float(pari.quadregulator(int(pari.quaddisc(d)))); pool.append((d,reg))
pool=np.array(pool)
nt=10000; null={'N1':[],'N2':[],'N3':[]}; perN1=np.zeros(len(T))
for t in range(nt):
  q1={k:logu(v,len(v)) if k!='Q3' else v for k,v in Q.items()}
  m,p,_=count(q1); null['N1'].append(m); perN1+=p
  idx=rng.integers(0,len(pool),496); d=pool[idx,0]; rg=pool[idx,1]
  q2=dict(Q); q2['Q1']=2*rg; q2['Q2']=rg/(2*np.sqrt(d)); q2['Q5']=np.sqrt(d)
  null['N2'].append(count(q2)[0])
  q3=dict(Q); q3['Q5']=np.sqrt(rng.integers(nmin,nmax+1,496)); q3['Q1']=logu(Q['Q1'],496); q3['Q2']=logu(Q['Q2'],496)
  null['N3'].append(count(q3)[0])
res={'N_trials':Ntr,'M_obs':int(Mobs),'per_target_obs':dict(zip([t[0] for t in T],perobs.tolist())),
 'per_target_null_N1_mean':dict(zip([t[0] for t in T],(perN1/nt).round(3).tolist()))}
for k,v in null.items():
  v=np.array(v); res[k]={'mean':float(v.mean()),'sd':float(v.std()),'p_global':float((np.sum(v>=Mobs)+1)/(nt+1))}
json.dump(res,open('partB_results.json','w'),indent=1)
with open('partB_matches.csv','w',newline='') as fh:
  w=csv.writer(fh); w.writerow(['quantity','op','s_index_or_row','value','target','target_value','sigma','s'])
  for qn,on,i,j,fv,tn,ty,ts in hits:
    s = (sorted(tabS)[i] if qn=='Q4' else int(R[i]['s'])); w.writerow([qn,on,i,fv,tn,ty,ts,s])
print(json.dumps(res,indent=1)); print(len(hits),'hits')
for h in hits[:60]: print(h)
