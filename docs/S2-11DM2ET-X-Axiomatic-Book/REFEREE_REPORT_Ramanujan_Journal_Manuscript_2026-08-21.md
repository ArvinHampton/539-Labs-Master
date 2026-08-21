# Referee Report — Ramanujan Journal Manuscript (2026-08-21)

**Document type:** Internal peer-review note (not journal submission)  
**Manuscript reviewed:** `Submission_Manuscript_Ramanujan_Journal_2026-08-20.txt`  
**Commit:** `f4d6dd3314a5357189555ba289ed1c2c6482a366` (2026-08-21 04:58 UTC)  
**Title:** Residual Packaging Identities and a Residual Analogue of Ramanujan's Fifth-Order Series  
**Author:** Arvin Hampton, 539 Labs  
**Target:** The Ramanujan Journal (Springer)  
**Recommendation:** **Do not submit this version.** An editor would desk-reject it. The q-series core can be salvaged after a rewrite.

Residual Discrete Algebra (539 COUNT) ≠ Resonant. Residual-flux provenance mandatory. Continuum ARCHIVE. This note is Category A arithmetic / q-series only.

---

## One-paragraph referee abstract

> The manuscript defines a mixed-scale family \(g_s(q)=\sum q^{n^2}/(-q^s;q^s)_n\) which for \(s=1\) is Ramanujan's fifth-order mock theta function \(f_0\). The double-sum identity of Section 4 is true and is classical Euler; it must be proved, not checked to degree 20. The vanishing of \(g_7\) coefficients on residue classes 3, 5, 6 modulo 7 is true and elementary. The claimed transformation law is not proved: the author's own bilateralisation note records that the quadratic-form matrix, multiplier, and holomorphic-projection check remain unwritten. Harmonic Maass of weight \(1/2\) and quantum modular of weight \(1/2\) are different statements and cannot be hedged with “or.” Section 2 (N_flux, undefined \(f_{\max}\), tautological packaging 18+521 and 3·68+5·67) is not q-series and will stop the paper at the editor. The map \(T_3\) as a rational formula is not integral on \(n\equiv 2\pmod{3}\); the corpus canonical map is integer division, equivalently the exact formula \((2n-1)/3\) on that class. The file is plain text, not a typeset submission. Do not send this text to Springer.

---

## What the paper is trying to do

Two pieces glued together.

**Piece 1.** Elementary arithmetic around 539: \(539=7^2\cdot 11\), \(3\cdot 68+5\cdot 67=539\), \(18+521=539\), and a ternary map \(T_3\).

**Piece 2.** The family
\[
g_s(q)=\sum_{n=0}^\infty \frac{q^{n^2}}{(-q^s;q^s)_n}.
\]
When \(s=1\) this is Ramanujan's fifth-order \(f_0\). The paper claims a double-sum, a triple-sum of signature (2,1), an Euler collapse, and that for \(s\in\{7,8,11\}\) the series is the holomorphic part of a weight \(1/2\) harmonic Maass form, or else quantum modular of weight \(1/2\), “by the classical Zwegers completion.”

Topic fit with the journal is real (q-series, mock theta functions, modular forms). Quality and originality, as submitted, are not.

---

## What is actually correct

1. The definition of \(f_0(q)=\sum q^{n^2}/(-q;q)_n\) is the standard fifth-order function of the last letter / lost notebook.
2. \(g_s(q)\) is not \(f_0(q^s)\), because \(f_0(q^s)\) has quadratic exponents \(s n^2\). The mixed scale is the one possibly new object.
3. \(539=7^2\cdot 11\), \(3\cdot 68+5\cdot 67=539\), and \(18+521=539\) are true and content-free as theorems.
4. The Section 4 double-sum identity is **true**. Proof: see companion note `Ramanujan_Journal_T3_Euler_g7_Corrections_2026-08-21.md`. Degree-20 expansion is not a proof.
5. \(\Phi(m;q)=(q^{m+1};q)_\infty\) is classical Euler, correctly specialised. Not new.
6. Coefficients of \(g_7\) vanish on classes 3, 5, 6 modulo 7. True. Proof in the companion note. Checked computationally through degree 80: no violations.

---

## Fatal problems

### F1. The main theorem is not proved

Section 6 asserts mock modularity (or quantum modularity) of \(g_s\) for \(s\in\{7,8,11\}\). There is no transformation law, no level, no multiplier, no shadow, no completed non-holomorphic term, and no numbered theorem.

The author's own `Bilateralisation_Complete_Status_2026-08-20.md` says the explicit matrix, the multiplier, and the check that the holomorphic projection recovers \(g_s\) remain a finite unwritten calculation. The manuscript claims the law is established. That is an overclaim.

Zwegers' machine applies after the quadratic form, the cone, and the character are written down. Mixed-scale \(n^2\) versus \(s\)-Pochhammer is not a substitution of “residual level and character into the classical order-5 law.” Partial theta series of this type are often quantum modular at roots of unity (Zagier) and often **not** holomorphic parts of harmonic Maass forms on a congruence subgroup. Pick one statement and prove it.

Status correction (this deposit): transformation law is **not closed**. Mechanism-level identification is not a theorem. See `Transformation_Law_STATUS_CORRECTION_2026-08-21.md`.

### F2. Section 2 will kill the submission

\(N_{\mathrm{flux}}=4880\) is not defined in the manuscript. It is \(\lfloor e^3\cdot 3^5\rfloor\) from the continuum model. \(f_{\max}\) is undefined. \(B'=\lfloor(N_{\mathrm{flux}}-f_{\max})/9\rfloor\) “with the conventional residual choice that yields \(B'=539\)” is circular. Back-solving gives \(f_{\max}\in[21,29]\). None of that is q-series.

A Ramanujan Journal editor who sees an unexplained flux integer in Section 2 will not send the paper to a mock-theta specialist.

\(3\cdot 68+5\cdot 67=539\) and \(18+521=539\) do not imply anything about \(g_7\), \(g_8\), or \(g_{11}\). The value \(s=8\) is not a factor of 539 and is not justified. If the series is interesting for every positive integer \(s\), say so and drop the packaging. If only 7, 8, and 11 matter, a theorem must name those levels.

### F3. \(T_3\) as written is not an exact integer formula

The manuscript writes
\[
T_3(n)=\frac{n}{3},\quad \frac{4n+2}{3},\quad \frac{2n+1}{3}
\]
by residue class, then says “with integer division” and “is integral.” Exact division fails on every \(n\equiv 2\pmod{3}\): \(n=2\) gives \(5/3\). Sixteen failures in \(\{0,\ldots,49\}\), all on the \(n\equiv 2\) branch.

The corpus canonical map (`scripts/hqcc_ternary_map_sympy.py`) is floor division, which is integral by construction. On \(n=3k+2\) one has
\[
\left\lfloor\frac{2n+1}{3}\right\rfloor=\frac{2n-1}{3}=2k+1.
\]
So the exact-integer write-up for a number-theory journal is
\[
T_3(n)=\begin{cases}
n/3 & n\equiv 0\pmod{3},\\
(4n+2)/3 & n\equiv 1\pmod{3},\\
(2n-1)/3 & n\equiv 2\pmod{3}.
\end{cases}
\]
That map is integral, and it agrees with the canonical floor map. \(T_3\) is unused in the \(g_s\) sections and can be omitted from a journal note.

### F4. Nothing new is proved, as submitted

After deleting Section 2 and the unproved modularity claim, what remains is a one-parameter interpolation of \(f_0\), a classical Euler expansion, a classical product identity, and an elementary congruence for \(s=7\). That is a remark, not a Ramanujan Journal article, until modularity is proved or a sharp conjecture is stated with evidence.

### F5. The file is not a submission

116 lines of plain text. No MSC codes, no keywords, no postal address, no email, no numbered theorems, no proofs, no LaTeX. The 19 August Google Doc had MSC 11F37, 11F30, 11B37, 11F50 and an email; this “final” manuscript dropped them.

Springer expects a typeset manuscript, an informative 100–250 word abstract, AMS classification, and a complete bibliography. References [1] and [2] lack years, volumes, and pages. Missing, given the claims: Bringmann–Ono, Zagier on quantum modular forms, Gordon–McIntosh, Folsom, Bringmann–Folsom–Ono–Rolen.

The 19 August draft was more honest: it posed Problems A–D and said no generating-function identity had been proved. The 20 August draft converted those open problems into a claimed theorem. That is the wrong direction.

---

## Strengths (keep)

- Mixed-scale \(g_s\) versus \(f_0(q^s)\) is a clean observation.
- Euler double-sum is correct (once proved).
- \(g_7\) residue vanishing is correct (once proved).
- Scope paragraph excluding continuum / holographic claims is the right hygiene for this journal.
- Acknowledgement of Andrews, Berndt, Hickerson, Mortenson, Zwegers is the right literature neighbourhood.

---

## What a submitable note would look like

One paper, one theorem. Cut everything that is not \(g_s\).

**Title suggestion:** A mixed-scale analogue of Ramanujan's fifth-order mock theta function \(f_0\).

Keep: definition of \(g_s\); Euler proof of the double-sum; residue theorem for \(g_s\) (general \(s\), or at least \(s=7\)); distinction \(g_s(q)\) versus \(f_0(q^s)\).

Then either:

**(A)** Prove modularity. Write the quadratic form on \((k,n)\), identify the cone, apply Zwegers or Hickerson–Mortenson, compute the shadow, and give the level and multiplier for at least one \(s\). Until those matrices exist, do not say “closed.”

or

**(B)** Do not claim modularity. Compute coefficients, radial limits at roots of unity, and a few identities, and state a precise conjecture: \(g_s\) is quantum modular of weight \(1/2\) on a specified group, or mixed mock modular of a specified type.

Delete \(N_{\mathrm{flux}}\), \(f_{\max}\), \(B'\), 18+521, fibre blocks 67 and 68, and \(T_3\) from the journal text. If 539 is only motivation, one sentence in a remark is the most it can be.

Typeset in LaTeX. Restore MSC, keywords, address, email. Number theorems. Write proofs. Complete the references.

---

## Assessment table

| Criterion | Grade | Note |
|-----------|-------|------|
| Topic fit | A− | Mock theta / q-series is on-scope |
| Correctness of Euler double-sum | A | True; proof missing in MS |
| Correctness of \(g_7\) vanishing | A | True; proof missing in MS |
| Correctness of \(\Phi\) collapse | A | Classical |
| \(T_3\) integrality as written | F | Rational formula fails; floor form is corpus-canonical |
| Section 2 packaging | F | Circular flux; tautologies |
| Modularity theorem | F | Asserted, not proved |
| Honesty vs internal notes | D | Bilateralisation already says matrices unwritten |
| Novelty | C− | Mixed-scale \(g_s\) is the only candidate |
| Submission format | F | Plain text, no MSC, incomplete refs |
| Category hygiene | B | Continuum excluded from the MS; N_flux still leaks in |

**Verdict:** Do not submit. Rewrite as a short \(g_s\) note with proofs, or prove the transformation law first.

---

## Checklist for next iteration

- [ ] Delete Section 2 from any journal-bound text (or reduce 539 to one motivational sentence)
- [ ] Prove the Euler double-sum (companion note already has the proof)
- [ ] Prove residue vanishing (companion note already has the proof)
- [ ] Either write Zwegers input (matrix, cone, shadow, level) or restate modularity as a conjecture
- [ ] Do not write “harmonic Maass or quantum modular”
- [ ] If \(T_3\) is kept anywhere: use the exact-integer formula with \((2n-1)/3\) on \(n\equiv 2\pmod{3}\)
- [ ] LaTeX, MSC, keywords, address, email, complete bibliography
- [ ] Do not overwrite `Submission_Manuscript_Ramanujan_Journal_2026-08-20.txt` until a replacement manuscript exists

---

*Referee note ends. 2026-08-21.*
