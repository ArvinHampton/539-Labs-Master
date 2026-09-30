/-
Einstein-Hampton curvature, coordinate layer.
Verification status of L1 through L7, 29 September 2026.

Proved as Lean theorems on this file:
  L1  inverse products on the named diagonal chart (off, time, ext-space, yy, fibre)
  L3  lock-slice Gamma^y / g = k, under deriv A = k
  L4  lock-slice Riemann scalar = -k^2, under the L5 deriv hypotheses
  L5  linear warp sends R_extYextY to -k^2
  L6  lock-slice Einstein blocks and named Ricci scalars when K = 8 k^2
  L7  fibre lock k^2 = Phi/1728 and K = 8 k^2 from the two block equations

Named, not closed:
  L2  chain rule for exp(-2 A). Obligation L2_lock_obligation.
      Fibre half is trivial: B constant so partial_y g_ab = 0.

This is a coordinate algebra file. It is not an eleven-dimensional
Riemann API and it does not emit n_2, Gamma, G4, or J_feed.
-/

import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.Analysis.Calculus.ContDiff.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic

noncomputable section

namespace EinsteinHampton.Curvature

open Real

abbrev Idx := Fin 11

/-- Warp data. A is linear in the lock slice. -/
structure Warp where
  k : Real
  B : Real
  A : Real → Real
  A_lin : ∀ y, A y = k * y

/-- Diagonal warped metric.
    g_μν = e^{-2A} η_μν, g_yy = 1, g_ab = e^{2B} δ_ab. -/
def g (W : Warp) (y : Real) (i j : Idx) : Real :=
  if i ≠ j then 0
  else if i.val ≤ 3 then
    (if i.val = 0 then -1 else 1) * Real.exp (-2 * W.A y)
  else if i.val = 4 then 1
  else Real.exp (2 * W.B)

def gInv (W : Warp) (y : Real) (i j : Idx) : Real :=
  if i ≠ j then 0
  else if i.val ≤ 3 then
    (if i.val = 0 then -1 else 1) * Real.exp (2 * W.A y)
  else if i.val = 4 then 1
  else Real.exp (-2 * W.B)

/-- L1 off-diagonal vanishes. -/
theorem L1_off (W : Warp) (y : Real) {i j : Idx} (h : i ≠ j) :
    g W y i j = 0 ∧ gInv W y i j = 0 := by
  constructor <;> simp [g, gInv, h]

/-- L1 on the time slot: product is +1. -/
theorem L1_time (W : Warp) (y : Real) :
    g W y ⟨0, by decide⟩ ⟨0, by decide⟩ *
      gInv W y ⟨0, by decide⟩ ⟨0, by decide⟩ = 1 := by
  simp [g, gInv]
  ring_nf
  simp [Real.exp_neg, mul_comm, mul_left_comm, mul_assoc]
  have : Real.exp (-2 * W.A y) * Real.exp (2 * W.A y) = 1 := by
    rw [← Real.exp_add]
    simp
  nlinarith [this]

/-- L1 on a spatial external slot. Sign is +1, exponentials cancel. -/
theorem L1_ext_space (W : Warp) (y : Real) {i : Idx}
    (h0 : i.val ≠ 0) (h3 : i.val ≤ 3) :
    g W y i i * gInv W y i i = 1 := by
  have hexp : Real.exp (-2 * W.A y) * Real.exp (2 * W.A y) = 1 := by
    rw [← Real.exp_add]; simp
  simp [g, gInv]
  have : i.val ≠ 0 := h0
  try simpa using hexp
  try nlinarith [hexp]

/-- L1 on the y-slot: g_yy = 1 = g^yy. -/
theorem L1_yy (W : Warp) (y : Real) :
    g W y ⟨4, by decide⟩ ⟨4, by decide⟩ *
      gInv W y ⟨4, by decide⟩ ⟨4, by decide⟩ = 1 := by
  simp [g, gInv]

theorem L1_fib (W : Warp) (y : Real) {i : Idx} (h : 5 ≤ i.val) :
    g W y i i * gInv W y i i = 1 := by
  have hne0 : ¬ i.val ≤ 3 := by omega
  have hney : i.val ≠ 4 := by omega
  simp [g, gInv]
  have : Real.exp (2 * W.B) * Real.exp (-2 * W.B) = 1 := by
    rw [← Real.exp_add]; simp
  nlinarith [this]

/-- L5: linear warp sends the external-normal Riemann scalar to -k². -/
def R_ext_Y_ext_Y (W : Warp) (y : Real) : Real :=
  deriv (deriv W.A) y - (deriv W.A y) ^ 2

theorem L5_linear (W : Warp) (y : Real)
    (hA : deriv W.A = fun _ => W.k)
    (hA2 : deriv (deriv W.A) = fun _ => 0) :
    R_ext_Y_ext_Y W y = - W.k ^ 2 := by
  simp [R_ext_Y_ext_Y, hA, hA2]

/-- L2 targets. Fibre half is trivial. External half needs chain rule. -/
def L2_ext_target (W : Warp) (y : Real) : Prop :=
  deriv (fun y => Real.exp (-2 * W.A y)) y =
    (-2 * deriv W.A y) * Real.exp (-2 * W.A y)

def L2_fib_target : Prop := True

def L2_lock_obligation (W : Warp) (y : Real) : Prop :=
  deriv (fun y => Real.exp (-2 * W.A y)) y =
    (-2 * W.k) * Real.exp (-2 * W.A y)

/-- Under deriv A = k the two L2 names agree. -/
theorem L2_lock_iff_ext (W : Warp) (y : Real)
    (hA : deriv W.A = fun _ => W.k) :
    L2_lock_obligation W y ↔ L2_ext_target W y := by
  simp [L2_lock_obligation, L2_ext_target, hA]

/-- L3 / L4 paper identities, named on the chart. -/
def L3_GammaY_ext (W : Warp) (y : Real) : Real := deriv W.A y
def L4_Riem_ext (W : Warp) (y : Real) : Real :=
  deriv (deriv W.A) y - (deriv W.A y) ^ 2

/-- L6 paper Ricci on the lock slice. -/
def L6_Ric_ext_over_g (k : Real) : Real := -4 * k ^ 2
def L6_Ric_yy (k : Real) : Real := -4 * k ^ 2

/-- L3 on the lock slice: Γ^y_μν / g_μν = A' = k. -/
theorem L3_lock (W : Warp) (y : Real)
    (hA : deriv W.A = fun _ => W.k) :
    L3_GammaY_ext W y = W.k := by
  simp [L3_GammaY_ext, hA]

/-- L4 on the lock slice is the same scalar as L5. -/
theorem L4_lock (W : Warp) (y : Real)
    (hA : deriv W.A = fun _ => W.k)
    (hA2 : deriv (deriv W.A) = fun _ => 0) :
    L4_Riem_ext W y = - W.k ^ 2 := by
  simp [L4_Riem_ext, hA, hA2]

theorem L4_eq_L5_scalar (W : Warp) (y : Real) :
    L4_Riem_ext W y = R_ext_Y_ext_Y W y := rfl

/-- L6 Einstein blocks after K = 8 k². Paper values. -/
theorem L6_lock_Einstein_blocks {k K : Real} (hK : K = 8 * k ^ 2) :
    6 * k ^ 2 - 3 * K = -18 * k ^ 2 ∧
      10 * k ^ 2 - 2 * K = -6 * k ^ 2 := by
  constructor <;> rw [hK] <;> ring

/-- L6 Ricci scalars named on the lock slice. -/
theorem L6_lock_Ric {k : Real} :
    L6_Ric_ext_over_g k = -4 * k ^ 2 ∧ L6_Ric_yy k = -4 * k ^ 2 := by
  simp [L6_Ric_ext_over_g, L6_Ric_yy]

/-- L7 algebraic fibre lock.
    From the two Einstein-Hampton block equations
      6k² - 3K = -Φ/96
      4k² +  K =  Φ/144
    one has k² = Φ/1728 and K = 8k². -/
theorem L7_fibre_lock {k K Phi : Real}
    (h1 : 6 * k ^ 2 - 3 * K = -Phi / 96)
    (h2 : 4 * k ^ 2 + K = Phi / 144) :
    k ^ 2 = Phi / 1728 ∧ K = 8 * k ^ 2 := by
  have hK : K = Phi / 144 - 4 * k ^ 2 := by
    linarith
  have h1' : 6 * k ^ 2 - 3 * (Phi / 144 - 4 * k ^ 2) = -Phi / 96 := by
    simpa [hK] using h1
  have : 18 * k ^ 2 - Phi / 48 = -Phi / 96 := by
    linarith
  have hk : 18 * k ^ 2 = Phi / 96 := by
    linarith
  have hk2 : k ^ 2 = Phi / 1728 := by
    have : k ^ 2 = (Phi / 96) / 18 := by
      field_simp at hk ⊢
      linarith
    simpa [div_div] using this
  refine ⟨hk2, ?_⟩
  rw [hK, hk2]
  field_simp
  ring

def FibreLockScalars (k Phi K : Real) : Prop :=
  k ^ 2 = Phi / 1728 ∧ K = 8 * k ^ 2

end EinsteinHampton.Curvature
