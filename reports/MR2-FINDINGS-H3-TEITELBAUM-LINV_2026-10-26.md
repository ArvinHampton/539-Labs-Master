# MR2 FINDINGS — H3 Teitelbaum 𝓛 queue (S₄(Γ₀(7)), p=7) — 2026-10-26

## Authority (sha verified before write)
- Physicist CONTINUE after Eigen R5 ACCEPT of MR2-FINDINGS-CATB2-CONTINUE-RESUME-STOP sha feae6fa3d37c0be080b382bfd7c46562f62da63dd74e986f5f38af43cf598f83 — VERIFIED
- Eigen REVIEW ACCEPT EIGEN_REVIEW_RELAY_MR2_CATB2_CONTINUE_RESUME_STOP sha 6fa05a81f3e20a83749610f7d87f42ace3c8e537152f6fedf2abd177f389bce1 — VERIFIED
- Rule 4: Eigen delegated H3 compute to MR2.

## Tip lock
Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md READ-ONLY; sha 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 before AND after. **tip_touched NO.**
GAP-5 Owner-reserved (no B′/B″ pick). A1–A4 NOT frozen. Kerr BLOCKED. Does NOT claim P5a. Bridge PARTIAL READY NO.

## STATUS: PARTIAL
Tools: python3 only (no Sage/PARI/Magma on box). Script: quantum-comp/scripts/mr2_h3_theta_filtration.py sha cf45cf5e7910bfe81b33ab604f911ca68342fd1a4297cb762bea41deff7d00f0.

## H3-0 Form identification — PROVED (computation)
JL side: B_{7,∞}=(−1,−7/Q), maximal order O=Z⟨1,i,(1+j)/2,(i+ij)/2⟩, h=1, O*={±1,±i} (mass 1/4 ✓ = (p−1)/24).
Weight-4 theta series Σ_{x∈O} P(x) q^{nrd x} with harmonic O*-invariant P=b²−7c² (pure part bi+cj+dij) gives (÷2):
f = q − q² − 2q³ − 7q⁴ + 16q⁵ + 2q⁶ − 7q⁷ + 15q⁸ − 23q⁹ − 16q¹⁰ − 8q¹¹ + … (Hecke-multiplicativity checked: a4=a2²−8, a6=a2a3, a8).
**a₇ = −7** (sign pinned; slope 1). Matches LMFDB 7.4.a.a (CITE-VERIFY: from memory, not on disk).
Other harmonic invariants (c²−d², cd) give 0 ⇒ JL space 1-dim, consistent with dim S₄^new(Γ₀(7))=1.

## H3-1 Teitelbaum 𝓛_f one-vertex — UNPROVEN (named gap)
Reduced: Γ=O[1/7]^×/Z[1/7]^× acts on T₇ with one vertex orbit; stabilizer O*/±1 ≅ Z/2; 8 edges at the vertex. 𝓛_f = Teitelbaum's ratio of the p-adic period (log-integral vs ord-integral of the Sym² V-valued harmonic cocycle c_f against Γ-hyperbolic elements).
Blocker: requires (a) explicit generators of Γ (edge-pairing γ ∈ O[1/7] of norm 7), (b) Sym²-valued harmonic cocycle solve, (c) p-adic Coleman/Darmon–Pollack-style integration to precision O(7^n). None implemented; no Sage/Magma (Darmon–Pollack/Greenberg overconvergent code absent). Not invented.

## H3-2 Colmez/Stevens 𝓛 = −2 a₇′/a₇ — UNPROVEN (named gap)
Needs slope-1 Coleman family through f (weight-k derivative of U₇ eigenvalue); requires overconvergent modular symbols (Pollack–Stevens) — software ABSENT. Formula itself CITE-VERIFY (not on disk).

## H3-3 Breuil–Mézard k=4, p=7 threshold — ABSENT (CITE-VERIFY failed)
rg over quantum-comp/{literature,papers,sources,theorems,notes} finds no Breuil–Mézard / Ghate–Chitrao semistable-reduction text. Threshold NOT verified on disk ⇒ sign/valuation test NOT applied (and no 𝓛 available anyway).

## H3-4 w(θ³f) — PROVED under stated convention, with CONVENTION FLAG
Convention: mod-7 Katz/Serre filtration on level-1 forms (span of E4^a E6^b Δ^c mod 7), q-expansion to 60 terms (> Sturm bound for all weights tested ≤ 56).
- w(f̄)=16, w(θf̄)=24, w(θ²f̄)=32, **w(θ³f̄)=40** (steps +8 = p+1, consistent with 7∤w).
- 40 ∉ {28,22,16,10,4}. All candidates and 40 are ≡4 mod 6, so the candidate list likely uses a different normalization (e.g. weights modulo p²−1=48 or a shifted θ-cycle). Under the stated convention none of {28,22,16,10,4} is attained. **Flag for Eigen: reconcile convention before using in Soft SF.**

## Soft SF risks (press content → Auditor; CONFIRM may HOLD)
- a₇=−7 and w(θ³f̄)=40 are safe computed facts (script + sha).
- Do NOT write any 𝓛_f value or Breuil–Mézard conclusion — none established.
- Convention mismatch on w(θ³f) is a live risk.

## Blockers
1. No Sage/PARI/Magma (Teitelbaum integration, Pollack–Stevens families).
2. Breuil–Mézard / semistable reduction literature absent on disk.
3. w-convention reconciliation with source of {28,…,4}.

tip_touched NO.
