# ADDENDUM N — Owner t4108 CRT character coordinates (relay-based; bounded; No CERT; no .tex)

## CRT table
- Setup: U140 ≅ U4 × U5 × U7, with generators 3 mod 4, 2 mod 5 and 3 mod 7. The orders are 2, 4 and 6, and 3 is a primitive root mod 7.
- All 11 tuples were VERIFIED exactly:
  - 3:(1,3,1)
  - 11:(1,0,4)
  - 37:(0,1,2)
  - 41:(0,0,3)
  - 47:(1,1,5)
  - 53:(0,3,4)
  - 61:(0,0,5)
  - 71:(1,0,0)
  - 79:(1,2,2)
  - 83:(1,3,3)
  - 89:(0,2,5)

## Characters and the expansion
- Characters: χ_abc(p) = (−1)^{ax} i^{by} ω^{cz}, where ω = (1+√−3)/2 is a primitive 6th root of unity. There are 48 characters, (a,b,c) ∈ Z2 × Z4 × Z6.
- The expansion λ_i(χ_abc) = Σ_{p∈K90} α_{i,p} · (−1)^{a x_p} i^{b y_p} ω^{c z_p} has exactly 11 terms. This is VALID provided the reindexing from α_{i,k} to α_{i,p} (by prime subscript) is declared.

## Eigenvalue field
- The claimed field "intersection Q(√35, √−3)" is WRONG: it omits i.
- The uniform splitting field is L = F(i, ω) = F(ζ12). With F = Q(√35), L = Q(√35, i, √3), which has degree 8 over Q and degree 4 over F.
- Witness: α_37 = 1 (all other α = 0) in sector (0,1,0) gives λ = i^{1} = i, and i ∉ F(√−3).
- Each individual eigenvalue may lie in a proper subfield, so the eigenvalues need not generate L.

## Cascade rank
- rank P = #{χ : τ(χ) ≠ 0}, where τ = Π_i λ_i. This is an exact count, not a numerical tolerance.
- A zero eigenvalue in one layer zeroes that sector's τ. It removes nothing that was not already absent.
- The transfer maps alone give no uniqueness at the boundary. That still needs Addendum M's criterion.

## η = χ140 (PROVED)
- η = χ_{1,2,3} = (−1)^{x+y+z}, using i² = −1 and ω³ = −1.
- Every one of the 11 tuples has an odd coordinate sum (verified), so η(p) = −1 for all of them. This is consistent with Addendum L.
- It follows that λ_i(χη) = −λ_i(χ), and therefore τ(χη) = (−1)^M τ(χ).
- The pairing χ ↔ χη has no fixed points (η ≠ 1), so the 48 characters fall into 24 pairs whose |τ| values are equal. Hence rank P is EVEN.

## Correction to Addendum M
- My line 12 ("labels must be sets") was too strong.
- A single label Ω_k is a valid row. What is needed is that the ordered family of rows covers the intended set, together with nonzero weights and enough rank.

## OPEN
- The physical choice of α, Ω and Λ.
- The N/W/capacity link.
- No 48×11 table was printed.
