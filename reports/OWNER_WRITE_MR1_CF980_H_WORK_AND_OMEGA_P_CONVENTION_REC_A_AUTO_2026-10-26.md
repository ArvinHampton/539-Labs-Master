# OWNER WRITE — CF(980) H_work + ω_p convention (Rec A AUTO) — 2026-10-26 ~17:39 CDT America/Chicago
Authority: Owner standing Rec A auto-approve. Source FINDINGS_MR1_EXACT_LIFT_CF980_CRT_2026-10-26.md sha256 adcae95625de96d918ed456d412b142c612d12834146c0fa77ec5703ab451d73.

## CLOSED A (auto) — conventions (definitional Write, not coefficient invent)

### G4c' — ω_p convention (LOCKED)
For every mod-p run at p≡1 mod 980 used for CF(980) CRT:
1. Choose **ω_p** = the least positive integer in {2,…,p−1} that is a primitive 980th root of unity in 𝔽_p (order exactly 980).
2. Record ω_p explicitly in the Soft SF PRESS / FINDINGS sidecar for that run.
3. All residues for a given p MUST be expressed relative to this same ω_p. Cross-prime CRT MUST use Gal(ℚ(ζ₉₈₀)/ℚ)-compatible identification via these recorded roots.

### G4b — H_work provisional CERT gate (LOCKED as convention)
1. **True height H** of the 7 FILLED-MODP cells in a fixed ℤ[ζ₉₈₀]-integral basis remains **UNPROVEN / OPEN** (G4b stands).
2. Owner names provisional working bound **H_work = 10^{18}** solely as a CERT product gate: generate additional eligible primes until ∏_p p > 2·H_work.
3. Any resulting lift is stamped **CERT-under-H_work**, not CERT-absolute. Absolute CERT waits on a proved H (or smaller proved H′ replacing H_work via later Owner Write).
4. No cell may be written as exact in CSV until CERT-under-H_work (or better) lands with ω_p recorded on every prime used.

### Authorize
MR1 (in-set): generate additional p≡1 mod 980 mod-p runs; apply CRT toward CERT-under-H_work for the 7 cells; keep ℚ(ζ₄₉) containment G4a OPEN (no ζ₄₉-only claim). Soft SF → Auditor. Parallel N6 q^121/D1 continues. No Eigen.

## Unchanged
tip Soft SF LOCK 7cddb188… tip_touched NO; Kerr BLOCKED; eight-only; proof standard; Cat-A gate OFF; 7 cells stay FILLED-MODP until CERT-under-H_work.
