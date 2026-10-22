# A33: Hom between the 36-dim law module V (fitted, Cat B) and rho7|W, E, C, twisted by chi^k; T-spectrum of V.
import sys,os,json,numpy as np
here=os.getcwd()
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/RTA_prereg/results')
os.chdir('/workspace/quantum-comp/reports/s_family_paths/RTA_prereg/results'); from run_all import EC; e7=EC(7); os.chdir(here)
from module import homdim
d=np.load('module.npz'); MS,MT=d['MS'],d['MT']
S7,T7=e7['S'],e7['T']; E,C=e7['E'],e7['C']
sub=lambda P:(P.conj().T@S7@P, P.conj().T@T7@P)
tg={'W':(S7,T7),'E':sub(E),'C':sub(C)}
out={'V_T_spectrum':sorted(round(float((np.angle(v)/(2*np.pi))%1)*140,4) for v in np.linalg.eigvals(MT))}
out['End_V']=homdim(MS,MT,MS,MT)
for conv,(a1,a2) in {'M':(MS,MT),'M^T':(MS.T,MT.T)}.items():
    for nm,(S2,T2) in tg.items():
        for k in range(12):
            cS=(-1j)**k; cT=np.exp(2j*np.pi*k/12)
            for dl in (False,True):
                s2,t2=(S2.conj(),T2.conj()) if dl else (S2,T2)
                h=homdim(a1*cS,a2*cT,s2,t2)
                if h: out[f"{conv} V(x)chi^{k} -> {nm}{'*' if dl else ''}"]=h
print(json.dumps(out,indent=0)); json.dump(out,open('to_rho7.json','w'),indent=1)
