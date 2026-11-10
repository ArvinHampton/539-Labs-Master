import json
O=[21+9*j for j in range(539)]; Oset=set(O); R={}
def reps(f,B):
    s=set()
    for a in range(-B,B+1):
        for b in range(-B,B+1):
            v=abs(f(a,b))
            if v in Oset: s.add(v)
    return s
S=reps(lambda a,b:a*a-35*b*b,300)
cnt=[0]*8
for j,x in enumerate(O):
    if x in S: cnt[j%8]+=1
R['C12']={'size':len(S),'fibre_counts':cnt,'pass':len(S)>0 and max(cnt)-min(cnt)<=1}
def tau(x): return x//21 if x<420 else 20+(x-420)//20
pairs={j for j in range(538) if tau(O[j])==tau(O[j+1])}
gate=len(pairs)==353
img={538-(j+1) for j in pairs}
R['C13']={'pairs':len(pairs),'gate_353':gate,'preserved':img==pairs,'sym_diff':len(img^pairs),'verdict':('VOID' if not gate else ('PASS' if img==pairs else 'FAIL'))}
SQ=reps(lambda a,b:2*a*a+14*a*b+7*b*b,300)
R['C14']={'size_SQ':len(SQ),'size_S':len(S),'intersection':len(SQ&S),'pass':len(SQ)>0 and not (SQ&S)}
json.dump(R,open('data/b3.json','w'),indent=1); print(json.dumps(R))
