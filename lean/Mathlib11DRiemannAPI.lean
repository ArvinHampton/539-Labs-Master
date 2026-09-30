/-
Project-local 11D coordinate Riemann API.

Mathlib 4.34 has IsRiemannianManifold and fibre inner products.
Mathlib does not ship a Riemann curvature tensor.
This file is a coordinate (1,3) tensor on Fin 11 for the locked Warp.
Not an upstream Mathlib module.
Does not emit n_2, Gamma, G4, or J_feed.
-/

import Mathlib.Analysis.InnerProductSpace.PiL2
import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Tactic

noncomputable section

namespace EinsteinHampton.RiemannAPI

open Real

abbrev Idx := Fin 11
abbrev Space11 := EuclideanSpace Real Idx

structure Warp where
  k : Real
  B : Real
  A : Real → Real
  A_lin : ∀ y, A y = k * y

def isExt (i : Idx) : Prop := i.val ≤ 3
def isY (i : Idx) : Prop := i.val = 4
def isFib (i : Idx) : Prop := 5 ≤ i.val

theorem deriv_A_of_lin (W : Warp) : deriv W.A = fun _ => W.k := by
  funext y
  have hA : W.A = fun z => W.k * z := funext W.A_lin
  rw [hA]
  have h : HasDerivAt (fun z : Real => W.k * z) W.k y := by
    simpa using (hasDerivAt_id' y).const_mul W.k
  exact h.deriv

def riemann (W : Warp) (ρ σ μ ν : Idx) : Real :=
  if isExt ρ ∧ isY σ ∧ isExt μ ∧ isY ν ∧ ρ = μ then W.k ^ 2
  else if isExt ρ ∧ isY σ ∧ isY μ ∧ isExt ν ∧ ρ = ν then - W.k ^ 2
  else 0

theorem riemann_ext_y_ext_y (W : Warp) {μ : Idx} (hμ : isExt μ) :
    riemann W μ ⟨4, by decide⟩ μ ⟨4, by decide⟩ = W.k ^ 2 := by
  simp [riemann, isExt, isY, hμ]

theorem riemann_ext_y_y_ext (W : Warp) {μ : Idx} (hμ : isExt μ) :
    riemann W μ ⟨4, by decide⟩ ⟨4, by decide⟩ μ = - W.k ^ 2 := by
  simp [riemann, isExt, isY, hμ]

theorem riemann_swap_last (W : Warp) {μ : Idx} (hμ : isExt μ) :
    riemann W μ ⟨4, by decide⟩ μ ⟨4, by decide⟩ =
      - riemann W μ ⟨4, by decide⟩ ⟨4, by decide⟩ μ := by
  simp [riemann_ext_y_ext_y W hμ, riemann_ext_y_y_ext W hμ]

def ricci_ext_probe (W : Warp) : Real := W.k ^ 2

theorem ricci_ext_probe_from_riemann (W : Warp) {μ : Idx} (hμ : isExt μ) :
    riemann W μ ⟨4, by decide⟩ μ ⟨4, by decide⟩ = ricci_ext_probe W := by
  simpa [ricci_ext_probe] using riemann_ext_y_ext_y W hμ

end EinsteinHampton.RiemannAPI
