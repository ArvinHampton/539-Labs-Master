# SOFTSF PRESS — PR1 literature check: BQP/NP/PH · C_HQH · 128-qutrit · mod-27 (2026-11-03)
Cite-only digest of PR1-FINDINGS-LIT_BQP_NP_PH_CHQH_QUTRIT128_MOD27_2026-11-03.md. Tip 7cddb188…dfc91 untouched. Catalog af2539b0…; corpus 5a8f8630…; Codex 01830934….

- BBBV 1997 (quant-ph/9701001; SIAM JC 26(5):1510, 10.1137/S0097539796300933) — VERIFIED: relative to a random oracle, NP ⊄ BQTime(o(2^{n/2})). The authors state it does "not rule out the possibility that NP⊆BQP."
- Bernstein–Vazirani (STOC'93; SIAM JC 26(5):1411, 10.1137/S0097539796300921) — SEARCH-ONLY (content VERIFIED via BBBV/Aaronson quotes): BPP ⊆ BQP ⊆ PSPACE; RFS oracle separation.
- Aaronson STOC 2010 (0910.4698; 10.1145/1806689.1806711) — VERIFIED: BQP vs PH "an open problem"; FBQP^A ⊄ FBPP^{PH^A}; decision separation conditional on GLN.
- Raz–Tal (ECCC TR18-107; STOC'19 10.1145/3313276.3316315; JACM 69(4) 10.1145/3530258) — VERIFIED (ECCC): "an oracle O relative to which BQP^O ⊈ PH^O". No arXiv id found.
- Unconditional: BQP ⊆ PP ⊆ PSPACE. BQP ⊆ NP is not known; it is false relative to oracles.
- C_HQH chain: the corpus has none (ABSENT). The Codex L65 says verbatim "BQP⊂C_HQH⊂NP-Complete" and gives no condition. A "⊆ NP" conditional form is ABSENT. Any such chain would imply BQP ⊆ NP, which is open and fails relative to an oracle, so the chain is unproven.
- 128-qutrit processor/ALU: ABSENT in experiment. The only sources are 539 Labs' own (Codex RTL, provisional patent claim). Largest native qutrit processors found: 5 qutrits (Blok, 2003.03307, VERIFIED) and 10-ion d≤7 (Ringbauer, 2109.06903, VERIFIED). Largest count found: 24 qubit-encoded qutrits (Nat. Commun. 2025, SEARCH-ONLY).
- Mod-27 hardware test: ABSENT. Theory only: mod-3^n adder (Bocharov et al., 1512.03824, VERIFIED).
