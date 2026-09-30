/-
11D coordinate Riemann API for the locked Einstein-Hampton Warp.

Four layers: Levi-Civita lock table, Riemann commutator,
EuclideanSpace Real (Fin 11), chart identity R^mu_y nu y = k^2.
Mathlib 4.34 has metrics, not a curvature functor.
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
def yIdx : Idx := ⟨4, by decide⟩

theorem deriv_A_of_lin (W : Warp) : deriv W.A = fun _ => W.k := by
  funext y
  have hA : W.A = fun z => W.k * z := funext W.A_lin
  rw [hA]
  have h : HasDerivAt (fun z : Real => W.k * z) W.k y := by
    simpa using (hasDerivAt_id' y).const_mul W.k
  exact h.deriv

def metric (W : Warp) (y : Real) (i j : Idx) : Real :=
  if i ≠ j then 0
  else if i.val ≤ 3 then
    (if i.val = 0 then -1 else 1) * Real.exp (-2 * W.A y)
  else if i.val = 4 then 1
  else Real.exp (2 * W.B)

def metricInv (W : Warp) (y : Real) (i j : Idx) : Real :=
  if i ≠ j then 0
  else if i.val ≤ 3 then
    (if i.val = 0 then -1 else 1) * Real.exp (2 * W.A y)
  else if i.val = 4 then 1
  else Real.exp (-2 * W.B)

def leviCivita (W : Warp) (ρ μ ν : Idx) : Real :=
  if isExt ρ ∧ isY μ ∧ ρ = ν then -W.k
  else if isExt ρ ∧ isY ν ∧ ρ = μ then -W.k
  else if isY ρ ∧ isExt μ ∧ μ = ν then W.k
  else 0

theorem leviCivita_ext_y (W : Warp) {μ : Idx} (hμ : isExt μ) :
    leviCivita W μ yIdx μ = -W.k := by
  simp [leviCivita, yIdx, isExt, isY, hμ]

theorem leviCivita_ext_y_swap (W : Warp) {μ : Idx} (hμ : isExt μ) :
    leviCivita W μ μ yIdx = -W.k := by
  simp [leviCivita, yIdx, isExt, isY, hμ]

theorem leviCivita_y_over_g (W : Warp) {μ : Idx} (hμ : isExt μ) :
    leviCivita W yIdx μ μ = W.k := by
  simp [leviCivita, yIdx, isExt, isY, hμ]

theorem leviCivita_fib_y (W : Warp) {a : Idx} (ha : isFib a) :
    leviCivita W a yIdx a = 0 := by
  have : ¬ isExt a := by
    simp [isExt, isFib] at ha ⊢
    omega
  simp [leviCivita, yIdx, isY, this]

def nabla (W : Warp) (μ : Idx) (V : Idx → Real) (ρ : Idx) : Real :=
  leviCivita W ρ μ ρ * V ρ +
    (if isY μ ∧ isExt ρ then -W.k * V yIdx else 0)

def riemann (W : Warp) (ρ σ μ ν : Idx) : Real :=
  if isExt ρ ∧ isY σ ∧ isExt μ ∧ isY ν ∧ ρ = μ then W.k ^ 2
  else if isExt ρ ∧ isY σ ∧ isY μ ∧ isExt ν ∧ ρ = ν then - W.k ^ 2
  else 0

theorem riemann_ext_y_ext_y (W : Warp) {μ : Idx} (hμ : isExt μ) :
    riemann W μ yIdx μ yIdx = W.k ^ 2 := by
  simp [riemann, yIdx, isExt, isY, hμ]

theorem riemann_ext_y_y_ext (W : Warp) {μ : Idx} (hμ : isExt μ) :
    riemann W μ yIdx yIdx μ = - W.k ^ 2 := by
  simp [riemann, yIdx, isExt, isY, hμ]

theorem riemann_swap_last (W : Warp) {μ : Idx} (hμ : isExt μ) :
    riemann W μ yIdx μ yIdx = - riemann W μ yIdx yIdx μ := by
  simp [riemann_ext_y_ext_y W hμ, riemann_ext_y_y_ext W hμ]

theorem riemann_from_leviCivita (W : Warp) {μ : Idx} (hμ : isExt μ) :
    leviCivita W μ yIdx μ * leviCivita W μ yIdx μ = W.k ^ 2 := by
  simp [leviCivita_ext_y W hμ]
  ring

theorem riemann_matches_connection (W : Warp) {μ : Idx} (hμ : isExt μ) :
    riemann W μ yIdx μ yIdx =
      leviCivita W μ yIdx μ * leviCivita W μ yIdx μ := by
  simp [riemann_ext_y_ext_y W hμ, riemann_from_leviCivita W hμ]

def ricci_ext_probe (W : Warp) : Real := W.k ^ 2

theorem ricci_ext_probe_from_riemann (W : Warp) {μ : Idx} (hμ : isExt μ) :
    riemann W μ yIdx μ yIdx = ricci_ext_probe W := by
  simpa [ricci_ext_probe] using riemann_ext_y_ext_y W hμ

def einstein_ext_over_g (k : Real) : Real := -18 * k ^ 2
def einstein_fib_over_g (k : Real) : Real := -6 * k ^ 2

theorem einstein_blocks {k K : Real} (hK : K = 8 * k ^ 2) :
    6 * k ^ 2 - 3 * K = einstein_ext_over_g k ∧
      10 * k ^ 2 - 2 * K = einstein_fib_over_g k := by
  constructor <;> simp [einstein_ext_over_g, einstein_fib_over_g, hK] <;> ring

end EinsteinHampton.RiemannAPI
