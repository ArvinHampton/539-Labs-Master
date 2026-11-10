# order32: RG27, RG27G, RG28. PREREG hashed first.
import sys, math, json, numpy as np
sys.dont_write_bytecode=True
from cornerlib import *
from symbols import S_rows
N=105; n=np.linalg.norm; k=1/math.sqrt(35); out={}; B='/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/'
d=np.load(B+'order18/data/a2_arrays.npz'); CO,SCO=d['CO'],d['SCO']
Z=np.load(B+'order27/data/o27_arrays.npz'); GCO,SGCO=Z['g^1h^0'],Z['Sg^1h^0']
C30=np.load(B+'order30/data/o30_cones.npz')
M=np.zeros((N,N),complex)
for j,dd in enumerate(S_rows()):
    for kk,es in dd.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
xs=np.array([float(x) for x in XS])
vtx=np.array([1.0 if (Fr(al[0]).denominator==1 and Fr(al[1]).denominator==1) else 0.0 for al,be in pairs]); V1=np.tile(vtx,(216,1)).astype(complex)
stk=lambda Y,SY: np.concatenate([Y.ravel(),SY.ravel()])
Qw,_=np.linalg.qr(np.stack([stk(CO,SCO),stk(GCO,SGCO),stk(V1,V1)],1))
def dist(Y,SY): v=stk(Y,SY); return float(n(v-Qw@(Qw.conj().T@v))/n(v))
def fam(Y,S):
    res={}
    for w in (-1,-0.5,0,0.5,1):
        X=(xs**-w)[:,None]*k*(Y@M.T); kap=np.vdot(X,S)/np.vdot(X,X); res[w]=(float(n(S-kap*X)/n(S)),complex(kap))
    return res
Am=np.array([[2,7],[7,7]])
def get(u1,u2):
    key=f"{u1}_{u2}"
    if key in C30.files: return C30[key],C30['S'+key],'order31'
    assert abs(round(np.linalg.det(np.array([u1,u2]))))==1
    for u in (u1,u2): assert 0.5*np.array(u)@Am@np.array(u)>0
    assert np.array(u1)@Am@np.array(u2)>0
    return (np.array([[corner(al,be,x,u1,u2) for (al,be) in pairs] for x in XS]),np.array([[corner(al,be,-1/x,u1,u2) for (al,be) in pairs] for x in XS]),'new')
E=[((1,0),(m,1)) for m in range(1,9)]+[((1,0),(8,-1)),((1,0),(9,-1))]
Cset=[tuple(map(lambda s: tuple(int(t) for t in s.strip('()').split(',')),kk.split('_'))) for kk in C30.files if not kk.startswith('S') and not kk.startswith('(1, 0)')]
Cset+=[((1,5),(0,1)),((1,6),(0,1))]
G=[((13,-2),(72,-11)),((13,-2),(85,-13))]
res={}; arrays={}
for grp,lst in (('E',E),('C',Cset),('G',G)):
    for u1,u2 in lst:
        Y,S,src=get(u1,u2); arrays[f"{u1}_{u2}"]=(Y,S); f=fam(Y,S); ws=min(f,key=lambda w:f[w][0]); r,kap=f[-1]
        res[f"{u1}_{u2}"]=dict(group=grp,src=src,r=r,kappa=[kap.real,kap.imag],wstar=ws,nonvac_d=dist(Y,S),crit=bool(ws==-1 and abs(kap-1)<=0.01 and r<=0.10))
np.savez('../data/o32_new_cones.npz',**{k_:v[0] for k_,v in arrays.items() if res[k_]['src']=='new'},**{'S'+k_:v[1] for k_,v in arrays.items() if res[k_]['src']=='new'})
out['cones']=res
def tally(grp,want,src=None):
    L_=[v for v in res.values() if v['group']==grp and v['nonvac_d']>1e-3 and (src is None or v['src']==src)]
    bad=sum(1 for v in L_ if v['crit']!=want); return dict(n=len(L_),bad=bad)
tE,tC=tally('E',True),tally('C',False)
v='PASS' if tE['bad']==0 and tC['bad']==0 else ('FAIL' if (tE['bad']>0.1*tE['n'] or tC['bad']>0.1*tC['n']) else 'inconclusive')
out['RG27']=dict(E=tE,C=tC,blind_E=tally('E',True,'new'),blind_C=tally('C',False,'new'),verdict=v)
pre={'((13, -2), (72, -11))':'(1, 0)_(5, 1)','((13, -2), (85, -13))':'(1, 0)_(6, 1)'}
gd={}
for gk,ek in (('(13, -2)_(72, -11)','(1, 0)_(5, 1)'),('(13, -2)_(85, -13)','(1, 0)_(6, 1)')):
    gd[gk]=dict(crit=res[gk]['crit'],dr=abs(res[gk]['r']-res[ek]['r']),dk=abs(complex(*res[gk]['kappa'])-complex(*res[ek]['kappa'])))
out['RG27G']=dict(pairs=gd,verdict='PASS' if all(t['crit'] and t['dr']<=1e-12 and t['dk']<=1e-12 for t in gd.values()) else 'FAIL')
U=[]
for k_,v_ in res.items():
    if v_['group']=='E' and v_['crit']:
        Y,S=arrays[k_]; Rv=(S-xs[:,None]*k*(Y@M.T)).ravel(); U.append(Rv/n(Rv))
U=np.array(U); Cm=np.abs(U.conj()@U.T); iu=np.triu_indices(len(U),1); sv=np.linalg.svd(U,compute_uv=False)
mn,mean=float(Cm[iu].min()),float(Cm[iu].mean())
out['RG28']=dict(n=len(U),min_cos=mn,mean_cos=mean,top_sv_share=float(sv[0]**2/(sv**2).sum()),verdict='PASS' if mn>=0.99 else ('FAIL' if mean<=0.5 else 'intermediate'))
json.dump(out,open('../data/o32.json','w'),indent=1)
print(json.dumps({k_:v_ for k_,v_ in out.items() if k_!='cones'},indent=1))
for k_,v_ in res.items(): print(v_['group'],v_['src'],k_,round(v_['r'],4),[round(t,4) for t in v_['kappa']],v_['wstar'],round(v_['nonvac_d'],3),v_['crit'])
