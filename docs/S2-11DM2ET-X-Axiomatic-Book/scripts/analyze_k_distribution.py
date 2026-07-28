#!/usr/bin/env python3
"""
Distribution of the minimal charge-correcting exponent k(n)
for the published rule:

  n ≡ 2 (mod 3):  T(n,k) = (n+1)//3 + 2 * 3**k
  k(n) = min { k ≥ 0 : T(n,k) ≡ n (mod 9) }   # Q(n)=n mod 9 preserved

Re-run: python analyze_k_distribution.py
"""
from __future__ import annotations

from collections import Counter, defaultdict
from math import log


def T(n: int, k: int) -> int:
    return (n + 1) // 3 + 2 * (3**k)


def min_k(n: int, max_k: int = 12) -> int | None:
    """Minimal k preserving Q(n)=n mod 9, or None if impossible in this family."""
    target = n % 9
    for k in range(0, max_k + 1):
        if T(n, k) % 9 == target:
            return k
    return None


def classify_mod_27() -> dict[int, int | None]:
    """k* as a function of n mod 27 for n ≡ 2 (mod 3)."""
    out: dict[int, int | None] = {}
    for r in range(27):
        if r % 3 != 2:
            continue
        n = r + 27 * 3  # large enough representative
        out[r] = min_k(n)
    return out


def main() -> None:
    print("=== Algebraic structure of 2*3^k mod 9 ===")
    for k in range(0, 8):
        print(f"  k={k}: 2*3^k = {2*3**k}, mod 9 = {(2*3**k) % 9}")
    print("  => only three distinct corrections: k=0 -> +2, k=1 -> +6, k>=2 -> +0 (mod 9)")
    print("  => k>=3 never improves on k=2 for mod-9 matching; k is bounded by 2 if it exists.\n")

    cls = classify_mod_27()
    print("=== Classification of n ≡ 2 (mod 3) by n mod 27 ===")
    print(f"{'r27':>4} {'r9':>3} {'k*':>4}")
    for r, k in sorted(cls.items()):
        print(f"{r:4d} {r%9:3d} {str(k):>4}")

    feasible = [r for r, k in cls.items() if k is not None]
    impossible = [r for r, k in cls.items() if k is None]
    print(f"\nFeasible r27 classes: {feasible}  ({len(feasible)}/9)")
    print(f"Impossible r27 classes: {impossible}  ({len(impossible)}/9)")
    print(f"Density of feasible branch-2 integers: {len(feasible)/9:.6f}")

    print("\n=== Monte Carlo over n ≡ 2 (mod 3), n < 3e6 ===")
    ks: list[int] = []
    imp = 0
    chi_large: list[float] = []
    for n in range(2, 3_000_000, 3):
        k = min_k(n)
        if k is None:
            imp += 1
            continue
        ks.append(k)
        Tn = T(n, k)
        if n > 0:
            chi_large.append(log(Tn / n))

    c = Counter(ks)
    N = len(ks) + imp
    print(f"N={N}  feasible={len(ks)}  impossible={imp}  P(impossible)={imp/N:.6f}")
    print(f"P(k|feasible) = {{" + ", ".join(f"{k}: {c[k]/len(ks):.6f}" for k in sorted(c)) + "}")
    print(f"E[k|feasible] = {sum(ks)/len(ks):.6f}")
    print(f"max k observed = {max(ks)}")
    print(f"E[chi|feasible, n<3e6] ≈ {sum(chi_large)/len(chi_large):.6f}")
    print(f"  (compare unrestricted ln(1/3)≈{log(1/3):.6f}, mean unres≈-0.405465)")

    print("\n=== Asymptotics for fixed k ===")
    print("  T(n,k)/n = (n+1)/(3n) + 2*3^k/n → 1/3  as n→∞, for any fixed k.")
    print("  Hence chi → ln(1/3) < 0 on every infinite feasible ray; no runaway from large k.")
    print("\n=== ACE implication ===")
    print("  Under this published family, k is NOT heavy-tailed and NOT unbounded.")
    print("  The open ACE difficulty is NOT 'arbitrarily large k'; it is:")
    print("    (1) 2/3 of branch-2 states admit NO preserving k;")
    print("    (2) dynamics on the feasible subspace + other branches still need a full measure;")
    print("    (3) bridge from E[chi] to integer 539 remains separate.")


if __name__ == "__main__":
    main()
