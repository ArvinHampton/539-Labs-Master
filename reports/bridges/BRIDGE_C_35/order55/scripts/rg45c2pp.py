# order55 RG45c-2' . PREREG sha 0cbb763f...fe22
import os,sys,json,math,time,numpy as np
from multiprocessing import Pool
O54='/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order54/scripts/'
os.chdir(O54); exec(open('rg45c.py').read().split('TS=[')[0]); os.chdir(os.path.dirname(os.path.abspath(__file__)))
def directc(al,be,x,w,t,CH=None):
    a1,a2=float(al[0]),float(al[1]); y=t/(2*math.pi)
    thF=Fr(al[0]) if w==1 else Fr(al[0])+21*Fr(al[1]); th=float(thF)
    dec=2.5 if w==1 else 1/34
    L=int(math.ceil(8/math.sqrt(dec*t)))+2
    if w==1: B=int(math.ceil(9/math.sqrt(3.5*t)))+3
    else: B=int(math.ceil(9/math.sqrt(297.5*t)))+3
    b=np.arange(-B,B+1); CH=max(1,int(2e6//len(b))); tot=0j
    for s in range(-L,L+1,CH):
        l=np.arange(s,min(s+CH,L+1)); lam=l+th; lam[(l*thF.denominator+thF.numerator)==0]=0.0
        if w==1:
            cen=-np.round(lam).astype(int); n=l[:,None]+0*b[None,:]; k=cen[:,None]+b[None,:]
            z=math.sqrt(10*y)*lam
        else:
            cen=np.round(lam/17).astype(int); bp=-cen[:,None]+b[None,:]
            n=l[:,None]+21*bp; k=-bp; z=math.sqrt(2*y/17)*lam
        nu1=a1+n; nu2=a2+k
        kk,M=phase_ints(al,be,x,np.stack([n,k],-1)); f=np.exp(2j*np.pi*kk/M)
        az=SQ*np.abs(z)
        hv=-np.sign(z)[:,None]*erfcx(az)[:,None]*np.exp(-az[:,None]**2-t*Qf(nu1,nu2))
        tot+=0.5*np.sum(hv*f)
    return tot
def run(c):
    x,j,w=c; al,be=pairs[j]; t0=time.time()
    try:
        Ps=max(period(al,be,x,WALL[w]['u']),period(al,be,x,(1,0)))
        T=math.pi**2/(40*WALL[w]['Qu']*Ps**2); TS=[T,T/2,T/4]
        v=np.array([math.sqrt(t)*directc(al,be,x,w,t) for t in TS])
        A=np.polyfit(TS,v.real,2)[-1]+1j*np.polyfit(TS,v.imag,2)[-1]
        p,hit=pred(al,be,x,w); pc,_=pred(al,be,x,w,-0.5)
        return dict(x=str(x),j=j,w=w,Pstar=Ps,T=T,A1_num=[A.real,A.imag],A1_pred=[p.real,p.imag],
          relerr=abs(A-p)/max(1,abs(p)),endpoint_hit=bool(hit),ctrl_dev=float(abs(A-pc)),sec=time.time()-t0)
    except Exception as e: return dict(x=str(x),j=j,w=w,error=repr(e),relerr=float('inf'),endpoint_hit=False,ctrl_dev=0.0)
if __name__=='__main__':
    C=[(x,j,w) for x in XS[:6] for j in range(0,105,5) for w in (1,2)]+[(Fr(1,14),26,1),(Fr(1,14),14,2)]
    C.sort(key=lambda c:-c[2])  # wall 2 first (load balance)
    out=[]
    with Pool(8) as pool:
        for r in pool.imap_unordered(run,C):
            out.append(r); print(len(out),r['x'],r['j'],r['w'],r.get('Pstar'),'%.2e'%r['relerr'],'%.1fs'%r.get('sec',0),flush=True)
    worst=max(r['relerr'] for r in out); hits=[r for r in out if r['endpoint_hit']]
    ctrl=max([r['ctrl_dev'] for r in hits],default=0)
    cs='VOID' if not hits else ('FAIL(good)' if ctrl>1e-4 else 'PASSED(bad)')
    pw={w:max(r['relerr'] for r in out if r['w']==w) for w in (1,2)}
    R=dict(n=len(out),worst_relerr=worst,worst_by_wall=pw,n_endpoint_cases=len(hits),control_maxdev=ctrl,control=cs,
           n_errors=sum('error' in r for r in out),PASS=bool(worst<=1e-6 and cs=='FAIL(good)'))
    print(json.dumps(R)); json.dump(dict(r=R,rows=out),open('../data/rg45c2pp.json','w'),indent=1)
