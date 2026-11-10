# task (a) radial data on XS216: orthant piece, H part, odd combination, axis false thetas F, line corrections U_H, U_O
import sys, math, pickle; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
from lib5mp import *
import lib5mp
from lib2 import XS
from symbols import FAM, sym_pair
def sgn(v): return (v>0)-(v<0)
def line_walls(al):
    a1,a2=al; s=a1+21*a2; UH=[]; UO=[]
    for n in range(math.floor(min(0,-a1))-2, math.ceil(max(0,-a1))+3):
        w=Fr(sgn(n+a1)-sgn(n),2)
        if w: UH.append((w,(n,0),(0,1))); UO.append((w,(n,0),(0,1)))
    for m in range(math.floor(min(0,-s))-2, math.ceil(max(0,-s))+3):
        w=Fr(sgn(m+s)-sgn(m),2)
        if w: UH.append((w,(m,0),(21,-1)))
    for k in range(math.floor(min(0,-a2))-2, math.ceil(max(0,-a2))+3):
        w=Fr(sgn(k+a2)-sgn(k),2)
        if w: UO.append((w,(0,k),(1,0)))
    full=lambda L:[t for (w,p,u) in L for t in ((w,p,u),(w,(p[0]-u[0],p[1]-u[1]),(-u[0],-u[1])))]
    return full(UH),full(UO)
FW=[(Fr(1,2),(1,0),(1,0)),(Fr(-1,2),(-1,0),(-1,0)),(Fr(1,2),(0,1),(0,1)),(Fr(-1,2),(0,-1),(0,-1))]
neg=lambda v:(-v[0],-v[1])
k,K=int(sys.argv[1]),int(sys.argv[2])
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
names=['full','orth','fullneg','F','UH','UO']
out={}
for i in range(216):
    if i%K!=k: continue
    for sx,x in (('x',XS[i]),('S',-1/XS[i])):
        rows=[]
        for al,be in pairs:
            UH,UO=line_walls(al)
            r=[A012mp(al,be,x),A012mp(al,be,x,pieces=PIECES[:1],walls=[]),A012mp(neg(al),neg(be),x),
               A012mp(al,be,x,pieces=[],walls=FW),A012mp(al,be,x,pieces=[],walls=UH),A012mp(al,be,x,pieces=[],walls=UO)]
            rows.append([[complex(v) for v in t] for t in r])
        out[(i,sx)]=rows
        lib5mp._ET.clear()
    print(i,flush=True)
pickle.dump(out,open('../data/a_chunk_%d.pkl'%k,'wb'))
