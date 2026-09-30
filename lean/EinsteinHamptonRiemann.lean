/-
Coordinate Riemann of the Einstein-Hampton Warp ansatz.

This file is the next layer after the Christoffel lock.
It is not Mathlib.Geometry.Manifold and it is not an
eleven-dimensional Riemann API. It names the one nonzero
external-normal Riemann scalar of this chart and proves
it equals k^2 on the lock slice.

Does not emit n_2, Gamma, G4, or J_feed.
-/

import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Tactic

noncomputable section

namespace EinsteinHampton.Riemann

open Real

structure Warp where
  k : Real
  B : Real
  A : Real → Real
  A_lin : ∀ y, A y = k * y

theorem deriv_A_of_lin (W : Warp) : deriv W.A = fun _ => W.k := by
  funext y
  have hA : W.A = fun z => W.k * z := funext W.A_lin
  rw [hA]
  have h : HasDerivAt (fun z : Real => W.k * z) W.k y := by
    simpa using (hasDerivAt_id' y).const_mul W.k
  exact h.deriv

theorem deriv2_A_of_lin (W : Warp) : deriv (deriv W.A) = fun _ => (0 : Real) := by
  funext y
  rw [deriv_A_of_lin W]
  exact (hasDerivAt_const (F := Real) y W.k).deriv

def Gamma_y_over_g_ext (W : Warp) (y : Real) : Real := deriv W.A y

def Gamma_ext_y (W : Warp) (y : Real) : Real := - deriv W.A y

def R_ext_y_ext_y (W : Warp) (y : Real) : Real :=
  deriv (Gamma_ext_y W) y + (deriv W.A y) ^ 2

def L4_Riem_ext (W : Warp) (y : Real) : Real :=
  deriv (deriv W.A) y - (deriv W.A y) ^ 2

theorem Gamma_y_over_g_ext_lock (W : Warp) (y : Real) :
    Gamma_y_over_g_ext W y = W.k := by
  simp [Gamma_y_over_g_ext, deriv_A_of_lin]

theorem Gamma_ext_y_lock (W : Warp) (y : Real) :
    Gamma_ext_y W y = -W.k := by
  simp [Gamma_ext_y, deriv_A_of_lin]

theorem R_ext_y_ext_y_lock (W : Warp) (y : Real) :
    R_ext_y_ext_y W y = W.k ^ 2 := by
  simp [R_ext_y_ext_y, Gamma_ext_y, deriv_A_of_lin, deriv2_A_of_lin]

theorem L4_lock (W : Warp) (y : Real) :
    L4_Riem_ext W y = - W.k ^ 2 := by
  simp [L4_Riem_ext, deriv_A_of_lin, deriv2_A_of_lin]

theorem R_neg_L4 (W : Warp) (y : Real) :
    R_ext_y_ext_y W y = - L4_Riem_ext W y := by
  rw [R_ext_y_ext_y_lock, L4_lock]
  ring

end EinsteinHampton.Riemann
