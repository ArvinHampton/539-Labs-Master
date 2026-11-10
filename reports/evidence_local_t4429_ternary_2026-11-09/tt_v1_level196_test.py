# Local-derived. t4429 fallback (i), step 1 (method test at the KNOWN level 196): is the f-packet K = ker T(9) ⊂ S_{3/2}(Gamma0(196),chi_28)
# spanned (mod nothing) by ternary theta series of the CM shape Q = a*N(x+y*omega) + b*z^2 (omega=(1+sqrt-7)/2, N = x^2+xy+2y^2),
# i.e. products theta_{L1}(a tau) * theta(b tau), and by their congruence-class refinements? Exact rank computations on q-expansions n<=NB.
import cypari2; pari=cypari2.Pari(); pari.allocatemem(2*10**9); P=pari
NB=300
P(f"NB={NB}; r1=Vec(qfrep([2,1;1,4],NB,1))")   # r1[n] = #{v : N(v)=n}/2 for n>=1 (qfrep counts pairs ±v)
P("thL(a)=my(v=vector(NB+1)); v[1]=1; for(n=1,NB\\a, v[a*n+1]=2*r1[n]); v")
P("th1(b)=my(v=vector(NB+1)); for(n=0,sqrtint(NB\\b), v[b*n^2+1]+=if(n,2,1)); v")
P("mul(u,w)=my(s=Ser(u)*Ser(w)+O(x^(NB+1))); Vec(s)[1..NB+1]")   # note Ser(v) uses variable x
P("m=mfinit([196,3/2,28],1); Kc=matker(mfheckemat(m,9)); CK=matrix(#Kc,NB+1,j,i,(mfcoefs(m,NB)*Kc[,j])[i])")
rows=[]
for a in [1,2,4,7,14,28]:
    for b in [1,7,49]:
        rows.append((a,b))
P("PR=[]")
for a,b in rows: P(f"PR=concat(PR,[mul(thL({a}),th1({b}))])")
P("PM=matrix(#PR,NB+1,j,i,PR[j][i])")
rP=int(P("matrank(PM)")); rK=int(P("matrank(CK)")); rU=int(P("matrank(matconcat([PM;CK]))"))
print("products theta_L1(a.)theta(b.), (a,b) in",rows)
print(f"rank products = {rP}; rank K = {rK}; rank union = {rU}; dim(span ∩ K) = {rP+rK-rU} (on n<={NB})")
