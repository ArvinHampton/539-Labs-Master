# FINDINGS — NL open-queue RETAG after t1133u — 2026-10-25 ~20:50 CDT (America/Chicago)
From Write `43433968a0742c115a8ae35ab3744c8ada80572f2d704a50dce1af4f7911000f` (ACK `a65aa6aaa0ebd3150d9ab494b3b1891e2563adfd701539b52f0bf2babf02d176`), grant `c1d59d58…`. Prior RETAG t1118u `3d61e20d…`. invent-ban **LIFTED** (Author scope). Not Cat A.

| Q | t1118u | t1133u | Note |
|---|---|---|---|
| Q1 | POINTER-ACKED | POINTER-ACKED | — |
| Q2 | PARTIAL-CLOSED | PARTIAL-CLOSED | — |
| Q3 | PARTIAL-CLOSED (def) | PARTIAL-CLOSED (def) | — |
| Q4 | ABSENT-hold | **ABSENT-hold KEEP** | human-turn re-sweep 0 hits gaps 5/7 |
| Q5 | ABSENT | ABSENT | — |
| Q6 | PARTIAL-CLOSED (def) | PARTIAL-CLOSED (def) | Φ(y) canonical (SF-W4 reconciled) |
| Q7 | OPEN-proof-gated | OPEN-proof-gated | no Lean |
| Q8 | ABSENT-hold (f_*); Ω UNAFFECTED | **ABSENT-hold (f_*)**; Ω_11D≡1 **LOCKED Local fact (tip 87fcda27… §1h) cataloged, not NL-edited**; "UNAFFECTED" retired | f_* 0 hits |
| Q9 | STOPPED | STOPPED | no unlock |
| Q10 | PARTIAL-CLOSED (mech) | **PARTIAL-CLOSED (mech + coeffs advanced)** | Written: ε_S8=1e-14, Δt_11D=t/(1+g_11Φ(y)), δ(t) split (5e-5 phase / 1e-20 s⁻¹ leak); OPEN: H, ψ, photon coupling, rates |
| Q11–13 | POINTER-ACKED | POINTER-ACKED | — |
| Q14–16 | STOPPED | STOPPED | — |
| Q17 | LOCKED Local | LOCKED Local | tip 87fcda27… MATCH |

Soft SF: W4 RECONCILED · W5 KEEP-compatible · W6 RECONCILED (τ_ent=539.9 s; 233.38 as = τ_ent^micro; GM/c³ = Clock I) · W7 RECONCILED (scoped) · W8 RECONCILED to tip Ω_11D≡1.

## Counts (17)
PARTIAL-CLOSED 4 (Q2,Q3,Q6,Q10) · ABSENT/ABSENT-hold 3 (Q4,Q5,Q8-f_*) · OPEN-proof-gated 1 (Q7) · POINTER-ACKED 4 (Q1,Q11–13) · STOPPED 4 (Q9,Q14–16) · LOCKED 1 (Q17) = 17. NEED WRITE: 0.

## Status
Bridge **PARTIAL** · residual-C **LOCKED** tip `87fcda27e6eac193e1bf6d258109b27a73ac5cdf86ecc155b7952085776393c4` (Ω_11D≡1 folded; NL read-only) · READY **NO** · invent-ban LIFTED · not Cat A.

## Tip-drift note (verify step, ~20:52 CDT America/Chicago)
Live residual-C is now sha256 `c7121aa8bf7d2e534f0ad55ce1b4a1a1a26db8289087979f3a263efe9565a5ef` (mtime 20:34:37 CDT), **not** `87fcda27…`. Edit was made by MR2 (§1i "55-Step retire fold", pending Auditor re-CONFIRM), backup `.pre-55step-retire-fold-87fcda27.md` = `87fcda27…` exactly. **NL did not touch residual-C.** Ω_11D ≡ 1 (§1h) remains in the live tip, so the NL catalog entry holds unchanged. Diff 87fcda27→c7121aa8: §1g/§1h status lines + new §1i only (retires 55-Step κ_dark^(class)=0.181, 58481, closure 539 identity, δa_μ^(55) prefactor); no NL lever affected.
