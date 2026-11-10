import sys, json
sys.dont_write_bytecode=True
sys.path.insert(0,'/tmp/repo539/docs/S2-11DM2ET-X-Axiomatic-Book/scripts')
from collections import defaultdict
from itertools import combinations
from sympy import Matrix
import residual_p_plus_multiscale_probe as P
N_flux,Q,f_max,B_prime,L_pref,loads=P.atoms()
residual=list(range(f_max,N_flux)); O=[residual[i] for i in range(len(residual)) if i%Q==0][:B_prime]
assert O==[21+9*j for j in range(539)]
bk=defaultdict(list)
for i,x in enumerate(O): bk[P.tower_of(x,loads)].append(i)
T=[t for v in bk.values() if len(v)>=3 for t in combinations(sorted(v),3)]
W=L_pref; inw=sum(1 for i,j,k in T if k<W); intw=sum(1 for i,j,k in T if i>=W-1)
gate=(len(T)==56 and inw==3 and intw==53)
def Arows(ts):
    rows=[]
    for i,j,k in ts:
        r=[0]*(B_prime-1)
        if j==i+1: r[i]=1
        if k==j+1: r[j]=1
        rows.append(r)
    return rows
def rk(rows): return Matrix(rows).rank() if rows else 0
n=[0]*8; byr=defaultdict(list)
for t in T: n[t[0]%8]+=1; byr[t[0]%8].append(t)
glob=len(T)-rk(Arows(T)); prox={r:len(byr[r])-rk(Arows(byr[r])) for r in range(8)}
cells=[c for t in T for c in t]; disjoint=len(cells)==len(set(cells)); consec=all(j==i+1 and k==j+1 for i,j,k in T)
E=sum(n[r] for r in (0,2,4,6)); Od=56-E
win=[t for t in T if t[2]<W]; ws=[t[0]%8 for t in win]
R=dict(gate=dict(n=len(T),in_window=inw,in_tower=intw,ok=gate),fibre_counts=n,E=E,Od=Od,global_proxy=glob,proxy_r=prox,disjoint=disjoint,all_consecutive=consec,window_triples=win,window_starts_mod8=ws)
if not gate: R.update(C21='VOID',C22='VOID',C23='VOID',C24='VOID')
else:
    R['C21']='PASS' if (Od<E and E-Od<=3) else 'FAIL'
    R['C22']='PASS' if n[2]==n[3]==n[5]==0 else 'FAIL'
    R['C23']=('PASS' if glob==0 and all(v==0 for v in prox.values()) else 'FAIL')+(' (vacuous)' if disjoint and consec else '')
    R['C24']='PASS' if len(set(ws))==3 else 'FAIL'
json.dump(R,open('data/b6.json','w'),indent=1,default=str); print(json.dumps(R,default=str))
