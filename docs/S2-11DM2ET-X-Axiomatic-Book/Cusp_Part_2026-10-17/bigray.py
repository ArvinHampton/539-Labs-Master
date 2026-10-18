# Ray class groups Cl_m^+ for larger moduli m | 2^k p5 p7 oo1 oo2; sigma action; Maass-type (pure infinity type) non-sigma-invariant characters
import cypari2, itertools
pari=cypari2.Pari(); pari.allocatemem(10**9); gp=lambda s: pari(s)
gp('bnf=bnfinit(y^2-35,1); P2=idealprimedec(bnf,2)[1]; P5=idealprimedec(bnf,5)[1]; P7=idealprimedec(bnf,7)[1]')
gp('sig(I)=nfgaloisapply(bnf,-y,I)')
out=[]
for name,mod in [("p2 p5 p7","idealmul(bnf,idealmul(bnf,P2,P5),P7)"),("p2^2 p5 p7","idealmul(bnf,idealmul(bnf,idealpow(bnf,P2,2),P5),P7)"),("p2^3 p5 p7","idealmul(bnf,idealmul(bnf,idealpow(bnf,P2,3),P5),P7)"),("p2 p5 p7^2","idealmul(bnf,idealmul(bnf,P2,P5),idealpow(bnf,P7,2))"),("p2 p5^2 p7","idealmul(bnf,idealmul(bnf,P2,idealpow(bnf,P5,2)),P7)")]:
    gp(f'm={mod}; bnr=bnrinit(bnf,[m,[1,1]],1); cyc=bnr.cyc; gens=bnr.gen')
    cyc=[int(c) for c in gp('cyc')]
    # sign classes: principal ideals (1+t*N) with prescribed signs, N=norm generator in m (use element of m)
    gp('mm=idealhnf(bnf,m); e=nfbasistoalg(bnf,mm[,1]); e2=nfbasistoalg(bnf,mm[,2]); ')
    # find x in 1+m with signs (+,-) and (-,+)
    gp('findsig(s1,s2)=for(a=-60,60,for(b=-60,60, my(x=1+a*e+b*e2, v=nfeltembed(bnf,x)); if(sign(v[1])==s1 && sign(v[2])==s2, return(bnrisprincipal(bnr,idealhnf(bnf,x),0))))); error("nf")')
    cpm=[int(t) for t in gp('findsig(1,-1)')]; cmp_=[int(t) for t in gp('findsig(-1,1)')]
    sg=[[int(t) for t in gp(f'bnrisprincipal(bnr,sig(gens[{i+1}]),0)')] for i in range(len(cyc))]
    from fractions import Fraction as Fr
    def val(chi,c): return sum(Fr(chi[i]*c[i],cyc[i]) for i in range(len(cyc)))%1
    tot=0; maass=[]; mixed=0
    for chi in itertools.product(*[range(c) for c in cyc]):
        t1=val(chi,cmp_)  # chi on c(-,+): 0 or 1/2
        t2=val(chi,cpm)
        typ=(int(t1*2),int(t2*2))
        # chi o sigma (c) = chi(sigma c)
        inv=all(val(chi,sg[i])==val(chi,[1 if k==i else 0 for k in range(len(cyc))]) for i in range(len(cyc)))
        if inv: continue
        tot+=1
        if typ[0]==typ[1]: maass.append((chi,typ))
        else: mixed+=1
    out.append(f"m={name}: Cl_m^+ = {cyc}; non-sigma-invariant chars: {tot}; pure type (Maass, lambda=1/4): {len(maass)}; mixed (weight-1 holo): {mixed}")
    out.append(f"   Maass chars (exponent vectors, type): {maass[:40]}")
print("\n".join(out)); open("bigray.txt","w").write("\n".join(out)+"\n")
