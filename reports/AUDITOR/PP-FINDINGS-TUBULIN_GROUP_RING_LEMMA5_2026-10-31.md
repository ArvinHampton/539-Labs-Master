# PP FINDINGS — Tubulin-to-Torsion, Lemma 5 group-ring candidate (Owner t58u) — 2026-10-31
Soft SF. REPORTS ONLY. No RECS. No CERT. tip Soft SF CONFIRM 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 tip_touched NO. Kerr BLOCKED.
Files: reports/tubulin-torsion/DEFINITIONS_GROUP_RING.md, PROOF_GROUP_RING_LEMMA5.md; updated THEOREMS.md, PROOF_TERNARY.md (Lemma 5 NF-WHY → PARTIAL).
Readings (invented pending mathematical proof): G := ℤ/Mℤ; H = per-layer elements h_i = Σ a_{i,c}[c·w_i]; ℤ⁺ = positive multiplicities; "total cancellation" := N − |W| (phrase ABSENT-as-written); regular spectral radius := spr over ℂ of ρ(|T|).
- A PROVED: ℤ⁺ coefficients ⇒ zero cancellation (all path weights ≥ 0); det unused.
- B PROVED: |W| ≤ N ≤ ∏‖h_i‖_1 = spr(ρ(|T|)); also |W| ≤ ∏ spr(ρ(h_i)).
- C PROVED (negative): det ρ ≠ 0 does not eliminate signed cancellation. M=3, h_1=[0]+[1], h_2=−[0]+[1]+3[2]: dets 2, 36; two paths 0→1 cancel (W=0, N=2).
- D PARTIAL: bound holds as the inequality in B with no det hypothesis; the det ⇒ bound causation is FALSE as content.
- E PROVED: weak NP-completeness survives on det≠0 + unit ℤ⁺ coeff slice (C={0,1}) — use odd M = 2^k+1 > Σ; 1+ω^j ≠ 0 for M odd. Standard M=2^k reduction gives det=0 when any w_i odd. Slice membership poly-checkable. General multiplicities: checkability NF-WHY.
- Reading (b) (block layered matrix over ℤ[G]): nilpotent ⇒ det = 0 always ⇒ claim vacuous.
Lemma 5 status: PARTIAL. No biophysics claimed.
