# POST-HOC (descriptive): add the second endpoint reflection u -> -u at c1 (refinement RG1', NOT preregistered)
import sys, json; sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from fractions import Fraction as Fr; from symbols import FAM,sym_pair
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]; isZ=lambda r: Fr(r).denominator==1
Rm={j for j,(al,be) in enumerate(pairs) if isZ(2*(al[0]+al[1])) and isZ(14*(be[0]+be[1])) and isZ(14*(be[0]+be[1])*(al[0]+al[1]))}
Ru={j for j,(al,be) in enumerate(pairs) if isZ(2*al[0]) and isZ(10*be[0]) and isZ(10*be[0]*al[0])}
Z1=set(json.load(open('../data/rg1.json'))['Z1'])
res=dict(Rm=sorted(Rm),Ru=sorted(Ru),union_equals_Z1=(Rm|Ru)==Z1,Z1_minus_union=sorted(Z1-(Rm|Ru)),union_minus_Z1=sorted((Rm|Ru)-Z1))
print(res); json.dump(res,open('../data/rg1posthoc.json','w'),indent=1)
