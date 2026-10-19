# Invariant line with correct normalisation: the true S is S_scaled/(Gauss factor); delta_{pZ} has S_scaled delta = p delta, T delta = delta.
import json
exec(open('factor_dims.py').read().split('out={}')[0])
out=json.load(open('factor_dims_121.json'))
for u in (1,2):
    S,T,ell=weil(121,u); Sd,Td,d=restrict(S,T,ell,121,1)
    I=flint.nmod_mat(d,d,[int(i==j) for i in range(d) for j in range(d)],ell)
    st=flint.nmod_mat(2*d,d,[int(X[i,j]) for X in (Sd-I*11,Td-I) for i in range(d) for j in range(d)],ell)
    n=st.nullspace()[1]; out[f"M=121,u={u},even"]["invariant_line_dim(S_scaled=11)"]=n; print(u,n)
json.dump(out,open("factor_dims_121.json","w"),indent=1)
