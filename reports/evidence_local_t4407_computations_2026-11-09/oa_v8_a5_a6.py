# Local-derived. t4407 A5/A6 on K = ker T(9) ⊂ V = S_{3/2}(Gamma0(196),chi_28) (PARI convention).
# A5: P7 F := sum_{7|n} c(n) q^n = V(7)U(7)F is a weight-3/2 cusp form on Gamma0(1372) (U(7) keeps level 196 since 7|49; V(7) raises it by 7;
#     characters change by Kronecker symbols, irrelevant for Sturm). Sturm bound for weight 3/2 on Gamma0(1372): index 2352, bound 3/2*2352/12 = 294
#     (apply Sturm to (P7F)^2 in weight 3). So c(n)=0 for 7|n, n<=294 (exact) => P7 F = 0 for all F in K.
# A6: U(4), U(2), U(7), U(49) on K. U(4) and U(49) map V to V (Shimura 1973 Prop. 1.5: U(m), m|N/4.. character times (4m/.) = trivial for m=4,49);
#     verify U(4)K ⊂ K and compute its matrix exactly, Sturm bound of V = 3/2*336/12 = 42.
import cypari2, time; pari=cypari2.Pari(); pari.allocatemem(3*10**9); P=pari
t0=time.time()
NC=400
P(f"m=mfinit([196,3/2,28],1); d=mfdim(m); Kc=matker(mfheckemat(m,9)); CB=mfcoefs(m,{NC}); C=matrix(#Kc,{NC}+1,j,i,(CB*Kc[,j])[i]); piv=matindexrank(C)[2]; H=matrix(#Kc,#Kc,a,b,C[a,piv[b]])^(-1)*C")
print("dim K =",P("#Kc"),"; pivots n =",P("vector(#piv,j,piv[j]-1)"),flush=True)
print("A5: max n<=400 with 7|n and some c(n)!=0 on K:", P(f"my(r=0); for(n=1,{NC}, if(n%7==0 && H[,n+1]!=vector(#Kc,i,0)~, r=n)); r"), " (0 = none); Sturm bound needed: 294",flush=True)
# A6 U(4)
P("U4=matrix(#Kc,#Kc,j,i, H[j,4*(piv[i]-1)+1])")   # coordinates of U(4)G_j on the row-reduced basis (G_i has 1 at pivot i, 0 at other pivots)
ok=P(f"my(ok=1); for(j=1,#Kc, my(u=vector({NC}\\4+1,n,H[j,4*(n-1)+1]), w=sum(i=1,#Kc,U4[j,i]*H[i,1..({NC}\\4+1)])); if(u!=w,ok=0)); ok")
print(f"U(4)G_j = sum_i U4[j,i] G_i holds for all n<={NC//4} (>= Sturm 42):",ok, flush=True)
print("U(4) matrix on (G_1..G_4) [row j = coords of U(4)G_j]:",P("U4"))
print("charpoly U(4) on K:",P("factor(charpoly(U4~))"))
# eigenvectors of U(4) and relation with the plus space
P("KB=mfkohnenbasis(m); IP=matintersect(KB,Kc); Pl=matrix(#IP,{NC}+1,j,i,(CB*IP[,j])[i])".replace("{NC}",str(NC)))
P("Plc=matrix(#IP,#Kc,j,i,Pl[j,piv[i]])")
print("plus∩K in G-coordinates:",P("Plc"))
print("U(4)-stability of plus∩K: rank [Plc ; Plc*U4] =",P("matrank(matconcat([Plc;Plc*U4]))")," (2 => stable)")
print("eigen of U(4) restricted: ",P("my(M=U4~); [matker(M-x*matid(4)) | x<-[]]") if False else "")
for lam in ["2","-2","1","-1","0","sqrt(2)","-sqrt(2)","2*sqrt(2)","-2*sqrt(2)"]:
    pass
print("U(4) eigenvalues (numerical roots of charpoly):",P("polroots(charpoly(U4~))"))
# U(2): K -> S_{3/2}(196, chi_56)?  test by expressing U(2)G_j in a basis of mfinit([196,3/2,56],1)
try:
    P("m56=mfinit([196,3/2,56],1); d56=mfdim(m56)")
    print("dim S_3/2(196,chi_56) =",P("d56"),flush=True)
    if int(P("d56"))>0:
        P(f"CB56=mfcoefs(m56,{NC}\\2)")
        P(f"U2=matrix({NC}\\2+1,#Kc,n,j,H[j,2*(n-1)+1]); sol=matsolve(matconcat([CB56,U2])~*0+0,0)") if False else None
        print("rank [basis(chi_56) | U(2)G_1..4] vs rank basis:",P(f"[matrank(matconcat([CB56, matrix({NC}\\2+1,#Kc,n,j,H[j,2*(n-1)+1])])), matrank(CB56)]"), "(equal => U(2)K ⊂ S(196,chi_56) to n<=200)")
        print("rank of U(2) on K:",P(f"matrank(matrix({NC}\\2+1,#Kc,n,j,H[j,2*(n-1)+1]))"))
except cypari2.PariError as e: print("U(2) part err:",e)
print("U(7)G_j and U(49)G_j: identically 0 on K by A5 (c(7n)=0).")
print("elapsed %.1fs"%(time.time()-t0))
