# Path A: function-span method for the S/T theta-lift family u_{al,be} of A_s=[[2,s],[s,s]] (family_s.py, all s).
#  (1) Fourier coefficient matrix C (labels x modes, + constant column), exact cone sums over gamma^K-fundamental domains:
#      coefficient of u_{al,be} at q:  (1/K) sum_{i<K} sum_{cones} sum_{nu in cone, gamma^i nu = al mod Z^2} e(B(gamma^i nu, be)),
#      cones: [e1, g e1), -[e1, g e1) (Q>0) and [f, g f), -[f, g f) (Q<0), f=(1,-1)  (as 2026-10-17-cusp-part/uvec.py, generalised).
#      Constant term: log(lambda_gamma) on labels with al = 0 mod Z^2.
#      dim V = rank C = sum over T-eigenblocks (q mod 1) of block ranks (distinct T-eigenvalues => independent).
#  (2) Eisenstein span: V_E = span of values of the Eisenstein part u_E = W := rho(SL2(Z))-cyclic span of the constant-term vector c
#      (a lambda=1/4 Maass form with zero constant terms at all cusps is cuspidal; constant term of xu at the cusp g^{-1}oo is x rho(g) c).
#  (3) Cusp span V_C (span of values of u_C): blockwise  dim(V_r+W_r)-dim W_r <= dim V_C,r <= dim(V_r+W_r);  exact if W_r = 0.
import numpy as np, math, sys, time, json
from fractions import Fraction as Fr
from family_s import Family
def run(s, Qmax, verbose=True):
    t0 = time.time(); F = Family(s); D = F.D; N = F.N; A = F.A; G = F.G
    K = F.gamma_order()
    S = F.Smatrix(); T = F.Tmatrix(); P = F.Pmatrix()
    lamg = (s-1) + math.sqrt(s*s-2*s); LOG = math.log(lamg)
    ALS = [np.array(a) for a in F.ALS]; alidx = {tuple(a): i for i, a in enumerate(F.ALS)}
    BES = [np.array(b) for b in F.BES]
    lab = {(tuple(al), tuple(be)): F.IDX[(tuple(al), tuple(be))] for al in F.ALS for be in F.BES}
    rows = []; Ms = []; vals = []
    e1 = np.array([1, 0]); f = np.array([1, -1])
    Gi = [np.linalg.matrix_power(G, i) for i in range(K)]
    for r1 in (e1, f):
        r2 = G@r1; det = int(r1[0]*r2[1] - r1[1]*r2[0]); sg = 1 if det > 0 else -1
        Q1 = abs(r1@A@r1)/2; Q2v = abs(r2@A@r2)/2
        Xm = math.sqrt(Qmax/min(Q1, Q2v)) + 1     # x,y <= Xm (form restricted to the quadrant >= a x^2 etc.)
        corners = np.array([[0, 0], r1*Xm, r2*Xm, (r1+r2)*Xm])
        k_lo, k_hi = corners[:, 1].min()-1, corners[:, 1].max()+1
        for al in ALS:
            a1, a2 = al[0]/D, al[1]/D
            k = np.arange(math.floor(k_lo - a2), math.ceil(k_hi - a2)+1); nu2 = a2 + k
            # nu1 range from parallelogram: nu = x r1 + y r2, 0<=x,y<=Xm
            n_lo = math.floor(corners[:, 0].min() - a1) - 1; n_hi = math.ceil(corners[:, 0].max() - a1) + 1
            n = np.arange(n_lo, n_hi+1)
            NN, KK = np.meshgrid(n, k, indexing='ij'); X1 = al[0] + D*NN.ravel(); X2 = al[1] + D*KK.ravel()   # X = D nu (integers)
            for sgn in (1, -1):
                Y1, Y2 = sgn*X1, sgn*X2      # point nu' = sgn*mu with mu in cone ; here mu = (X1,X2)/D, nu = sgn*mu, and nu = al-coset point means mu in sgn*al+Z^2
                # we enumerate mu in coset al (al ranges over the symmetric set ALS), membership in cone [r1,r2): x>0, y>=0
                xs = (X1*r2[1] - X2*r2[0])*sg; ys = (r1[0]*X2 - r1[1]*X1)*sg
                m = (xs > 0) & (ys >= 0)
                Qi = (2*X1[m]*X1[m] + 2*s*X1[m]*X2[m] + s*X2[m]*X2[m])        # = 2 D^2 Q(mu), integer
                keep = (np.abs(Qi) <= 2*D*D*Qmax) & (Qi != 0)
                P1, P2, QQ = Y1[m][keep], Y2[m][keep], Qi[m.nonzero()[0]*0 + np.arange(m.sum())][keep] if False else Qi[keep]
                for i in range(K):
                    Z1 = Gi[i][0, 0]*P1 + Gi[i][0, 1]*P2; Z2 = Gi[i][1, 0]*P1 + Gi[i][1, 1]*P2     # gamma^i nu'
                    alr = np.stack([Z1 % D, Z2 % D], 1)
                    for be in BES:
                        ph = np.exp(2j*np.pi*((Z1*(A[0, 0]*be[0] + A[0, 1]*be[1]) + Z2*(A[1, 0]*be[0] + A[1, 1]*be[1])) % (D*D))/(D*D))
                        idx = np.array([lab[((int(x), int(y)), tuple(be))] for x, y in alr]) if len(alr) else np.zeros(0, int)
                        rows.append(idx); Ms.append(QQ.astype(np.int64)); vals.append(ph/K)
    rows = np.concatenate(rows); Ms = np.concatenate(Ms); vals = np.concatenate(vals)
    # constant column (mode key 0)
    c = np.zeros(N, complex)
    for be in BES:
        c[lab[((0, 0), tuple(be))]] = LOG
    # blocks by M mod 2D^2
    MOD = 2*D*D; blk = Ms % MOD
    order = np.lexsort((Ms, blk)); rows, Ms, vals, blk = rows[order], Ms[order], vals[order], blk[order]
    ub, starts = np.unique(blk, return_index=True); ends = list(starts[1:]) + [len(blk)]
    Vb = {}; rankV = 0
    for b_, st, en in zip(ub, starts, ends):
        r_, M_, v_ = rows[st:en], Ms[st:en], vals[st:en]
        um, mi = np.unique(M_, return_inverse=True); ur, ri = np.unique(r_, return_inverse=True)
        Cm = np.zeros((len(ur), len(um) + (1 if b_ == 0 else 0)), complex)
        np.add.at(Cm, (ri, mi), v_)
        if b_ == 0:   # constant column belongs to the q=0 block
            for i_, rr in enumerate(ur): Cm[i_, -1] = c[rr]
        if b_ == 0 and not np.isin(np.nonzero(c)[0], ur).all():
            extra = [x for x in np.nonzero(c)[0] if x not in ur]; ur = np.concatenate([ur, extra]); Cm = np.vstack([Cm, np.zeros((len(extra), Cm.shape[1]))]); Cm[-len(extra):, -1] = c[extra]
        U, sv, _ = np.linalg.svd(Cm, full_matrices=False)
        rk = int((sv > 1e-9*max(1, sv[0])).sum()) if len(sv) else 0
        Vb[int(b_)] = (ur, U[:, :rk]); rankV += rk
    if 0 not in Vb:
        nz = np.nonzero(c)[0]; Vb[0] = (nz, (c[nz]/np.linalg.norm(c[nz]))[:, None]); rankV += 1
    # W: cyclic span of c under S, T
    Wb = (c/np.linalg.norm(c))[:, None]
    while True:
        cand = np.hstack([Wb, S@Wb, T@Wb])
        U, sv, _ = np.linalg.svd(cand, full_matrices=False); rk = int((sv > 1e-9*sv[0]).sum())
        if rk == Wb.shape[1]: break
        Wb = U[:, :rk]
    dimW = Wb.shape[1]
    # T-eigen decomposition of W
    R = Wb.conj().T@T@Wb; ev, evec = np.linalg.eig(R)
    rr = np.rint((np.angle(ev)/(2*np.pi)) % 1*MOD).astype(np.int64) % MOD
    Wblocks = {}
    for b_ in np.unique(rr):
        sel = rr == b_; Wv = Wb@evec[:, sel]
        U, sv, _ = np.linalg.svd(Wv, full_matrices=False); Wblocks[int(b_)] = U[:, :int((sv > 1e-9*sv[0]).sum())]
    # blockwise cusp bounds
    lo = hi = exact_part = 0; mixed_blocks = []
    for b_, (ur, Ub) in Vb.items():
        dv = Ub.shape[1]
        Vfull = np.zeros((N, dv), complex); Vfull[ur, :] = Ub
        if b_ in Wblocks:
            Wr = Wblocks[b_]; dw = Wr.shape[1]
            sv = np.linalg.svd(np.hstack([Vfull, Wr]), compute_uv=False); dvw = int((sv > 1e-9*sv[0]).sum())
            lo += dvw - dw; hi += min(dvw, dv + dw)
            mixed_blocks.append((b_, dv, dw, dvw))
        else:
            lo += dv; hi += dv; exact_part += dv
    # W inside V ?
    Wb_in_V = all(np.linalg.norm(Wblocks[b_] - (np.zeros((N, 0)) if b_ not in Vb else
                  (lambda ur, Ub: (lambda Vf: Vf@(Vf.conj().T@Wblocks[b_]))(np.pad(np.zeros((0, 0)), 0) if False else _emb(N, ur, Ub)))(*Vb[b_]))) < 1e-7 for b_ in Wblocks)
    # u_L block info
    aL = tuple(int(z) for z in F.a % D); iL = lab[(aL, (0, 0))]
    c0 = Fr(s, 4*(s-2)); rL = int((-c0*MOD) % MOD)   # q = Q(nu) for nu in a+Z^2 is -c0 mod 1
    info = dict(s=s, N=N, K=K, D=D, Qmax=Qmax, dimV=rankV, dimW=dimW, cusp_lo=lo, cusp_hi=hi, cusp_exact_part=exact_part,
                n_blocks=len(Vb), W_blocks=len(Wblocks), mixed_blocks=len(mixed_blocks), W_in_V=bool(Wb_in_V),
                uL_block_has_W=rL in Wblocks, uL_block_dimV=(Vb[rL][1].shape[1] if rL in Vb else 0), uL_block_dimW=(Wblocks[rL].shape[1] if rL in Wblocks else 0),
                relations=dict(S2_P=float(np.abs(S@S - P).max()), ST3_on_FixP=float(np.abs((np.linalg.matrix_power(S@T, 3) - np.eye(N))@_fixP(P)).max())),
                time=round(time.time()-t0, 1))
    if verbose: print(json.dumps(info), flush=True)
    return info
def _emb(N, ur, Ub):
    V = np.zeros((N, Ub.shape[1]), complex); V[ur, :] = Ub; return V
def _fixP(P):
    w, v = np.linalg.eig(P); return v[:, np.abs(w-1) < 1e-8]
if __name__ == "__main__":
    s = int(sys.argv[1]); Qm = float(sys.argv[2]); run(s, Qm)
