import sys,json
sys.dont_write_bytecode=True
sys.path.insert(0,'/tmp/repo539/docs/S2-11DM2ET-X-Axiomatic-Book/scripts')
import flint, architecture_A4plus_probe as A
T=json.load(open('data/modular_table.json'))
N_flux,N_tow,Q,f_max,B,loads=A.atoms(); O=A.core_q0(N_flux,f_max,Q,B)
E,F=A.build_complex(O,loads,'A2_enrich'); E=sorted(E); F=sorted(F); V=len(O)
ei={e:k for k,e in enumerate(E)}
d1=[[0]*V for _ in E]
for k,(a,b) in enumerate(E): d1[k][a]=-1; d1[k][b]=1
d2=[[0]*len(E) for _ in F]
for k,(a,b,c) in enumerate(F): d2[k][ei[(b,c)]]=1; d2[k][ei[(a,c)]]=-1; d2[k][ei[(a,b)]]=1
# check d2*d1 = 0
import numpy as np
assert not (np.array(d2)@np.array(d1)).any()
gate=(V,len(E),len(F))==(539,594,56)
def ranks(p=None):
    if p is None: return flint.fmpz_mat(d1).rank(), flint.fmpz_mat(d2).rank()
    return flint.nmod_mat(d1,p).rank(), flint.nmod_mat(d2,p).rank()
def betti(r1,r2): return (V-r1, len(E)-r1-r2, len(F)-r2)
rQ=ranks(); R={'counts':[V,len(E),len(F)],'gate':gate,'betti_Q':betti(*rQ)}
bp={}; tors=[]
for p in T['primes_dividing_D']+T['control_primes']:
    r=ranks(p); bp[p]=betti(*r)
    if r!=rQ: tors.append(p)
R['betti_Fp']=bp; R['torsion_primes']=tors
if not gate: R['C25']=R['C26']='VOID'
else:
    b3=bp[3]
    R['C25']='PASS' if any(bp[p]!=b3 for p in T['primes_dividing_D']) and all(bp[p]==b3 for p in T['control_primes']) else 'FAIL'
    R['C26']='PASS' if tors and set(tors)<=set(T['primes_dividing_D']) else 'FAIL'
json.dump(R,open('data/b7.json','w'),indent=1); print(json.dumps(R))
