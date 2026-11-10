# Generates every modular datum used in BATCH7 PREREG. Run BEFORE writing PREREG.
import json
from sympy import factorint, primerange, kronecker_symbol
D=140
ram=sorted(factorint(D))
ctrl=[p for p in primerange(3,30) if D%p]
T={'D':D,'primes_dividing_D':ram,'control_primes':ctrl,
   'kronecker_D_p':{p:int(kronecker_symbol(D,p)) for p in ctrl},
   'split_primes':[p for p in ctrl if kronecker_symbol(D,p)==1],
   'inert_primes':[p for p in ctrl if kronecker_symbol(D,p)==-1]}
json.dump(T,open('data/modular_table.json','w'),indent=1); print(json.dumps(T))
