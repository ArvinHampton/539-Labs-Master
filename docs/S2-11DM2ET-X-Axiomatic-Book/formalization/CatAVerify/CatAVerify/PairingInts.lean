/-
  Locked pairing integers recorded as Nat identities.
  The sector-band dictionary that interprets these counts stays Category B.
  Not a master equation. Not a fifth-order series theorem.
-/

namespace CatAVerify.PairingInts

def Sigma     : Nat := 8676
def Sigma_win : Nat := 252
def Sigma_tow : Nat := 8424

theorem pairing_sum : Sigma_win + Sigma_tow = Sigma := rfl

theorem pairing_sum_eval : 252 + 8424 = 8676 := rfl

theorem edge_split_17_521 : 17 + 521 = 538 := rfl

theorem edge_split_is_B_minus_one : 17 + 521 = 539 - 1 := rfl

end CatAVerify.PairingInts
