# T0: exact, unconditional class data for O = Z[sqrt n] (disc 4n), n = s(s-2), and the maximal order.
# Cl via Gauss reduction cycles (same algorithm as A34/scripts/classno_exact.py), group law via composition of
# forms with coprime leading coefficients (exact integers), fundamental unit via continued fraction of sqrt n,
# (O/DO)^x order and exponent by exhaustive enumeration over prime powers. No PARI, no GRH.
import sys, math, json, itertools
from fractions import Fraction as Fr
sys.dont_write_bytecode=True
def reduced_forms(D):
    r=math.isqrt(D); out=[]; sq=math.sqrt(D)
    for b in range(1,r+1):
        if (b*b-D)%4: continue
        ac=(b*b-D)//4
        for a in range(1,2*r+2):
            if ac%a: continue
            c=ac//a
            for A,C in ((a,c),(-a,-c)):
                if math.gcd(math.gcd(abs(A),b),abs(C))!=1: continue
                if sq-b<2*abs(A)<sq+b: out.append((A,b,C))
    return sorted(set(out))
def isred(f,D):
    # exact test: 0<b<sqrtD, sqrtD-b<2|a|<sqrtD+b  (D non-square, compare squares)
    a,b,c=f; A=2*abs(a)
    if b<=0 or b*b>=D: return False
    return (A+b)**2>D and (A-b<0 or (A-b)**2<D)
def rho(f,D):
    a,b,c=f; cc=abs(c); r=math.isqrt(D)
    bp=(-b)%(2*cc)
    # want sqrtD-2|c| < bp < sqrtD  (if |c|<sqrtD), else -|c|<bp<=|c|
    if cc<= r:
        while bp<=r-2*cc or (bp==r-2*cc+0 and False): bp+=2*cc
        while bp> r: bp-=2*cc
        while bp+2*cc<=r: bp+=2*cc
    else:
        while bp>cc: bp-=2*cc
        while bp<=-cc: bp+=2*cc
    return (c,bp,(bp*bp-D)//(4*c))
def reduce_form(f,D):
    for _ in range(100000):
        if isred(f,D): return f
        f=rho(f,D)
    raise RuntimeError(f)
class Cl:
    def __init__(self,D):
        self.D=D; R=reduced_forms(D); S=set(R); seen=set(); self.cycles=[]
        for f in R:
            if f in seen: continue
            cyc=[];g=f
            while g not in seen:
                assert g in S; seen.add(g); cyc.append(g); g=rho(g,D)
            self.cycles.append(cyc)
        self.idx={g:i for i,c in enumerate(self.cycles) for g in c}
        self.hplus=len(self.cycles)
        neg=[self.idx[(-c[0][0],c[0][1],-c[0][2])] for c in self.cycles]
        self.neg=neg
        self.wide=sorted({tuple(sorted((i,neg[i]))) for i in range(self.hplus)})
        self.widx={}
        for j,o in enumerate(self.wide):
            for i in o: self.widx[i]=j
        self.h=len(self.wide)
    def cls(self,f): return self.idx[reduce_form(f,self.D)]
    def equiv_with_a(self,f,avoid):
        # properly equivalent form whose first coefficient is coprime to avoid
        a,b,c=f
        for x in range(0,60):
            for y in range(-60,61):
                if math.gcd(x,y)!=1: continue
                m=a*x*x+b*x*y+c*y*y
                if m==0 or math.gcd(m,avoid)!=1: continue
                # complete [[x,r],[y,t]] with xt-ry=1
                g,t,r_=self._eg(x,y); r_=-r_  # x*t - y*r = 1
                assert x*t-y*r_==1
                B=2*a*x*r_+b*(x*t+y*r_)+2*c*y*t
                C=a*r_*r_+b*r_*t+c*t*t
                return (m,B,C)
        raise RuntimeError
    @staticmethod
    def _eg(x,y):
        # returns (g,t,r) with x*t + y*r = g
        if y==0: return (x, 1 if x>0 else -1, 0)
        g,a_,b_=Cl._eg(y,x%y); return (g,b_,a_-(x//y)*b_)
    def compose(self,f,g):
        D=self.D; f2=self.equiv_with_a(f,1); g2=self.equiv_with_a(g,abs(f2[0]))
        a1,b1,_=f2; a2,b2,_=g2; M=2*abs(a1*a2)
        for B in range(M):
            if (B-b1)%(2*abs(a1))==0 and (B-b2)%(2*abs(a2))==0 and (B*B-D)%(4*abs(a1*a2))==0:
                return reduce_form((a1*a2,B,(B*B-D)//(4*a1*a2)),D)
        raise RuntimeError
    def rep(self,i): return self.cycles[i][0]
    def order_narrow(self,i):
        e=self.idx[(1,)+self._principal()[1:]] if False else self.cls(self._principal())
        f=self.rep(i); k=1; g=f
        while self.cls(g)!=e: g=self.compose(g,f); k+=1
        return k
    def _principal(self):
        D=self.D; b=D%2
        return (1,b,(b*b-D)//4)
    def wide_structure(self):
        # orders of wide classes; |Cl[2]| ; cyclic?
        e=self.widx[self.cls(self._principal())]
        orders={}
        for j,o in enumerate(self.wide):
            f=self.rep(o[0]); g=f; k=1
            while self.widx[self.cls(g)]!=e: g=self.compose(g,f); k+=1
            orders[j]=k
        two=sum(1 for v in orders.values() if v<=2)
        return orders, two, max(orders.values())==self.h
def fund_unit(n):
    # smallest x+y sqrt n >1 with x^2-n y^2 = +-1 via continued fraction of sqrt n (exact integers)
    a0=math.isqrt(n); m,d,a=0,1,a0; p0,p1=1,a0; q0,q1=0,1
    while True:
        if p1*p1-n*q1*q1 in (1,-1): return (p1,q1,p1*p1-n*q1*q1)
        m=d*a-m; d=(n-m*m)//d; a=(a0+m)//d
        p0,p1=p1,a*p1+p0; q0,q1=q1,a*q1+q0
def factor(n):
    f={};p=2
    while p*p<=n:
        while n%p==0: f[p]=f.get(p,0)+1; n//=p
        p+=1
    if n>1: f[n]=f.get(n,0)+1
    return f
def unit_group_modq(n,q):
    # (Z/q)[t]/(t^2-n) units: list as pairs (x,y)
    U=[(x,y) for x in range(q) for y in range(q) if math.gcd((x*x-n*y*y)%q,q)==1]
    return U
def mul(u,v,n,q): return ((u[0]*v[0]+n*u[1]*v[1])%q,(u[0]*v[1]+u[1]*v[0])%q)
def order(u,n,q):
    k=1;g=u
    while g!=(1%q,0): g=mul(g,u,n,q); k+=1
    return k
def OD_data(n,D):
    tot=1; ex=1
    for p,e in factor(D).items():
        q=p**e; U=unit_group_modq(n,q); tot*=len(U); ex=math.lcm(ex,*[order(u,n,q) for u in U])
    return tot,ex
def subgroup_order(gens,n,D):
    # order of subgroup of (O/D)^x generated by gens (BFS)
    one=(1%D,0); S={one}; fr=[one]
    while fr:
        nf=[]
        for x in fr:
            for g in gens:
                y=mul(x,g,n,D)
                if y not in S: S.add(y); nf.append(y)
        fr=nf
    return len(S)
def data(s):
    n=s*(s-2); import numpy as np
    Dlab=math.lcm(n,2*(s-2))
    C=Cl(4*n); orders,two,cyc=C.wide_structure()
    x,y,nm=fund_unit(n)
    eplus=(x,y) if nm==1 else ((x*x+n*y*y),(2*x*y))
    tot,ex=OD_data(n,Dlab)
    U=subgroup_order([((-1)%Dlab,0),(eplus[0]%Dlab,eplus[1]%Dlab)],n,Dlab)
    G0=Fr(C.h*tot,U)
    return {'s':s,'n':n,'D_label':Dlab,'disc':4*n,'h_narrow':C.hplus,'h_wide':C.h,'wide_class_orders':sorted(orders.values()),
            'Cl_wide_cyclic':cyc,'Cl_wide_2torsion':two,'ring_class_cusp_pairs':(C.h-two)//2,
            'fund_unit':[x,y],'fund_unit_norm':nm,'eps_s_is_power':None,
            'OD_units_order':tot,'OD_units_exponent':ex,'unit_image_order':U,'G0_order':int(G0),'E_bound':ex*C.h}
if __name__=='__main__':
    out=[]
    for s in [int(a) for a in sys.argv[1].split(',')]:
        d=data(s); n=d['n']
        # is eps_s=(s-1)+sqrt n a power of the fundamental unit?
        x,y=d['fund_unit']; g=(x,y); k=1
        while g[0]<s-1 and k<50: g=(g[0]*x+n*g[1]*y,g[0]*y+g[1]*x); k+=1
        d['eps_s_is_power']=k if g==(s-1,1) else 'no'
        print(json.dumps(d),flush=True); out.append(d)
    json.dump(out,open(sys.argv[2],'w'),indent=1)
