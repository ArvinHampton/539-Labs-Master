#!/usr/bin/env python3
"""Sanity checks for residue-1 Canonical 4q+2 (see Architecture_Residue1_4q2_Map.md)."""
from __future__ import annotations


def T(n: int) -> int:
    q, r = divmod(n, 3)
    if r == 0:
        return q
    if r == 1:
        return (q << 2) + 2
    return (q << 1) | 1


def main() -> None:
    for q in range(0, 1000):
        n = 3 * q + 1
        y = T(n)
        assert y == 4 * q + 2
        assert y == (4 * n + 2) // 3
        assert (4 * n + 2) % 3 == 0
        assert y % 4 == 2
        # vs T4121
        y4121 = (4 * n + 1) // 3
        assert y == y4121 + 1
    assert T(1) == 2 and T(2) == 1  # 2-cycle, not fixed 1
    print("residue-1 4q+2 checks: PASS (1000 q's + cycle)")


if __name__ == "__main__":
    main()
