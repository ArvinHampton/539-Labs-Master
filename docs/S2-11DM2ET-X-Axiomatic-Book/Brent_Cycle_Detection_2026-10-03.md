# Brent cycle detection

Date: 2026-10-03
Status: algorithm note. Not a new factor.
CORE_FREEZE unchanged. No new residual-flux object.

The input is a function f and a seed x0. The sequence is x, f(x), f(f(x)), and so on. Brent finds the cycle length lambda and the index mu where the cycle starts.

Search. Keep a power of two. Hold one value fixed and advance the other until the block length equals that power. If the two values meet, the block contains a cycle and lambda is the number of steps since the value was fixed. If they do not meet, double the power and repeat.

Start index. Advance a second copy by lambda steps, then advance both until they meet. The number of steps is mu.

Cost is on the order of mu + lambda function evaluations, and a few stored values. Floyd uses the same order and more evaluations, because the hare steps twice and the test is every step.

On the Pollard walk x^2 + 1, modulo 7 from seed 2 the cycle starts at index 1 and has length 1. Modulo 11 it starts at index 2 and has length 2. Those cycles are why the gcd test in the factoring use succeeds. They do not add a factor.
