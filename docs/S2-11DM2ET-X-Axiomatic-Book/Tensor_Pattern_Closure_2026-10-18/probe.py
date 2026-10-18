import sys; sys.path.insert(0,'.')
import numpy as np
from family import *
S=Smatrix(); T=Tmatrix()
print("nonzeros per row S:",set((abs(S)>1e-12).sum(1)), " |S| values:",set(np.round(abs(S[abs(S)>1e-12]),9)))
print("nonzeros per row T:",set((abs(T)>1e-12).sum(1)))
