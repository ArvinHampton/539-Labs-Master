# Sanity checks of the in-progress H_s-Closure closed forms (H_closed2.txt) against
# exact facts: H_5 == 0, s=8 sqrt(pi)-rationality, agreement with H_s-Closed-Forms H_{-1/2}.
import sympy as sp
s=sp.symbols('s',positive=True)
def g(sv): return sp.gcd(24, sv-8)
def H(k,sv):
    D=(sv-2)*(7*sv-32); r=sp.sqrt(D); G=g(sv); pre=sp.sqrt(2*sp.pi*sv)
    if k==-1: return pre*(-sp.Rational(1,2)/(sv-2)+r/(2*(sv-2)*(7*sv-32)))
    if k==1: return pre*(-(sv-4)*(3*sv-2)/sp.Integer(48*(sv-2)**2)+(2*G**2*sv-4*G**2+sv**3-44*sv**2+192*sv)/sp.Integer(48*(sv-2)**2*(7*sv-32)**2)*r)
    if k==3: return pre*(-(15*sv**4-76*sv**3+108*sv**2+96*sv-128)/sp.Integer(3840*(sv-2)**3)+(-8*G**4*sv**2+32*G**4*sv-32*G**4+20*G**2*sv**4-360*G**2*sv**3+1920*G**2*sv**2-2560*G**2*sv+3*sv**6-152*sv**5+3872*sv**4-28160*sv**3+61440*sv**2)/sp.Integer(3840*(sv-2)**3*(7*sv-32)**3)*r)
for k in (-1,1,3):
    print(f"H_{k}/2: s=5 ->",sp.nsimplify(sp.simplify(H(k,5))),"; s=8 ->",sp.simplify(H(k,8)))
# compare with H_s-Closed-Forms: H_{-1/2}=1/2 sqrt(2 pi s)[1/sqrt(D)-1/(s-2)]
for sv in range(5,30):
    D=(sv-2)*(7*sv-32); ref=sp.sqrt(2*sp.pi*sv)/2*(1/sp.sqrt(D)-sp.Rational(1,sv-2))
    assert sp.simplify(H(-1,sv)-ref)==0
print("H_{-1/2} closure form == H_s-Closed-Forms form for s=5..29: PASS")
