# Local-derived. Quick independent checks for the PP edcd9551 fixes (exact unless stated).
import cypari2; pari = cypari2.Pari(); pari.allocatemem(2*10**9)
E = pari.ellinit([1,-1,0,-2,-1]); a = [int(x) for x in pari.ellan(E, 40)]; A = lambda n: a[n-1]
print("49a1 a1..a20:", a[:20])
f2 = lambda n: A(n//2) if n % 2 == 0 else 0
liftS3 = [0,-2,0,-2,0,0,0,2,0,0,0,0,0,0,0,6,0,6,0,0]      # PP pp_3b3.log, j=1, t=3, own formula
liftS5 = [1,2,0,0,0,0,0,-4,-3,0,4,0,0,0,0,-4,0,-6,0,0]     # PP pp_3b3.log, j=1, t=5, own formula
print("Fix8: S3(K1) == -2 f(2tau) (n<=20):", liftS3 == [-2*f2(n) for n in range(1,21)])
print("Fix8: S5(K1) == f + f(2tau) (n<=20):", liftS5 == [A(n)+f2(n) for n in range(1,21)])
S = pari('[0,-1;1,0]'); T = pari('[1,1;0,1]')
print("Fix4: S*T*S^-1 =", S*T*S**-1, " S^-1*T*S =", S**-1*T*S, " S^-1*T^-1*S =", S**-1*T**-1*S)
print("Fix5: 49*20^2 =", 49*400, "; 49*140^2 =", 49*140**2, "; lcm(49,140^2) =", pari.lcm(49,140**2))
print("Fix6: 19600 divides 980?", 980 % 19600 == 0)
ok = all(int(pari.kronecker(140,n)) == int(pari.kronecker(-20,n))*int(pari.kronecker(-7,n)) for n in range(1,141))
print("Fix (E10 support): chi140 == chi_-20 * chi_-7 on n=1..140:", ok)
print("Fix12 (N2): twists 49a1 x chi_D with eps=+1, L~0 in part3_check2:")
for D in [40,44,53,57,172,188,248,264,316]:
    Et = pari.ellinit(pari.elltwist(E, D)); r = pari.ellrank(Et)
    print(f"  D={D}: cond {pari.ellglobalred(Et)[0]}, rootno {pari.ellrootno(Et)}, ellrank bounds [{r[0]},{r[1]}]")
print("Fix13: n=7: coredisc(-7) =", pari.coredisc(-7), "; f x chi_-7 = f (CM), L(49a1,1) =", pari.lfun(E,1), "(float, nonzero) while c(7)=0 on K per part3_check2 row 7")
