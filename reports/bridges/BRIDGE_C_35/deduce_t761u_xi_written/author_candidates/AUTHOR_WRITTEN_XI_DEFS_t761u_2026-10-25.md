# AUTHOR-WRITTEN CANDIDATE — Ξ-chain definitions (t761u authority) — NOT Cat A, NOT DEDUCED
Status: DRAFT awaiting Arvin ACCEPT (menu below) + Auditor CONFIRM. Ledger form (7dbd63af… L37/L40):
Ξ_s(q) = Σ_{k∈ℤ} χ_s(k) q^{-35k²/4-7k/2} ϑ_s(q; n+7k/2), s∈{even,odd}; Q_7(n,k)=(n+7k/2)²-35k²/4-7k/2 (L33).

## Supporting arithmetic (DEDUCED, logs/exponent_parity_check.log)
For k=2m (m≥0): -35k²/4-7k/2 = -(35m²+7m) = -outer_even(m); characteristic 7k/2=7m.
For k=2m+1 (m≥0): exponent = -(35m²+42m+49/4) = -outer_odd(m); characteristic 7m+7/2.
outer_* forms as Written in e60cad9b… L16–22 / 1bab65c4… L16–18 (cited via t713u RESULTS L5); characteristics match HD 552541cf L20–22. k<0 terms are NOT of this form.

## AW-1  χ_even(k), χ_odd(k)  [recommended pick AW-1a]
- AW-1a (parity indicator, k≥0): χ_even(k)=1 if k≥0 and k≡0 mod 2, else 0; χ_odd(k)=1 if k≥0 and k≡1 mod 2, else 0.
  Rationale: unique choice making ledger "even/odd" = k-parity (X4 item iii) and matching HD characteristics 7m, 7m+7/2; kills k<0 (X4 item i folding not needed).
- AW-1b (parity indicator, all k∈ℤ): same parity, no k≥0 cut. Gap: k<0 terms not matched to any Written outer_*.
- AW-1c (character): χ_s = a Dirichlet/genus character mod 35 (MISSED_VARS L9 reading "characters"). Gap: no Written character supplied; NOT recommended (would need further supply).
- Gap flag G-1: t713u cites outer_even for m≥1; AW-1a includes k=0 (m=0, exponent 0). Sub-pick: AW-1a-0 include k=0 [recommended, ledger sum has k=0] / AW-1a-1 exclude k=0 (χ_even(0)=0).

## AW-2  ϑ_even(q;z), ϑ_odd(q;z)  [recommended AW-2a]
- AW-2a: ϑ_even(q;z)=ϑ_odd(q;z)=ϑ(q;z):=Σ_{j≥0} (j+z) q^{(j+z)²}  (partial weight-3/2 unary theta; HD L24 Θ_{3/2}(·;a)=Σ(n+a)q^{(n+a)²} plain form; j≥0 since full-ℤ sum vanishes for z∈½ℤ, t713u PREREG L22 reading).
- AW-2b: "χ-twisted analogue" (HD L24 alternative) — form not Written; would need twist supply. Not recommended.
- Gap flag G-2 (sign/normalization): with AW-1a+AW-2a+n, Ξ_s carries q^{-outer}·ϑ(q;n+a); HD product form carries outer(m) as q^{+outer}·Θ_{3/2}(·;a) (t713u reading). Ledger↔HD equality is NOT claimed here (that is X4, separate). Q_7 completed-square: q^{-35k²/4-7k/2}·q^{(j+n+7k/2)²} = q^{Q_7(n+j,k)} — so under AW-2a, Ξ_s = Σ_k χ_s(k) Σ_{j≥0}(j+n+7k/2) q^{Q_7(n+j,k)}, consistent with ledger Q_7.

## AW-3  n  [recommended AW-3a]
- AW-3a: n is the ϑ-offset (shift of summation start), fixed parameter; the locked specialization is n=1 (ledger L44–49). Equivalently ϑ(q;1+7k/2)=Σ_{j≥1}(j+7k/2)q^{(j+7k/2)²}.
- AW-3b: n free (family in n), n=1 displayed only. Gap: no Written use of other n.

## AW-4  N_trunc  [menu; recommended AW-4a]
- AW-4a: N_trunc = 106 (q-exponent ν ≤ 106 truncation of Ξ_N; Θ_third landmark, last listed degree 736cfd72/1bab65c4; precedent t713u PREREG P5 under t713s4497 ACCEPT defaults — parent fill 4da09dec… REJECTED, the default itself not revived as Cat A).
- AW-4b: N_trunc = 100 (pins/TRUNCATION_DEGREE_C_N100 — locked truncation degree for C, t617u). Note: pin is for C, not Ξ.
- AW-4c: N_trunc = Written free parameter; numeric runs report N-sensitivity (t713u L17,L22: δ is N-sensitive).

## Coefficient tables
NOT drafted (invent-ban for numerics stands). Schema only: table ν | c_ν = Σ_{(s,k,j): Q_7(n+j,k)=ν, χ_s(k)=1} (j+n+7k/2), ν≤N_trunc — EMPTY until ACCEPT. Alternate path menu: regenerated Ξ 35b186f9… (HD product form) as reference only, not as ledger coeffs.

## MENU (Arvin)
- AW-α ACCEPT all as recommended: AW-1a(-0), AW-2a, AW-3a, AW-4a
- AW-β ACCEPT subset (list items, e.g. AW-1a + AW-3a only)
- AW-γ REVISE (notes; e.g. pick AW-4b, AW-1a-1, AW-2b with twist supply)
- AW-δ REJECT — hold Ξ symbolic (F-PIN-1 stands)
- AW-X4 (OPTIONAL, SEPARATE): ACCEPT ledger Ξ_s ≡ HD Ξ_s (outer_*·Θ_{3/2}); requires resolving G-2 sign. Not implied by AW-α.
