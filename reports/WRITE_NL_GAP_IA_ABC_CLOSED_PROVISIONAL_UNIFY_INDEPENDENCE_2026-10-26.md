# WRITE — NL Gap-I(a) a∥b∥c CLOSED-provisional UNIFY + independence lemmas — STATUS RE-STAMP / DELTA on unify Write 1bb51cfd… — 2026-10-26
**PROVISIONAL — UNPROVEN — NOT Category A — NOT Owner-Written corpus — NL write-authority grant.**

Lane: Non Local Path · Soft SF Write-only → Auditor · tip Soft SF LOCK READ ONLY, tip_touched **NO**
Date: 2026-10-26 ~19:35 CDT America/Chicago
**Frame:** status re-stamp / delta on unify Write `1bb51cfd3afee1f0be810e1ba1d1b2b77f8f4cbb056bd50c8efa4b37a0a9a4fa`. Owner ACCEPT of H_conv (OW `500d27663fbbea448ed5af58e0d79e64b836cd55baa8ab5bdaf762aa935b0dea`; PRESS `0dbf0ba143de15bb0152a3a987c888cf4655d5ae18794360a95c19dcb91ed6f9`; NL ACK `15414195e091dec3bf88ea6b9ab3e00f0e76734d847cd7b7d7bb1ea57d78828f`) is LIVE. The 1bb51cfd §2 line "path (b) PARTIAL" is re-stamped → **CLOSED-provisional under Owner-Accepted H_conv + ψ_prov**. No new Φ/ψ/w objects.
**Result class: CLOSED-provisional UNIFY — paths (a) ∥ (b) ∥ (c) — under Φ_prov + Owner-Accepted H_conv / ψ_prov. PROVISIONAL — NOT Category A.**

## 1. Status board (delta vs 1bb51cfd)
| Path | 1bb51cfd status | Re-stamped status | Basis |
|---|---|---|---|
| (a) coords / modes gloss / any contraction | CLOSED-provisional | CLOSED-provisional (unchanged) | Lemma U (§2), dc314171, 5848b62f §1–2 |
| (b) analytic t→q | PARTIAL | **CLOSED-provisional under Owner-Accepted H_conv + ψ_prov** | Lemma B (§2); OW 500d2766… |
| (c) w≡1 or C_prov,X | CLOSED-provisional | CLOSED-provisional (unchanged) | Lemma U; dc314171, 5848b62f §3 |

All three: PROVISIONAL — NOT Category A; promotion requires later Owner Write + Auditor CONFIRM.

## 2. Independence lemmas (COOK prove-tighten)
Setting (as 1bb51cfd §1): R := ℚ[[q]], I := q^8 R ideal; I1 (GS-IND 4212ae4d…): h_{s,s'} := g_s − g_{s'} ∈ I, s,s' ∈ {7,8,11}. Load L_s := g_s · Σ_{j∈J} c_j w_j Y_j, J finite, c_j ∈ ℚ, w_j ∈ R g_s-free, Y_j ∈ B_prov (X^M_prov, M=0..10) or B_prov,modes (X_n), under Φ_prov.

**Lemma U (formal; paths (a),(c)) — restated.** L_s − L_{s'} ∈ I, so L_s mod q^8 is s-independent.
*Proof.* L_s − L_{s'} = h_{s,s'} · Σ c_j w_j Y_j; sum ∈ R; h ∈ I; I ideal. ∎
Caveat: s-dependent weights lie outside Lemma U.

**Lemma B (analytic; path (b), Accepted regime).** Assume Owner-Accepted H_conv (∃ρ>r: g_s, and each Y_j and w_j, converge on |q|<ρ) and Accepted ψ_prov: q(t)=e^{-t/τ} (or oscillatory variant with |q(t)|=e^{-t/τ}). Fix ρ' with r<ρ'<ρ and M_{ρ'} := max_{|q|=ρ'} |L_s − L_{s'}|. Then for all t ≥ t_r := τ ln(1/r) and all s,s':
  |L_s − L_{s'}|(q(t)) ≤ M_{ρ'} (r/ρ')^8 / (1 − r/ρ') = O(r^8).
*Proof.* (i) By Lemma U, D := L_s − L_{s'} = Σ_{n≥8} a_n q^n as a formal series. (ii) Under H_conv, D is a finite sum of products of functions holomorphic on |q|<ρ, hence holomorphic there, and its Taylor series equals the formal one. (iii) Cauchy: |a_n| ≤ M_{ρ'} ρ'^{-n} (radius-only; no extra growth assumption — 5848b62f §4 tighten). (iv) t ≥ t_r ⇒ |q(t)| = e^{-t/τ} ≤ r; the oscillatory phase does not change |q|. (v) Geometric tail: |D| ≤ M_{ρ'} Σ_{n≥8} (r/ρ')^n. ∎
**Corollary (s-independence, Accepted regime).** In the late-time window t ≥ τ ln(1/r) the evaluated load is s-independent up to O(r^8), uniformly across coords/modes gloss, every contraction, and every g_s-free weight; path (b) therefore reduces to Lemma U + Accepted analyticity. Constants M_{ρ'}, ρ, τ, r are NOT fixed here (no numeric claim).
Caveat: Lemma B is conditional on the Accepted hypothesis; it is not a proof of H_conv itself.

## 3. Unified roster update
| Object | Source | Status |
|---|---|---|
| Φ_prov | dc314171 | provisional scalar; ≠ Written 11D Φ |
| w_prov ≡ 1 | dc314171 | provisional; path (c) |
| C_prov,X / w_prov,X = 1+λ[q^0]X | 5848b62f §3 | C_alt; reduces to Lemma U; λ unfixed |
| B_prov (coords X^M) | dc314171 | provisional gloss |
| B_prov,modes (X_n) | 5848b62f §1 | alternate gloss; conflict l.280 vs l.570 unresolved |
| X̄_prov (1/11) / X_modes (1/N) | 5848b62f §1–2 | provisional; contraction-independent |
| ψ_prov (q=e^{-t/τ}, oscillatory variant) | d1765fba | **Owner-Accepted** (OW 500d2766…) |
| H_conv_prov (radius ρ>r) | d1765fba / 5848b62f §4 | **Owner-Accepted** (no longer an UNPROVEN gate for path (b)); still not proven |
| I1 (h ∈ q^8ℚ[[q]]) | 4212ae4d | GS-IND input, cited |

Remaining Owner-gated promotion items (NOT covered by Accept):
1. B gloss conflict: coords vs modes (l.280 vs l.570).
2. Φ_prov ≠ Written 11D Φ — type promotion needs Owner Write.
3. Category A for a/b/c needs later Owner Write + Auditor CONFIRM.
4. Optional: Written growth bound on X^M + Written t↦q (B4) would replace Accepted H_conv/ψ_prov by Written premises.

## 4. Holds
No MIXED obs↔model maps; no χ² as proven; no Gap-X1; no s-pick; Kerr / Path4 C2–C3 BLOCKED; no tip folds (tip READ ONLY); ZX cite-only, no re-link.

## 5. Live sha256sum (all MATCH, checked ~19:33 CDT)
| Item | sha256 | Result |
|---|---|---|
| Tip LOCK residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 | MATCH |
| OW H_conv Accept | 500d27663fbbea448ed5af58e0d79e64b836cd55baa8ab5bdaf762aa935b0dea | MATCH |
| PRESS OW Accept | 0dbf0ba143de15bb0152a3a987c888cf4655d5ae18794360a95c19dcb91ed6f9 | MATCH |
| NL ACK Soft SF | 15414195e091dec3bf88ea6b9ab3e00f0e76734d847cd7b7d7bb1ea57d78828f | MATCH |
| Φ_prov path (a)+(c) | dc3141716d8c6c5bad92dbbe2dd9b3cf8f1f47793fa5a2a850a2188796a813a7 | MATCH |
| ψ_prov path (b) | d1765fbab449162679d128aba145c4708f23ac3532e7a94a8987a7c917366229 | MATCH |
| Remaining B/C/D | 5848b62f02d2f22c28ceef0f97f83f5be76a1841b55fcd97ea15003a898eb959 | MATCH |
| COOK unify (re-stamped) | 1bb51cfd3afee1f0be810e1ba1d1b2b77f8f4cbb056bd50c8efa4b37a0a9a4fa | MATCH |
| GS-IND I1 | 4212ae4dc3564fbe52963047e19f8b2a5da87dd54e1258d4335b4c7bfa0568fe | MATCH |
| Write authority | 5544907ec1fff3687b35740c0b91725ac7b684db5667453a634f29887ffc6a0b | MATCH |
| Freedom | c3954963745870d59b07aafde0bfdefba56c4e50bbf4b0e81e764d8785f6bb70 | MATCH |

Soft SF → Auditor. tip_touched NO.
