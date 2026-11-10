import sys; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import *
import mpmath as mp
mp.mp.dps=30
_K={}
def Kmat(p,q,r):
    key=(p,q,r)
    if key not in _K:
        p_,q_,r_=map(mp.mpf,(float(p),float(q),float(r)))
        phi=lambda th: p_*mp.cos(th)**2+q_*mp.cos(th)*mp.sin(th)+r_*mp.sin(th)**2
        K11=mp.quad(lambda th: mp.cos(th)**2/(2*phi(th)**2),[0,mp.pi/2])
        K12=mp.quad(lambda th: mp.cos(th)*mp.sin(th)/(2*phi(th)**2),[0,mp.pi/2])
        K22=mp.quad(lambda th: mp.sin(th)**2/(2*phi(th)**2),[0,mp.pi/2])
        Ar=mp.quad(lambda th: 1/(2*phi(th)),[0,mp.pi/2])
        assert abs(float(Ar)-area(p,q,r))<1e-12
        _K[key]=(float(K11),float(K12),float(K22))
    return _K[key]
B1=lambda y: y-0.5
B2=lambda y: y*y-y+1/6
def A012(al,be,x,corner_sign=1.0):
    A0=A1=A2=0j
    for sg,c,U in PIECES:
        d=piece_data(al,be,x,c,U); N=d['N']; f=np.exp(2j*np.pi*d['k']/d['M'])
        y1=d['z1']/N; y2=d['z2']/N; mf=f.mean()
        w1=(f*B1(y1)).sum()/N; w2=(f*B1(y2)).sum()/N
        p,q,r=d['p'],d['q'],d['r']; l1,l2=float(d['l1']),float(d['l2'])
        ac=(al[0]+c[0],al[1]+c[1]); Q0=float(Fr(Bi(ac,ac),2))
        K11,K12,K22=Kmat(p,q,r); Ar=area(p,q,r); Ja,Jb=J(p,q,r)
        pf,qf,rf=float(p),float(q),float(r)
        A0+=float(sg)*mf*Ar
        A1+=float(sg)*(-mf*(l1*Ja+l2*Jb)-(SQPI/2)*(w1/math.sqrt(rf)+w2/math.sqrt(pf)))
        a2=mf*(0.5*(l1*l1*K11+2*l1*l2*K12+l2*l2*K22)-Q0*Ar)+w1*l2/(2*rf)+w2*l1/(2*pf) \
           +(qf/4)*((f*B2(y1)).sum()/rf+(f*B2(y2)).sum()/pf)+corner_sign*(f*B1(y1)*B1(y2)).sum()
        A2+=float(sg)*a2
    for sg,c,u in WALLS:
        d=wall_data(al,be,x,c,u); N=d['N']; f=np.exp(2j*np.pi*d['k']/d['M'])
        ac=(al[0]+c[0],al[1]+c[1]); Qu=float(d['Qu'])
        A1+=float(sg)*(SQPI/2)*f.mean()/math.sqrt(Qu)
        A2+=float(sg)*(-f.mean()*Bi(u,ac)/(2*Qu)-(f*B1(np.arange(N)/N)).sum())
    return A0,A1,A2
def corner_mag(al,be,x):
    s=0j
    for sg,c,U in PIECES:
        d=piece_data(al,be,x,c,U); N=d['N']; f=np.exp(2j*np.pi*d['k']/d['M'])
        s+=float(sg)*(f*B1(d['z1']/N)*B1(d['z2']/N)).sum()
    return abs(s)
