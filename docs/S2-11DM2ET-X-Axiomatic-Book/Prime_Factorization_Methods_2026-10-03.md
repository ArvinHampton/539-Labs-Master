# Prime factorization methods

Date: 2026-10-03
Status: methods note. No new factors. Not a bridge.
CORE_FREEZE unchanged. No new residual-flux object.

## What was used

Trial division. For a prime p and an integer n, count how many times p divides n by repeated division. That is the valuation. It is exact on the written list, whose largest entry is 4880 * 539 = 2,630,320. Every factor reported for 7, 11, 13, and 19 came from this.

A complete factorization of the same list is the same work continued over all primes up to the square root. 539 = 7^2 * 11 and 4880 = 2^4 * 5 * 61 are complete. No missing small factor is hiding in them.

## Methods that do not change this list

Pollard rho and the elliptic-curve method factor larger composites by finding a collision or a smooth relation. The quadratic sieve and the number-field sieve do the same for cryptographic sizes. The written integers are below the range where those methods differ from trial division. Using them would reprint the same factors.

Fermat factorization looks for a representation n = a^2 - b^2. It is fast only near a square. 539 and 4880 are not near squares in a way that adds a factor. 539 is 23^2 + 10, not a difference that changes the known split.

## Not a bridge

A method is not a new integer. Factoring 539 again does not produce 13. The protofilament count stays outside the packaging set.
