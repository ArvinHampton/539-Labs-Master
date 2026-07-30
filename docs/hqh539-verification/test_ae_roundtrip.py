"""AEAD roundtrip tests: HQH-539 KDF + ChaCha20-Poly1305 (crypto_hqh)."""
from __future__ import annotations

import os
import unittest

from crypto_hqh import (
    CryptoError,
    decrypt_bytes,
    encrypt_bytes,
    hqh539_kdf,
    is_hqh539_package,
    pack_encrypted_file,
    unpack_encrypted_file,
)


class TestKdf(unittest.TestCase):
    def test_length(self):
        out = hqh539_kdf(b"password", salt=os.urandom(32), length=44)
        self.assertEqual(len(out), 44)

    def test_deterministic(self):
        salt = b"S" * 32
        self.assertEqual(
            hqh539_kdf(b"pw", salt=salt, length=44),
            hqh539_kdf(b"pw", salt=salt, length=44),
        )

    def test_salt_changes(self):
        self.assertNotEqual(
            hqh539_kdf(b"pw", salt=b"A" * 32, length=44),
            hqh539_kdf(b"pw", salt=b"B" * 32, length=44),
        )

    def test_empty_secret_rejected(self):
        with self.assertRaises(CryptoError):
            hqh539_kdf(b"", salt=b"S" * 32)


class TestAeRoundtrip(unittest.TestCase):
    def test_empty_plaintext(self):
        salt, ct, _ = encrypt_bytes(b"", b"password-secret")
        self.assertEqual(decrypt_bytes(ct, b"password-secret", salt), b"")

    def test_short_message(self):
        msg = b"hello HQH-539"
        salt, ct, _ = encrypt_bytes(msg, b"password-secret")
        self.assertEqual(decrypt_bytes(ct, b"password-secret", salt), msg)

    def test_binary_blob(self):
        msg = bytes(range(256)) * 4
        salt, ct, _ = encrypt_bytes(msg, b"pw")
        self.assertEqual(decrypt_bytes(ct, b"pw", salt), msg)

    def test_large_blob(self):
        msg = os.urandom(100_000)
        salt, ct, _ = encrypt_bytes(msg, b"large-pw")
        self.assertEqual(decrypt_bytes(ct, b"large-pw", salt), msg)

    def test_wrong_password_fails(self):
        salt, ct, _ = encrypt_bytes(b"secret-data", b"correct-password")
        with self.assertRaises(CryptoError):
            decrypt_bytes(ct, b"wrong-password", salt)

    def test_aad_roundtrip(self):
        msg = b"payload"
        aad = b"header-meta-v1"
        salt, ct, _ = encrypt_bytes(msg, b"pw", associated_data=aad)
        self.assertEqual(decrypt_bytes(ct, b"pw", salt, associated_data=aad), msg)
        with self.assertRaises(CryptoError):
            decrypt_bytes(ct, b"pw", salt, associated_data=b"tampered")

    def test_tampered_ciphertext_fails(self):
        salt, ct, _ = encrypt_bytes(b"data", b"pw")
        bad = bytearray(ct)
        bad[-1] ^= 0x01
        with self.assertRaises(CryptoError):
            decrypt_bytes(bytes(bad), b"pw", salt)

    def test_different_salts_different_ct(self):
        msg = b"same"
        s1, c1, _ = encrypt_bytes(msg, b"pw", salt=b"1" * 32)
        s2, c2, _ = encrypt_bytes(msg, b"pw", salt=b"2" * 32)
        self.assertNotEqual(c1, c2)
        self.assertEqual(decrypt_bytes(c1, b"pw", s1), msg)
        self.assertEqual(decrypt_bytes(c2, b"pw", s2), msg)


class TestPackagedBlob(unittest.TestCase):
    def test_pack_roundtrip(self):
        msg = b"file-bytes-content"
        blob = pack_encrypted_file(msg, b"pw", "demo.bin")
        self.assertTrue(is_hqh539_package(blob))
        pt, name = unpack_encrypted_file(blob, b"pw")
        self.assertEqual(pt, msg)
        self.assertEqual(name, "demo.bin")

    def test_pack_wrong_password(self):
        blob = pack_encrypted_file(b"secret", b"good", "x.bin")
        with self.assertRaises(CryptoError):
            unpack_encrypted_file(blob, b"bad")

    def test_pack_bad_magic(self):
        blob = pack_encrypted_file(b"x", b"pw", "x.bin")
        bad = b"XXXXXXXX" + blob[8:]
        with self.assertRaises(CryptoError):
            unpack_encrypted_file(bad, b"pw")


if __name__ == "__main__":
    unittest.main(verbosity=2)
