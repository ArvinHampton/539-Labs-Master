# MR2 FINDINGS — H3 Jochnowitz recompute + Sage attempts (2026-10-26)
STATUS: PARTIAL — H3-4 DONE (10 ∈ list); H3-1/H3-2 UNPROVEN (named software gaps); H3-3 ABSENT.
Authority: prior FINDINGS sha bdcaf1e6…257ef (a₇=−7 reused, re-confirmed by Sage); Eigen R5 sha e3ac6df9…74dd9c. Tip sha 7cddb188…dfc91 verified before/after; tip_touched NO. GAP-5 not picked; Kerr BLOCKED; no P5a claim; Bridge PARTIAL READY NO.
Tool: passagemath 10.5.49 (/tmp/pm/bin/sage). Script: scripts/mr2_h3_jochnowitz_g07.sage sha f84b9d8037e6f27cfc5f21193b97498243bdcbf7616e65d8f123fb51b005a840.

## H3-4 Jochnowitz recompute — DONE
**Named convention ("Γ₀(7)-geometric"):** w(g) = least k with g ≡ h mod 7, h ∈ M_k(Γ₀(7), Z_(7)) (q-expansion membership in Sage integral basis ⊗ F₇), so w(f)=4 for f=7.4.a.a (Sage newform: q−q²−2q³−7q⁴+16q⁵…, a₇=−7). Search over k ≡ w mod 6 (E₆≡1 mod 7), precision 100 > Sturm 27 at k=40.
Results w(θⁱf): i=0:4, 1:6, 2:8, **3:10**, 4:6, 5:8, 6:4 (θ⁶f≡f-cycle closes).
**w(θ³f)=10 ∈ {28,22,16,10,4}.** Caveat: Jochnowitz's theory assumes p∤N; here p=N=7, so this is the Γ₀(7) q-expansion-minimal-weight convention, not literal Jochnowitz (p∤N). The naive bound w+8i gives 4,12,20,28,… (28 at i=3), showing the prior list is the Γ₀(7)/w=4 grid; 10 is the realized filtration. Katz level-1 value 40 (prior) stands under its own convention. Reconciliation of which list element is "operative" → Owner/Auditor.

## H3-1 Teitelbaum 𝓛_f — UNPROVEN (named gap)
Blocker: Sage BrandtModule(7,1,4) → "weight != 2 not yet implemented"; no p-adic (Teitelbaum) integration on Bruhat–Tits tree in this Sage.

## H3-2 Colmez/Stevens −2a₇′/a₇ — UNPROVEN (named gap)
Pollack–Stevens present but lift(7,…) → "Lifting non-ordinary eigensymbols not implemented (issue #20)"; f has slope 1 = critical (k−2)/2. No family derivative computable.

## H3-3 Breuil–Mézard — ABSENT
grep -ril breuil over /workspace/quantum-comp: only MR2/Eigen/Auditor reports, no source paper. No threshold asserted.

## Soft SF
YES only for: w(θ³f)=10 ∈ list under named Γ₀(7)-geometric convention (p|N caveat). Not for 𝓛-values.
