# Collision analysis: residue-1 \(4q+2\) and Canonical \(T\)

**Status:** Structural / engineering analysis (2026-08-01)  
**Scope:** The Canonical r1 branch \(n=3q+1\mapsto 4q+2\), full one-step \(T\), iterates \(T^k\), and implications for HQH-539  
**Not:** A proof that HQH-539 is collision-resistant  

**Hardness language (hash layer):** computationally infeasible with known classical/quantum methods, pending peer review of a full reduction.

Results file: `collision_4q2_analysis_results.json`  
Probe: analysis script embedded in git history / re-run notes below.

---

## 1. Executive answer

| Object | Collision-resistant? | Why |
|--------|----------------------|-----|
| Map on \(q\): \(q\mapsto 4q+2\) | **Yes (trivially)** | Injective on \(\mathbb{N}\). Wrong security interface. |
| One-step Canonical \(T\) | **No** | Explicit infinite collision families (below). |
| \(T^k\) for any \(k\ge 1\) | **No** as a free function on \(\mathbb{Z}\) | 1-step collisions **lift** to all further iterates. |
| Bare \(T^{539}\) on free wide seeds | **Very weak** | Strong contraction → small image; many seeds share state. |
| Full HQH-539 (SHA3 → \(T^{539}\) → SHA3) | **Not broken by this analysis** | Message collisions need seed control through SHA3; bare \(T\)-collisions do not freely become message collisions. |

**Bottom line:** \(4q+2\) does **not** supply collision resistance. It also does **not** introduce same-branch (r1–r1) collisions. CR of HQH, if any, must come from the **SHA3 seed/finalize sandwich**, not from injectivity of \(4q+2\).

---

## 2. The \(4q+2\) branch alone

\[
n = 3q+1 \quad\Rightarrow\quad T(n) = 4q+2 = \frac{4n+2}{3}.
\]

- **Injective in \(q\):** \(4q+2 = 4q'+2 \Rightarrow q=q'\).  
- **Census:** over \(x \in [0,10^5)\), number of **r1–r1** colliding pairs under \(T\) is **0**.  
- **vs T4121:** \(4q+1\) is likewise injective in \(q\); both avoid r1–r1 collisions.

So “collision resistance of \(4q+2\)” in the sense of “two different residue-1 inputs, same output” is **vacuously true** and **cryptographically irrelevant**: the dangerous collisions for \(T\) are **cross-branch**.

---

## 3. Constructive collisions for full \(T\) (Canonical)

### Family A — r0 with r1 (uses \(4q+2\) as the **common image**)

\[
T\bigl(3(4q+2)\bigr) = 4q+2 = T(3q+1).
\]

| \(q\) | \(x_{\mathrm{r0}} = 3(4q+2)\) | \(x_{\mathrm{r1}} = 3q+1\) | \(T\) |
|------|-------------------------------|----------------------------|-------|
| 0 | 6 | 1 | 2 |
| 1 | 18 | 4 | 6 |
| 2 | 30 | 7 | 10 |

Every \(q \ge 0\) gives a collision pair. The r1 side is exactly the \(4q+2\) branch; the collision is with the **multiply-by-3** (r0) branch, not a failure of injectivity of \(4q+2\).

### Family B — r0 with r2

\[
T\bigl(3(2q+1)\bigr) = 2q+1 = T(3q+2).
\]

### Family C — r1 with r2

\[
4q+2 = 2q'+1
\]
even = odd → **impossible**. So \(4q+2\) **never** collides with the r2 branch in one step.

### Lift

If \(T(a)=T(b)\), then \(T^k(a)=T^k(b)\) for all \(k \ge 1\).  
One-step collisions are **permanent** under iteration.

---

## 4. Finite-domain collision census

On \([0, 10^5)\):

| Residue pair type | Collision pairs (unordered) |
|-------------------|----------------------------|
| (0,1) | 8333 |
| (0,2) | 16667 |
| (1,1) | **0** |
| (1,2) | **0** |

Mean preimage size ~ order 1–2; max preimage size 2 on that sample.  
Formal one-step preimage branching mean ≈ 1.75 (prior residue note).

### vs T4121 (domain \([0,5\cdot 10^4)\))

| | Outputs | Multi-preimage outs | Unordered pairs |
|--|---------|---------------------|-----------------|
| Canonical | 37500 | 12500 | 12500 |
| T4121 | 33334 | 12499 | 20833 |

Same order of multi-collisions; T4121 shows **more** unordered pairs on this segment (different image packing), not a CR win for either.

---

## 5. Iterates and contraction (why bare \(T^{539}\) fails CR)

Asymptotic bit change per step \(\approx -0.585\) bits → 539 steps erase hundreds of bits from a 512-bit seed (typical end width ~150–230 bits, often smaller in short trials).

**Consequence:** as a map on free integers of large bit-width, \(T^{539}\) is an extreme **compressor**. Birthday / multi-collision on the state becomes easy if the adversary chooses seeds freely:

- Truncated-tag sampling at \(k=539\) shows collision counts **far above** the ideal \(n^2/2^{t}\) model when tags are short — consistent with a **small effective image**, not with ideal random \(T^{539}\).
- At small \(k\) with wide free inputs, truncated birthdays track the ideal model more closely.

This is a property of the **iterated ternary map**, not a special bug in \(+2\) vs \(+1\).

---

## 6. HQH-539 shell (message → digest)

\[
\mathrm{seed} = \mathrm{SHA3\text{-}512}(m \parallel \mathrm{salt}),\quad
s = T^{539}(\mathrm{seed}),\quad
\mathrm{digest} = \mathrm{SHA3\text{-}512}(\mathrm{encode}(s)\parallel\mathrm{salt}).
\]

### What a collision needs

A message collision \(m \neq m'\) with same digest requires either:

1. **SHA3 seed collision** (then whole pipeline matches), or  
2. Seeds \(s_0 \neq s_0'\) with \(T^{539}(s_0)=T^{539}(s_0')\) **and** identical finalize encoding, with \(s_0,s_0'\) both in the image of SHA3 under the salt, or  
3. Distinct fingerprints that **collide in the outer SHA3** finalize.

Constructive \(T\)-pairs such as \((6,1)\) are **not** SHA3-512 outputs under a normal message API without inverting SHA3. So Family A/B are **not** automatic HQH message collisions.

### Toy shell sampling

Truncated 32-bit HQH digests, 3000 sequential messages: **0** collisions (as expected for \(n \ll 2^{16}\)).  
Does **not** prove 256-bit CR.

---

## 7. Role of \(4q+2\) specifically

| Question | Answer |
|----------|--------|
| Does \(4q+2\) cause r1–r1 collisions? | **No** (injective). |
| Does it participate in collisions? | **Yes** — as the **shared image** of Family A with r0. |
| Would \(4q+1\) avoid Family A? | No — T4121 has the same r0/r1 joining pattern with image \(4q+1\). |
| Does switching \(+2\) vs \(+1\) restore CR of \(T\)? | **No.** |
| Does injectivity of \(4q+2\) make HQH CR? | **No.** |

Design takeaway: residue-1 exactness and cycle hygiene (no fixed point at 1) are **algebraic hygiene**, not a CR proof ingredient by themselves.

---

## 8. Heuristic bounds (informal)

| Layer | Naive scale | Caveat |
|-------|-------------|--------|
| Output digest birthday | \(2^{256}\) queries | Classical; assumes ideal random digest |
| Free-seed state birthday after 539 | \(\ll 2^{98}\) if ~196-bit state were uniform | State is **not** uniform; contraction + structure; free seeds ≠ API |
| Message API | Must pass SHA3 preimage/collision | Main barrier against lifting \(T\)-collisions |

No attack here lowers the full 512-bit digest birthday under a standard model of SHA3.

---

## 9. Conclusions

1. **\(4q+2\) is injective** — zero same-branch collisions; good local algebra, not CR.  
2. **Canonical \(T\) is not CR** — infinite constructive families; collisions lift under iteration.  
3. **Bare \(T^{539}\) is a poor free-standing CR primitive** — contraction collapses free seeds.  
4. **HQH-539 CR is a sandwich property** — seed SHA3 + map + finalize SHA3; structural \(T\)-collisions do not freely become message collisions.  
5. **Option A remains justified on algebra/RTL grounds**; this note does **not** promote \(4q+2\) as a CR source and does **not** demote it relative to T4121 on CR (both fail bare CR similarly).

---

## 10. Non-claims

- No proof of collision resistance for HQH-539  
- No claim of insecurity of HQH-539 from Family A/B  
- No quantum analysis  
- No reduction to SHA3-CR alone without a formal game

---

## 11. Reproduce

```bash
# regenerates collision_4q2_analysis_results.json (from engine tree)
python3 - <<'PY'
# see commit / re-run analysis block in history, or:
from pathlib import Path
import json
print(Path('collision_4q2_analysis_results.json').read_text()[:500])
PY
```

*Per aspera ad astra.*
