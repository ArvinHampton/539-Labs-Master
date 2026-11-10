# Local-derived (t4436, branches J-2 / J-1). SUPERSEDES s2b_j2_minimal_level.py (kept on disk; killed ~22:05 CST during level 9800).
# s2b used mftobasis(mf,v,1). For the FULL space M_2 (mfinit flag 4) that call returned a 'solution' at levels 2800 and 3920 although the
# direct rank test below shows f_Xi is NOT in M_2(Gamma0(2800)) (rank rises 516 -> 517); so s2b's M_2 rows are UNRELIABLE and not used.
# Its S_2 rows (NONE at 2800 and 3920) agree with the rank test here.
# Method here (citation-free linear algebra): C = mfcoefs(mf,B) (rows n = 0..B, columns = basis), v = (a_0..a_B) of the target.
# If rank[C|v] = rank C + 1 then no element of the space has these first B+1 coefficients, so the target is not in the space.
# Exactness: C and v are rational; we scale columns to integers and compute ranks modulo a large prime p. Over Q the rank is >= the rank mod
# p, and rank C over Q <= dim; so rank_p[C|v] = dim + 1 proves rank_Q[C|v] = dim + 1 > rank_Q C. Positive control: 49a1 (level 49) must
# lie in S_2(Gamma0(M)) iff 49 | M; this is reported by the same rank test (for 'in', rank over Q is computed exactly where feasible).
import cypari2, time; pari=cypari2.Pari(); pari.allocatemem(12*10**9)
P=lambda s: pari(s)
P("E=ellinit([1,-1,0,-2,-1]); Xi=ellinit(elltwist(E,140)); p=nextprime(2^61)")
P("intmat(C)=my(D=matrix(#C[,1],#C,i,j,0)); for(j=1,#C, my(c=C[,j], d=denominator(c)); for(i=1,#c, D[i,j]=c[i]*d)); D")
print("Xi conductor", P("ellglobalred(Xi)[1]"), "; prime p =", P("p"), flush=True)
jobs=[(2800,1),(2800,4),(3920,1),(3920,4),(9800,1),(9800,4),(980,1),(980,4)]
for M,flag in jobs:
    t0=time.time()
    P(f"mf=mfinit([{M},2],{flag}); dm=mfdim(mf); B=mfsturm(mf)+50; C=intmat(mfcoefs(mf,B)); v=concat(0,ellan(Xi,B))~; w=concat(0,ellan(E,B))~")
    rC=P("matrank(C*Mod(1,p))"); rv=P("matrank(matconcat([C,v])*Mod(1,p))"); rw=P("matrank(matconcat([C,w])*Mod(1,p))")
    sp={1:"S_2",4:"M_2"}[flag]
    print(f"level {M}, {sp}: dim {P('dm')}, rows n=0..{P('B')}, rank_p C = {rC}, rank_p [C|f_Xi] = {rv} -> {'f_Xi NOT in space (PROVED)' if int(rv)==int(P('dm'))+1 else 'undetermined by this test'}; control 49a1: rank_p [C|w] = {rw} ({'49a1 consistent with space' if int(rw)==int(rC) else '49a1 NOT in space'}); {time.time()-t0:.0f}s", flush=True)
