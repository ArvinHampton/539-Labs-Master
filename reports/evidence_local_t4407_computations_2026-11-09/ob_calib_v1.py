# Local-derived. t4407 O-b calibration (cheap): at which 2-power level does the weight-3/2 Shimura preimage of E (x) chi_-4 first appear,
# for curves E with GOOD reduction at 2 (like 49a1)? Searches S_{3/2}(Gamma0(2^a * N_odd), chi_D), all PARI-admissible quadratic D,
# for the joint kernel of T(p^2) - chi_-4(p) a_p(E), p in first three odd primes not dividing the level.
import cypari2, time; pari=cypari2.Pari(); pari.allocatemem(2*10**9); P=pari
t0=time.time()
for lab,ainv,Nodd in [("11a1","[0,-1,1,-10,-20]",11),("15a1","[1,1,1,-10,-10]",15),("49a1","[1,-1,0,-2,-1]",49)]:
    P(f"E=ellinit({ainv}); Et=ellinit(elltwist(E,-4)); ag=vector(400,n,kronecker(-4,n)*ellan(E,400)[n])")
    print(f"{lab}: conductor of twist by -4 =",P("ellglobalred(Et)[1]"),flush=True)
    ps=[p for p in [3,5,7,11,13,17,19,23] if Nodd%p!=0][:3]
    for a in [5,6,7,8]:
        N=2**a*Nodd
        if N>6272: continue
        if lab=="49a1" and N in (1568,3136,6272): continue   # done in ob_v1 / ob_v2
        Ds=[D for D in [1,-4,8,-8]+[D0*s for D0 in [Nodd] for s in [1,-1,-4,4,8,-8,-1*8]] if N%abs(D if D%4 in (0,1) else 4*D)==0 or True]
        for D in sorted(set([1,8,-4,-8,Nodd,-Nodd,4*Nodd,-4*Nodd,8*Nodd,-8*Nodd])):
            try:
                if int(P(f"kronecker({D},1)"))!=1: continue
                dd=int(P(f"mfdim([{N},3/2,{D}],1)"))
            except cypari2.PariError: continue
            if dd==0: continue
            t1=time.time()
            P(f"m=mfinit([{N},3/2,{D}],1); d=mfdim(m); K=matid(d)")
            for p in ps:
                P(f"Mh=mfheckemat(m,{p}^2); K=K*matker((Mh-ag[{p}]*matid(d))*K)")
                if int(P("#K"))==0: break
            print(f"  {lab}: N={N}=2^{a}*{Nodd}, D={D}: dim {dd}, joint kernel dim = {P('#K')} [{time.time()-t1:.0f}s]",flush=True)
print("elapsed %.0fs"%(time.time()-t0))
