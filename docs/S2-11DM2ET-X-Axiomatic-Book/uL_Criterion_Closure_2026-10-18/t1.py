import sys, json, time
from alg_T import *
for s in map(int, sys.argv[1].split(',')):
    t=time.time(); E = setup(s); T, cnt, tot = T_c(E, {}, True); cr, S, SJ = crit(E, T)
    print(s, E['D0'], E['c'], E['M'], E['cyc'], 'res', tot, cnt, cr, 'pure', genus_pure(E, T), round(time.time()-t,1), flush=True)
