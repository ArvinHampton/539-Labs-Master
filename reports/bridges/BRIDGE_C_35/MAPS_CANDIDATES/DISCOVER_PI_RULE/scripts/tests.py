import json, itertools
def segs(w):
    return [len(list(g)) for _,g in itertools.groupby(w)]
C1=[0]*539; MX=([0,1]*270)[:539]
r={'T1_segments':len(segs(C1)),'T2_segments':len(segs(MX))}
r['T1']='FAIL' if r['T1_segments']!=4 else 'CHECK'; r['T2']='FAIL' if r['T2_segments']!=4 else 'CHECK'
N=539; cur={a:(0,1) for a in range(3)}
for i in range(1,N):
    nxt={}
    for b in range(3):
        c=[(h+(a==0 and b==1),k) for a,(h,k) in cur.items()]; m=max(h for h,_ in c); nxt[b]=(m,sum(k for h,k in c if h==m))
    cur=nxt
m=max(h for h,_ in cur.values()); r['T3c_max']=m; r['T3c_count']=sum(k for h,k in cur.values() if h==m)
r['T3c']='PASS' if r['T3c_count']>1 else 'FAIL'
r['Pi_max_sha256']=__import__('hashlib').sha256(bytes(MX)).hexdigest()
json.dump(r,open('data/tests.json','w'),indent=1); print(r)
