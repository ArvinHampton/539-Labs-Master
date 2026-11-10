import sys, json; sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from fractions import Fraction as Fr; from symbols import FAM1, FAM, sym_pair, MU, a, hA, add
sgn=lambda v:(v>0)-(v<0); ind=lambda b: 1 if b else 0
pairs=[(f,i,sym_pair(f,i)) for f in FAM1 for i in range(35)]
bad=0; table=[]
for f,i,(al,be) in pairs:
    s_=al[0]+21*al[1]
    h1=lambda n: ind(n>=0)-Fr(1+sgn(n+al[0]),2); h2=lambda k: ind(k>=0)-Fr(1+sgn(k+al[1]),2)
    g1=lambda n: sgn(n)-sgn(n+al[0]); g3=lambda m: sgn(m)-sgn(m+s_)
    for n in range(-100,101):
        for k in range(-100,101):
            nu=(al[0]+n,al[1]+k); s1,s2,s3=sgn(nu[0]),sgn(nu[1]),sgn(nu[0]+21*nu[1])
            W=ind(n>=0 and k>=0)-Fr(sgn(n)+sgn(n+21*k),2); p=Fr((1+s1)*(1+s2),4)-Fr(s1+s3,2)
            D=Fr(1+s1,2)*h2(k)+Fr(1+s2,2)*h1(n)+h1(n)*h2(k)-Fr(g1(n),2)-Fr(g3(n+21*k),2)
            if W-p!=D: bad+=1
    R=range(-30,31)
    table.append(dict(family=f,i=i,alpha=[str(x) for x in al],beta=[str(x) for x in be],sigma=str(s_),
        h1={n:str(h1(n)) for n in R if h1(n)},h2={k:str(h2(k)) for k in R if h2(k)},g1={n:g1(n) for n in R if g1(n)},g3={m:g3(m) for m in R if g3(m)}))
print('A1 mismatches',bad,flush=True)
json.dump(dict(A1_mismatches=bad,A1='pass' if bad==0 else 'FAIL',table=table),open('../data/lineterms.json','w'),indent=1)
# B1: criterion vs stored zero sets
isZ=lambda r: Fr(r).denominator==1
crit=lambda al,be:(isZ(2*(al[0]+al[1])) and isZ(14*(be[0]+be[1])) and isZ(14*(be[0]+be[1])*(al[0]+al[1]))) or (isZ(2*al[0]) and isZ(10*be[0]) and isZ(10*be[0]*al[0]))
base='/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/'
p105=[sym_pair(f,i) for f in FAM for i in range(35)]
z105=set(json.load(open(base+'order14/data/rg1.json'))['Z1']); c105={j for j,(al,be) in enumerate(p105) if crit(al,be)}
H=[(mu,hA) for mu in MU]+[(add(a,mu),add(a,hA)) for mu in MU]
zH=set(json.load(open(base+'order15/data/H.json'))['zero']); cH={j for j,(al,be) in enumerate(H) if crit(al,be)}
K1=[sym_pair('K1',i) for i in range(35)]
zK=set(json.load(open(base+'order14/data/rg1k1.json'))['meas_zero']); cK={j for j,(al,be) in enumerate(K1) if crit(al,be)}
B1=dict(s105=z105==c105,H=zH==cH,K1=zK==cK); B1['verdict']='pass' if all(B1.values()) else 'FAIL'; print('B1',B1)
json.dump(B1,open('../data/b1.json','w'),indent=1)
