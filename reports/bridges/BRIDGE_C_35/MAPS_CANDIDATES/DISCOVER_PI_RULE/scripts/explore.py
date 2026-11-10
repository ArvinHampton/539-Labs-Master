# Pre-PREREG exploration (Category A checks, exhaustive at small depth)
import itertools, json
def T3(u):
    q,r=divmod(u,3); return [q,4*q+2,2*q+1][r]
def word(x,n):
    w=[]
    for _ in range(n): w.append(x%3); x=T3(x)
    return tuple(w)
out={}
# E1: seed mod 3^n -> word bijection (residue-word bijection), n<=8
for n in range(1,9):
    ws={word(x,n) for x in range(3**n)}
    assert len(ws)==3**n
    # word depends only on x mod 3^n
    for x in range(3**n): assert word(x,n)==word(x+3**n*7,n)
out['E1_bijection_n_le_8']=True
# E2: P_res(u) <=> w_i=0 and w_{i+1}=1
for u in range(10**6): assert (u%9==3)==(u%3==0 and T3(u)%3==1)
out['E2_Pres_is_pattern_01']=True
# E3: max hits in 539-step word = number of disjoint '01' with hit i<=538 needing w_539 -> use 540 letters
# hits at i in 0..538 need w_i=0,w_{i+1}=1 (w_539 is next value's branch). Max = 270? pattern 0101..: hits at even i<=538 -> 270
# count maximisers by DP over 540 letters
from functools import lru_cache
import sys; sys.setrecursionlimit(10000)
N=540
best=[{} for _ in range(N+1)]
# state: last letter; value: (maxhits, count)
cur={a:(0,1) for a in range(3)}
for i in range(1,N):
    nxt={}
    for b in range(3):
        cands=[(h+(1 if (a==0 and b==1) else 0),c) for a,(h,c) in cur.items()]
        m=max(h for h,_ in cands); nxt[b]=(m,sum(c for h,c in cands if h==m))
    cur=nxt
m=max(h for h,_ in cur.values()); cnt=sum(c for h,c in cur.values() if h==m)
out['E3_max_hits']=m; out['E3_num_maximising_words_540letters']=cnt
# E4: O_res sorted (539 elems 21+9j) branch word
Ores=[21+9*j for j in range(539)]
w=[u%3 for u in Ores]; out['E4_C1_literal_word_set']=sorted(set(w))
out['E4_T3_image_in_Ores_count']=sum(1 for u in Ores if T3(u) in set(Ores))
out['E4_consecutive_T3_links']=sum(1 for a,b in zip(Ores,Ores[1:]) if T3(a)==b)
# E5: number of distinct P_res-compatible words with >=1 hit (log3 of total) — family size
out['E5_total_words_log3']=539
json.dump(out,open('data/explore.json','w'),indent=1); print(out)
