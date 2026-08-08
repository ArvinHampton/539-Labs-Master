# RH Solid Direction 3 — Path Continuation from On-Line Ω (Next Step)

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` · pure Category A · ZLA  
**Does not prove:** O-M1.3bis · O-TL · RH  
**Reservoir:** on-line strong Omega for hybrid discrepancy (accepted programme theorem at typical √(log log X) scale; model size ≍ √X/log X for fixed X)

---

## 1. Open differential bound (precise)

Along a horizontal or slightly inclined path from ½+it_* to σ_*+it_* (σ_* maximal abscissa),

|∂_σ Δ_X(σ+it_*)| ≤ Φ(σ, t_*, X)

with Φ an explicit majorant from |ζ′/ζ| and the hybrid remainder. If

∫_{1/2}^{σ_*} Φ(σ,t_*,X) dσ  <  |Δ_X(½+it_*)| / 2

then a large on-line value survives continuation to σ_*.

---

## 2. Concrete next steps

### P3.1 — Majorant Φ from explicit formula

Build Φ from:
- truncated explicit formula for ζ′/ζ on ½ ≤ σ ≤ 1;
- density bounds (CS / Ingham) for the zero sum;
- GHK remainder for the hybrid piece.

**Success:** a written majorant with tracked constants (no numerics required for the statement).

### P3.2 — Compare to on-line reservoir size

For fixed large X, on-line |Δ_X| is infinitely often ≫ √X / log X (model). Check whether ∫ Φ is o(of that size) on average or on a positive-density subset of the locked progression.

**Success:** conditional inequality under a named zero-density input, or a clear obstruction (∫ Φ too large).

### P3.3 — Do not use monodromy of P_X about zeros

Frozen: monodromy of zero-free P_X about a zero of ζ is not an mπ engine. Path continuation must use genuine variation of arg / discrepancy, not monodromy.

---

## 3. Interface

| Direction | Interface |
|-----------|-----------|
| 1 Density | Supplies zero-sum bounds inside Φ |
| 2 Iso_H | Not required for this bypass |
| 4 Off-line resonance | Parallel bypass |
| O-M1.3bis | Direct consumer if integral is small |

---

## 4. Status

Direction 3 open lemma restated; executable P3.1–P3.2 listed. No closure.

**Status code:** `RH_SOLID_DIR3_PATH_CONTINUATION_NEXT_2026-08-08`

*Per aspera ad astra.*
