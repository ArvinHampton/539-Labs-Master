"""Dual-profile tests: REF KATs + P32 KATs + non-interchangeability."""
from __future__ import annotations

import json
import unittest
from pathlib import Path

from hqh539 import hqh_539_512
from profiles import hqh_539_512_p32

ROOT = Path(__file__).resolve().parent
REF = json.loads((ROOT / "golden_vectors.json").read_text(encoding="utf-8"))
P32 = json.loads((ROOT / "golden_vectors_p32.json").read_text(encoding="utf-8"))


class TestRefGoldens(unittest.TestCase):
    def test_profile_tag(self):
        self.assertEqual(REF.get("profile"), "REF")

    def test_ref_cases(self):
        self.assertEqual(hqh_539_512(b"", b""), REF["hqh_539_512"]["empty"])
        self.assertEqual(
            hqh_539_512("The universe counts in threes.", b""),
            REF["hqh_539_512"]["canonical"],
        )
        self.assertEqual(
            hqh_539_512(str(10**18), b""),
            REF["hqh_539_512"]["large_int"],
        )
        self.assertEqual(
            hqh_539_512("The universe counts in threes.", b"hqh539-2026"),
            REF["hqh_539_512"]["salted"],
        )


class TestP32Goldens(unittest.TestCase):
    def test_profile_tag(self):
        self.assertEqual(P32.get("profile"), "P32")

    def test_p32_cases(self):
        self.assertEqual(hqh_539_512_p32(b"", b""), P32["hqh_539_512"]["empty"])
        self.assertEqual(
            hqh_539_512_p32("The universe counts in threes.", b""),
            P32["hqh_539_512"]["canonical"],
        )
        self.assertEqual(
            hqh_539_512_p32(str(10**18), b""),
            P32["hqh_539_512"]["large_int"],
        )
        self.assertEqual(
            hqh_539_512_p32("The universe counts in threes.", b"hqh539-2026"),
            P32["hqh_539_512"]["salted"],
        )


class TestNonInterchangeable(unittest.TestCase):
    def test_ref_ne_p32_for_all_kat_messages(self):
        for key in ("empty", "canonical", "large_int", "salted"):
            self.assertNotEqual(
                REF["hqh_539_512"][key],
                P32["hqh_539_512"][key],
                msg=f"REF and P32 unexpectedly equal for {key}",
            )


if __name__ == "__main__":
    unittest.main(verbosity=2)
