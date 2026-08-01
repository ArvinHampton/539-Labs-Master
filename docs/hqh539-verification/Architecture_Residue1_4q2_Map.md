# Residue-1 mapping: Canonical \(4q+2\)

**Status:** Cat A algebra + engineering notes (Option A primitive)  
**Map branch:** if \(n = 3q + 1\), then  
\[
T(n) = \frac{4n + 2}{3} = 4q + 2
\]  
exactly (integer division with no remainder).

Related: T4121 uses \(4q+1 = \lfloor(4n+1)/3\rfloor\) on the same inputs.

---

## 1. Exact identities

| Form | Expression |
|------|------------|
| In \(n\) | \(n \equiv 1 \pmod{3}\), \(n = 3q+1\) |
| Affine in \(n\) | \(T(n) = \frac{4}{3}n + \frac{2}{3}\) (exact in \(\mathbb{Q}\), lands in \(\mathbb{Z}\)) |
| Affine in \(q\) | \(T = 4q + 2\) |
| RTL (after `div3`) | `map = (q << 2) + 2` |
| Divisibility | \(4n+2 = 12q+6 = 3(4q+2)\) — **exact** |
| T4121 contrast | \(4n+1 = 12q+5\) — **not** divisible by 3; floor yields \(4q+1\) |

**Corollary:** On every residue-1 input,
\[
T_{\mathrm{Canonical}}(n) = T_{\mathrm{T4121}}(n) + 1.
\]
The two maps never agree on residue-1; they always differ by exactly one.

---

## 2. Image structure

- \(4q+2 \equiv 2 \pmod{4}\) always → output is **even** and **2 mod 4** (binary `…10`).
- Residue of the image mod 3 is **balanced** across \(\{0,1,2\}\) as \(q\) runs (since \(4q+2 \equiv q+2 \pmod{3}\)).
- As a map on \(q \in \mathbb{N}\): \(q \mapsto 4q+2\) is **injective**, not surjective (misses all odds and all \(0 \bmod 4\)).

### One-step inverse (residue-1 branch only)

\(y\) has a residue-1 Canonical preimage iff \(y \ge 2\) and \(y \equiv 2 \pmod{4}\):

\[
q = \frac{y-2}{4},\qquad n = 3q+1.
\]

---

## 3. Full \(T\) preimage portrait (Canonical)

Combining all three branches, formal preimages of \(y\) are among:

| Branch | Candidate \(x\) | Condition |
|--------|-----------------|-----------|
| \(r=0\) | \(x = 3y\) | always a candidate; verify \(x/3 = y\) |
| \(r=1\) | \(x = 3\frac{y-2}{4}+1\) | \(y \equiv 2 \pmod{4}\) |
| \(r=2\) | \(x = 3\frac{y-1}{2}+2\) | \(y\) odd |

Empirically (and by the formulas), typical preimage counts are **1 or 2** (mean formal branching ≈ **1.75** on a large sample). This is a **non-bijective**, mildly expanding cover map — same qualitative class as many Collatz-like ternary maps.

---

## 4. Dynamics notes

| Object | Canonical | T4121 |
|--------|-----------|-------|
| Fixed points (small search) | \(\{0\}\) | \(\{0,1\}\) |
| 2-cycle | \(1 \leftrightarrow 2\) | none small (1 fixed) |
| Growth on r1 | \(\sim 4/3\) | \(\sim 4/3\) (same leading term) |
| Global contraction (mixed residues) | \(\mathbb{E}[\Delta\mathrm{bits}] \approx -0.585\)/step | same asymptotics |

**Cycle \(1 \to 2 \to 1\):**  
\(T(1)=4\cdot0+2=2\), \(T(2)=(4+1)/3=1\).  
T4121 instead fixes \(1\) (\(4\cdot0+1=1\)), a structural defect avoided by Canonical.

Residue-1 hit rate along long trajectories stays near \(\sim 1/3\) under mixing (exact rate depends on the residue transition kernel). Empirical transition kernels for Canonical send r1 mass into all three residue classes roughly evenly via \(q+2 \bmod 3\).

---

## 5. Bit / hardware view

```text
q = n // 3
r = n %  3
if r == 1:
    y = (q << 2) + 2    // 4q+2, sets low pattern *10
```

- No floor-error path; synthesizable as shift-add.
- Differs from T4121 only in the final `+2` vs `\| 1` (`+1`).
- Local Hamming sensitivity along the r1 branch under single-bit flips of \(q\) is an affine shear (output xor often low weight for single-bit \(q\) changes) — **diffusion relies on iterating mixed branches + SHA3 shell**, not on one r1 step alone.

---

## 6. Why Option A prefers this branch

1. **Exact integrality** — peer-reviewable closed form, no floor ambiguity.  
2. **No fixed point at 1** — T4121’s \(T(1)=1\) is a clean algebraic footgun.  
3. **RTL simplicity** — same `div3` quotient/remainder pipeline; only the r1 mux constant changes.  
4. **Comparable diffusion** in full HQH shell (prior primitive comparison).

---

## 7. Non-claims

- Not a proof of collision/preimage resistance of HQH-539.  
- Not a claim that \(+1\) vs T4121 is cryptographically large (it is tiny locally; security is in depth 539 + SHA3).  
- Not a Collatz convergence proof for unrestricted iteration counts.

Hardness framing for the hash: computationally infeasible with known methods, pending peer review.

---

## 8. Reproduce

```python
def T(n):
    q, r = divmod(n, 3)
    if r == 0: return q
    if r == 1: return (q << 2) + 2   # 4q+2
    return (q << 1) | 1              # 2q+1
```

*Per aspera ad astra.*
