#!/usr/bin/env python3
"""Known-answer tests for HQH-539 reference (implementation checks, not hardness)."""
from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path

from hqh539 import STEPS, T3, hqh_539_256, hqh_539_512, iterate_n_steps

GOLDEN = json.loads((Path(__file__).parent / "golden_vectors.json").read_text(encoding="utf-8"))


class TestT3(unittest.TestCase):
    def test_branch_oracle_values(self):
        for n_str, expected in GOLDEN["t3"].items():
            self.assertEqual(T3(int(n_str)), expected)

    def test_integrality_sample(self):
        for n in range(0, 300):
            y = T3(n)
            self.assertIsInstance(y, int)
            self.assertGreaterEqual(y, 0)


class TestIterate(unittest.TestCase):
    def test_exactly_539(self):
        n = 10**18
        state = n
        for _ in range(STEPS):
            state = T3(state)
        self.assertEqual(state, iterate_n_steps(n, STEPS))

    def test_large_seed_oracle(self):
        for n_str, expected in GOLDEN["iterate_n_steps_539"].items():
            self.assertEqual(iterate_n_steps(int(n_str), STEPS), expected)


class TestHQH(unittest.TestCase):
    def test_length(self):
        d = hqh_539_512("probe")
        self.assertEqual(len(d), 128)

    def test_256_prefix(self):
        full = hqh_539_512("The universe counts in threes.")
        short = hqh_539_256("The universe counts in threes.")
        self.assertEqual(short, full[:64])
        self.assertEqual(short, GOLDEN["hqh_539_256_prefix"])

    def test_golden(self):
        self.assertEqual(hqh_539_512(b"", b""), GOLDEN["hqh_539_512"]["empty"])
        self.assertEqual(
            hqh_539_512("The universe counts in threes.", b""),
            GOLDEN["hqh_539_512"]["canonical"],
        )
        self.assertEqual(
            hqh_539_512(str(10**18), b""),
            GOLDEN["hqh_539_512"]["large_int"],
        )
        self.assertEqual(
            hqh_539_512("The universe counts in threes.", b"hqh539-2026"),
            GOLDEN["hqh_539_512"]["salted"],
        )

    def test_salt_changes(self):
        self.assertNotEqual(hqh_539_512("m", b"a"), hqh_539_512("m", b"b"))


if __name__ == "__main__":
    r = unittest.main(verbosity=2, exit=False)
    sys.exit(0 if r.result.wasSuccessful() else 1)
