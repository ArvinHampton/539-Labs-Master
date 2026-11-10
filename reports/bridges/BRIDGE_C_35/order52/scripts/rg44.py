from fractions import Fraction as F
import re,itertools,json
A=[[2,7],[7,7]];B=lambda u,v:sum(u[i]*A[i][j]*v[j] for i in range(2) for j in range(2));Q=lambda c:B(c,c)/2
c1=[F(-1,5),F(1,5)];c2=[F(4),F(-1)];m1=[-x for x in c1];sg=lambda r:(r>0)-(r<0)
g=[(a,b) for a in range(-6,7) for b in range(-6,7)]
r={"T1":all(B(c1,v)==v[0] and B(c2,v)==v[0]+21*v[1] for v in g),
"T2":B(c1,c2)==4 and B(m1,c2)==-4,"T3":Q(m1)==F(-1,10) and Q(c2)==F(-17,2),
"T4":all(sg(a)+sg(b)==sg(b)-sg(-a) for a,b in g)}
s=open('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order18/scripts/a2.py').read()
r["T5"]=("-Fr(g1(n),2)" in s) and ("-Fr(g3(mm),2)" in s) and "g1=lambda n:sg(n)-sg(n+a1)" in s and "g3=lambda m:sg(m)-sg(m+sig)" in s
r["PASS"]=all(r.values());print(json.dumps(r));json.dump(r,open('../data/rg44.json','w'))
