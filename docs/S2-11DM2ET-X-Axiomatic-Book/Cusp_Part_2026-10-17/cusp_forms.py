# Explicit dihedral Maass cusp forms: conductors, levels, nebentypus, Maass consistency, exact coefficients of the cusp components.
import numpy as np, cypari2, pickle, math, itertools, uvec, cmath
from fractions import Fraction as Fr
from collections import defaultdict
from uvec import vectors
from family import LABELS
pari=cypari2.Pari(); pari.allocatemem(2*10**9); gp=lambda s: pari(s)
d=pickle.load(open("fitF.pkl","rb")); pc=d['per_comp']; cyc=d['cyc']
gp('bnf=bnfinit(y^2-35,1); P2=idealprimedec(bnf,2)[1]; P5=idealprimedec(bnf,5)[1]; P7=idealprimedec(bnf,7)[1]')
gp('m=idealmul(bnf,idealmul(bnf,idealpow(bnf,P2,3),P5),P7); bnr=bnrinit(bnf,[m,[1,1]],1)')
out=[]
cuspcomps=sorted({i for i,rec in pc.items() for s,r in rec.items() if r and r['cusp']>1e-12})
out.append(f"cusp components ({len(cuspcomps)}): "+", ".join(f"{i}:{tuple(int(t) for t in LABELS[i][0])}/70|{tuple(int(t) for t in LABELS[i][1])}/70" for i in cuspcomps))
eiscomps=[i for i in pc if i not in cuspcomps]
out.append(f"pure-Eisenstein components: {len(eiscomps)} (all others; max |cusp|^2 there = {max(r['cusp'] for i in eiscomps for r in pc[i].values() if r):.1e})")
out.append(f"max |Eis|^2 inside cusp components = {max(r['eis'] for i in cuspcomps for r in pc[i].values() if r):.1e}")
# characters
orbits=[]
for j in range(1,24,2):
    for l in (0,1):
        chi=(j,l,1)
        cond=gp(f'bnrconductor(bnr,{list(chi)})')
        Nf=int(gp(f'idealnorm(bnf,bnrconductor(bnr,{list(chi)})[1])')); inf=[int(t) for t in gp(f'bnrconductor(bnr,{list(chi)})[2]')]
        # nebentypus: omega(n)=chi_K(n)*chi((n)) for primes n=p
        neb=[]
        for p in (3,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113):
            c=[int(t) for t in gp(f'bnrisprincipal(bnr,idealhnf(bnf,{p}),0)')]
            v=sum(Fr(chi[i]*c[i],cyc[i]) for i in range(3))%1
            kK=int(gp(f'kronecker(140,{p})'))
            neb.append((p,str(v),kK))
        orbits.append((chi,Nf,inf,neb))
ords=lambda chi: math.lcm(*[cyc[i]//math.gcd(chi[i],cyc[i]) for i in range(3)])
for chi,Nf,inf,neb in orbits:
    restr=set((p,v) for p,v,k in neb)
    out.append(f"chi{chi}: order {ords(chi)}, conductor norm {Nf}, conductor inf {inf}, level 140*N(f)={140*Nf}; chi on rational primes (p, value as fraction of turn): {[ (p,v) for p,v,k in neb[:10]]}")
# Is chi((n)) for rational n a function of n mod 280? (the nebentypus is chi_140 * that)
pickle.dump(orbits,open("cusp_chars.pkl","wb"))
# Maass consistency: Fhat_-(chi) vs Fhat_+(chi)
mc=[]
for i in cuspcomps:
    fp=dict(pc[i][1]['cusp_chars']); fm=dict(pc[i][-1]['cusp_chars'])
    for chi in fp:
        if abs(fp[chi])>1e-9: mc.append((chi[1], fm.get(chi,0)/fp[chi]))
r0=[complex(v) for l,v in mc if l==0]; r1=[complex(v) for l,v in mc if l==1]
out.append(f"Maass consistency Fhat_-/Fhat_+ : l=0 (type (0,0)) ratios in {sorted(set(np.round(r0,8)))}, l=1 (type (1,1)) ratios in {sorted(set(np.round(r1,8)))}")
# exact values of the cusp coefficients: |Fhat| and phase in turns
vals=set()
for i in cuspcomps:
    for chi,v in pc[i][1]['cusp_chars']:
        vals.add((round(abs(v)*48,6), round((cmath.phase(v)/(2*math.pi))%1*120,4)))
out.append(f"cusp coefficients Fhat_+(chi): 48*|Fhat| in {sorted(set(a for a,b in vals))}; phase*120 (turns) in {sorted(set(b for a,b in vals))[:30]}")
open("cusp_forms.txt","w").write("\n".join(out)+"\n"); print("\n".join(out))
