# Local-derived. t4407 O-a v3: structure of the f-isotypic subspace K = ker T(9) of S_{3/2}(Gamma0(196),chi_28) (dim 4; see oa_v2.log).
# Lighter than v1/v2 (coefficients to 700 only) because the box is heavily loaded; v1, v2 kept untouched.
import cypari2, time; pari=cypari2.Pari(); pari.allocatemem(3*10**9); P=pari
t0=time.time()
P("E=ellinit([1,-1,0,-2,-1]); af=ellan(E,700); m=mfinit([196,3/2,28],1); Bh=mfbasis(m); d=mfdim(m); K=matker(mfheckemat(m,9))")
print("dim K = ker T(9) =", P("#K"), flush=True)
P("C=matrix(#K,701,j,i,mfcoefs(mflinear(Bh,K[,j]),700)[i]); piv=matindexrank(C)[2]; H=matrix(#K,#K,a,b,C[a,piv[b]])^(-1)*C")
print("pivot indices n:", P("vector(#piv,j,piv[j]-1)"), flush=True)
for j in range(1,5): print(f"G_{j} (row-reduced, exact) n=0..80:", P(f"H[{j},1..81]"), flush=True)
print("support by n mod 4 (n<=700):", P("vector(4,r,sum(n=1,700,(n%4==r-1)&&(H[,n+1]!=vector(#K,i,0)~)))"))
print("support by n mod 7 (n<=700):", P("vector(7,r,sum(n=1,700,(n%7==r-1)&&(H[,n+1]!=vector(#K,i,0)~)))"))
print("support by n mod 8 (n<=700):", P("vector(8,r,sum(n=1,700,(n%8==r-1)&&(H[,n+1]!=vector(#K,i,0)~)))"), flush=True)
# splitting of K by residue classes mod 4 (plus/minus-type pieces): subspace of K with c(n)=0 for n = 2,3 mod 4 etc.
for name,cond in [("c(n)=0 unless n=0,1 mod 4 (Kohnen-type plus)","n%4==2||n%4==3"),("c(n)=0 unless n=0,3 mod 4","n%4==1||n%4==2"),("c(n)=0 unless n=2,3 mod 4","n%4==0||n%4==1"),("supported on n=1 mod 4 only","n%4!=1"),("supported on n=2 mod 4 only","n%4!=2"),("supported on n=3 mod 4 only","n%4!=3"),("supported on n=0 mod 4 only","n%4!=0"),("c(n)=0 for 7|n","n%7!=0")]:
    P(f"Z=[]; for(n=1,700, if({cond}, Z=concat(Z,[H[,n+1]~]))); Zm=if(#Z,Mat(Z~)~,matrix(0,#K)); ker_=if(#Z,matker(Mat(vector(#Z,i,Z[i])~)),matid(#K))")
    print(f" dim of subspace of K with [{name}]:", P("#ker_"), flush=True)
try:
    P("KB=mfkohnenbasis(m)"); print("PARI mfkohnenbasis dim =", P("matsize(KB)[2]"), "; dim(plus ∩ K) =", P("my(I=matintersect(KB,K)); if(#I,matsize(I)[2],0)"), flush=True)
except cypari2.PariError as e: print("mfkohnenbasis:", e, flush=True)
# explicit Shimura lift S_t (Shimura 1973 formula, k=1): S_t(F)_n = sum_{d|n} chi_28(d) chi_-4(d) (t/d) c(t n^2/d^2) ; compare with f, f(2.), f(4.)
B=12
P(f"shim(h,t,B)=vector(B,n,sumdiv(n,dd,kronecker(28,dd)*kronecker(-4,dd)*kronecker(t,dd)*h[t*(n/dd)^2+1])); fv=vector({B},n,af[n]); fv2=vector({B},n,if(n%2,0,af[n/2])); fv4=vector({B},n,if(n%4,0,af[n/4])); A=Mat([fv;fv2;fv4])")
for t in [1,2,3,5,6,13]:
    rows=[]
    for j in range(1,5):
        P(f"s=shim(H[{j},],{t},{B})")
        rows.append(str(P("[matrank(Mat([fv;fv2;fv4;s]))-3, s==0*s, s[1], s[2], s[4]]")))
    print(f" t={t}: per G_j [extra rank beyond span(f,f(2.),f(4.)), lift==0, S_t coeff n=1,2,4]:", rows, flush=True)
print("elapsed %.1fs"%(time.time()-t0))
