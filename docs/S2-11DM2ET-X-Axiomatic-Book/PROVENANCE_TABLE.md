# Integer Provenance Table (Front Matter)

**Single source of provenance.**  
Companion TeX: `Provenance_and_DepthMacros.tex`  
Depth macros: \(N_\star = 14\) always; \(\sigma = 539\) always. **Never write \(N_\star=539\).**

---

## Depth split (mandatory)

| Symbol | Value | Meaning | May equal the other? |
|--------|-------|---------|----------------------|
| \(\Nstar = N_\star\) | **14** | ACE / crude flux-bridge e-fold depth | **No** |
| \(\sigma = N_{\mathrm{HQCC}}\) | **539** | Model HQCC / resonant combinatorial depth | **No** |
| \(G_4\) | **539.9** s | Claimed gravitational breathing period | Not an integer depth |

Banach rates:

| Rate | Formula | Status |
|------|---------|--------|
| \(\lambda_{\mathrm{mean}}\) | \(4^{1/3}/3 \approx 0.529\) | Derived (ACE); free of 539 |
| \(\lambda_{\sigma}\) | \(\ln 3/\sigma = \ln 3/539\) | **Conditional** on \(\sigma=539\) only |

---

## Provenance codes

| Code | Meaning |
|------|---------|
| **A0** | Forced by Axiom 0 (three generations / multiplicity three) |
| **Res** | Residue-class / ternary map structure (\(T_3\), \(Q=n\bmod 9\)) |
| **Tower** | Tower lattice / flux integer construction (\(3^5\), \(W_{np}=e^3\)) |
| **Dem** | Flux democracy (tower-symmetric partition of seeds) |
| **ACE** | Completed map \(T^\sharp\) + stationary mean (no 539 in inputs) |
| **Mod** | Model / extra structure **not** forced by Res+Tower+Dem+ACE |
| **Pack** | Length packaging: \(L_{\mathrm{pref}}\) (Cat.\ A) + \(L_{\mathrm{body}}\) under principle (S); or single-shot \(L_{\mathrm{pack}}'\) |
| **(S)** | Minimal-action single max-tower seed clear — combination rule beyond pure atoms |
| **Cond** | Conditional on assuming \(\sigma=539\) (or \(|P|=61\) only via that route) |
| **Emp** | Empirical hypothesis to be tested (not a derivation) |

---

## Table: \(\{3,9,20,21,61,80,243,539,4880,539.9\}\)

| Integer | Symbol(s) | Value | Provenance | Status under No-Go |
|---------|-----------|-------|------------|--------------------|
| **3** | generations; branch modulus | 3 | **A0** | A priori. Forces ternary branching scale. |
| **9** | \(Q=n\bmod 9\) | 9 | **Res** (\(3^2\)) | Charge modulus from map structure; free of 539. |
| **20** | seed type / multiplicity | 20 | **Dem** + **Tower** | Democratic partition of flux into seed classes with 21. Free of 539. |
| **21** | seed type / multiplicity | 21 | **Dem** + **Tower** | Partner of 20 under democracy; free of 539. |
| **61** | \(\|P\|\) punctures | 61 | **Mod** | Not forced by Res+Tower+Dem+ACE. Input to \(w_j=\sigma+\|P\|j\) and \(\beta_{\mathrm{PBH}}=11/61\). |
| **80** | \(N_{\mathrm{flux}}/\|P\|\) | 80 | **Mod** (via 61) or combinatorial | \(4880/61=80\). Inherits provenance of 61 when used that way. |
| **243** | \(N_{\mathrm{tow}}=3^5\) | 243 | **A0** + **Tower** | Tower multiplicity; free of 539. |
| **539** | \(\sigma=N_{\mathrm{HQCC}}\) | 539 | **Pack** under (S) as *length*; **Mod**/interpretive as free *objects* | As **crypto round count**: \(L_{\mathrm{pack}}=18+521\) or \(\lfloor(N_{\mathrm{flux}}-f_{\max})/9\rfloor\) once packaging+(S) adopted (`Resonant_Layer_Resolved.md`). As **free \(T^\sharp\) object count**: still **not** forced (No-Go; Option 3). Never from ACE alone. |
| **4880** | \(N_{\mathrm{flux}}=\lfloor e^3\cdot 3^5\rfloor\) | 4880 | **Tower** (+ \(W_{np}=e^3\)) | Flux integer; free of 539. Enters crude bridge for \(N_\star\). |
| **539.9** | \(G_4\) (seconds) | 539.9 | **Emp** / **Mod** | Not an integer depth. Empirical period hypothesis; optional compatibility test only after non-circular spectral estimate. |

---

## Derived companions (not in the requested set, for ledger completeness)

| Object | Value | Provenance | Notes |
|--------|-------|------------|-------|
| \(\mathbb{E}_\pi[\chi]\) | \(\ln(4^{1/3}/3)\approx -0.6365\) | **ACE** + **Dem** | Free of 539 |
| \(\lambda_{\mathrm{mean}}\) | \(4^{1/3}/3\approx 0.529\) | **ACE** | Free of 539 |
| \(N_\star\) | **14** | **ACE** + **Tower** (\(4880\)) | **Never** set equal to 539 |
| \(L_{\mathrm{pref}}\) | **18** | \(\lfloor e^3/\ln 3\rfloor\) (Tower / instanton scale) | Free of 539 |
| \(L_{\mathrm{body}}\) | **521** | **Pack** + **(S)**: \(B_Q-f_{\max}\) | Free of 539 on RHS |
| \(L_{\mathrm{pack}}\) | **539** | \(L_{\mathrm{pref}}+L_{\mathrm{body}}\) or \(L_{\mathrm{pack}}'\) | Length only; resonant hard budget when adopted |
| \(\kappa_{\mathrm{dark}}\) | \(243/539\) | **Cond** | Uses \(\sigma\) |
| \(f_{\mathrm{snap}}\) | \(243/4880\) | **Tower** | Free of 539 |
| \(\beta_{\mathrm{PBH}}\) | \(11/61\) | **Mod** (uses \(\|P\|\)) | Free of 539 as integer, not free of 61 |
| \(w_j\) | \(539+61j\) | **Cond** + **Mod** | Unforced by No-Go data |
| \(\lambda=\ln 3/539\) | \(\ln 3/\sigma\) | **Cond** | Circular if used to *derive* free \(\sigma\); licit after \(\sigma:=L_{\mathrm{pack}}\) by design |

---

## Forbidden identifications

| Forbidden | Reason |
|-----------|--------|
| \(N_\star = 539\) | Conflates ACE e-fold depth with HQCC model depth |
| \(N_\star = \sigma\) | Same |
| \(\lambda_{\mathrm{mean}} = \ln 3/539\) | Different objects; left free of 539, right conditional |
| “Democracy \(\Rightarrow 539\)” | Blocked by No-Go Theorem |
| “ACE \(\Rightarrow w_j=539+61j\)” | Unforced |
| “Free \(T^\sharp\) basins \(=539\)” | Refuted for executed seed-orbit / C2 packages |
| “Resonant layer = mysterious free dynamics” | Superseded: resonant layer = packaging as hard budget (`Resonant_Layer_Resolved.md`) |

---

## Allowed short phrases

- “\(N_\star=14\) from ACE + flux bridge.”
- “Conditional on \(\sigma=539\), \(\lambda=\ln 3/\sigma<1\).”
- “Empirical \(\hat T\); test compatibility with \(G_4=539.9\) afterward.”
- “\(f_{\mathrm{snap}}=243/4880\) from towers and flux only.”
- “Crypto \(\sigma:=L_{\mathrm{pack}}=18+521\) under packaging + (S); free basins remain two and short.”
- “Option 3 default for free-dynamics 539 objects; Bott paused.”

---

## File links

| File | Role |
|------|------|
| `Provenance_and_DepthMacros.tex` | Book chapter + LaTeX macros |
| `CLOSED_CONSTANTS.md` | Numeric closed ratios (must respect this table) |
| `NoGo_Theorem_Canonical.md` | Why 539 is not forced |
| `ACE_Status_of_Record.md` | Locked ACE / \(N_\star=14\) ledger |
