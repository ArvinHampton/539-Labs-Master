# Canonical T3 vs T4121 — which is the superior primitive?

**Status:** Engineering comparison complete (2026-07-30)  
**Winner (engineering):** **Canonical T3**  
**Probe:** `compare_ternary_primitives.py` → `ternary_primitive_comparison_results.json`  
**Security:** Not a reduction. Hardness remains: computationally infeasible with known methods, pending peer review.

---

## 1. What differs

Both maps agree on residues 0 and 2. They **disagree only when** \(n \equiv 1 \pmod 3\):

| Residue | Canonical T3 | T4121 |
|---------|--------------|-------|
| \(n \equiv 0\) | \(n//3\) | \(n//3\) |
| \(n \equiv 1\) | \((4n+2)//3\) | \((4n+1)//3\) |
| \(n \equiv 2\) | \((2n+1)//3\) | \((2n+1)//3\) |

Empirically, maps disagree on **exactly ~1/3** of integers (all residue-1 inputs). 100% of disagreements are residue-1.

**Algebra:** Canonical residue-1 is **exact** divisible by 3. T4121 residue-1 is **floor** division (\(4n+1 = 12q+5\)).

---

## 2. Fair test shell

To compare maps (not wrappers), both used the same shell:

```text
SHA3-512(message ‖ salt) → 539 × map → SHA3-512(min-length BE fingerprint ‖ salt)
```

RTL product domain / 32-byte finalize held fixed off the comparison so the map is isolated.

---

## 3. Results (summary)

| Metric | Canonical T3 | T4121 | Edge |
|--------|--------------|-------|------|
| HQH-shell avalanche mean bit-flip | **0.4985** | 0.5010 | Tie ≈ 0.5 (Canonical slightly tighter MAD) |
| Avalanche MAD from 0.5 | **0.0171** | 0.0188 | Canonical |
| Branch occupancy | ≈ 1/3 each | ≈ 1/3 each | Tie |
| End bit-length after 539 (512-bit seeds) | ~195–197 | ~196–197 | Tie (both contract) |
| Contraction path variance @539 | **lower σ** | higher σ | Canonical (more stable width) |
| Mid-state sensitivity @18 | 0.483 | 0.477 | Slight Canonical |
| Mid-state sensitivity @539 | 0.373 | **0.398** | Slight T4121 |
| Local T(n) vs T(n⊕1) Hamming | 127.7 | 128.0 | Tie |
| Fixed points (n<50k) | {0} | {0, **1**} | Canonical cleaner |
| Exact residue-1 division | **Yes** | No (floor) | Canonical |
| Throughput (same shell) | ~0.18 ms | ~0.18 ms | Tie |
| Toy 32-bit reduced-round collisions (8 rounds, 8k msgs) | 0 | 0 | Tie (not a break) |
| Engineering score (0–100 heuristic) | **67.5** | 62.0 | **Canonical** |

SHA3-512 control avalanche ≈ 0.500 — both maps sit in the same band as the Category A outer hash under this shell.

---

## 4. Interpretation

1. **Diffusion (avalanche):** Both are acceptable and near 50% under the HQH shell. Neither is a clear diffusion champion; Canonical has slightly better MAD.
2. **Algebra / implementability:** Canonical wins cleanly — exact branch on residue 1, single fixed point 0 in the small sample, no extra fixed point at 1.
3. **Contraction:** Both strongly contract 512-bit seeds to ~196 bits after 539 steps (matches the ~−0.585 bit/step asymptotic). Canonical shows **tighter** width variance (better for fixed-width RTL sizing arguments).
4. **T4121 mid-state @539** is slightly higher in this trial (more residual xor-fraction); not enough alone to overturn algebra + MAD + variance + fixed-point cleanliness.
5. **RTL history:** T4121 earned post-route timing notes. That is a **hardware** win for an experimental core, not automatic proof it is the better **crypto** map.

---

## 5. Superior primitive decision

> **Primary crypto primitive: Canonical T3.**  
> **T4121: experimental / historical RTL path** — retain for Kerckhoffs inspection and timing artefacts; do not treat as the default HQH-539 product map unless a future study shows clear, reproducible diffusion superiority (not shown here).

This aligns engine **REF** and deprecates treating PRODUCT_T4121 vectors as the security target.

### Product implication (profile freeze leaning **option A**)

| Item | Action |
|------|--------|
| Engine REF | Keep Canonical T3 |
| Public primitive claim | Canonical T3 |
| RTL vectors in repo | Label **PRODUCT_T4121 / historical** |
| New RTL for product | Re-vector under Canonical (+ chosen finalize/domain) |
| crypto_hqh KDF | Stay on REF (Canonical) |

---

## 6. Non-claims

- Not a security reduction  
- Not “T4121 is broken”  
- Not information-theoretic hardness  
- Not independence from SHA3 wrapper for full-primitive claims (shell includes SHA3)

---

## 7. Reproduce

```bash
python3 compare_ternary_primitives.py
# → ternary_primitive_comparison_results.json
```

*Per aspera ad astra.*
