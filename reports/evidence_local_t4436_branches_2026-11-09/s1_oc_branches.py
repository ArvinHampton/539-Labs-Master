# Local-derived (t4436, branches Oc-1, Oc-2, Oc-3). PARI/GP via cypari2 (computational base: exact mfinit / Hecke matrices / mftobasis).
# Space: S = S_{3/2}(Gamma0(196), chi_28) (PARI mfinit([196,3/2,28],1)); K = ker T(9) (dim 4).
import cypari2; pari=cypari2.Pari(); pari.allocatemem(3*10**9)
P=lambda s: pari(s)
B=600
P(f"m=mfinit([196,3/2,28],1); Bh=mfbasis(m); d=mfdim(m); C=matconcat(vector(d,j,mfcoefs(Bh[j],{B})~))")  # (B+1) x d coefficient matrix
print("[1] S_{3/2}(196,chi28): mfparams =", P("mfparams(m)"), " dim =", P("d"), " Sturm bound (3/2)/12*[SL2:G0(196)] =", P("3/2/12*196*(1+1/2)*(1+1/7)"))
P("E=ellinit([1,-1,0,-2,-1]); af=ellan(E,400)")
P("T9=mfheckemat(m,9); K=matker(T9)")
P("W=matid(d); foreach([3,11,13,23,29,37],p, my(M=mfheckemat(m,p^2)); W=W*matker((M-af[p]*matid(d))*W))")
print("[2] dim K = ker T(9) =", P("#K"), "; dim W4 (menu Oc-1 def, p in {3,11,13,23,29,37}) =", P("#W"), "; rank[W4|K] =", P("matrank(matconcat([W,K]))"), "(4 => W4 = K)")
print("    c(35) on the K basis:", P("vector(#K,j,(C*K[,j])[36])"))
# [3] square-supported subspaces (coefficients vanish at every non-square n <= B)
P(f"ns=select(n->!issquare(n),vector({B},n,n)); Cns=matrix(#ns,d,i,j,C[ns[i]+1,j])")
print("[3] dim {F in S : c(n)=0 for all non-square n <=",B,"} =", P("#matker(Cns)"))
print("    dim {F in K : c(n)=0 for all non-square n <=",B,"} =", P("#matker(Cns*K)"))
# [4] unary theta u_psi = sum_{k>=1} psi(k) k q^{k^2}: test consistency with S (exact linear algebra on n<=B)
def unary(psi):
    return f"vector({B+1},n,my(k);if(n>1&&issquare(n-1,&k),{psi}*k,0))~"
for name,psi in [("1 (untwisted partial theta)","1"),("chi_-4","kronecker(-4,k)"),("chi_-7","kronecker(-7,k)"),("chi_-3","kronecker(-3,k)"),("chi_-8","kronecker(-8,k)"),("chi_-20","kronecker(-20,k)"),("chi_-35","kronecker(-35,k)"),("chi_28","kronecker(28,k)"),("chi_140","kronecker(140,k)")]:
    P(f"u={unary(psi)}; sol=matsolve(matconcat([C,u]) , vectorv({B+1}))")  # dummy to keep syntax simple
    r0=int(P("matrank(C)")); r1=int(P("matrank(matconcat([C,u]))"))
    rk=int(P("matrank(matconcat([C*K,u]))")); r0k=int(P("matrank(C*K)"))
    print(f"[4] u_psi, psi = {name}: rank C = {r0}, rank [C|u] = {r1} -> {'coefficients CONSISTENT with S (n<=%d)'%B if r1==r0 else 'NOT in S (rank rises)'};  rank [C K|u] = {rk} vs {r0k} -> {'consistent with K' if rk==r0k else 'NOT in K'}")
    if r1==r0:
        P("x=matinverseimage(C,u)")
        print("     coordinates in mfbasis:", P("x~"), "; T(9) x =", P("(T9*x)~"), "; T(9)-eigen:", P("matrank(matconcat([x,T9*x]))==1"),
              "; eigenvalue lambda_9 =", P("my(y=T9*x,i=0);for(j=1,#x,if(x[j],i=j;break));y[i]/x[i]"))
        for p in [3,5,11,13]:
            print(f"       T({p}^2) eigenvalue on u:", P(f"my(M=mfheckemat(m,{p}^2),y=M*x,i=0);for(j=1,#x,if(x[j],i=j;break));if(matrank(matconcat([x,y]))==1,y[i]/x[i],\"not eigen\")"))
# [5] Oc-2 at small levels: common eigenspace of T(p^2) with eigenvalue chi_140(p) a_p(f), p in {11,37,53,71} (chi_140(p)=-1, a_p != 0)
print("[5] a_p(f), chi_140(p) for p in {11,37,53,71}:", P("[[p,af[p],kronecker(140,p)]|p<-[11,37,53,71]]"))
for N in [196,392,784]:
    for D in [1,-4,-7,28,-8,8,-56,56,5,-20,-35,140,-3,12]:
        try:
            P(f"mm=mfinit([{N},3/2,{D}],1); dd=mfdim(mm)")
        except cypari2.PariError as e:
            continue
        if int(P("dd"))==0:
            print(f"    level {N}, char {D}: dim 0"); continue
        P("V=matid(dd); foreach([11,37,53,71],p, my(M=mfheckemat(mm,p^2)); if(#V, V=V*matker((M-kronecker(140,p)*af[p]*matid(dd))*V)))")
        P("V2=matid(dd); foreach([11,37,53,71],p, my(M=mfheckemat(mm,p^2)); if(#V2, V2=V2*matker((M-af[p]*matid(dd))*V2)))")
        print(f"    level {N}, char {D}: dim S = {P('dd')}; dim common eigensp. for chi140(p)a_p(f) (Xi) = {P('#V')}; for a_p(f) (49a1 packet) = {P('#V2')}")
