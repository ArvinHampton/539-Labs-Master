# Rewrite c_e = sqrt(pi) * [R_e(s) + S_e(s) sqrt(2s)] with R_e, S_e in Q(s) (exact).
import pickle, sympy as sp, json
d=pickle.load(open('axes_closed_K13.pkl','rb')); c=d['c']; w=sp.symbols('w',positive=True); s=sp.symbols('s',positive=True)
out={}
for e in range(-1,14,2):
    v=sp.together(sp.expand(c[e]/sp.sqrt(sp.pi)))
    num,den=sp.fraction(v)
    conj=den.subs(w,-w); num=sp.expand(num*conj); den=sp.expand(den*conj)   # den now even in w
    num=sp.Poly(num,w); even=sum(cf*w**m[0] for m,cf in zip(num.monoms(),num.coeffs()) if m[0]%2==0)
    odd=sum(cf*w**(m[0]-1) for m,cf in zip(num.monoms(),num.coeffs()) if m[0]%2==1)
    sub=lambda z: sp.factor(sp.expand(z).subs(w**2,s/2) if True else z)
    R=sp.factor(sp.expand(even/den).subs(w,sp.sqrt(s/2))); S=sp.factor(sp.expand(odd/den).subs(w,sp.sqrt(s/2))/2)  # w = sqrt(2s)/2
    chk=sp.simplify(R+S*sp.sqrt(2*s)-(c[e]/sp.sqrt(sp.pi)).subs(w,sp.sqrt(s/2)))
    out[e]=dict(R=str(R),S=str(S),check=str(chk)); print(e,'R =',R,'| S =',S,'| check',chk,flush=True)
json.dump(out,open('axes_RS_forms.json','w'),indent=1)
