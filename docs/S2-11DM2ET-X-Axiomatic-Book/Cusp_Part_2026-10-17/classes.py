# Step 1-2: ray class group mod f*oo1*oo2 (f=p2 p5), characters, infinity types, Galois action,
# and the ray classes of the ideals attached to the lattice vectors of u_L in each sign region.
import cypari2, numpy as np, json
from uvec import cone_pts
from family import G
pari=cypari2.Pari(); pari.allocatemem(10**9); gp=lambda s: pari(s)
gp('bnf=bnfinit(y^2-35,1); P2=idealprimedec(bnf,2)[1]; P5=idealprimedec(bnf,5)[1]; f=idealmul(bnf,P2,P5); bnr=bnrinit(bnf,[f,[1,1]],1)')
gp('cl(I)=bnrisprincipal(bnr,I,0)')
gp('dd=idealmul(bnf,idealpow(bnf,P2,2),P5)')            # d' = p2^2 p5
out=[]
cpm=[int(v) for v in gp('cl(idealhnf(bnf,1+10*y))')]      # alpha=1+10sqrt35: signs (+,-)
cmp=[int(v) for v in gp('cl(idealhnf(bnf,1-10*y))')]      # signs (-,+)
cmm=[int(v) for v in gp('cl(idealhnf(bnf,-1+20*y-0))')] if False else None
out.append(f"sign classes: c(+,-) = {cpm}, c(-,+) = {cmp}   [classes of (alpha), alpha = 1 +/- 10 sqrt35 = 1 mod^x f]")
def classof(nu70):
    X,Y=int(nu70[0])//7,int(nu70[1])//7          # (X,Y)=10 nu ; nu70 = 70 nu
    b=f"{2*X+7*Y}+{Y}*y"
    I=gp(f'idealdiv(bnf,idealhnf(bnf,{b}),dd)')
    return [int(v) for v in gp('cl')(I)], int(gp('idealnorm')(gp('bnf'),I))
regions={'S+':((1,0),tuple(G@np.array([1,0])),1),'S-':((1,0),tuple(G@np.array([1,0])),-1),
         'T+':((1,-1),tuple(G@np.array([1,-1])),1),'T-':((1,-1),tuple(G@np.array([1,-1])),-1)}
from uvec import D
res={}
for name,(r1,r2,sg) in regions.items():
    # enumerate nu in (a+Z^2) cap sg*cone directly (reuse cone_pts internals)
    m=np.arange(-40,41); M1,M2=np.meshgrid(m,m,indexing='ij')
    N1=(49)+D*M1.ravel(); N2=(-14)+D*M2.ravel()
    s=sg*(N1*r2[1]-N2*r2[0])*np.sign(r1[0]*r2[1]-r1[1]*r2[0]); t=sg*(r1[0]*N2-r1[1]*N1)*np.sign(r1[0]*r2[1]-r1[1]*r2[0])
    ok=(s>0)&(t>=0); N1=N1[ok];N2=N2[ok]
    q=(2*N1*N1+14*N1*N2+7*N2*N2)/(2*D*D); o=np.argsort(np.abs(q))
    cls=set(); norms=[]
    for i in o[:60]:
        c,nrm=classof((N1[i],N2[i])); cls.add(tuple(c)); norms.append((round(20*abs(q[i])),nrm))
    assert all(a==b for a,b in norms), norms[:5]
    res[name]=sorted(cls)
    out.append(f"region {name}: first 60 vectors -> ideals with N = 20|Q2| (checked), ray classes {sorted(cls)}")
json.dump({k:[list(c) for c in v] for k,v in res.items()},open("region_classes.json","w"))
# characters chi_{j,l}(c)=e(j c1/8 + l c2/2); infinity type p1=[chi(c(-,+))=-1], p2=[chi(c(+,-))=-1]; sigma: g1->5g1, g2->4g1+g2
def chi(j,l,c): return np.exp(2j*np.pi*(j*c[0]/8+l*c[1]/2))
sg1=[int(v) for v in gp('cl(nfgaloisapply(bnf,-y,bnr.gen[1]))')]; sg2=[int(v) for v in gp('cl(nfgaloisapply(bnf,-y,bnr.gen[2]))')]
out.append(f"sigma(g1)={sg1}, sigma(g2)={sg2}")
tab=[]
for j in range(8):
    for l in range(2):
        p1=int(round(chi(j,l,cmp).real))==-1; p2=int(round(chi(j,l,cpm).real))==-1
        cond=gp(f'bnrconductor(bnr,[{j},{l}])')
        inv=(j%2==0)
        tab.append(dict(j=j,l=l,type=(int(p1),int(p2)),sigma_inv=inv,cond=str(cond)))
        out.append(f"chi_({j},{l}): infinity type {(int(p1),int(p2))}, sigma-invariant={inv}, conductor={cond}")
json.dump(tab,open("characters.json","w"))
print("\n".join(out)); open("classes.txt","w").write("\n".join(out)+"\n")
