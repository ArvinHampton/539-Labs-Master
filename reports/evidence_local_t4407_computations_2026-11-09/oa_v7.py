# Local-derived. t4407 O-a v7 (v6 crashed on GP row-extraction syntax in the coords step; v6 kept; coords now (s1, s2-s1*a2)). Earlier: (v5 crashed: mfcoefs needs the space, not the basis vector; v5 kept). Earlier: (v4 crashed: 'I' is reserved in GP; v4 kept untouched). Aim: close PP N1 (K f-isotypic for ALL p).
# Computes: (1) Kohnen-plus part of K = ker T(9); (2) explicit Shimura lifts S_t (Shimura's defining formula) of the K-basis K_1..K_4
# (matker columns, PP naming) and of the row-reduced G_j; (3) injectivity of the truncated lift map Phi_T : V -> prod_{t in T} C^{nmax},
# F -> (A_t(n))_{t in T, n<=nmax}, on V = S_{3/2}(196,chi_28) (dim 9) and on K, for several finite sets T of squarefree t.
import cypari2, time; pari=cypari2.Pari(); pari.allocatemem(3*10**9); P=pari
t0=time.time()
NC=860
P(f"E=ellinit([1,-1,0,-2,-1]); af=ellan(E,{NC}); m=mfinit([196,3/2,28],1); Bh=mfbasis(m); d=mfdim(m); Kc=matker(mfheckemat(m,9))")
P(f"CB=mfcoefs(m,{NC}); CBt=matrix(d,{NC}+1,j,i,CB[i,j])")   # row j = coefficients of basis form j
print("coeff matrix size:",P("matsize(CB)"),"t=%.0fs"%(time.time()-t0),flush=True)
P("KK=Kc~*CBt")  # rows: K_1..K_4 (matker columns) coefficient vectors
P("KB=mfkohnenbasis(m); IP=matintersect(KB,Kc); KPl=IP~*CBt")
print("dim K =",P("#Kc"),"; dim Kohnen plus space =",P("matsize(KB)[2]"),"; dim(plus ∩ K) =",P("#IP"),flush=True)
for j in range(1,int(P("#IP"))+1): print(f" plus∩K basis vector {j}, n=0..60:",P(f"KPl[{j},1..61]"),flush=True)
P("shim(h,t,B)=vector(B,n,sumdiv(n,dd,kronecker(28,dd)*kronecker(-4,dd)*kronecker(t,dd)*h[t*(n/dd)^2+1]))")
B=8
P(f"fv=vector({B},n,af[n]); fv2=vector({B},n,if(n%2,0,af[n/2])); A2=matconcat([fv~,fv2~])")
print("K_j (matker columns): S_t(K_j) on n<=8 as coords (f, f(2.)) [rank-extra beyond span{f,f(2.)} must be 0]:",flush=True)
for t in [1,2,3,5,6,10,13]:
    rows=[]
    for j in range(1,5):
        P(f"s=shim(KK[{j},],{t},{B})")
        rows.append(str(P("[matrank(matconcat([A2,s~]))-2, s[1], s[2]-s[1]*fv[2]]")))
    print(f"  t={t}:",rows,flush=True)
# truncated lift map ranks
def rank_for(T, nmax, rowsname, nrows):
    P(f"Mx=matrix({nrows},1)")
    for t in T:
        P(f"Mx=matconcat([Mx, matrix({nrows},{nmax},j,n,shim({rowsname}[j,],{t},{nmax})[n])])")
    return int(P("matrank(Mx[,2..#Mx])"))
for T in [[1],[1,2],[1,2,5],[1,2,3],[1,2,3,5],[1,2,5,13],[1,2,3,5,6,10,13]]:
    nmax=max(1,int(( (NC)//max(T) )**0.5))
    nmax=min(nmax,8)
    rV=rank_for(T,nmax,"CBt","d"); rK=rank_for(T,nmax,"KK","4")
    print(f" T={T}, n<={nmax}: rank Phi_T on V (dim 9) = {rV}; on K (dim 4) = {rK}",flush=True)
print("elapsed %.1fs"%(time.time()-t0))
