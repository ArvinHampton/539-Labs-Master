# A33: T-spectrum of E (from WFam via RTA_prereg EC) vs fitted V; smallest singular values of the Hom systems (gap)
import sys,os,json,numpy as np
here=os.getcwd(); sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/RTA_prereg/results')
os.chdir('/workspace/quantum-comp/reports/s_family_paths/RTA_prereg/results'); from run_all import EC; e7=EC(7); os.chdir(here)
d=np.load('module.npz'); MS,MT=d['MS'],d['MT']; E,C=e7['E'],e7['C']; S7,T7=e7['S'],e7['T']
sp=lambda T: sorted(int(round(((np.angle(v)/(2*np.pi))%1)*140))%140 for v in np.linalg.eigvals(T))
TE=E.conj().T@T7@E; SE=E.conj().T@S7@E; TC=C.conj().T@T7@C
def svs(MS1,MT1,MS2,MT2):
    d1,d2=len(MS1),len(MS2); I1,I2=np.eye(d1),np.eye(d2)
    K=np.vstack([np.kron(I2,MS1.T)-np.kron(MS2,I1), np.kron(I2,MT1.T)-np.kron(MT2,I1)])
    return [float(x) for x in np.linalg.svd(K,compute_uv=False)[-3:]]
out=dict(spec_V=sp(MT),spec_E=sp(TE),spec_C=sp(TC),equal_V_E=sp(MT)==sp(TE),
         sv_V_to_E=svs(MS,MT,SE,TE))
print(out); json.dump(out,open('spec_check.json','w'),indent=1)
