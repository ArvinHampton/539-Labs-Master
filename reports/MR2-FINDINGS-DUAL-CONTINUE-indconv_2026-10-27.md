# MR2 FINDINGS — DUAL CONTINUE — indconv (2026-10-27)
Labels: [Soft SF] [DUAL: Filtration 10 ∥ 40 BOTH NAMED PARALLEL — no pick]. REPORTS ONLY — no RECS. Kerr BLOCKED. Residual-C pick OPEN dual (not picked).
Parent: MR2-FINDINGS-DUAL-CONTINUE-socK2_2026-10-27.md ced59b8a5eea3de0fec12e557f626a42e2f4515ff8152c19918934e28e4c4ef4

## Tip check
- Before: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91
- After: see .sha256 companion check in PRESS; tip_touched NO (not opened for write).

## 1. Ind-convention [Soft SF] — MATCH Soft SF (with one named caveat)
- SF-IC1 (project definition, quote): sigma-gaps FINDINGS row 2h quotes Hu–Tan 1309.1658 l.1670: "πα := Ind_P^G (ω ⊗ ω^{-1})", P = "the upper triangular Borel subgroup" (1309.1658 l.301). 1005.2008 l.244: "(Ind_P^G ω⊗ω^{-1}) ⊗ η∘det".
- SF-IC2 (character slot, quote): Paškūnas 1209.5205 l.1278–1283: "Let P be the subgroup of upper triangular matrices … we write χ1 ⊗ χ2 for a character of P, which maps (a b; 0 d) to χ1(a)χ2(d)."
- SF-IC3 (equivariance side, quote): 1209.5205 l.3546: "functions f : G → L such that f(bg) = χ(b)f(g) for all b ∈ P and g ∈ G" (unnormalised, left P-equivariant). Also 1005.2008 l.5530 "f(bg) = b f(g) for all b ∈ P".
- SF-IC4 (BP, quote = SF-SK2a/b): BP txt l.600–606: B acts on σ^U by "χ: (a ∗; 0 d) ↦ a^r η(ad)"; "Ind_B^Γ χ (resp. Ind_B^Γ χ^s) … isomorphic to Ind_I^K χ (resp. Ind_I^K χ^s)"; l.676: "χ^s … (a ∗; 0 d) ↦ d^r η(ad)".
- Verdict: same Borel (upper triangular), same slot convention (χ1 on a, χ2 on d), same unnormalised left-equivariance ⇒ MATCH Soft SF.
- Caveat SF-IC-c (named): SF-IC3 is stated in 1209.5205 for locally analytic / continuous Ind, not verbatim for smooth mod-p Ind_P^G; extension to smooth mod-p case is reading-consistent, not quoted.

## 2. χ vs χ^s [Soft SF] — derived (not quoted end-to-end)
- SF-CS1 (derivation): restrict ω⊗ω⁻¹ to B(F_p) (ω|Z_p^× = reduction): χ(diag(a,d)) = a·d^{-1}. Solve a^r η(ad) = a d^{-1}: η = (·)^{-1}, r = 2. So our χ is BP's χ attached to σ = Sym^2 ⊗ det^{-1} (f = 1). χ ≠ χ^s since 0 < r=2 < p−1 for p>3 (consistent SF-SK2f).
- SF-CS2 (quote): BP l.708 "σ is then the socle of Ind_B^Γ χ^s by Theorem 2.4"; Thm 2.4(ii) "(Ind_B^Γ χ)_i = (Ind_B^Γ χ^s)_{f−i}".
- SF-CS3 (derivation, f=1): our Ind is of χ (not χ^s) ⇒ soc = (Ind χ^s)_1 = the ℓ=1 weight, Lemma 2.2 λ0 = p−1−x, e(λ) = ½(p−1 + r − (p−1−r)) = r = 2 ⇒ σ^[s] = Sym^{p−3} ⊗ det^2 ⊗ det^{-1} = Sym^{p−3} ⊗ det.
- SF-CS4: agrees with independent derivation SF-SK3 (socK FINDINGS: σ_{p−3}⊗det ⊂ soc_K(πα)). Socle of Γ-Ind = σ^[s] = Sym^{p−3}⊗det, NOT σ = Sym^2⊗det^{-1}.
- Status: χ/χ^s labelling CLOSED Soft SF conditional on SF-IC-c and on soc_K equality (below).

## 3. BL94 hunt — SF-BL1 MISS (stands)
Tried: WebSearch (title+Duke+pdf); doi.org; Project Euclid .pdf and euclid.dmj download URLs via curl → HTML (paywall/landing), not PDF; only free item = Project Euclid first-page preview (intro, no socle statement); Berger ENS-Lyon article21.pdf cites BL94 Thm (π(r,λ,χ) ≅ ind(µ_λ⊗χω^r µ_λ^{-1})) only. No HAL/numdam/author copy found. Not ingested.

## 4. BM02 — NEW free source, INGESTED
- Breuil author page: https://www.imo.universite-paris-saclay.fr/~christophe.breuil/PUBLICATIONS/multiplicite.pdf
- /workspace/quantum-comp/lit/bm/bm02_multiplicite.pdf ec42c9a450a7f7368a72670a3e9c54b75cad77802f18ac08d4dac6078bf7fa02
- /workspace/quantum-comp/lit/bm/bm02_multiplicite.txt aa4893cfffb4b43d4d716f133fd5d12d5c0c482db3cebee474e83fc6b264a22d
- MANIFEST.sha256 appended (sha256sum -c OK): 662be25e4deb53555a730d4477950c28a6a4ff6323fad086ba69670aed8b8252
- Content not yet mined for this flag. BM02 MISS → INGESTED (unread).

## OPEN Soft SF-named
- soc_K equality soc_K(πα) = soc_Γ(Ind_B^Γ χ̄): OPEN-narrowed (SF-SK2e inference; BL94 MISS).
- SF-IC-c: smooth mod-p Ind convention not verbatim in on-disk sources (analytic/continuous only).
- SF-R3′ OPEN-named stands. Residual-C pick OPEN dual. Rem 6.2 L₂ stands. Kerr BLOCKED.
