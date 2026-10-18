# Test "averaging" condition: for each even n in chain (allowed n sorted), e_n <= (o_prev + o_next)/2,
# where o_prev/o_next are the nearest odd allowed n below/above (term 0 if absent/out of range).
# If it held for all even n, summing gives E_d <= O_d (each odd term used with weight <= 1/2+1/2).
import pickle
A=pickle.load(open('a_200_6000.pkl','rb'))
D=40000
def term(d,n): 
    if n<0 or n*n>d or (d-n*n)%7: return 0
    return A[n][(d-n*n)//7]
fails=[]
for d in range(1,D+1):
    if d%7 not in (0,1,2,4): continue
    ns=[n for n in range(0,int(d**.5)+1) if (d-n*n)%7==0]
    odds=[n for n in ns if n%2]
    for n in ns:
        if n%2: continue
        lo=max([o for o in odds if o<n],default=None); hi=min([o for o in odds if o>n],default=None)
        if hi is None: hi=min(o for o in range(n+1,n+15) if o%2 and (o*o-d)%7==0)
        tl=term(d,lo) if lo is not None else 0; th=term(d,hi)
        e=term(d,n)
        if 2*e>tl+th: fails.append((d,n,e,lo,tl,hi,th))
print('fails',len(fails),'last d',fails[-1][0] if fails else None)
import collections
print('fail count by d-range:',collections.Counter(f[0]//5000*5000 for f in fails))
print('sample late fails:',fails[-10:])
# position of fails relative to sqrt(d)
print('late fails n/sqrt(d):',sorted(set(round(f[1]/f[0]**.5,2) for f in fails if f[0]>30000))[:40])
