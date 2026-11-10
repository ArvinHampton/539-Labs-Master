# Local-derived. Independent verification of PP's TT-1 generators (t4429), different route from tt_v1/tt_v3b:
# theta series computed DIRECTLY as ternary-form theta series via qfrep on Gram matrices (no product of q-series),
#   theta(a,b) := theta of Q = a(x^2+xy+2y^2) + b z^2, Gram [[2a,a,0],[a,4a,0],[0,0,2b]]   (= theta_{L1}(a tau) theta(b tau)),
# then coordinates via mftobasis in the full space S_{3/2}(Gamma0(196),chi_28) (cusp space, flag 1), exact check of the coefficient
# identity for all n <= 600, and T(9)-kernel membership via mfheckemat on coordinates.
#   G1 = theta(1,49) - theta(7,1)
#   G2 = 3 theta(1,49) - 2 theta(2,49) - 3 theta(7,1) + 2 theta(14,1)
import cypari2; P=cypari2.Pari(); P.allocatemem(10**9)
NB=600
P(f"NB={NB}")
P("th(a,b)=my(G=[2*a,a,0;a,4*a,0;0,0,2*b]); concat([1],2*Vec(qfrep(G,NB,1)))")
P("G1=th(1,49)-th(7,1); G2=3*th(1,49)-2*th(2,49)-3*th(7,1)+2*th(14,1)")
P("S=mfinit([196,3/2,28],1); B=mfcoefs(S,NB); T9=mfheckemat(S,9)")
print("dim S_{3/2}(196,chi28) =",P("mfdim(S)"),"; dim ker T(9) =",P("#matker(T9)"))
for g in ["G1","G2"]:
    P(f"c=matinverseimage(B,{g}~)")
    print(g,": in span of S basis (exact, n<=600):",P(f"#c>0 && B*c=={g}~"),"; T(9)c == 0:",P("#c>0 && T9*c==0"),"; coords:",P("c~"))
P("C1=matinverseimage(B,G1~); C2=matinverseimage(B,G2~)")
print("rank[C1,C2] =",P("matrank(matconcat([C1,C2]))"))
print("G1 first terms:",P("G1[1..30]"))
print("G2 first terms:",P("G2[1..30]"))
