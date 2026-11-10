# RG1: compare Z1 (numerical zero set of B(c1)) with R1 (exact rho_{c1} criterion)
import sys, json; sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from fractions import Fraction as Fr; from symbols import FAM,sym_pair
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
isZ=lambda r: Fr(r).denominator==1
R1={j for j,(al,be) in enumerate(pairs) if isZ(2*(al[0]+al[1])) and isZ(14*(be[0]+be[1])) and isZ(14*(be[0]+be[1])*(al[0]+al[1]))}
d=json.load(open('../data/c1.json')); Z1={int(r[0]) for r in d['per'] if float(r[3])<=1e-25}
gap=min([float(r[3]) for r in d['per'] if int(r[0]) not in R1]+[1.0])
res=dict(R1=sorted(R1),Z1=sorted(Z1),Z1_minus_R1=sorted(Z1-R1),R1_minus_Z1=sorted(R1-Z1),min_nonzero_outside_R1=gap,
         verdict='pass' if Z1==R1 else 'FAIL')
print(res); json.dump(res,open('../data/rg1.json','w'),indent=1)
