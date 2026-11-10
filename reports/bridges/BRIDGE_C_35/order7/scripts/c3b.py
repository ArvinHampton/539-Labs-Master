# candidate 3 (enlarged law space W_420) and candidate-2 coupling test, on T660
import sys, json, numpy as np; sys.dont_write_bytecode=True
d={k:np.load('../data/W_%s.npz'%k) for k in ('E','H','O','ThE')}
T=d['E']['T']; y=T.imag
Wmat=np.hstack([d[k]['V'] for k in ('E','H','O','ThE')])
def keep(B): n=np.linalg.norm(B,axis=0); return B[:,n>1e-10*n.max()]
def basis(B):
    B=keep(B)
    B=B/np.linalg.norm(B,axis=0); U,s,_=np.linalg.svd(B,full_matrices=False); r=int((s/s[0]>1e-12).sum()); return U[:,:r],r,s
def eps(U,Tg):
    Tg=keep(Tg); R=Tg-U@(U.conj().T@Tg); return float((np.linalg.norm(R,axis=0)/np.linalg.norm(Tg,axis=0)).max())
U,rW,s=basis(Wmat); res={'rows':len(T),'rank_W':rW,'sv_cut':[float(s[rW-1]/s[0]),float(s[rW]/s[0]) if rW<len(s) else 0.0]}
res['inconclusive_by_rank']=rW>=0.9*len(T)
full=lambda which: 0.5*d['E'][which]+0.5*d['O'][which]-d['H'][which]
X={'H':d['H']['W'],'E':d['E']['W'],'ThE':d['ThE']['W'],'full':full('W')}
v=lambda e:'pass' if e<=1e-10 else ('FAIL' if e>=1e-4 else 'inconclusive')
for name,Xm in X.items():
    for w in (0,1):
        e=eps(U,(T**(-w))[:,None]*Xm); res['eps_%s_w%d'%(name,w)]=e; res['v_%s_w%d'%(name,w)]=v(e)
res['positive_control']=res['v_H_w1']=='pass'
# coupling (candidate 2)
Phi=np.load('../data/Phi660.npz')['V']   # (660,2,105)
C=np.hstack([(y**-0.5)[:,None]*Phi[:,0],(y**-0.5)[:,None]*Phi[:,1],(y**0.5)[:,None]*Phi[:,0],(y**0.5)[:,None]*Phi[:,1]])
Uc,rc,sc=basis(C); res['coupling_rank']=rc
e=eps(Uc,d['E']['V']); res['coupling_eps']=e; res['coupling']=v(e)
print(json.dumps(res,indent=1)); json.dump(res,open('../data/c3b.json','w'),indent=1)
