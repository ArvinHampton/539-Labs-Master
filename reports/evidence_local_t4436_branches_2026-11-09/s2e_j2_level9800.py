# Local-derived (t4436, branch J-2), written by the t4407/t4429 Local stream at the parent's request. NEW script; s2c/s2d and their logs are kept untouched.
# Reruns s2d_j2_level9800_capped.py's computation (same rank method, same prime, same rows B = Sturm+50) at level 9800 for S_2 then M_2,
# with a ~5.5 GB PARI stack, started only after ob_v3 (other stream) closed so the jobs do not compete for memory.
# Test: f_Xi = newform of Xi = elltwist(49a1,140) (conductor 19600). If rank_p [C | a(f_Xi)] = dim + 1 then the coefficient vector of f_Xi is not in the
# Q-span of the space's q-expansions (rank mod p <= rank over Q), so f_Xi is NOT in the space. Control: 49a1 (level 49 | 9800) must be consistent.
import cypari2, time; pari=cypari2.Pari(); pari.allocatemem(int(5.5*10**9))
P=lambda s: pari(s)
T0=time.time()
P("E=ellinit([1,-1,0,-2,-1]); Xi=ellinit(elltwist(E,140)); p=nextprime(2^61)")
print("Xi conductor:",P("ellglobalred(Xi)[1]"),flush=True)
P("intmat(C)=my(D=matrix(#C[,1],#C,i,j,0)); for(j=1,#C, my(c=C[,j], d=denominator(c)); for(i=1,#c, D[i,j]=c[i]*d)); D")
for M,flag in [(9800,1),(9800,4)]:
    t0=time.time()
    try:
        P(f"mf=mfinit([{M},2],{flag}); dm=mfdim(mf); B=mfsturm(mf)+50; C=intmat(mfcoefs(mf,B)); v=concat(0,ellan(Xi,B))~; w=concat(0,ellan(E,B))~")
        sp={1:"S_2",4:"M_2"}[flag]
        print(f" level {M} {sp}: mfinit+coefs done, dim {P('dm')}, B={P('B')} [{time.time()-t0:.0f}s]",flush=True)
        rC=P("matrank(C*Mod(1,p))"); rv=P("matrank(matconcat([C,v])*Mod(1,p))"); rw=P("matrank(matconcat([C,w])*Mod(1,p))")
        print(f"level {M}, {sp}: dim {P('dm')}, rows n=0..{P('B')}, rank_p C = {rC}, rank_p [C|f_Xi] = {rv} -> {'f_Xi NOT in space' if int(rv)==int(P('dm'))+1 else 'undetermined by this test'}; control 49a1: rank_p [C|w] = {rw} ({'49a1 consistent with space' if int(rw)==int(rC) else '49a1 NOT in space'}); {time.time()-t0:.0f}s", flush=True)
        P("kill(mf); kill(C)")
    except cypari2.PariError as e:
        print(f"level {M} flag {flag}: PARI error {e} [{time.time()-t0:.0f}s]",flush=True)
print("elapsed %.0fs"%(time.time()-T0))
