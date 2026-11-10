import sys, json, re, numpy as np
sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import phase_ints, Fr
from symbols import FAM, sym_pair, reduce
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
out={}
# H1 audit: in lines() source, be and x appear only as args to ph()/period()
src=open('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order18/scripts/a2.py').read()
body=src[src.index('def lines'):src.index('P=np.zeros')]
bad=[l for l in body.splitlines()[1:] if re.search(r'\bbe\b|\bx\b',re.sub(r'(ph|period)\(al,be,x,','',l))]
out['H1_offending_lines']=bad; out['H1']=not bad
# H2 exact
g=np.stack(np.meshgrid(np.arange(-6,7),np.arange(-6,7),indexing='ij'),-1).reshape(-1,2)
ok=True
for al,be in pairs:
    nb=(-be[0],-be[1])
    for x in (Fr(2),Fr(1,3),Fr(5,7),Fr(9,2)):
        k,M=phase_ints(al,be,x,g); k2,M2=phase_ints(al,nb,-x,g); ok&= M==M2 and bool(((k+k2)%M==0).all())
out['H2']=ok
# H3 exact
h3=[]
for al,be in pairs:
    kk,e=reduce(al,(-be[0],-be[1])); al2,be2=pairs[kk]; h3.append(tuple(map(Fr,al2))==tuple(map(Fr,al)))
out['H3']=all(h3); out['H3_count']=sum(h3)
# H3b exact: constant ratio pointwise f_{al,-be} = e(c) f_{al,be'}
ok=True
for al,be in pairs:
    kk,e=reduce(al,(-be[0],-be[1])); al2,be2=pairs[kk]
    for x in (Fr(2),Fr(5,7)):
        k,M=phase_ints(al,(-be[0],-be[1]),x,g); k2,_=phase_ints(al2,be2,x,g); d=(k-k2)%M; ok&=bool((d==d[0]).all())
out['H3b_constant_ratio']=ok
out['H4']='follows from H2,H3b and period() using only equality tests of k'
out['verdict']='PASS' if out['H1'] and out['H2'] and out['H3'] and out['H3b_constant_ratio'] else 'FAIL'
print(out); json.dump(out,open('../data/o49.json','w'),indent=1)
