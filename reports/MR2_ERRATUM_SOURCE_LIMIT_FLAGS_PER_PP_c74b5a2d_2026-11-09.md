# MR2 erratum — source-limit flags a4084322…, per PP audit c74b5a2d… — 2026-11-09 ~18:28 CST (America/Chicago)

**Role:** Math Research 2. Additive new file only. REPORTS ONLY. No CERT. Tip `7cddb188…` untouched. No Gemini. Nothing sent outside. **A citation alone never upgrades a status to PROVED.**

## Authority / integrity

| Object | sha256 | Note |
|---|---|---|
| PP audit | `c74b5a2d67c29d262977692dde59e83ee6dcd04af5bb4c4a55006527386f3abc` | `FINDINGS_PP_CITATION_SCOPE_REGRADE_OW_36683379_NL_ERRATUM13_MR2_FLAGS_2026-11-09_1832.md` — MATCH (re-hashed this pass) |
| MR2 flags (target) | `a40843225c36e0010ba82375ab440f6ef23eac685aa49aa419caeac7515fce8b` | not overwritten; fixes live here |
| NL Erratum 13 | `b5190ea8c908200f8dab6455bcd4462143cad8b4e01993c88425c925be003412` | `NL_ERRATUM13_CITATION_MATH_CHECKS_OW_36683379_2026-11-09_1818.md` — MATCH |
| OW 36683379 | `36683379e18ac23c46236b37ed45ec1ddf70a93ac9094d2abc476c953433904f` | all-sources, math-checked |
| tip | `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` | untouched |

PP C1–C9 and Fixes **MR2** 1–5 from `c74b5a2d…` are applied below.

Crossref checks: `curl` → `https://api.crossref.org/works/<doi>` on **2026-11-09 ~18:27–18:28 CST (America/Chicago)**.

---

## Fix 1 — Taubes pin for Y12 (PP C2)

**REFUTED as the Y12 source:** Taubes, “Stability in Yang-Mills theories,” *Commun. Math. Phys.* **91** (1983) 235–263, doi `10.1007/BF01211160`.

Crossref return (this pass):
- title: Stability in Yang-Mills theories
- authors: Taubes
- container: Communications in Mathematical Physics
- issued: [1983, 6]; vol/issue/page: 91 / 2 / 235-263
- DOI: 10.1007/bf01211160

**Pinned Y12 source (replacement):** Taubes, “Self-dual Yang-Mills connections on non-self-dual 4-manifolds,” *J. Differential Geom.* **17** (1982) 139–170, doi `10.4310/jdg/1214436701`.

Crossref return (this pass):
- title: Self-dual Yang-Mills connections on non-self-dual 4-manifolds
- authors: Taubes
- container: Journal of Differential Geometry
- issued: [1982, 1, 1]; vol/issue/page: 17 / 1 / 139-170
- DOI: 10.4310/jdg/1214436701

The flags file’s “likely CMP 91” wording is withdrawn. Y12 bibliographic pin = **JDG 17 (1982) 139–170** only. Math of Taubes’s gluing/contraction (NL E13 M7) stays **cited, math-unchecked CONDITIONAL** — not PROVED by this pin.

---

## Fix 2 — Jenni bibliographic pin (PP C3)

**Jenni** = *Commentarii Mathematici Helvetici* **59** (1984) 193–203, doi `10.1007/BF02566345`.

Crossref return (this pass):
- title: Ueber den ersten Eigenwert des Laplace-Operators auf ausgewählten Beispielen kompakter Riemannscher Flächen
- authors: Jenni
- container: Commentarii Mathematici Helvetici
- issued: [1984, 12]; vol/issue/page: 59 / 1 / 193-203
- DOI: 10.1007/bf02566345

The flags file’s “1981/1984” ambiguity is corrected to **1984**. (CMH 54 / 1979 by Jenni is a different paper — not used.)

**Primary PDF:** doi.org → Springer article page. `content/pdf/10.1007/BF02566345.pdf` returned HTML (Client Challenge / non-PDF magic), not a PDF. **Global-maximality statement: left pending** (math-unchecked CONDITIONAL), consistent with PP B-M13 and C3. Bolza *length formulas* remain numerically verified as in the flags file / PP B-M12; that does **not** prove Jenni’s global-max theorem.

---

## Fix 3 — CMP 145 DOI; name Bourguignon–Lawson for CMP 79 (PP C1)

**Sadun–Segert CMP 145** DOI (omitted in flags): `10.1007/BF02099143`.

Crossref return (this pass):
- title: Non-self-dual Yang-Mills connections with quadrupole symmetry
- authors: Sadun, Segert
- container: Communications in Mathematical Physics
- issued: [1992, 4]; vol/issue/page: 145 / 2 / 363-391
- DOI: 10.1007/bf02099143

**Follow-on to BLS PNAS:** **Bourguignon–Lawson** (no Simons), “Stability and isolation phenomena for Yang-Mills fields,” *Commun. Math. Phys.* **79** (1981) 189–230, doi `10.1007/BF01942061`.

Crossref return (this pass):
- title: Stability and isolation phenomena for Yang-Mills fields
- authors: Bourguignon, Lawson
- container: Communications in Mathematical Physics
- issued: [1981, 3]; vol/page: 79 / 189-230
- DOI: 10.1007/bf01942061

**Also reconfirmed (Crossref, this pass):**

| Paper | DOI | Crossref summary |
|---|---|---|
| SSU PNAS 86 (1989) 8610–8613 | `10.1073/pnas.86.22.8610` | Sibner, Sibner, Uhlenbeck; PNAS; issued [1989, 11]; 86/22/8610-8613 |
| Sadun–Segert Bull. AMS 24 (1991) 163–170 | `10.1090/S0273-0979-1991-15978-1` | Sadun, Segert; Bull. AMS; issued [1991]; 24/1/163-170 |
| BLS PNAS 76 (1979) 1550–1553 | `10.1073/pnas.76.4.1550` | Bourguignon, Lawson, Simons; PNAS; issued [1979, 4]; 76/4/1550-1553 |

---

## Fix 4 — Sadun–Segert sign convention (PP C5)

**MR2 convention** (as used in flags F4 / sample values):  
\[
C_2^{\mathrm{(MR2)}} = \frac{n_-^{2} - n_+^{2}}{8}.
\]
Sample values under this convention, reading pairs as \((n_+, n_-)\):  
(3,3)→0, (3,5)→2, (5,7)→3, (1,3)→1.

**NL / E13 convention:**  
\[
C_2^{\mathrm{(NL)}} = \frac{n_+^{2} - n_-^{2}}{8}.
\]
These are **exact reverses** (orientation only). **Harmless** for existence statements and for the attained-set claim \(\mathbb{Z}\setminus\{\pm 1\}\).

**(1,3) is the excluded case:** under either convention, \(n_+=1\) (or a swapped pair with a factor 1) is exactly the `n± ≠ 1` exclusion of Sadun–Segert Theorem 1 / NL E13 M5. The sample (1,3)→±1 is consistent with PP B-M4 (“±1 impossible for \(n_\pm\ge 3\)”). It is **not** an attained charge under the theorem’s hypotheses.

---

## Fix 5 — SSU / Sadun–Segert / BLS math steps superseded by NL Erratum 13 (PP C9)

Cite: `NL_ERRATUM13_CITATION_MATH_CHECKS_OW_36683379_2026-11-09_1818.md`, sha256 **`b5190ea8c908200f8dab6455bcd4462143cad8b4e01993c88425c925be003412`**.

The flags file’s “math check pending” labels on the **reduction / combinatorics / Thm 4.2 example** steps for SSU, Sadun–Segert and BLS are **superseded step-by-step** by NL E13 (as audited by PP C9):

| Step | NL E13 item | Grade (per E13 / PP) |
|---|---|---|
| SSU conformal reduction ℝ⁴∖ℝ² ≅_conf H³×S¹ | M1 | cited, math-checked (PROVED as a step) |
| SSU min–max existence | M2 | cited, math-unchecked CONDITIONAL |
| Sadun–Segert cohomogeneity-1 orbits | M3 | cited, math-checked |
| Sadun–Segert C₂ combinatorics | M4 | cited, math-checked (PP strengthened to ℤ∖{±1}) |
| Sadun–Segert ODE existence / Prop. 2.5 | M5 | cited, math-unchecked CONDITIONAL |
| BLS Thm 4.2 Levi-Civita example | M8 | cited, math-checked |
| BLS Thm 4.1 weak-stability ⇒ (A)SD | M9 | cited, math-unchecked CONDITIONAL |

**Headline existence and stability theorems (M2, M5, M9) remain pending in both files.** No contradiction. **Nothing here is upgraded to PROVED by citation alone.** F11 (Bolza wall file) inheritance, per PP C9: length math-checked; Aut⁺ = 48 math-checked except one lemma (E13/PP); global maximality still pending (Fix 2).

---

## Net

| Fix | Action | Status language |
|---|---|---|
| 1 | CMP 91 REFUTED as Y12 pin; Y12 = Taubes JDG 17 (1982) 139–170 | bibliographic CORRECTED; M7 still CONDITIONAL |
| 2 | Jenni = CMH 59 (1984) 193–203, doi 10.1007/BF02566345 | bibliographic CORRECTED; global-max **pending** (PDF unreachable) |
| 3 | CMP 145 doi 10.1007/BF02099143 added; CMP 79 named Bourguignon–Lawson (doi 10.1007/BF01942061) | bibliographic CORRECTED |
| 4 | MR2 SS sign stated; reverse of NL; (1,3) excluded | clarified |
| 5 | SSU/SS/BLS step checks superseded by NL E13 `b5190ea8…` | pending→superseded where E13 math-checked; M2/M5/M9 still CONDITIONAL |

No CERT. No tip edit. No Gemini. Nothing adopted. Nothing PROVED by citation alone.

Contribution path: `/workspace/quantum-comp/reports/MR2_ERRATUM_SOURCE_LIMIT_FLAGS_PER_PP_c74b5a2d_2026-11-09.md`
