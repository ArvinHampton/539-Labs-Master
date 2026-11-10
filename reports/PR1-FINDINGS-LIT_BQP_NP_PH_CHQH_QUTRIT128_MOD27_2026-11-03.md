# PR1 FINDINGS — Literature check: BQP vs NP/PH · C_HQH chain wording · 128-qutrit / mod-27 hardware
Role: Physics Research 1 (Project Quantum Comp), write-only, cite-only. No invented content, no proofs, no recommendations.
Date: 2026-11-03 ~11:02 CST. Tip and obs-data files NOT edited.

## §0 Live hashes (sha256, taken 2026-11-03 ~11:02 CST)
| Role | Path | sha256 |
|---|---|---|
| tip | /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (= required; untouched) |
| obs-data (untouched) | /workspace/obs-data-PR1-HEPP-QM-GR.md | 6c680789ff64a7bb1a83276690e20a1748d8d2a31f19a97b869c13109b77f33d |
| catalog | quantum-comp/reports/ENTANGLEMENT_DATASETS_CATALOG_2026-10-25.md | af2539b05b24b48559c43a95ac00848650d0c3f19c20674bb24c3ab338a7b99c |
| corpus | quantum-comp/reports/539labs/539_Labs_Technical_Corpus.md | 5a8f863093c6eacb57a03b74b8c3906808111fbe43f6ba9677aebae4b8f17f9e |
| corpus Codex | quantum-comp/reports/539labs/539_Labs_Technical_Corpus_Codex_2026-11-03.txt | 0183093491115f3c7928446eaa5d9c15a0b30bd32d09acdd7484a67799c1cc21 (matches its sidecar) |

Status key: VERIFIED = abstract/landing page opened this run. SEARCH-ONLY = seen in search results only, page not opened.

## §1 BQP vs NP and BQP vs PH — citations and verbatim statements
1. **Bernstein & Vazirani, "Quantum Complexity Theory."** STOC 1993, pp. 11–20, DOI 10.1145/167088.167097; SIAM J. Comput. 26(5):1411–1473 (1997), DOI 10.1137/S0097539796300921. Status: SEARCH-ONLY (DOIs from the reference lists of DOI landing pages; the BV paper itself was not opened). Content as quoted by VERIFIED secondary sources:
   - BBBV (arXiv quant-ph/9701001, §1): "Bernstein and Vazirani [4] proved that BPP ⊆ BQP ⊆ PSPACE … They actually proved that relative to an oracle, the recursive Fourier sampling problem can be solved in BQP, but cannot even be solved by Arthur-Merlin games [1] with a time bound of n^{o(log n)} … They conjecture that the recursive Fourier sampling cannot even be solved in the unrelativized polynomial-time hierarchy."
   - Aaronson 0910.4698 §1: "In their original 1993 paper defining BQP, Bernstein and Vazirani [11] showed that BPP⊆BQP⊆P^{#P}." Footnote: "The upper bound was later improved to BQP⊆PP by Adleman, DeMarrais, and Huang [3]."
2. **Bennett, Bernstein, Brassard & Vazirani, "Strengths and Weaknesses of Quantum Computing."** SIAM J. Comput. 26(5):1510–1523 (1997), DOI 10.1137/S0097539796300933 (DOI SEARCH-ONLY); arXiv quant-ph/9701001. Status: VERIFIED (arXiv opened).
   - Abstract: "we address this question by proving that relative to an oracle chosen uniformly at random, with probability 1, the class NP cannot be solved on a quantum Turing machine in time o(2^{n/2}). We also show that relative to a permutation oracle chosen uniformly at random, with probability 1, the class NP∩co–NP cannot be solved on a quantum Turing machine in time o(2^{n/3})."
   - Theorem 3.5: "For any T(n) which is o(2^{n/2}), relative to a random oracle, with probability 1, BQTime(T(n)) does not contain NP."
   - §1 caveat: "We should emphasize that they do not rule out the possibility that NP⊆BQP."
3. **Aaronson, "BQP and the Polynomial Hierarchy."** STOC 2010, pp. 141–150, DOI 10.1145/1806689.1806711 (DOI SEARCH-ONLY); arXiv 0910.4698. Status: VERIFIED (arXiv opened).
   - Abstract: "The relationship between BQP and PH has been an open problem since the earliest days of quantum computing."
   - Theorem 1: "There exists an oracle A relative to which FBQP^A ⊄ FBPP^{PH^A}".
   - Theorem 3: "Assuming the Generalized Linial-Nisan Conjecture, there exists an oracle A relative to which BQP^A ⊄ PH^A … Unconditionally, there exists an oracle A relative to which BQP^A ⊄ BPP_path^A and BQP^A ⊄ SZK^A."
   - §1: "Recursive Fourier Sampling yields oracles A relative to which BQP^A ⊄ NP^A and indeed BQP^A ⊄ MA^A." Also: "Bennett et al. [9] gave oracle evidence that NP⊄BQP, and while no one regards such evidence as decisive, today it seems extremely unlikely that quantum computers can solve NP-complete problems in polynomial time."
4. **Raz & Tal, "Oracle Separation of BQP and PH."** ECCC TR18-107 (31 May 2018); STOC 2019, pp. 13–23, DOI 10.1145/3313276.3316315; J. ACM 69(4) (2022), DOI 10.1145/3530258. arXiv id: none found / not opened. Status: VERIFIED (ECCC page opened); the STOC/JACM DOIs are SEARCH-ONLY (the doi.org JACM abstract came back in search results and matches the ECCC abstract).
   - Abstract: "By well known reductions, this gives a separation of the classes Promise-BQP and Promise-PH in the black-box model and implies an oracle O relative to which BQP^O ⊈ PH^O."
5. **Unconditional (non-oracle) results, as stated in the VERIFIED sources above:** BPP ⊆ BQP ⊆ PSPACE (BV, quoted by BBBV); BQP ⊆ P^{#P}, later improved to BQP ⊆ PP (Adleman–DeMarrais–Huang, quoted by Aaronson); BQP^BQP = BQP (BBBV Cor. 4.15). No source opened here shows unconditionally either BQP ⊆ NP or NP ⊆ BQP. BBBV adds that conclusively proving BQP ≠ BPP would require resolving P vs PSPACE. All the separations are relative to an oracle.

## §2 On-disk wording of the "BQP … C_HQH … NP" chain (verbatim)
Command run: rg 'C_HQH|HQH|BQP' under /workspace (binaries and base64 excluded).
- **Corpus** `539_Labs_Technical_Corpus.md` (5a8f8630…): **ABSENT.** The file contains no "C_HQH" or "BQP" string. Related lines:
  - L12: "The induced path-state cancellation bounds $N - |W|$ directly reduce to weak NP-completeness over the unit-coefficient binary slice via exact subset sum mappings …"
  - L53: "* **Slide 3: Silicon Execution:** Hardware execution blueprint using the 128 Logic-Qutrit Hardware ALU matrix."
- **Codex** `539_Labs_Technical_Corpus_Codex_2026-11-03.txt` (01830934…):
  - L64–65: "The complexity of reversing an HQH-539-512 digest is formally classified as sitting within a unique complexity slice strictly between BQP (Bounded-Error Quantum Polynomial-Time) and NP-Complete:" / "\(\text{BQP}\subset \mathcal{C}_{\text{HQH}}\subset \text{NP-Complete}\)"
  - L210: "• The 539 Solution: Introducing a completely separate complexity slice lying between BQP and NP-Complete via 3-adic metrics."
  - The text gives no condition, assumption, or proof for this chain. It states the chain as a classification.
- **Live site capture** `live_check/page_encrypt.html` (c580539c…) L20 meta: "… the patent-protected 128 Logic-Qutrit Hampton Processor — a new computational hardness class harder than BQP."
- **Prior audit** `quantum-comp/bridges/PROFESSOR_PROOF/PP-FINDINGS-CATA_FOOLPROOF_2026-11-03.md` (4e70be9a…) L21: "| 10 | BQP ⊂ C_HQH ⊂ NP-Complete | FALSE (∅∈BQP not NP-complete); repaired ⊆NP reading open/ABSENT (Raz–Tal oracle) | Codex §2.2 | §10 |"
- **A conditional form "BQP ⊆ C_HQH ⊆ NP" (with ⊆ NP): ABSENT on disk.** The only on-disk wording is the Codex's strict "⊂ … ⊂ NP-Complete".
- **What the cited results bear on (cite-only):** any chain of the form BQP ⊆ X ⊆ NP would imply BQP ⊆ NP. Per §1, that inclusion is open. Relative to oracles it fails: Aaronson §1 states RFS gives BQP^A ⊄ NP^A, and Raz–Tal give BQP^O ⊈ PH^O ⊇ NP^O. Separately, BBBV gives oracle evidence against NP ⊆ BQP. No VERIFIED source supports the chain unconditionally, so on the literature it can only be an unproven or conditional claim.

## §3 Qutrit hardware: 128-qutrit processor/ALU and mod-27 test
- (a) **128-qutrit processor or ALU in experimental literature: ABSENT.** Searches found no demonstrated device. The only on-disk sources are 539 Labs' own: Codex L102 "MODULE 4: HARDWARE ARCHITECTURE (128 LOGIC-QUTRIT ALU)" (a SystemVerilog RTL listing, `qutrit_alu_core.sv`, L115–166); `539-labs-nsf-project-pitch.md` (c74947ee…) L129 "patent-protected 128 LQH Processor (U.S. provisional 64/093,263, filed 2026-06-17)"; `zenodo-arvin-hampton-full.md` (e48056d8…) L781 "128-Logical-Qutrit Hampton Processor 128 qutrits → 3¹²⁸ …". Codex L227 itself lists "Deployment … into physical field-programmable qutrit emulation arrays" as a future "Phase 2". Note that 2'b-encoded RTL is classical ternary logic, not a quantum device.
- Largest demonstrated, for context:
  - Superconducting transmon: Blok et al., "Quantum Information Scrambling on a Superconducting Qutrit Processor," arXiv 2003.03307 (published in Phys. Rev. X 11, 021010 (2021); the venue is SEARCH-ONLY). VERIFIED: "we have demonstrated a five-qutrit quantum processor built from superconducting transmon circuits" (8-transmon ring, 5 used).
  - Superconducting multipartite: "Extending the computational reach of a superconducting qutrit processor," npj Quantum Inf. (2024), DOI 10.1038/s41534-024-00892-z. SEARCH-ONLY: 3-qutrit GHZ, "F=0.818" unmitigated, "0.951" mitigated.
  - Trapped-ion native qudits: Ringbauer et al., "A universal qudit quantum processor with trapped ions," arXiv 2109.06903. VERIFIED: "local Hilbert space dimension of up to 7"; entangling gates benchmarked in "3 and 10 ion string[s]".
  - Trapped-ion (Yb+), arXiv 2310.20432 (PT-symmetry). SEARCH-ONLY: "a chain of ten 171Yb+ ions … qudit dimension up to d=6"; "parallel computation on 5 out of 10 ions" (single-qudit only).
  - Qubit-encoded qutrits: "Qutrit toric code and parafermions in trapped ions," Nat. Commun. (2025), DOI 10.1038/s41467-025-61391-z. SEARCH-ONLY: "Z3 toric code state on 24 qutrits (obtained by encoding one qutrit into two qubits)" on Quantinuum H2 (56 qubits). This is the largest qutrit count seen, but it is emulated on qubits.
  - Photonic: Nat. Commun. (2025) s41467-025-59717-y. SEARCH-ONLY: three- and four-photon three-level GHZ.
- (b) **Mod-27 (3^3) arithmetic test on qutrit hardware: ABSENT.** No experimental source was found. Theory only: Bocharov, Cui, Roetteler, Svore, "Improved Quantum Ternary Arithmetics," arXiv 1512.03824, QIC 16 (2016). VERIFIED. §4.1: "To add two n-qutrit numbers modulo 3^n, we simply do not compute the the high carry trit c_n." With n=3, this gives mod 27, as a circuit construction only. On disk, mod-27 appears only in internal map analyses (e.g. grok-chats extracts "mod-27 merge automaton") and not as a hardware test.

## §4 Scope note
This file contains citations and quotes only. It offers no proofs and no recommendations. No messages were sent. The tip sha still equals 7cddb188…dfc91.
