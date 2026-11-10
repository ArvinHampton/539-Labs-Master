# PROOF — Idempotent spectrum lemma; status of corpus Π_fast (2026-11-03)
REPORTS ONLY. No CERT. Video excluded.

## Lemma (PROVED). Let P be a linear operator on a finite-dim space V over ℝ or ℂ with P² = P.
(a) spec P ⊆ {0,1}: Pv=λv, v≠0 ⇒ λv = P²v = λ²v ⇒ λ∈{0,1}.
(b) Diagonalizable: minimal polynomial divides x(x−1), which has distinct roots ⇒ diagonalizable; V = ker P ⊕ im P (v = (v−Pv)+Pv; v∈ker∩im ⇒ v=Pv=P²... v=Pw ⇒ Pv=Pw=v, and Pv=0 ⇒ v=0).
(c) On an inner-product space, P is an orthogonal projection (im P ⊥ ker P) ⇔ P = P* (real: symmetric). (⇐) ⟨Px,(I−P)y⟩ = ⟨x,(P−P²)y⟩ = 0. (⇒) if im ⊥ ker, ⟨Px,y⟩ = ⟨Px,Py⟩ = ⟨x,Py⟩. ∎
Remark: spec ⊆ {0,1} does NOT imply idempotent (e.g. [[1,1],[0,1]] or [[0,1],[0,0]]). So "Spectrum: formally bounded within {0,1}" in the corpus is a consequence, not a definition.
Infinite-dim: (a) holds for point spectrum; full spectrum ⊆{0,1} for bounded idempotents ((P−λ)^{-1} = −λ^{-1}(I−P) + (1−λ)^{-1}P for λ∉{0,1}).

## Corpus Π_fast (539_Labs_Technical_Corpus.md L8–L10)
"idempotent projectry operator: Π_fast = (Id − G_4^{-1}∫_0^{G_4} · dt) ∘ Ad_{(ζ^t − 1)∧}"
- A f := G_4^{-1}∫_0^{G_4} f dt (as constant function) is idempotent on L¹([0,G_4]) (A of a constant is the constant). Hence Q := Id − A is idempotent (Q² = I − 2A + A² = Q). PROVED.
- Ad_{(ζ^t − 1)∧}: ζ, the wedge "∧", the algebra being Ad-acted on, and the space Π_fast acts on are NOT defined in the corpus or in DEFINITIONS*.md/THEOREMS.md (rg "fast" no hit). Π_fast = Q∘B is idempotent iff QBQB = QB; this holds e.g. if B=Id or B commutes with Q and is idempotent; fails in general (B = 2·Id ⇒ (QB)² = 4Q ≠ 2Q). Since Ad of an invertible element is invertible, and an invertible idempotent is Id, Q∘Ad_g is idempotent iff it is ... not automatic. Status: invented pending mathematical proof (definition missing).
