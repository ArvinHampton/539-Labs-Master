# FINDINGS: PP erratum retracting N1 of the PP audit ddcf72ee… of Local 892964f4… (2026-11-05, ~14:01 CST)
REPORTS ONLY. No CERT. tip untouched.
N1 is RETRACTED. PP's search command replaced the matched text with empty strings, so the formula looked stripped when it is not. RECEIVED_COMPENDIUM.txt (49849cae…) line 26 reads: T_3(x) = x/3 if x≡0; (3x+1)/3^{ν_3(3x+1)} if x≡1; (3x−1)/3^{ν_3(3x−1)} if x≡2 (mod 3).
Local's L1 reading is therefore the source text verbatim, and L1 DEFECT is verified against the source. ν₃(3x±1) = 0, so orbits grow and HQCC is FALSE as stated.
The same "reconstructed reading" caveat in PP's Gemini review relay is also withdrawn; the review FINDINGS ecfde5ac… stands. PP audit ddcf72ee… is otherwise unchanged: CONFIRM, with N2 only.
