# Local-derived. Task 3: weight-3/2 forms in S_{3/2}(Gamma0(196)) (and Kohnen plus space) whose Shimura lift is f_49a1;
# the same forms govern Xi = f (x) chi_-20 = f (x) chi_140 through the quadratic-twist family (Waldspurger).
import cypari2; pari=cypari2.Pari(); pari.allocatemem(4*10**9); pari.set_real_precision(38)
P=lambda s: pari(s)
P("E=ellinit([1,-1,0,-2,-1]); Ep=ellinit(elltwist(E,140)); af=ellan(E,200);")
print("a_p(49a1) for p=3,5,11,23,29,37,43:", P("[af[3],af[5],af[11],af[23],af[29],af[37],af[43]]"))
P("mfh=mfinit([196,3/2],1); Bh=mfbasis(mfh)")
print("dim S_3/2(Gamma0(196)) =", P("mfdim(mfh)"))
# common eigenspace of T(p^2) with eigenvalue a_p(f)
P("K=matid(mfdim(mfh)); foreach([3,5,11,23,29,37,43],p, my(M=mfheckemat(mfh,p^2)); K=K*matker(K~*0+ (M-af[p]*matid(#M))*K) ); ")
print("dim of {F : T(p^2)F = a_p(f) F, p in {3,5,11,23,29,37,43}} =", P("#K"))
P("Fs=vector(#K,j,mflinear(Bh,K[,j]))")
for j in range(int(P("#K"))):
    print(f" F_{j+1} coeffs n=0..60:", P(f"mfcoefs(Fs[{j+1}],60)"))
    for t in [1,3,5,6,10,13,17,19,20]:
        pass
# Shimura lifts: for each F and several t, lift should be c*f
P("fnew=mfeigenbasis(mfinit([49,2],1))[1]; fc=mfcoefs(fnew,40)")
for j in range(int(P("#K"))):
    out=[]
    for t in [1,2,3,5,6,7,10,11,13,14,15,17,19,20,21,22,23]:
        P(f"L=mfshimura(mfh,Fs[{j+1}],{t}); lc=mfcoefs(L[2],40)")
        prop=P("my(k=0); for(i=2,#fc,if(fc[i],k=i;break)); if(lc==vector(#lc,i,0),\"0\", if(lc*fc[k]==fc*lc[k], lc[k]/fc[k], \"NOT-prop\"))")
        out.append((t,str(prop)))
    print(f" F_{j+1}: Shimura lift S_t(F) = c_t * f_49a1 ; [t, c_t]:", out)
# Kohnen plus space (N=49 odd)
try:
    P("KB=mfkohnenbasis(mfh)")
    print("dim Kohnen plus space S^+_3/2(196) =", P("matsize(KB)[2]"))
    P("Kp=mfh; KF=vector(matsize(KB)[2],j,mflinear(Bh,KB[,j]))")
    # eigen-subspace inside plus space
    P("Mv=matconcat(K); Ip=matintersect(KB,Mv)")
    print("dim (plus space) ∩ (f-eigenspace) =", P("if(type(Ip)==\"t_MAT\",matsize(Ip)[2],0)"))
    if int(P("if(type(Ip)==\"t_MAT\",matsize(Ip)[2],0)"))>0:
        P("G=mflinear(Bh,Ip[,1]); gc=mfcoefs(G,200)")
        print(" Kohnen-plus eigenform G coeffs n=0..80:", P("gc[1..81]"))
        P("ix(D)=gc[abs(D)+1]")
        rows=[]
        for D in [-3,-4,-7,-8,-11,-15,-19,-20,-23,-24,-31,-35,-39,-40,-43,-47,-51,-52,-55,-56,-59,-67,-68,-71,-79,-83,-84,-87,-88,-91,-95]:
            if int(P(f"isfundamental({D})"))!=1: continue
            Lv=P(f"my(Ed=ellinit(elltwist(E,{D}))); [ellglobalred(Ed)[1], ellrootno(Ed), round(lfun(lfuncreate(Ed),1)*10^8)/10^8]")
            rows.append((D, str(P(f"ix({D})")), str(Lv)))
        print(" [D, c(|D|) of G, (cond, rootno, L(f x chi_D,1))]:")
        for r in rows: print("  ", r)
        print(" Xi check: D=-20 gives f x chi_-20 = f_Xi: c(20) =", P("ix(-20)"), " L(Xi,1) =", P("lfun(lfuncreate(Ep),1)"))
except cypari2.PariError as e:
    print("Kohnen ERR", e)
