# Vectorised exact builder: integer phase exponents mod K = 2 D^2 for S (scaled by sqrt|det|), T, and label maps (neg, gamma, Z_p).
import numpy as np, math, sympy
from sympy.ntheory.modular import crt
from family_s import Family
class VF:
    def __init__(self,s):
        F=Family(s); self.F=F; D=F.D; self.D=D; A=F.A.astype(np.int64); self.A=A; self.K=2*D*D
        AL=np.array([l[0] for l in F.LABELS],dtype=np.int64); BE=np.array([l[1] for l in F.LABELS],dtype=np.int64)
        self.AL,self.BE=AL,BE; N=F.N; self.N=N
        BES=np.array(F.BES,dtype=np.int64)
        tab=-np.ones((D*D,len(BES)),dtype=np.int64)
        for i,(al,be) in enumerate(F.LABELS):
            b=F.BES.index(tuple(be)); tab[(al[0]%D)*D+al[1]%D,b]=i
        self.tab=tab; self.BESa=BES
    def b0idx(self,b):   # b: (...,2) array -> index of BES coset with A(b-b0) ≡ 0 mod D
        out=-np.ones(b.shape[:-1],dtype=np.int64)
        for k,b0 in enumerate(self.BESa):
            ok=np.all(((b-b0)@self.A.T)%self.D==0,axis=-1); out[ok&(out<0)]=k
        assert np.all(out>=0); return out
    def B2(self,x,y): return 2*np.einsum('...i,ij,...j->...',x,self.A,y)   # K*B(x,y)
    def reduce(self,a,b):  # returns index, exponent (mod K) of e(B(a,b-b0))
        k=self.b0idx(b); b0=self.BESa[k]; am=a%self.D
        idx=self.tab[am[...,0]*self.D+am[...,1],k]; assert np.all(idx>=0)
        return idx,self.B2(a,b-b0)%self.K
    def S_exp(self):
        F=self.F; LP=np.array(F.LP,dtype=np.int64); N=self.N
        E=-np.ones((N,N),dtype=np.int64)
        for i in range(N):
            al=self.AL[i]; be=self.BE[i]
            a=LP-be; b=np.broadcast_to(al,a.shape)
            j,ph=self.reduce(a,b); pre=self.B2(al,be)%self.K
            assert len(set(j.tolist()))==len(j)
            E[i,j]=(pre+ph)%self.K
        return E
    def T_exp(self):
        WC=np.array(self.F.WC,dtype=np.int64); a=self.AL; b=self.AL+self.BE+WC
        j,ph=self.reduce(a,b)
        Q2=np.einsum('ni,ij,nj->n',a,self.A,a)  # K*Q = x^T A x
        e=(-Q2-self.B2(a,np.broadcast_to(WC,a.shape))+ph)%self.K
        E=-np.ones((self.N,self.N),dtype=np.int64); E[np.arange(self.N),j]=e; return E
    def map_exp(self,Mint):  # label map al->M al, be->M be ; matrix X[j,i]=e(ph)
        a=(self.AL@Mint.T)%self.D; b=self.BE@Mint.T
        j,ph=self.reduce(a,b); E=-np.ones((self.N,self.N),dtype=np.int64); E[j,np.arange(self.N)]=ph; return E
    def maps(self):
        s=self.F.s; D=self.D; Mx=2*D; out={'neg':self.map_exp(-np.eye(2,dtype=np.int64)),'gamma':self.map_exp(self.F.G.astype(np.int64))}
        for p in [p for p in sympy.factorint(s*(s-2)) if p!=2]:
            pe=p**sympy.multiplicity(p,Mx); u=int(crt([pe,Mx//pe],[pe-1,1])[0])
            out[p]=self.map_exp(u*np.eye(2,dtype=np.int64))
        return out
def to_complex(E,K):
    X=np.zeros(E.shape,complex); m=E>=0; X[m]=np.exp(2j*np.pi*E[m]/K); return X
