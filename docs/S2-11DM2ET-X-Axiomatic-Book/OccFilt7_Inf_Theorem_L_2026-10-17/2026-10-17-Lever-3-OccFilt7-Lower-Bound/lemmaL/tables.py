# exact tables a_n(m) = (-1)^m phi_n(m) for n<=N, m<=M  (pickled numpy object array)
import sys, pickle
N=int(sys.argv[1]); M=int(sys.argv[2])
p=[1]+[0]*M; A=[[ (p[m] if m%2==0 else -p[m]) for m in range(M+1)]]
for n in range(1,N+1):
    for m in range(n,M+1): p[m]-=p[m-n]
    A.append([(p[m] if m%2==0 else -p[m]) for m in range(M+1)])
assert all(v>=0 for row in A for v in row)
pickle.dump(A,open(f'a_{N}_{M}.pkl','wb'))
print('ok')
