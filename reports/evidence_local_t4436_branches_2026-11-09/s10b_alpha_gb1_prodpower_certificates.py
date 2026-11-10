# Local-derived (PP fix A1, optional, second pass). For the 194 GB=[1] jobs that s10 could not certify within its degree bounds, look for
# a certificate  sum_i c_i g_i = P^k  (P = product of the substituted alpha's, k = 1,2), with deg c_i <= D (D <= 4) in the tau-variables.
# Such an identity shows every common zero of the g_i has P = 0, i.e. some alpha_k = 0, contradicting full support: the same conclusion as
# GB(g, zP-1) = [1], checkable by expansion. Exact rational linear algebra (python-flint), each identity re-verified by sympy.expand.
import sys, itertools, time, sympy as sp, flint, importlib.util, ast, os
sys.dont_write_bytecode=True
spec=importlib.util.spec_from_file_location("s10m","s10_alpha_gb1_cofactor_certificates.py")
src=open("s10_alpha_gb1_cofactor_certificates.py").read()
head=src.split("t0=time.time(); done=0")[0].replace("assert not os.path.exists(OUT)","")
ns={}; exec(compile(head,"s10_head","exec"),ns)
system=ns['system']; monos=ns['monos']
last=[l for l in open('s10_alpha_gb1_cofactor_certificates.log') if l.startswith('GB=[1] jobs:')][0]
fails=ast.literal_eval(last.split('degree bounds: 194 ',1)[1])
OUT='s10b_alpha_gb1_prodpower_certificates.txt'; fh=open(OUT,'x')
def certify_target(gens,vs,D,target):
    cols=[]; labels=[]
    for i,g in enumerate(gens):
        for m in monos(vs,D):
            cols.append(sp.Poly(sp.expand(m*g),*vs).as_dict()); labels.append((i,m))
    tdict=sp.Poly(target,*vs).as_dict()
    keys=sorted({k for c in cols for k in c}|set(tdict)); idx={k:j for j,k in enumerate(keys)}
    A=flint.fmpq_mat(len(keys),len(cols)+1)
    for j,c in enumerate(cols):
        for k,v in c.items():
            nu,de=sp.fraction(sp.Rational(v)); A[idx[k],j]=flint.fmpq(int(nu),int(de))
    for k,v in tdict.items():
        nu,de=sp.fraction(sp.Rational(v)); A[idx[k],len(cols)]=flint.fmpq(int(nu),int(de))
    R,r=A.rref()
    piv=[]; row=0
    for j in range(len(cols)+1):
        if row<len(keys) and R[row,j]!=0: piv.append(j); row+=1
    if len(cols) in piv: return None
    c=[sp.Integer(0)]*len(gens)
    for i,j in enumerate(piv):
        xv=sp.Rational(int(R[i,len(cols)].p),int(R[i,len(cols)].q))
        if xv: ii,m=labels[j]; c[ii]+=xv*m
    assert sp.expand(sum(ci*g for ci,g in zip(c,gens))-target)==0
    return c
t0=time.time(); cert=0; still=[]
for T,s in fails:
    eqs,prod,y,z=system(T,s); got=None
    for k in (1,2):
        for D in range(0,5):
            if len(y)>=6 and D>3: break
            got=certify_target(eqs,y,D,sp.expand(prod**k))
            if got is not None: kind=f'P^{k}, D={D}'; break
        if got is not None: break
    if got is None: still.append((T,s)); print('NO CERT',T,s,round(time.time()-t0),flush=True); continue
    cert+=1
    fh.write(f'JOB support={T} sign={s} vars={y} (sum c_i g_i = {kind}); P = {prod}; verified by sympy.expand\n')
    for ci,g in zip(got,eqs):
        if ci!=0: fh.write(f'  c = {ci}\n  g = {g}\n')
    fh.flush(); print('CERT',T,s,kind,round(time.time()-t0),flush=True)
fh.close()
print(f'second pass: {len(fails)} jobs; certified {cert}; still uncertified {len(still)} {still}')
