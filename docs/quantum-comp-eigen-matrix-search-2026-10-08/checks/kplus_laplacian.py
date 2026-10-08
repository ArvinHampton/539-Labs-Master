"""Reconstruct residual K+ (V=539,E=594,F=56) from facts quoted in the archive and
re-run the weighted Laplacian / heat-kernel numbers quoted in chat-02 (Pure Math Status).
Facts used (all quoted in raw/chat-02.txt 1299-1311 and raw/chat-05.txt 976-994):
 - 539 vertices on a residual path (538 path edges); same-tower fibers are consecutive blocks
 - fibers: 1 singleton, 185 doubletons, 56 tripletons; tripletons filled as triangles (F=56)
 - E = 594 = 538 path edges + 56 extra chords (chat-05 line 989 'if path edges 538 then extra 56')
 - gaps between consecutive P+ triples {5:6, 7:25, 9:24}; 3 triples in window W=18, 53 in tower
 - n_jump = 241 inter-fiber path edges
The ORDER of gaps and the position of the singleton are NOT given in the archive; we sample
random orders to show which quoted numbers are order-independent."""
import numpy as np, random, json, sys
V=539
def build(seed):
    rng=random.Random(seed)
    while True:
        gaps=[5]*6+[7]*25+[9]*24; rng.shuffle(gaps)
        starts=[0]
        for g in gaps: starts.append(starts[-1]+g)
        if sum(1 for s in starts if s+2<=17)==3: break
    blocks=[]  # list of (start,size)
    pos=0
    for i,s in enumerate(starts):
        while pos<s: blocks.append((pos,2)); pos+=2
        blocks.append((pos,3)); pos+=3
    tail=['D']*57+['S']; rng.shuffle(tail)
    for b in tail:
        sz=2 if b=='D' else 1; blocks.append((pos,sz)); pos+=sz
    assert pos==V
    sizes=sorted([b[1] for b in blocks]); 
    assert sizes.count(1)==1 and sizes.count(2)==185 and sizes.count(3)==56
    fiber=np.zeros(V,int)
    for (p,sz) in blocks: fiber[p:p+sz]=sz
    edges={}
    for i in range(V-1): edges[(i,i+1)]='path'
    for (p,sz) in blocks:
        if sz==3: edges[(p,p+2)]='chord'
    return blocks,fiber,edges
def lap(edges,wfun):
    L=np.zeros((V,V))
    for (i,j),kind in edges.items():
        w=wfun(i,j,kind); L[i,j]-=w; L[j,i]-=w; L[i,i]+=w; L[j,j]+=w
    return L
def stats(L):
    ev=np.linalg.eigvalsh(L); ev[np.abs(ev)<1e-10]=0
    ts=[0.001,0.01,0.05,0.1,0.2,0.5,1,2,5,10,20,50,100]
    return dict(gap=float(sorted(ev)[1]),max=float(ev.max()),mean=float(ev.mean()),
        mult0=int((ev==0).sum()),trL=float(np.trace(L)),trL2=float(np.trace(L@L)),
        N01=int((ev<=0.1).sum()),N1=int((ev<=1).sum()),N2=int((ev<=2).sum()),N5=int((ev<=5).sum()),
        heat={t:float(np.exp(-t*ev).sum()) for t in ts})
res=[]
for seed in range(int(sys.argv[1]) if len(sys.argv)>1 else 20):
    blocks,fiber,edges=build(seed)
    assert len(edges)==594
    njump=sum(1 for (i,j),k in edges.items() if k=='path' and not any(p<=i and j<p+sz for p,sz in blocks))
    unw=stats(lap(edges,lambda i,j,k:1.0))
    # tower-size: path edges 1, same-tower edges weight = fiber size (consistent with Tr(L)=2230)
    def tw(i,j,k):
        same=any(p<=i and j<p+sz for p,sz in blocks)
        return float(fiber[i]) if same else 1.0
    tow=stats(lap(edges,tw))
    # path-decay: |i-j|=1 path edges 1/(1+sqrt1)=0.5, non-path same-tower chords weight 2 (consistent with Tr(L)=762)
    pd=stats(lap(edges,lambda i,j,k: 1/(1+np.sqrt(abs(i-j))) if k=='path' else 2.0))
    res.append(dict(seed=seed,njump=njump,unw=unw,tow=tow,pd=pd))
# adjacency spectrum of the disjoint union of fiber cliques ('incidence spectrum' chat-05 l.991)
blocks,fiber,edges=build(0)
A=np.zeros((V,V))
for p,sz in blocks:
    for a in range(p,p+sz):
        for b in range(p,p+sz):
            if a!=b: A[a,b]=1
ev=np.round(np.linalg.eigvalsh(A),8); vals,cnt=np.unique(ev,return_counts=True)
out=dict(clique_adjacency_spectrum={str(v):int(c) for v,c in zip(vals,cnt)},samples=res)
json.dump(out,open('/workspace/quantum-comp/eigen-matrix-search/checks/kplus_results.json','w'),indent=1)
def rng_(key,sub):
    xs=[r[key][sub] for r in res]; return (min(xs),max(xs))
print('clique adjacency spectrum',out['clique_adjacency_spectrum'])
print('njump',set(r['njump'] for r in res))
for key in ['unw','tow','pd']:
    print(key,{s:rng_(key,s) for s in ['gap','max','mean','mult0','trL','trL2','N01','N1','N2','N5']})
    for t in [0.001,0.01,0.05,0.1,0.2,0.5,1,2,5,10,20,50,100]:
        xs=[r[key]['heat'][t] for r in res]; print('  t=%g heat %.3f..%.3f'%(t,min(xs),max(xs)))
