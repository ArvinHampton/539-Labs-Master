import json, numpy as np
from collections import Counter
R={}
CO=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order18/data/a2_arrays.npz')['CO']
mx=np.abs(CO).max(axis=0); k=int((mx>1e-10).sum()); gap=bool(((mx>=1e-13)&(mx<=1e-7)).any())
R['C15']={'k':k,'col_max_min_nonzero':float(mx[mx>1e-10].min()) if k else None,'col_max_max_zero':float(mx[mx<=1e-10].max()) if k<105 else None,'gap_hit':gap,'verdict':'VOID' if gap else ('PASS' if k%8==0 else 'FAIL')}
O=[21+9*j for j in range(539)]
tau=lambda x: x//21 if x<420 else 20+(x-420)//20
f=[tau(x) for x in O]; df=[f[i+1]-f[i] for i in range(538)]
cls=[0]*8
for i,d in enumerate(df):
    if d: cls[i%8]+=1
g16=sum(df)==241
R['C16']={'sum_df':sum(df),'class_counts':cls,'verdict':'VOID' if not g16 else ('PASS' if max(cls)-min(cls)<=1 else 'FAIL')}
c=Counter(f); seq=[c[t] for t in sorted(c)]
g17=sum(v*(v-1)//2 for v in seq)==353 and len(seq)==242
R['C17']={'n_towers':len(seq),'pairs':sum(v*(v-1)//2 for v in seq),'seq_head':seq[:25],'seq_tail':seq[-25:],'verdict':'VOID' if not g17 else ('PASS' if seq==seq[::-1] else 'FAIL')}
v=[sum(df[i] for i in range(538) if i%8==r)*(-1) for r in range(8)]  # alpha(0,8)=sgn(0-8)=-1
R['C18']={'v':v,'verdict':'PASS' if all(v[r]==v[(1-r)%8] for r in range(8)) else 'FAIL'}
json.dump(R,open('data/b4.json','w'),indent=1); print(json.dumps(R))
