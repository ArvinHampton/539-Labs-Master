# order8 notes (disclosures; verdicts stand)
1. **M2c fit was under-resolved.** The preregistered 5-term fit on 6 points leaves out the t^{3/2} term, which biases A2 at about 1e−5 to 1e−3. m2posthoc.py is a new file, hashed before it ran, labelled descriptive. It refits with 8 points and terms up to t² for x = 1 and ⅓, giving max errors of 3.7e−7 and 5.2e−6. The M2c verdict stays FAIL.
2. **M2a/b at x = ½.** Here mean f = 0, so both the prediction and the measurement vanish (about 1e−15). That point is non-discriminating. x = 1 is the informative case.
3. **Interior M3 data.** M3 reuses order7's 660-τ arrays (read-only). The design is a fixed-matrix residual with one scalar, not a span test.
4. **Steering (3:42 PM CDT).** No weight −1 attack: odd weights are blocked by the parity obstruction.
5. **Reading.** The even piece has the form "D^{1/2} of the holomorphic projection of a weight-0 Siegel integral over the half unit-angle [ĉ1, ĉ′]". The natural next object is the boundary of Φ_orth over the full unit arc [ĉ1, γĉ1], which is Φ_0 from order7: twice the orthant angle. That suggests Θ_E plus its γ-image (the complementary cone) equals 𝓗(Φ_0), a full Hecke-type sum. Not tested here.
6. **Process.** nice, OMP_NUM_THREADS=1, ulimit -v 3000000. No push, no external sends. New files only.
