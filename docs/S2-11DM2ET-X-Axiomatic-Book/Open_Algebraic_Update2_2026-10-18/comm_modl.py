# mod-ell commutant dim of s=9 (+,+) sector: dim_Fl >= dim_C commutant (upper bound for char 0).
import flint, numpy as np, itertools, sys
sys.argv=['x','9']; src=open('irr_modl.py').read()
src=src.replace('spans=[]','spans=[]\n        if d==60:\n            n=d; rows=[]\n            for M_ in (Sd,Td):\n                Mt=[[int(M_[i,j]) for j in range(n)] for i in range(n)]\n                for i in range(n):\n                    for j in range(n):\n                        r=[0]*(n*n)\n                        for k_ in range(n):\n                            r[i*n+k_]=(r[i*n+k_]+Mt[k_][j])%ell\n                            r[k_*n+j]=(r[k_*n+j]-Mt[i][k_])%ell\n                        rows.append(r)\n            _,cd=flint.nmod_mat(rows,ell).nullspace(); print("COMMUTANT_modl",cd,flush=True)')
exec(src)
