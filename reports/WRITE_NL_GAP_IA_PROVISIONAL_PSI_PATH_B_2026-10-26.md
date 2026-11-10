# WRITE — NL provisional ψ_prov (t↦q) + path (b) regime |q|≤r — 2026-10-26
**PROVISIONAL — UNPROVEN — NOT Category A — NOT Owner-Written corpus — NL write-authority grant.**

Lane: Non Local Path · Soft SF Write-only → Auditor · tip Soft SF LOCK untouched tip_touched **NO**
Date: 2026-10-26 ~19:20 CDT America/Chicago
**Result class: PARTIAL under invent** — path (b) closes *conditionally* on a named convergence hypothesis H_conv (§3) that is not established in the corpus or here.

## Authority (live sha256sum)
- OW write authority `5544907ec1fff3687b35740c0b91725ac7b684db5667453a634f29887ffc6a0b` MATCH
- Freedom OW `c3954963745870d59b07aafde0bfdefba56c4e50bbf4b0e81e764d8785f6bb70` MATCH
- First Write Φ_prov/w_prov/B_prov path a/c `dc3141716d8c6c5bad92dbbe2dd9b3cf8f1f47793fa5a2a850a2188796a813a7` MATCH (USED)
- GS-IND `4212ae4dc3564fbe52963047e19f8b2a5da87dd54e1258d4335b4c7bfa0568fe` cite (I1, I4)
- Tip LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` READ ONLY
- Zenodo `e48056d8ff13669ab0432b4a758925ad4164ecdc754181fa694b57d842f13f53` cite — Written envelope e^{-t/τ}, period 539.9

## 1. ψ_prov candidates (PROVISIONAL)
- **ψ_prov,0 (primary):** q(t) := e^{-t/τ}, τ>0, t≥0 ⇒ q∈(0,1], |q| = e^{-t/τ}.
- **ψ_prov,1 (optional oscillatory):** q(t) := e^{-t/τ}·e^{2πi t/539.9}. Then |q| = e^{-t/τ}; all modulus bounds below are identical to ψ_prov,0. Introduces complex q; Φ_prov extended ℂ-linearly (provisional).
τ is **not** fixed here (no Written value adopted as LOCKED).

## 2. Regime |q|≤r
For 0<r<1: |q(t)|≤r ⇔ t ≥ t_r := τ·ln(1/r), for both candidates.

## 3. Path (b) — tolerance O(r^8) under Φ_prov
Formal statement already closed in path (a): (g_s−g_{s'})X^M_prov ∈ q^8 ℚ[[q]] (GS-IND I1). To pass from formal to evaluated at q=ψ_prov(t) one needs:

**H_conv (named, UNPROVEN):** g_s (s∈{7,8,11}) and X^M_prov have radius of convergence ρ>r, so h := (g_s−g_{s'})X^M_prov = Σ_{n≥8} a_n q^n with |a_n| ≤ C ρ^{-n}.

**Lemma (provisional).** Under H_conv, for t≥t_r:
|h(q(t))| ≤ C (r/ρ)^8 /(1−r/ρ) = O(r^8),
and the evaluated load g_s X^M_prov(q(t)) equals (1+q+q^4)X^M_prov(q(t)) up to O(r^8), independent of s.
*Proof.* Geometric tail bound Σ_{n≥8} C(r/ρ)^n. ∎

**Status:** conditional close. Without H_conv (no Written growth bound on X^M; B4 Written t↦q absent) the evaluated statement is not established ⇒ **PARTIAL under invent**.

## 4. Holds / non-claims
- No s∈{7,8,11} pick. No χ² or Gap-X1 as proven. ZX UNLINK cite-only. Kerr BLOCKED.
- tip Soft SF LOCK untouched tip_touched NO.
- Corpus gaps B4 (Written t↦q), D1, C1, B gloss conflict remain real. Promotion requires Owner Accept + Auditor CONFIRM.

## Route
Soft SF → Auditor. Relay → Physicist.
