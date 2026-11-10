# order40 RG37. PREREG hashed first. Stored arrays only.
import sys, math, json, numpy as np
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import XS, Fr
from symbols import S_rows, L
B='/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/'
Z=np.load(B+'order19/data/rg5_arrays.npz'); C,SC=Z['C'],Z['SC']; P=np.load(B+'order34/data/o34_control_pieces.npz')
M=np.zeros((105,105),complex)
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for ee in es: M[j,kk]+=np.exp(2j*np.pi*ee/L)
n=np.linalg.norm; xs=np.array([float(x) for x in XS]); k=1/math.sqrt(35)
def crit(Y,S):
    f={}
    for w in (-1,-0.5,0,0.5,1):
        X=(xs**-w)[:,None]*k*(Y@M.T); kap=np.vdot(X,S)/np.vdot(X,X); f[w]=(float(n(S-kap*X)/n(S)),complex(kap))
    ws=min(f,key=lambda w:f[w][0]); r,kap=f[-1]; return dict(r=r,kappa=[kap.real,kap.imag],wstar=ws,crit=bool(ws==-1 and abs(kap-1)<=0.01 and r<=0.10))
out={}; rC2a=crit(C[1],SC[1])['r']; rC2b=crit(C[2],SC[2])['r']; out['r_C2a']=rC2a; out['r_C2b']=rC2b
ie=0.0; rows={}
for m in range(1,7):
    key=f"(1, {m})_(0, 1)"; T,ST=P[key],P['S'+key]; c=(1+m)/2
    ie=max(ie,float(np.abs(T[1]-c*C[1]).max()),float(np.abs(ST[1]-c*SC[1]).max()))
    te=crit(T[1],ST[1]); b2=crit(T[0]+T[1],ST[0]+ST[1]); bb=crit(T[2],ST[2])
    rows[key]=dict(T_e2=te,B2=b2,BB=bb,dr_vs_C2a=abs(te['r']-rC2a)); print(key,round(te['r'],5),round(b2['r'],5),round(bb['r'],4),flush=True)
out['I_e2']=dict(err=ie,verdict='PASS' if ie<=1e-10 else ('FAIL' if ie>=1e-6 else 'inconclusive'))
out['cones']=rows
out['RG37a']='PASS' if all(v['dr_vs_C2a']<=1e-12 and v['T_e2']['crit'] for v in rows.values()) else 'FAIL'
okb=sum(1 for v in rows.values() if 0.5*rC2a<=v['B2']['r']<=2*rC2a); okbb=sum(1 for v in rows.values() if not v['BB']['crit'])
out['RG37b']=dict(B2_in_band=okb,BB_fail=okbb,verdict='PASS' if okb==6 and okbb==6 else ('FAIL' if (6-okb)>=2 or (6-okbb)>=2 else 'inconclusive'))
def bestres(A,Bv): s=np.vdot(Bv.ravel(),A.ravel())/np.vdot(Bv.ravel(),Bv.ravel()); return float(n(A-s*Bv)/n(A))
viol=0; cnt=0
for kk in P.files:
    if kk.startswith('S') or '_(0, 1)' in kk: continue
    for pi in (0,1):
        cnt+=1
        if min(bestres(P[kk][pi],C[1]),bestres(P[kk][pi],C[2]))<1e-3: viol+=1
out['control_interior']=dict(pieces=cnt,scalar_multiple_violations=viol,verdict='PASS' if viol==0 else 'FAIL')
json.dump(out,open('../data/o40.json','w'),indent=1); print(json.dumps({k_:v for k_,v in out.items() if k_!='cones'},indent=1))
