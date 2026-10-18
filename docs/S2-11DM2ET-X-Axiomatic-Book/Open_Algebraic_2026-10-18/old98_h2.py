# (e') does h=(g+I)/4 map the + set of each extra relation onto its - set (as a set map on class orbits)?
import json, sympy as sp
exec(open('old98_rel.py').read().split("M=flint.fmpz_mat(rows)")[0].replace("Q=float(sys.argv[1])","Q=2.0"))
R=json.load(open('old98_rel_Q40.json'))
g=sp.Matrix([[0,-m],[sp.Rational(1,m),2*m]]); h=(g+sp.eye(2))/4
tv=sp.Matrix([sp.Rational(t[0],D),sp.Rational(t[1],D)])
def hits(x):
    H=set()
    for j in range(p):
        for a in range(28):
            for b in range(28):
                w=h*(sp.Matrix([sp.Rational(x[0],D)+a,sp.Rational(x[1],D)+b])+j*tv)
                if all((wi*D).q==1 for wi in w):
                    z=(int(w[0]*D)%mod[0],int(w[1]*D)%mod[1])
                    H.add(co[cls[z]] if z in cls else 'out')
    return H
out=[]
for e in R['extra']:
    plus={d['class_orbit'] for d in e['support'] if int(d['coef'])>0}; minus={d['class_orbit'] for d in e['support'] if int(d['coef'])<0}
    mp={c:sorted(map(str,hits(corep[c][0]))) for c in plus|minus}
    out.append(dict(plus=sorted(plus),minus=sorted(minus),h_images=mp)); print(out[-1],flush=True)
json.dump(out,open("old98_h2.json","w"),indent=1)
