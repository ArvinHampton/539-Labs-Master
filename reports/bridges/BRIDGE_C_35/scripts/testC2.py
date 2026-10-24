# Map C (descriptive corollary): |Lambda_C| at the four RTA sample points and their W_7 images, exact via entry 18.
from common import *
import json, math
I=math.log(6+math.sqrt(35))/(2*math.sqrt(35))
def mag(x):  # entry 18: 0 if 2|m or 5|m; 1/m if 7 not| m; sqrt7/m if 7|m  (times I)
    m=Fr(x).denominator
    if m%2==0 or m%5==0: return '0',0.0
    return ('sqrt7/%d'%m, math.sqrt(7)/m) if m%7==0 else ('1/%d'%m,1/m)
out=[]
for x in [Fr(1,7),Fr(3,7),Fr(5,7),Fr(1)]:
    w=-1/(7*x); s1,v1=mag(x); s2,v2=mag(w)
    chk=tuple(bool(c) for c in (abs(abs(Grta_c(x))-v1)<1e-12, abs(abs(Grta_c(w))-v2)<1e-12))
    ratio=None if v1==0 else v2/(abs(float(7*x))**-0.5*v1)
    out.append(dict(x=str(x),W7x=str(w),absG_x=s1,absG_W7x=s2,float_check=chk,ratio_to_halfweight=ratio))
    print(out[-1])
json.dump(out,open('../data/testC.json','w'),indent=1)
