# AUTHOR-CANDIDATE (NOT Cat A) — B1 residual_factor off-sample selector
Status: **HISTORICAL / SUPERSEDED** (object-type stamp 2026-10-25 ~18:23 CDT America/Chicago).
Superseded for residual_factor identity by Owner CONFIRM Item (2): residual_factor ∈ V (dim 42) — OWNER_WRITE_ITEM2 sha 49aba949…; residual-C draft 5bb86c70… §1b item 5.
Do **not** ACCEPT S-B1 / S-B1′ under this scalar selector. File kept as historical record only (prior sha fdc79a110bccfbf84e313e75d85721912ae4aefc78087a2439436cf0eb8d4868).
Campaign deduce_t682u (PREREG c3316e3d0da3ba1b63eea8bd0c385b0f4c5e7d480d55db83a464eea0e02c9860). No numeric tables; no new numbers. invent-ban held; residual-C not edited by this stamp.

## What Written already says (DEDUCED quotes)
- 7add2a9a L35: deg-3 polynomial interpolates the four ratios exactly but "does not constitute a residual modular Fricke polynomial identity".
- 7368b855 L46–L49: written ansatz residual_slash = |7x|^{-1/2}·residual_factor(x), residual_factor = a+bt+ct²+d/(1+t²), t=7x−3 (4 parameters / 4 samples ⇒ interpolation, not forcing).
- 13eb50e6 L143–L144 (B7) + L161 (OB4): Dual-split agrees at 4 samples, disagrees off-sample; off-sample uniqueness not forced.
- pins/RESIDUAL_LAW_C_CANDIDATE_W7 (b9a21438): ∀x identity "not yet proved".

## Proposed selector (for ACCEPT)
S-B1 (W_7 cocycle consistency): residual_slash must satisfy the involution compatibility
  residual_slash(x) · residual_slash(W_7 x) = 1 on the domain of h (from W_7² = id applied twice to δ_{W_7}h = 0),
together with
S-B1' (weight-1/2 growth): |residual_factor(x)| = O(1) as x→0⁺ and as x→∞ along the real axis (prefactor |7x|^{-1/2} carries all weight-1/2 growth).
Rationale: deg-3 polynomial has |·|→∞ as x→∞ (fails S-B1'); Dual-split's off-sample disagreement is to be tested against S-B1 (Written does not state Dual-split values off-sample, so exclusion of Dual-split under S-B1 is UNVERIFIED and is itself an ACCEPT item).

## Arvin must ACCEPT
1. S-B1 as a Cat A residual law premise (Written only has δ_{W_7}h as candidate).
2. S-B1' growth condition.
3. That S-B1 ∧ S-B1' are to be checked against Dual-split (C5/B7) before any uniqueness claim.
Even after ACCEPT, uniqueness requires a separate PREREG→RESULTS proof; δ≡0 not claimed.
