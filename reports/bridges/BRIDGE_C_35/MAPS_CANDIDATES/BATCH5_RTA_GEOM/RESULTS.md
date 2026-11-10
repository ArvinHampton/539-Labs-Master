# RESULTS: BATCH5_RTA_GEOM
PREREG.md sha256 35563f1388e39795799b6f37b0f7987aa2c1add25677d1dfb9e0160688c48379, hashed before tests. Script scripts/b5.py (hash in scripts/SHA256SUMS); data data/b5.json; log logs/b5.log. Exact integer Gram ranks (sympy), under 1 s.

| Test | Measured | Verdict |
|---|---|---|
| Full-carrier control (written lock) | rank[t_w, η] = 2, rank[t_w, η, s_ad] = 3 → survives | control OK (run valid) |
| Map-C19: survives in all 8 fibres | survival set {0, …, 7} | **PASS** (Category B), **non-discriminating**, see below |
| Map-C20: survives iff χ₁₄₀(2r+1) = 1, predicted set {0, 4, 6} | survival set {0, …, 7} | **FAIL** |
| C6, C10, C11, E1–E3 | still blocked | OPEN |

## Why the C19 pass carries no modular content (Category A, elementary; found after the run, verdict unchanged)
- On any slice, suppose s_ad = x·t_w + y·η. The squares force y = 1, if s_ad ≠ 0 on the slice. The triangles then force x·ω₂ = ω₂·f(i) for every slice vertex i, i.e. f is constant on the slice.
- Hence **survival on a slice ⇔ (δf ≠ 0 on some slice edge) and (f not constant on the slice vertices).**
- Every fibre has 26–40 tower jumps (BATCH4 C16) and non-constant f, so survival in all 8 fibres is forced by the carrier alone, whatever the modular datum.
- The C19 "pass" is therefore a survived but vacuous prediction. It is **not** a Residual–Resonant or geometric bridge, and no bridge claim is made.
- The same lemma shows that any per-fibre (or any sub-sampled) version of this criterion is non-discriminating. The written thin-F survival test cannot single out fibres.
