# order27: exact certificates X1-X4, controls N1-N3, RG18. PREREG hashed first.
import sys, math, json, numpy as np
from collections import Counter
sys.dont_write_bytecode=True
from cornerlib import *
from symbols import S_rows
Sr=S_rows(); N=105; n=np.linalg.norm; out={}
def gam(gm):
    p=[None]*N; e=[None]*N
    for j,(al,be) in enumerate(pairs):
        ga=tuple(sum(Fr(int(gm[r][c]))*al[c] for c in range(2)) for r in range(2)); gb=tuple(sum(Fr(int(gm[r][c]))*be[c] for c in range(2)) for r in range(2))
        p[j],e[j]=reduce(ga,gb)
    return p,e
def mul(X,Y):  # monomial product X@Y in (perm,exp) form
    return [Y[0][X[0][j]] for j in range(N)],[(X[1][j]+Y[1][X[0][j]])%L for j in range(N)]
Id=(list(range(N)),[0]*N)
def eq(X,Y): return X[0]==Y[0] and all((a-b)%L==0 for a,b in zip(X[1],Y[1]))
mI=[[-1,0],[0,-1]]; sg=[[-1,-7],[0,1]]; h=[[1,7],[0,-1]]
Gm,Gs,Gh,Gg=gam(mI),gam(sg),gam(h),gam(g.tolist())
out['Gamma_sigma_is_I']=eq(Gs,Id); out['Gamma_minusI_is_I']=eq(Gm,Id)
out['X1']=eq(Gh,mul(Gs,Gm)) and eq(Gh,mul(Gm,Gs))
out['X2']=eq(mul(Gm,Gm),Id) and eq(mul(Gh,Gh),Id)
def commM(P):
    p,e=P; inv=[0]*N
    for j in range(N): inv[p[j]]=j
    bad=0
    for j in range(N):
        for k in range(N):
            if Counter((e[j]+x)%L for x in Sr[p[j]].get(k,[]))!=Counter((x+e[inv[k]])%L for x in Sr[j].get(inv[k],[])): bad+=1
    return bad
out['X3_mismatches']=commM(Gh); out['X3']=out['X3_mismatches']==0
out['X4_commute']=eq(mul(Gh,Gg),mul(Gg,Gh))
def mat(P):
    G=np.zeros((N,N),complex)
    for j in range(N): G[j,P[0][j]]=np.exp(2j*np.pi*P[1][j]/L)
    return G
Hm,GG=mat(Gh),mat(Gg)
M=np.zeros((N,N),complex)
for j,dd in enumerate(Sr):
    for kk,es in dd.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
d=np.load('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order18/data/a2_arrays.npz'); CO,SCO=d['CO'],d['SCO']
gn=np.array(g); gin=np.array(gi); hn=np.array(h)
words={}
for a in range(-2,3):
    ga=np.linalg.matrix_power(gn if a>=0 else gin,abs(a))
    for b in (0,1):
        w=ga@(hn if b else np.eye(2,dtype=int)); words[f"g^{a}h^{b}"]=w
words['-I']=-np.eye(2,dtype=int)
V={}; SV={}
for nm,w in words.items():
    u1=tuple(int(t) for t in w[:,0]); u2=tuple(int(t) for t in w[:,1])
    V[nm]=np.array([[corner(al,be,x,u1,u2) for (al,be) in pairs] for x in XS]); SV[nm]=np.array([[corner(al,be,-1/x,u1,u2) for (al,be) in pairs] for x in XS])
np.savez('../data/o27_arrays.npz',**V,**{'S'+k:v for k,v in SV.items()})
out['N1']=float(max(np.abs(V['g^0h^1']-CO).max(),np.abs(SV['g^0h^1']-SCO).max(),np.abs(V['-I']-CO).max(),np.abs(SV['-I']-SCO).max()))
out['N2']=float(max(np.abs(CO@Hm.T-CO).max(),np.abs(SCO@Hm.T-SCO).max()))
o26=np.load('../../order26/data/o26_arrays.npz'); out['N3']=float(np.abs(o26['B']-V['g^0h^1']).max())
stk=lambda Y,SY: np.concatenate([Y.ravel(),SY.ravel()])
W=np.stack([stk(CO,SCO),stk(CO@GG.T,SCO@GG.T)],1); Qw,_=np.linalg.qr(W)
rn={k:float(n(stk(V[k],SV[k])-Qw@(Qw.conj().T@stk(V[k],SV[k])))/n(stk(CO,SCO))) for k in V}
out['RG18']=dict(r_new_each=rn,r_new=max(rn.values()),verdict='VACUOUS' if max(rn.values())<=1e-10 else 'TEST_NEW_DIRECTIONS')
if out['X4_commute']:
    ranks={}
    for e1 in (1,-1):
        for e2 in (1,-1):
            P=0.25*(np.eye(N)+e1*GG)@(np.eye(N)+e2*Hm); ranks[f"{e1},{e2}"]=int(np.linalg.matrix_rank(P,1e-9))
    out['proj_ranks']=ranks
print(json.dumps(out,indent=1)); json.dump(out,open('../data/o27.json','w'),indent=1)
