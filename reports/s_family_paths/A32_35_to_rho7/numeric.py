import sys,json,numpy as np,math,scipy.linalg as sl
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/RTA_prereg/results')
import os; os.chdir('/workspace/quantum-comp/reports/s_family_paths/RTA_prereg/results')
from run_all import EC, weil_odd, hom
os.chdir('/workspace/quantum-comp/reports/s_family_paths/A32_35_to_rho7')
e7=EC(7); S7,T7=e7['S'],e7['T']
S,T,eps=weil_odd([[2,7],[7,7]])
out={}
for k in (3,):
  cS=(-1j)**k; cT=np.exp(2j*np.pi*k/12)
  d,gap,B=hom(S*cS,T*cT,S7,T7); X=B[0]
  sv=np.linalg.svd(X,compute_uv=False); r=int((sv>1e-8*sv[0]).sum())
  res=max(np.abs(X@(S*cS)-S7@X).max(),np.abs(X@(T*cT)-T7@X).max())
  img=X@np.linalg.pinv(X)@np.eye(42)  # projector onto image
  inE=np.linalg.norm(e7['E'].conj().T@X)/np.linalg.norm(X); inC=np.linalg.norm(e7['C'].conj().T@X)/np.linalg.norm(X)
  ker=sl.null_space(X)
  out[k]=dict(dimHom=d,gap=gap,rank=r,residual=float(res),sv=[float(x) for x in sv[:r+2]],frac_E=float(inE),frac_C=float(inC),dimE=e7['E'].shape[1],dimC=e7['C'].shape[1],eps=str(eps))
  np.save('X_chi3.npy',X)
  # which 35 components (labels mu) survive: column norms
  out[k]['col_norms']=[round(float(x),4) for x in np.linalg.norm(X,axis=0)]
  # kernel: T-eigenvalues of ker restricted
  Tk=ker.conj().T@(T*cT)@ker; out[k]['ker_T_eigs']=sorted(round(float((np.angle(v)/(2*np.pi))%1),5) for v in np.linalg.eigvals(Tk))
print(json.dumps(out,indent=0)); json.dump(out,open('numeric.json','w'),indent=1)
