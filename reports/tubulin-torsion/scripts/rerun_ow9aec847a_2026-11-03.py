# Re-run checks under OW 9aec847a definitions. numpy only.
import numpy as np, itertools
def ad(X):
    n=X.shape[0]; I=np.eye(n)
    return np.kron(X,I)-np.kron(I,X.T)   # vec(XY-YX) row-major
print("== Pi_fast with Ad=[X,.] ==")
for M in (3,5,7):
    z=np.exp(2j*np.pi/M)
    D=np.diag([1,-1,1,-1]).astype(complex)  # wedge model: parity +-1 shifts
    ops=[ad((z**t-1)*D) for t in range(M)]
    avg=sum(ops)/M
    for t in range(M):
        P=ops[t]-avg            # (Id - time average) o Ad_{(z^t-1)wedge}
        ev=np.round(np.linalg.eigvals(P),6)
        print(f"M={M} t={t} idempotent={np.allclose(P@P,P)} tr={np.round(np.trace(P),9)} spec={sorted(set(ev.tolist()),key=abs)}")
    # time-averaged operator itself
    print(f"M={M} avg(ad)=ad(mean X) tr={np.round(np.trace(avg),9)} nilpotent_part? spec={sorted(set(np.round(np.linalg.eigvals(avg),6).tolist()),key=abs)}")
# random X: tr ad_X = 0 always
X=np.random.randn(5,5)+1j*np.random.randn(5,5); print("tr ad_X random:",np.round(np.trace(ad(X)),9))
N=np.array([[0,1],[0,0]],complex); A=ad(N); print("ad nilpotent X: A^3==0",np.allclose(A@A@A,0), "A^2==A",np.allclose(A@A,A))
print("== odd M: det rho(h)!=0 automatic for h=[0]+[w] ==")
bad=[(M,w) for M in range(3,40,2) for w in range(M) for k in range(M) if abs(1+np.exp(2j*np.pi*k*w/M))<1e-9]
print("zeros found:",bad)
print("== Lemma5 slice needs M>Sigma: wraparound example M=3, w={1,2}, target 0 ==")
w=[1,2]; S=[s for s in itertools.product([0,1],repeat=2) if sum(a*b for a,b in zip(s,w))%3==0]
print("subsets hitting 0 mod 3:",S,"(true SS target 0 only by empty set; (1,1) sum=3 is false positive)")
print("== T3 budget 18+521 =",18+521,"=7^2*11:",7*7*11)
print("== HQCC orbit growth (Codex Phi, see codex_items script) reused ==")
