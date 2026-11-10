import numpy as np, itertools
M=3
circ=lambda h: np.array([[h[(i-j)%M] for j in range(M)] for i in range(M)],float)
def WN(h1,h2,r=1):
    t=[(h1[a]*h2[b]) for a in range(M) for b in range(M) if (a+b)%M==r]
    return sum(t), sum(map(abs,t))
for name,(h1,h2) in {"corpus":([1,1,0],[-1,1,3]),"mod3-unit":([1,1,0],[-1,1,1])}.items():
    d=[round(np.linalg.det(circ(h))) for h in (h1,h2)]
    W,N=WN(h1,h2); print(name,"det",d,"det mod3",[x%3 for x in d],"W",W,"N",N,"Omega=N-|W|",N-abs(W),"Omega%539",(N-abs(W))%539)
# item 7: Phi on integers
def phi(x): return x//3 if x%3==0 else 3*x+(-1 if x%3==1 else 1)
for x0 in [1,2,4,5,7,-1,9]:
    x=x0; tr=[x]
    for _ in range(8): x=phi(x); tr.append(x)
    print("Phi orbit",x0,tr)
assert all(abs(phi(x))>abs(x) for x in range(-10**4,10**4) if x%3)
assert all(phi(x)%3 for x in range(-10**4,10**4) if x%3)
print("checked |Phi(x)|>|x| and Phi(x) not≡0 for units, |x|<1e4")
# item 6: commutant dim for unitary T with eigen-multiplicities m: sum m^2
for m in [(8,8),(128**0.5,),(1,)*128,(11,4,1,1,1)]:
    print("mults",m,"dim commutant",sum(int(k)**2 for k in m) if all(float(k).is_integer() for k in m) else "n/a")
# RTL: 9'sd539 truncates
print("9-bit signed 539 ->", ((539+256)%512)-256)
