# (i) phi_4 well-defined on SL2(Z/4): enumerate pairs (rho, matrix mod 4); (ii) central signs: S_p^2 = rho(-I_p) scalars on each joint piece; model S^2 vs reflection.
exec(open('local.py').read().split("iso={}")[0])
o=[]
def restr(Wsp,M): return Wsp.conj().T@M@Wsp
S4=(np.array([[0,-1],[1,0]])%4).astype(complex); T4=(np.array([[1,1],[0,1]])%4).astype(complex)
class M4w:
    pass
def enum4(maxn=5000):
    key=lambda g: np.rint(np.concatenate([g[0].real.ravel(),g[0].imag.ravel()])*1e4).astype(np.int64).tobytes()+np.array(g[1],dtype=np.int64).tobytes()
    gens=[(SP[4],np.array([[0,-1],[1,0]])%4),(TP[4],np.array([[1,1],[0,1]]))]
    st=(Id,np.eye(2,dtype=int)); els={key(st):st}; fr=[st]
    while fr:
        nf=[]
        for g in fr:
            for h in gens:
                n=(g[0]@h[0],(g[1]@h[1])%4); k=key(n)
                if k not in els: els[k]=n; nf.append(n)
        fr=nf
    return list(els.values())
G=enum4(); o.append(f"pairs (rho_W(g), g mod 4) generated: {len(G)} = |SL2(Z/4)| -> rho on the 2-local subgroup is a function of g mod 4 (phi_4 well defined)")
for p in (5,7):
    Sm_,Tm_=models[p]; x=np.arange(p); Z=np.zeros((p,p)); Z[x,(-x)%p]=1
    sc=Sm_@Sm_; o.append(f"model Weil p={p}: S^2 = {np.round(np.trace(sc@Z)/p,6)} * Z (Z = reflection x->-x)  => -I acts on W{p}^+ by {np.round(np.trace(sc@Z)/p,6)} and on W{p}^- by {np.round(-np.trace(sc@Z)/p,6)}")
for nm,Wsp in (("V_Eis",VE),("V_cusp",VC)):
    o.append(f"{nm}: scalars of rho(M_p)^2 (= rho(-I at p)): "+", ".join(f"p={p}: {np.round(np.trace(restr(Wsp,SP[p]@SP[p]))/Wsp.shape[1],6)}" for p in (4,5,7)))
# V^perp pieces
w,U=np.linalg.eigh(restr(Vp,SP[4]@SP[4]).real if False else (restr(Vp,SP[5]@SP[5])+restr(Vp,SP[5]@SP[5]).conj().T)/2)
o.append(f"V^perp: eigenvalues of rho(M_5)^2: {sorted(set(np.round(w,6)))}")
print("\n".join(o)); open("extra.txt","w").write("\n".join(o)+"\n")
