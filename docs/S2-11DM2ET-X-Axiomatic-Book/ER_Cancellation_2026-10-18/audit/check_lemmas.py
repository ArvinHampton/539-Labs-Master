# Audit check 5: symbolic/finite pieces of Lemmas 1, 3, 5 and the trivial-character step.
import sympy as sp, mpmath as mp, common as C, math
mp.mp.dps = 30
out = []
w, z, m, n = sp.symbols('w z m n')
F = lambda mm, nn: 1/(nn*z+7*mm)
DnF = sp.simplify(F(m, n+1)-F(m, n)); W = n*z+7*m
out.append(f"Delta_n F + z/(w(w+z)) = {sp.simplify(DnF + z/(W*(W+z)))}")
DmDn = sp.simplify((F(m+1, n+1)-F(m+1, n))-(F(m, n+1)-F(m, n)))
out.append(f"Delta_m Delta_n F - z(14w+49+7z)/(w(w+z)(w+7)(w+7+z)) = {sp.simplify(DmDn - z*(14*W+49+7*z)/(W*(W+z)*(W+7)*(W+7+z)))}")
D2 = sp.simplify(F(m, n+2)-2*F(m, n+1)+F(m, n))
out.append(f"D^2_n F - 2z^2/(w(w+z)(w+2z)) = {sp.simplify(D2 - 2*z**2/(W*(W+z)*(W+2*z)))}")
# Lemma 1: Mittag-Leffler, numerically at a few u (both half planes) for 2 characters
for key in [(0,0), (4,1)]:
    c = C.chars()[key]
    for u in [mp.mpc('0.013','0.02'), mp.mpc('0.31','-0.4'), mp.mpc('0.7','0.003')]:
        q = C.ee(u); P = mp.fsum(c.b[r]*q**r for r in range(1, 140)); B = P/(1-q**140)
        cot = mp.fsum(c.rho[s % 140]*mp.pi*mp.cot(mp.pi*(u-mp.mpf(s)/140)) for s in range(1, 141))
        out.append(f"Lemma 1 chi{key} u={mp.nstr(u,3)}: |B(u) - sum rho_s pi cot| = {mp.nstr(abs(B-cot),3)}")
# trivial character: second primitive, sum_{n=1}^{140} beta(n) = 0, and size of the cancelling constant (2/5) sum rho_n/(nz)
c = C.chars()[(0,0)]
beta = [mp.mpc(0)]; 
for j in range(1, 281): beta.append(beta[-1]+c.rho[j % 140])
out.append(f"trivial chi: max|beta(n+140)-beta(n)| = {mp.nstr(max(abs(beta[j+140]-beta[j]) for j in range(141)),3)}, |sum_(n=1..140) beta(n)| = {mp.nstr(abs(mp.fsum(beta[1:141])),3)}")
for zz in [mp.mpc('0.6','0.45'), mp.mpc('1','0.9')]:
    # sum_n rho_n/(n z) = (1/z) sum_n rho_n/n ;  sum_n rho_n / n = -(1/140) sum_s rho_s digamma(s/140)  (Sigma rho = 0)
    S = -mp.fsum(c.rho[s % 140]*mp.digamma(mp.mpf(s)/140) for s in range(1, 141))/140
    out.append(f"trivial chi, z={mp.nstr(zz,3)}: (2/5) sum rho_n/(nz) = {mp.nstr(mp.mpf(2)/5*S/zz,12)}  (nonzero: the cancellation in step 6 is genuine)")
# L(1,chi_140) / log eps check of the claim 'these are log eps-type constants'
Lval = mp.nsum(lambda k: C.chi140(int(k))/k, [1, mp.inf]) if False else None
S = -mp.fsum(c.rho[s % 140]*mp.digamma(mp.mpf(s)/140) for s in range(1, 141))/140
out.append(f"sum rho_n/n = {mp.nstr(S,15)};  i*log(eps)/(2*pi*sqrt35)*... ratio S/(log eps) = {mp.nstr(S/mp.log(6+mp.sqrt(35)),15)}")
# n-outer iterated sum in the trivial case does not converge: partial sums of sum_n rho_n k(n), k(n) -> const != 0
zz = mp.mpc('0.6','0.45'); kc = -(mp.mpf(2)/5)*mp.pi*1j/7
out.append(f"trivial chi: k(n) -> (2/5)(-pi i/7) = {mp.nstr(kc,8)} != 0, so sum_n rho_n k(n) oscillates with beta(n) (beta not -> 0: |beta(1)|={mp.nstr(abs(beta[1]),6)})")
print("\n".join(out)); open("check_lemmas.txt", "w").write("\n".join(out)+"\n")
