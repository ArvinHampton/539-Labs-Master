# Local-derived. Task 3 follow-up: (i) Shimura lifts (t=1,3,5) of the f-eigenspace lie in span{f(tau), f(2tau)} (oldspace of f at level 98);
# (ii) Waldspurger zero pattern with the character twist: c(n) vs L(f x chi_{coredisc(n)},1)  [chi_{-n} * chi_28 * (CM chi_-7) = chi_{coredisc(n)}].
import cypari2; pari=cypari2.Pari(); pari.allocatemem(4*10**9); pari.set_real_precision(38)
P=pari
P("E=ellinit([1,-1,0,-2,-1]); af=ellan(E,100); m=mfinit([196,3/2,28],1); Bh=mfbasis(m)")
P("K=matid(mfdim(m)); foreach([3,11,13,23,29,37],p, my(M=mfheckemat(m,p^2)); K=K*matker((M-af[p]*matid(#M))*K))")
P("f1=concat(0,af[1..60]); f2=vector(61,i,if((i-1)%2==0&&i>1,af[(i-1)/2],0));")
res=[]
for t in [1,3,5]:
    for j in range(1,5):
        P(f"lc=mfcoefs(mfshimura(m,mflinear(Bh,K[,{j}]),{t})[2],60)")
        r=P("matrank(matconcat([f1~,f2~,lc~]))")
        z=P("lc==vector(61,i,0)")
        res.append((t,j,int(r),int(z)))
print("[t, basis vec j, rank span{f(tau),f(2tau),S_t(F_j)} (2 => lift in oldspace of f), lift==0]:", res)
P("C=matrix(#K,401,j,i,mfcoefs(mflinear(Bh,K[,j]),400)[i])")
rows=[]; agree=0; tot=0
for n in range(1,121):
    if int(P(f"issquarefree({n})"))!=1: continue
    allzero=int(P(f"C[,{n}+1]==vector(#K,i,0)~"))
    D=int(P(f"coredisc({n})"))
    if D==1:
        Lv=P("lfun(lfuncreate(E),1)"); rn=1
    else:
        rn=int(P(f"ellrootno(ellinit(elltwist(E,{D})))")); Lv=P(f"lfun(lfuncreate(ellinit(elltwist(E,{D}))),1)")
    Lnz = abs(float(Lv))>1e-20
    tot+=1; agree += int((not allzero)==Lnz)
    rows.append((n, "c=0" if allzero else "c!=0", D, rn, round(float(Lv),6)))
for r in rows: print("  ",r)
print("squarefree n<=120: c(n)!=0 <=> L(f x chi_coredisc(n),1)!=0 holds for", agree, "of", tot)
print("Xi index: n=35, coredisc(35) =", P("coredisc(35)"), "; chi_140 = chi_coredisc(35); Xi central value index")
