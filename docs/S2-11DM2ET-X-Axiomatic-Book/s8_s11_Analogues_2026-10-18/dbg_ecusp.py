import sys; sys.argv=['x','11','2:1,3:2','300','9.5']
src=open('ecusp_s.py').read()
src=src[:src.index("Hl=list(H)")]
exec(src)
from collections import Counter
for tag,pts,Fd,NCd in (('L',ptsL,FL,NCL),('R',ptsR,FR,NCR)):
    cntp=Counter()
    for (x1,x2),v in pts:
        J=pari.idealhnf(K,(2*int(x1)+s*int(x2))+c*int(x2)*w); Cp=[]
        for P in Pbad: Cp.append(int(pari.idealval(K,J,P)))
        cntp[tuple(Cp)]+=1
    for Cp in sorted(Fd,key=lambda k:NCd[k])[:6]:
        NC=NCd[Cp]; Nb=4*D*D*Qc/NC
        hit=[cidx[k] for k in Fd[Cp]]
        m=(norms<=Nb)&np.isin(cidxs,hit)
        print(tag,Cp,"NC",NC,"points",cntp[Cp],"ideals in hit classes up to bound",int(m.sum()),"Nb",int(Nb),"hit classes",len(hit))
Hl=list(H)
src2=open('ecusp_s.py').read()
exec(src2[src2.index("def nonEis"):src2.index("sq=math.sqrt")].replace('raise SystemExit','print'))
tau=1j*0.8
for tag,pts,G in (('L',ptsL,GL),('R',ptsR,GR)):
    direct=sum(v*np.exp(2j*np.pi*((x1*x1+s*x1*x2+(s/2)*x2*x2)/(D*D))*tau) for (x1,x2),v in pts if (x1*x1+s*x1*x2+(s/2)*x2*x2)/(D*D)<=9.5)
    print(tag,"direct",direct,"synth",Eeval(G,tau,0))
    # per smallest frequencies
    qs=sorted(((x1*x1+s*x1*x2+(s/2)*x2*x2)/(D*D),v) for (x1,x2),v in pts)[:5]; print("  lowest Q:",[(round(q,5),np.round(v,3)) for q,v in qs])
    lam,Gv,Fv=sorted(G,key=lambda t:t[0])[0]; m=norms*lam<=2
    print("  synth lowest:",sorted([(round(lam*n,5),np.round(Fv[ci],3)) for n,ci in zip(norms[m],cidxs[m]) if abs(Fv[ci])>0])[:5])
