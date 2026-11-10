# MR2 FINDINGS — DUAL-CONTINUE — ind-invent-proxy — 2026-10-27
Role: Math Research 2, Soft SF writer, Project Quantum Comp. REPORTS ONLY — No RECS. Soft SF → Auditor.
Invent lift cited: Owner invent ban LIFTED (OW 1c7163de…; call-a0858383).
Tip (READ-ONLY): /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md
- BEFORE sha256: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91
- AFTER  sha256: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — MATCH. tip_touched NO. No tip-fold. Kerr BLOCKED (not invented). P5a NOT claimed.

## STATUS
- SF-IC-c′: Soft SF-NARROWED (verbatim char-0 proxy found) + Soft SF-INVENTED-CLOSED (mod-p convention INVENTED, conditional on invent lift).
- OPEN-SK-conv: Soft SF-INVENTED-CLOSED conditional (function-space convention INVENTED, matched to proxies).
- soc_K=soc_Γ verbatim: OPEN (no BL-free Soft SF text found; NOT claimed).
- OPEN-SK-p3: OPEN (invented convention gives no p=3 soc_K value).

## 1. Search log (cwd /workspace/quantum-comp/lit/bm)
| command | count |
|---|---|
| grep -ciE 'Ind_\|induite\|induction\|f\(bg\)\|chi\(b\)' breuil_GL2Qp_I.txt | 2 |
| same, breuil_GL2Qp_II.txt | 8 |
| same, bm02_multiplicite.txt | 21 |
| same, 1209.5205.txt | 4 |
| same, 1309.1658.txt | 5 |
| grep -c 'soc_Γ\|socΓ' (all lit/bm *.txt) | 0 everywhere except breuil_paskunas_supersingular.txt: 25 (not in task scope; not used for verbatim claim) |

Verbatim hits:
- 1209.5205 l.3424–3425: "(Ind_P^G χ)^an be the space of locally analytic function f : G → L, such that f(bg) = χ(b)f(g) for all b ∈ P and g ∈ G, where G acts … by right translations."
- 1209.5205 l.3545–3547: "I^sm(χ) denotes the space of locally constant functions f : G → L such that f(bg) = χ(b)f(g) for all b ∈ P and g ∈ G, with G-action by the right translations."  ← word-for-word χ(b)f(g) smooth induction; coefficients L (char 0), NOT mod p.
- Breuil GL2Qp I l.77–78: compact induction as functions f : GL2(Qp) → Sym^r F̄p, compact support mod Z, f(kg)=Sym^r(k)f(g) (left-equivariance convention, mod p, K Z not P).
- Breuil GL2Qp II l.672: "l'induite parabolique est l'induite lisse classique" (no formula).
- BM02 l.8213: "induite parabolique (normalisée ou non) de χ1⊗χ2" restricted to K, via [Ca] p.311 (no formula; normalization-agnostic for K-restriction).
- No mod-p f(bg)=χ(b)f(g) verbatim in scope.

## 2. INVENTED convention (label: INVENTED — not BL94/BL95)
INV-Ind (mod p): For a smooth character χ = χ1⊗χ2 : T(Qp) → F̄p^×, inflated to B (upper-triangular P), set
 Ind_B^G χ := { f : G → F̄p locally constant | f(bg) = χ(b) f(g) ∀ b∈B, g∈G }, G acting by (g·f)(x)=f(xg). Unnormalized (no modulus twist).
Justification as proxy: identical shape to 1209.5205 I^sm(χ) (verbatim, char 0) with L replaced by F̄p; left-equivariance/right-translation matches Breuil I l.77 compact-induction convention; BM02 l.8213 implies K-restriction insensitive to normalization, so the unnormalized choice does not affect soc_K.
Consistency checks:
- χ vs χ^s: matches on-disk indconv Soft SF MATCH (χ/χ^s CLOSED conditional) — INV-Ind uses χ on B with f(bg)=χ(b)f(g); the χ^s-form arises from the opposite Borel / w-conjugation, as already recorded there. No new conflict.
- soc_K: with INV-Ind, Ind_B^G χ|_K = Ind_{B(Zp)}^K χ (Iwasawa), whose K-socle is the weight recorded in Rem 6.2 / sockval Soft SF: Sym^{p−3}⊗det, CLOSED-conditional p≥5. Consistent; not re-derived independently.

## 3. Flag outcomes
- SF-IC-c′: Soft SF-INVENTED-CLOSED (conditional on invent lift + indconv/sockval conditionals). Remaining gap named: no mod-p verbatim source; char-0 → mod-p transfer is INVENTED.
- OPEN-SK-conv: Soft SF-INVENTED-CLOSED (conditional). Remaining gap: BL94 verbatim still MISS.
- soc_K=soc_Γ verbatim: OPEN (carried).
- OPEN-SK-p3: OPEN (carried).

## 4. Carried flags
SF-IC-c′ (INVENTED-CLOSED cond.), OPEN-SK-conv (INVENTED-CLOSED cond.), soc_K=soc_Γ verbatim OPEN, OPEN-SK-p3 OPEN, BL94/BL95 MISS, Kerr BLOCKED, P5a not claimed, tip READ-ONLY.

REPORTS ONLY — No RECS.
