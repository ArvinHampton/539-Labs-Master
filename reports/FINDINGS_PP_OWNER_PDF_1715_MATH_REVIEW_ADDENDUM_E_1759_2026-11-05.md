# ADDENDUM E — Owner 17:59 Σq / graph-energy theorem (same review; exact analytic checks; No CERT)
## Lemma "Σq(t)=0 iff q driven by Π_fast"
- Σ_x(LΦ)_x=0 always (column sums of L vanish) — PROVED; this is a SPATIAL condition at each t.
- ∫Ad dt=0 ⇒ ∫Σq dt=0 is a TEMPORAL mean; it does not give Σq(t)=0 at each t. Π_fast=(Id−time avg)∘Ad zeroes the mean of the OUTPUT, not of raw Ad.
- Counterexample (⇒ fails): T>0, s=sin(2πt/T), q=(s,s): each component has zero temporal mean, but Σq=2s≠0 for t∉{0,T/2,T}; LΦ=q has no solution there.
- Counterexample (⇐ fails): q=(1,−1) constant: Σq=0 at every t, temporal mean ≠0. "iff" FALSE both directions.
- Repair, PROVED: q=Bj (B = incidence matrix, j any edge flux) ⇒ Σq=0 for every t. That this is the project's q needs proof (potential/flux consistency, boundary support): OPEN.
## Theorem "∫(N−|W|)=∫ΦLΦ=0"
- Algebra PROVED: E=ΦᵀLΦ=Σ_xΦ_x²Σ_y w_xy − Σ_{x,y}w_xyΦ_xΦ_y = Σ_edges w(Φx−Φy)² ≥ 0.
- Counterexample A: 2 nodes, w=1, q=(s,−s), Φ=(s/2,−s/2): LΦ=q, Σq=0 each t, each q_x has zero temporal mean, E=s², ∫_0^T E dt=T/2>0.
- Counterexample B (non-empty interior): path 1–2–3, w=1, q=(s,0,−s), Φ=(s,0,−s): LΦ=q, node 2 harmonic, both balances hold, E=2s², ∫_0^T E=T>0.
- Hence "interior harmonic + balanced q ⇒ ∫ΦLΦ=0" is FALSE. In fact ∫E=0 ⇔ Φ(t) constant for a.e. t ⇔ q≡0 a.e.
- First term = N paths, cross term = Σdet ρ(h_i): UNPROVED. Scaling Φ→cΦ multiplies the cross term by c² while det ρ(h_i) is fixed, so the identity needs a stated normalization. A time average gives no operator inversion.
- |W| ≤ ∏‖h_i‖₁ = spr(ρ(|T|)): asserted, not derived (GAP).
## Status of the original N and W: OPEN (not refuted) — the energy counterexamples refute only the claimed vanishing.
Minimal mapping obligations:
(1) explicit map group-ring h_i=Σ_c a_{i,c}[c] → real symmetric positive conductances w_xy;
(2) normalization of vertex potentials Φ;
(3) the heat kernel or time operator and the type of Ad_(ζ^t−1)∧;
(4) a proof that the original path count equals the degree term and |W| the cross term;
(5) a derivation of the |W| bound.
The geometry ledger stays LOCKED and is not advanced by this.
