# Q-side local factors and comparison with sector signs. Reads local_eps.json (exact values in Q(zeta_840)).
# Convention A throughout: psi_Q = e(x) at infinity, e(-{x}_p) at p; psi_K = psi_Q o Tr.
#  lambda_p = lambda(K_P/Q_p, psi_p) = eps(eta_p, psi_p)  (Langlands lambda; Tate NTB §3.4, inductivity in degree 0),
#  eps_p(pi_p) = eps(Ind psi_P) = lambda_p * eps(psi_P, psi_p o Tr),   pi_p = Ind_{K_P}^{Q_p} psi_P  (local comp. of f_psi, level 19600).
import cypari2, json, math, cmath
from fractions import Fraction as Fr
pari=cypari2.Pari(); pari.allocatemem(10**9); gp=lambda s: pari(s); pari.set_real_precision(60)
D=json.load(open('local_eps.json')); NZ=D['NZ']
gp(f'Phi=polcyclo({NZ},x); z=Mod(x,Phi)')
gp('bnf=bnfinit(y^2-35,1); P2=idealprimedec(bnf,2)[1]; P5=idealprimedec(bnf,5)[1]; P7=idealprimedec(bnf,7)[1]')
gp('m=idealmul(bnf,idealmul(bnf,idealpow(bnf,P2,3),P5),P7); bnr=bnrinit(bnf,[m,[1,1]],1)')
gp('z5=z^168; z7=z^120; Iz=z^210; s5=sum(a=1,4,kronecker(a,5)*z5^a); s7=-Iz*sum(a=1,6,kronecker(a,7)*z7^a)')
assert gp('s5^2==5 && s7^2==7')
def E(t):
    k=Fr(t)*NZ; assert k.denominator==1; return f'z^{int(k)%NZ}'
def ppart_frac(r,p):
    r=Fr(r); B=r.denominator; k=0
    while B%p==0: B//=p; k+=1
    if k==0: return Fr(0)
    pk=p**k; return Fr((r.numerator*pow(B,-1,pk))%pk, pk)
num=lambda e: complex(gp(f'subst(lift({e}),x,exp(2*Pi*sqrt(-1)/{NZ}))'))
eq=lambda a,b: bool(gp(f'({a})==({b})'))
out={'lambda':{},'checks':{},'per_char':[]}
# --- Langlands lambda factors, exact
SQ={2:'2',5:'s5',7:'s7'}
lam={}
for p,a in ((2,2),(5,1),(7,1)):
    c=p**a; eta=lambda x: int(gp(f'hilbert({x},35,{p})'))
    terms=[]; 
    for u in range(1,c):
        if math.gcd(u,c)>1: continue
        tu=Fr(0) if eta(u)==1 else Fr(1,2)
        terms.append((tu - ppart_frac(Fr(u,c),p))%1)
    tc=Fr(0) if eta(c)==1 else Fr(1,2)
    lam[p]=gp(f"({E(tc)})*({'+'.join(E(t) for t in terms)})/{SQ[p]}")
    # conductor exponent of eta_p is a: check eta trivial on 1+p^a Z_p but not on units
    k=[k for k in range(NZ) if eq(lam[p],f'z^{k}')]
    out['lambda'][p]={'value_turns':str(Fr(k[0],NZ)) if k else None,'numeric':str(num(lam[p]))}
assert eq(f'{lam[2]}*{lam[5]}*{lam[7]}','1'); out['checks']['prod_lambda_eq_1']=True   # global lambda(K/Q)=1, lambda_inf=1 (split)
print('lambda',out['lambda'])
R=D['results']; idx={tuple(r['chi']):i for i,r in enumerate(R)}
X=lambda r,P: f"Mod({r['local'][P]['A']['exact']},Phi)"
Pp={'P2':2,'P5':5,'P7':7}
nchk={'tate_inverse':0,'sigma_pair':0,'inf_partner':0}
for r in R:
    chi=tuple(r['chi']); inv=(24-chi[0],chi[1],chi[2]); ri=R[idx[inv]]
    row={'chi':list(chi),'inf':r['inf']}
    for P,p in Pp.items():
        e=X(r,P); ei=X(ri,P); cm1=Fr(r['local'][P]['chiP(-1)_turns'])
        # Tate: eps(chi)eps(chi^-1) = chi(-1)  (exact)
        assert eq(f'{e}*{ei}',E(cm1)); nchk['tate_inverse']+=1
        epi=gp(f'({e})*({lam[p]})'); epii=gp(f'({ei})*({lam[p]})')
        etam1=int(gp(f'hilbert(-1,35,{p})')); om=(cm1+(Fr(0) if etam1==1 else Fr(1,2)))%1   # omega_{pi_p}(-1)=eta_p(-1)chi_P(-1)
        assert eq(f'{epi}*{epii}',E(om))
        z1=num(e); z2=num(epi)
        row[P]={'eps_psiP':[z1.real,z1.imag],'eps_psiP_arg_turns':(cmath.phase(z1)/2/math.pi)%1,
                'eps_psiP_is_pm1':bool(eq(f'({e})^2','1')),
                'eps_pi_p':[z2.real,z2.imag],'eps_pi_p_arg_turns':(cmath.phase(z2)/2/math.pi)%1,
                'eps_pi_p_is_pm1':bool(eq(f'({epi})^2','1')),
                'chiP(-1)':1 if cm1==0 else -1,'eta_p(-1)':etam1,'omega_pi_p(-1)':1 if om==0 else -1}
    # Galois pair chi <-> chi o sigma (claim: k <-> k+12 mod 24): local eps equal exactly?
    pair=((chi[0]+12)%24,chi[1],chi[2]); rp=R[idx[pair]]
    row['sigma_pair_same_local']=all(eq(X(r,P),X(rp,P)) for P in Pp)
    # archimedean partner [k,1,1] vs [k,0,1]: same finite local factors?
    part=(chi[0],1-chi[1],chi[2]); rq=R[idx[part]]
    row['inf_partner_same_finite_local']=all(eq(X(r,P),X(rq,P)) for P in Pp)
    out['per_char'].append(row)
# Is chi o sigma really chi_{k+12}? check on ideals: psi(sigma(Q)) for primes Q above split p
def psi(ch,I): return Fr(str(gp(f'chareval(bnr,{list(ch)},{I})')))
ok=True
for p in (3,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83):
    dec=gp(f'idealprimedec(bnf,{p})')
    if len(dec)==2:
        for k in range(1,24,2):
            for e in (0,1):
                a=psi((k,e,1),f'idealprimedec(bnf,{p})[1]'); b=psi(((k+12)%24,e,1),f'idealprimedec(bnf,{p})[2]')
                ok &= (a==b)
out['checks']['chi_sigma_equals_chi_k+12_on_split_primes_upto_83']=bool(ok)
# Nebentypus of f_psi (level 19600): omega(n)=kron(140,n)*psi((n)); p-component at -1 via CRT, compare with eta_p(-1)chi_P(-1)
N=19600
for r,row in zip(R,out['per_char']):
    chi=r['chi']
    for P,p in Pp.items():
        q=p**(4 if p==2 else 2); Q2=N//q
        n=int(gp(f'lift(chinese(Mod(-1,{q}),Mod(1,{Q2})))'))
        w=(psi(chi,f'idealhnf(bnf,{n})') + (0 if int(gp(f'kronecker(140,{n})'))==1 else Fr(1,2)))%1
        row[P]['nebentypus_p_part(-1)_dirichlet']=1 if w==0 else (-1 if w==Fr(1,2) else str(w))
        assert row[P]['nebentypus_p_part(-1)_dirichlet']==row[P]['omega_pi_p(-1)'], (chi,P)
        # Atkin-Li: W_Q^2 = chi_Q(-1) * conj(chi_{Q'}(Q)), Q=p^e || N
        n2=int(gp(f'lift(chinese(Mod(1,{q}),Mod({q},{Q2})))'))
        w2=(psi(chi,f'idealhnf(bnf,{n2})') + (0 if int(gp(f'kronecker(140,{n2})'))==1 else Fr(1,2)))%1
        row[P]['chi_Qprime(Q)_turns']=str(w2)
        row[P]['W_Q^2_AtkinLi_turns']=str(((0 if row[P]['omega_pi_p(-1)']==1 else Fr(1,2)) - w2)%1)
out['checks'].update({k:v for k,v in nchk.items()})
out['checks']['omega_pi_p(-1)_equals_dirichlet_nebentypus_p_part(-1)']=True
json.dump(out,open('compare.json','w'),indent=1)
for row in out['per_char']:
    print(row['chi'],row['inf'],' '.join(f"{P}: eps(psi)={row[P]['eps_psiP_arg_turns']:.6f} eps(pi)={row[P]['eps_pi_p_arg_turns']:.6f} chiP(-1)={row[P]['chiP(-1)']} om(-1)={row[P]['omega_pi_p(-1)']} W^2={row[P]['W_Q^2_AtkinLi_turns']} chi'(Q)={row[P]['chi_Qprime(Q)_turns']}" for P in Pp), 'sig',row['sigma_pair_same_local'],'infp',row['inf_partner_same_finite_local'])
print(out['checks'])
