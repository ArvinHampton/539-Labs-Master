# FINDINGS — PR2 Tubulin biophysics literature check (PP item 4) — 2026-11-03
Lane: Physics Research 2 (PR2), Soft SF. REPORTS ONLY. No CERT. No RECS. Invent-ban: citations or ABSENT only; nothing invented. Video EXCLUDED.

## Live hashes (sha256, verified 2026-11-03 ~11:00 CST)
- OW reports/OWNER_WRITE_CAT_A_FOOLPROOF_539_CORPUS_LIFT_STOP_2026-11-03.md: 8a0325da19ba3802652a654523b681cf74a623d28a4f1a4484999420098a453b MATCH
- tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 MATCH, tip_touched NO
- corpus reports/539labs/539_Labs_Technical_Corpus.md: 5a8f863093c6eacb57a03b74b8c3906808111fbe43f6ba9677aebae4b8f17f9e (as cited by OW L9 and INTAKE L7)
- PP-FINDINGS-CATA_FOOLPROOF_2026-11-03.md: 4e70be9ad36c29149510620bb8749e9265759f55cf69f093693adb1f9fbefeae
- PP-FINDINGS-TUBULIN_22_TO_13_WILSON_2026-10-31.md: bdd77eab7bee46ede56b868493d42d8acb515fd1c1c944dd8a62fda44572b5f9
- PP-FINDINGS-TUBULIN_LAMBDA22_PROOF_2026-10-31.md: 2d99acf698d5cf73abe51feab5a58e88b182ddac199b2e634bbbcd3811101181
- PP-FINDINGS-TUBULIN_TORSION_MOVE_TO_PROVE_2026-10-31.md: bca0ed5b37ddd6ed8a9616cd508c08f9d063a3e15ee40807517e3a60ddc817f3
- PP-FINDINGS-TUBULIN_T3_STRESS_ENERGY_2026-10-31.md: f4872e817b13e3822c41a390f549c23c96ed44143786e7d05c60c790e0810925
- INTAKE_539LABS_TECHNICAL_CORPUS_2026-11-03.md: d75a0a3a71cbc32d029d6a439fe7714ef37f62f8643a4460f2b53e6deb76081f

On-disk lit: no peer-reviewed tubulin/MT literature found under /workspace/quantum-comp/ (only internal PP/OW/MR2 bridge notes). All citations below come from web lookups (DOI resolver / PubMed / publisher abstracts) this session.

## (A) 13 protofilaments, A/B lattice — CITATIONS
A1. Tilney LG et al. "Microtubules: evidence for 13 protofilaments." J Cell Biol 59(2):267–275, 1973. DOI 10.1083/jcb.59.2.267. (Title-level claim; abstract not quoted.)
A2. Mandelkow EM, Schultheiss R, Rapp R, Müller M, Mandelkow E. "On the surface lattice of microtubules: helix starts, protofilament number, seam, and handedness." J Cell Biol 102(3):1067–1073, 1986. DOI 10.1083/jcb.102.3.1067. Quote: "The tubulin monomers of brain microtubules reassembled in vitro are arranged on a 3-start helix, irrespective of whether the number of protofilaments is 13 or 14. The dimer packing is that of the B-lattice"; body: "With 13 protofilaments, the A-lattice could be helically symmetric, whereas the B-lattice could not"; "4-nm repeat of monomers … staggered by ~0.9 nm, thus generating a 3-start helix".
A3. Kikkawa M, Ishikawa T, Nakata T, Wakabayashi T, Hirokawa N. "Direct visualization of the microtubule lattice seam both in vitro and in vivo." J Cell Biol 127(6):1965–1971, 1994. DOI 10.1083/jcb.127.6.1965. Quote: "microtubules have a predominantly B lattice, but that A lattice bonds between tubulin subunits are found at the seam."
A4. Chaaban S, Brouhard GJ. "A microtubule bestiary: structural diversity in tubulin polymers." Mol Biol Cell 2017, PMID 29084910 (DOI not verified this session — cite by PMID). Quote (Fig. 1): "Adjacent protofilaments have a longitudinal offset of 9.2 Å between tubulins such that 13-protofilament microtubules have straight protofilaments."
Verdict A: PRESENT. Standard fact: 13-pf, 3-start (13_3) B-lattice with one A-lattice seam; hence NOT strictly helically symmetric (13-fold helical symmetry only in the A-lattice idealisation).

## (B) MT torsion / twist — CITATIONS
B1. Chrétien D, Fuller SD. "Microtubules switch occasionally into unfavorable configurations during elongation." J Mol Biol 298(4):663–676, 2000. DOI 10.1006/jmbi.2000.3696. Quote: "Protofilament skewing is restricted to within +/-2 degrees… Configurations with theoretical protofilament skew angles larger than +/-4 degrees … were not observed."
B2. Ray S, Meyhöfer E, Milligan RA, Howard J. "Kinesin follows the microtubule's protofilament axis." J Cell Biol 121(5):1083–1093, 1993. DOI 10.1083/jcb.121.5.1083. Quote: "those with supertwisted protofilaments, did rotate; the pitch and handedness of the rotation accorded with the supertwist measured by electron cryo-microscopy."
B3. Wade RH, Chrétien D, Job D. "Characterization of microtubule protofilament numbers. How does the surface lattice accommodate?" J Mol Biol 212(4):775–786, 1990. DOI 10.1016/0022-2836(90)90236-f. (Reference-list level; abstract not quoted.)
B4. Chaaban & Brouhard 2017 (A4): "non–13-protofilament microtubules … must accommodate by imposing a protofilament supertwist."
Verdict B: PRESENT for geometric twist (pf skew/supertwist; 13_3 ≈ 0°, others within ~±2°). Quantitative torsional rigidity (modulus) value: ABSENT this session (not located/verified; not supplied).

## (C) Coordinates 14–22 / Λ_22 physical meaning — ABSENT (model-internal)
No peer-reviewed biophysics source located assigning physical meaning to a 22-dimensional lattice Λ_22, ℤ^22/D_22, or "coordinates 14–22" for tubulin/MTs. Searched concepts: Λ_22/22-dim lattice + microtubule; none found. Only literature use of "14" is the 14-protofilament MT type (A2, B1) — a different object (protofilament count), NOT coordinates 14..22 of a 22-vector. Conflating them would be invented. Consistent with PP-FINDINGS-TUBULIN_LAMBDA22_PROOF L9 "NF-WHY: any physical/tubulin meaning of Λ_22, helicity, or the 9 extra coordinates."

## (D) PP item 4 cross-cite
PP-FINDINGS-CATA_FOOLPROOF (4e70be9a…) table row 4: "Wilson C1: (1+κ)^{-7/20} | FALSE under R_x const; corrected … PROVED under INVENTED assumption A1 | PROOF_22_TO_13 Phase 2 (not corpus)". No literal "refused" token found in that file or OW 8a0325da…; item 4 taken as this row. Lit relevance: (A)/(B) give no Wilson-RG exponent −7/20 or κ for tubulin — ABSENT in literature checked; A1 remains INVENTED per PP. The 22→13 reduction has biophysical support only for the "13" end (A); the "22" end is ABSENT (C).

## Constraints
tip untouched (sha MATCH 7cddb188…). No CERT. No RECS. No other lanes amended. Only FINDINGS_PR2_* / SOFTSF_PRESS_FINDINGS_PR2_* written. Invented content: NONE.
