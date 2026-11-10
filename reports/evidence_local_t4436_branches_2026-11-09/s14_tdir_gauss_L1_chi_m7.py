# Local-derived (t4436, T-Dir / a-3). Exact certificates supporting
# FINDINGS_LOCAL_t4436_TDIR_GAUSS_AND_A3_L1_CHI_M7_2026-11-10_*.md
#
# [G4]  G(chi_{-4}) = 2i, by a 4-term sum (exact).
# [G5]  In Z[zeta_5]/(Phi_5): phi=zeta+zeta^4 and psi=zeta^2+zeta^3 satisfy
#       phi+psi=-1, phi*psi=-1, so they are the roots of X^2+X-1=0;
#       G = 1+2*phi, and G^2=5 exactly. The sign G=+sqrt(5) is the root
#       of X^2-5=0 that equals 1+2*phi with phi=((-1)+sqrt(5))/2>0, as
#       proved in the findings (X^2+X-1, positive root).
# [G140] Assembly: chi_140 = chi_{-4} chi_{-35}, chi_{-35}=chi_5 chi_{-7},
#       Gauss-sum product formula with exact Kronecker factors
#       chi_{-4}(35)=-1, chi_{-35}(4)=1, chi_5(7)=-1, chi_{-7}(5)=-1,
#       and G(chi_{-7})=i*sqrt(7) from the already-filed T-theta1 certificate
#       (s13 [G], not re-edited here). Result: G(chi_140)=sqrt(140).
# [S7]  sum_{m=1}^{6} m chi_{-7}(m) = -7, exact (six-term sum).
# No PARI. No floating point is used in any certificate.
# The Kronecker implementation is checked against a short table.

def kronecker(D,n):
    D=int(D); n=int(n)
    if n==0:
        return 1 if abs(D)==1 else 0
    sign=1
    if n<0:
        if D<0:
            sign=-1
        n=-n
    odd,v=n,0
    while odd%2==0:
        odd//=2; v+=1
    res=sign
    if v:
        if D%2==0:
            return 0
        t=(D*D-1)//8
        if v%2==1 and t%2==1:
            res=-res
    def jacobi(a,m):
        a=a%m
        if a<0:
            a+=m
        r=1
        while a!=0:
            while a%2==0:
                a//=2
                if m%8 in (3,5):
                    r=-r
            a,m=m,a
            if a%4==3 and m%4==3:
                r=-r
            a=a%m
        return r if m==1 else 0
    if odd>1:
        res*=jacobi(D,odd)
    return res

# table checks
assert kronecker(-4,1)==1 and kronecker(-4,2)==0 and kronecker(-4,3)==-1
assert kronecker(-4,-1)==-1 and kronecker(5,-1)==1 and kronecker(140,-1)==1
assert kronecker(-7,-1)==-1 and kronecker(-35,-1)==-1
assert kronecker(5,1)==1 and kronecker(5,2)==-1 and kronecker(5,3)==-1 and kronecker(5,4)==1

print('=== [G4] G(chi_{-4}) = 2i ===')
# G = sum_{k=0}^{3} chi_{-4}(k) exp(2 pi i k/4) = chi(1)*i + chi(3)*(-i)
# chi(1)=1, chi(3)=-1, so i - (-i) = 2i
terms=[(k, kronecker(-4,k)) for k in range(4)]
print('chi_{-4}(k) for k=0..3:', terms)
# exactly: G = 1*(i) + (-1)*(-i) = 2i
print('G = 1*i + (-1)*(-i) = 2i')
assert terms==[(0,0),(1,1),(2,0),(3,-1)]

print('=== [G5] G(chi_5)^2 = 5 in Z[zeta_5], and G=1+2*phi ===')
# Basis 1,z,z^2,z^3 of Z[x]/(1+x+x^2+x^3+x^4); z^4=-1-z-z^2-z^3
def red5(c):
    c=list(c)
    while len(c)>4:
        ak=c.pop()
        deg=len(c)          # we popped x^{deg}
        # x^4 = -1-x-x^2-x^3, x^{4+r} = -x^r(1+x+x^2+x^3)
        r=deg-4
        while len(c)<r+4:
            c.append(0)
        for i in range(4):
            c[r+i]-=ak
    while len(c)<4:
        c.append(0)
    if len(c)>4:
        return red5(c)
    return c[:4]

def mul5(a,b):
    r=[0]*8
    for i,ai in enumerate(a):
        for j,bj in enumerate(b):
            r[i+j]+=ai*bj
    return red5(r)

def add5(a,b):
    return [a[i]+b[i] for i in range(4)]

# zeta^4 reduced: -1-z-z^2-z^3
z4=red5([0,0,0,0,1])
print('zeta^4 reduced:', z4)   # should be [-1,-1,-1,-1]
assert z4==[-1,-1,-1,-1]
phi=add5([0,1,0,0], z4)        # zeta + zeta^4
psi=add5([0,0,1,0], [0,0,0,1]) # zeta^2 + zeta^3
print('phi=zeta+zeta^4:', phi)
print('psi=zeta^2+zeta^3:', psi)
print('phi+psi:', add5(phi,psi), 'expected -1 (=[-1,0,0,0] after using 1+z+z2+z3+z4=0)?')
# 1+z+z2+z3+z4=0 so 1+z+z2+z3 = -z4, not immediately -1 in this basis.
# In C, phi+psi=-1. In the basis, phi+psi = (z+z^4)+(z^2+z^3)= z+z^2+z^3+z^4 = -1.
# z^4 is already reduced, so phi+psi = [0,1,1,1] + [-1,-1,-1,-1] = [-1,0,0,0]. Yes.
print('phi+psi reduced:', add5(phi,psi))
assert add5(phi,psi)==[-1,0,0,0]
print('phi*psi:', mul5(phi,psi), 'expected -1')
assert mul5(phi,psi)==[-1,0,0,0]
# G = chi_5(1) z + chi_5(2) z^2 + chi_5(3) z^3 + chi_5(4) z^4
#   = z - z^2 - z^3 + z^4 = (z+z^4) - (z^2+z^3) = phi-psi
G=add5(phi, [-psi[0],-psi[1],-psi[2],-psi[3]])
print('G=phi-psi:', G)
# also 1+2*phi
one_plus_2phi=add5([1,0,0,0], [2*c for c in phi])
print('1+2*phi:', one_plus_2phi)
assert G==one_plus_2phi
G2=mul5(G,G)
print('G^2:', G2, 'equals 5?', G2==[5,0,0,0])
assert G2==[5,0,0,0]
print('X^2+X-1: findings identify phi as the positive root ((-1)+sqrt(5))/2, hence G=sqrt(5)')

print('=== [G140] Kronecker factors and assembly ===')
a=kronecker(-4,35); b=kronecker(-35,4)
c=kronecker(5,7); d=kronecker(-7,5)
print('chi_{-4}(35)=',a, 'chi_{-35}(4)=',b)
print('chi_5(7)=',c, 'chi_{-7}(5)=',d)
assert (a,b,c,d)==(-1,1,-1,-1)
# G(chi_140) = chi_{-4}(35) chi_{-35}(4) G(chi_{-4}) G(chi_{-35})
# G(chi_{-35}) = chi_5(7) chi_{-7}(5) G(chi_5) G(chi_{-7})
# = (-1)*(-1)*sqrt(5)*i*sqrt(7) = i*sqrt(35)
# G(chi_140) = (-1)*(1)*(2i)*(i*sqrt(35)) = -2i*i*sqrt(35)=2*sqrt(35)=sqrt(140)
print('G(chi_{-35}) = (chi_5(7)*chi_{-7}(5))*sqrt(5)*i*sqrt(7) = i*sqrt(35)')
print('G(chi_140) = (chi_{-4}(35)*chi_{-35}(4))*2i*i*sqrt(35) = -2 i^2 sqrt(35) = 2*sqrt(35) = sqrt(140)')

print('=== [S7] sum_{m=1..6} m chi_{-7}(m) ===')
vals=[(m,kronecker(-7,m),m*kronecker(-7,m)) for m in range(1,7)]
s=sum(t[2] for t in vals)
print('terms:', vals)
print('sum =', s)
assert s==-7
# Hence, by the sawtooth formula in the findings,
# L(1,chi_{-7}) = - (pi i / (7 * G)) * sum = - (pi i / (7*i*sqrt(7))) * (-7) = pi/sqrt(7)

print('DONE; all exact assertions passed.')
