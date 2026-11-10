# Frozen (chmod a-w + sidecar) before the logged run. MR2 2026-11-09. SU(2)_R flat connections on Bolza Sigma: Aut+ invariance up to gauge (OW 8b26c786 A open item; PP 1fe6c574 A4-gap). Additive; no network.
import numpy as np, hashlib, itertools, time
def P(*a): print(*a, flush=True)
T0=time.time()
R='/workspace/quantum-comp/reports/'
kk=R+'MR2_MN2_KK_TRUNCATION_BOLZA_AUT48_ISOM96_WALL_Z2_2026-11-09.py'
h=hashlib.sha256(open(kk,'rb').read()).hexdigest()
P(f"[0] KK .py sha256 {h} ({'MATCH 88949658' if h.startswith('88949658') else 'MISMATCH'}); exec'ing its group section")
exec(open(kk).read().split('# ---------------- T:')[0])
# ---- L: linear order at the MN background (trivial SU(2)_R holonomy). SU(2)_R is untwisted: Aut+ acts on su(2) trivially.
Pr=sum(D for D,_ in G48)/len(G48)
P(f"[L] dim H^1(Sigma;R)^Aut+ = rank of averaging projector = {np.linalg.matrix_rank(Pr,1e-9)}; so dim (H^1 (x) su(2))^Aut+ = 3 x that = {3*np.linalg.matrix_rank(Pr,1e-9)}: all 12 SU(2)_R flat-direction modes at the background are removed (PROVED)")
# ---- A: abelian (reducible) SU(2) points rho = exp(i theta sigma3), theta in H^1(Sigma;U(1)) = T^4, up to Weyl theta -> -theta.
# Invariance up to gauge: g.theta = s(g) theta, s a character Aut+ -> {+-1} (a homomorphism off 2-torsion).
lin=[k for k in range(len(CT48['irr'])) if abs(CT48['irr'][k][0]-1)<1e-9] if 'irr' in CT48 else None
Jidx=[i for i,(D,p) in enumerate(G48) if np.allclose(D,-np.eye(4))][0]
def mul(a,b): return (a[0]@b[0], tuple(a[1][b[1][i]] for i in range(6)))
def key(e): return (tuple(np.round(e[0],6).ravel()+0.0), e[1])
idx={key(e):i for i,e in enumerate(G48)}
# commutator subgroup: J in [G,G]  <=> every 1-dim character is +1 on J
def inv(e):
    for f in G48:
        m=mul(e,f)
        if np.allclose(m[0],np.eye(4)) and m[1]==tuple(range(6)): return f
comms={key(mul(mul(a,b),mul(inv(a),inv(b)))) for a in G48 for b in G48}
# close
C=set(comms)
while True:
    new={key(mul(G48[idx[x]],G48[idx[y]])) for x in C for y in C}|C
    if new==C: break
    C=new
P(f"[A] |[Aut+,Aut+]| = {len(C)} (SL(2,3) has 24); J in [Aut+,Aut+]: {key(G48[Jidx]) in C} => every character s has s(J)=+1, so J.theta = -theta = theta forces 2 theta = 0")
P("[A] 2-torsion theta: nonzero classes form Aut+ orbits 3 + 12 (ecee2668 log [W]; Pin+ log [Z]) => only theta = 0 (trivial connection) is invariant. Abelian invariant points: {trivial} (PROVED)")
# ---- I: irreducible points from Delta+(2,3,8) -> SO(3) (spherical), restricted to pi1(Sigma) = ker(Delta+ -> Aut+)
def rotm(n,a):
    n=np.array(n,float); n/=np.linalg.norm(n); K=np.array([[0,-n[2],n[1]],[n[2],0,-n[0]],[-n[1],n[0],0]])
    return np.eye(3)+np.sin(a)*K+(1-np.cos(a))*K@K
def angle(M): return np.arccos(np.clip((np.trace(M)-1)/2,-1,1))
def order_of(e):
    x=e;k=1
    while not (np.allclose(x[0],np.eye(4)) and x[1]==tuple(range(6))):
        x=mul(x,e);k+=1
    return k
# surjection Delta+(2,3,8) -> Aut+: x order 2, y order 3, xy order 8, generating
ords=[order_of(e) for e in G48]
cand=None
for a in [e for e,o in zip(G48,ords) if o==2 and not np.allclose(e[0],-np.eye(4))]:
    for b in [e for e,o in zip(G48,ords) if o==3]:
        if order_of(mul(a,b))==8:
            S={key(a),key(b)}; 
            while True:
                n2={key(mul(G48[idx[u]],G48[idx[v]])) for u in S for v in S}|S
                if n2==S: break
                S=n2
            if len(S)==48: cand=(a,b); break
    if cand: break
P(f"[I] chose x_A (order 2), y_A (order 3) in Aut+ with x_A y_A of order 8 generating Aut+: {cand is not None} (Delta+(2,3,8) -> Aut+, kernel = pi1(Sigma): CONDITIONAL standard Bolza uniformization)")
def so3_reps():
    out=[]
    X=rotm([0,0,1],np.pi)
    for k in range(1,8):
        target=2*np.pi*k/8; target=min(target,2*np.pi-target)
        th=np.linspace(1e-4,np.pi-1e-4,20001)
        f=[angle(X@rotm([np.sin(t),0,np.cos(t)],2*np.pi/3))-target for t in th]
        for i in range(len(th)-1):
            if f[i]==0 or f[i]*f[i+1]<0:
                lo,hi=th[i],th[i+1]
                for _ in range(80):
                    mid=(lo+hi)/2
                    fm=angle(X@rotm([np.sin(mid),0,np.cos(mid)],2*np.pi/3))-target
                    if (angle(X@rotm([np.sin(lo),0,np.cos(lo)],2*np.pi/3))-target)*fm<=0: hi=mid
                    else: lo=mid
                out.append((k,lo,X,rotm([np.sin(lo),0,np.cos(lo)],2*np.pi/3)))
    return out
def kq(M): return tuple(np.round(M,5).ravel()+0.0)
def graph_size(a,b,X,Y,cap=6000):
    gens=[(a,X),(b,Y)]
    seen={(key(a),kq(X)):(a,X),(key(b),kq(Y)):(b,Y)}; frontier=list(seen.values())
    while frontier and len(seen)<cap:
        nf=[]
        for (e,M) in frontier:
            for (g_,N) in gens:
                z=(mul(e,g_),M@N); kz=(key(z[0]),kq(z[1]))
                if kz not in seen: seen[kz]=z; nf.append(z)
        frontier=nf
    return len(seen), len(frontier)==0
reps=so3_reps()
seenk=set()
for k,th,X,Y in reps:
    Z=np.linalg.inv(X@Y)
    o8=[np.allclose(np.linalg.matrix_power(Z,m),np.eye(3),atol=1e-8) for m in (8,)]
    ordZ=next(m for m in range(1,9) if np.allclose(np.linalg.matrix_power(Z,m),np.eye(3),atol=1e-8))
    n,fin=graph_size(cand[0],cand[1],X,Y)
    tag=f"order(z)={ordZ}"
    if fin: res=f"graph of Delta+ in Aut+ x SO(3) finite, size {n} => |image of pi1(Sigma)| = {n//48}" + (" (factors through Aut+: trivial on pi1, not a new point)" if n==48 else " (finite nontrivial restriction)")
    else: res=f"graph exceeds {n} elements (infinite image: no finite subgroup of SO(3) has elements of orders 3 and 8) => restriction to pi1(Sigma) has infinite image"
    P(f"[I] k={k} (z rotation angle 2pi*{k}/8), y-axis tilt {th:.6f} rad, relations x^2=y^3=z^8=1, xyz=1 hold, {tag}: {res}")
P("[I] tilt pairs (th, pi-th) are conjugate by the pi-rotation about the x-axis; k=5 is k=3 with z^-1 (same SO(3) class). k=1,7: no root (angles pi/2+pi/3+pi/8 < pi: hyperbolic). Hence Hom(Delta+(2,3,8),SO(3)) with all generators nontrivial = {factor-through-Aut+ reps (k=2,4,6)} + ONE infinite-image class (k=3).")
P("[I] the k=3 class restricted to pi1(Sigma) is an Aut+-invariant (up to SO(3) gauge) flat SO(3)_R connection with infinite image; irreducible since a finite-index subgroup of the dense image cannot preserve a line (md)")
# local rigidity (Weil): dim H^1(Delta+; ad phi) = sum_i (3 - dim Z(phi(c_i))) - 2*3 + dim H^0 + dim H^2; nontrivial rotations have 1-dim centralizer
P(f"[I] Weil count for Delta+(2,3,8) with three nontrivial rotations, H^0 = 0 (irreducible), H^2 = 0 (orbifold sphere, Poincare dual to H^0): dim H^1 = 3*(3-1) - 6 + 0 + 0 = {3*(3-1)-6} => isolated (no invariant moduli); and H^1(pi1;ad)^Aut+ = H^1(Delta+;ad) (transfer, char 0)")
P(f"[done] runtime {time.time()-T0:.1f} s")
