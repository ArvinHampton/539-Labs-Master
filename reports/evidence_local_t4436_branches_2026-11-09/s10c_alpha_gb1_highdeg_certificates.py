# Local-derived (PP fix A1', optional, third pass). For the 146 GB=[1] jobs left uncertified by s10/s10b (they have 2-6 tau-variables),
# search  sum_i c_i g_i = P^k  (k = 1,2) with deg c_i <= D for D = 4..7. The degree D is found by a rank test mod p = 2^61-1 (nmod_mat);
# the exact cofactors are then solved over Q on the mod-p pivot columns (fmpq_mat rref), and every identity is re-verified by sympy.expand.
# Only exact, expansion-verified identities count as certificates. No grade depends on this file.
import sys, time, ast, sympy as sp, flint
sys.dont_write_bytecode=True
src=open("s10_alpha_gb1_cofactor_certificates.py").read()
head=src.split("t0=time.time(); done=0")[0].replace("assert not os.path.exists(OUT)","")
ns={}; exec(compile(head,"s10_head","exec"),ns); system=ns['system']; monos=ns['monos']
l=[x for x in open('s10b_alpha_gb1_prodpower_certificates.log') if x.startswith('second pass')][0]
jobs=ast.literal_eval(l.split('still uncertified 146 ',1)[1]); assert len(jobs)==146
jobs.sort(key=lambda j: len(j[0]))
PR=(1<<61)-1
OUT='s10c_alpha_gb1_highdeg_certificates.txt'; fh=open(OUT,'x')
def build(gens,vs,D,target):
    cols=[]; labels=[]
    for i,g in enumerate(gens):
        for m in monos(vs,D):
            cols.append(sp.Poly(sp.expand(m*g),*vs).as_dict()); labels.append((i,m))
    td=sp.Poly(target,*vs).as_dict()
    keys=sorted({k for c in cols for k in c}|set(td)); idx={k:j for j,k in enumerate(keys)}
    return cols,labels,td,keys,idx
def modp(v):
    v=sp.Rational(v); return int(v.p)*pow(int(v.q),-1,PR)%PR
def try_cert(gens,vs,D,target):
    cols,labels,td,keys,idx=build(gens,vs,D,target)
    nr,nc=len(keys),len(cols)
    A=flint.nmod_mat(nr,nc+1,PR)
    for j,c in enumerate(cols):
        for k,v in c.items(): A[idx[k],j]=modp(v)
    for k,v in td.items(): A[idx[k],nc]=modp(v)
    R=A.rref()[0]
    piv=[]; row=0
    for j in range(nc+1):
        if row<nr and int(R[row,j])!=0: piv.append(j); row+=1
    if nc in piv: return None, (nr,nc)
    Q=flint.fmpq_mat(nr,len(piv)+1)
    for jj,j in enumerate(piv):
        for k,v in cols[j].items():
            v=sp.Rational(v); Q[idx[k],jj]=flint.fmpq(int(v.p),int(v.q))
    for k,v in td.items():
        v=sp.Rational(v); Q[idx[k],len(piv)]=flint.fmpq(int(v.p),int(v.q))
    RQ=Q.rref()[0]
    qp=[]; row=0
    for j in range(len(piv)+1):
        if row<nr and RQ[row,j]!=0: qp.append(j); row+=1
    if len(piv) in qp: return None, (nr,nc)   # spurious mod-p consistency
    c=[sp.Integer(0)]*len(gens)
    for r_,jj in enumerate(qp):
        x=RQ[r_,len(piv)]
        if x!=0: i,m=labels[piv[jj]]; c[i]+=sp.Rational(int(x.p),int(x.q))*m
    assert sp.expand(sum(ci*g for ci,g in zip(c,gens))-target)==0
    return c,(nr,nc)
t0=time.time(); cert=0; still=[]
for T,s in jobs:
    eqs,prod,y,z=system(T,s); got=None
    for D in range(4,8):
        for k in (1,2):
            tj=time.time()
            got,shape=try_cert(eqs,y,D,sp.expand(prod**k))
            print(f'  {T} {s} vars={len(y)} D={D} k={k} matrix {shape[0]}x{shape[1]}: {"CERT" if got else "no"} {time.time()-tj:.0f}s',flush=True)
            if got is not None: kind=f'P^{k}, D={D}'; break
        if got is not None: break
    if got is None: still.append((T,s)); print('NO CERT',T,s,round(time.time()-t0),flush=True); continue
    cert+=1
    fh.write(f'JOB support={T} sign={s} vars={y} (sum c_i g_i = {kind}); P = {prod}; verified by sympy.expand\n')
    for ci,g in zip(got,eqs):
        if ci!=0: fh.write(f'  c = {ci}\n  g = {g}\n')
    fh.flush(); print('CERT',T,s,kind,round(time.time()-t0),flush=True)
fh.close()
print(f'third pass: {len(jobs)} jobs; certified {cert}; still uncertified {len(still)} {still}')
