# (a) Is Z_all (u = -1 on odd part of 2D, +1 on 2-part) a uniform element of <gamma,-1> on Delta?  Test on all of Delta = Z/D x Z/2D.
import sys, json, sympy
from sympy.ntheory.modular import crt
out=[]
for s in range(5,int(sys.argv[1])+1,2):
    D=2*s*(s-2); M=2*D; odd=M
    while odd%2==0: odd//=2
    u=int(crt([odd,M//odd],[odd-1,1])[0])
    G=sympy.Matrix([[-1,-s],[2,2*s-1]])
    # candidates h = ±gamma^k (k mod order on Delta); compare with u*I as maps mod (D,2D) on generators e1=(1,0), e2=(0,1)
    def red(Mx): return [(Mx[0,0]%D,Mx[1,0]%(2*D)),(Mx[0,1]%D,Mx[1,1]%(2*D))]
    target=red(u*sympy.eye(2)); P=sympy.eye(2); found=[]
    for k in range(0,4*s):
        for sg in (1,-1):
            if red(sg*P)==target: found.append((sg,k))
        P=P*G
    out.append(dict(s=s,uniform=found[:2]))
print([ (o['s'],o['uniform']) for o in out][:12]); print("all uniform:",all(o['uniform'] for o in out))
json.dump(out,open("zall.json","w"))
