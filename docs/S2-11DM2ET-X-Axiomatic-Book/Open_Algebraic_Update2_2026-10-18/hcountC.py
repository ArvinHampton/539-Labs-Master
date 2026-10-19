# Items 3+4: lattice-level computation (no theta counts).  s=2m^2, A=[[2,s],[s,s]] (Qi = x^T A x), L'=A^{-1}Z^2.
# t0 = generator of the order-m isotropic subgroup of the (cyclic, Z/m^2) m-part of L'/Z^2; M_t = Z^2 + Z t0.
# (3) check g M_t = M_t (g=(gamma+I)/(2m)).  (4) if 2m+2=r^2: h=(g+I)/r, M = ∩_{k<4} h^k M_t, enumerate M#/M,
#   F = Fun(M_t#/M_t)^{<gamma,-1>}; rank_X = rank of F -> Fun(<X,-1>-orbits on M#/M) (orbit sums), X in {g,h}.
import sys, json, math, sympy as sp, flint
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form
def lat(cols):
    den=sp.ilcm(*[sp.Rational(c).q for v in cols for c in v])
    Mi=sp.Matrix.hstack(*[sp.Matrix(v)*den for v in cols]); Mi=sp.Matrix(Mi.shape[0],Mi.shape[1],[int(x) for x in Mi])
    H=hermite_normal_form(Mi); H=H[:,[j for j in range(H.shape[1]) if any(H[:,j])]]
    return H/den
def inlat(B,v): return all(sp.Rational(x).q==1 for x in B.inv()*v)
def dualA(B,A): return A.inv()*(B.T).inv()
def run(m,do_h=True):
    s=2*m*m; A=sp.Matrix([[2,s],[s,s]]); n=abs(A.det())
    G=sp.Matrix([[-1,-s],[2,2*s-1]]); g=(G+sp.eye(2))/(2*m)
    mp=m*m; other=n//mp
    assert math.gcd(mp,other)==1 or True
    # m-part generator: find x in L' with order m^2 mod Z^2 after multiplying by 'other part'
    Ai=A.inv(); cand=[Ai*sp.Matrix([1,0]),Ai*sp.Matrix([0,1]),Ai*sp.Matrix([1,1])]
    # remove non-m part: multiply by e with e≡0 mod (n/m^2-part)... use CRT idempotent on exponent
    expo=sp.ilcm(*[sp.Rational(c).q for v in cand for c in v])
    mm=1
    for p_ in sp.factorint(m): mm*=p_**sp.multiplicity(p_,expo)
    oth=expo//mm; e=(pow(oth,-1,mm)*oth)%expo
    gen=None
    for v in cand:
        w=(e*v).applyfunc(lambda z: z-sp.floor(z))
        o=sp.ilcm(*[sp.Rational(c).q for c in w])
        if o==mm: gen=w; break
    assert gen is not None and mm==m*m, (mm,m)
    t0=m*gen; Qt=(t0.T*A*t0)[0]/2
    Mt=lat([sp.Matrix([1,0]),sp.Matrix([0,1]),t0])
    res=dict(m=m,s=s,isotropic=bool(sp.Rational(Qt).q==1),gMt_eq_Mt=bool(all(inlat(Mt,g*Mt[:,j]) and inlat(Mt,g.inv()*Mt[:,j]) for j in range(2))))
    r=math.isqrt(2*m+2)
    if not do_h: return res
    X={'g':g}
    if r*r==2*m+2:
        h=(g+sp.eye(2))/r; X['h']=h; res['h_isometry']=bool(h.T*A*h==A); res['h_sq_g']=bool(h*h==g)
        M=lat([ (h**k*Mt)[:,j] for k in range(4) for j in range(2)])  # sum, not intersection -> use dual trick
        # intersection via duals
        D_=lat([ (( (h**k*Mt).T).inv())[:,j] for k in range(4) for j in range(2)])
        M=lat([ ((D_.T).inv())[:,j] for j in range(2)])
    else:
        M=Mt
    res['hM_eq_M']=bool(all(inlat(M,X[k]*M[:,j]) and inlat(M,X[k].inv()*M[:,j]) for k in X for j in range(2)))
    GM=M.T*A*M; L=abs(GM.det()); res['M_basis']=str(M.tolist()); res['M_gram']=str(GM.tolist()); res['|M#/M|']=int(L)
    # integer model: element y in M# written as M*(c/L), c in Z^2 mod L ; M# coords = GM^{-1} Z^2 -> c = L*GM^{-1}*z
    Ginv=(GM.inv()*L).applyfunc(int)
    els=set()
    for a in range(int(L)):
        # generate subgroup by columns of Ginv (BFS cheap: all a*col1 + b*col2 mod L, with a,b < L) -- use SNF orders
        pass
    S=smith_normal_form(sp.Matrix(GM.applyfunc(int)))
    d1,d2=abs(int(S[0,0])),abs(int(S[1,1]))
    c1=[int(x) for x in Ginv[:,0]]; c2=[int(x) for x in Ginv[:,1]]
    for a in range(int(L)):
        x=((a*c1[0])%L,(a*c1[1])%L)
        if a>0 and x==(0,0): break
        for b in range(int(L)):
            y=((x[0]+b*c2[0])%L,(x[1]+b*c2[1])%L)
            if b>0 and y==x: break
            els.add(y)
    res['enumerated']=len(els)
    def matM(Y): return (M.inv()*Y*M).applyfunc(int)
    acts={k:matM(v) for k,v in X.items()}; acts['gamma']=matM(G); acts['neg']=-sp.eye(2)
    ap=lambda T,y:((int(T[0,0])*y[0]+int(T[0,1])*y[1])%L,(int(T[1,0])*y[0]+int(T[1,1])*y[1])%L)
    # membership in Mt# : B(y, b)=y^T A b in Z for b in Mt basis ; y = M c/L
    Pm=(M.T*A*Mt)  # rows: c^T * Pm / L must be integer
    inMts=lambda y: all(((y[0]*Pm[0,j]+y[1]*Pm[1,j])/L).q==1 for j in range(2)) if False else all(sp.Rational(y[0]*Pm[0,j]+y[1]*Pm[1,j],L).q==1 for j in range(2))
    W=Mt.inv()*M  # Mt-coords of y = W c / L
    def key(y): return tuple(sp.Rational(W[i,0]*y[0]+W[i,1]*y[1],L)%1 for i in range(2))
    old=[y for y in els if inMts(y)]
    cls={}
    for y in old: cls.setdefault(key(y),[]).append(y)
    ckeys=list(cls); res['n_old_classes']=len(ckeys)
    elkey={y:key(y) for y in old}
    # <gamma,-1> orbits on classes
    def orbits(items,fs):
        lab={}; k=0
        for it in items:
            if it in lab: continue
            st=[it]; lab[it]=k
            while st:
                a=st.pop()
                for f in fs:
                    b=f(a)
                    if b not in lab: lab[b]=k; st.append(b)
            k+=1
        return lab,k
    clsmap=lambda T: (lambda kk: elkey[ap(T,cls[kk][0])])
    Flab,nF=orbits(ckeys,[clsmap(acts['gamma']),clsmap(acts['neg'])]); res['dim_F']=nF
    for nm in X:
        lab,nb=orbits(list(els),[lambda y,T=acts[nm]:ap(T,y),lambda y:ap(acts['neg'],y),lambda y:ap(acts['gamma'],y)])
        rows=[[0]*nb for _ in range(nF)]
        for y in old: rows[Flab[elkey[y]]][lab[y]]+=1
        res[f'rank_{nm}']=flint.fmpz_mat(rows).rank()
        if nm=='g': res['classorbits_g']=orbits(ckeys,[clsmap(acts['g']),clsmap(acts['neg'])])[1]
    if 'h' in X:
        labg,ng=orbits(list(els),[lambda y:ap(acts['g'],y),lambda y:ap(acts['neg'],y),lambda y:ap(acts['gamma'],y)])
        oldorb=set(labg[y] for y in old)
        # h acts on g-orbits as involution (h^2=g)
        rep={}
        for y in els: rep.setdefault(labg[y],y)
        moved=[o for o in oldorb if labg[ap(acts['h'],rep[o])]!=o]
        to_new=[o for o in moved if labg[ap(acts['h'],rep[o])] not in oldorb]
        res['g_orbits_meeting_old']=len(oldorb); res['h_moved_old_g_orbits']=len(moved); res['h_moves_old_to_nonold']=len(to_new)
        sizes={}
        for y in els: sizes[labg[y]]=sizes.get(labg[y],0)+1
        res['moved_orbit_sizes']=None
        oldset=set(old)
        cnt_old={}
        for y in els:
            if y in oldset: cnt_old[labg[y]]=cnt_old.get(labg[y],0)+1
        fully_old=set(o for o in oldorb if cnt_old.get(o,0)==sizes[o])
        himg={o:labg[ap(acts['h'],rep[o])] for o in oldorb}
        closed=[o for o in fully_old if himg[o] in fully_old]
        fixedc=[o for o in closed if himg[o]==o]
        # columns v(O) in Fun(<gamma,-1>-orbits of old classes)
        def vec(o):
            v=[0]*nF
            return v
        V={o:[0]*nF for o in oldorb}
        for y in old: V[labg[y]][Flab[elkey[y]]]+=1
        rk=lambda cols: flint.fmpz_mat([list(c) for c in cols]).rank() if cols else 0
        diffs_closed=[[a-b for a,b in zip(V[o],V[himg[o]])] for o in closed if himg[o]!=o]
        diffs_oo=[[a-b for a,b in zip(V[o],V[himg[o]])] for o in oldorb if himg[o] in oldorb and himg[o]!=o]
        res.update(n_fully_old=len(fully_old),n_closed=len(closed),closed_hfixed=len(fixedc),closed_nonfixed=len(closed)-len(fixedc),
                   rank_V=rk(list(V.values())),span_diff_closed=rk(diffs_closed),span_diff_oldold=rk(diffs_oo))
    if 'rank_h' in res: res['predicted_extra_relations']=res['rank_g']-res['rank_h']
    return res
if __name__=="__main__":
    do_h=sys.argv[2]!='noh' if len(sys.argv)>2 else True
    out=[]
    for m in map(int,sys.argv[1].split(',')):
        r=run(m,do_h); print(json.dumps(r,default=str),flush=True); out.append(r)
    json.dump(out,open(f"hcountC_{sys.argv[1].replace(',','_')}.json","w"),indent=1,default=str)
