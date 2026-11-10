# PREREG order25 — exact Γ_γ facts; RG15 (anti-invariant piece); RG16 (defect split)
Written 2026-10-24 (America/Chicago) BEFORE any order25 numerics. CORE_FREEZE. MAPS_CANDIDATES untouched; no Resonant objects. Inputs read-only: order18 a2_arrays.npz (CO, SCO); symbols.py (exact S_rows exponents, reduce). k := 35^{−1/2}; L = 9800, ζ = e(1/L).

## 1. Exact check (Category A target)
Γ_γ is monomial: (Γ_γ)_{j,π(j)} = ζ^{g_j} from reduce(γα_j, γβ_j) (exact Fraction arithmetic, exponents mod L).
- E1: Γ_γ² = I ⇔ π∘π = id and g_j + g_{π(j)} ≡ 0 (mod L) for all j.
- E2: [Γ_γ, M] = 0 where M_{jk} = Σ_{e∈S(j,k)} ζ^e (S = exponent multisets from S_rows). (Γ M)_{jk} = Σ_{e∈S(π j,k)} ζ^{g_j+e}; (M Γ)_{jk} = Σ_{e∈S(j,π⁻¹k)} ζ^{e+g_{π⁻¹k}}. Check: equality of these exponent multisets mod L for every (j,k). Equality of multisets is sufficient for equality in Z[ζ] (exact). If some multiset pair differs, fall back to the 3360-embedding certificate of paper Prop. M2 and report.
PASS = all identities exact.

## 2. Exact identities used (Category A, written now)
Since Γ_γ is a unitary involution (E1), P_± = (I ± Γ_γ)/2 are complementary orthogonal projectors; by order24 rank P_+ = 60, rank P_− = 45. With row-vector data (rows = points), Y_± := CO·P_±ᵀ. By v8 Prop. transport, CO·Γ_γᵀ = Cor_{γ⁻¹K}, so Y_− = ½(Cor_K − Cor_{γ⁻¹K}) = −½D (D = RG13 γ-defect). If E2 holds, the law residual R(Y) = Y(−1/x) − x kM Y(x) satisfies R(Y_±) = R(CO)·P_±ᵀ and ‖R(CO)‖² = ‖R(Y_+)‖² + ‖R(Y_−)‖².
Disclosure: from order24, ‖R(Y_+)‖ = 15.90 (RG14) and ‖R(D)‖ = 104.06 (RG13) are already known; the predictions below follow from them and are therefore consistency checks, not blind tests.

## 3. Map RG15 (anti-invariant piece)
Y_− against the law Y(−1/x) = x kM Y(x). Absolute metric a = ‖R(Y_−)‖_F. Non-vacuity ‖Y_−‖_F ≥ 1e−3‖CO‖_F. PASS iff a ≤ 1e−8; FAIL iff a ≥ 1e−3‖Y_−(−1/x)‖_F. Predicted: FAIL with a = ½·104.06 = 52.03 (±1e−9); identity check Y_− = −½D to ≤ 1e−12.
Exact geometric law of Y_− (stated): Γ_γ Y_− = −Y_− (anti-invariance) and Y_− = ½(Cor_K − Cor_{γ⁻¹K}); check ≤ 1e−12.

## 4. Map RG16 (where the defect lives)
Statement: the defect is NOT entirely in P_+: share_− := ‖R(Y_−)‖²/‖R(CO)‖² satisfies share_− ≥ 0.5 (most of the defect is anti-invariant). Predicted share_− = 52.03²/54.41² ≈ 0.915. Also check the Pythagoras identity to 1e−9 relative. PASS iff share_− ≥ 0.5 and Pythagoras holds; FAIL iff share_− < 0.5.
Any pass is residual-internal, not a bridge. E1–E3 OPEN.
nice, OMP_NUM_THREADS=1, <3 GB; no push/sends; new files only.
