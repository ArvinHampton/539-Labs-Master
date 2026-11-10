import sys, json, hashlib, math
sys.dont_write_bytecode=True
sys.path.insert(0,'/tmp/repo539/docs/S2-11DM2ET-X-Axiomatic-Book/scripts')
import architecture_A4plus_probe as A
def T3(n): return n//3 if n%3==0 else ((4*n+2)//3 if n%3==1 else (2*n+1)//3)
R={}
# D1
bad=[u for u in range(3,3*10**6,9) if T3(u)%3!=1]
pred=set(u%9 for u in range(3*10**6) if T3(u)%9==3)
proof=all(T3(r)%3==1 for r in (3,12,21))  # u=27t+r: T3(u)=9t+r/3, mod 3 = r/3 mod 3 = 1
R['D1']=dict(counterexamples=len(bad),pred_classes=sorted(pred),residue_proof=proof,verdict='PASS' if not bad and pred<= {0,4,5} and proof else 'FAIL')
# D2/D3/D5
n=0;h=0;cons=0;fib=[0]*8;small=0;minbits=10**9
for s in range(1000):
    u=int.from_bytes(hashlib.sha3_512(b'holdout-'+str(s).encode()).digest(),'big')
    prev=False
    for i in range(539):
        v=T3(u); n+=1; hit=(v%9==3)
        if hit:
            h+=1; fib[((v-21)//9)%8]+=1
            if prev: cons+=1
            if 21<=v<4880: small+=1
        prev=hit; u=v; minbits=min(minbits,u.bit_length())
p=1/9; sig=math.sqrt(p*(1-p)/n); hf=h/n
R['D2']=dict(n=n,hits=h,frac=hf,z=(hf-p)/sig,consecutive=cons,verdict='PASS' if abs(hf-p)<=4*sig and cons==0 else 'FAIL')
e=h/8; chi=sum((c-e)**2/e for c in fib)
R['D3']=dict(fibre_counts=fib,chi2=chi,verdict='PASS' if chi<=24.32 else 'FAIL')
R['D5']=dict(small_hits=small,min_bitlength_seen=minbits,verdict='PASS' if small==0 else 'FAIL')
# D4: F2 system on K+ 1-skeleton
N_flux,N_tow,Q,f_max,B,loads=A.atoms(); O=A.core_q0(N_flux,f_max,Q,B)
E,F=A.build_complex(O,loads,'A2_enrich')
tau=[A.tower_of(x,loads) for x in O]
# unknown bits b_j (g=(-1)^b); equations b_a+b_b = c(e)
rows=[]
for a,b in sorted(E):
    c=0 if tau[a]==tau[b] else ((tau[b]-tau[a])%2 if b==a+1 else None)
    if c is None: raise SystemExit('non-path cross-tower edge')
    rows.append((a,b,c))
# connectivity => solution unique up to global flip: BFS
adj=[[] for _ in O]
for a,b,c in rows: adj[a].append((b,c)); adj[b].append((a,c))
sol=[None]*len(O); sol[0]=tau[0]%2; st=[0]; ok=True
while st:
    x=st.pop()
    for y,c in adj[x]:
        v=sol[x]^c
        if sol[y] is None: sol[y]=v; st.append(y)
        elif sol[y]!=v: ok=False
conn=all(s is not None for s in sol)
R['D4']=dict(consistent=ok,connected=conn,matches_g=sol==[t%2 for t in tau],verdict='PASS' if ok and conn and sol==[t%2 for t in tau] else 'FAIL')
json.dump(R,open('data/tests.json','w'),indent=1); print(json.dumps(R))
