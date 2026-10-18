# Exact tensor factorisation of S and T in adapted CRT coordinates (x5,x7,eps,delta).
# Basis: u'_{x,eps,delta} := u_{x g + eps a2, -delta a2}, a2 = (1/2,0), g = (14,6)/70  (a = a2 + a_odd, a_odd=(1/5,-1/5) in L').
import sys; sys.path.insert(0,'.')
import numpy as np, itertools, json
from fractions import Fraction as F
from exact import Sexact, Texact, red, N, D
g=np.array([14,6]); a2=np.array([35,0])
lab=[(x,e,d) for x in range(35) for e in (0,1) for d in (0,1)]
# u'_k = e(ph_k) u_{j_k}
J={}; 
for k,(x,e,d) in enumerate(lab):
    j,ph=red((x*g+e*a2)%D, -d*a2); J[k]=(j,ph)
assert len({j for j,_ in J.values()})==N
inv={j:(k,ph) for k,(j,ph) in J.items()}
Sx=Sexact(); Tx=Texact()
# S on u (vector law u(-1/w) = S u(w)): u'_k(-1/w) = e(ph_k) sum_j S[jk,j] u_j = e(ph_k) sum_j S[jk,j] e(-ph'_j) u'_{k(j)}
Sp={}
for (i,j),r in Sx.items():
    for k,(jk,phk) in J.items():
        pass
rowsof={}
for (i,j),r in Sx.items(): rowsof.setdefault(i,[]).append((j,r))
for k,(jk,phk) in J.items():
    for j,r in rowsof[jk]:
        l,phl=inv[j]; Sp[(k,l)]=(phk+r-phl)%1
Tp={}
for k,(jk,phk) in J.items():
    j,r=Tx[jk]; l,phl=inv[j]; Tp[k]=(l,(phk+r-phl)%1)
out=[]
# T: does pi act only on (eps,delta) with exponent t5(x5)+t7(x7)+t2(e,d)?
okperm=all(lab[l][0]==lab[k][0] for k,(l,_) in Tp.items())
out.append(f"T permutes only the 2-adic labels: {okperm}; T-perm on (eps,delta): { {lab[k][1:]:lab[l][1:] for k,(l,_) in Tp.items() if lab[k][0]==0} }")
def x_of(x5,x7): return [x for x in range(35) if x%5==x5 and x%7==x7][0]
idx={l:k for k,l in enumerate(lab)}
# T exponent split
t=lambda x,e,d: Tp[idx[(x,e,d)]][1]
t5={x5:(t(x_of(x5,0),0,0)-t(0,0,0))%1 for x5 in range(5)}; t7={x7:(t(x_of(0,x7),0,0)-t(0,0,0))%1 for x7 in range(7)}
t2={(e,d):t(0,e,d) for e in (0,1) for d in (0,1)}
okT=all((t(x,e,d)-t5[x%5]-t7[x%7]-t2[(e,d)])%1==0 for (x,e,d) in lab)
out.append(f"T exponent = t5(x5)+t7(x7)+t2(e,d) exactly: {okT}; t5={ {k:str(v) for k,v in t5.items()} }, t7={ {k:str(v) for k,v in t7.items()} }, t2={ {k:str(v) for k,v in t2.items()} }")
# S: 2-adic pattern and exponent split
s=lambda k,l: Sp.get((idx[k],idx[l]))
pat={}
for e,d in itertools.product((0,1),repeat=2):
    tg={lab[l][1:] for (k,l) in Sp if lab[k]==(0,e,d)}; pat[(e,d)]=tg
out.append(f"S 2-adic support: {pat}")
okS=True; s5={}; s7={}; s2={}
for (e,d),tg in pat.items():
    (e2,d2),=tg
    base=s((0,e,d),(0,e2,d2)); s2[((e,d),(e2,d2))]=base
    for x5 in range(5):
        for y5 in range(5): s5[(x5,y5)]=(s((x_of(x5,0),e,d),(x_of(y5,0),e2,d2))-base)%1
    for x7 in range(7):
        for y7 in range(7): s7[(x7,y7)]=(s((x_of(0,x7),e,d),(x_of(0,y7),e2,d2))-base)%1
    for x in range(35):
        for y in range(35):
            v=s((x,e,d),(y,e2,d2))
            if v is None or (v-s5[(x%5,y%5)]-s7[(x%7,y%7)]-base)%1!=0: okS=False
out.append(f"S exponent = s5(x5,y5)+s7(x7,y7)+s2(2-adic) exactly (same s5,s7 for all 2-adic blocks): {okS}")
out.append(f"s5(x,y) = {sorted({str(v) for v in s5.values()})} ; check s5 = -2*2*x*y/5? {all((s5[(x,y)]-F(-4*x*y,5))%1==0 for x in range(5) for y in range(5))}; s5 = c5*x*y/5 with c5 in { [c for c in range(5) if all((s5[(x,y)]-F(c*x*y,5))%1==0 for x in range(5) for y in range(5))] }")
out.append(f"s7 = c7*x*y/7 with c7 in { [c for c in range(7) if all((s7[(x,y)]-F(c*x*y,7))%1==0 for x in range(7) for y in range(7))] }")
out.append(f"t5 = k5*x^2/5 with k5 in { [c for c in range(5) if all((t5[x]-F(c*x*x,5))%1==0 for x in range(5))] }; t7 = k7*x^2/7 with k7 in { [c for c in range(7) if all((t7[x]-F(c*x*x,7))%1==0 for x in range(7))] }")
out.append(f"s2 (2-adic S, x 1/sqrt35 overall): { {str(k):str(v) for k,v in s2.items()} }")
print("\n".join(out)); open("factor.txt","w").write("\n".join(out)+"\n")
json.dump(dict(t2={str(k):str(v) for k,v in t2.items()},s2={str(k):str(v) for k,v in s2.items()},Tperm={str(lab[k][1:]):str(lab[l][1:]) for k,(l,_) in Tp.items() if lab[k][0]==0}),open("local2.json","w"))
