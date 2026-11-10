# Local-derived (t4436, alpha-3 structure). Lemma: in Q[A] (A abelian) with b^2 = 1, t = g*(1/2)(1+a) + g*(1/2)(1-a)b satisfies t t* = 1 for
# every a, g in A (cross terms cancel: (1+a)(1-a^-1) + (1-a)(1+a^-1) = 0). Check: each of the 6 supports of s4c is g*{1, a, b, ab} with b = 111,
# and every one of the 48 solutions is +-g*[(1/2)(1+a) + (1/2)(1-a)b] for some labelling (g, a) of the support.
import itertools
from fractions import Fraction as F
inv=lambda x: pow(x,-1,140)
print("111^2 mod 140 =",111*111%140,"; 111 mod 4,5,7 =",111%4,111%5,111%7)
sups=[(3,37,47,53),(3,41,53,71),(3,53,79,89),(37,41,47,71),(37,47,79,89),(41,71,79,89)]
def tt(t):
    pr={}
    for p,x in t.items():
        for q,y in t.items():
            g=(p*inv(q))%140; pr[g]=pr.get(g,0)+x*y
    return {g:v for g,v in pr.items() if v}
total=set()
for S in sups:
    forms=set()
    for g in S:
        for a in range(1,140):
            if any(a%r==0 for r in (2,5,7)): continue
            Sg={g, g*a%140, g*111%140, g*a*111%140}
            if Sg!=set(S) or len(Sg)<4: continue
            for sgn in (1,-1):
                t={g:F(sgn,2)}; t[g*a%140]=t.get(g*a%140,0)+F(sgn,2); t[g*111%140]=t.get(g*111%140,0)+F(sgn,2); t[g*a*111%140]=t.get(g*a*111%140,0)-F(sgn,2)
                assert tt(t)=={1:1}
                forms.add(tuple(sorted(t.items())))
    print(S,": g^-1 S = {1,a,111,111a} realisable:",len(forms)>0,"; distinct solutions of lemma form:",len(forms))
    total|=forms
print("total distinct lemma-form solutions over the 6 supports:",len(total),"(s4c found 48)")
