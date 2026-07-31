# Remaining analytic obligations (unchanged)

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**.  
**Axiom ZLA** applies to every future theorem (`RH_Zeta_Language_Admissibility.md`).  
**No model constants.** RH open.

These five obligations are the **open analytic core** of the phase programme. Infrastructure (L1–M1.4 notes, GHK, \(c_i\), HD-low diagnostics, ZLA, L4) does **not** discharge them. Their status is **unchanged**: open.

**Companions:** `RH_L1_Phase_Functional_CatA.md`, `RH_M1_2_Remainder_Bound_Strategy.md`, `RH_M1_3_Path_Design.md`, `RH_M1_3_HD_Low_Path_Report.md`, `RH_Target_Lemma_Sketch_Literature_L5.md`, `RH_Deep_Pursuit_2026-07-31.md`.

---

## Obligation list

| ID | Obligation | Status |
|----|------------|--------|
| **O-M1.2** | Uniform M1.2 under classical zero-density alone | **Architecture accepted** (`RH_M1_2_Effective_Density.md`); **concrete density constants recorded** (`RH_Deep_Pursuit_2026-07-31.md`); numerical \(\gamma_1\) **open** |
| **O-M1.3bis** | Path design that accumulates argument to size \(\gg\log\log X\) | **Open** |
| **O-PC** | Phase / discrepancy | **On-line strong Omega accepted** (model \(\operatorname{Im} D_X\) + hybrid discrepancy; fixed \(X\); continuous-arg caveat) — `RH_Resonance_Discrepancy_Attack.md`; **O-TL locations open** |
| **O-Moll** | Construction of a genuinely phase-oriented mollifier | **Open** |
| **O-TL** | The target lemma itself | **Open — primary** |

---

## 1. O-M1.2 — Uniform M1.2 under classical zero-density alone

**Goal.** Prove a bound of the form
\[
\bigl\lvert\operatorname{Im}\widetilde{\mathcal{R}}(s)\bigr\rvert
\le
c_0\,m\cdot\sup\lvert\arg_{\mathrm{reg}}(s,\rho)\rvert
+
O\bigl(\lvert\mathcal{E}_{\mathrm{GHK}}\rvert\bigr)
\]
(or the IvM form for \(\operatorname{Im}\mathcal{R}_x^{\mathrm{EP}}\)) **uniformly** for \(s\) on the M1.3 path about a zero \(\rho\) of multiplicity \(m\), with \(c_0<1\), using **only**:

- classical zero-density / \(N(T)\) estimates (L4 **H4**),  
- GHK or IvM identities (ZLA-admissible),  
- effective \(c_1,c_2\) for a fixed weight (already majorized for \(f_\star\)),

and **not** RH-strength zero-free regions or finite Odlyzko tables as the sole support of the bound.

**What is already done (does not close O-M1.2):**

- Named remainder \(\mathcal{R}_x^{\mathrm{EP}}\), M1.2 strategy, M1.2-GHK sketch.  
- Admissible \(c_1\le 291\), \(c_2\le 8\) for \(f_\star\).  
- HD-low **diagnostics** and finite-height empirical \(\lvert\mathcal{E}\rvert\), \(\lvert R_{\mathrm{reg}}\rvert\).

**What is missing:** a **uniform** proof that distant-zero / archimedean / tail contributions stay below the local main term for all large \(\lvert\gamma\rvert\). Architecture + concrete density constants are recorded; a specific numerical \(\gamma_1\) under one fixed published triple remains open as finite arithmetic (does not close O-TL).

---

## 2. O-M1.3bis — Path design with \(\Delta\theta\gg\log\log X\)

**Goal.** Construct a path \(\gamma_{\mathrm{path}}\) (and possibly a scale \(X=X(s)\)) such that the continuous argument \(\theta_X=\arg P_X\) (or smoothed \(A_X\)) satisfies
\[
\bigl\lvert\Delta_{\gamma_{\mathrm{path}}}\theta_X\bigr\rvert
\gg
\log\log X
\]
(or \(\gg m\log\log X\) at a zero of multiplicity \(m\)), while a **regularised** remainder remains controlled by O-M1.2.

**What is already done (does not close O-M1.3bis):**

- Semicircle geometry: monodromy of zero-free \(P_X\) is \(\approx 0\) (correctly withdrawn as an \(m\pi\) engine).  
- Approach paths \(\sigma:1.5\to\tfrac12+r\): natural geometry; low-height \(\Delta\arg P\) is **small**.  
- Multi-\(X\) batch R2: no \(\log\log X\) growth visible at first zeros.

**What is missing:** a path (or family of paths / \(X(s)\)) that **accumulates** phase to target-lemma scale, not merely \(O(1)\) motion.

**Structural constraint (frozen):** accumulation cannot come from monodromy of \(P_X\) about a zero of \(\zeta\). It must come from genuine variation of \(\arg P_X\) along a long or slowly modulated path, or from coupling with modulus via renormalization (Akatsuka-type), still under ZLA.

---

## 3. O-PC — Pair correlation \(\to\) phase lower bounds

**Practical status:** `RH_Pair_Correlation_Practical_Status.md` · **Partial resolution:** `RH_OPC_Partial_Resolution.md` · **Gap spec:** `RH_OPC_Conversion_Gap.md`.

- Pair correlation is **classical and ZLA-admissible**.  
- Hybrid identity \(\theta_X=\arg\zeta-\arg Z_X-\operatorname{Im}\mathcal{E}\) **proved**.  
- **Omega at typical scale (proved):** \(\limsup_t\lvert\theta_X(\tfrac12+it)\rvert\gg\sqrt{\log\log X}\) and same for \(\lvert\Delta_X\rvert\) (`RH_OPC_Omega_Discrepancy.md`).  
- **Strong core (open):** \(\lvert\Delta_X\rvert\) or \(\lvert A_X\rvert\gg\log\log X\) (O-TL scale); off-line Omega open.  
- Typical vs Omega distinction is **explicit**: O-TL needs strong Omega, not only typical/\(L^2\) size.  
- **Ledger position:** upstream of or parallel to O-M1.2.

**Goal.** Take a **precisely stated** pair-correlation (or \(n\)-level correlation) hypothesis on the zeros of \(\zeta\) — classical Montgomery-type or a labelled weakening — and **derive** a lower bound for continuous \(\theta_X\) or \(A_X\) with fully tracked error terms.

**What is already done (does not close O-PC):**

- Classical PCC and partial pair-correlation theorems as **zero-side** infrastructure (almost-all simplicity / criticality under PCC).  
- GHK / RMT commentary as **heuristic** for moments (Keating–Snaith).  
- L4: full PCC as a **hypothesis** for unbounded theorems remains conditional (**C2**); almost-all corollaries under PCC are classical.  
- Function-field monodromy theorems as **analogies**, not transfers to \(\zeta\).

**What is missing:** the full conversion chain — see **`RH_OPC_Conversion_Gap.md`**:

1. Local isolation from PC / \(n\)-level density at the evaluation points.  
2. Hybrid translation \(\to\) lower bound on \(\arg Z_X\) (or \(\Delta\arg Z_X\)).  
3. Remainder domination (uniform M1.2 at those points).  
4. Transfer to \(\arg P_X\) or \(A_X\) of size \(\gg\log\log x\) (or \(\gg 1\) feeding O-TL).

**None of steps 1–4 is currently a theorem** (published or internal to this programme).

**Circularity warning (L4):** any form of PC that is known only under RH, or that encodes RH-scale repulsion stronger than classical density, must be labelled and not silently treated as free. PCC itself is a conjecture about zeros; using it as a hypothesis is ZLA-clean but **conditional**.

---

## 4. O-Moll — Genuinely phase-oriented mollifier

**Goal.** Construct a mollifier (smooth weight on primes / Dirichlet polynomials / hybrid \(X\)-window) whose design criterion is **phase** of the partial Euler product (or of \(A_X\)), not only modulus \(\lvert\zeta\rvert\) or moment asymptotics.

Classical mollifiers (Levinson, Conrey, etc.) optimise detection of zeros or mean squares of \(\lvert\zeta\rvert\). A **phase-oriented** mollifier would optimise or stabilise continuous \(\arg P_X\) / \(A_X\) along the M1.3-bis path.

**What is already done (does not close O-Moll):**

- GHK weight \(u\) / \(U=\int u\,E_1\): spectral–arithmetic split; not phase-optimised.  
- M1.4 log-average in \(Y\): smoothing of \(\theta_Y\), not a Dirichlet mollifier.  
- Named bump \(f_\star\): fixed for \(c_i\) majorants.

**What is missing:** an explicit family \(M(s;X)\) (or modified \(P_X\)) with a theorem or conditional bound that \(\arg(M\cdot P_X)\) or \(\arg P_X^{M}\) has improved lower bounds relative to the unmollified product.

---

## 5. O-TL — The target lemma itself

**Goal (L1).** At a zero \(\rho=\beta+i\gamma\) of multiplicity \(m\) with \(\beta=Y=\sup\operatorname{Re}\rho'\), there exist \(c>0\) and a sequence \(X_n\to\infty\) such that
\[
\bigl\lvert A_{X_n}(Y,\gamma)\bigr\rvert
\ge
c\,m\log\log X_n,
\]
with \(A_X\) as in L1 / M1.4, **ZLA-clean**, no model constants.

**Dependence:** O-TL is the **primary open claim**. In the intended architecture it is fed by O-M1.2 + O-M1.3bis (and optionally O-PC, O-Moll), then M1.4 smoothing.

**What is already done (does not close O-TL):**

- Formal definition of \(A_X\) and statement of the target lemma.  
- Literature map (Conrad–Goldfeld–Akatsuka; GHK).  
- Diagnostics showing low-height \(A_X\) and \(\Delta\arg P\) are **not** yet at \(\log\log\) scale.

**Status:** **Open — primary.** Equivalent in strength (in the programme’s contrappositive story) to controlling off-line zeros of maximal real part via partial-product phase; **not** a proved theorem.

---

## Dependency sketch

```
                    ┌──► O-M1.2 (classical zero-density alone)
O-PC (open) ────────┤        ▲
  upstream/parallel └──► (spacing / almost-all input)
                              │
O-Moll (optional) ────────────┤
classical density ────────────┤
                              ▼
                         O-M1.3bis ──► M1.4 ──► O-TL
                              ▲
                    regularised remainder (GHK/IvM)
```

None of the five boxes is checked. **O-PC is first-class and open**, upstream of or parallel to O-M1.2. O-Moll remains optional. Neither substitutes for O-TL.

---

## Solid directions (current)

See `RH_Existing_Theorems_Solid_Directions.md` §6.

| Rank | Direction | Status |
|------|-----------|--------|
| **1** | Resonance **off the line** | **Open** — precise lemma in `RH_Deep_Pursuit_2026-07-31.md` |
| **2** | **Effective density constants** for conditional M1.2 | Architecture accepted; **constants recorded**; \(\gamma_1\) arithmetic **open** |
| **3** | Finite-product approximation **off the line** | **Open** — argument lemma in deep-pursuit note |
| **4** | **Path continuation** from known on-line Omega | **Open** — differential \(\Phi\) in deep-pursuit note |

On-line strong Omega (fixed \(X\)) is **accepted**, not re-listed.  
Deep pursuit freeze: `RH_Deep_Pursuit_2026-07-31.md`.  
**O-TL remains open** (primary). RH remains open.

## Explicit non-claims

| Claim | Status |
|-------|--------|
| O-TL / strong O-PC / RH proved | **No** |
| Typical Omega \(\gg\sqrt{\log\log X}\) for \(\theta_X,\Delta_X\) on the line | **Yes** (programme theorem) |
| Diagnostics imply O-TL | **No** |
| ZLA / L4 / \(c_i\) / GHK survey close RH | **No** |
| Silent weakening of O-TL to \(\sqrt{\log\log X}\) | **Not adopted** |

---

## One-liner

**The pure Cat A phase programme still owes five analytic obligations — uniform M1.2 under classical density, \(\log\log X\) path accumulation (M1.3-bis), PC\(\to\)phase theorems, a phase-oriented mollifier, and the target lemma — all open; infrastructure does not discharge them.**

*Per aspera ad astra.*
