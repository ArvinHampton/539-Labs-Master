/-
  Category A only. Canonical T3 on Nat.
  No G4. No HQCC-as-physics. No 539-step free-orbit claim.
-/

namespace CatAVerify.T3

/-- Canonical T3. Integer division on each residue class. -/
def T3 (n : Nat) : Nat :=
  match n % 3 with
  | 0 => n / 3
  | 1 => (4 * n + 2) / 3
  | _ => (2 * n + 1) / 3

theorem T3_integrality (n : Nat) : ∃ m : Nat, T3 n = m :=
  ⟨T3 n, rfl⟩

theorem T3_fixedPoint_zero : T3 0 = 0 := rfl

theorem T3_cycle_one_two : T3 1 = 2 ∧ T3 2 = 1 :=
  ⟨rfl, rfl⟩

theorem T3_three : T3 3 = 1 := rfl
theorem T3_four  : T3 4 = 6 := rfl
theorem T3_five  : T3 5 = 3 := rfl

theorem T3_of_mul3 (k : Nat) : T3 (3 * k) = k := by
  have hmod : (3 * k) % 3 = 0 := Nat.mul_mod_right 3 k
  simp [T3, hmod]

theorem T3_of_residue1 (k : Nat) : T3 (3 * k + 1) = 4 * k + 2 := by
  have hmod : (3 * k + 1) % 3 = 1 := by omega
  have hexp : 4 * (3 * k + 1) + 2 = 3 * (4 * k + 2) := by omega
  simp [T3, hmod]
  rw [hexp, Nat.mul_div_right (4 * k + 2) (by decide : 0 < 3)]

theorem T3_of_residue2 (k : Nat) : T3 (3 * k + 2) = 2 * k + 1 := by
  have hmod : (3 * k + 2) % 3 = 2 := by omega
  have hexp : 2 * (3 * k + 2) + 1 = 3 * (2 * k + 1) + 2 := by omega
  simp [T3, hmod]
  have hdiv : (3 * (2 * k + 1) + 2) / 3 = 2 * k + 1 := by omega
  rw [hexp, hdiv]

/-- Finite fuel check. Not a global termination theorem. -/
def reachesSmall : Nat → Nat → Bool
  | 0, n => n ≤ 2
  | fuel + 1, n => n ≤ 2 || reachesSmall fuel (T3 n)

def allReach : Nat → Bool
  | 0 => reachesSmall 200 0
  | n + 1 => reachesSmall 400 (n + 1) && allReach n

/-- Seeds 0 through 300 reach {0,1,2} within 400 iterates. Sample only. -/
theorem finite_sample_0_to_300 : allReach 300 = true := by
  native_decide

end CatAVerify.T3
