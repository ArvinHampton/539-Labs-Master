import sys,time; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order3c/scripts')
from lib5mp import *
import lib3c
from symbols import sym_pair
for x in (Fr(1),Fr(7,24),Fr(23,19)):
  for al,be in (sym_pair('K2',0),sym_pair('K3',5),sym_pair('K4',17)):
    t=time.time(); a=A012mp(al,be,x); dt=time.time()-t; f=lib3c.A012(al,be,x)
    print(str(x),round(dt,2),[abs(complex(a[i])-f[i]) for i in range(3)],flush=True)
