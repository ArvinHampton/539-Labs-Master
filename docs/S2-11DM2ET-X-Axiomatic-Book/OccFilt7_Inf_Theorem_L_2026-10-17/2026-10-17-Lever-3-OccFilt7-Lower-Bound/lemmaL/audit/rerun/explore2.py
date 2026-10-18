import mpmath as mp
def Phi1(u):
    return (mp.quad(lambda x:mp.log(1+mp.e**-x),[0,u])-mp.quad(lambda x:mp.log(1-mp.e**-x),[u,2*u]))/(2*u)
def Psi(a):
    f=lambda u: a*Phi1(u)+(1-a*a)*u/(7*a)
    # golden search
    lo,hi=mp.mpf('1e-4'),mp.mpf(20)
    for _ in range(80):
        m1=lo+(hi-lo)*0.382; m2=lo+(hi-lo)*0.618
        if f(m1)<f(m2): hi=m2
        else: lo=m1
    return f(lo),lo
y=mp.findroot(lambda y:y**7+y**2-1,0.84); c=mp.sqrt((mp.polylog(2,y*y)+7*mp.log(y)**2)/7)
print('closed form c=',c)
best=Psi(mp.mpf('0.438'));print('Psi(0.438)',best)
for a in [0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.438,0.5,0.55,0.6,0.7,0.8,0.9,0.97]:
    v,u=Psi(mp.mpf(a)); print(a, mp.nstr(v,6),'u*',mp.nstr(u,4),'deficit per sqrt(d):',mp.nstr(best[0]-v,4))
