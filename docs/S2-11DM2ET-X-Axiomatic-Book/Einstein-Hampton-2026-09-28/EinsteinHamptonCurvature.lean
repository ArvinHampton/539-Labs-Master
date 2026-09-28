/-
Coordinate layer. L1 pieces, L5, and L7 algebraic lock are the proved statements.
L2-L4 and L6 remain named paper identities pending HasDerivAt and index contraction.
-/
import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Tactic
noncomputable section
namespace EinsteinHampton.Curvature
open Real
theorem L7_fibre_lock {k K Phi : Real}
    (h1 : 6 * k ^ 2 - 3 * K = -Phi / 96)
    (h2 : 4 * k ^ 2 + K = Phi / 144) :
    k ^ 2 = Phi / 1728 ∧ K = 8 * k ^ 2 := by
  have hK : K = Phi / 144 - 4 * k ^ 2 := by linarith
  have : 18 * k ^ 2 - Phi / 48 = -Phi / 96 := by
    have h1' : 6 * k ^ 2 - 3 * (Phi / 144 - 4 * k ^ 2) = -Phi / 96 := by simpa [hK] using h1
    linarith
  have hk : 18 * k ^ 2 = Phi / 96 := by linarith
  have hk2 : k ^ 2 = Phi / 1728 := by
    have : k ^ 2 = (Phi / 96) / 18 := by field_simp at hk ⊢; linarith
    simpa [div_div] using this
  refine ⟨hk2, ?_⟩
  rw [hK, hk2]; field_simp; ring
end EinsteinHampton.Curvature
