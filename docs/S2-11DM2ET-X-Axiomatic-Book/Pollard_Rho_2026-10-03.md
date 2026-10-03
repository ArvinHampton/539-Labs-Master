# Pollard rho

Date: 2026-10-03
Status: method note. No new factor. Not a bridge.
CORE_FREEZE unchanged. No new residual-flux object.

Pollard rho factors a composite n by a pseudorandom walk modulo n. Fix f(x) = x^2 + c, usually c = 1, and a seed x_0. The sequence is x_{i+1} = f(x_i) mod n.

Floyd's cycle test keeps a tortoise at x_i and a hare at x_{2i}. At each step compute d = gcd(|x_i - x_{2i}|, n). If d is strictly between 1 and n, it is a factor. If d = n, the walk failed and c or the seed is changed.

The walk modulo a hidden prime factor p is periodic. A collision modulo p, but not modulo n, is what the gcd detects. The expected number of steps is on the order of the square root of the smallest prime factor.

On the written list the smallest prime factors are already known by trial division. Rho reprints 7^2 * 11 for 539 and 2^4 * 5 * 61 for 4880. It does not insert 13.
