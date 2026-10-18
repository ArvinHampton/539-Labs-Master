# Item 2: N and gamma as Kronecker products in the even-s factorisation; joint-fixed dims per (odd,2-adic) sign sector.
import sys, json, numpy as np, cmath, math
from even_exact import run, red
out=[]
for s in [int(z) for z in sys.argv[1].split(',')]:
    r,F,O,Tw,key,Sx,Tx=run(s); D=F.D
    oi={o:i for i,o in enumerate(O)}; ti={t:i for i,t in enumerate(Tw)}
    def mats(f):
        Mo=np.zeros((len(O),len(O))); M2=np.zeros((len(Tw),len(Tw)),complex)
        for i,(al,be) in enumerate(F.LABELS):
            j,ph=red(F,f(np.array(al))%D,f(np.array(be)))
            Mo[oi[key[j][0]],oi[key[i][0]]]=1; M2[ti[key[j][1]],ti[key[i][1]]]=cmath.exp(2j*math.pi*float(ph))
        return Mo,M2
    No,N2=mats(lambda v:-v); Go,G2=mats(lambda v:F.G@v)
    def fix(Ms):
        A=np.vstack([M-np.eye(len(M)) for M in Ms]); return A.shape[1]-np.linalg.matrix_rank(A,tol=1e-8)
    def eig_sec(M1,M2,a,b):  # dim of {N=a,γ=b}
        A=np.vstack([M1-a*np.eye(len(M1)),M2-b*np.eye(len(M2))]); return A.shape[1]-np.linalg.matrix_rank(A,tol=1e-8)
    # eigenvalues of gamma on odd part
    ev=sorted({complex(round(z.real,6),round(z.imag,6)) for z in np.linalg.eigvals(Go)},key=lambda z:(z.real,z.imag))
    tab={}; tot=0
    for a in (1,-1):
        for b in ev:
            do=eig_sec(No,Go,a,b)
            if do==0: continue
            d2=eig_sec(N2,G2,a,np.conj(b))  # need product eigen 1
            tab[f"N={a},γ_odd={b}"]=[do,d2]; tot+=do*d2
    full=fix([np.kron(No,N2),np.kron(Go,G2)])
    rec={"s":s,"sectors[odd,2adic]":tab,"dimU_sum":tot,"dimU_direct":full,"orbit_bound":(s//2)*(s//2+1)}
    print(json.dumps(rec,default=str),flush=True); out.append(rec)
json.dump(out,open("even_sectors.json","w"),indent=1,default=str)
