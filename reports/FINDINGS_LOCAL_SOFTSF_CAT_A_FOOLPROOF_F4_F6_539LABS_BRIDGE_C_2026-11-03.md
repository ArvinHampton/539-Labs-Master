# FINDINGS — Local Soft SF — Cat A foolproof F4–F6 — 539 Labs corpus — Bridge C — 2026-11-03
OW 8a0325da19ba3802652a654523b681cf74a623d28a4f1a4484999420098a453b. REPORTS ONLY.
Tip: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (read-only; tip_touched NO). No CERT. Local scope only; video EXCLUDED; no nonlocal/EH 11D/PT/simulated physics. Prior FINDINGS 733db7de995eb20d9923bbcf02e765a7126e795d729a758ed4b2b5ea6ecea865 not rewritten.
Source: reports/539labs/539_Labs_Technical_Corpus.md sha 5a8f863093c6eacb57a03b74b8c3906808111fbe43f6ba9677aebae4b8f17f9e.

## F4 Π_fast — PARTIAL (factor READY; composite FALSE as stated in general)
Invent label LOC-F4-M0 (pending): on H = L²(R/G_4 Z) (or C(R/G_4 Z)), M f := G_4^{-1}∫_0^{G_4} f dt · 1, P0 := Id − M.
Lemma LOC-F4-L1 (proof, Cat A-grade elementary): M(1)=1 and M f is constant, so M²=M; hence P0² = Id − 2M + M² = P0. M is self-adjoint in L² (⟨Mf,g⟩ = G_4·mean(f)·conj mean(g)), so P0 is the orthogonal projector onto mean-zero functions. Range(M)=constants≠0 and range(P0)≠0 (e.g. sin(2πt/G_4)), so σ(P0)={0,1} exactly. ∎
Composite Π = P0∘A, A = Ad_{(ζ^t−1)∧}: on disk the symbols ζ, ∧, Ad_(ζ^t−1)∧ are undefined (INTAKE_539LABS line 13: "G_4, Ad_(ζ^t−1)∧ undefined on disk"). General claim false: counterexample LOC-F4-CX1, 2-dim model P=diag(0,1) (constant ⊕ one mean-zero mode), A=2·Id (commutes with P): (PA)^2==PA: False; eig(PA)=[np.float64(0.0), np.float64(2.0)]. So idempotence/spectrum {0,1} fails.
Sufficient condition LOC-F4-S1 (proof): if A commutes with P0 then (P0A)² = P0A² ; so P0A idempotent iff P0A²=P0A, i.e. A|range(P0) idempotent; if A invertible, iff A = Id on range(P0) (then P0A = P0). Without commutation no general statement. Status: composite needs a defined A and a proof of S1-type hypothesis — not on disk.

## F5 T_3=539 stabilization — FALSE (vs Cat A freeze) / ABSENT-with-rigor for any supporting statement
Corpus line 5: "exact topological orbits under T_3 = 539 stabilization". Cat A freeze on disk contradicts reading 539 as a T₃ dynamical quantity:
- theorems/batch-nov-dec/ADVANCEMENTS.md (sha d4ad9a72e74eeb5f6ff4e006e131084a0429c0a5b0f0cafd03025a62ea650730) L131: "Cat A freeze: free T₃ max 55 on [1,50000], seed 4880 is 14 (T₃) or 7 (charge-preserving). 539 is hash depth 18+521, not a free-map stopping time." Also L23, L244.
- theorems/batch-jan/ADVANCEMENTS.md (sha c9f946c57287780250125a2cc0ffb5e170d927ebc9fa96b95191752ffce9f9c9) L16, L366 (FAIL canonical), L558 (Cat A FAIL as free-map orbit).
- oct17-master/README.md (sha 34d3c67802edea21ce4ce444ef9342df90df97e5cf185c05f18ac00aa118aae5) L44: 539 = engineered hard budget 18+521; "Do not market free-map stopping time as 539-step hardness"; L87.
- theorems/CORPUS.md (sha cae17b42b76ea3d9b4b0118ab655842d80e8ce8c2fbc1e50d5e955422f2fcafb) L418: 539±1 chain printed, variants "not reconciled".
No Cat A statement on disk defines or proves "stabilization" under T_3; 539 is only a packaging/hash depth. Invent label LOC-F5-ABS.

## F6 C outside V_35 / polar bounds w/o cocycle vanishing — ABSENT-with-rigor
Corpus line 44 is the only plain-text occurrence of V_35 under reports/, theorems/, tip (other hits: bridges/* intake/PP files quoting the corpus; .b64 blobs = base64 byte coincidences, not text). V_35 is defined nowhere on disk. Tip uses V₄₂ (dim 42 monomial class basis, Cat B; tip L152–159, L256, L288). 35 appears only as conductor/field (Q(√35), 140th-root exponents a=35x₄+28x₅+20x₇: reports/heavy-daily/2026-10-18-Tensor-Pattern-Proof.md sha b7728d15b6b8e92d4e32b53facb9267b370f29166ed1f8acbbee7a1516cd471c L16, L54) — no space V_35, no relation V_35⊂V_42 stated. Transfer element C "leading profile" and "polar bounds": no proved statement found. Contra: PHYSICIST_RTA_BRIDGE_C_RIGOROUS_THEOREM_COUNT_2026-10-26.md (sha ae22f151bd59ca66336aff975ee5a9883f6f1846001dfdf7bffc92bf9f5a5e71) L37: cocycle vanishing only "to machine precision", uniqueness open; tip L416 P5b and L525 (A) cocycle-dimension statements are "[[ to prove / accepted ]]". Invent label LOC-F6-ABS.

## Summary
F4 PARTIAL (P0 READY; composite FALSE in general, CX1). F5 FALSE/ABSENT-with-rigor. F6 ABSENT-with-rigor.
