import csv,math,random,sympy,numpy as np
from scipy import stats
R=[r for r in csv.DictReader(open('partA_table.csv'))]
for r in R:
  for k in r:
    try: r[k]=float(r[k]) if '.' in r[k] or 'e' in r[k] else int(r[k])
    except: pass
for r in R:
  if r['s']==98: r['dimV']=2406; r['dcusp']=2406-r['dEis_formula']; r['dimV_status']='manuscript Thm s98'
out=[];P=lambda x:(out.append(x),print(x))
# 1. eps_s non-fundamental
nf=[r for r in R if r['k_power']>1]
P(f"[A1] eps_s non-fundamental (k>1) for {len(nf)}/496 s: "+", ".join(f"s={r['s']}(k={r['k_power']},N={r['N_epsK']})" for r in nf))
def cheb_ok(r):
  s,k=r['s'],r['k_power']; eta=((s-1)+math.sqrt(r['n_s']))**(1/k)
  t=eta+ (1/eta if r['N_epsK']==1 or k%2==0 and False else 0)
  tr=eta+1/eta if (r['N_epsK']==1) else eta-1/eta  # for norm -1 root: eta - 1/eta = trace
  return round(tr,6)
sq=[r['s'] for r in nf if r['k_power']==2 and r['N_epsK']==1]
P(f"[A1] k=2 with N(eta)=+1 at s={sq}; s=2m^2 in range: {[2*m*m for m in range(2,16) if 2*m*m<=500]}")
P("[A1] traces of eta=eps_s^(1/k): "+", ".join(f"s={r['s']}:tr={cheb_ok(r)}" for r in nf))
# 2. cusp dims
tab=[r for r in R if r['s']<=51 or r['s']==72]
P(f"[A2] proved/tabulated (s<=51,72): d_cusp=0 only at s={[r['s'] for r in tab if r['dcusp']==0]}")
ext=[r for r in R if r['dcusp']<=0]
P(f"[A2] formula extrapolation s<=500 (Cat B): d_cusp<=0 at s={[r['s'] for r in ext]}")
odd=[r for r in R if r['s']%2]; ev=[r for r in R if r['s']%2==0]
for nm,g in [('odd',odd),('even',ev)]:
  x=np.log([r['s'] for r in g]); y=np.log([max(r['dcusp'],1)/r['dimV'] for r in g])
  sl,ic,rr,_,_=stats.linregress(x,y)
  P(f"[A2] {nm} s: log(dcusp/dimV) ~ {sl:.3f} log s + {ic:.3f}, r={rr:.3f}; median ratio s>200: {np.median([r['dcusp']/r['dimV'] for r in g if r['s']>200]):.3f}")
P(f"[A2] odd s: dEis/dimV = 3*prod((p^e+1)/2)/(s(s-1)); for n_s squarefree with odd primes p|n_s this is 3*prod(p+1)/2^w / (s(s-1)) (closed form, Cat A given manuscript Thm dims (iii) and dimV=s(s-1))")
for m in (2,3,4,6):
  res={a:int(np.mean([r['dcusp']%2 for r in R if r['s']%m==a])*100) for a in range(m)}
  P(f"[A2] % of s with odd d_cusp by s mod {m}: {res}")
# 3. Cohen-Lenstra (odd part of h_K) over distinct fields
seen={};
for r in R: seen.setdefault(r['d_K'],r['h_K'])
hs=list(seen.values()); oddpart=[h//(2**(len(bin(h))-len(bin(h).rstrip('0')))) for h in hs]
frac=np.mean([o==1 for o in oddpart]); n=len(hs)
P(f"[A3] distinct fields K_s: {n}; fraction with odd part of h = 1: {frac:.3f} (Cohen-Lenstra real quadratic heuristic ~0.754; binomial 95% CI half-width {1.96*math.sqrt(0.754*0.246/n):.3f}); Gauss genus: 2-rank of h+ = omega(d_K)-1 (Cat A theorem)")
gen=np.mean([ (r['hplus_K'] % 2**(len(sympy.primefactors(abs(r['d_K'])))-1)==0) for r in R])
P(f"[A3] check genus theory 2^(omega-1) | h+: holds for {gen*100:.1f}% of s (must be 100%)")
# 4. twin primes
tw=[r for r in R if r['twin']]
P(f"[A4] twin subfamily ({len(tw)} s): h+_K values {[r['hplus_K'] for r in tw]}; all have k=1: {all(r['k_power']==1 for r in tw)}; omega(d_K)=3 (2, s-2, s) so 4 | h+ (genus) : {all(r['hplus_K']%4==0 for r in tw)}")
# 5. correlations (Spearman, permutation, BH), raw and after removing log s trend
vars_={'log s':[math.log(r['s']) for r in R],'log h+_K':[math.log(r['hplus_K']) for r in R],'log ray':[math.log(r['ray_no']) for r in R],
 'log reg_K':[math.log(r['regulator_K']) for r in R],'k':[r['k_power'] for r in R],'cusp/dimV':[r['dcusp']/r['dimV'] for r in R],'f (conductor)':[r['f'] for r in R]}
names=list(vars_); X=np.array([vars_[k] for k in names])
ls=X[0]
def resid(v): b=np.polyfit(ls,v,1); return v-np.polyval(b,ls)
rng=np.random.default_rng(0); res=[]
for i in range(len(names)):
  for j in range(i+1,len(names)):
    for mode in ('raw','detrended'):
      if mode=='detrended' and (i==0): continue
      a,b=(X[i],X[j]) if mode=='raw' else (resid(X[i]),resid(X[j]))
      rho=stats.spearmanr(a,b).correlation
      perm=np.array([stats.spearmanr(a,rng.permutation(b)).correlation for _ in range(2000)])
      p=(np.sum(np.abs(perm)>=abs(rho))+1)/2001; res.append([names[i],names[j],mode,rho,p])
ps=np.array([r[4] for r in res]); m=len(ps); order=np.argsort(ps); bh=np.empty(m)
for rank,idx in enumerate(order,1): bh[idx]=ps[idx]*m/rank
bh=np.minimum.accumulate(bh[order][::-1])[::-1]; bhf=np.empty(m); bhf[order]=np.minimum(bh,1)
with open('partA_correlations.csv','w',newline='') as fh:
  w=csv.writer(fh); w.writerow(['x','y','mode','spearman','perm_p','bonferroni_p','BH_q'])
  for r,q in zip(res,bhf): w.writerow(r+[min(1,r[4]*m),q])
sig=[(r[0],r[1],r[2],round(r[3],3)) for r,q in zip(res,bhf) if q<0.05]
P(f"[A5] {m} tests; BH q<0.05: {sig}")
open('partA_analysis.out','w').write("\n".join(out))
