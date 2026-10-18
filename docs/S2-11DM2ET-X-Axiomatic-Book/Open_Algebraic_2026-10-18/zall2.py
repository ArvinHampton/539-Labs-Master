import sys, json, sympy
from sympy.ntheory.modular import crt
from item1_lead import data
out=[]
for s in map(int,sys.argv[1].split(',')):
    orb,counts,modes,mod,D,Mx,no=data(s,2)
    M=2*D; odd=M
    while odd%2==0: odd//=2
    u=int(crt([odd,M//odd],[odd-1,1])[0])
    els=list(orb)
    fixed=all(orb[(u*x[0]%mod[0],u*x[1]%mod[1])]==orb[x] for x in els)
    G=[[-1,-s],[2,2*s-1]]
    def ap(P,x): return ((P[0][0]*x[0]+P[0][1]*x[1])%mod[0],(P[1][0]*x[0]+P[1][1]*x[1])%mod[1])
    P=[[1,0],[0,1]]; uni=[]
    for k in range(4*s):
        for sg in (1,-1):
            if all(ap([[sg*P[0][0],sg*P[0][1]],[sg*P[1][0],sg*P[1][1]]],x)==(u*x[0]%mod[0],u*x[1]%mod[1]) for x in els): uni.append((sg,k))
        P=[[sum(P[i][t]*G[t][j] for t in range(2)) for j in range(2)] for i in range(2)]
        if uni: break
    # structure of els: x2 parity etc
    par=sorted({(x[0]%2,x[1]%4) for x in els})
    r=dict(s=s,Zall_fixes_every_orbit=fixed,uniform_element=uni,els_2adic_residues=par); print(r,flush=True); out.append(r)
json.dump(out,open("zall2.json","w"),default=str)
