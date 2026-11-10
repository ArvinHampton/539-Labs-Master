# Pre-PREREG: check only that the two written tau sources agree on O_res (no block sums computed here).
import sys, json; sys.dont_write_bytecode=True
sys.path.insert(0,'/tmp/repo539/docs/S2-11DM2ET-X-Axiomatic-Book/scripts')
import architecture_A4plus_probe as A
N_flux,N_tow,Q,f_max,B,loads=A.atoms(); O=A.core_q0(N_flux,f_max,Q,B)
f=lambda x: x//21 if x<420 else 20+(x-420)//20
print(json.dumps(dict(n=len(O),O_is_21_9j=list(O)==[21+9*j for j in range(539)],
  tau_agree=all(A.tower_of(x,loads)==f(x) for x in O))))
