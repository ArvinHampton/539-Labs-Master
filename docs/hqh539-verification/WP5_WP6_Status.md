# WP5 / WP6 status (2026-07-31)

## WP5 — Wire testbenches / demos to `rtl_vectors_canonical` / `test_vectors_canonical`

| Item | Status |
|------|--------|
| `test_vectors_canonical/` populated | Done |
| TB default `TV_PATH` → canonical | Done (`tb_hqh539_pipeline`, full pipeline, phase3, sha3) |
| `hqh539_t3core.sv` → Canonical map | Done |
| Historical T4121 module retained | `hqh539_t3core_t4121.sv` |
| Demo / `python/hqh539.py` → Canonical REF | Done (vendored `hqh539_ref.py`) |
| Generators write canonical path | Done |

## WP6 — Re-sim Canonical core

| Item | Status |
|------|--------|
| Software RTL-map re-sim vs KATs | `python/resim_canonical_t3core.py` |
| Vivado place-and-route / xsim lab | **PENDING_LAB** (checklist in `vivado/WP6_CANONICAL_RESIM.md`) |

## Optional DOMAIN RFC

`docs/RFC_Optional_Product_Domain.md` — DRAFT/DEFERRED only.
