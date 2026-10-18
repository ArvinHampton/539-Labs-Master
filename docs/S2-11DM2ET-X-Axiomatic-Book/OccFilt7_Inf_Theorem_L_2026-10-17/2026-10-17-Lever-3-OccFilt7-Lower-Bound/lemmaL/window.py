import pickle,math
A=pickle.load(open('a_200_6000.pkl','rb'))
def a(n,m): return A[n][m] if m>=0 else 0
def partner(n):
    c=[n2 for n2 in range(max(1,n-7),n+8) if n2%2==1 and (n+n2)%14==7]
    return min(c,key=lambda x:(abs(x-n),-x))
for d in [x for x in range(9996,10004)]+[x for x in range(39990,40001)]:
    if d%7 not in (0,1,2,4): continue
    terms=[]; 
    for n in range(0,int(d**.5)+1):
        if (d-n*n)%7==0: terms.append((n,a(n,(d-n*n)//7)))
    tot=sum(t for _,t in terms); peak=max(terms,key=lambda t:t[1])
    ok=[];bad=[]
    for n,t in terms:
        if n%2: continue
        n2=partner(n); t2=a(n2,(d-n2*n2)//7) if n2*n2<=d else 0
        (ok if t<=t2 else bad).append(n)
    badmass=sum(t for n,t in terms if n in bad)
    print(d,'sqrt',round(d**.5,1),'peak n',peak[0],'0.438sqrt',round(.438*d**.5,1),'bad even n',bad,'bad mass/total %.2e'%(badmass/tot))
