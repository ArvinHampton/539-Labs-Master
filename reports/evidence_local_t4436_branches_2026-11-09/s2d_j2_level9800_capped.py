# Local-derived (t4436, branch J-2). Continuation of s2c_j2_minimal_level_rank.py (kept on disk; it finished levels 2800 and 3920 and was
# OOM-killed by the kernel at level 9800 while another stream's job was also running). Same rank method, level 9800 only (S_2 then M_2),
# run under a hard virtual-memory cap (ulimit -v) with a 2.5 GB PARI stack so that it fails cleanly instead of pressuring other jobs.
import cypari2, time; pari=cypari2.Pari(); pari.allocatemem(int(2.5*10**9))
P=lambda s: pari(s)
P("E=ellinit([1,-1,0,-2,-1]); Xi=ellinit(elltwist(E,140)); p=nextprime(2^61)")
P("intmat(C)=my(D=matrix(#C[,1],#C,i,j,0)); for(j=1,#C, my(c=C[,j], d=denominator(c)); for(i=1,#c, D[i,j]=c[i]*d)); D")
for M,flag in [(9800,1),(9800,4)]:
    t0=time.time()
    P(f"mf=mfinit([{M},2],{flag}); dm=mfdim(mf); B=mfsturm(mf)+50; C=intmat(mfcoefs(mf,B)); v=concat(0,ellan(Xi,B))~; w=concat(0,ellan(E,B))~")
    rC=P("matrank(C*Mod(1,p))"); rv=P("matrank(matconcat([C,v])*Mod(1,p))"); rw=P("matrank(matconcat([C,w])*Mod(1,p))")
    sp={1:"S_2",4:"M_2"}[flag]
    print(f"level {M}, {sp}: dim {P('dm')}, rows n=0..{P('B')}, rank_p C = {rC}, rank_p [C|f_Xi] = {rv} -> {'f_Xi NOT in space (PROVED)' if int(rv)==int(P('dm'))+1 else 'undetermined by this test'}; control 49a1: rank_p [C|w] = {rw} ({'49a1 consistent with space' if int(rw)==int(rC) else '49a1 NOT in space'}); {time.time()-t0:.0f}s", flush=True)
    P("kill(mf); kill(C)")
