import sys; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order2/scripts')
from lib2 import *
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
def rays(al,be,x):
    o={Fr(7,2):0j,Fr(595,2):0j}
    for sg,c,u in WALLS:
        d=wall_data(al,be,x,c,u); f=np.exp(2j*np.pi*d['k']/d['M'])
        o[d['Qu']]+=float(sg)*(SQPI/2)*f.mean()/math.sqrt(float(d['Qu']))
    return o[Fr(7,2)],o[Fr(595,2)]
R7=np.zeros((216,105),complex);R595=R7.copy();S7=R7.copy();S595=R7.copy()
for ix,x in enumerate(XS):
    for j,(al,be) in enumerate(pairs):
        R7[ix,j],R595[ix,j]=rays(al,be,x); S7[ix,j],S595[ix,j]=rays(al,be,-1/x)
np.savez('../data/rays_split.npz',R7=R7,R595=R595,S_R7=S7,S_R595=S595)
