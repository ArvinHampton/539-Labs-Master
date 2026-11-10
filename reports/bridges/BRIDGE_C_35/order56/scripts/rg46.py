# order56 RG46. PREREG sha in ../PREREG.sha256
import os,sys,json,math,numpy as np
from multiprocessing import Pool
B='/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/'
here=os.path.dirname(os.path.abspath(__file__))
os.chdir(B+'order54/scripts'); exec(open('rg45c.py').read().split('TS=[')[0]); os.chdir(here)
from lib2 import PIECES, piece_data, J, SQPI
def lineper(al,be,x,c,u):
    N=2*Fr(x).denominator
    for mult in (1,2,5,7,10,14,35,70,140):
        P=N*mult; j=np.arange(P); pts=np.array(c)[None,:]+j[:,None]*np.array(u)[None,:]
        k1,_=phase_ints(al,be,x,pts); k2,_=phase_ints(al,be,x,pts+P*np.array(u))
        if (k1==k2).all(): return pts
    raise RuntimeError
def sgf(q): return (q>0)-(q<0)
def strip(al,be,x):
    s=0j; a1,a2=Fr(al[0]),Fr(al[1])
    for w,th in ((1,a1),(2,a1+21*a2)):
        u=WALL[w]['u']; lo=math.floor(min(0,-th)); hi=math.ceil(max(0,-th))
        for l in range(lo,hi+1):
            d=Fr(sgf(l)-sgf(l+th),2)
            if d==0: continue
            s+=float(d)*math.sqrt(math.pi/WALL[w]['Qu'])*ph(al,be,x,lineper(al,be,x,(l,0),u)).mean()
    return s
def orth(al,be,x):
    sg,c,U=PIECES[0]; d=piece_data(al,be,x,c,U); N=d['N']; f=np.exp(2j*np.pi*d['k']/d['M'])
    mf=f.mean(); w1=(f*(d['z1']/N-0.5)).sum()/N; w2=(f*(d['z2']/N-0.5)).sum()/N; Ja,Jb=J(d['p'],d['q'],d['r'])
    return float(sg)*(-mf*(float(d['l1'])*Ja+float(d['l2'])*Jb)-(SQPI/2)*(w1/math.sqrt(float(d['r']))+w2/math.sqrt(float(d['p']))))
def row(i):
    x=XS[i]; out=[]
    for X in (x,-1/x):
        r=[]
        for al,be in pairs: r.append((pred(al,be,X,1)[0]+pred(al,be,X,2)[0],strip(al,be,X),orth(al,be,X)))
        out.append(r)
    return out
if __name__=='__main__':
    with Pool(8) as p: R=p.map(row,range(216))
    R=np.array(R)  # 216,2,105,3
    P=np.load(B+'order3/data/parts.npz')
    res={}
    for tag,A1,k in (('x',P['A1'],0),('S',P['S_A1'],1)):
        Xi,St,Or=R[:,k,:,0],R[:,k,:,1],R[:,k,:,2]; sc=np.maximum(1,abs(A1))
        res[tag]=dict(dev=float((abs(A1-Xi+St-Or)/sc).max()),ctrl=float((abs(A1-Xi-St-Or)/sc).max()),strip_max=float(abs(St).max()),xi_max=float(abs(Xi).max()))
    a=res['x'];b=res['S']
    res['RG46a_PASS']=bool(max(a['dev'],b['dev'])<=1e-9); res['ctrl_fail_good']=bool(max(a['ctrl'],b['ctrl'])>1e-4); res['nonvacuous']=bool(max(a['strip_max'],b['strip_max'])>1e-6)
    xs=np.array([abs(float(x)) for x in XS])
    def rk(M): s=np.linalg.svd(M,compute_uv=False); return int((s/s[0]>1e-9).sum())
    def t(F,FS,w): r=rk(F); j=rk(np.hstack([F,(xs**w)[:,None]*FS])); return dict(rank=r,joint=j,closed=r==j)
    H=P['A1']-R[:,0,:,0]+R[:,0,:,1]; HS=P['S_A1']-R[:,1,:,0]+R[:,1,:,1]
    res['gate_w1']=t(P['A0'],P['S_A0'],1.0); res['gate_wrong']=t(P['A0'],P['S_A0'],-1.0)
    res['gate_pass']=res['gate_w1']['rank']==36 and res['gate_w1']['closed'] and res['gate_wrong']['joint']>36
    for w in (0.5,1.0): res['Ahat_w%s'%w]=t(H,HS,w)
    res['RG46b_PASS']=bool(res['gate_pass'] and any(res['Ahat_w%s'%w]['closed'] for w in (0.5,1.0)))
    print(json.dumps(res,indent=1)); json.dump(res,open('../data/rg46.json','w'),indent=1)
    np.save('../data/rg46_raw.npy',R)
