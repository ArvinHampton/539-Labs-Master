import sys,json,numpy as np,os
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/RTA_prereg/results')
os.chdir('/workspace/quantum-comp/reports/s_family_paths/RTA_prereg/results')
from run_all import EC, weil_odd, hom
os.chdir('/workspace/quantum-comp/reports/s_family_paths/A32_35_to_rho7')
e7=EC(7); S7,T7=e7['S'],e7['T']; out={}
lat={'A7':[[2,7],[7,7]],'[[2,1],[1,18]]':[[2,1],[1,18]],'[[6,1],[1,6]]':[[6,1],[1,6]],'-[[2,1],[1,18]]':[[-2,-1],[-1,-18]],'-[[6,1],[1,6]]':[[-6,-1],[-1,-6]],'[[1,0],[0,35]]':[[1,0],[0,35]],'[[5,0],[0,7]]':[[5,0],[0,7]],'[[3,1],[1,12]]':[[3,1],[1,12]],'[[4,1],[1,9]]':[[4,1],[1,9]],'[[2,1],[1,-17]]':[[2,1],[1,-17]]}
for nm,A in lat.items():
  try: S,T,eps=weil_odd(A)
  except Exception as ex: out[nm]=str(ex); continue
  row={}
  for tag,(Sx,Tx) in {'rho':(S,T),'dual':(S.conj(),T.conj())}.items():
    row[tag]=[hom(Sx*(-1j)**k,Tx*np.exp(2j*np.pi*k/12),S7,T7)[0] for k in range(12)]
  out[nm]=row; print(nm,row,flush=True)
json.dump(out,open('controls.json','w'),indent=1)
