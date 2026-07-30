# Constant-time notes for HQH-539 T3 (engineering)

**Status:** engineering checklist — not a full side-channel proof.

## Goal
Avoid secret-dependent branches and table lookups on key material / intermediate state where feasible.

## Canonical T3 (reference)
```
r = n % 3
if r == 0: n//3
elif r == 1: (4n+2)//3
else: (2n+1)//3
```
Branching on `n % 3` is data-dependent. For hashing public messages this is typically acceptable; for keyed KDF/MAC paths under side-channel threat models, prefer arithmetic selection:

```
# illustrative arithmetic selection (pseudocode)
c0 = 1 if r==0 else 0
c1 = 1 if r==1 else 0
c2 = 1 if r==2 else 0
# better: constant-time equality masks from r
out = c0*(n//3) + c1*((4*n+2)//3) + c2*((2*n+1)//3)
```
Still requires constant-time division / modular reduction on big integers — platform-dependent (Python integers are not constant-time).

## Production guidance
1. Python reference: clarity + KATs; not a CT guarantee.
2. RTL / C ports: fixed 539 iterations; arithmetic selection on residue; no early abort.
3. Side-channel claims require platform measurement (TVLA etc.) — pending.

## Framing
Constant-time work is Category A engineering when it only uses standard practices; it does not complete a security reduction for HQH-539 hardness.
