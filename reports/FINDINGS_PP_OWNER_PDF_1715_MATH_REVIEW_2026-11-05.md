# PP math review — Owner PDF 01M6PZWMGT7HB8CRARJ1RXF4BE (17:15 CST, 2026-11-05)
Pure-math standard (Owner 16:23). No code run. No CERT. tip untouched. Usage 88.6% at start.

## §3 K_140 / 25-prime / D1–D3 (txt L54–73, script L200–259)
- FALSE: det K_140 ≠ 0. The list contains p=7, and gcd(7·p_j,140)≥7 for every j, so row "7" is identically 0 by the document's own rule. Hence det K_140 = 0.
- INCONSISTENT definition: K is said to be the Kronecker symbol (35/·), but with p_i=p_j=3 the product is 9 → K=−1, whereas (35/9)=(35/3)²=+1. Products with residues outside {1,3,9,13,27} are set to 0, while a character would give ±1.
- GAP (non sequitur): even if det≠0, a nonsingular ±1/0 sign matrix says nothing about Gal-stable descent (D1), the height (D3), or CRT sufficiency (Π p > 2H²). D1, D2, D3 and 25-prime sufficiency remain OPEN.
- Script does not parse (`elif residue in:` has no set; indentation is broken). Its output is not evidence.
- DEFINITION/PROVED: Gal(Q(ζ49)/Q) is cyclic of order 42; conductor of Q(√35) is 140. Both correct.

## §1 Junction (L1–28)
- INCONSISTENT: imposing [K_ij]−γ_ij[K]=0 in Israel's condition ([K_ij]−γ_ij[K] = −8πG S_ij) forces S_ij=0. The document's S_ij = (…)+T^(3)_ij then requires T^(3)=0, so the condition cannot "match the 4D stress-energy".
- GAP: a hypersurface y=const of the 5D metric is 4D (coords x^μ), but Σ is written with 3 coords (t,χ,φ). The codimension is not stated, so the 4D/3D mismatch is NOT removed. "KK modes absorbed / vacuum balance follows" is asserted without derivation.
- OPEN: 𝒥_finite, R_x and a(t) are undefined; G_4 vs G_5 normalization is unstated.

## §2 3-adic S_eff (L30–52)
- DEFINITION: S_eff := 539 (a stipulation, not a derivation). "|x|_3 = 3^{-k}" is just the value set of the 3-adic norm, not a new constraint.
- Tier E input: a_μ = 11659181×10⁻¹⁰ is the muon g−2 measured value, not an arithmetic constant. κ = 1.595361 = √(2/0.7858) uses fitted Λ₀ (Tier E). The phrase "discovered by the Auditor" is a claim, not evidence.
- OPEN: P[Φ] — ∇₃ is undefined and the orbit index set is undefined (Σ 3^{539j} converges 3-adically only for j≥0). The confinement claim N−|W|=0 has no proof.

## Python / SystemVerilog / "verified" assertions
Claims only; the code was not executed per the Owner's instruction. The RTL encodes the same flawed rule.

## Remaining obligations
Gal-stable descent proof (D1); cleared integral matrix (D2); norm→Q-height bound (D3); explicit Σ codimension and bulk with T^(3) consistent with Israel; definitions of 𝒥_finite, ∇₃, the orbit set; a derivation (not a setting) of S_eff and Λ₀.
