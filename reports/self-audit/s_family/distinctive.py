import csv,sympy
R=list(csv.DictReader(open('s_family.csv'))); S=lambda f:[int(r['s']) for r in R if f(r)]
r7=[r for r in R if r['s']=='7'][0]
props={
 "n_s squarefree (Z[sqrt n_s] = maximal order, eps_s fundamental unit, used at s03_main.tex:28)":lambda r:r['Z_sqrt_n_maximal']=='True' and float(r['eps_s_power_of_epsK'])==1.0,
 "eps_s = (s-1)+sqrt(n_s) is the fundamental unit of K (power 1)":lambda r:float(r['eps_s_power_of_epsK'])==1.0,
 "N(fund. unit of K) = +1":lambda r:r['N_epsK']=='1',
 "n_s = p*q, both prime (s-2 and s twin primes)":lambda r:sympy.isprime(int(r['s'])) and sympy.isprime(int(r['s'])-2),
 "h(K)=2":lambda r:r['h_K']=='2',
 "h+(K)=4":lambda r:r['h_plus_K']=='4',
 "h(K)=2 and h+(K)=4":lambda r:r['h_K']=='2' and r['h_plus_K']=='4',
 "one narrow class per genus (h+ = 2^(omega(d_K)-1))":lambda r:r['one_class_per_genus_K']=='True',
 "narrow ray class number mod f_s inf1 inf2 = 16":lambda r:r['narrow_ray_no_f_s']=='16',
 "table dim V = Burnside orbit bound (s(s-1) odd, (s/2)(s/2+1) even)":lambda r:r['dimV_eq_orbit']=='True',
 "d_cusp = 6":lambda r:r['table_dcusp']=='6',
 "dim V = 42":lambda r:r['table_dimV']=='42',
 "d_cusp > 0":lambda r:r['table_dcusp'] not in ('','0'),
 "d_cusp = 0":lambda r:r['table_dcusp']=='0',
 "twin-prime n_s AND h+=4":lambda r:sympy.isprime(int(r['s'])) and sympy.isprime(int(r['s'])-2) and r['h_plus_K']=='4',
}
out=[]
for k,f in props.items():
  ss=S(f); out.append(f"{k}: holds at s=7? {7 in ss}; s in 5..60 with property: {len(ss)} -> {ss}")
out.append(f"2 log eps_s at s=7 = {r7['two_log_eps_s']}; minimal over s is at s=5 ({[r['two_log_eps_s'] for r in R if r['s']=='5'][0]}) since eps_s increases with s")
open('distinctive.out','w').write("\n".join(out)); print("\n".join(out))
