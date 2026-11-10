# Local-derived. t4429 / PP Fix G step (ii): explicit lambda for the 2-dim ternary part of K, exact over Q, n <= 600 (> 42 Sturm, > 84 for squares via V5).
# h1 = theta(a=7,b=1) - theta(a=1,b=49) ; h2 = theta(a=14,b=1) - theta(a=2,b=49), theta(a,b) := theta_{L1}(a tau) theta(b tau), L1: x^2+xy+2y^2.
# Only b in {1,49} used (character chi_28 per PP split). Check h_i in span_Q(K) exactly and report coordinates on the row-reduced basis G1..G4.
import cypari2; P=cypari2.Pari(); P.allocatemem(10**9)
NB=600
P(f"NB={NB}; r1=Vec(qfrep([2,1;1,4],NB,1))")
P("thL(a)=my(v=vector(NB+1)); v[1]=1; for(n=1,NB\\a, v[a*n+1]=2*r1[n]); v")
P("th1(b)=my(v=vector(NB+1)); for(n=0,sqrtint(NB\\b), v[b*n^2+1]+=if(n,2,1)); v")
P("mul(u,w)=Vec(Ser(u)*Ser(w)+O(x^(NB+1)))[1..NB+1]")
P("h1=mul(thL(7),th1(1))-mul(thL(1),th1(49)); h2=mul(thL(14),th1(1))-mul(thL(2),th1(49))")
P("m=mfinit([196,3/2,28],1); C=mfcoefs(m,NB); Kc=matker(mfheckemat(m,9)); CK=C*Kc; Gr=matrix(4,NB+1); R=matrref(CK~); ")
print("dim K =",P("#Kc"))
for h in ["h1","h2"]:
    P(f"sol=matsolve(CK[1..40,]~*CK[1..40,]+0,CK[1..40,]~*({h}[1..40]~))")  # least-squares-style solve on first 40 rows, then exact check on all
    ok=P(f"CK*sol=={h}~")
    print(h,"in span(K) exactly on n<=600:",ok,"; coordinates on matker columns K1..K4:",P("sol~"))
print("rank[h1,h2] =",P("matrank(Mat([h1;h2]))"))
P("Sp=mfinit([196,3/2,28]); Cv=mfcoefs(Sp,NB)")
print("h1,h2 in span of full M_{3/2}(196,chi28) basis on n<=600:",P("matrank(matconcat([Cv,h1~,h2~]))==matrank(Cv)"))
