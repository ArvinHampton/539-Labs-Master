# Plan: Canonical re-vector of RTL KATs

**Parent:** `RFC_Profile_Freeze_Option_A.md` (ACCEPTED)  
**Goal:** Replace *product* RTL known-answer targets with **Canonical T3** vectors, without destroying historical T4121 artefacts.

---

## 1. Scope

| Layer | Historical (keep) | New product target |
|-------|-------------------|--------------------|
| SHA3 standalone | `rtl_vectors/stimulus_sha3.dat` | Unchanged (Category A) |
| T3 core (Phase 2) | `rtl_vectors/*_t3core.dat` (**T4121**) | `rtl_vectors_canonical/*_t3core.dat` (**Canonical**) |
| Phase 3 finalize | product domain + 32-byte | Two tracks (below) |
| Pipeline e2e | T4121 + product domain | Canonical + **chosen** finalize |

### Finalize choice for new RTL product vectors

| Track | Finalize | Domain | Use |
|-------|----------|--------|-----|
| **C-REF** (default, matches engine) | min-length BE fingerprint | `b""` | Software/REF parity |
| **C-P32** (optional HW-friendly) | fixed 32-byte BE (low 256 bits) | `b""` or product domain | Fixed-width SHA3 input in RTL |

**Phase-1 re-vector ships C-REF for software parity and C-P32 for hardware-shaped Phase3/pipeline.**  
Product **digest** claims for “HQH-539” without qualifier remain **C-REF** (engine).

Salt for message→seed in vector generators (message catalogue):

- Keep `SALT_STD = b"539-LABS-2026-RESONANT-SALT"` for **seed construction** of stimulus files (same messages as historical), so seeds can be compared side-by-side with old files.  
- REF finalize uses the **same salt bytes** as the call (engine API), not a forced product domain string.

---

## 2. Directory layout

```text
rtl_vectors/                 # HISTORICAL T4121 + product domain (frozen read-only label)
rtl_vectors_canonical/       # NEW product KATs (Canonical)
  stimulus_t3core.dat
  expected_t3core.dat
  stimulus_phase3_p32.dat
  expected_phase3_p32.dat
  stimulus_pipeline.dat
  expected_pipeline_ref.dat      # C-REF digests
  expected_pipeline_p32.dat      # C-P32 digests
  MANIFEST.json
```

Historical path is never deleted by this plan.

---

## 3. Vector definitions

### 3.1 T3 core (Phase 2)

- **Stimulus:** 512-bit seed hex = `int(SHA3-512(msg_i ‖ SALT_STD))`  
  `msg_i = f"Resonant test vector {i} for 539 Labs - STD mode".encode()`  
- **Expected:** `CanonicalT3^539(seed)` as 1024-bit zero-padded hex  
- **N:** 100 (match historical count)

### 3.2 Phase 3 (P32 HW shape)

- **Stimulus:** 32-byte BE state = `(state & (2^256-1)).to_bytes(32)` after Canonical^539 on random or pipeline seeds  
- **Expected:** `SHA3-512(state_32 ‖ SALT_STD)` with **empty** domain (engine-aligned)  
  *Note: historical used `DOMAIN = b":HQH-539-RESONANT:"` — not used for C-P32 empty-domain track.*

### 3.3 Pipeline e2e

- **Stimulus:** same seeds as t3core  
- **expected_pipeline_ref.dat:** full engine `hqh_539_512(msg, SALT_STD)` (Canonical REF)  
- **expected_pipeline_p32.dat:** Canonical + 32-byte finalize + salt, domain empty (`hqh_539_512_p32`)

---

## 4. Work packages

| WP | Task | Exit criteria |
|----|------|----------------|
| WP0 | Freeze Option A RFC | This plan + RFC merged |
| WP1 | Generator script `scripts/gen_canonical_rtl_vectors.py` | Reproducible; seed 539 |
| WP2 | Emit `rtl_vectors_canonical/*` | MANIFEST hashes recorded |
| WP3 | Cross-check script mode `--canonical` | 100% pass on new files |
| WP4 | Label historical `rtl_vectors/README_HISTORICAL.md` | T4121 only |
| WP5 | (Later) 539-Labs-repo / RTL TB point at canonical paths | Separate commit |
| WP6 | (Later) Silicon / sim re-run on Canonical core | Lab schedule |

---

## 5. Risks

| Risk | Mitigation |
|------|------------|
| Old demos expect T4121 digests | Version/profile tag; do not break historical paths |
| 32-byte overflow if state > 256 bits | Mask low 256 bits (observed max ~237 bits after 539) |
| Domain string drift | Empty domain for C-REF/C-P32 unless new RFC |
| Accidental mix in CI | Separate directories + MANIFEST profile field |

---

## 6. Acceptance for re-vector complete

- [x] Generator exists and is deterministic  
- [x] `rtl_vectors_canonical/` populated  
- [x] Cross-check passes 100% on Canonical files  
- [x] Historical `rtl_vectors/` still pass T4121 cross-check  
- [ ] External RTL TB / 539-Labs-repo switched (WP5 — follow-up)

---

## 7. Commands

```bash
python3 scripts/gen_canonical_rtl_vectors.py
python3 rtl_vector_crosscheck.py              # historical T4121
python3 rtl_vector_crosscheck_canonical.py    # new Canonical
```

*Per aspera ad astra.*
