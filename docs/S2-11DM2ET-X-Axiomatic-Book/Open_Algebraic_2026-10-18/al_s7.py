# (d) s=7 cusp ray-class characters: global root numbers (PARI lfunrootres) and local data at ramified primes.
import cypari2, pickle, json
pari=cypari2.Pari(); pari.allocatemem(2*10**9); gp=lambda s: pari(s)
gp('bnf=bnfinit(y^2-35,1); P2=idealprimedec(bnf,2)[1]; P5=idealprimedec(bnf,5)[1]; P7=idealprimedec(bnf,7)[1]')
gp('m=idealmul(bnf,idealmul(bnf,idealpow(bnf,P2,3),P5),P7); bnr=bnrinit(bnf,[m,[1,1]],1)')
ch=pickle.load(open('../2026-10-17-cusp-part/cusp_chars.pkl','rb'))
out=[]
for c in ch:
    chi=list(c[0]); r={"chi":chi,"cond_norm":c[1],"inf":c[2]}
    cond=gp(f'bnrconductor(bnr,{chi})')
    r["cond_exps"]={str(p):int(gp(f'idealval(bnf,bnrconductor(bnr,{chi})[1],P{p})')) for p in (2,5,7)}
    try:
        L=gp(f'lfuncreate([bnr,{chi}])'); rr=pari.lfunrootres(L)
        w=complex(rr[2]); r["root_number"]=[round(w.real,8),round(w.imag,8)]
    except Exception as e: r["root_number_error"]=str(e)[:200]
    print(r,flush=True); out.append(r)
json.dump(out,open("al_s7.json","w"),indent=1)
