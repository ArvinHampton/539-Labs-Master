# Parameterizes the RTA packaging identities (zenodo/txt/22143607_Final_draft*: lines 144-167, 186-196) by N.
import random,math,json
def T3(n):
  r=n%3; return n//3 if r==0 else ((4*n+2)//3 if r==1 else (2*n+1)//3)
def fibre(N,m=8):
  q,r=divmod(N,m); sols=[(a,b) for b in range(N//(q+1)+1) for a in [ (N-(q+1)*b) ] if a>=0 and a%q==0 for a in [a//q]]
  return dict(q=q,r=r,partition=f"{r}*{q+1}+{m-r}*{q}",nonneg_solutions_q_qp1=sols,unique=len(sols)==1)
def floorB(N):  # does some (N_flux,f_max) with f_max<9... give B'=N? always: N_flux=9N+8+f_max
  return dict(N_flux_for_fmax21=9*N+8+21, check=(9*N+8)//9==N)
def PW(N):
  # PW(a,b;3^5): N=a^2 b, window a+b, fibres 3b+5a & ab-10, body 2*243+5a; test whether these reproduce N's own fibre blocks / window split
  out=[]
  for a in range(2,int(math.isqrt(N))+1):
    if N%(a*a)==0:
      b=N//(a*a); w=a+b; f1=3*b+5*a; f2=a*b-10; body=2*243+5*a
      fb=fibre(N); ok=(f1==fb['q']+1 and f2==fb['q'] and w+body==N)
      out.append(dict(a=a,b=b,window=w,fib=(f1,f2),body=body,window_plus_body=w+body,all_PW_relations_hold=ok))
  return out
def orbit_len(n):
  seen=set();i=0
  while n not in (0,1,2) and i<10**5: n=T3(n);i+=1
  return i
random.seed(539)
Ns=list(range(530,551))+[49*p for p in (3,5,13,17)]+[11*q*q for q in (2,3,5,13)]+sorted(random.sample(range(100,2001),20))
rows=[]
for N in Ns:
  fb=fibre(N); pw=PW(N)
  rows.append(dict(N=N,fibre=fb['partition'],fibre_unique=fb['unique'],floor_formula_ok=floorB(N)['check'],
    window_split=f"18+{N-18}",PW_any=any(p['all_PW_relations_hold'] for p in pw),PW=pw,T3_orbit_len_of_N=orbit_len(N)))
for r in rows: print(r['N'],r['fibre'],'unique' if r['fibre_unique'] else 'NOT unique',r['floor_formula_ok'],r['window_split'],'PW' if r['PW_any'] else '-',r['T3_orbit_len_of_N'])
# Where can the full PW pattern hold? search all N<=10^5
hits=[N for N in range(10,100001) if any(p['all_PW_relations_hold'] for p in PW(N))]
print("N<=1e5 satisfying all PW(a,b;3^5) relations:",hits)
# T3 orbit lengths: does any seed have length exactly 539 / is 539 a natural length?
L=[orbit_len(n) for n in range(3,200001)]
print("max T3 orbit length for seeds<2e5:",max(L),"; #seeds with length 539:",L.count(539))
json.dump(dict(rows=rows,PW_hits=hits,maxlen=max(L)),open('packaging_controls.json','w'),indent=1,default=str)
