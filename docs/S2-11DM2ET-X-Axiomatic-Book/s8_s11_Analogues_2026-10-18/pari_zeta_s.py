# Independent (Hecke L-function) check of step 3: partial narrow-ray-class zeta values of the E_s ideal set at w=0,-1, residue at w=1.
#   zeta_m(w,C) = (1/|G|) sum_chi conj(chi(C)) L_m(w,chi),  L_m(w,chi) = L(w,chi_prim) prod_{P|m}(1 - a_{NP}(chi_prim) NP^-w)
#   (every P | m is the unique ideal of its norm here, so a_{NP}=chi_prim(P)).  zeta_E(w) = kappa^w * sum_{a in E} N(a)^-w.
import cypari2, numpy as np, itertools, cmath
from fractions import Fraction as Fr
pari=cypari2.Pari(); pari.allocatemem(2*10**9); pari.set_real_precision(38)
CFG={7:(35,1,[(2,1),(5,1)],20),8:(3,4,[(2,2),(3,1)],3),11:(11,3,[(2,1),(3,2)],36)}
out=[]
for s,(D0,c,pe,kappa) in CFG.items():
    d=2*(s-2); K=pari(f'bnfinit(x^2-{D0},1)'); w=pari('Mod(x,x^2-%d)'%D0)
    a=(Fr(s,2*(s-2)),Fr(-1,s-2)); X0=(int(d*a[0]),int(d*a[1])); beta=lambda X1,X2:(2*X1+s*X2)+c*X2*w
    Dp=pari.idealhnf(K,beta(*X0))
    for gg in (beta(d,0),beta(0,d)): Dp=pari.idealadd(K,Dp,gg)
    mod=pari.idealhnf(K,1); Ps=[]
    for p,e in pe:
        for P in pari.idealprimedec(K,p): Ps.append(P); mod=pari.idealmul(K,mod,pari.idealpow(K,P,e))
    bnr=pari.bnrinit(K,[mod,[1,1]],1); cyc=[int(m) for m in pari('(b)->b.cyc')(bnr)]; G=int(pari('(b)->b.no')(bnr))
    g=np.array([[-1,-s],[2,2*s-1]]); gr=g@np.array((1,0)); hits={}
    for n in range(-40,41):
        for k in range(0,41):
            X1=d*n+X0[0]; X2=d*k+X0[1]
            if not ((X1*gr[1]-X2*gr[0])>0 and X2>=0): continue
            J=pari.idealdiv(K,beta(X1,X2),Dp); cp=1; Jp=J
            for P in Ps:
                v=int(pari.idealval(K,J,P))
                if v: cp*=int(pari.idealnorm(K,P))**v; Jp=pari.idealdiv(K,Jp,pari.idealpow(K,P,v))
            hits.setdefault(cp,set()).add(tuple(int(z) for z in pari.bnrisprincipal(bnr,Jp,0)))
    NPs=[int(pari.idealnorm(K,P)) for P in Ps]
    Lm={0:{},-1:{}}
    for chi in itertools.product(*[range(m) for m in cyc]):
        L=pari.lfuncreate([bnr,list(chi)]); an=pari.lfunan(L,max(NPs))
        for w0 in (0,-1):
            v=complex(pari.lfun(L,w0))
            for NP in NPs: v*=1-complex(an[NP-1])*NP**(-w0)
            Lm[w0][chi]=v
    def zpart(w0,cl):
        return sum(cmath.exp(-2j*cmath.pi*sum(x*y/m for x,y,m in zip(chi,cl,cyc)))*v for chi,v in Lm[w0].items())/G
    tot={}
    for w0 in (0,-1):
        tot[w0]=sum(cp**(-w0)*zpart(w0,cl) for cp,S in hits.items() for cl in S)*kappa**w0
    zK=pari.lfuncreate(pari(f'x^2-{D0}')); res=complex(pari.lfunres(zK)) if False else None
    hR=float(pari('(K)->K.reg')(K))*int(pari('(K)->K.no')(K)); dK=abs(int(pari('(K)->K.disc')(K)))
    resK=2*hR/dK**0.5; ncl=sum(len(S) for S in hits.values())
    corr=1.0
    for NP in NPs: corr*=1-1/NP
    resE=resK*corr/G*sum(len(S)/cp for cp,S in hits.items())*kappa  # Res_{w=1} kappa^w sum N a^-w
    out.append(f"s={s}: m={pe} (exponent per prime above p) * oo1 oo2, |Cl_m^+|={G} cyc={cyc}; E-set = "+"; ".join(f"N(c)={cp}: {len(S)} class(es)" for cp,S in hits.items()))
    out.append(f"   zeta_E(0) = {tot[0].real:.15f} (imag {abs(tot[0].imag):.1e}),  zeta_E(-1) = {tot[-1].real:.15f} (imag {abs(tot[-1].imag):.1e}),  Res_(w=1) zeta_E = {resE:.15f}")
    print("\n".join(out[-2:]),flush=True)
open("pari_zeta_s.txt","w").write("\n".join(out)+"\n")
