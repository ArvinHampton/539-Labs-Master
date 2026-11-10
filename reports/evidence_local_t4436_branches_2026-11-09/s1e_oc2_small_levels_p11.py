# Local-derived (t4436, branch Oc-2). SUPERSEDES s1d_oc2_small_levels.py (kept on disk): s1d used T(p^2) for p up to 71 and spent >5 min on
# the first level-392 space without output; killed ~22:15 CST. Here: T(11^2) first (chi_140(11) = -1, a_11(49a1) = 4, so a_11(Xi) = -4);
# T(37^2) only if the -4 eigenspace of T(121) is nonzero. dim 0 => no Oc-2 vector at that level and character.
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
        P("M11=mfheckemat(mm,121); V=matker(M11+4*matid(dd)); V2=matker(M11-4*matid(dd))")
        extra=""
        if int(P("#V"))>0:
            P("M37=mfheckemat(mm,37^2); V=V*matker((M37-6*matid(dd))*V)"); extra=f" -> after T(37^2) (a_37(Xi)=+6): {P('#V')}"
        print(f"level {N}, char {D}: dim S = {P('dd')}; T(121) eigenspace for a_11(Xi) = -4: {P('#matker(M11+4*matid(dd))')}{extra}; for a_11(49a1) = +4: {P('#V2')}; {time.time()-t0:.0f}s", flush=True)
