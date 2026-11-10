# Local-derived. t4407 O-b, stage 1: Shimura preimage of g := f (x) chi_-4 (f=49a1; conductor 784) in weight 3/2.
# Route: Xi's eigen-system a_p(f_Xi) = chi_-20(p) a_p(f) = chi_5(p) * [chi_-4(p) a_p(f)].  chi_140 and chi_-20 are NOT squares of Dirichlet
# characters (their 2-adic part chi_-4 is odd), so Xi's form is not a character twist of the level-196 packet; but chi_5 = psi5^2 with
# psi5 of order 4 mod 5, so H := G (x) psi5 has T(p^2)-eigenvalues chi_5(p) lambda_p(G) (Shimura 1973, twisting lemma).
# Stage 1 finds G: T(p^2) G = chi_-4(p) a_p(f) G in S_{3/2}(Gamma0(4N), chi_D), 2N divisible by 784.
import cypari2, time, sys; pari=cypari2.Pari(); pari.allocatemem(6*10**9); P=pari
t0=time.time()
P("E=ellinit([1,-1,0,-2,-1]); Em4=ellinit(elltwist(E,-4)); af=ellan(E,500); ag=vector(500,n,kronecker(-4,n)*af[n])")
print("conductor of 49a1 (x) chi_-4:", P("ellglobalred(Em4)[1]"), "; a_n(Em4)==chi_-4(n)a_n(f) n<=500:", P("ellan(Em4,500)==ag"), flush=True)
for N in [1568, 3136]:
    for D in [1,-4,8,-8,-7,28,-56,56]:
        try:
            dd=P(f"mfdim([{N},3/2,{D}],1)")
        except cypari2.PariError as e:
            print(f" N={N} D={D}: dim err {e}",flush=True); continue
        print(f" N={N} D={D}: dim S_3/2 = {dd}  t={time.time()-t0:.0f}s",flush=True)
sys.stdout.flush()
for N in [1568, 3136]:
    for D in [1,-4,8,-8,-7,28,-56,56]:
        if int(P(f"mfdim([{N},3/2,{D}],1)"))==0: continue
        t1=time.time()
        try:
            P(f"m=mfinit([{N},3/2,{D}],1); d=mfdim(m); K=matid(d)")
            for p in [3,5,11]:
                P(f"Mh=mfheckemat(m,{p}^2); K=K*matker((Mh-ag[{p}]*matid(d))*K)")
                if int(P("#K"))==0: break
            print(f" N={N} D={D}: dim {P('d')}, joint kernel (T(p^2)=chi_-4(p)a_p(f), p=3,5,11) dim = {P('#K')}  [{time.time()-t1:.0f}s]",flush=True)
            if int(P("#K"))>0:
                P(f"write(\"ob_v1_found_N{N}_D{D}.gp\", [ {N}, {D}, K, mfcoefs(mfbasis(m)[1],1)*0 ])")
        except cypari2.PariError as e:
            print(f" N={N} D={D}: err {e}",flush=True)
print("elapsed %.0fs"%(time.time()-t0))
