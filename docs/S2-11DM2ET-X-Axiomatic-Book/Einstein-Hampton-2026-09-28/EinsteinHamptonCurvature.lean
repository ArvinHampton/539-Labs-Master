/-
Einstein-Hampton curvature, coordinate layer.

Mathlib already has manifolds and Riemannian metrics.
It does not ship a complete 11D Riemann plus Ricci API.
This file works on EuclideanSpace R (Fin 11) with an explicit warped metric.
-/

import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.Analysis.Calculus.ContDiff.Basic
import Mathlib.Analysis.SpecialFunctions.Exp

noncomputable section

namespace EinsteinHampton.Curvature

open Real

abbrev Idx := Fin 11

def isExt (i : Idx) : Prop := i.val ≤ 3
def isY   (i : Idx) : Prop := i.val = 4
def isFib (i : Idx) : Prop := 5 ≤ i.val

structure Warp where
  k : ℝ
  B : ℝ
  A : ℝ → ℝ
  A_lin : ∀ y, A y = k * y

def g (W : Warp) (y : ℝ) (i j : Idx) : ℝ :=
  if i ≠ j then 0
  else if i.val ≤ 3 then
    (if i.val = 0 then -1 else 1) * Real.exp (-2 * W.A y)
  else if i.val = 4 then 1
  else Real.exp (2 * W.B)

def gInv (W : Warp) (y : ℝ) (i j : Idx) : ℝ :=
  if i ≠ j then 0
  else if i.val ≤ 3 then
    (if i.val = 0 then -1 else 1) * Real.exp (2 * W.A y)
  else if i.val = 4 then 1
  else Real.exp (-2 * W.B)

def GammaY_ext (W : Warp) (y : ℝ) : ℝ := deriv W.A y
def GammaExt_Y (W : Warp) (y : ℝ) : ℝ := - deriv W.A y
def GammaY_fib (W : Warp) : ℝ := 0
def GammaFib_Y (W : Warp) : ℝ := 0

def R_ext_Y_ext_Y (W : Warp) (y : ℝ) : ℝ :=
  deriv (deriv W.A) y - (deriv W.A y) ^ 2

theorem R_ext_Y_ext_Y_of_linear (W : Warp) (y : ℝ)
    (hA : deriv W.A = fun _ => W.k)
    (hA2 : deriv (deriv W.A) = fun _ => 0) :
    R_ext_Y_ext_Y W y = - W.k ^ 2 := by
  simp [R_ext_Y_ext_Y, hA, hA2]

def FibreLockScalars (k Phi K : ℝ) : Prop :=
  k ^ 2 = Phi / 1728 ∧ K = 8 * k ^ 2

end EinsteinHampton.Curvature
