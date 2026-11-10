# Local-derived. t4407 O-a v4: Shimura-lift part only (v3 crashed on a GP matrix-syntax error at that step; v3 kept untouched).
import cypari2, time; pari=cypari2.Pari(); pari.allocatemem(3*10**9); P=pari
t0=time.time()
P("E=ellinit([1,-1,0,-2,-1]); af=ellan(E,700); m=mfinit([196,3/2,28],1); Bh=mfbasis(m); K=matker(mfheckemat(m,9))")
P("C=matrix(#K,701,j,i,mfcoefs(mflinear(Bh,K[,j]),700)[i]); piv=matindexrank(C)[2]; H=matrix(#K,#K,a,b,C[a,piv[b]])^(-1)*C")
P("KB=mfkohnenbasis(m); I=matintersect(KB,K); KP=matrix(#I,701,j,i,mfcoefs(mflinear(Bh,I[,j]),700)[i])")
print("dim K =",P("#K"),"; dim(Kohnen plus ∩ K) =",P("#I"),flush=True)
for j in range(1,int(P("#I"))+1): print(f" plus-part basis P_{j} n=0..60:",P(f"KP[{j},1..61]"),flush=True)
B=12
P(f"shim(h,t,B)=vector(B,n,sumdiv(n,dd,kronecker(28,dd)*kronecker(-4,dd)*kronecker(t,dd)*h[t*(n/dd)^2+1])); fv=vector({B},n,af[n]); fv2=vector({B},n,if(n%2,0,af[n/2])); fv4=vector({B},n,if(n%4,0,af[n/4])); A=matconcat([fv~,fv2~,fv4~])")
print("rank span(f,f(2.),f(4.)) on n<=12:",P("matrank(A)"))
for lab,Mx in [("G","H"),("P","KP")]:
    for t in [1,2,3,5,6,13]:
        rows=[]
        for j in range(1,int(P(f"matsize({Mx})[1]"))+1):
            P(f"s=shim({Mx}[{j},],{t},{B})")
            rows.append(str(P("[matrank(matconcat([A,s~]))-3, s==0*s, matsolve(A[[1,2,4],],s[[1,2,4]]~)~]")))
        print(f" {lab}, t={t}: per basis vector [extra rank beyond span(f,f(2.),f(4.)), lift==0, coords (f,f(2.),f(4.))]:",rows,flush=True)
print("elapsed %.1fs"%(time.time()-t0))
