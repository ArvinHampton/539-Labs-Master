# Lean L1–L7 assumptions vs derivations (cite only; oct17-master/lean, identical in self-audit/repo/lean and _git_v8_unpushed_clone/lean per diff -q)
File: EinsteinHamptonCurvature.lean. No `axiom`/`sorry` found.
| Li | Lean | Proved | Assumed |
|---|---|---|---|
| L1 | L1_off/time/ext_space/yy/fib (:59-86) | inverse products on diagonal chart | chart defs g,gInv |
| L2 | L2_lock (:128), L2_fibre (:113) | chain rule under A=ky | fibre half = `True` (trivial def :102) |
| L3 | L3_lock (:152) | Γ^y/g=k | Γ defined directly (:145,:163-166), not from metric derivation |
| L4 | L4_lock (:185) | Riem scalar −k² | L4_Riem_ext is a def from A', not computed 11D Riemann |
| L5 | L5_linear (:189) | −k² | linear warp |
| L6 | L6_lock_Einstein_blocks (:196) | blocks −18k², −6k² | hK: K=8k² as hypothesis; block formulas 6k²−3K,10k²−2K, Ric −4k² are defs (:149-150) |
| L7 | L7_fibre_lock (:205) | k²=Φ/1728, K=8k² | h1, h2 hypotheses; Φ is free real (no quantisation, no Ω) |
EinsteinHampton.lean: EinsteinHamptonEquation G=8πG11·T_total (def only); HamptonStress has T_G4 slot but no weights.
Status discrepancy: Lean header (:15-16) "Lake 4.34.0 … built L1-L7 on 29 September 2026"; EH1 zenodo App. C "Lean source: L5, L7. No kernel run here." Header itself: "not an eleven-dimensional Riemann API"; Mathlib11DRiemannAPI.lean:123 is the separate 09-29 API (not audited here). No kernel run performed by us.
Key: L7 is pure linear algebra on assumed block equations; four-form content enters only via h1/h2 (now shown EH-FF1 to follow from a=1/24 weights given Φ≡G², 8πG11=1).
