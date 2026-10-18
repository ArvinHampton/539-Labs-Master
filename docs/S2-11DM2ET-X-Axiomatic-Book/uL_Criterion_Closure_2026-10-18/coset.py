# Coset property for all c-parts.
# Lemma (proved in report Sec. 4): W = {u in (O/M)^x : u*(beta0+L) = beta0+L mod M}.  For lambda in O, lambda >> 0, coprime to M,
# lambda mod M in W:  beta -> lambda*beta maps admissible beta with c-part c to admissible beta with the same c-part, so
# T_c + psi(W) = T_c for EVERY c (psi(lambda) = class of (lambda)).  If S0 := Stab(T_0) equals psi(W), every T_c is a union
# of S0-cosets (coset property, all c at once).  If moreover Hbar = 1 (H in S0 + <j>), every c-part is genus-pure.
import sys, json, itertools, numpy as np
from alg_T import *
def W_local(E):
    K = E['K']; M = E['M']; tob = E['tob']
    Lm = pari.matrix(2, 2, [int(E['Lmat'][0,0]), int(E['Lmat'][0,1]), int(E['Lmat'][1,0]), int(E['Lmat'][1,1])])
    def inL(a):
        X = pari.matsolve(Lm, pari.mattranspose(pari.Mat(pari(tob(a)))))
        return str(pari.type(X[0, 0])) == 't_INT' and str(pari.type(X[1, 0])) == 't_INT'
    zk = pari('(K)->K.zk')(K); om = pari.nfbasistoalg(K, zk[1])
    out = {}
    for p in E['mprimes']:
        q = p**int(pari.valuation(M, p)); r = M//q
        Wp = []
        for a0 in range(q):
            for a1 in range(q):
                # CRT: u = a0 + a1*om mod q, u = 1 mod r
                c0 = int(pari.chinese(pari.Mod(a0, q), pari.Mod(1, r)).lift()); c1 = int(pari.chinese(pari.Mod(a1, q), pari.Mod(0, r)).lift())
                u = c0 + c1*om
                if int(pari.norm(pari.Mod(u, pari('x^2-%d' % E['D0'])))) % p == 0: continue
                if not inL((u - 1)*E['b0']) or not inL(u*E['l1']) or not inL(u*E['l2']): continue
                Wp.append(u)
        out[p] = Wp
    return out
def psi(E, u):
    K = E['K']; M = E['M']
    emb = [abs(float(z)) for z in pari.nfeltembed(K, u)]; k = int(max(emb)/M) + 2
    return E['cls'](pari.idealhnf(K, u + k*M))
def analyse(s, expos=()):
    E = setup(s); cycv = np.array(E['cyc'])
    T0 = T_c(E, {}); cr, S0, SJ = crit(E, T0)
    Wl = W_local(E)
    psiW = closure([psi(E, u) for p in Wl for u in Wl[p]], cycv)
    H = closure(Hgens(E), cycv)
    res = dict(s=s, cyc=E['cyc'], crit=cr, W_sizes={p: len(v) for p, v in Wl.items()}, psiW=len(psiW), S0=len(S0),
               S0_eq_psiW=(S0 == psiW), psiW_sub_S0=psiW <= S0,
               H_in_psiW_plus_j=H <= closure(list(psiW) + [tuple((E['jv'] % cycv).tolist())], cycv))
    parts = []
    for ex in expos:
        expo = {E['key'](P): e for P, e in zip(E['Ps'], ex)}
        T, cnt, tot = T_c(E, expo, True)
        if not T: parts.append(dict(e=ex, empty=True)); continue
        inv = all(tuple(((np.array(t) + np.array(g)) % cycv).tolist()) in T for t in T for g in psiW)
        invS0 = all(tuple(((np.array(t) + np.array(g)) % cycv).tolist()) in T for t in T for g in S0)
        parts.append(dict(e=ex, n=len(T), residues=cnt, psiW_inv=inv, S0_union_cosets=invS0, n_cosets=len(T)//len(S0), pure=genus_pure(E, T)))
    res['primes'] = [list(map(str, E['key'](P))) for P in E['Ps']]
    res['parts'] = parts
    return res
if __name__ == "__main__":
    s = int(sys.argv[1]); emax = int(sys.argv[2]) if len(sys.argv) > 2 else 0
    E = setup(s); nP = len(E['Ps'])
    expos = [ex for ex in itertools.product(range(emax+1), repeat=nP) if any(ex)] if emax else []
    r = analyse(s, expos)
    print(json.dumps(r), flush=True)
    json.dump(r, open(f'coset_s{s}_e{emax}.json', 'w'), indent=1)
