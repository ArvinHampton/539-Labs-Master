# FINDINGS — PP Soft SF audit — 539 Ops HQH Crit.3 open-lemma pinboard cc95ceb9… — 2026-11-05
REPORTS ONLY. No CERT. No RECS. Tip 7cddb188… tip_touched NO.
Authority: OW 4ba9151f… (sidecar MATCH). The pinboard FINDINGS cc95ceb9… MATCHes its sidecar. This is the follow-on named in Ops FINDINGS 70091747… (PP CONFIRM 284268a8…).
Checks:
- OL-3, the Π domain card. It gives three choices (free, bounded, SHA3-image) and leaves the choice BLANK. The easiness of the bounded domain is labelled heuristic: CONFIRM.
- OL-5, the λ family. Every field is BLANK, and it notes that poly/negl are not well-typed without it: CONFIRM.
- OL-7, the C2 definition. Recomputed: for U, U′ iid uniform on {0,1}^n, Pr[U≠U′ ∧ f(U)=f(U′)] = Σ_z p_z² − 2^{−n}. This is correct. The union bound C(q,2)·ε_C2 is correctly stated as conditional. The target bound is left OPEN, and the Rényi 2^70 / 2^140 figures are not imported. The direction is right: by R6 the term enters as an additive loss, so an upper bound is what's needed: CONFIRM.
- §4, the Adv template. It is template only, R is not asserted to exist, and the FG-A obstruction is cited: CONFIRM.
NOTE: Ops sent no separate PRESS file, only an inline relay. This is a record note only.
Verdict: CONFIRM. Soft SF → Keeper.
