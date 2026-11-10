import sys,json
from math import lcm
sys.path.insert(0,'/workspace/quantum-comp/reports/bridges/_git_v8_unpushed_clone/reports/s_family_paths/A35_lawspace_exact')
from symbols import T_rows, L
R={}
rows=T_rows(); perm=[list(r)[0] for r in rows]; ph=[list(r.values())[0][0] for r in rows]
# order of monomial matrix: for each cycle, length c and product of phases e(sum/L); order = lcm(c * ord(phase sum))
seen=set(); o=1
for s in range(105):
    if s in seen: continue
    c=0; tot=0; j=s
    while j not in seen: seen.add(j); tot+=ph[j]; j=perm[j]; c+=1
    from math import gcd
    o=lcm(o, c*(L//gcd(tot%L,L)))
R['C7']={'L':L,'ord_MT':o,'pass':o%49==0 and o%11!=0}
def T3(n): return n//3 if n%3==0 else ((4*n+2)//3 if n%3==1 else (2*n+1)//3)
st={}
for n in range(1,540):
    x=n;k=0
    while x!=1 and k<10**5: x=T3(x);k+=1
    st[n]=k if x==1 else None
ok=all(v is not None for v in st.values()); m=max(v for v in st.values() if v is not None)
R['C8']={'all_reach_1':ok,'max_steps':m,'argmax':[n for n in st if st[n]==m],'pass':ok and m==18}
c=sum(1 for v in st.values() if v is not None and v<=14)
R['C9']={'count_le14':c,'pass':c==521}
json.dump(R,open('data/b2.json','w'),indent=1); print(json.dumps(R))
