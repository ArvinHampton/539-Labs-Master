# RFC: Residual charge sectors \(\leftrightarrow\) DDG / MT band dictionary

**Status:** **Category B** — dictionary version **D2.0**; pre-registered D2 executed on CHB-MIT `chb01_01`; S1–S3 **PASS** on this dataset → **working Cat B dictionary** (not residual lock; **not** multi-cohort validated).  
**Purpose:** Make the only bridge that can falsify bio-scale contact with residual \(Q=9\) **explicit**.  
**Provenance:** residual form side stays **(S)**; band side is empirical.  
**Does not** claim \(9=12\), peak counts 18/521, or free \(T^\sharp\) 539.  
**Probe:** `scripts/sector_band_S1S3_probe.py` → `sector_band_S1S3_results.json`.

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

## 6. Executed first public test (D2 · CHB-MIT)

**Pre-registration (frozen in probe):**  
9 log-bins on \([0.5,40]\) Hz; \(q=0\ldots8\) low→high; \(n_{\mathrm{perm}}=200\); seed 5399; shell = top 2 bins; deep = bottom 4 bins; \(\alpha=0.05\); 120 s × 8 bipolar channels; mean PLV coupling matrix \(C_{qr}\).

**Dataset:** PhysioNet CHB-MIT `chb01_01.edf` (real scalp EEG).

| Statistic | Observed | Null / comparison | Result |
|-----------|----------|-------------------|--------|
| **S1** mean adjacent PLV | \(\approx 0.0646\) | label-shuffle mean lower; \(p=0\) (one-sided, 200 perm) | **PASS** |
| **S2** high-shell within vs deep cross | within \(\approx 0.0779\) > cross \(\approx 0.0018\) | reverse would fail | **PASS** |
| **S3** path-order drop vs noise drop | scramble drop \(\approx 0.0083\) > noise drop \(\approx -0.0083\) | mixed diagnostic falls under phase scramble | **PASS** |

**Decision code:** `PROMOTE_WORKING_CAT_B_DICTIONARY`

### Caveats (mandatory)

- **Single recording / single subject** — not a multi-cohort claim.  
- **Filter adjacency leakage** can inflate S1 adjacent coupling; pass is necessary, not sufficient, for “sector physics.”  
- **Not** residual \(H^2\) identification; **not** 18/521 peaks; **not** Orch-OR; **not** security.  
- Residual form locks and Option 3 are **unchanged**.  
- Next: replicate on independent DDG/MT sets; anesthesia / relative SS design remains open.

---

## 7. One-line

**D2 sector↔band map is a working Category B dictionary on CHB-MIT `chb01_01` (S1–S3 pass); residual math stays locked and independent — further cohorts required before any stronger bio claim.**
