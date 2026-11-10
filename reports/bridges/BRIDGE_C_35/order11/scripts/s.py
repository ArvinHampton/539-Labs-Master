# order11 N1-N3 + control; mpmath
import sys, json; sys.dont_write_bytecode=True
sys.path.insert(0,'/workspace/quantum-comp/reports/s_family_paths/A35_lawspace_exact')
import mpmath as mp
from fractions import Fraction as Fr
from symbols import FAM, sym_pair, S_rows, L as LL
mp.mp.dps=int(sys.argv[1]) if len(sys.argv)>1 else 30
pairs=[sym_pair(f,i) for f in FAM for i in range(35)]
Gi=((13,7),(-2,-1)); ap=lambda Mx,v:(Mx[0][0]*v[0]+Mx[0][1]*v[1],Mx[1][0]*v[0]+Mx[1][1]*v[1])
M=mp.matrix(105,105)
for j,d in enumerate(S_rows()):
    for kk,es in d.items():
        for e in es: M[j,kk]+=mp.expjpi(mp.mpf(2*e)/LL)
fm=lambda r: mp.mpf(r.numerator)/r.denominator
ef=lambda r: mp.expjpi(2*fm(Fr(r)%1))
eq=lambda Q,tau: mp.exp(2j*mp.pi*fm(Q)*tau)
sgn=lambda v:(v>0)-(v<0)
def ThE(al,be,tau):
    s=0
    for n in range(-9,10):
        for k in range(-7,8):
            nu=(al[0]+n,al[1]+k); p=Fr(1+sgn(nu[0])*sgn(nu[1]),2)
            if not p: continue
            Q=nu[0]**2+7*nu[0]*nu[1]+Fr(7,2)*nu[1]**2
            if Q>45: continue
            s+=p*eq(Q,tau)*ef(nu[0]*(2*be[0]+7*be[1])+nu[1]*(7*be[0]+7*be[1]))
    return s
def th72(al,be,tau): return sum(eq(Fr(7,2)*m*m,tau)*ef(7*(be[0]+be[1])*m) for m in (al[0]+al[1]+n for n in range(-7,8)))
def Tc1(al,be,tau):
    y=tau.imag; s=0
    for n in range(-9,10):
        u=al[0]+n
        if u==0: continue
        s+=sgn(u)*mp.erfc(mp.sqrt(10*mp.pi*y)*abs(fm(u)))*eq(-Fr(5,2)*u*u,tau)*ef(-5*be[0]*u)
    return -th72(al,be,tau)*s
def W(al,be,tau): return Tc1(al,be,tau)-Tc1(ap(Gi,al),ap(Gi,be),tau)
def vtheta(al,be,tau): return sum(fm(u)*eq(Fr(5,2)*u*u,tau)*ef(5*be[0]*u) for u in (al[0]+n for n in range(-9,10)))
def GO(al,be,tau,B=16):
    y=tau.imag; s=0; sp=mp.sqrt(mp.pi)
    for n in range(-B,B+1):
        for k in range(-B,B+1):
            nu=(al[0]+n,al[1]+k); Q=nu[0]**2+7*nu[0]*nu[1]+Fr(7,2)*nu[1]**2
            a1=mp.sqrt(10*y)*fm(nu[0]); a2=mp.sqrt(35*y)*fm(nu[1]); s1=sgn(nu[0]); s2=sgn(nu[1])
            if s1==-s2 and s1!=0: w=s1*(mp.erfc(sp*abs(a2))-mp.erfc(sp*abs(a1)))/2
            else: w=(s1*(1-mp.erfc(sp*abs(a1)))+s2*(1-mp.erfc(sp*abs(a2))))/2
            if w==0: continue
            s+=w*eq(Q,tau)*ef(nu[0]*(2*be[0]+7*be[1])+nu[1]*(7*be[0]+7*be[1]))
    return s
neg=lambda v:(-v[0],-v[1])
taus=[mp.mpc(0.1,0.95),mp.mpc(-0.2,1.05),mp.mpc(0.3,0.9)]
out={}
# N1
t=taus[0]; n1T=max(abs(W(neg(a),neg(b),t)+W(a,b,t)) for a,b in pairs); n1E=max(abs(ThE(neg(a),neg(b),t)-ThE(a,b,t)) for a,b in pairs)
out['N1']=dict(T_odd=mp.nstr(n1T,4),ThE_even=mp.nstr(n1E,4)); print(out,flush=True)
# N2
al,be=pairs[1]; f=lambda x,y: Tc1(al,be,mp.mpc(x,y)); x0,y0=mp.mpf('0.1'),mp.mpf('0.95')
dbar=(mp.diff(lambda x:f(x,y0),x0)+1j*mp.diff(lambda y:f(x0,y),y0))/2
pred=1j*mp.sqrt(10)/2*y0**-0.5*th72(al,be,mp.mpc(x0,y0))*mp.conj(vtheta(al,be,mp.mpc(x0,y0)))
out['N2']=mp.nstr(abs(dbar-pred)/abs(pred),4); print('N2',out['N2'],flush=True)
# N3
c=lambda tau: tau/mp.sqrt(35)
def vec(F,tau): return mp.matrix([F(a,b,tau) for a,b in pairs])
rows={}
for tau in taus:
    st=-1/tau
    rows[str(tau)]=dict(E=(vec(ThE,st),vec(ThE,tau)),W=(vec(W,st),vec(W,tau)))
    print('vec',tau,flush=True)
mx=lambda v: max(abs(x) for x in v)
res={}
for nm,chi in (('1',1),('-1',-1),('i',1j),('-i',-1j)):
    num=0; den=0; dat=[]
    for tau in taus:
        Es,Et=rows[str(tau)]['E']; Ws,Wt=rows[str(tau)]['W']
        a=Es-chi*c(tau)*(M*Et); b=Ws-chi*c(tau)*(M*Wt); dat.append((a,b,Et,Wt))
        num+=sum(mp.conj(b[i])*a[i] for i in range(105)); den+=sum(abs(b[i])**2 for i in range(105))
    kfit=-num/den
    def r(k): return max(mx(a+k*b)/max(mx(Et+k*Wt),1) for a,b,Et,Wt in dat)
    res[nm]=dict(r_half=mp.nstr(r(mp.mpf(1)/2),4),kappa_fit=mp.nstr(kfit,6),r_fit=mp.nstr(r(kfit),4),r_ThE_only=mp.nstr(r(0),4),
                 r_W_only=mp.nstr(max(mx(b)/max(mx(Wt),1) for a,b,Et,Wt in dat),4))
    print(nm,res[nm],flush=True)
out['N3']=res
# control G_O chi=1 (dps reduced)
mp.mp.dps=20; rc=0
for tau in taus[:2]:
    vs=vec(GO,-1/tau); vt=vec(GO,tau); rc=max(rc,mx(vs-c(tau)*(M*vt))/mx(vs))
out['control_GO_chi1']=mp.nstr(rc,4); print('control',out['control_GO_chi1'])
json.dump(out,open('../data/s.json','w'),indent=1)
