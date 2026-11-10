# Local-derived. Task 3: Shimura preimages of f_49a1 in S_{3/2}(Gamma0(196), chi_28), chi_28=(28/.)=chi_-4*chi_-7; Waldspurger zero-pattern vs L(f x chi_D,1); Xi = f x chi_-20 = f x chi_140.
import cypari2; pari=cypari2.Pari(); pari.allocatemem(4*10**9); pari.set_real_precision(38)
P=pari
P("E=ellinit([1,-1,0,-2,-1]); Ep=ellinit(elltwist(E,140)); af=ellan(E,100);")
P("m=mfinit([196,3/2,28],1); Bh=mfbasis(m)")
print("S_3/2(Gamma0(196),chi_28) dim =", P("mfdim(m)"))
P("K=matid(mfdim(m)); foreach([3,11,13,23,29,37],p, my(M=mfheckemat(m,p^2)); K=K*matker((M-af[p]*matid(#M))*K))")
print("dim f-eigenspace (T(p^2)=a_p(f), p=3,11,13,23,29,37):", P("#K"))
P("C=matrix(#K,401,j,i,mfcoefs(mflinear(Bh,K[,j]),400)[i]); piv=matindexrank(C)[2]; H=matrix(#K,#K,a,b,C[a,piv[b]])^(-1)*C")
P("Fs=vector(#K,j,H[j,])")  # row-reduced q-expansions (coefficient vectors n=0..400)
for j in range(int(P("#K"))):
    print(f"F_{j+1} (row-reduced) coeffs n=0..60:", P(f"Fs[{j+1}][1..61]"))
# Shimura lifts of the eigen-subspace (t squarefree)
P("fc=concat(0,af[1..40])")
outs=[]
for t in [1,2,3,5,6,7,10,11,13,14,15,17,19,21,23,26,29,30,31,35]:
    P(f"L=vector(#K,j,mfcoefs(mfshimura(m,mflinear(Bh,K[,j]),{t})[2],40))")
    ok=P("my(r=1); for(j=1,#L, my(lc=L[j]); if(lc!=vector(41,i,0) && lc*fc[2]!=fc*lc[2], r=0)); r")
    nz=P("sum(j=1,#L,L[j]!=vector(41,i,0))")
    outs.append((t,int(ok),int(nz)))
print("Shimura lift check [t, all lifts proportional to f (1=yes), #nonzero lifts]:", outs)
# zero pattern: coefficient vectors at squarefree n vs L(f x chi_D,1)
rows=[]
for n in range(1,80):
    if int(P(f"issquarefree({n})"))!=1: continue
    cn=P(f"vector(#Fs,j,Fs[j][{n}+1])")
    allzero = all(int(P(f"Fs[{j+1}][{n}+1]==0")) for j in range(int(P('#Fs'))))
    D1=int(P(f"coredisc(-{n})"))
    L1=P(f"my(Ed=ellinit(elltwist(E,{D1}))); [ellrootno(Ed), round(lfun(lfuncreate(Ed),1)*10^6)/10^6]")
    rows.append((n,"all-zero" if allzero else "nonzero", D1, str(L1)))
print("[n, coeffs of eigenspace at n, D=coredisc(-n), (rootno, L(f x chi_D,1))]:")
for r in rows: print("  ",r)
print("Xi: L(Xi,1) =", P("lfun(lfuncreate(Ep),1)"), " ; coredisc(-5) =", P("coredisc(-5)"), "; f x chi_-20 = f_Xi (part1)")
