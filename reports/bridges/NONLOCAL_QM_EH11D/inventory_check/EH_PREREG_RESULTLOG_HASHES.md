# EH_PREREG_RESULTLOG_HASHES — W-NL-4 (verify-closed 2026-10-24 22:29 CDT)
**Canonical SUMS:** `inventory_check/SHA256SUMS`
**Paths:** `../prereg/.../result.log` (relative to inventory_check/)

Run from the directory that contains the SUMS file:
```
cd /workspace/quantum-comp/reports/bridges/NONLOCAL_QM_EH11D/inventory_check && sha256sum -c SHA256SUMS
```
Expected: 3 OK (CJS / GC1 / original RICCIBLOCK result.log).

Prereg dirs untouched (no in-dir RESULTS.sha256; CORE_FREEZE). Post-hoc integrity from this stamp forward.
