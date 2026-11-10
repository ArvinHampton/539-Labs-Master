# Fine invariants of the Bridge C s-family, s=5..60. Uses PARI (cypari2).
import cypari2, csv, math, re
pari=cypari2.Pari(); pari.allocatemem(2*10**9)
tab={}
for l in open('/workspace/quantum-comp/reports/heavy-daily/2026-10-19-Bridge-C-Clean-v2/tex/s12_dims.tex'):
  m=re.match(r'^(\d+) & (\d+) & (\d+) & (\d+) && (\d+) & (\d+) & (\d+) & (\d+)\\\\',l.strip())
  if m:
    g=list(map(int,m.groups())); tab[g[0]]=g[1:4]; tab[g[4]]=g[5:8]
rows=[]
for s in range(5,61):
  n=s*(s-2); core=int(pari.core(n)); f=int(math.isqrt(n//core))
  dK=int(pari.quaddisc(n))
  Ds=4*n if s%2 else n               # order discriminant of the (primitive) form, s01_intro.tex:134
  # field
  bnf=pari.bnfinit(f"x^2-{core}",1)
  hK=int(bnf.bnf_get_no()); epsK=pari.quadunit(dK); NepsK=int(pari.norm(epsK))
  hK_plus=hK*(2 if NepsK==1 else 1)
  # order of disc Ds
  cu=pari.quadclassunit(Ds); hD=int(cu[0]); epsD=pari.quadunit(Ds); NepsD=int(pari.norm(epsD))
  hD_plus=hD*(2 if NepsD==1 else 1)
  # automorph unit eps_s=(s-1)+sqrt(n): power of the field fundamental unit
  eps_s=(s-1)+math.sqrt(n)
  regK=float(pari.quadregulator(dK))
  k=math.log(eps_s)/regK
  # narrow ray class number modulo f_s = product of primes above primes dividing 2(s-2), with both infinite places
  primes=[int(p) for p in pari.factor(2*(s-2))[0]]
  ideal=pari.idealhnf(bnf,1)
  for p in primes:
    for P in pari.idealprimedec(bnf,p): ideal=pari.idealmul(bnf,ideal,P)
  bnr=pari.bnrinit(bnf,[ideal,[1,1]]); hray=int(bnr.bnr_get_no()) if hasattr(bnr,'bnr_get_no') else int(pari.bnrclassno(bnf,[ideal,[1,1]]))
  omega=len(pari.factor(abs(dK))[0]); genus_one=(hK_plus==2**(omega-1))
  tv=tab.get(s)
  orbit=s*(s-1) if s%2 else (s//2)*(s//2+1)
  rows.append(dict(s=s,n_s=n,squarefree_core=core,conductor_f=f,d_K=dK,D_s=Ds,
    Z_sqrt_n_maximal=(f==1 and core%4!=1),h_K=hK,N_epsK=NepsK,h_plus_K=hK_plus,h_D=hD,N_epsD=NepsD,h_plus_D=hD_plus,
    eps_s=f"{s-1}+sqrt({n})",two_log_eps_s=round(2*math.log(eps_s),6),eps_s_power_of_epsK=round(k,6),
    one_class_per_genus_K=genus_one,narrow_ray_no_f_s=hray,disc_group_order=n,orbit_bound=orbit,
    table_dimV=tv[0] if tv else '',table_dEis=tv[1] if tv else '',table_dcusp=tv[2] if tv else '',
    dimV_eq_orbit=(tv[0]==orbit) if tv else ''))
with open('s_family.csv','w',newline='') as fh:
  w=csv.DictWriter(fh,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for r in rows: print(r['s'],r['n_s'],r['squarefree_core'],r['conductor_f'],r['d_K'],r['h_K'],r['h_plus_K'],r['N_epsK'],r['h_D'],r['h_plus_D'],r['eps_s_power_of_epsK'],r['narrow_ray_no_f_s'],r['table_dimV'],r['table_dcusp'],r['dimV_eq_orbit'])
