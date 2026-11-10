# Local-derived. t4407 O-a (v2: unbuffered, primes <=37; v1 kept, its buffered output was lost to timeout): exact f-isotypic subspace (f = 49a1) of S_{3/2}(Gamma0(196), chi_28), PARI convention (CHI includes theta multiplier).
import cypari2, time; pari=cypari2.Pari(); pari.allocatemem(4*10**9); P=pari
t0=time.time()
P("E=ellinit([1,-1,0,-2,-1]); af=ellan(E,2000); m=mfinit([196,3/2,28],1); Bh=mfbasis(m); d=mfdim(m)")
print("dim S_3/2(196,chi_28) =", P("d"))
ps=[3,5,11,13,17,19,23,29,31,37]
for p in [3,5,11,13]:
    print(f"charpoly T({p}^2) on full space:", P(f"factor(charpoly(mfheckemat(m,{p}^2)))"))
# joint kernel over all primes 3<=p<80, p != 7
P("K=matid(d)")
for p in ps:
    P(f"M=mfheckemat(m,{p}^2); K=K*matker((M-af[{p}]*matid(d))*K)")
    print(f" after p={p}: dim joint f-eigenspace =", P("#K"))
P("K3=matker(mfheckemat(m,9))")
print("dim ker T(9) alone =", P("#K3"), "; K3 == span(K)?", P("matrank(concat(K,K3))==#K && #K3==#K"))
# weight-2 side: all Hecke eigen systems of S_2(Gamma0(98)) (Niwa: lifts of level-196 forms land in level 98)
P("m2=mfinit([98,2],1); L2=mfeigenbasis(m2)")
print("S_2(Gamma0(98)) newforms (level, a_3, a_5, a_11):")
for lev in [7,14,49,98]:
    try:
        P(f"mm=mfinit([{lev},2],0); EB=mfeigenbasis(mm)")
        n=int(P("#EB"))
        for j in range(1,n+1):
            print(f"  level {lev} #{j}: field", P(f"mffields(mm)[{j}]"), " a_2..a_13:", P(f"mfcoefs(EB[{j}],13)[3..14]"))
    except cypari2.PariError as e: print("  level",lev,"err",e)
print("a_3(f) =", P("af[3]"), "; Eisenstein-type |lambda_3| = 4 (Hasse: |a_3(g)|<=2sqrt3 < 4)")
P("C=matrix(#K,1201,j,i,mfcoefs(mflinear(Bh,K[,j]),1200)[i]); piv=matindexrank(C)[2]; H=matrix(#K,#K,a,b,C[a,piv[b]])^(-1)*C")
for j in range(1,int(P("#K"))+1):
    print(f"G_{j} (row-reduced, exact) n=0..80:", P(f"H[{j},1..81]"))
# support mod 4 and square classes
print("support of the isotypic space by n mod 4 (count of n<=1200 with some nonzero coeff):", P("vector(4,r,sum(n=1,1200,(n%4==r-1)&&(H[,n+1]!=vector(#K,i,0)~)))"))
print("support by n mod 7 :", P("vector(7,r,sum(n=1,1200,(n%7==r-1)&&(H[,n+1]!=vector(#K,i,0)~)))"))
# Kohnen plus space
try:
    P("KB=mfkohnenbasis(m)"); print("Kohnen plus space dim =", P("matsize(KB)[2]"))
    print("dim (plus space ∩ f-isotypic) =", P("my(I=matintersect(KB,K)); if(#I,matsize(I)[2],0)"))
except cypari2.PariError as e: print("mfkohnenbasis err:", e)
# explicit Shimura lift (textbook formula, k=1): S_t(F)_n = sum_{d|n} psi_t(d) c(t n^2/d^2), psi_t(d) = chi_28(d) chi_-4(d) (t/d)
P("shim(h,t,B)=vector(B,n,sumdiv(n,dd,kronecker(28,dd)*kronecker(-4,dd)*kronecker(t,dd)*h[t*(n/dd)^2+1]))")
P("fv=vector(30,n,af[n]); fv2=vector(30,n,if(n%2,0,af[n/2])); fv4=vector(30,n,if(n%4,0,af[n/4]))")
for t in [1,2,3,5,6,13]:
    rows=[]
    for j in range(1,int(P("#K"))+1):
        P(f"s=shim(H[{j},],{t},30)")
        rows.append(str(P("[matrank(Mat([fv;fv2;fv4;s]))-matrank(Mat([fv;fv2;fv4])), if(s==0*s,0,1), matsolve(Mat([fv;fv2;fv4])[,[1,2,4]]~, s[[1,2,4]]~)~]")))
    print(f" t={t}: per G_j [extra rank beyond span(f,f(2.),f(4.)), nonzero?, coords on (f,f(2.),f(4.))]:", rows)
print("elapsed %.1fs"%(time.time()-t0))
