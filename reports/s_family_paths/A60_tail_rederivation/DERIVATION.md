# A60 DERIVATION: the tail step for g_k(q) = sum_n q^{n^2}/(-q^k;q^k)_n, odd k, from first principles

Written before any A60 code (see `prereg.md`, `FREEZE_time.txt`). Category A. Notation: k odd, N1 = 1500, n0 = N1 - k, eta_t = 1e-6, y = sqrt(d).
Only the statements of A56/A57 were used as input (what must be delivered); every lemma below is proved here with explicit constants.

## 1. Product formula, E-O identity

phi_n(m) = [x^m] prod_{i<=n} 1/(1+x^i), and g_k(d) = sum_{n^2<=d, k | d-n^2} phi_n((d-n^2)/k). Put a_n(m) = (-1)^m phi_n(m) = [x^m] A_n(x), A_n(x) = prod_{j<=n} 1/(1+(-x)^j).
For odd j: 1+(-x)^j = 1-x^j and 1/(1-x^j) = (1+x^j)/(1-x^{2j}). For even j: 1/(1+x^j) = (1-x^j)/(1-x^{2j}).
Multiplying over j <= n, the numerators (1-x^{2i}) coming from even j = 2i (i <= floor(n/2)) cancel the denominators (1-x^{2l}) with l <= floor(n/2) (the denominators are (1-x^{2j}), j <= n):

  A_n(x) = prod_{j odd <= n} (1+x^j) * prod_{floor(n/2) < l <= n} (1-x^{2l})^{-1}.            (1.1)

All factors have nonnegative coefficients, so a_n(m) >= 0. For odd k and d = n^2 + k m: (-1)^d = (-1)^{n+m} (k odd, n^2 = n mod 2), hence
(-1)^d g_k(d) = sum_n (-1)^{n+m_n} phi_n(m_n) = sum_n (-1)^n a_n(m_n) = E_d - O_d, E_d (O_d) the sum over even (odd) n of a_n(m_n) >= 0.         (1.2)
(Since a_n(m) = (-1)^m phi_n(m), the term (-1)^d phi_n(m) = (-1)^{n+m} phi_n(m) equals (-1)^n a_n(m). Verified numerically in J6.)
Consequently E_d < O_d implies (-1)^d g_k(d) < 0 and g_k(d) != 0. Parity Dominance needs E_d <= (1-eta) O_d: E_d = (block part) + (tail part); the block part is <= R O_d (block step, not re-derived here), and the tail part is shown below to be <= eta_t O_d, so eta = 1 - R - eta_t.

## 2. Probabilistic model and the mean/variance functions

(1.1) is a product of independent factors: for r in (0,1), a_n(m) r^m / A_n(r) = P(S = m) with S = sum_{j odd <= n} j B_j + sum_{floor(n/2) < l <= n} 2 l N_l, B_j ~ Bernoulli(r^j/(1+r^j)), N_l geometric with ratio w_l = r^{2l}. Tilt r = e^{-u/n}.
 mu_n(u) = sum_{j odd<=n} j/(e^{ju/n}+1) + sum_l 2l/(e^{2lu/n}-1),  sigma_n^2(u) = sum_{j odd} j^2 e^{ju/n}/(e^{ju/n}+1)^2 + sum_l (2l)^2 e^{2lu/n}/(e^{2lu/n}-1)^2.
 With M_n = mu_n/n^2, S_n = sigma_n^2/n^3 these are Riemann sums:
 M_n = (1/n) sum_{j odd} p(j/n) + (1/n) sum_l q(l/n),  p(x) = x/(e^{ux}+1), q(x) = 2x/(e^{2ux}-1);
 S_n = (1/n) sum_{j odd} r(j/n) + (1/n) sum_l s(l/n),  r(x) = x^2 e^{ux}/(e^{ux}+1)^2, s(x) = x^2/sinh^2(ux).
 Limits: M(u) = (1/2) int_0^1 p + int_{1/2}^1 q, S(u) = (1/2) int_0^1 r + int_{1/2}^1 s.

## 3. Chernoff upper bound for even n (no additive constants)

Since a_n(m) >= 0 and a_n(m) r^m <= A_n(r): a_n(m) <= A_n(r) r^{-m}, r = e^{-u/n}, any u > 0.
log A_n(r) = P + Q, P = sum_{j odd<=n} f(j), f(x) = log(1+e^{-ux/n}), Q = sum_{l=n/2+1}^{n} h(l) (n even), h(x) = -log(1-e^{-2ux/n}).
 * f is convex and decreasing, so by Hermite-Hadamard 2 f(j) <= int_{j-1}^{j+1} f; for even n the intervals [j-1,j+1], j odd <= n-1, tile [0,n]: 2P <= int_0^n f.
 * h is decreasing: h(l) <= int_{l-1}^{l} h, so Q <= int_{n/2}^{n} h.
 Substituting x = n t and using int_0^u log(1+e^{-s}) ds = Li2(-e^{-u}) + pi^2/12 (since d/ds Li2(-e^{-s}) = log(1+e^{-s}), Li2(-1) = -pi^2/12) and
 int_u^{2u} -log(1-e^{-s}) ds = Li2(e^{-u}) - Li2(e^{-2u}):

   log A_n(e^{-u/n}) <= n Phi1(u),   Phi1(u) = [Li2(-e^{-u}) + pi^2/12 + Li2(e^{-u}) - Li2(e^{-2u})] / (2u),   n even.        (3.1)

With alpha = n/sqrt(d), m = (d-n^2)/k = n^2 rho(alpha), rho(alpha) = (1/alpha^2 - 1)/k, we get u m/n = sqrt(d) u (1-alpha^2)/(k alpha) and

   e_n := a_n(m_n) <= exp( sqrt(d) F(alpha,u) ),   F(alpha,u) = alpha Phi1(u) + (1-alpha^2) u/(k alpha),   every even n >= 2, every u > 0.       (3.2)

(3.1) is slightly sharper than the "+log 2 + g(u)" form: for even n the convexity/monotonicity bounds already give the integral with no remainder. (Checked against exact a_n(m) in J2.)

### Convexity of F in alpha (rigorous)
For fixed u > 0: F(alpha,u) = alpha (Phi1(u) - u/k) + (u/k)/alpha. The first term is linear in alpha, and (u/k)/alpha has second derivative 2u/(k alpha^3) > 0 on alpha > 0. Hence d^2F/d alpha^2 = 2u/(k alpha^3) > 0, F is strictly convex, and for any interval [a,b] with 0 < a < b:

   sup_{alpha in [a,b]} F(alpha,u) = max( F(a,u), F(b,u) )   (exactly, by convexity: F lies below its chord).                          (3.3)

So endpoint evaluation gives the exact supremum of the Chernoff exponent over the piece for the fixed u, with NO loss from the width of the piece. (A ball evaluation of F over the whole alpha-interval loses ~ width * (|Phi1 - u/k| + u/(k a^2)), because alpha occurs in three places: this is the ball-arithmetic artefact tested in J5.)

### Tiny alpha (alpha <= alpha_t = 0.005): analytic bound, u = c alpha, c = 3/2
2u Phi1(u) = int_0^u log(1+e^{-s})ds + int_u^{2u} -log(1-e^{-s}) ds <= u log 2 + int_u^{2u} (-ln s + s/2) ds, using 1-e^{-s} >= s e^{-s/2} (2 sinh(s/2) >= s). Hence
 Phi1(u) <= (1/2)(1 - ln 2 - ln u + (3/4) u).                                                                                          (3.4)
F(alpha, c alpha) = alpha Phi1(c alpha) + (1-alpha^2) c/k <= B(alpha) + c/k, B(alpha) = (1/2) alpha (1 - ln 2 - ln(c alpha) + (3/4) c alpha).
B'(alpha) = (1/2)(-ln(2 c alpha) + (3/2) c alpha) > 0 when 2 c alpha < 1, so B is increasing on (0, alpha_t] and F <= B(alpha_t) + c/k there. (c/k = 0.048 for k = 31; B(0.005) = 0.0138.)

## 4. Lower bound on one odd term; local CLT enters here only

For odd n, P = sum_{j odd <= n} f(j): f decreasing, so 2 f(j) >= int_j^{j+2} f and 2P >= int_1^{n+2} f >= int_0^n f - int_0^1 f >= int_0^n f - log 2. So P >= (1/2) int_0^n f - (1/2) log 2.
Q = sum_{l=(n+1)/2}^{n} h(l) >= int_{(n+1)/2}^{n+1} h >= int_{n/2}^{n} h - int_{n/2}^{(n+1)/2} h >= int_{n/2}^n h - (1/2) h(n/2), and h(n/2) = g(u) := -log(1-e^{-u}). Therefore

   log A_n(e^{-u/n}) >= n Phi1(u) - (1/2) log 2 - (1/2) g(u),   n odd.                                                           (4.1)

Local CLT (hypothesis H_CLT, supplied by the local-CLT layer, not proved here): P(S = m) >= (exp(-x^2/(2 sigma^2)) - delta_H) / (sqrt(2 pi) sigma), x = m - mu, at tilt u*, n >= n0.
Then for odd n and m: a_n(m) = A_n(r) r^{-m} P(S=m), so

   log a_n(m) >= sqrt(d) F(beta,u*) - (1/2) log 2 - (1/2) g(u*) + log( exp(-x^2/(2 sigma^2)) - delta_H ) - log( sqrt(2 pi) sigma ),   beta = n/sqrt(d).          (4.2)

### Saddle point and choice of the odd term
(alpha*, u*) is the point where both partials of F vanish: F_u = -alpha M(u) + (1-alpha^2)/(k alpha) = 0 (because Phi1' = -M, i.e. d/du log A_n(e^{-u/n}) = -mu/n) and F_alpha = Phi1(u) - u/(k alpha^2) - u/k = 0. Define F* = F(alpha*,u*) (I use rational approximations of (alpha*,u*), F* is then the exact value of F at these rationals and the residuals |F_alpha|, |rho(alpha*) - M(u*)| are enclosed and used below).
For allowed d there is n_0' with n_0'^2 = d mod k; odd n with n = +-n_0' mod k form a progression of difference 2k, so there is an odd n_c in [alpha* y - k, alpha* y + k] with k | d - n_c^2 and m_c = (d-n_c^2)/k >= 0 (n_c < y). Put beta = n_c/y, |beta - alpha*| <= k/y.
 * Convexity (3.3 / tangent): F(beta,u*) >= F* + F_alpha(alpha*,u*)(beta - alpha*), so y F(beta,u*) >= y F* - k |F_alpha(alpha*,u*)|.
 * x = m_c - mu_{n_c}(u*) = n^2 (rho(beta) - rho(alpha*)) + n^2 (rho(alpha*) - M(u*)) + n^2 (M(u*) - M_n(u*)). With |rho'| = 2/(k alpha^3), |rho(beta) - rho(alpha*)| <= 2 (k/y)/(k (alpha* - k/y)^3) and |M - M_n| <= (a_M/n + b_M/n^2) (section 5):
   |x| <= X(y) := (alpha* y + k)^2 [ 2 y^2/(alpha* y - k)^3 + res_rho ] + a_M (alpha* y + k) + b_M, res_rho = |rho(alpha*) - M(u*)|.
 * sigma^2 = S_n n^3 with S_n in [S_lo, S_hi] (section 5), n in [alpha* y - k, alpha* y + k]: sigma_min^2 = S_lo (alpha* y - k)^3, sigma_max^2 = S_hi (alpha* y + k)^3.
 * kappa(y) = X(y)/sigma_min(y). Both X/sigma_min pieces decrease in y for alpha* y > k (log-derivatives 2/y+2 alpha*/(alpha* y+k)-4.5 alpha*/(alpha* y-k) < 0 and 1/(z+k) - 1.5/(z-k) < 0, z = alpha* y), so kappa decreases.
Thus for every d >= D with y = sqrt(D):
   log o_c >= y F* - C_o(y),  C_o(y) = k|F_alpha| + (1/2) log 2 + (1/2) g(u*) + log sqrt(2 pi) + log sigma_max(y) - log( exp(-kappa(y)^2/2) - delta_H ).        (4.3)
Every odd term is <= O_d, so O_d >= o_c.

## 5. Riemann-sum lemma with explicit constants (midpoint rule), all n >= n0

Let f in {p, r} (odd type, f >= 0, on [0, 1+1/n0]) with kappa_f = sup |f''|, and g in {q, s} (decreasing, on [1/2, 1+1/(2 n0)]) with kappa_g = sup |g''|. O_n(f) = (1/n) sum_{j odd<=n} f(j/n), G_n(g) = (1/n) sum_{l=floor(n/2)+1}^{n} g(l/n).
Cells [(j-1)/n, (j+1)/n] (j odd) tile [0, (J+1)/n], J = largest odd <= n, (J+1)/n = 1 (n even) or 1 + 1/n (n odd). Midpoint rule on a cell of width h: |h f(mid) - int| <= h^3 kappa/24. There are <= (n+1)/2 cells, h = 2/n:
  (1/2) int_0^1 f - kappa_f (1+1/n)/(12 n^2) <= O_n(f) <= (1/2) int_0^1 f + max_{[1,1+1/n0]} f /(2n) + kappa_f (1+1/n)/(12 n^2).
Cells [(l-1/2)/n, (l+1/2)/n], l = floor(n/2)+1..n tile [(a+1/2)/n, (n+1/2)/n], a = floor(n/2): (a+1/2)/n = 1/2 (n odd) or 1/2 + 1/(2n) (n even). With g decreasing:
  int g - (g(1/2) - g(1+1/(2 n0)))/(2n) - (n+1) kappa_g/(48 n^3) <= G_n(g) <= int g + g(1)/(2n) + (n+1) kappa_g/(48 n^3).
All error terms are nonincreasing in n, so the n = n0 values give bounds valid for all n >= n0. Applied to (p,q) and (r,s):
  M(u) - A_lo/n - B/n^2 <= M_n(u) <= M(u) + A_hi/n + B/n^2, similarly S_lo/S_hi.
 M_lo := M(u) - A_lo/n0 - B/n0^2 (all n >= n0), M_hi := M(u) + A_hi/n0 + B/n0^2; a_M = max(A_lo, A_hi), b_M = B.
Closed forms (proved by differentiating): N(u) = 2u Phi1(u), N'(u) = -log(1-e^{-2u}); with L = log(1-e^{-2u}):
  M(u) = -Phi1'(u) = L/(2u) + N/(2u^2),   S(u) = -M'(u) = -1/(u (e^{2u}-1)) + L/u^2 + N/u^3   (since d mu/du = -Var/n).
Both are checked against interval quadrature of the four integrals and against exact finite sums (J2). f'' bounds by arb series (second Taylor coefficient over boxes).

## 6. D0 and the interface with the block step

The block step treats even n >= N1 whose saddle tilt u_n (mu_n(u_n) = m_n) lies in [UA, UB]. M_n(u) is decreasing in u (mu decreases with u). For even n, d: if alpha_n > alpha_1 := 1/sqrt(1+k M_lo(UA)) (any larger rational alpha_1' is also fine) then m_n/n^2 = rho(alpha_n) < rho(alpha_1) = M_lo(UA) <= M_n(UA) = mu_n(UA)/n^2, so mu_n(UA) > m_n and u_n > UA (n >= n0). Likewise alpha_n < alpha_2 := 1/sqrt(1+k M_hi(UB)) implies u_n < UB.
n = alpha sqrt(d) >= N1 for alpha > alpha_1 iff d >= D0 := ceil((N1/alpha_1)^2). So the TAIL is: even n with alpha <= alpha_1 (this contains all n < N1 when d >= D0) or alpha >= alpha_2 (up to alpha = 1 since m >= 0).

## 7. Tail inequality T(y)

Cover [alpha_t, alpha_1] and [alpha_2, 1] by pieces [a_i, b_i] with fixed u_i > 0 (adaptive: u_i = argmin_u F(mid_i, u) found in floating point, then fixed as an exact rational; endpoints exact rationals; consecutive pieces share endpoints). By (3.3) each piece has sup F = max(F(a_i,u_i),F(b_i,u_i)) (arb upper bound). Define
   F_tail := max over pieces of those maxima, and with the tiny part, max(F_tail, B(alpha_t) + c/k);  gamma := F_tail - F*  (< 0 required).
Number of even n <= y/2. By (3.2): tail sum <= (y/2) exp(y (F* + gamma)). With (4.3):

   T(y) := log(y/2) + y gamma + C_o(y) - log eta_t   =>   tail sum <= eta_t O_d  iff T <= 0 (sufficient).                              (7.1)

Monotonicity: T'(y) <= 1/y + gamma + 1.5 alpha*/(alpha* y + k) + (decreasing kappa term) <= gamma + 2.5/y, so T is decreasing for y >= 2.5/|gamma|; with T(sqrt(D0)) < 0 and gamma <= -2.5/sqrt(D0) the inequality holds for ALL d >= D0.
The three evaluation modes of J5 differ only in how max_{alpha in piece} F(alpha,u_i) is bounded: CONVEX (endpoints, exact by 3.3), BALL_COARSE (arb ball on the whole 0.0025 piece), BALL_FINE (arb balls on 0.0001 sub-pieces, u re-chosen per sub-piece).

## 8. Finite certificate and zero sets

For d < D0 (and d > max Z_k) the claim g_k(d) != 0 is by computation: G[d] = (-1)^d g_k(d) = sum_n (-1)^n a_n(m_n) via the signed recursion a_n[m] = a_{n-1}[m] - (-1)^n a_n[m-n] (from A_n = A_{n-1}/(1+(-x)^n): A_n (1+(-x)^n) = A_{n-1}) modulo primes p1, p2: a nonzero residue proves g_k(d) != 0 (an integer that is 0 has residue 0). Double zeros are verified exactly. Exact computation with Python integers up to d <= 300 000 gives Z_k; the q-series definition (phi recursion 1/(1+x^i)) gives an independent check of (1.2). The needed range is D_cert >= D0.
Statement delivered: for allowed d > max Z_k: d < D_cert -> certificate; d >= D0 -> PD (block R_k < 1 - eta_t, tail T(D0) < 0) => (-1)^d g_k(d) < 0.

## 9. Revision log (before freeze)
 - x-bound: the first draft of |rho(beta)-rho(alpha*)| carried a spurious factor 1/y (found by the hand estimate x ~ 2y/alpha*, which gives kappa ~ 0.9 at D0, against 0.009 from the draft). Corrected in text and code; the first run's outputs are kept in `out/superseded/`, `logs/superseded/` and were not used.
 - wording of section 1 (product formula) cleaned; no mathematical change.
