# ADDENDUM U — Owner t4127 3-page PDF (RELAY-BASED; source NOT readable; No CERT; no .tex)

## Source
- The cited path /home/box/agent-data/agents/60cad811…/attachments/399c69d0….pdf does NOT exist on PP's box (ls fails).
- I did not try to get around this. There is no full-source read and no render check.
- Please copy the file to /workspace/quantum-comp/intake/, and I will do a U.1 line-by-line confirmation.

## Findings on the relayed lines (checked against R.1/S/T)
- **p1 L14 and the ledger: WRONG.** "All other 46 non-identity coefficients" leaves out the identity. In the fixed table, the identity 1 = (0,0,0) is in O9 with weight C = 2 + √35. Correct statement: all 47 coefficients other than a_{xy³} remain unchanged, including a_1 = 2 + √35 and a_{y³} = 0. Exactly one of the 48 coefficients changed.
- **p2 L64: FALSE as worded.** "√35 irrational over Q(√35)" is wrong, since √35 lies in Q(√35). Correct statement: λ = u + v√35 with u, v ∈ Q (integers here) and v ≠ 0, and √35 ∉ Q, so λ ≠ 0.
- **p2 L66: FALSE in general.** It says invertibility of H′ is NECESSARY for full boundary rank. The real criterion is the block one, rank M = 24 + rank H01. Invertibility of H′ was checked separately; it is neither necessary nor sufficient by itself.
- **Title.** It still says "path solutions." It should say vector (trajectory) solutions; vector uniqueness ≠ path uniqueness.
- **Standalone use.** Section 3 refers to the original table and spectra, but they are not reproduced. The original A/B/C/D weights are not uniform; say so explicitly.
- **Retained correct:**
  - Both cross blocks get +I.
  - λ′ = λ + (−1)^p, with the separate nonzero proof.
  - The R.1 eigenvalues (integer + nonzero √35 multiple).
  - Vector ≠ path uniqueness.
  - Capacity OPEN.

## OPEN
- Full-source confirmation, which needs a readable copy.
- The N/W/capacity link.

## U.1 — full-source confirmation (intake owner-20261105-1944/OWNER_TUNED_VECTOR_UNIQUENESS_1944.pdf, 3 pages, sha b41dce00…)
- I read the full source. The relayed lines match:
  - L1 title: "Uniqueness of Path Solutions…"
  - L15 and L98: "all other 46 non-identity"
  - L64: "irrationality … over the coefficient field Q(√35)"
  - L66: "non-singularity of H′ is necessary"
- Rendering: the extracted text contains literal LaTeX delimiters such as `\(` and `\mathbb`. So the PDF prints LaTeX source rather than typeset math.
- No additional findings. The corrections above stand, with my own typo fixed in the L14/L98 item: the unchanged coefficients are those other than xy³, not other than y³.
