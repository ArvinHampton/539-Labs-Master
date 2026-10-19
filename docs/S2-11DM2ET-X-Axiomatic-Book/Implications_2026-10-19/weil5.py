import numpy as np, json, itertools
p=5;a=2
e=lambda r: np.exp(2j*np.pi*r)
T=np.diag([e(a*x*x/p) for x in range(p)])
S=np.array([[e(-2*a*i*j/p) for j in range(p)] for i in range(p)])/np.sqrt(p)
Be=np.array([[1,0,0],[0,1,0],[0,0,1],[0,0,1],[0,1,0]],float)
Bo=np.array([[0,0],[1,0],[0,1],[0,-1],[-1,0]],float)
def res(M,B): return np.linalg.inv(B.T@B)@B.T@M@B
def group(gens):
    I=np.eye(gens[0].shape[0],dtype=complex); els=[I]; keys={tuple(np.round(I,7).flatten())}; fr=[I]
    while fr:
        nf=[]
        for X in fr:
            for M in gens:
                Y=M@X; k=tuple(np.round(Y,7).flatten())
                if k not in keys: keys.add(k); els.append(Y); nf.append(Y)
        fr=nf
    return els
out={}
for name,B in (('even',Be),('odd',Bo)):
    G=group([res(S,B),res(T,B)])
    d=B.shape[1]
    scal=[X for X in G if np.allclose(X, X[0,0]*np.eye(d),atol=1e-7)]
    out[name]={'dim':d,'|G|':len(G),'|scalars in G|':len(scal),'|G/scalars|':len(G)//len(scal),
               'element orders mod scalars':sorted(set(next(n for n in range(1,61) if np.allclose(np.linalg.matrix_power(X,n), np.linalg.matrix_power(X,n)[0,0]*np.eye(d),atol=1e-6)) for X in G))}
print(json.dumps(out,indent=1)); json.dump(out,open('weil5.json','w'),indent=1)
