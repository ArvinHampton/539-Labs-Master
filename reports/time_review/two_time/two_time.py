# Cat B exploration: checked algebra/numerics for the two-time postulate (t+, t-).
import sympy as sp, numpy as np, json
out={}
Tp,Tm=sp.Rational(5399,10),sp.Integer(540)
# 1) Beat / torus: drivers at 539.9 (+U) and 540 (E_cosmos -U base, delta=0)
beat=sp.nsimplify(1/(1/Tp-1/Tm)); out['beat_period_s']=float(beat); out['beat_days']=float(beat/86400)
r=sp.nsimplify(Tp/Tm); out['ratio']=str(r)  # 5399/5400 -> closed torus orbit
out['torus_closure_s']=float(sp.ilcm(5399,5400)/10)
# 2) Reversal-lock: t- = -t+ + phi  => sin(2pi t-/T) = -sin(2pi t+/T - 2pi phi/T): one time, phase only
t,phi,T=sp.symbols('t phi T',real=True)
out['lock_identity_zero']=sp.simplify(sp.sin(2*sp.pi*(-t+phi)/T)+sp.sin(2*sp.pi*t/T-2*sp.pi*phi/T))==0
# 3) N-SFA-style coupled oscillators: +U normal sign, -U negative norm, brane coupling g a b
w1,w2,g,W=sp.symbols('omega1 omega2 g Omega',positive=True)
a,b=sp.symbols('a b',cls=sp.Function)
L=sp.Rational(1,2)*(a(t).diff(t)**2-w1**2*a(t)**2)-sp.Rational(1,2)*(b(t).diff(t)**2-w2**2*b(t)**2)-g*a(t)*b(t)
eqs=[sp.euler_equations(L,[a(t),b(t)],t)[i].lhs for i in range(2)]
M=sp.Matrix([[w1**2-W**2,g],[-g,w2**2-W**2]])  # from a''=-w1^2 a - g b ; b''=-w2^2 b + g a
char=sp.expand(M.det()); out['charpoly']=str(char)
sol=sp.solve(char,W**2); out['Omega2']=[str(s) for s in sol]
gcrit=(w1**2-w2**2)/2; out['g_crit']=str(sp.Abs(gcrit))
w1n,w2n=2*np.pi/539.9,2*np.pi/540
out['g_crit_numeric_s^-2']=abs(w1n**2-w2n**2)/2
out['g_crit_over_omega2']=out['g_crit_numeric_s^-2']/w1n**2
# conserved energy: E = E+ - E- + g a b (sign structure); verify dE/dt=0 on shell
E=sp.Rational(1,2)*(a(t).diff(t)**2+w1**2*a(t)**2)-sp.Rational(1,2)*(b(t).diff(t)**2+w2**2*b(t)**2)+g*a(t)*b(t)
ode={a(t).diff(t,2):-w1**2*a(t)-g*b(t), b(t).diff(t,2):-w2**2*b(t)+g*a(t)}
out['dE_dt_on_shell']=str(sp.simplify(E.diff(t).subs(ode)))
# numerics: g below / above critical
def run(gv,tmax=2e6,dt=1.0):
    y=np.array([1.0,0,0.5,0])
    def f(y): A,Ad,B,Bd=y; return np.array([Ad,-w1n**2*A-gv*B,Bd,-w2n**2*B+gv*A])
    mx=0;Es=[]
    for i in range(int(tmax/dt)):
        k1=f(y);k2=f(y+dt/2*k1);k3=f(y+dt/2*k2);k4=f(y+dt*k3);y=y+dt/6*(k1+2*k2+2*k3+k4)
        mx=max(mx,abs(y[0]))
        if i%100000==0: Es.append(0.5*(y[1]**2+w1n**2*y[0]**2)-0.5*(y[3]**2+w2n**2*y[2]**2)+gv*y[0]*y[2])
    return mx,max(Es)-min(Es)
gc=out['g_crit_numeric_s^-2']
for lab,gv in [('0.5gc',0.5*gc),('2gc',2*gc)]:
    mx,dE=run(gv); out[f'max|a|_{lab}']=mx; out[f'Edrift_{lab}']=dE
json.dump(out,open('two_time_output.json','w'),indent=1,default=str); print(json.dumps(out,indent=1,default=str))
