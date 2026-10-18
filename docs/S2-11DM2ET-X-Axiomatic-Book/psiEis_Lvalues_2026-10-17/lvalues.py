# (B) Hecke L-values of all 96 characters of Cl_m^+ (m = p2^3 p5 p7 oo1 oo2) via PARI lfun:
#   L_m(s,chi) = L(s,chi_prim) * prod_{P | m, P not | f_chi} (1 - chi_prim(P) NP^{-s})
from fractions import Fraction as fr
import cypari2, itertools, pickle, cmath, math
pari=cypari2.Pari(); pari.allocatemem(2*10**9); pari.set_real_precision(38)
gp=lambda s: pari(s)
gp('bnf=bnfinit(y^2-35,1); P2=idealprimedec(bnf,2)[1]; P5=idealprimedec(bnf,5)[1]; P7=idealprimedec(bnf,7)[1]')
gp('m=idealmul(bnf,idealmul(bnf,idealpow(bnf,P2,3),P5),P7); bnr=bnrinit(bnf,[m,[1,1]],1)')
cyc=[int(c) for c in gp('bnr.cyc')]
chars=list(itertools.product(*[range(c) for c in cyc]))
res={}
for chi in chars:
    v=list(chi)
    gp(f'chi={v}; C=bnrconductor(bnr,chi); bC=bnrinit(bnf,C,1); Mp=bnrmap(bnr,bC); L=lfuncreate([bnr,chi])')
    cycC=[int(t) for t in gp('bC.cyc')]; Mp=[[int(gp(f'Mp[1][{k+1},{i+1}]')) for i in range(len(cyc))] for k in range(len(cycC))]
    chiC=None
    for cand in itertools.product(*[range(c) for c in cycC]):
        ok=True
        for i in range(len(cyc)):
            lhs=fr(chi[i],cyc[i]); rhs=sum(fr(cand[k]*Mp[k][i],cycC[k]) for k in range(len(cycC)))
            if (lhs-rhs)%1!=0: ok=False;break
        if ok: chiC=cand;break
    assert chiC is not None
    fac0=1; fach=1
    for P in ("P2","P5","P7"):
        if int(gp(f'idealval(bnf,C[1],{P})'))==0:
            c=[int(t) for t in gp(f'bnrisprincipal(bC,{P},0)')]
            val=cmath.exp(2j*math.pi*float(sum(fr(chiC[k]*c[k],cycC[k]) for k in range(len(cycC)))))
            NP=int(gp(f'idealnorm(bnf,{P})'))
            fac0*=(1-val); fach*=(1-val*NP**-0.5)
    L0=complex(gp('lfun(L,0)'))
    rec=dict(cond_norm=int(gp('idealnorm(bnf,C[1])')),cond_inf=[int(t) for t in gp('C[2]')],L0prim=L0,L0=L0*fac0,fac0=fac0)
    if chi[0]%2==1 and chi[2]==1:
        Lh=complex(gp('lfun(L,1/2)')); rec.update(Lhalf_prim=Lh,Lhalf=Lh*fach, Lone=complex(gp('lfun(L,1)')),
             rootno=complex(gp('lfunrootres(L)[3]')))
    res[chi]=rec
    print(chi,rec['cond_norm'],rec['L0'],flush=True)
pickle.dump(dict(cyc=cyc,res=res),open("lvalues.pkl","wb"))
out=["Hecke L-values over Q(sqrt35), characters of Cl_m^+ = Z/24 x Z/2 x Z/2 (m = p2^3 p5 p7 oo oo); PARI lfun, 38 digits"]
out.append("Cusp characters chi=(j,l,1), j odd: conductor, root number, L(1/2,chi) (primitive = Hecke L of the Maass newform u_chi), L(1,chi):")
for chi in chars:
    r=res[chi]
    if 'Lhalf' in r:
        out.append(f"  chi{chi}: cond N={r['cond_norm']} inf={r['cond_inf']} eps={r['rootno']:.6f}  L(1/2)={r['Lhalf_prim']:.15f}  L(0)={r['L0prim']:.3e}  L(1)={r['Lone']:.12f}")
nz=[(chi,res[chi]['L0']) for chi in chars if abs(res[chi]['L0'])>1e-20]
out.append(f"characters with L_m(0,chi) != 0: {len(nz)}")
open("lvalues.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
