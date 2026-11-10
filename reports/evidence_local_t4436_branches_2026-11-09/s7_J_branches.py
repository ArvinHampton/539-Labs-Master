# Local-derived (t4436, branches J-1/J-2/J-3). PARI exact computations (computational base: ellrank 2-descent bounds, elltors, ellorder,
# mfinit coefficient matrices). Rank tests as in s2c (mod-p rank of integer-scaled coefficient matrix).
import cypari2; pari=cypari2.Pari(); pari.allocatemem(6*10**9)
P=lambda s: pari(s)
P("E=ellinit([1,-1,0,-2,-1]); Xi=ellinit(elltwist(E,140)); p=nextprime(2^61)")
print("[J-3] 49a1: conductor",P("ellglobalred(E)[1]"),", torsion",P("elltors(E)[2]"),", ellrank [lower, upper, ...]:",P("ellrank(E)[1..2]"))
print("[J-3] Xi : conductor",P("ellglobalred(Xi)[1]"),", torsion",P("elltors(Xi)[2]"),", ellrank [lower, upper]:",P("my(r=ellrank(Xi)); [r[1],r[2]]"))
P("r=ellrank(Xi); pts=r[4]")
print("      Xi points found:",P("pts"), "; on curve:",P("vector(#pts,i,ellisoncurve(Xi,pts[i]))"), "; ellorder (0 = infinite order):",P("vector(#pts,i,ellorder(Xi,pts[i]))"), "; canonical height:",P("vector(#pts,i,ellheight(Xi,pts[i]))"))
print("      Xi minimal model a-invariants:",P("ellminimalmodel(Xi).a1"), P("[ellminimalmodel(Xi).a1,ellminimalmodel(Xi).a2,ellminimalmodel(Xi).a3,ellminimalmodel(Xi).a4,ellminimalmodel(Xi).a6]"))
# E over K = Q(sqrt35): rank via PARI over the number field (independent cross-check of rank E(K) = rank E(Q) + rank Xi(Q))
try:
    P("K=nfinit(y^2-35); EK=ellinit([1,-1,0,-2,-1],K)")
    print("[J-3] E over Q(sqrt35): ellrank [lower, upper]:",P("my(r=ellrank(EK)); [r[1],r[2]]"), "; torsion:",P("elltors(EK)[2]"))
except cypari2.PariError as e:
    print("[J-3] ellrank over K failed:",e)
# J-1 with nebentypus chi_140: rank test of f_Xi and f_49a1 against S_2(Gamma0(980), chi_140) and M_2
P("intmat(C)=my(D=matrix(#C[,1],#C,i,j,0)); for(j=1,#C, my(c=C[,j], d=denominator(c)); for(i=1,#c, D[i,j]=c[i]*d)); D")
for flag in (1,4):
    try:
        P(f"mf=mfinit([980,2,140],{flag}); dm=mfdim(mf); B=mfsturm(mf)+50")
        if int(P("dm"))==0:
            print(f"[J-1] mfinit([980,2,140],{flag}): dim 0"); continue
        P("C=intmat(mfcoefs(mf,B)); v=concat(0,ellan(Xi,B))~; w=concat(0,ellan(E,B))~")
        print(f"[J-1] [980,2,chi_140] flag {flag}: dim {P('dm')}, rank_p C {P('matrank(C*Mod(1,p))')}, rank_p[C|f_Xi] {P('matrank(matconcat([C,v])*Mod(1,p))')}, rank_p[C|f_49a1] {P('matrank(matconcat([C,w])*Mod(1,p))')}")
    except cypari2.PariError as e:
        print("[J-1] mfinit error", e)
print("[J-1] f_49a1 old copies in S_2(Gamma0(980)): number of d | 20 =",P("numdiv(20)"))
