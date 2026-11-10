# SEARCH: written α1 / α2 or a mod-8 companion indexing (read-only, 2026-10-24 America/Chicago)
Tree searched: /workspace/quantum-comp (all text, not PDFs). That includes reports/, oct17-master/, grok-chats/, grok_export/ and the Bridge C rev8 sources under reports/self-audit/repo/docs/.... Commands: `rg -S "α1|α_1|alpha1|alpha_1|α₁"`, `rg -S 9800`, and a scan for companion + mod 8.
Read-only: papers/RTA_FOUNDATION_BOUND was grepped only and not modified. bridges/BRIDGE_C_35/order*/ was not opened beyond grep.

## Hits
1. reports/self-audit/repo/docs/S2-11DM2ET-X-Axiomatic-Book/Bridge_C_Consolidated_rev8_2026-10-19/bridge_c_consolidated_rev8.tex:272:
   "Let $u_{\alpha,\beta}$ ($\alpha\in(\{0,a\}+L')/\Z^2$, $\beta\in\{0,-a\}$; $140$ labels)". **α = (α1, α2) is a per-label characteristic, not one constant.**
2. Same file, l.785: "The $24$ cusp components are the $\beta=-a$ labels with $70\alpha_1\in\{7,21,49,63\}$ and $7\mid$ denominator of $\alpha_2$". The vanishing labels include α ∈ {(7/10,4/5),(9/10,3/5),(1/10,2/5),(3/10,1/5),(1/2,0),(1/2,j/7)}. So α1 ∈ (1/70)Z varies by label.
3. Same file, l.213 (and U1_LEDGER_P_s_Structure_RayClass_2026-10-17.md:39): "p7(α1) for any α1 ≡ 1 mod^× p2 p5 with signs (−,+)". This is a different α1, a field element in a ray class, not the theta shift.
4. papers/RTA_FOUNDATION_BOUND/src/partIII_shadow_v5.tex:115 (read-only): "ϑ^-(τ)=Σ_{u∈α1+Z} u e(5/2 u² τ + 5 b0 u)", with integrality condition "2α1, 10b0, 10b0α1 ∈ Z". So α1 is generic here as well; no value is fixed.
5. 9800: only reports/heavy-daily/2026-10-18-ER-cancellation/fastkappa.py:39–41 ("q2num = 2*N1*N1 + 14*N1*N2 + 7*N2*N2  # /(9800)"). This is a denominator, not a companion indexing.
6. Companion + mod 8: only MAPS_CANDIDATES/BATCH3_RTA_GEOM/PREREG.md:26 (a count k ≡ 0 mod 8). This is not an indexing of the 105 companions on Z/8.

## Assessment
- **No single written α1 is attached to the E3 / 5n²/2 series.** α1 is written only as a label coordinate, ranging over 140 labels with 70α1 ∈ Z.
- Choosing one label, or a pooling or weighting over labels, would be a new selection rule. So would choosing a scaling that makes 170(α1+n)² integral (70α1 ∉ 2Z in general, so ×68 does not give integers, and mod 8 is undefined). Writing that rule now would mean inventing the object, which the brief forbids.
- **No written mod-8 indexing of the 105 companions or of the T-phases k/9800.**
