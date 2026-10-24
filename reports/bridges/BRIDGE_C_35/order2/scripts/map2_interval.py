# Map 2: certify A1(x) != 0 for q^{-7/20}C at x in Z0 (2|m or 5|m), and at y=-1/5, in mpmath interval arithmetic.
from lib2 import *
import json
from mpmath import iv, mpf
iv.dps=60
PI=iv.pi; SQ=iv.sqrt(PI)
def ivsqrt(fr): return iv.sqrt(iv.mpf(fr.numerator)/fr.denominator)
def ivexp_sum(coef,M):   # sum_k coef[k] e(k/M), coef exact Fractions
    re=iv.mpf(0); im=iv.mpf(0)
    for k,cf in coef.items():
        if cf==0: continue
        ang=2*PI*iv.mpf(k)/M; c=iv.mpf(cf.numerator)/cf.denominator
        re+=c*iv.cos(ang); im+=c*iv.sin(ang)
    return re,im
def hist(keys,weights):
    d={}
    for k,w in zip(keys.tolist(),weights): d[k]=d.get(k,Fr(0))+w
    return d
def A1_iv(al,be,x):
    RE=iv.mpf(0); IM=iv.mpf(0)
    for sg,c,U in PIECES:
        d=piece_data(al,be,x,c,U); N=d['N']; n2=N*N
        mf=hist(d['k'],[Fr(1,n2)]*n2)
        w1=hist(d['k'],[Fr(int(z),N*N)-Fr(1,2*N) for z in d['z1']])
        w2=hist(d['k'],[Fr(int(z),N*N)-Fr(1,2*N) for z in d['z2']])
        p,q,r=d['p'],d['q'],d['r']; den=4*p*r-q*q
        Ja=(SQ/4)*(2/(iv.mpf(den.numerator)/den.denominator))*(2*ivsqrt(r)-iv.mpf(q.numerator)/q.denominator/ivsqrt(p))
        Jb=(SQ/4)*(2/(iv.mpf(den.numerator)/den.denominator))*(2*ivsqrt(p)-iv.mpf(q.numerator)/q.denominator/ivsqrt(r))
        cm=-(iv.mpf(d['l1'].numerator)/d['l1'].denominator*Ja+iv.mpf(d['l2'].numerator)/d['l2'].denominator*Jb)
        for coef,fac in ((mf,cm),(w1,-(SQ/2)/ivsqrt(r)),(w2,-(SQ/2)/ivsqrt(p))):
            re,im=ivexp_sum(coef,d['M']); s=iv.mpf(sg.numerator)/sg.denominator
            RE+=s*fac*re; IM+=s*fac*im
    for sg,c,u in WALLS:
        d=wall_data(al,be,x,c,u); N=d['N']
        re,im=ivexp_sum(hist(d['k'],[Fr(1,N)]*N),d['M'])
        fac=(iv.mpf(sg.numerator)/sg.denominator)*(SQ/2)/ivsqrt(d['Qu'])
        RE+=fac*re; IM+=fac*im
    return RE,IM
Z0=[x for x in XS if x.denominator%2==0 or x.denominator%5==0]+[Fr(-1,5)]
out=[]; zeros=[]
for x in Z0:
    RE,IM=A1_iv(a,(Fr(0),Fr(0)),x); ab2=RE*RE+IM*IM
    cert=bool(ab2.a>0)
    if not cert: zeros.append(str(x))
    out.append(dict(x=str(x),re=str(RE.mid),im=str(IM.mid),abs=float(iv.sqrt(ab2).mid),width=float((ab2.b-ab2.a)),nonzero_certified=cert))
    print(x,round(out[-1]['abs'],10),cert,flush=True)
json.dump(dict(points=len(Z0),not_certified=zeros,results=out),open('../data/map2_interval.json','w'),indent=1)
