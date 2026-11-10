# MR1: read-only extraction of N6 seed-component leading cusp-inf columns from on-disk mod-p 89-basis; verify rank 89 (pi_S injective mod p).
import csv,hashlib,sys
P=1027606441
SRC='/workspace/grok-batches/eigen-q89-basis/rhos/q89_basis_q18_modp.csv'
print('src sha256',hashlib.sha256(open(SRC,'rb').read()).hexdigest())
rows=list(csv.reader(open(SRC)))
assert rows[0][0].startswith('# p=1027606441')
hdr=rows[1][1:]; M=[[int(x)%P for x in r[1:]] for r in rows[2:]]
print('basis rows',len(M),'cols',len(hdr))
# rank mod p
A=[r[:] for r in M]; rk=0; nc=len(hdr)
for c in range(nc):
    piv=next((i for i in range(rk,len(A)) if A[i][c]),None)
    if piv is None: continue
    A[rk],A[piv]=A[piv],A[rk]; inv=pow(A[rk][c],P-2,P)
    A[rk]=[x*inv%P for x in A[rk]]
    for i in range(len(A)):
        if i!=rk and A[i][c]:
            f=A[i][c]; A[i]=[(x-f*y)%P for x,y in zip(A[i],A[rk])]
    rk+=1
    if rk==len(A): break
print('rank mod p',rk)
out=open('N6_D1_nu_columns_modp.csv','w')
out.write('nu,column,p,nz,first3,full_vector_by_basis_row\n')
for nu,a in [(1,0),(9,1),(29,2),(81,3),(109,4),(121,5)]:
    col='a%d_c0_e%d/140'%(a,nu); j=hdr.index(col); v=[M[i][j] for i in range(len(M))]
    nz=[(i,x) for i,x in enumerate(v) if x]
    f3=';'.join('%d:%d'%t for t in nz[:3])
    print(nu,col,'nz=%d/89'%len(nz),f3)
    out.write('%d,%s,%d,%d/89,%s,%s\n'%(nu,col,P,len(nz),f3,' '.join(map(str,v))))
