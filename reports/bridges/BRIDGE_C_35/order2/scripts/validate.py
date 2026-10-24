# validation: (i) orthant alone at x=0 reproduces a_P=0.5256172043; (ii) A0 from pieces equals I*G_{al,be}(x) (float) on samples
from lib2 import *
import json
I=math.log(6+math.sqrt(35))/(2*math.sqrt(35))
d=piece_data(a,(Fr(0),Fr(0)),Fr(0,1),(0,0),((1,0),(0,1)))
Ja,Jb=J(d['p'],d['q'],d['r'])
aP=-(float(d['l1'])*Ja+float(d['l2'])*Jb)-(SQPI/2)*(-0.5/math.sqrt(float(d['r']))-0.5/math.sqrt(float(d['p'])))
print('a_P formula',aP)
def Gfl(al,be,x):
    m=Fr(x).denominator; N=4*m
    z1,z2=np.meshgrid(np.arange(N),np.arange(N),indexing='ij'); k,M=phase_ints(al,be,x,np.stack([z1,z2],-1))
    return np.exp(2j*np.pi*k/M).mean()
worst=0
for x in [Fr(1),Fr(1,3),Fr(2,7),Fr(5,9),Fr(-5,12),Fr(7,11),Fr(-1,5)]:
    for f in FAM:
        for i in (0,7,20):
            al,be=sym_pair(f,i); A0,_=A01_float(al,be,x); worst=max(worst,abs(A0-I*Gfl(al,be,x)))
print('max |A0_pieces - I G| =',worst)
json.dump({'a_P_formula':aP,'a_P_written':0.5256172043,'A0_check_maxdiff':worst},open('../data/validate.json','w'),indent=1)
