# A(1): explicit criterion for odd s with s(s-2) squarefree (c = 1):
#   |Gbar| = h(K) phi(s-2),  |Gbar^sigma| = 2^{omega(s)} phi(s-2)  =>  u_L (coprime part) Eisenstein  <=>  h(Q(sqrt(s(s-2)))) = 2^{omega(s)},
#   number of non-genus pure characters = phi(s-2) (h - 2^{omega(s)}).   Class numbers certified with bnfcertify.
import cypari2, json, sys
pari = cypari2.Pari(); pari.allocatemem(2*10**9)
out = []
for s in range(5, int(sys.argv[1]) + 1, 2):
    D = s*(s-2)
    if not pari.issquarefree(D): continue
    K = pari(f'bnfinit(x^2-{D},1)'); h = int(pari('(K)->K.clgp.no')(K)); cert = int(pari.bnfcertify(K))
    w = len(pari.factor(s)[0]); phi = int(pari.eulerphi(s-2))
    out.append(dict(s=s, D0=D, h=h, certified=cert, omega_s=w, predicted=('Eis' if h == 2**w else 'CUSP'), n_nongenus_pred=phi*(h - 2**w)))
    print(json.dumps(out[-1]), flush=True)
json.dump(out, open('predict_c1.json', 'w'), indent=1)
