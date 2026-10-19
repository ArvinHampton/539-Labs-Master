# Local root numbers eps_v(1/2, chi_v, psi_v) of the 24 s=7 cusp Hecke characters of K=Q(sqrt35),
# conductor P2^2 P5 P7, via explicit local Gauss sums (Tate, "Number theoretic background", Corvallis 1979, §3.2):
#   ramified chi_v, conductor exponent a, psi_v of conductor exponent n(psi_v)=d (trivial on P^-d, not on P^-d-1),
#   dx self-dual for psi_v:  eps(chi_v|.|^{1/2},psi_v,dx) = chi_v(c) * N(P)^{-a/2} * sum_{u in (O/P^a)^x} chi_v^{-1}(u) psi_v(u/c),
#   with v_P(c) = a+d.   Real place: eps(sgn^N, x->e(x)) = i^N.   Unramified v: eps = 1.
# Global additive character psi = psi_Q o Tr_{K/Q}, psi_Q = prod_v psi_{Q,v}, trivial on Q:
#   convention A: psi_inf(x)=e(x),  psi_p(x)=e(-{x}_p);   convention B: complex conjugate of A.
# Since psi_P = psi_p o Tr_{K_P/Q_p}, its conductor is the inverse different: d = v_P(different) (=2,1,1 at P2,P5,P7).
import cypari2, pickle, json, sys, math, itertools, cmath
from fractions import Fraction as Fr
pari=cypari2.Pari(); pari.allocatemem(2*10**9); gp=lambda s: pari(s)
pari.set_real_precision(60)
gp('bnf=bnfinit(y^2-35,1); P2=idealprimedec(bnf,2)[1]; P5=idealprimedec(bnf,5)[1]; P7=idealprimedec(bnf,7)[1]')
gp('m=idealmul(bnf,idealmul(bnf,idealpow(bnf,P2,3),P5),P7); bnr=bnrinit(bnf,[m,[1,1]],1)')
NZ=840; gp(f'Phi=polcyclo({NZ},x); z=Mod(x,Phi)')
def E(t):  # exact e(t) in Q(zeta_840), t a Fraction
    k=t*NZ; assert k.denominator==1, t; return f'z^{int(k)%NZ}'
cyc=[int(t) for t in gp('bnr.cyc')]
assert cyc==[24,2,2]
ch=pickle.load(open('../2026-10-17-cusp-part/cusp_chars.pkl','rb'))
alj=json.load(open('../2026-10-18-Open-Algebraic/al_s7.json'))
Pname={2:'P2',5:'P5',7:'P7'}
dval={p:int(gp(f'idealval(bnf,idealhnf(bnf,nfinit(y^2-35).diff),{Pname[p]})')) for p in (2,5,7)}
assert dval=={2:2,5:1,7:1}, dval
# exact square roots in Q(zeta_840)
gp('z5=z^168; z7=z^120; Iz=z^210; g5=sum(a=1,4,kronecker(a,5)*z5^a); g7=sum(a=1,6,kronecker(a,7)*z7^a)')
gp('s5=g5; s7=-Iz*g7'); assert gp('s5^2==5 && s7^2==7')
assert abs(float(gp('real(subst(lift(s5),x,exp(2*Pi*sqrt(-1)/840)))'))-5**.5)<1e-30
assert abs(float(gp('real(subst(lift(s7),x,exp(2*Pi*sqrt(-1)/840)))'))-7**.5)<1e-30
SQ={2:'2',5:'s5',7:'s7'}   # sqrt(N(P)^a) with a=2,1,1
def vge(x,P,k):
    return bool(gp(f'my(t={x}); t==0 || nfeltval(bnf,t,{P})>={k}'))
def ppart_frac(r,p):  # {r}_p in [0,1)
    r=Fr(r); B=r.denominator; k=0
    while B%p==0: B//=p; k+=1
    if k==0: return Fr(0)
    pk=p**k; return Fr((r.numerator*pow(B,-1,pk))%pk, pk)
def chi_ideal(chi,ideal):  # psi(ideal) in turns, ideal coprime to m
    return Fr(str(gp(f'chareval(bnr,{chi},{ideal})')))
def cond_other(p,aexp):
    # factorisation matrix of modulus for the chinese remainder: P^e at p, Q^{a_Q} elsewhere (we use the full modulus exponents 3,1,1 there)
    rows=[]
    for q in (2,5,7):
        e = aexp if q==p else {2:3,5:1,7:1}[q]
        rows.append(f'{Pname[q]},{e}')
    return '['+';'.join(rows)+']'
results=[]
EX={}
gens_report={}
for idx,c in enumerate(ch):
    chi=list(c[0]); chis=str(chi)
    cond=gp(f'bnrconductor(bnr,{chis})')
    a={p:int(gp(f'idealval(bnf,bnrconductor(bnr,{chis})[1],{Pname[p]})')) for p in (2,5,7)}
    Ninf=[int(t) for t in gp(f'bnrconductor(bnr,{chis})[2]')]
    assert a=={2:2,5:1,7:1}
    rec={'chi':chi,'inf':Ninf,'a':a,'d':dval,'local':{}}
    for p in (2,5,7):
        P=Pname[p]; ap=a[p]; dp=dval[p]; Pa=f'idealpow(bnf,{P},{ap})'
        G=gp(f'G=idealstar(bnf,{Pa},2)'); gcyc=[int(t) for t in gp('G.cyc')]; gens=gp('G.gen')
        gens_report[P+f'^{ap}']={'cyc':gcyc,'gen':[str(gp(f'nfbasistoalg(bnf,G.gen[{i+1}])')) for i in range(len(gcyc))]}
        # enumerate (O/P^a)^x
        units=[]
        for ex in itertools.product(*[range(n) for n in gcyc]):
            s='1'
            for i,e in enumerate(ex): s=f'nfeltmul(bnf,{s},nfeltpow(bnf,G.gen[{i+1}],{e}))'
            units.append(gp(f'nfeltreduce(bnf,{s},{Pa})'))
        Nq=int(gp(f'idealnorm(bnf,{P})'))
        assert len(units)==Nq**ap-Nq**(ap-1)
        assert len({str(u) for u in units})==len(units)
        # chi_P on units: alpha = u mod P^a, = 1 mod other conductor primes (to full modulus exps), totally positive
        def chiP_unit(u):
            ys=[]
            for q in (2,5,7): ys.append(str(u) if q==p else '1')
            al=gp(f'al=idealchinese(bnf,[{cond_other(p,ap)},[1,1]],[{",".join(ys)}])')
            assert gp('nfeltsign(bnf,al)')==gp('[1,1]')
            assert vge(f'nfeltadd(bnf,al,nfeltmul(bnf,-1,{u}))',P,ap)
            for q in (2,5,7):
                if q!=p: assert vge('nfeltadd(bnf,al,-1)',Pname[q],{2:3,5:1,7:1}[q])
            return (-chi_ideal(chis,'idealhnf(bnf,al)'))%1
        # c: v_P(c)=a+d exactly, c=1 mod other primes, totally positive
        t0={2:'4',5:'5',7:'7'}[p]; ev=ap+dp
        assert int(gp(f'nfeltval(bnf,{t0},{P})'))==ev
        def chiP_of_c(cc):
            # (cc) = P^{ev} * b, chi_P(cc) = psi(b)^{-1}
            b=f'idealdiv(bnf,idealhnf(bnf,{cc}),idealpow(bnf,{P},{ev}))'
            return (-chi_ideal(chis,b))%1
        def gauss_eps(cc,conv):
            # returns exact eps (polmod in z) and turns of chi_P(c)
            sgn = 1 if conv=='A' else -1
            terms=[]
            for u in units:
                tu=chiP_unit(u)
                r=Fr(str(gp(f'nfelttrace(bnf,nfeltdiv(bnf,{u},{cc}))')))
                tpsi=(-sgn*ppart_frac(r,p))%1        # psi_P(u/c)
                terms.append(((-tu+tpsi)%1))
            S='('+'+'.join(E(t) for t in terms)+')'
            tc=chiP_of_c(cc)
            eps=gp(f'eps_=({E(tc)})*{S}/{SQ[p]}')
            return eps,terms,tc
        loc={}
        for conv in ('A','B'):
            vals=[]
            # two different choices of c to test independence
            ys=[]
            for q in (2,5,7): ys.append(t0 if q==p else '1')
            mod=f'[{";".join((P+","+str(ev+1)) if q==p else (Pname[q]+","+str({2:3,5:1,7:1}[q])) for q in (2,5,7))}]'
            c1=gp(f'c1=idealchinese(bnf,[{mod},[1,1]],[{",".join(ys)}])')
            ys2=[(f'nfeltmul(bnf,{t0},{units[-1]})' if q==p else '1') for q in (2,5,7)]
            c2=gp(f'c2=idealchinese(bnf,[{mod},[1,1]],[{",".join(ys2)}])')
            for cc in ('c1','c2'):
                assert int(gp(f'nfeltval(bnf,{cc},{P})'))==ev and gp(f'nfeltsign(bnf,{cc})')==gp('[1,1]')
            e1,terms,tc=gauss_eps('c1',conv); e2,_,_=gauss_eps('c2',conv)
            assert gp(f'{e1}=={e2}'), 'c-dependence!'
            # exact checks in Q(zeta_840): |eps|^2 = 1 (eps * complex-conjugate, conj: z -> z^-1)
            assert gp(f'{e1}*Mod(subst(lift({e1}),x,x^{NZ-1}),Phi)==1'), ('|eps|!=1',p,chi)
            k=[k for k in range(NZ) if gp(f'{e1}==z^{k}')]
            num=complex(gp(f'subst(lift({e1}),x,exp(2*Pi*sqrt(-1)/{NZ}))'))
            loc[conv]={'exact':str(gp(f'lift({e1})')),'root_of_unity_840':(str(Fr(k[0],NZ)) if k else None),
                       'numeric':[num.real,num.imag],'arg_turns':(cmath.phase(num)/(2*math.pi))%1,
                       'chiP_c_turns':str(tc),'c':str(gp('nfbasistoalg(bnf,c1)')),
                       'gauss_terms_turns':[str(t) for t in terms]}
            EX[(idx,P,conv)]=e1
        # chi_P(-1) (exact, turns)
        loc['chiP(-1)_turns']=str(chiP_unit(gp('-1')))
        rec['local'][P]=loc
    # archimedean
    rec['local']['inf']={'A':[str(Fr(n,4)) for n in Ninf],'B':[str(Fr(-n,4)%1) for n in Ninf]}
    for conv in ('A','B'):
        ninf=Ninf if conv=='A' else [-n for n in Ninf]
        prod=gp(f"({EX[(idx,'P2',conv)]})*({EX[(idx,'P5',conv)]})*({EX[(idx,'P7',conv)]})*z^{(210*sum(ninf))%NZ}")
        EX[(idx,'prod',conv)]=prod
        pn=complex(gp(f'subst(lift({prod}),x,exp(2*Pi*sqrt(-1)/{NZ}))'))
        rec['prod_'+conv]={'exact':str(gp(f'lift({prod})')),'numeric':[pn.real,pn.imag]}
    assert gp(f"{EX[(idx,'prod','A')]}=={EX[(idx,'prod','B')]}"), 'convention dependence'
    # global root number, numerically (lfunrootres)
    L=gp(f'L=lfuncreate([bnr,{chis}])'); rr=gp('lfunrootres(L)'); w=complex(rr[2])
    rec['W_numeric']=[float(w.real),float(w.imag)]
    pv=complex(*rec['prod_A']['numeric']); pw=complex(gp(f"subst(lift({EX[(idx,'prod','A')]}),x,exp(2*Pi*sqrt(-1)/{NZ}))-L0".replace('L0','lfunrootres(L)[3]'))); rec['abs_diff']=float(abs(pw))
    rec['W_numeric_str']=str(rr[2])
    old=alj[idx]; assert old['chi']==chi
    rec['abs_diff_vs_al_s7json']=abs(pv-complex(*old['root_number']))
    print(chi, Ninf, {P:round(rec['local'][P]['A']['arg_turns'],6) for P in ('P2','P5','P7')}, rec['local']['inf']['A'], 'prod',pv,'|prod-W|=%.2e'%rec['abs_diff'],flush=True)
    results.append(rec)
json.dump({'generators':gens_report,'NZ':NZ,'results':results},open('local_eps.json','w'),indent=1)
