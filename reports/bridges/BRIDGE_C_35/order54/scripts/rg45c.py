# order54 RG45c-2. PREREG sha af2e5c10...1404
import sys,json,math,numpy as np
from scipy.special import erfcx
src=open('/workspace/quantum-comp/reports/bridges/BRIDGE_C_35/order18/scripts/a2.py').read().split('\n')
exec('\n'.join(src[:30]))   # read-only import of lib2/symbols/pairs/period/ph/B1b
SQ=math.sqrt(math.pi)
def Qf(n1,n2): return n1*n1+7*n1*n2+3.5*n2*n2
WALL={1:dict(u=(0,1),Qu=3.5),2:dict(u=(21,-1),Qu=297.5)}
def direct(al,be,x,w,t):
    a1,a2=float(al[0]),float(al[1]); y=t/(2*math.pi)
    th=a1 if w==1 else a1+21*a2
    dec=2.5 if w==1 else 1/34
    L=int(math.ceil(8/math.sqrt(dec*t)))+2
    l=np.arange(-L,L+1); lam=l+th
    if w==1:
        B=int(math.ceil(9/math.sqrt(3.5*t)))+3; b=np.arange(-B,B+1)
        cen=-np.round(lam).astype(int)  # nu1+nu2 ~ 0 -> k ~ -n
        n=l[:,None]+0*b[None,:]; k=cen[:,None]+b[None,:]
        z=math.sqrt(10*y)*lam
    else:
        B=int(math.ceil(9/math.sqrt(297.5*t)))+3; b=np.arange(-B,B+1)
        cen=np.round(lam/17).astype(int)  # nu2 ~ 35 lam/595 = lam/17 ; v=(l+21b',-b') with nu2=a2-b'
        bp=-cen[:,None]+b[None,:]
        n=l[:,None]+21*bp; k=-bp
        z=math.sqrt(2*y/17)*lam
    nu1=a1+n; nu2=a2+k
    pts=np.stack([n,k],-1)
    kk,M=phase_ints(al,be,x,pts); f=np.exp(2j*np.pi*kk/M)
    az=SQ*np.abs(z)
    ex=-az[:,None]**2 - t*Qf(nu1,nu2)
    hv=-np.sign(z)[:,None]*erfcx(az)[:,None]*np.exp(ex)
    return 0.5*np.sum(hv*f)
def pred(al,be,x,w,b0=0.0):
    u=WALL[w]['u']; Nt=period(al,be,x,(1,0)); a1,a2=Fr(al[0]),Fr(al[1])
    th=a1 if w==1 else a1+21*a2; s=0j; hit=False
    for r in range(Nt):
        P=period(al,be,x,u); bb=np.arange(P)
        m=ph(al,be,x,np.array([r,0])[None,:]+bb[:,None]*np.array(u)[None,:]).mean()
        q=Fr(r+th)/Nt
        if q.denominator==1:
            s+=m*b0; hit = hit or abs(m)>1e-12
        else: s+=m*B1b(q)
    return math.sqrt(math.pi/WALL[w]['Qu'])*s, hit
TS=[4e-3,2e-3,1e-3]
out=[];worst=0;ctrl=0;nhit=0
for x in XS[:6]:
  for j,(al,be) in enumerate(pairs):
    for w in (1,2):
      v=np.array([math.sqrt(t)*direct(al,be,x,w,t) for t in TS])
      A=np.polyfit(TS,v.real,2)[-1]+1j*np.polyfit(TS,v.imag,2)[-1]
      p,hit=pred(al,be,x,w); pc,_=pred(al,be,x,w,-0.5)
      e=abs(A-p)/max(1,abs(p)); worst=max(worst,e)
      if hit: nhit+=1; ctrl=max(ctrl,abs(A-pc))
      out.append(dict(x=str(x),j=j,w=w,A1_num=[A.real,A.imag],A1_pred=[p.real,p.imag],relerr=e,endpoint_hit=bool(hit)))
  print('x',x,'worst',worst,'nhit',nhit,'ctrl',ctrl,flush=True)
ctrl_status='VOID' if nhit==0 else ('FAIL(good)' if ctrl>1e-4 else 'PASSED(bad)')
PASS=bool(worst<=1e-6) and ctrl_status=='FAIL(good)'
r=dict(worst_relerr=worst,n_endpoint_cases=nhit,control_maxdev=ctrl,control=ctrl_status,PASS=PASS,n=len(out))
print(json.dumps(r)); json.dump(dict(r=r,rows=out),open('../data/rg45c.json','w'),indent=1)
