# Local-derived. Search for weight-3/2 Hecke eigen-subspaces with T(p^2)-eigenvalues a_p(49a1) (p=3,11,13,23), i.e. Shimura preimages of f_49a1.
import cypari2; pari=cypari2.Pari(); pari.allocatemem(6*10**9)
P=pari
P("E=ellinit([1,-1,0,-2,-1]); af=ellan(E,100);")
P("eig(m,plist)=my(K=matid(mfdim(m))); foreach(plist,p, my(M=mfheckemat(m,p^2)); my(Z=matker((M-af[p]*matid(#M))*K)); K=K*Z; if(#K==0,break)); K")
for N in [196,392,980,784]:
    for D in [1,5,8,-4,-8,28,-7,7,-20,20,140,-35]:
        try:
            P(f"m=mfinit([{N},3/2,{D}],1)")
            d=int(P("mfdim(m)"))
            if d==0 or d>80: print(N,D,"dim",d,"(skipped)" if d>80 else ""); continue
            k=int(P("#eig(m,[3,11,13,23])"))
            print(N,D,"dim",d,"f-eigenspace dim",k, flush=True)
        except Exception as e: print(N,D,"ERR",str(e)[:80], flush=True)
