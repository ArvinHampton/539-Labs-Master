# RFC: Residual charge sectors \(\leftrightarrow\) DDG / MT band dictionary

**Status:** **Category B** proposal + pre-registration stub — **not locked**.  
**Purpose:** Make the only bridge that can falsify bio-scale contact with residual \(Q=9\) **explicit**.  
**Provenance:** residual form side stays **(S)**; band side is empirical.  
**Does not** claim \(9=12\), peak counts 18/521, or free \(T^\sharp\) 539.

---

## 1. Problem

Residual form coupling lives on **9 charge sectors**.  
DDG literature often cites **12** nested bands; MT catalogs span **decades** (kHz–THz).  
Without a pre-registered dictionary, “sector = band” is metaphor (**O/B**).

---

## 2. Candidate dictionaries (choose one before analysis)

| ID | Map idea | Risk |
|----|----------|------|
| **D1** | 9 sectors → 9 coarsened band *groups* (merge 12→9 by fixed rule) | Merge rule must be pre-registered |
| **D2** | 9 sectors → 9 MT *decades* or log-bins on \(\log_{10} f\) | Independent of DDG-12 |
| **D3** | 9 sectors → 9 spatial / montage groups (not frequency) | Different ontology |
| **D0** | **Null:** no map; residual class not tested on bio bands | Always available |

**Default for first public test:** **D2** (log-frequency bins), because it does not force \(9=12\).

### D2 rule (proposed)

Partition observed peaks / power into 9 bins of equal width in \(\log_{10} f\) between \(f_{\min}\) and \(f_{\max}\) of the study.  
Sector label \(q\in\{0,\ldots,8\}\) = bin index low→high or high→low (state orientation in pre-reg).

---

## 3. Pre-registered statistics (pass/fail)

Let \(C_{q r}\) be a cross-band coupling matrix (e.g. PLV, coherence) after dictionary labels.

| Statistic | Prediction if residual mixed-class story applies | Fail |
|-----------|--------------------------------------------------|------|
| **S1** | Mean coupling inside “adjacent sectors” \(>\) shuffled sector labels | \(p>0.05\) on pre-reg null |
| **S2** | High-frequency shell (window metaphor) shows stronger *within*-shell coupling than cross to deep shell | reverse inequality |
| **S3** | Path-order surrogate (shuffle time within band) reduces mixed diagnostic more than amplitude-matched noise | no differential drop |

**Tolerance:** report effects with confidence intervals; no post-hoc sector renumbering.

---

## 4. Explicit non-claims

- Not a proof of Orch-OR\(^{11\mathrm{D}}\).  
- Not recovery of integers 18/521 from peaks.  
- Not identification of residual \([\alpha\otimes\delta f]\) with a measured PLV eigenvalue without the dictionary + S1–S3.  
- Not a security reduction.

---

## 5. Decision rule

| Outcome | Action |
|---------|--------|
| S1–S2 pass on primary DDG/MT | Promote dictionary to **working Cat B**; design relative SS tests (anesthesia) |
| Clear fail | Keep residual math; **retire** bio-sector metaphor for that dataset |
| No data | RFC remains open; residual locks unchanged |

---

## 6. One-line

**Until a pre-registered sector↔band map is tested, biological unification across residual form and DDG/MT is metaphor; this RFC is the minimal falsifiable bridge.**
