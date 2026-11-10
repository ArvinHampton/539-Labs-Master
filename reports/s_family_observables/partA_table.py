# Part A table s=5..500 (PARI via cypari2). Conductor analogue f_s = primes over p|2(s-2), both infinite places (reproduces 16 at s=7).
import cypari2,csv,math,sympy
pari=cypari2.Pari(); pari.allocatemem(4*10**9)
def dEis_odd(n):
  r=3
  for p,e in sympy.factorint(n).items(): r*= (p**e+1)//2
  return r
def dEis_even(s):
  t=s//2; N=2*t*(t-1); k=0
  while N%2==0: N//=2; k+=1
  v=N; base=2**(k-1)+(4 if k%2==0 else (6 if v%4==1 else 5))
  for p,e in sympy.factorint(v).items(): base*=(p**e+1)//2
  return base
rows=[]
for s in range(5,501):
  n=s*(s-2); core=int(pari.core(n)); f=math.isqrt(n//core); dK=int(pari.quaddisc(n))
  Ds=4*n if s%2 else n
  bnf=pari.bnfinit(f"x^2-{core}",1); hK=int(bnf.bnf_get_no())
  NK=int(pari.norm(pari.quadunit(dK))); hKp=hK*(2 if NK==1 else 1)
  hD=int(pari.quadclassunit(Ds)[0]); ND=int(pari.norm(pari.quadunit(Ds))); hDp=hD*(2 if ND==1 else 1)
  reg=float(pari.quadregulator(dK)); le=math.log((s-1)+math.sqrt(n)); k=round(le/reg)
  ideal=pari.idealhnf(bnf,1)
  for p in sympy.primefactors(2*(s-2)):
    for P in pari.idealprimedec(bnf,p): ideal=pari.idealmul(bnf,ideal,P)
  try: ray=int(pari.bnrclassno(bnf,[ideal,[1,1]]))
  except Exception as e: ray=''
  orbit=s*(s-1) if s%2 else (s//2)*(s//2+1)
  if s%2==0 and math.isqrt(s//2)**2==s//2: mm=math.isqrt(s//2); dimV=orbit-mm*(mm-1); dimV_status='half-cone bound (exact m<=6)'
  else: dimV=orbit; dimV_status='orbit bound (exact s<=51)'
  dE=dEis_odd(n) if s%2 else dEis_even(s)
  rows.append(dict(s=s,n_s=n,core=core,f=f,d_K=dK,D_s=Ds,h_K=hK,hplus_K=hKp,N_epsK=NK,h_D=hD,hplus_D=hDp,N_epsD=ND,
    regulator_K=reg,two_log_eps_s=2*le,I_s=le/(2*math.sqrt(n)),k_power=k,ray_no=ray,dimV=dimV,dimV_status=dimV_status,dEis_formula=dE,dcusp=dimV-dE,
    twin=int(sympy.isprime(s) and sympy.isprime(s-2))))
with open('partA_table.csv','w',newline='') as fh:
  w=csv.DictWriter(fh,fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
print(len(rows))
