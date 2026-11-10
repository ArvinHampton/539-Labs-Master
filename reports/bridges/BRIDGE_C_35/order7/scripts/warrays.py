# arrays on T660 for candidate 3 (and coupling target), one kind per process
import sys, numpy as np; sys.dont_write_bytecode=True
from lib7 import *
kind=sys.argv[1]; T=taus(660,7)
V=np.array([[series(al,be,t,kind) for al,be in pairs] for t in T])
W=np.array([[series(al,be,-1/t,kind) for al,be in pairs] for t in T])
np.savez('../data/W_%s.npz'%kind,V=V,W=W,T=np.array(T)); print('done',kind)
