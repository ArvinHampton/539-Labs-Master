import hashlib
def T3(n): return n//3 if n%3==0 else ((4*n+2)//3 if n%3==1 else (2*n+1)//3)
def joint(tag,N,steps=539,mod2=8,skip=20):
    J={}
    for d in range(N):
        u=int.from_bytes(hashlib.sha3_512(tag+b'-%d'%d).digest(),'big')
        for i in range(steps):
            u=T3(u)
            if i<skip: continue
            k=(u%3,u%mod2); J[k]=J.get(k,0)+1
    return J
LAW8={1:7,2:8,3:5,5:1,6:8,7:3}  # /32, from MARKOV_FIBRE_FREQ L2
def stats(J,mod2):
    n=sum(J.values()); m2={}
    for (a,c),v in J.items(): m2[c]=m2.get(c,0)+v
    chi_ind=0; maxdev=0; tv=0
    for c in m2:
        for a in range(3):
            e=m2[c]/3; o=J.get((a,c),0); chi_ind+=(o-e)**2/e; maxdev=max(maxdev,abs(o/m2[c]-1/3))
    # fully specified null on mod 8
    chi_full=None
    if mod2==8:
        chi_full=0
        for c,w in LAW8.items():
            for a in range(3):
                e=n*w/96; o=J.get((a,c),0); chi_full+=(o-e)**2/e; tv+=abs(o/n-w/96)/2
    return dict(n=n,m2={c:m2[c]/n for c in sorted(m2)},chi_ind=chi_ind,df_ind=2*(len(m2)-1),maxdev_cond=maxdev,chi_full=chi_full,tv_full=tv,
                bad_mod4=sum(v for (a,c),v in J.items() if c%4==0))
