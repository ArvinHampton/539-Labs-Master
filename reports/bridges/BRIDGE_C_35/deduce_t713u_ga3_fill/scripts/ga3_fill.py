# t713u G-A3 fill: regenerate Xi to N_trunc, compute psi, h^high, delta. See PREREG.md.
import sys, math, cmath, json
from fractions import Fraction as Fr
PSI_DIR="/workspace/quantum-comp/reports/heavy-daily/2026-10-17-psi-cocycle"
sys.path.insert(0,PSI_DIR)
import os; os.chdir(PSI_DIR)
from fastkappa import psi as psi_pos, cone_terms, REPS, a as A_, ma, zero
def psi_any(x):
    x=Fr(x)
    if x>0: return psi_pos(x)
    kL=cone_terms(A_,zero,-1/x)[1]; sk=sum(cone_terms(p,ma,x)[1] for p in REPS)
    return kL-abs(float(x))/math.sqrt(35)*sk
def xi_table(N, partials=False):
    c={}
    def add(nu,v): c[nu]=c.get(nu,0)+v
    m=1
    while 35*m*m+7*m+(7*m)**2<=N:
        a=Fr(7*m); o=Fr(35*m*m+7*m); n=0
        while o+(n+a)**2<=N: add(o+(n+a)**2, n+a); n+=1
        m+=1
    m=0
    while Fr(35*m*m+42*m)+Fr(49,4)+(7*m+Fr(7,2))**2<=N:
        a=7*m+Fr(7,2); o=35*m*m+42*m+Fr(49,4); n=0
        while o+(n+a)**2<=N: add(o+(n+a)**2, n+a); n+=1
        m+=1
    if partials:
        for nu in (43,58,67): add(Fr(nu),Fr(1))
    return dict(sorted(c.items()))
E=lambda z: cmath.exp(2j*math.pi*z)
def I(x,c): return sum(-cmath.exp(1j*math.pi/4)*float(v)*E(float(nu)*x)/math.sqrt(2*float(nu)) for nu,v in c.items())
def h(x,c): return psi_any(x)*cmath.exp(-1j*math.pi/4) - I(float(x),c)
A,B,C,D=10.6923,0.2160,2.7618,-7.5316
def slash(x):
    t=7*x-3; return abs(7*x)**-0.5*(A+B*t+C*t*t+D/(1+t*t)), abs(7*x)**-0.5*5e-5*(1+abs(t)+t*t+1/(1+t*t))
if __name__=="__main__":
    N=int(sys.argv[1]) if len(sys.argv)>1 else 106
    out={}
    for var in ("main","partials"):
        c=xi_table(N, var=="partials"); rows=[]
        for x in (Fr(1,7),Fr(3,7),Fr(5,7),Fr(1)):
            wx=-1/(7*x); ps=psi_any(x); hx=h(x,c); hw=h(wx,c); s,sig=slash(float(x))
            d=hx-s*hw; tol=10*(1e-12+sig*abs(hw))
            rows.append(dict(x=str(x),Wx=str(wx),psi=[ps.real,ps.imag],psiW=[psi_any(wx).real,psi_any(wx).imag],h=[hx.real,hx.imag],hW=[hw.real,hw.imag],slash=s,delta=[d.real,d.imag],absdelta=abs(d),tol=tol))
        out[var]=dict(N=N,table={str(k):str(v) for k,v in c.items()},rows=rows)
    print(json.dumps(out,indent=1))
