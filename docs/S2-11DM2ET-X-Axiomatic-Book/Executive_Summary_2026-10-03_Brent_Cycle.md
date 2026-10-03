# Executive Summary: Brent cycle detection, 2026-10-03

Finds cycle length lambda and start index mu of a functional sequence. Power-of-two blocks. Cost on the order of mu + lambda. Floyd is the same order with more evaluations.

On the Pollard walk, modulo 7 the cycle is length 1, modulo 11 length 2. That is why the gcd test works. No new factor.

Full note: artifacts/Brent_Cycle_Detection_2026-10-03.md
