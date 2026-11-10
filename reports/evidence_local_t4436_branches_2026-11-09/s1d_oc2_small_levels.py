# Local-derived (t4436, branch Oc-2). Continuation of block [5] of s1b_oc_branches.py (kept on disk): s1b completed level 196 for every
# admissible character and then stalled >10 min on mfinit([196,3/2,-8]) (a character whose conductor 8 does not divide 196) and was
# killed at ~22:08 CST. Here only characters whose conductor divides N are used.
# Test: dimension of the common eigenspace in S_{3/2}(Gamma0(N), chi_D) of T(p^2), p in {11,37,53,71}, with eigenvalue chi_140(p) a_p(49a1)
# (= a_p(Xi); chi_140(p) = -1 and a_p != 0 for these p). Zero => no Oc-2 vector at that level/character. Same for eigenvalue a_p(49a1).
import cypari2, time; pari=cypari2.Pari(); pari.allocatemem(2*10**9)
P=lambda s: pari(s)
P("E=ellinit([1,-1,0,-2,-1]); af=ellan(E,100)")
for N,Ds in [(392,[1,-4,8,-8,-7,28,-56,56]),(784,[1,-4,8,-8,-7,28,-56,56])]:
    for D in Ds:
        t0=time.time()
        try:
            P(f"mm=mfinit([{N},3/2,{D}],1); dd=mfdim(mm)")
        except cypari2.PariError as e:
            print(f"level {N}, char {D}: mfinit error {str(e)[:80]}", flush=True); continue
        if int(P("dd"))==0:
            print(f"level {N}, char {D}: dim 0", flush=True); continue
        P("V=matid(dd); foreach([11,37,53,71],p, my(M=mfheckemat(mm,p^2)); if(#V, V=V*matker((M-kronecker(140,p)*af[p]*matid(dd))*V)))")
        P("V2=matid(dd); foreach([11,37,53,71],p, my(M=mfheckemat(mm,p^2)); if(#V2, V2=V2*matker((M-af[p]*matid(dd))*V2)))")
        print(f"level {N}, char {D}: dim S = {P('dd')}; common eigenspace for a_p(Xi) = {P('#V')}; for a_p(49a1) = {P('#V2')}; {time.time()-t0:.0f}s", flush=True)
