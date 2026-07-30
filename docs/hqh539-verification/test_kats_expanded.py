"""Expanded Known-Answer / property tests for HQH-539 REF profile."""
from __future__ import annotations

import hashlib
import json
import unittest
from pathlib import Path

from hqh539 import (
    DOMAIN_SEP,
    PREFIX_ROUNDS,
    STEPS,
    SUFFIX_ROUNDS,
    T3,
    hqh_539_256,
    hqh_539_512,
    iterate_n_steps,
)

ROOT = Path(__file__).resolve().parent
REF = json.loads((ROOT / "golden_vectors.json").read_text(encoding="utf-8"))


class TestStructureConstants(unittest.TestCase):
    def test_steps_18_plus_521(self):
        self.assertEqual(STEPS, 539)
        self.assertEqual(PREFIX_ROUNDS, 18)
        self.assertEqual(SUFFIX_ROUNDS, 521)
        self.assertEqual(PREFIX_ROUNDS + SUFFIX_ROUNDS, STEPS)

    def test_domain_sep_empty(self):
        self.assertEqual(DOMAIN_SEP, b"")


class TestT3Integrality(unittest.TestCase):
    def test_range_0_to_9999_nonneg_int(self):
        for n in range(10000):
            y = T3(n)
            self.assertIsInstance(y, int)
            self.assertGreaterEqual(y, 0)

    def test_branch0_exact(self):
        for q in range(0, 500):
            n = 3 * q
            self.assertEqual(T3(n), q)

    def test_branch1_formula(self):
        for q in range(0, 500):
            n = 3 * q + 1
            self.assertEqual(T3(n), (4 * n + 2) // 3)

    def test_branch2_formula(self):
        for q in range(0, 500):
            n = 3 * q + 2
            self.assertEqual(T3(n), (2 * n + 1) // 3)


class TestExpandedHashKats(unittest.TestCase):
    CASES = [
        (b"", b"", "empty"),
        (b"a", b"", "single_a"),
        (b"\x00", b"", "null_byte"),
        (b"\x00\x01\x02\xff", b"", "binary_short"),
        (b"x" * 1, b"", "len_1"),
        (b"x" * 16, b"", "len_16"),
        (b"x" * 63, b"", "len_63"),
        (b"x" * 64, b"", "len_64"),
        (b"x" * 65, b"", "len_65"),
        (b"x" * 1024, b"", "len_1024"),
        (b"x" * 4096, b"", "len_4096"),
        ("The universe counts in threes.", b"", "canonical_str"),
        ("The universe counts in threes.", b"hqh539-2026", "salted"),
        (b"msg", b"s", "tiny_salt"),
        (str(10**18), b"", "large_int_str"),
        (str(10**100), b"", "huge_int_str"),
    ]

    def test_length_hex_charset(self):
        for msg, salt, name in self.CASES:
            with self.subTest(name=name):
                d = hqh_539_512(msg, salt)
                self.assertEqual(len(d), 128, name)
                self.assertEqual(d, d.lower())
                self.assertTrue(all(c in "0123456789abcdef" for c in d), name)

    def test_deterministic(self):
        for msg, salt, name in self.CASES:
            with self.subTest(name=name):
                self.assertEqual(hqh_539_512(msg, salt), hqh_539_512(msg, salt), name)

    def test_256_is_prefix(self):
        for msg, salt, name in self.CASES[:8]:
            with self.subTest(name=name):
                full = hqh_539_512(msg, salt)
                self.assertEqual(hqh_539_256(msg, salt), full[:64])

    def test_salt_sensitivity(self):
        base = hqh_539_512(b"message", b"salt-a")
        other = hqh_539_512(b"message", b"salt-b")
        self.assertNotEqual(base, other)

    def test_message_sensitivity(self):
        a = hqh_539_512(b"message-a", b"")
        b = hqh_539_512(b"message-b", b"")
        self.assertNotEqual(a, b)

    def test_str_vs_bytes_utf8(self):
        s = "The universe counts in threes."
        self.assertEqual(hqh_539_512(s, b""), hqh_539_512(s.encode("utf-8"), b""))

    def test_ref_goldens_still_bind(self):
        self.assertEqual(hqh_539_512(b"", b""), REF["hqh_539_512"]["empty"])
        self.assertEqual(
            hqh_539_512("The universe counts in threes.", b""),
            REF["hqh_539_512"]["canonical"],
        )

    def test_seed_equals_sha3_then_t3_path(self):
        """Manual composition must match hqh_539_512 for a few messages."""
        for msg, salt in [(b"", b""), (b"abc", b"xyz"), (b"\xff\x00", b"s")]:
            seed = int.from_bytes(hashlib.sha3_512(msg + salt).digest(), "big")
            fp = iterate_n_steps(seed, STEPS)
            flen = max(1, (fp.bit_length() + 7) // 8) if fp != 0 else 1
            # match hqh539.py: (bit_length+7)//8 — for fp=0 this is 0 and to_bytes(0) errors
            # live code uses (fingerprint.bit_length()+7)//8 which is 0 for 0
            if fp == 0:
                # document behavior: rare; skip if would crash
                continue
            nbytes = (fp.bit_length() + 7) // 8
            expected = hashlib.sha3_512(
                fp.to_bytes(nbytes, "big") + salt + DOMAIN_SEP
            ).hexdigest()
            self.assertEqual(hqh_539_512(msg, salt), expected)


class TestIterateProperties(unittest.TestCase):
    def test_zero_fixed_point_chain(self):
        self.assertEqual(iterate_n_steps(0, STEPS), 0)

    def test_large_seed_oracle(self):
        for n_str, exp in REF["iterate_n_steps_539"].items():
            self.assertEqual(iterate_n_steps(int(n_str), STEPS), exp)


if __name__ == "__main__":
    unittest.main(verbosity=2)
