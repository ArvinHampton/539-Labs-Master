import json,hashlib,subprocess,numpy as np
h=open('PREREG.sha256').read().split()[0]; assert hashlib.sha256(open('PREREG.md','rb').read()).hexdigest()==h
subprocess.run(['python3','scripts/explore.py','400'],check=True,stdout=subprocess.DEVNULL)
d=json.load(open('data/explore_R400.json')); m=np.array(d['POOL_ABS_norm'])
r=np.array([1,8,3,0,7,8,5,0])/32
sm=[i for i in range(8) if m[i]>1e-6]; sr=[i for i in range(8) if r[i]>0]
ok=np.abs(m-r).max()<=1e-3 and sm==sr
out=dict(prereg_sha=h,R=400,rho_mod=m.round(9).tolist(),rho_res=r.tolist(),maxdiff=float(np.abs(m-r).max()),
 TV=float(np.abs(m-r).sum()/2),supp_mod=sm,supp_res=sr,verdict='PASS' if ok else 'FAIL')
print(json.dumps(out)); json.dump(out,open('data/test.json','w'),indent=1)
