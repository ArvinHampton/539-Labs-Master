# test termwise pairings even n -> odd n' (n'^2 = n^2 mod 7), report failures a_n(m_n) > a_n'(m_n')
import pickle,sys
A=pickle.load(open('a_200_6000.pkl','rb')); N=len(A)-1; M=len(A[0])-1
D=min(N*N, 7*M)
def a(n,m): return A[n][m] if (0<=m and n<=N) else 0
def partner_reflect(n):
    # odd n' with n+n' = 7 mod 14, |n'-n| minimal (class 0: n'=n+7 if possible)
    c=[n2 for n2 in range(max(1,n-7),n+8) if n2%2==1 and (n+n2)%14==7]
    return min(c,key=lambda x:(abs(x-n),-x))
def test(partner,name):
    fails=[]
    for d in range(1,D+1):
        if d%7 not in (0,1,2,4): continue
        for n in range(0,int(d**.5)+1,2):
            if (d-n*n)%7: continue
            m=(d-n*n)//7; n2=partner(n)
            m2=(d-n2*n2)//7 if n2*n2<=d else -1
            if a(n,m)>a(n2,m2): fails.append((d,n,m,n2,m2,a(n,m),a(n2,m2)))
    print(name,'fails:',len(fails))
    # characterise: failures with m >= threshold
    big=[f for f in fails if f[2]>=3*f[1]]
    print('  failures with m>=3n:',len(big), big[:8])
    print('  max d of failure with m >= n:', max([f[0] for f in fails if f[2]>=f[1]],default=None))
test(partner_reflect,'reflect')
test(lambda n:n+7,'n+7')
test(lambda n:abs(n-7),'n-7')
