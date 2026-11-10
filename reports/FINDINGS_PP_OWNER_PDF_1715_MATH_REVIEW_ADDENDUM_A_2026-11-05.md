# ADDENDUM A to FINDINGS_PP_OWNER_PDF_1715_MATH_REVIEW (base sha 17ab357b…) — additive clarification, same review
Scope: same PDF review under 90% exception. No code, no fan-out, No CERT, tip untouched.

## A1. §1 junction — QUALIFIED
- Zero Israel LHS ([K_ij]−γ_ij[K]=0) forces S_ij=T_ij=0. This contradicts ONLY a stated requirement that the source be nonzero; the zero-source (vacuum) junction is consistent. Regrade: "incompatible stated conditions", NOT "no junction possible".
- PDF pp13–14 (Theorem 1) does nonzero-source matching: K^±=∓kγ, [K_ij]=−2kγ_ij, [K]=−6k (using dim Σ=3), LHS=4kγ_ij, T^(3)=(k/2πG₄)γ_ij. Arithmetic CORRECT given dim Σ=3.
- Remaining issues: (a) GAP/INCONSISTENT: metric e^{−2k|y|}γ_ij dx^i dx^j+dy² in a 5D bulk makes y=0 a 4D slice; then [K]=−8k and LHS=6kγ_ij. dim Σ=3 needs a 4D bulk or a stated extra-dimension reduction. (b) Conservation ∇^iT_ij=0 follows from metric compatibility alone (T ∝ γ, tension-type); the stated "iff Weyl contributions vanish symmetrically" is NOT proved — the "only if" direction is unsupported (GAP). (c) "maps homeomorphically" is undefined wording, not a step.

## A2. §2/§3 constants and ∇₃ — QUALIFIED
- Under the pure-math rule, measured/fitted provenance (a_μ, Λ₀, κ=1.595361…) does NOT refute a stipulated constant. Relabel: "external input / source claim (Tier E, separate)", not a rejection criterion. As math they are stipulated parameters (DEFINITION).
- pp15–16 DO give ∇₃Φ(x)=(Φ(x)−Φ(x′))/|x−x′|₃ with x′ the immediate ancestral node. Withdraw "∇₃ undefined". Missing specifications (GAP): which tree (Bruhat–Tits/coset tree of ℤ₃ with layer index k) and how a point x∈ℤ₃ is assigned an ancestor (x is a leaf/end, not a node — need Φ on vertices or a coset-averaging rule); the function space of Φ (locally constant? L²(ℤ₃,μ₃)?); and the layer-sum identity Σ3^k·3^{−2k}|ΔΦ_k|² needs |·|₃² of a real-valued difference defined (|·|₃ is on ℚ₃, Φ̂ values unspecified). Orbit index set still undefined; Lemma 1 confinement still OPEN (W/N step not derived).

## Unchanged
- §3 K_140: exact singularity refutation STANDS (row p=7 zero ⇒ det=0; K(3,3)=−1 vs (35/9)=+1 inconsistent).
- No inference about actual 25-prime insufficiency: that remains OPEN.
- Gal(ℚ(ζ₄₉)/ℚ) cyclic of order 42 and conductor 140 remain correct.
