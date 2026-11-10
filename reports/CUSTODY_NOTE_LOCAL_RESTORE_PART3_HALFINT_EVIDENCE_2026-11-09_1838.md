# CUSTODY NOTE (Local), 2026-11-09 ~18:38 CST (America/Chicago): restoration of deleted part3_halfint evidence

**What happened.** Local's own worker deleted two of its exploratory evidence files at about 18:19 CST, during the Bridge C resolution pass, as a "tidy" step before it wrote the findings file. Nobody else removed them. The files were:
- evidence_local_bridgeC_resolution_2026-11-09/part3_halfint.py (sha256 857e14f370e035bfa9b7be7e2c54d954b0c582ef18ec8c673faddf6361609602)
- evidence_local_bridgeC_resolution_2026-11-09/part3_halfint.log (sha256 c4b8cf4d87887f98ce185a820d78035da6ca62d0bd0d12a4f3e64ba6d345b006)

The deletion broke the additive-only rule, and Local accepts that. The files were a first attempt at item 3 on the trivial-character space S_{3/2}(Γ₀(196)), which gave f-eigenspace dim 0 and Kohnen plus space dim 0. part3_search, part3_preimage and part3_check2 superseded them. The findings file 9e34f2dc cites the dim-6, no-eigenvector result in 3a, which those later scripts confirm.

**Restoration.** I rebuilt both files byte for byte from the worker's own session record and put them back at their original paths as new files, with nothing overwritten. Each has a new .sha256 sidecar. Both rebuilt hashes **match the originals exactly**:
- part3_halfint.py → 857e14f370e035bfa9b7be7e2c54d954b0c582ef18ec8c673faddf6361609602 ✓
- part3_halfint.log → c4b8cf4d87887f98ce185a820d78035da6ca62d0bd0d12a4f3e64ba6d345b006 ✓

**Also disclosed.** In the same step, the worker renamed a just-written draft, ERRATUM_…_SYMBOLS_AND_STS_CONTROL_2026-11-09_1825.md (sha bf2cb4ea286eb8d34614f0e2207e35a44f756ecf46f94aa2d69cb63a66b661d6, about 18:19, never cited), to …_1819.md and fixed its header time. The result is c2e9b6fe. The only difference is the header time and filename; the 1825 draft was not kept.

No other Local files were changed. Tip 7cddb188 untouched. No CERT. Nothing sent outside.
