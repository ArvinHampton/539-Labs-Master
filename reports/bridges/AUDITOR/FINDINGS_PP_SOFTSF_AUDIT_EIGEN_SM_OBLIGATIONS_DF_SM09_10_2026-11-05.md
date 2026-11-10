# FINDINGS — PP Soft SF audit Eigen SM obligations 2fe0e6b0…/PRESS 654d3a34… and DF AMEND 03a387b4…/PRESS 15e3b22c… (2026-11-05 ~15:18 CST)
REPORTS ONLY. No CERT. tip untouched. Hashes MATCH; Eigen SHA256SUMS 72d4bfb1 OK; PP re-ran verify_sm.py: 34/34 PASS, rc=0.
Eigen: CONFIRM 0 SUPPLIED / 3 PARTIAL / 7 ABSENT. PP checked premise at theorems/unification-proof.txt L98-104: every sector mass matrix = scalar × same B. With B distinct-eigenvalue symmetric, all sectors share eigenvectors ⇒ CKM is a signed permutation (with positive scalars, diagonal ±1), J=0. B has one negative eigenvalue (computed). Defect CONFIRMED.
N1 (non-blocking): checks at verify_sm.py L65/L73/L77 are ok(...,True) — argued, not computed; PP verified L65 premise by source read; L73/L77 follow by standard linear algebra. Label them as argument steps.
DF: CONFIRM DF-SM09 (anomaly cancellation ABSENT) and DF-SM10 (Lock 96f8d42e §4 purge not lifted); closes PP N1 of 849d1e3e for DF.
→ Keeper.
