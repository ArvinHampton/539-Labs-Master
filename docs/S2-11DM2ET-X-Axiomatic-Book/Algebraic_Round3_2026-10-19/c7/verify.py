# Compare exact closed forms with (a) 65-digit engine numerics run6 (axes cases), (b) direct summation at held-out s.
import pickle, json, glob, mpmath as mp, sympy as sp
mp.mp.dps=60
d=pickle.load(open('axes_closed_K13.pkl','rb')); c=d['c']; w=sp.symbols('w',positive=True)
out={'engine':{},'direct':{}}
cases={7:'run6_s7_a7_b2',8:'run6_s8_a4_b1',9:'run6_s9_a9_b2',10:'run6_s10_a5_b1',11:'run6_s11_a11_b2',12:'run6_s12_a6_b1',13:'run6_s13_a13_b2',15:'run6_s15_a15_b2',16:'run6_s16_a8_b1'}
if __name__=="__main__":
  pass
for s,f in (cases.items() if __name__=="__main__" else []):
    try: R=json.load(open(f'../c6/{f}.json'))
    except FileNotFoundError: continue
    wv=mp.sqrt(mp.mpf(s)/2)
    diffs={e:mp.nstr(abs(mp.mpf(R['coeffs'][str(e)]['val'])-sp.N(c[e].subs(w,sp.sqrt(sp.Rational(s,2))),60)),3) for e in range(-2,10)}
    out['engine'][s]=diffs; print('engine',s,diffs,flush=True)
# direct: H^axes(e^{-t}) = P - Caxis - Cthird summed numerically; residual vs expansion through eps^13
def Hdirect(s,t):
    N=int(mp.sqrt(80/t))+5; tot=mp.mpf(0)
    for n in range(0,N):
        for k in range(0,N):
            Qp=n*n+s*n*k+s*k*(k+1)//2
            if t*Qp>200 and k>0: break
            tot+=mp.e**(-t*Qp)
            if n>=1 and k>=1: tot-=mp.e**(-t*(n*n+s*n*k+s*k*(k-1)//2))
    tot-=mp.mpf(3)/2+sum(mp.e**(-t*n*n) for n in range(1,N))+sum(mp.e**(-t*s*k*(k+1)/2) for k in range(1,N))
    return tot
mp.mp.dps=30
for s in ((20,31) if __name__=="__main__" else ()):
    row=[]
    for t in (mp.mpf('0.04'),mp.mpf('0.02'),mp.mpf('0.01')):
        e_=mp.sqrt(t); asym=sum(mp.mpf(sp.N(c[e].subs(w,sp.sqrt(sp.Rational(s,2))),40))*e_**e for e in range(-2,14))
        row.append((mp.nstr(t,3),mp.nstr((Hdirect(s,t)-asym)/t**mp.mpf(7.5),6)))
    out['direct'][s]=row; print('direct',s,row,flush=True)
json.dump(out,open('verify.json','w'),indent=1,default=str)
