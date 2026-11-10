# Formal Submission of Dossier Gaps — Local F1–F3 Interface Verification (CORRECTED v2)

Date: 2026-11-03 (America/Chicago)
Status: CORRECTED v2 — resubmitted to Professor Proof per Owner order (call-5e2a78c2); absorbs PP FLAGs 5d13a960….
Scope: Local Path, Bridge C A1→Ξ→RTA, Cat A READY = Local F1–F3 cite-lifts only.
Tip Soft SF LOCK 7cddb188… tip_touched NO. No CERT requested.
Supersedes the refused draft (Soft SF REFUSE OW c072f9fc…).

## 1. Purpose

This dossier asks Professor Proof to open an audit of the Local F1–F3 interface as cite-lifts only.
It lists open gaps as questions. It asserts no value as proved that the Owner has not written.

## 1a. F1–F3 interface statements (cite-lifts; from Local FINDINGS 733db7de… and 999906ac…)

- F1 (Thm A/B + Lemma 5 E): Weak NP-completeness of the RPP cancellation problem. It holds when M is part of the input; the slice M = 2^k+1 > Σ with C = {0,1} and unit coefficients is a subfamily of odd M ≥ 3. For odd M, 1+ω^j ≠ 0, so det ρ ≠ 0 on that slice. It is FALSE for fixed odd M ≤ Σ (counterexample M = 3, w = {1,2}, target 0). Weak only (pseudo-polynomial DP O(nM)).
- F2 (Lemma 5 C): det ρ ≠ 0 does not prevent signed cancellation. Counterexample M = 3: h₁ = [0]+[1], h₂ = −[0]+[1]+3[2]; dets 2 and 36, yet W = 0, N = 2 at target residue 1.
- F3 (Lemma 5 B): |W| ≤ N ≤ ∏‖h_i‖₁ = spr(ρ(|T|)). The det-causation reading in Lemma 5 D is FALSE and is not lifted; "total cancellation" stays invent-pending.
- Lemma 5 overall PARTIAL; only B, C, E lifted.

## 2. Normalization scalar Λ₀ — posed as an open question (not asserted)

Candidate values on record:
- 1.81 — prior asserted value; no derivation on disk.
- ≈0.7858 — Gemini-supplied value; does not match its own formula (numeric drift; OW 4e5a39af…).
- Λ₀ := ln(6+√35)/√10 ≈ 0.7835772 — arithmetic checked (OW 8df5e913…). Identity Soft SF note: √10 = √(Tr ε − 2) = √ε − 1/√ε with ε=6+√35, Tr ε=12. Justification that this is the F1–F3 normalization remains open.
- For comparison, Res_{s=1} ζ_K = 2 h_K ln(ε_K)/√140 = 2 ln(6+√35)/√35 ≈ 0.837679, with h_K = 2 and ε_K = 6+√35. This is not equal to the candidate above.

Question for PP: Which, if any, of these is the correct normalization for the F1–F3 interface, and what derivation is required for the √10 factor?
No value is to be treated as governing F1–F3 until the Owner writes it.

## 3. Prime conditions — inert, not split

The interface conditions are stated on primes inert in K = Q(√35), that is (140/p) = −1, with the ramified primes {2, 5, 7} excluded.
Inert residues mod 140 (arithmetic checked):
{3, 11, 27, 37, 39, 41, 47, 51, 53, 57, 61, 69, 71, 79, 83, 87, 89, 93, 99, 101, 103, 113, 129, 137}.
The earlier phrase "split-prime zero conditions" is withdrawn.
This set is listed for audit reference only; it is not hardcoded into the F1 coordinate map.

## 4. Withdrawn items

- The exponent 7/20 and the β(κ) Mellin–Barnes loop are withdrawn; 7/20 has no source (it is not Kim–Sarnak's 7/64).
- No Burgess bound is claimed; the classical Burgess exponent is 3/16, and no bound for this setting is in Cat A.
- The mod-35 residue table and its Python filter are withdrawn.
- T₃ = 539 is a fixed runtime window, not a stabilization claim.

## 5. Open gaps for audit (not READY)

- G1: V₃₅ as a Hilbert newform space over Q(√35), parallel weight (2,2), level (1). LMFDB lists four newforms of dimensions 2, 2, 2, 8; which subspace V₃₅ means is open.
- G2: Π_fast via Cesàro average of exp(t·ad_{iX}). The idempotence and the domain are unproved.
- G3: Boundary vector C and the claim C ∉ V₃₅. The construction is open; the elliptic curve Y² = X³ − 35X (conductor 78400) is a different object from V₃₅.
- Retracted (not used): earlier hard fails from OW 49500bfd… (spectral-radius product claim false, CERN URL, LMFDB uniqueness) are retracted, not used.

## 6. Requested PP action

Open the audit of the Local F1–F3 cite-lifts only. Answer the question in §2. Treat G1–G3 as open, not as proved. G4 is Retracted (not used).

Disposition: tip untouched; no CERT; not submitted.
