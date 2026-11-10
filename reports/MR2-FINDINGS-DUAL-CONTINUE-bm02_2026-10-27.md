# MR2 FINDINGS DUAL-CONTINUE bm02 — 2026-10-27 (Soft SF / dual-label) — REPORTS ONLY, NO RECS
Tip before: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (LOCK 7cddb188…; untouched)
Parents: indconv FINDINGS 5aeeca13ac3532799e89a53464702675a80d3d61dfa9853de21fa2131cd95142; PRESS indconv 39612d9e4ea8aa9061078c3d15c9a7f8d340138d069e96716edf3d7be10a242f; socK2 ced59b8a5eea3de0fec12e557f626a42e2f4515ff8152c19918934e28e4c4ef4
Source: lit/bm/bm02_multiplicite.pdf ec42c9a450a7f7368a72670a3e9c54b75cad77802f18ac08d4dac6078bf7fa02; .txt aa4893cfffb4b43d4d716f133fd5d12d5c0c482db3cebee474e83fc6b264a22d (Breuil–Mézard, French; line nos = txt)

## Soft SF facts (quoted)
- F1 (txt L1097-1103, §2.1.2): irreducible mod-p GL2(Zp) reps "σn,m = Symn(Fp) ⊗ det^m, (n,m) ∈ {0..p−1}×{0..p−2}" — labelling consistent with σ^[s]=Sym^{p−3}⊗det form (n=p−3,m=1). Soft SF: notation-compatible only.
- F2 (L909-911, Lemme 2.1.1.2(ii)): "τ ≃ (Ind_{Wp2}^{Wp} χ)|Ip ≃ χ|Ip ⊕ χ^s|Ip … s le générateur de Gal(Qp2/Qp) et χ^s le conjugué de χ". Soft SF: defines χ^s as Galois-side Weil-group conjugate; this is NOT the GL2/Γ-side χ^s of indconv. χ vs χ^s stays CLOSED-conditional (no change), BM02 neither contradicts nor strengthens.
- F3 (L921-928, Th 2.1.1.3, Henniart appendix): unique σ(τ) with "π|GL2(Zp) contient σ(τ) ⇔ WD(π)|Ip ≃ τ. De plus, σ(τ) intervient alors dans π|GL2(Zp) avec multiplicité 1." Characteristic 0 (over Qp-bar) only.
- F4 (L659, L1084-1087, Rem 2.1.1.5): Ind_{U0(p)}^{GL2(Zp)} used; "σ(τ) = στ^∨ … σ(τ)=Ind_{U0(p)}^{GL2(Zp)} στ^∨"; contragredient taken due to [CDT]/[BCDT] class-field normalisation. Soft SF: a convention-dependence (dual) flag, compact induction from finite-index U0(p), char 0.
- F5 (L1105-1181): admission rule with multiplicities µn,m(ρ) ∈ {0,1,2}; mult 2 only for σ_{p−1,m} with ρ ≃ (ω^{m+1}λ(α) *; 0 ω^m λ(α)), * peu ramifié; L1185-1187 authors: no reasonable explanation for mult 2 beyond fitting conj 2.3.1.1. L1188: rule is "duale de Cartier" of [BCDT] rule.
- F6 (L1204-1213): µaut(k,τ,ρ) defined via Jordan–Hölder factors of reduction of σ(k,τ). L1422-1429: µgal = Samuel multiplicity of R(k,τ,ρ)⊗F (EndF[Gp](ρ)=F hypothesis, L1425).

## Soft SF effect on flags
- SF-IC-c (smooth mod-p Ind word-for-word): NOT closed. BM02 has no smooth mod-p Ind_B^{GL2(Qp)} statement; only char-0 Ind_{U0(p)}^{GL2(Zp)} and Weil-group Ind. Narrowed: gap now named SF-IC-c′ = "smooth mod-p parabolic Ind of GL2(Qp) not in BM02; BM02 adds dual/contragredient normalisation caveat (F4)".
- soc_K equality: OPEN. BM02 contains no socle statement (grep "soc": 0 hits). Gap named SF-SK-bm02: "no soc_K(Ind) in BM02". SF-SK2e inference unchanged.
- SF-BL1 BL94: MISS stands; BM02 cites [BL2] prop.1 (L1103) only for σn,m classification. No new free BL94 full-text lead hunted/found.
- Residual-mult / End / lattice dual names (touch only, NO pick): F5 mult-2 case and F6 End=F hypothesis Soft SF-touch residual-mult and End names; F4 dual convention Soft SF-touches lattice-dual naming. Residual-C pick OPEN dual. SF-R3′ OPEN-named. Rem 6.2 L₂ stands. Kerr BLOCKED. Filtration 10∥40 BOTH NAMED PARALLEL.

## STATUS: PARTIAL Soft SF (narrowed, nothing newly closed)
