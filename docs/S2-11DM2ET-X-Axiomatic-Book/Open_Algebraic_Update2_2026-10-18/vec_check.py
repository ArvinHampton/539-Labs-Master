import sys, numpy as np, time
from vecfam import VF, to_complex
for s in map(int,sys.argv[1].split(',')):
    t=time.time(); v=VF(s); S=to_complex(v.S_exp(),v.K)/np.sqrt(abs(v.F.det)); T=to_complex(v.T_exp(),v.K); tb=time.time()-t
    msg=f"s={s} N={v.N} build {tb:.1f}s"
    if s<=11:
        S0=v.F.Smatrix(); T0=v.F.Tmatrix(); msg+=f" |S-S0|={np.abs(S-S0).max():.2e} |T-T0|={np.abs(T-T0).max():.2e}"
    msg+=f" |S^2-P|... unitary err {np.abs(S@S.conj().T-np.eye(v.N)).max():.2e}"
    print(msg,flush=True)
