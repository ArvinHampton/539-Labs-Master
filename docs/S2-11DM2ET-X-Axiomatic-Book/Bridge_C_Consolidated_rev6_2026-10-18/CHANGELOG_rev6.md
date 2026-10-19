# Bridge C consolidated — CHANGELOG rev5 → rev6 (2026-10-18)

The PDF is bridge_c_consolidated_rev6.pdf.b64. Decode it with `base64 -d`. It has 57 pages and 746168 bytes; sha256 bca68b2352003729b6bd82601af7e68aacd45b8fd5b6a54751829c315b6ed433.

The build is pdflatex ×3, with no errors and no undefined references (build_rev6.log). The other \input files are dims_table.tex, rev4_*.tex and rev5_*.tex. They are unchanged and are in Bridge_C_Consolidated_rev5_2026-10-18/.

## Added
- §14, Revision 6:
  - 14.1 Symmetry audit: Prop 14.1 and the audit table.
  - 14.2 Prime-square sectors:
    - Thm 14.2, conditional on C1–C3;
    - Prop 14.3, exact splits 12+48, 18+72, 36+432, 72+1728;
    - Prop on (C3) at p ∈ {3,5,7,11,13,59}, Cat A;
    - s=121 and s=3481 factor-dimension predictions (Cat B);
    - the Mp2(Z/N) outline (cited).
  - 14.3 h-relations: exact counts 2, 6, 12; orbit fits; h-eigenspace data. The k(k−1) formula is Cat B.
  - 14.4 Analytic:
    - Thm 14.5, period 72 at x=1/3 (Cat A);
    - t^{11/2} and t^{13/2};
    - general x=a/N (Prop 14.7) and the q-adic reduction lemma (Lemma 14.8);
    - even-N periods; x=1/4 Gauss data.
  - 14.5 s=7 local root numbers.
  - 14.6 Open problems after rev6.
- Appendix E (R6.1–R6.6), including Erratum 2.
- Sources S32–S35.

## Renamed
The Analytic-CatB report's "Theorem L" is now Prop 14.7(ii), and its "Lemma R" is now Lemma 14.8. This avoids collisions with the framework's Theorem L and with Lemma R of rev. 4.

## Superseded
The Open-Algebraic 21:15 CDT "retraction" section is superseded (transpose bug) and is not used.
