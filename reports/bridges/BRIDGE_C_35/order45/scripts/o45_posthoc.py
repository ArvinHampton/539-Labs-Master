# POST-HOC (after RG43 verdict recorded): mechanism check for ||R(1/x)|| = ||R(x)||/x at kappa=1.
# Candidate identity: R(1/x) = -(1/x) * conj( Pi (kM)^{-1} R(x) ), Pi from (alpha,beta)->(alpha,-beta).
import sys; sys.argv=['x']
exec(open('o45.py').read().split('# ---- order45')[0])
from symbols import reduce
Pi=np.zeros((105,105),complex)
for j,(al,be) in enumerate(pairs):
    kk,ee=reduce(al,(-be[0],-be[1])); Pi[j,kk]=np.exp(2j*np.pi*ee/L)
kM=M/math.sqrt(35); I=np.eye(105); out={}
out['kM_unitary']=float(np.abs(kM@kM.conj().T-I).max())
out['Pi_unitary']=float(np.abs(Pi@Pi.conj().T-I).max())
out['conjM_relation']=float(np.abs(kM.conj()@Pi@kM-Pi).max())   # conj(kM) Pi = Pi (kM)^{-1}
# F(-x) = conj(Pi F(x)) check at two x
chk=0.0
for x in (Fr(2),Fr(2,3)):
    Fx=np.array([C2b_direct(al,be,x)[0] for al,be in pairs]); Fm=np.array([C2b_direct(al,be,-x)[0] for al,be in pairs])
    chk=max(chk,float(np.abs(Fm-np.conj(Pi@Fx)).max()))
out['F_minus_x']=chk
kap=1.0; idn=0.0
for x in (Fr(2),Fr(5,7),Fr(9,2)):
    _,_,Rx,_,_=split(x,*data(x)); _,_,Ry,_,_=split(1/x,*data(1/x))
    pred=-(1/float(x))*np.conj(Pi@np.linalg.solve(kM,Rx)); idn=max(idn,float(np.abs(Ry-pred).max()/np.abs(Ry).max()))
out['identity_R_inv']=idn
print(out); json.dump(out,open('../data/o45_posthoc.json','w'),indent=1)
