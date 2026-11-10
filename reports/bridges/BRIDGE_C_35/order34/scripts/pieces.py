# corner split into the three written pieces (same arithmetic as cornerlib.corner)
from cornerlib import *
def corner_pieces(al,be,x,u1,u2):
    N=math.lcm(period(al,be,x,(1,0)),period(al,be,x,(0,1)))
    i=np.arange(N); V=np.stack(np.meshgrid(i,i,indexing='ij'),-1).reshape(-1,2)
    k0,Mm=phase_ints(al,be,x,V); f=np.exp(2j*np.pi*k0/Mm)
    U=np.array([u1,u2]).T; assert abs(round(np.linalg.det(U)))==1
    Ui=np.round(np.linalg.inv(U)).astype(np.int64)
    q=math.lcm(Fr(al[0]).denominator,Fr(al[1]).denominator)
    an=np.array([int(Fr(al[0])*q),int(Fr(al[1])*q)])
    W=(an[None,:]+q*V)@Ui.T; o=[]
    for c in range(2):
        fr,z=fracs(W[:,c],q*N); o.append((np.where(z,0.0,fr-0.5),fr*fr-fr+1/6))
    Bu=Bi(u1,u2); Q1=Bi(u1,u1)/2; Q2=Bi(u2,u2)/2
    return np.sum(f*(Bu/(4*Q1)*o[1][1])), np.sum(f*(Bu/(4*Q2)*o[0][1])), np.sum(f*o[0][0]*o[1][0])   # T_e1, T_other, T_BB
