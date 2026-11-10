# order34: RG31.1-3. PREREG hashed first.
import sys, math, json, numpy as np
sys.dont_write_bytecode=True
from pieces import *
from symbols import S_rows
N=105; n=np.linalg.norm; k=1/math.sqrt(35); out={}; B='/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/'
d=np.load(B+'order18/data/a2_arrays.npz'); CO,SCO=d['CO'],d['SCO']
Z=np.load(B+'order27/data/o27_arrays.npz'); GCO,SGCO=Z['g^1h^0'],Z['Sg^1h^0']
C30=np.load(B+'order30/data/o30_cones.npz'); C32=np.load(B+'order32/data/o32_new_cones.npz'); P33=np.load(B+'order33/data/o33_pieces.npz')
R19=np.load(B+'order19/data/rg5_arrays.npz'); C19,SC19=R19['C'],R19['SC']
M=np.zeros((N,N),complex)
for j,dd in enumerate(S_rows()):
    for kk,es in dd.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
xs=np.array([float(x) for x in XS])
vtx=np.array([1.0 if (Fr(al[0]).denominator==1 and Fr(al[1]).denominator==1) else 0.0 for al,be in pairs]); V1=np.tile(vtx,(216,1)).astype(complex)
stk=lambda Y,SY: np.concatenate([Y.ravel(),SY.ravel()])
Qw,_=np.linalg.qr(np.stack([stk(CO,SCO),stk(GCO,SGCO),stk(V1,V1)],1))
def dist(Y,SY): v=stk(Y,SY); return float(n(v-Qw@(Qw.conj().T@v))/max(n(v),1e-300))
def crit(Y,S):
    f={}
    for w in (-1,-0.5,0,0.5,1):
        X=(xs**-w)[:,None]*k*(Y@M.T); kap=np.vdot(X,S)/np.vdot(X,X); f[w]=(float(n(S-kap*X)/n(S)),complex(kap))
    ws=min(f,key=lambda w:f[w][0]); r,kap=f[-1]; dv=dist(Y,S)
    return dict(r=r,kappa=[kap.real,kap.imag],wstar=ws,nonvac_d=dv,crit=bool(dv>1e-3 and ws==-1 and abs(kap-1)<=0.01 and r<=0.10))
E=[((1,0),(0,1))]+[((1,0),(m,1)) for m in range(1,9)]
Cset=[tuple(tuple(int(t) for t in s.strip('()').split(',')) for s in kk.split('_')) for kk in C30.files if not kk.startswith('S') and not kk.startswith('(1, 0)')]+[((1,5),(0,1)),((1,6),(0,1))]
res={}; recon=0.0; save={}
for grp,lst in (('E',E),('C',Cset)):
    for u1,u2 in lst:
        key=f"{u1}_{u2}"
        if grp=='E': P,SP=P33[key],P33['S'+key]   # order: T_2b(e1), T_2a(other), T_BB
        else:
            P=np.zeros((3,216,105),complex); SP=P.copy()
            for ix,x in enumerate(XS):
                for j,(al,be) in enumerate(pairs):
                    P[:,ix,j]=corner_pieces(al,be,x,u1,u2); SP[:,ix,j]=corner_pieces(al,be,-1/x,u1,u2)
            save[key]=P; save['S'+key]=SP
        St=C30 if key in C30.files else C32
        recon=max(recon,float(np.abs(P.sum(0)-St[key]).max()),float(np.abs(SP.sum(0)-St['S'+key]).max()))
        res[key]=dict(group=grp,B2=crit(P[0]+P[1],SP[0]+SP[1]),BB=crit(P[2],SP[2]))
        print(grp,key,round(res[key]['B2']['r'],4),res[key]['B2']['crit'],round(res[key]['BB']['r'],4),res[key]['BB']['crit'],flush=True)
np.savez('../data/o34_control_pieces.npz',**save)
out['recon']=recon; out['cones']=res
nb=len(res); bad1=sum(1 for v in res.values() if not (v['B2']['crit'] and v['B2']['r']<=0.01)); bad2=sum(1 for v in res.values() if v['BB']['crit'])
out['RG31_1']=dict(n=nb,bad=bad1,max_r=max(v['B2']['r'] for v in res.values()),max_r_controls=max(v['B2']['r'] for v in res.values() if v['group']=='C'),verdict='PASS' if bad1==0 else ('FAIL' if bad1>0.1*nb else 'inconclusive'))
out['RG31_2']=dict(n=nb,bad=bad2,min_r=min(v['BB']['r'] for v in res.values()),verdict='PASS' if bad2==0 else ('FAIL' if bad2>0.1*nb else 'inconclusive'))
K='(1, 0)_(0, 1)'; PK,SPK=P33[K],P33['S'+K]
def ident(A,SA,Bv,SBv): e=float(max(np.abs(A-Bv).max(),np.abs(SA-SBv).max())); return dict(err=e,verdict='PASS' if e<=1e-10 else ('FAIL' if e>=1e-6 else 'inconclusive'))
def ratio(A,Bv): return complex(np.vdot(Bv.ravel(),A.ravel())/np.vdot(Bv.ravel(),Bv.ravel()))
I={}
I['I-b']=ident(PK[0],SPK[0],1.75*C19[2],1.75*SC19[2]); I['I-a']=ident(PK[1],SPK[1],0.5*C19[1],0.5*SC19[1]); I['I-11']=ident(PK[2],SPK[2],C19[0],SC19[0])
for nm,A,Bv in (('I-b',PK[0],C19[2]),('I-a',PK[1],C19[1]),('I-11',PK[2],C19[0])): r_=ratio(A,Bv); I[nm]['ratio_diag']=[r_.real,r_.imag]
en=0.0
for m in range(1,9):
    key=f"(1, 0)_({m}, 1)"; c=(2*m+7)/4; en=max(en,float(np.abs(P33[key][0]-c*C19[2]).max()),float(np.abs(P33['S'+key][0]-c*SC19[2]).max()))
I['I-n']=dict(err=en,verdict='PASS' if en<=1e-10 else ('FAIL' if en>=1e-6 else 'inconclusive'))
I['consistency_r_C2b_vs_Te1']=abs(crit(C19[2],SC19[2])['r']-crit(PK[0],SPK[0])['r']); I['r_C2b']=crit(C19[2],SC19[2])['r']
out['RG31_3']=I
json.dump(out,open('../data/o34.json','w'),indent=1)
print(json.dumps({k_:v_ for k_,v_ in out.items() if k_!='cones'},indent=1))
