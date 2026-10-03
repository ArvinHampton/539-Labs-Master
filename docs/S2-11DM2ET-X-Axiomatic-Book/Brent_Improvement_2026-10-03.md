# Brent's improvement of Pollard rho

Date: 2026-10-03
Status: method note. Same factors. Not a bridge.
CORE_FREEZE unchanged. No new residual-flux object.

Floyd advances a hare twice as fast as a tortoise and tests every step. Brent keeps one value fixed for a block of length a power of two, advances the other through the block, and accumulates the product of the gaps. The gcd is taken on the product, not on every gap. A failed block doubles the length.

The walk is the same polynomial x^2 + c. Only the cycle test changes. The expected saving against Floyd is about a quarter of the function evaluations. It does not change the factors.

On c = 1 and seed 2: 539 returns 7 in 6 steps, cofactor 77. 4880 returns 8 in 2 steps, cofactor 610. 247 returns 13 in 6 steps, cofactor 19. These are the known splits. Brent does not insert 13 into 539 or 4880.
