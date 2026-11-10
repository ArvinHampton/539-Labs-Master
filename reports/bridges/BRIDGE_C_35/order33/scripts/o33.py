# order33: RG29, RG30. PREREG hashed first.
import sys, math, json, numpy as np
sys.dont_write_bytecode=True
from pieces import *
from symbols import S_rows
N=105; n=np.linalg.norm; k=1/math.sqrt(35); out={}; B='/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/'
d=np.load(B+'order18/data/a2_arrays.npz'); CO,SCO=d['CO'],d['SCO']
Z=np.load(B+'order27/data/o27_arrays.npz'); GCO,SGCO=Z['g^1h^0'],Z['Sg^1h^0']
C30=np.load(B+'order30/data/o30_cones.npz'); C32=np.load(B+'order32/data/o32_new_cones.npz')
M=np.zeros((N,N),complex)
for j,dd in enumerate(S_rows()):
    for kk,es in dd.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
xs=np.array([float(x) for x in XS])
vtx=np.array([1.0 if (Fr(al[0]).denominator==1 and Fr(al[1]).denominator==1) else 0.0 for al,be in pairs]); V1=np.tile(vtx,(216,1)).astype(complex)
stk=lambda Y,SY: np.concatenate([Y.ravel(),SY.ravel()])
Qw,_=np.linalg.qr(np.stack([stk(CO,SCO),stk(GCO,SGCO),stk(V1,V1)],1))
def dist(Y,SY): v=stk(Y,SY); return float(n(v-Qw@(Qw.conj().T@v))/max(n(v),1e-300))
def fam(Y,S):
    res={}
    for w in (-1,-0.5,0,0.5,1):
        X=(xs**-w)[:,None]*k*(Y@M.T); kap=np.vdot(X,S)/np.vdot(X,X); res[w]=(float(n(S-kap*X)/n(S)),complex(kap))
    return res
R=lambda Y,SY: SY-xs[:,None]*k*(Y@M.T)
cones=[((1,0),(0,1))]+[((1,0),(m,1)) for m in range(1,9)]
res={}; recon=0.0; stored=0.0; Dv=[]; save={}
for u1,u2 in cones:
    P=np.zeros((3,216,105),complex); SP=P.copy()
    for ix,x in enumerate(XS):
        for j,(al,be) in enumerate(pairs):
            P[:,ix,j]=corner_pieces(al,be,x,u1,u2); SP[:,ix,j]=corner_pieces(al,be,-1/x,u1,u2)
    key=f"{u1}_{u2}"; save[key]=P; save['S'+key]=SP
    St=(C30 if key in C30.files else C32); Cr,SCr=St[key],St['S'+key]
    recon=max(recon,float(np.abs(P.sum(0)-Cr).max()),float(np.abs(SP.sum(0)-SCr).max()))
    Cor,SCor=P.sum(0),SP.sum(0); nc=float(n(Cor))
    row={}
    objs={'T_e1':(P[0],SP[0]),'T_other':(P[1],SP[1]),'T_BB':(P[2],SP[2]),'T_e1+T_other':(P[0]+P[1],SP[0]+SP[1]),'T_e1+T_BB':(P[0]+P[2],SP[0]+SP[2]),'Cor':(Cor,SCor)}
    for nm,(Y,S) in objs.items():
        f=fam(Y,S); ws=min(f,key=lambda w:f[w][0]); r,kap=f[-1]; dv=dist(Y,S); small=float(n(Y))<1e-6*nc
        row[nm]=dict(r=r,kappa=[kap.real,kap.imag],wstar=ws,nonvac_d=dv,norm=float(n(Y)),vacuous=bool(dv<=1e-3 or small),crit=bool((not (dv<=1e-3 or small)) and ws==-1 and abs(kap-1)<=0.01 and r<=0.10))
    RD=R(P[1]+P[2],SP[1]+SP[2]); RC=R(Cor,SCor)
    row['RG30']=dict(share=float(n(RD)**2/n(RC)**2),cos=float(np.real(np.vdot(RD.ravel(),RC.ravel()))/(n(RD)*n(RC))),R_e1=float(n(R(P[0],SP[0]))),R_cor=float(n(RC)))
    Dv.append(RD.ravel()/n(RD)); res[key]=row
    print(key,{nm:(round(v['r'],4),round(v['kappa'][0],4),v['wstar'],v['crit']) for nm,v in row.items() if nm!='RG30'},row['RG30'],flush=True)
np.savez('../data/o33_pieces.npz',**save)
out['recon_and_stored']=recon; out['cones']=res
p={nm:sum(res[c][nm]['crit'] for c in res) for nm in ('T_e1','T_other','T_BB','T_e1+T_other','T_e1+T_BB','Cor')}
v='PASS' if (p['T_e1']==9 and p['T_other']<=1 and p['T_BB']<=1) else ('FAIL' if p['T_e1']<=6 else 'inconclusive')
out['RG29']=dict(pass_counts=p,verdict=v)
sh=[res[c]['RG30']['share'] for c in res]; cs=[res[c]['RG30']['cos'] for c in res]
Dv=np.array(Dv); Cm=np.abs(Dv.conj()@Dv.T); iu=np.triu_indices(len(Dv),1)
out['RG30']=dict(median_share=float(np.median(sh)),median_cos=float(np.median(cs)),accounts_for_most=bool(np.median(sh)>=0.5 and np.median(cs)>=0.7),scatter_min=float(Cm[iu].min()),scatter_mean=float(Cm[iu].mean()),scattered=bool(Cm[iu].mean()<=0.5))
json.dump(out,open('../data/o33.json','w'),indent=1)
print(json.dumps({k_:v_ for k_,v_ in out.items() if k_!='cones'},indent=1))
