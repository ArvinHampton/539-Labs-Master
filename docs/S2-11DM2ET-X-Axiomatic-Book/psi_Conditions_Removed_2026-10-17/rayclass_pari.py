# Exact ray-class data (PARI/GP via cypari2) for K=Q(sqrt35), modulus p2*p5*oo1*oo2. Output: rayclass_pari.txt
import cypari2
pari=cypari2.Pari(); gp=lambda s: pari(s)
gp('bnf=bnfinit(y^2-35,1); P2=idealprimedec(bnf,2)[1]; P5=idealprimedec(bnf,5)[1]; f=idealmul(bnf,P2,P5); bnr=bnrinit(bnf,[f,[1,1]],1)')
L=[f"Cl(K)={gp('bnf.cyc')}  narrow Cl^+(K)={gp('bnrinit(bnf,[1,[1,1]]).cyc')}  fu={gp('bnf.fu')}  bnfcertify={gp('bnfcertify(bnf)')}",
f"Cl_f^+ (f=p2 p5, both oo) cyc={gp('bnr.cyc')} order={gp('bnr.no')}",
f"sigma(g1)={gp('bnrisprincipal(bnr,nfgaloisapply(bnf,-y,bnr.gen[1]),0)')}  sigma(g2)={gp('bnrisprincipal(bnr,nfgaloisapply(bnf,-y,bnr.gen[2]),0)')}",
f"classes: primes over 13 = {gp('[bnrisprincipal(bnr,idealprimedec(bnf,13)[1],0), bnrisprincipal(bnr,idealprimedec(bnf,13)[2],0)]')}, p7 = {gp('bnrisprincipal(bnr,idealprimedec(bnf,7)[1],0)')}"]
open("rayclass_pari.txt","w").write("\n".join(L)+"\n"); print("\n".join(L))
