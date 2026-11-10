# OWNER WRITE — Remedy T3 conflict (128-LQH build)
- **When:** 2026-11-09 ~18:40 CST, main chat t4406u. Verbatim: "Remedy conflict."
- **Finding (checked by Physicist):** No mathematical conflict. The FPGA paper's own formal definition (§2, line 16; Lemma 2) is T3(0)=0; r=n mod 3; r=0: n//3; r=1: (4n+2)//3; r=2: (2n+1)//3, i.e. T3(3k)=k, T3(3k+1)=4k+2, T3(3k+2)=2k+1 — identical to T3_ref. The abstract's "Residue 0 and residue 1 divide exactly by 3" refers to the numerators n and 4n+2 being divisible by 3; "Residue 2 is floor division and equals (2n−1)/3" is also correct, since (2n+1)//3 = (2n−1)/3 = 2k+1 for n=3k+2.
- **Check:** T3_ref^539(4880) = 2 recomputed (Python); matches paper Table 1 orbit 4880→…→1 then the 1↔2 cycle.
- **Remedy:** keep T3_ref unchanged in code; close the OPEN issue as a wording ambiguity; add a docs note stating the numerator reading. No paper or frozen file edited.
