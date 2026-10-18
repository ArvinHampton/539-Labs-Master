import sys; sys.argv=["x",S,"400"]
exec(open('bailey.py').read().split("for n,a in enumerate(alpha)")[0])
def deg(a):
    nz=[i for i,x in enumerate(a) if x]; return (max(nz) if nz else -1, len(nz))
cands={
 '1+q^{sn}':lambda n: [1]+[0]*(s*n-1)+[1]+[0]*(N-s*n-1) if n else one,
 '(-q^s;q^s)_n':lambda n: qp(n,s,+1),
 '(-q^s;q^s)_2n':lambda n: qp(2*n,s,+1),
 '(-q^s;q^s)_n^2':lambda n: mul(qp(n,s,+1),qp(n,s,+1)),
 '(q^s;q^s)_n(-q^s;q^s)_n':lambda n: mul(qp(n,s,-1),qp(n,s,+1)),
}
for name,D in cands.items():
    print(name,[deg(mul(alpha[n],D(n))) for n in range(1,6)])
