# Soft SF FINDINGS: PP audit of Local ABSORB a4130f51 and its PRESS, against MR1 B §III review f4305f21 — CONFIRM
Prepared 2026-11-09, audit ~12:20 CST, filed ~12:30 CST (America/Chicago).

**Authority.** Owner DIRECT on the live call of Nov 9 at 12:29 CST, relayed by Physicist: additive new dated files only. No CERT. tip 7cddb188 untouched.

## Hashes (all MATCH on disk)
- MR1: f4305f21
- Local ABSORB: a4130f51 (as cited in PRESS L4–5)
- B compendium: 9c6f83da (§III.1 read directly, L28–33)
- Local pass: 2a5edc87
- tip: 7cddb188

## Audit
- **S1 — PROVED.** √(2/0.7858) = 1.5953610531, so the rounding to 1.5953611 is correct. The circularity diagnosis holds while Λ₀ is underived.
- **S2 — OPEN.** Inputs (a)–(e) are not defined in B.
  - Standard fact: the 4-regular Bruhat–Tits tree of Q₃ has growth 3 and Kesten radius 2√3 ≈ 3.4641.
  - This shows only that a normalization is missing. It does not refute B, and FAIL was correctly not claimed.
- **S3 — OPEN.** 1.59543 − 1.5953611 = 6.8947×10⁻⁵, which exceeds the 4×10⁻⁵ tolerance. By contrast, 1.5954 is within it (3.89×10⁻⁵).
  - So 1.59543 is underived and is not the Λ₀ value. It is not refuted as a value.
- **S4 — OPEN.** It depends on S2 and S3. The supersession by the Owner C Tier E de-escalation is consistent.
  - Caveat: the file for Owner C 918f5c37 was not located by name, so I took that hash as cited.

**Net.** B §III is not a derivation. R_c stays UNDERIVED, at Tier E (E-UNTESTED), with no Tier P status. Local's grades are confirmed: 4 MATCH, 0 FLAG, 0 FAIL.

REPORTS ONLY. No CERT.
