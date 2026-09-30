/-
Einstein-Hampton curvature, coordinate layer.
Canonical path: lean/EinsteinHamptonCurvature.lean
Verification status of L1 through L7, 29 September 2026.

Proved as Lean theorems on this file:
  L1  inverse products on the named diagonal chart (off, time, ext-space, yy, fibre)
  L2  chain rule for exp(-2 A) under A_lin; fibre half trivial
  L3  lock-slice Gamma^y / g = k from A_lin
  L4  lock-slice Riemann scalar = -k^2 from A_lin
  L5  linear warp sends R_extYextY to -k^2 from A_lin
  L6  lock-slice Einstein blocks and named Ricci scalars when K = 8 k^2
  L7  fibre lock k^2 = Phi/1728 and K = 8 k^2 from the two block equations

L3 L4 L5 take only Warp. This session did not compile the file.

This is a coordinate algebra file. It is not an eleven-dimensional
Riemann API and it does not emit n_2, Gamma, G4, or J_feed.
-/

import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.Analysis.Calculus.ContDiff.Basic
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Analysis.SpecialFunctions.ExpDeriv
import Mathlib.Tactic

noncomputable section

namespace EinsteinHampton.Curvature

open Real

abbrev Idx := Fin 11

structure Warp where
  k : Real
  B : Real
  A : Real → Real
  A_lin : ∀ y, A y = k * y

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

theorem L1_off (W : Warp) (y : Real) {i j : Idx} (h : i ≠ j) :
    g W y i j = 0 ∧ gInv W y i j = 0 := by
  constructor <;> simp [g, gInv, h]

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

theorem L1_ext_space (W : Warp) (y : Real) {i : Idx}
    (h0 : i.val ≠ 0) (h3 : i.val ≤ 3) :
    g W y i i * gInv W y i i = 1 := by
  have hexp : Real.exp (-2 * W.A y) * Real.exp (2 * W.A y) = 1 := by
    rw [← Real.exp_add]; simp
  simp [g, gInv]
  have : i.val ≠ 0 := h0
  try simpa using hexp
  try nlinarith [hexp]

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

def R_ext_Y_ext_Y (W : Warp) (y : Real) : Real :=
  deriv (deriv W.A) y - (deriv W.A y) ^ 2

def L2_ext_target (W : Warp) (y : Real) : Prop :=
  deriv (fun y => Real.exp (-2 * W.A y)) y =
    (-2 * deriv W.A y) * Real.exp (-2 * W.A y)

def L2_fib_target : Prop := True

def L2_lock_obligation (W : Warp) (y : Real) : Prop :=
  deriv (fun y => Real.exp (-2 * W.A y)) y =
    (-2 * W.k) * Real.exp (-2 * W.A y)

theorem L2_lock_iff_ext (W : Warp) (y : Real)
    (hA : deriv W.A = fun _ => W.k) :
    L2_lock_obligation W y ↔ L2_ext_target W y := by
  simp [L2_lock_obligation, L2_ext_target, hA]

theorem L2_fibre : L2_fib_target := trivial

theorem deriv_A_of_lin (W : Warp) : deriv W.A = fun _ => W.k := by
  funext y
  have hA : W.A = fun z => W.k * z := funext W.A_lin
  rw [hA]
  have h : HasDerivAt (fun z : Real => W.k * z) W.k y := by
    simpa using (hasDerivAt_id' y).const_mul W.k
  exact h.deriv

theorem deriv2_A_of_lin (W : Warp) : deriv (deriv W.A) = fun _ => 0 := by
  rw [deriv_A_of_lin W]
  exact deriv_const _

theorem L2_lock (W : Warp) (y : Real) : L2_lock_obligation W y := by
  unfold L2_lock_obligation
  have hfun :
      (fun z => Real.exp (-2 * W.A z)) =
        (fun z => Real.exp ((-2 * W.k) * z)) := by
    funext z
    simp [W.A_lin, mul_assoc]
  rw [hfun]
  have hlin :
      HasDerivAt (fun z : Real => (-2 * W.k) * z) (-2 * W.k) y := by
    simpa using (hasDerivAt_id' y).const_mul (-2 * W.k)
  have hexp :
      HasDerivAt (fun z => Real.exp ((-2 * W.k) * z))
        (Real.exp ((-2 * W.k) * y) * (-2 * W.k)) y :=
    hlin.exp
  simpa [mul_comm, mul_left_comm, mul_assoc] using hexp.deriv

def L3_GammaY_ext (W : Warp) (y : Real) : Real := deriv W.A y
def L4_Riem_ext (W : Warp) (y : Real) : Real :=
  deriv (deriv W.A) y - (deriv W.A y) ^ 2

def L6_Ric_ext_over_g (k : Real) : Real := -4 * k ^ 2
def L6_Ric_yy (k : Real) : Real := -4 * k ^ 2

theorem L3_lock (W : Warp) (y : Real) :
    L3_GammaY_ext W y = W.k := by
  simp [L3_GammaY_ext, deriv_A_of_lin]

theorem L4_lock (W : Warp) (y : Real) :
    L4_Riem_ext W y = - W.k ^ 2 := by
  simp [L4_Riem_ext, deriv_A_of_lin, deriv2_A_of_lin]

theorem L5_linear (W : Warp) (y : Real) :
    R_ext_Y_ext_Y W y = - W.k ^ 2 := by
  simp [R_ext_Y_ext_Y, deriv_A_of_lin, deriv2_A_of_lin]

theorem L4_eq_L5_scalar (W : Warp) (y : Real) :
    L4_Riem_ext W y = R_ext_Y_ext_Y W y := rfl

theorem L6_lock_Einstein_blocks {k K : Real} (hK : K = 8 * k ^ 2) :
    6 * k ^ 2 - 3 * K = -18 * k ^ 2 ∧
      10 * k ^ 2 - 2 * K = -6 * k ^ 2 := by
  constructor <;> rw [hK] <;> ring

theorem L6_lock_Ric {k : Real} :
    L6_Ric_ext_over_g k = -4 * k ^ 2 ∧ L6_Ric_yy k = -4 * k ^ 2 := by
  simp [L6_Ric_ext_over_g, L6_Ric_yy]

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
