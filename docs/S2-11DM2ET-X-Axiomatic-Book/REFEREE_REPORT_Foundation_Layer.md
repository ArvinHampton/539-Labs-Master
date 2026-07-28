# Referee Report — S²-11DM²ET-X Axiomatic Book (Foundation Layer)

**Document type:** Internal peer-review note (not journal submission)  
**Scope:** Foundation layer as of the No-Go / ACE alignment (`NoGo_Theorem_Canonical.*`, `NoGo_FluxDemocracy_ResonantAttractor.*`, `ACE_Status_of_Record.md`, supporting ACE / empirical notes)  
**Recommendation:** **Revise and clarify** — the no-go logic is sound and valuable; several claims elsewhere in the book still need the same separation discipline.

---

## Summary for the author

The foundation layer is strongest where it is most self-critical. The **No-Go Theorem** correctly separates (i) data free of \(539\) from (ii) conclusions that insert \(539\), \(|P|=61\), or period \(539.9\). Closing an ACE for the completed map \(T^\sharp\) with
\[
\mathbb{E}_\pi[\chi]\approx -0.6365,\qquad
\lambda_{\mathrm{mean}}\approx 0.529,\qquad
N_\star=14
\]
is a genuine advance: it supplies the a priori estimate the older obstruction note demanded, and it **strengthens** the no-go for the model depth \(539\) rather than quietly erasing it.

The book will only be coherent if **every** slogan that still treats \(539\), \(G_4=539.9\), \(\kappa_{\mathrm{dark}}=243/539\), or \(w_j=539+61j\) as “parameter-free from Axiom 0 alone” is rewritten to match this ledger: either **conditional on \(\sigma=539\)**, **empirical hypothesis**, or **extra axiom**.

---

## Strengths

1. **Honest obstruction theorem.**  
   Cirularity of “assume \(N_\star=539\Rightarrow\lambda=\ln 3/539\Rightarrow\) terminate in \(539\) steps” is diagnosed cleanly. Democracy is not allowed to launder the input.

2. **Explicit, checkable numerics.**  
   Local factors \(\chi_0,\chi_1,\chi_2\), unrestricted mean \(\frac13\ln(8/27)\), stationary mean \(\ln(4^{1/3}/3)\), and \(N_\star=\lceil\ln 4880/|\mathbb{E}_\pi[\chi]|\rceil=14\) are elementary and reproducible.

3. **Completion rule discipline.**  
   Restricting \(T^\sharp\) to min charge defect among \(k\in\{0,1,2\}\) prevents smuggling a global period into the map definition.

4. **Empirical escape hatch, correctly scoped.**  
   Periodogram / multitaper protocol with \(539.9\) only as a post-estimate compatibility test is the right scientific posture.

5. **Dictionary split.**  
   Separating a priori cocycles \(c_j\) (and possibly shells from \(1001\)) from \(\sigma\)-anchored windings \(w_j\) is the right individuality hygiene.

---

## Major comments (must address for internal consistency)

### M1. Global slogans vs. No-Go ledger

The README and closed-constants material still present
\[
G_4=539.9,\quad |P|=61,\quad \kappa_{\mathrm{dark}}=243/539,\quad w_j=539+61j
\]
as key constants “derived parameter-free from Axiom 0.” Under the No-Go Theorem those are **not** consequences of residue structure + 243-tower topology + flux democracy + \(T^\sharp\).

**Required:** A single front-matter status table with columns  
*Derived without 539* | *Conditional on \(\sigma=539\)* | *Empirical hypothesis* | *Extra structure*.  
Every later chapter must cite that table when using \(539\).

### M2. Two depths, one name

The framework now has two integer depths in play:

| Symbol | Value | Provenance |
|--------|-------|------------|
| \(N_\star\) (ACE/crude bridge) | \(14\) | Non-circular from \(\mathbb{E}_\pi[\chi]\) and \(4880\) |
| \(\sigma\) (model / HQCC / resonant) | \(539\) | Outside the no-go data |

**Required:** Never use \(N_\star\) for both. Keep \(N_\star\) for the ACE depth and \(\sigma\) (or \(N_{\mathrm{HQCC}}\)) for the resonant length. Audit all TeX macros and status notes.

### M3. Justification of \(\mathbb{E}_\pi[\chi]\)

The stationary mean assumes (i) branch-2 leading ratio \(\to 1/3\) after \(T^\sharp\), and (ii) 3-adic equidistribution consistent with the 243-tower average. Both are modeling hypotheses free of \(539\), but they are not automatic theorems from the residue table alone.

**Required:** In `ACE_Resolution_CompletedMap`, state precise measure-theoretic hypotheses and which parts are proved vs. assumed. The no-go does not need more; any positive claim of “termination in 14 steps for all seeds” does.

### M4. Conditional escape vs. claimed lift

Older text said ACE was missing; newer text supplies ACE at depth \(14\). Do not describe the no-go as “lifted.” It is **lifted only for depth 14**; it **stands for 539**.

---

## Minor comments

1. **Wording “blocked.”**  
   Fixed in the canonical files: conclusions (a)–(c) *hold*; programme claims (a′)–(c′) are *blocked*. Keep that dual form in all abstracts and slides.

2. **Lemma on branch mean \(2/3\).**  
   Arithmetic mean of ratios is not the same object as \(\exp(\mathbb{E}[\chi])\). The chapter already uses the log-mean for ACE; avoid mixing the two in one sentence without labels.

3. **Composition \(18+1+520=539\).**  
   Flag every occurrence as *candidate bridge only if summands are independently forced*.

4. **Empirical protocol.**  
   Pre-registration language is good; add an explicit default horizon \(H\) independent of \(539\) and a multiple-testing note if several spectral methods are tried.

5. **Cross-references.**  
   Flux-democracy chapter → canonical no-go → ACE status of record should form a one-way dependency chain with no contradictory status sentences.

---

## Assessment of the No-Go Theorem (technical)

| Criterion | Grade | Note |
|-----------|-------|------|
| Clarity of hypotheses | A− | Equidistribution clause could be more formal |
| Separation of circular inputs | A | Excellent |
| Correctness of elementary identities | A | Verified numerically |
| Strength of conclusion for \(\lambda=\ln 3/539\) | A | Sound |
| Strength of conclusion for \(w_j=539+61j\) | A− | Relies on uniqueness needing the anchor |
| Consistency with ACE \(N_\star=14\) | A | After alignment edits |
| Compatibility with empirical programme | A | Corollary is well posed |

**Verdict on the no-go material:** Accept as foundation-layer canon, subject to M1–M2 book-wide consistency.

---

## Assessment of the book as a whole (foundation layer)

| Area | Status |
|------|--------|
| Axiom 0 / individuality composite dictionary | Conditional part \(w_j\) must stay conditional |
| Closed continuum ratios using \(539\) or \(61\) | Relabel as model inputs or derived-under-\(\sigma\) |
| Photon-ring / \(f_{\mathrm{snap}}=243/4880\) | \(4880\) and \(243\) can stay; do not smuggle \(539\) without flag |
| GW250114 / three clocks | Keep clock separation; Clock tied to \(G_4=539.9\) is hypothesis-grade |
| Wilson / QCD notes | Appropriately modest if they refuse to derive \(539\) from confinement |
| Empirical phase lock / holographic window | Right methodology; report nulls as nulls |

**Overall recommendation:**  
**Major revision of status language and constant provenance; no-go/ACE core is in good shape.**

---

## Suggested author checklist (next iteration)

- [x] Front-matter provenance table for all integers \(\{3,9,20,21,61,80,243,539,4880,539.9\}\) — `PROVENANCE_TABLE.md`, Ch.~\ref{ch:provenance}
- [x] Macro split: `\Nstar`/`\Nstarval` = 14 only; `\sigmaHQCC`/`\sigmaval`/`\NHQCC` = 539 only
- [x] README “Key Constants” rewritten to match No-Go ledger
- [ ] One sentence in every chapter that uses \(539\): “Input / conditional / empirical — not from democracy+ACE”
- [ ] ACE chapter: proved vs. assumed for equidistribution and branch-2 asymptotics
- [x] Provenance chapter + macros loaded from main book TeX
- [x] Migrate remaining hard-coded \(N_\star=539\) phrases in circular-schema / ACE_Open notes to \(\sigma\)

---

## One-paragraph referee abstract

> The No-Go Theorem of the foundation layer is correctly stated and, after alignment with the completed-map ACE, correctly strengthened: residue structure, 243-tower topology, flux democracy, and min-defect completion determine a negative stationary expansion mean and a non-circular depth \(N_\star=14\), not the Banach rate \(\lambda=\ln 3/539\) or the generational windings \(w_j=539+61j\). Empirical search for a period near \(539.9\) remains legitimate only as a hypothesis test. The principal defect of the book is not the no-go chapter but residual global language that still markets \(539\) and \(G_4\) as parameter-free outputs of Axiom 0. Fix provenance, rename depths, and the foundation layer becomes internally consistent.

---

*Referee note ends.*
