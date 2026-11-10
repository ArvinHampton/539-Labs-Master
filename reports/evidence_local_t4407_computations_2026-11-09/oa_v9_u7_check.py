# Local-derived. t4407 A5 support: consistency check of the U7 mapping lemma (Shimura 1973 Prop. 1.5: U(m) maps S_{k/2}(N,chi) to
# S_{k/2}(N, chi*(4m/.)) for m | N/4 ; here m=7, (28/.)*chi_28 = trivial) on ALL of V = S_{3/2}(196,chi_28): is the q-expansion
# sum c(7n)q^n of each basis form in the span of S_{3/2}(196, trivial) (dim 6) for n <= 60 (> Sturm 42)?  This checks the normalisation,
# it does not prove the lemma. Also U(4) -> V check on all of V (m=4: (16/.) trivial change).
import cypari2, time; pari=cypari2.Pari(); pari.allocatemem(3*10**9); P=pari
t0=time.time()
P("m=mfinit([196,3/2,28],1); CB=mfcoefs(m,420); m1=mfinit([196,3/2],1); C1=mfcoefs(m1,60)")
print("dim V =",P("mfdim(m)"),"; dim S_3/2(196,triv) =",P("mfdim(m1)"),flush=True)
P("U7=matrix(61,mfdim(m),n,j,CB[7*(n-1)+1,j])")
print("rank U7(V) =",P("matrank(U7)"),"; rank [S(196,triv) | U7(V)] =",P("matrank(matconcat([C1,U7]))"),"; rank S(196,triv) =",P("matrank(C1)"), "(equal => U7(V) ⊂ S(196,triv) on n<=60)")
P("C28=mfcoefs(m,60); U4=matrix(61,mfdim(m),n,j,CB[4*(n-1)+1,j])")
print("rank [V | U4(V)] =",P("matrank(matconcat([C28,U4]))"),"; rank V =",P("matrank(C28)"),"(equal => U4(V) ⊂ V on n<=60)")
P("Kc=matker(mfheckemat(m,9))")
print("U7 on K: max |coeff| of sum c(7n)q^n, n<=60, over K basis:",P("my(r=0); for(j=1,#Kc, my(v=U7*Kc[,j]); for(i=1,#v, r=max(r,abs(v[i])))); r"))
print("elapsed %.1fs"%(time.time()-t0))
