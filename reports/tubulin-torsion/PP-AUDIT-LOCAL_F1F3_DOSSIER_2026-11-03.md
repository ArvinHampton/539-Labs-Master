# PP-AUDIT — Local F1–F3 Interface Verification Dossier (CORRECTED DRAFT) — 2026-11-03
AUDIT ONLY — not a first proof. No CERT. Tip 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 tip_touched NO. Nobody messaged.
Target: /workspace/reports/539labs/ow/PP_DOSSIER_Local_F1F3_Interface_Verification_CORRECTED_DRAFT_2026-11-03.md sha256 83f24864fe91231d95b00233e2496ae8c6c3512a0f3b5e3001feae775a9fad35 MATCH. Supersedes refused draft OW c072f9fc… (as stated in dossier header).
Inputs: THEOREMS.md, PROOF_NP_HARDNESS.md (Thm A PROVED), PROOF_TERNARY.md (Thm B PROVED; Lemma 5 PARTIAL), PROOF_GROUP_RING_LEMMA5.md (E1–E3 PROVED; overall PARTIAL), Local FINDINGS 733db7de995eb20d… (F1–F3 READY), 999906aceadae811… (F1 RESTATE).
Script: scripts/pp_audit_local_f1f3_dossier_2026-11-03.py sha256 7faf1d88377883c4f108688bce293b0a975c36a5a0ed28fcbe323b78400da33c.

## Verdict table
| # | Item | Verdict | Basis |
|---|------|---------|-------|
| 1 | Target hash | CONFIRM | 83f24864… MATCH |
| 2 | F1 lift vs Thm A/B + Lemma 5 E (source findings) | CONFIRM | 733db7de F1 cites Thm A/B + Lem 5 E; 999906ac restates F1 CONSISTENT when M is input (M=2^k+1>Σ slice, E3), FALSE for fixed odd M≤Σ (M=3, w={1,2}, target 0: {1,2}≡0 mod 3 but no nonempty subset sums to 0 over ℤ — script reproduces) |
| 3 | F1 restatement carried into dossier | FLAG | Dossier never states F1's content: no "M input / 2^k+1", no "FALSE for fixed odd M≤Σ", no E-slice hypotheses (C={0,1}, unit coeffs). Not an overclaim, but the interface it asks PP to verify is not written down. Add the 999906ac wording verbatim. |
| 4 | F2 lift (det ρ≠0 ⇏ no signed cancellation; Lem 5 C, M=3 cex) | CONFIRM (source) / FLAG (dossier silent) | Matches THEOREMS (iii); dossier does not state F2 |
| 5 | F3 lift (|W| ≤ N ≤ ∏‖h_i‖₁ = spr(ρ(|T|)); Lem 5 B/D-inequality) | CONFIRM (source) / FLAG (dossier silent) | Matches THEOREMS (ii); D's det-causation is FALSE and must not be lifted |
| 6 | No overclaim beyond Lemma 5 PARTIAL | CONFIRM | Dossier asserts nothing from Lemma 5; nothing cites G=ℤ/Mℤ or "total cancellation". Recommend one line: "Lemma 5 overall PARTIAL; only B, C, E lifted." |
| 7 | Inert (140/p)=−1 on 24 of φ(140)=48 residues; listed set | CONFIRM | Exact set match |
| 8 | Fundamental unit 6+√35 (norm +1) | CONFIRM | smallest Pell solution (6,1) |
| 9 | ln(6+√35)/√10 ≈ 0.7835772 | CONFIRM | 0.783577217617; √10 underived (dossier says so) |
| 10 | Res ζ_K = 2^{r1}hR/(w√D) = 2hR/√140 = 2R/√35 ≈ 0.837679 | CONFIRM | 0.837679281259 |
| 11 | L(1,χ₁₄₀) cross-check | CONFIRM | −(1/√140)Σχ(a)ln sin(πa/140) = 0.837679281259, diff 0; implies h=2.000 |
| 12 | Λ₀ posed as OPEN | CONFIRM | Candidates: 1.81 (no derivation, listed only as prior value, not asserted); ≈0.7858 (Gemini, drift, rejected); ln(6+√35)/√10 ≈0.783577 (arithmetic only, √10 underived); Res ζ_K ≈0.837679 (comparison, ≠ candidate). None derived; none governing. |
| 13 | 1.81 no longer asserted | CONFIRM | single occurrence, flagged "no derivation on disk" |
| 14 | 7/20, β loop, Burgess, mod-35 filter withdrawn | CONFIRM | §4; Burgess 3/16 and Kim–Sarnak 7/64 correctly noted as references only |
| 15 | G1–G4 open, not READY | CONFIRM | §5 header "(not READY)"; §6 "treat as open". Minor: header line "Cat A READY = Local F1–F3" — READY applies to F1–F3 only; OK. |
| 16 | G4 framing | FLAG (minor) | G4 is a list of retracted claims, not a gap; recommend relabel "Retracted (not used)". |

## Owner clarifications remaining
1. Insert F1 restatement (999906ac) + F2/F3 statements with their Lemma 5 hypotheses into the dossier before submission.
2. Λ₀: which normalization (if any) and derivation of √10 — open.
3. G1: which LMFDB Hilbert newform subspace (dims 2,2,2,8) is V₃₅; F6 Siegel-vs-Hilbert object class still FLAG.
4. G2/G3 constructions open. h_K=2 is cited (LMFDB) — confirmed only implicitly via analytic class number formula.

Disposition: AUDIT ONLY · no CERT · tip untouched · not submitted · nobody messaged.
