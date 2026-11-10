# Local-derived (t4436, branch J-2). Citation-free check that f_Xi := sum a_n(Xi) q^n (a_n from the curve Xi = elltwist(49a1,140))
# lies in NO S_2(Gamma0(M)) and NO M_2(Gamma0(M)) for the maximal proper divisors M of 19600 = 2^4 5^2 7^2: M in {9800, 3920, 2800}.
# Every proper divisor M' of 19600 divides one of these, and S_2(Gamma0(M')) is contained in S_2(Gamma0(M)) when M'|M, so this covers all
# proper divisors. Method (as PP pp_2g_980): if f_Xi were in the space, its first B coefficients would be a linear combination of the
# basis' first B coefficients; mftobasis(mf, v, 1) returns [] when the linear system on the given coefficients has no solution.
# A "no solution" answer on finitely many coefficients is a proof of non-membership (no Sturm bound or newform theory needed).
# Membership at 19600 itself is PP 2050 V7 (PROVED). Together: f_Xi lies in S_2(Gamma0(N)) for N=19600 and for no proper divisor of 19600.
import cypari2, time; pari=cypari2.Pari(); pari.allocatemem(8*10**9)
P=lambda s: pari(s)
P("Xi=ellinit(elltwist(ellinit([1,-1,0,-2,-1]),140)); print(\"Xi conductor \", ellglobalred(Xi)[1])")
for M in [2800,3920,9800]:
    for space,flag in [("S_2",1),("M_2",4)]:
        t0=time.time()
        P(f"mf=mfinit([{M},2],{flag}); dm=mfdim(mf); B=mfsturm(mf)+50; v=ellan(Xi,B); v=concat(0,v); sol=mftobasis(mf,v~,1)")
        print(f"level {M}, {space}: dim {P('dm')}, coefficients used n<= {P('B')}, mftobasis solution: {P('if(#sol==0,\"NONE (f_Xi not in space)\",sol)')}, time {time.time()-t0:.0f}s", flush=True)
