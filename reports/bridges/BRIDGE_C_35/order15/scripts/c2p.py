# C2' preregistered: K1, box 80, offsets |.|<=4: literal line corrections, exact rationals
import sys, json; sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from fractions import Fraction as Fr; from symbols import FAM1,sym_pair,reduce
pairs=[sym_pair('K1',i) for i in range(35)]
sgn=lambda v:(v>0)-(v<0)
def W(v): n,k=v; return Fr(int(n>=0 and k>=0))-Fr(sgn(n)+sgn(n+21*k),2)
B=80; out={'per':[]}; unc=0; lines={}
for j,(al,be) in enumerate(pairs):
    kk,_=reduce((-al[0],-al[1]),(-be[0],-be[1]),FAM1); alk=sym_pair(FAM1[kk//35],kk%35)[0]
    for n in range(-B,B+1):
        for k in range(-B,B+1):
            nu=(al[0]+n,al[1]+k); s1,s2,s3=sgn(nu[0]),sgn(nu[1]),sgn(nu[0]+21*nu[1])
            w1=W((n,k)); vm=(-nu[0]-alk[0],-nu[1]-alk[1]); assert vm[0].denominator==1 and vm[1].denominator==1
            w2=W((int(vm[0]),int(vm[1])))
            dE=(w1+w2)/2-Fr(1+s1*s2,4); dO=(w1-w2)/2-(Fr(s1+s2,4)-Fr(s1+s3,2))
            for nm,d in (('E',dE),('O',dO)):
                if d==0: continue
                m=n+21*k; cls=None
                for lab,val in (('n',n),('k',k),('m',m)):
                    if abs(val)<=4: cls=(lab,val); break
                if cls is None: unc+=1; continue
                key=(nm,cls[0],cls[1],str(d)); L=lines.setdefault(key,[0,0,0]); 
                t={'n':k,'k':n,'m':k}[cls[0]]; L[0]+=1; L[1]+= (t>30); L[2]+=(t<-30)
out['uncovered']=unc
out['lines']=[dict(parity=k[0],line=k[1]+'='+str(k[2]),value=k[3],count=v[0],far_plus=v[1],far_minus=v[2],
                   type=('full' if v[1] and v[2] else ('half' if v[1] or v[2] else 'finite'))) for k,v in sorted(lines.items())]
out['C2']='pass' if unc==0 else 'FAIL'
summ={}
for l in out['lines']: summ.setdefault((l['parity'],l['type']),0); summ[(l['parity'],l['type'])]+=l['count']
out['summary']={str(k):v for k,v in summ.items()}
print(out['C2'],unc,out['summary']); json.dump(out,open('../data/c2p.json','w'),indent=1)
