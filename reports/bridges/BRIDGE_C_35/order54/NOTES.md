# order54 NOTES
- Lock: CORE_FREEZE.
  - New files only, all in order54/.
  - order2/5/18/53 were read-only. order18 a2.py lines 1–30 were exec'd, not modified.
  - MAPS_CANDIDATES was not touched.
  - No Ξ/Π/α1 was invented. α is the existing companion shift.
  - RG* labels only. 35-component law vector. No push and no sends.
- Deviation: the first run finished all cases but crashed on JSON serialization of a numpy bool. I fixed only the serialization (bool casts), updated SHA256SUMS, and reran. The results were identical (worst relative error 1.386).
- posthoc_diag.py is explicitly post hoc and does not change the verdict.
