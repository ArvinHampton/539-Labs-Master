# order-3 step: split A1 (order2 entry-107 formula) into drift D, rays R, sawtooth walls W[1], W[7/2], W[595/2].
import sys; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import *
def parts(al,be,x):
    out={'A0':0j,'D':0j,'R':0j,'W1':0j,'W7/2':0j,'W595/2':0j}
    for sg,c,U in PIECES:
        d=piece_data(al,be,x,c,U); N=d['N']; f=np.exp(2j*np.pi*d['k']/d['M'])
        mf=f.mean(); w1=(f*(d['z1']/N-0.5)).sum()/N; w2=(f*(d['z2']/N-0.5)).sum()/N
        Ja,Jb=J(d['p'],d['q'],d['r']); s=float(sg)
        out['A0']+=s*mf*area(d['p'],d['q'],d['r'])
        out['D']+=s*(-mf*(float(d['l1'])*Ja+float(d['l2'])*Jb))
        # W_1 : wall a=0, Gaussian along u2 (Q=r); W_2 : wall b=0, along u1 (Q=p)
        for w,Qv in ((w1,d['r']),(w2,d['p'])):
            key={Fr(1):'W1',Fr(7,2):'W7/2',Fr(595,2):'W595/2'}[Qv]
            out[key]+=s*(-(SQPI/2)*w/math.sqrt(float(Qv)))
    for sg,c,u in WALLS:
        d=wall_data(al,be,x,c,u); f=np.exp(2j*np.pi*d['k']/d['M'])
        out['R']+=float(sg)*(SQPI/2)*f.mean()/math.sqrt(float(d['Qu']))
    out['A1']=out['D']+out['R']+out['W1']+out['W7/2']+out['W595/2']
    return out
