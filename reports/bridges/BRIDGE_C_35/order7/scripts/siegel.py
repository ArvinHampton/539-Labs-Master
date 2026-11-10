# candidate 2: Phi_k on T120 (law) and on T660 at tau (coupling); arg: part law|coup
import sys, json, math, numpy as np; sys.dont_write_bytecode=True
from lib7 import *
nodes,mut=arc_nodes(24)
def Phi(tau):
    out=np.zeros((2,105),complex)
    for z,wq,mu in nodes:
        v=np.array([series(al,be,tau,'siegel',30,z) for al,be in pairs])
        out[0]+=wq*v; out[1]+=wq*np.exp(2j*np.pi*mu/mut)*v
    return out
part=sys.argv[1]
if part=='law':
    T=taus(120,5); V=np.array([Phi(t) for t in T]); W=np.array([Phi(-1/t) for t in T])
    res={'mu_total':mut}
    for k in (0,1):
        for eps in (1,-1):
            pred=np.array([eps*(M@V[i,k])/math.sqrt(35) for i in range(len(T))])
            res['r_k%d_eps%d'%(k,eps)]=float(np.abs(W[:,k]-pred).max()/max(1,np.abs(W[:,k]).max()))
        res['parity_k%d'%k]=float(np.abs(np.einsum('jk,tk->tj',P,V[:,k])-V[:,k]).max()/np.abs(V[:,k]).max())
    # trunc check
    z,wq,mu=nodes[5]; res['trunc30vs40']=float(abs(series(*pairs[3],T[0],'siegel',30,z)-series(*pairs[3],T[0],'siegel',40,z)))
    json.dump(res,open('../data/c2_law.json','w'),indent=1); print(json.dumps(res,indent=1))
else:
    T=taus(660,7); V=np.array([Phi(t) for t in T]); np.savez('../data/Phi660.npz',V=V); print('done')
