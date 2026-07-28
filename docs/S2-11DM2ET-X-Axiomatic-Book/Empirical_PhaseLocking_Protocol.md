# Empirical phase-locking investigation (outside the No-Go)

## Principle

An empirical investigation of phase-locking is **still possible** and remains **outside the No-Go**.

One may:

1. evolve trajectories under **any chosen completion** of the map (e.g. \(T^\sharp\), unrestricted \(T_3\), or another declared rule);
2. construct a **phase observable** \(\Phi_t\) from the data;
3. estimate its **dominant period** by standard spectral methods **with no reference to 539.9** in the estimator, grid, filters, or horizon;
4. **only afterward** test whether \(\hat T\) and the phase-error distribution are compatible with the model’s claimed value.

Such a test **does not insert 539.9 into the definition of the dynamics**; it treats that value as a **hypothesis to be checked**.

The numerical value **539.9 enters the analysis only at the final compatibility step, if at all.**

---

## Protocol (pre-register before looking at results)

### P0 — Declare dynamics (no target period)

| Choice | Example |
|--------|---------|
| Map | \(T^\sharp\) (min-defect completion) **or** unrestricted \(T_3\) **or** other declared rule |
| Domain | integer seeds / message–salt ensemble (stated distribution) |
| Horizon \(N\) | **Pre-declared**; not tuned to be an integer multiple of 539. Typical: powers of two or fixed multiples of the short contraction depth, e.g. \(2^{10}\) or \(2^{12}\) steps (see **Horizon control** below) |

**Forbidden in P0:** setting step count, window length, or frequency grid **to privilege 1/539.9**.

### P1 — Phase observable

From each trajectory define a real series \(\Phi_t\) via a **pre-declared** feature map (e.g. fractional part, \(\ln n\) residual, modular coordinate with \(M\notin\{539\}\)).  
HQH-style templates \(A_c\cos+A_s\sin\) are used only **after** period estimation (at \(\hat T\), or at 539.9 **for the compatibility test only**).

---

## P2 — Spectral estimate of the dominant period (no reference to 539.9)

The empirical protocol requires a spectral estimate of the dominant period **obtained without any reference to the number 539.9**. The following choices satisfy that requirement and are standard in time-series analysis.

### Primary estimator — ordinary periodogram

The **ordinary periodogram** (squared modulus of the discrete Fourier transform) computed on \(\Phi_t\) **after removal of a linear trend**.

Frequency grid = **natural DFT grid**:

\[
f_k = \frac{k}{N\,\Delta t},
\qquad
k = 1,\ldots,\bigl\lfloor N/2\bigr\rfloor,
\]

where \(N\) is the number of retained steps and \(\Delta t\) is the uniform step size of the discrete map (typically \(\Delta t=1\)).

**No frequency bin is placed preferentially at \(1/539.9\).**

Dominant period:

\[
\hat T = \frac{1}{f_{k^\ast}},
\qquad
k^\ast = \arg\max_k I(f_k)
\]

with \(I\) the periodogram.

### Variance-reduced alternative — multitaper (Thomson)

A **multitaper periodogram** (Thomson) with a small number of Slepian tapers (typically **3–5**) may be substituted when the trajectory is long.

- The **same natural frequency grid** is retained.  
- Multitaper lowers variance of the continuum **without introducing an external period**.

### Uneven or gapped sampling — Lomb–Scargle

If projections or rejections produce **irregularly spaced** valid steps, use the **Lomb–Scargle periodogram**.

Frequency grid again **independent of 539.9**, e.g. uniform in frequency from \(1/(N\Delta t)\) up to the Nyquist frequency of the **median** sampling interval.

### Pre-processing (estimation stage)

| Allowed | Forbidden at estimation stage |
|---------|-------------------------------|
| Subtract a **linear least-squares trend** from \(\Phi_t\) | Band-pass or notch filter **centred near \(1/539.9\)** |
| Optionally a **single low-order polynomial** detrend if slow residual drift remains | Any pre-whitening or filter that privileges the model period |
| Standard taper window if declared (e.g. Hann) for the plain DFT | Inserting 539.9 into the series construction |

### Peak selection

| Step | Method |
|------|--------|
| Dominant period \(\hat T\) | Reciprocal of the frequency that **maximises** the chosen periodogram |
| Optional HWHM | Half-width at half-maximum of the peak (descriptive width only) |

**Point estimate first:** bootstrap uncertainty is obtained **after** \(\hat T\) has been computed, and **without any reference to 539.9**.

### Bootstrap uncertainty for \(\hat T\) (standard; protocol-compatible)

All schemes below use the **identical** frequency grid and horizon \(N\) as the original point estimate. They do **not** use 539.9.

#### 1. Basic residual bootstrap (default for evenly spaced series)

1. After linear (or low-order polynomial) detrending, form residuals  
   \[
   r_t = \Phi_t - \mathrm{trend}_t.
   \]
2. Generate \(B\) bootstrap series by drawing \(\{r_t\}\) **with replacement** and adding them back to the **fixed** trend.
3. On each bootstrap series, recompute the **same** periodogram (ordinary or multitaper) on the **identical** frequency grid; record the maximising period \(\hat T^{(b)}\).
4. The collection \(\{\hat T^{(b)}\}_{b=1}^{B}\) is the empirical sampling distribution of \(\hat T\).

#### 2. Phase-randomisation bootstrap (preserves power-spectrum shape)

1. Compute the DFT of the detrended series.
2. Replace phases by independent uniform random phases; invert the transform.
3. Surrogates share the same periodogram ordinates but randomised phase relations.
4. Repeat \(B\) times; re-estimate the dominant period on each surrogate.

This construction also supplies a **direct significance test** for the original peak (compare original peak height / \(\hat T\) stability to the surrogate ensemble).

#### 3. Moving-block or stationary bootstrap (serial dependence)

When consecutive phase increments are appreciably correlated:

- **Moving-block:** resample overlapping blocks of fixed length \(L\);  
- **Stationary bootstrap:** block lengths geometrically distributed.

Typical \(L\sim\sqrt{N}\), or choose \(L\) by the automatic rule of **Politis & White**.  
Then recompute the periodogram peak on each bootstrap series (same as above).

#### Number of replicates and interval construction

| Choice | Standard setting |
|--------|------------------|
| Replicates | \(B=2000\) ordinarily sufficient for a stable percentile interval |
| Central 95% percentile interval | 2.5% and 97.5% quantiles of \(\{\hat T^{(b)}\}\) |
| Also allowed | Basic bootstrap interval; normal approximation \(\hat T \pm z\cdot s_{\mathrm{boot}}\) |
| Optional | Bias-corrected accelerated (**BCa**) intervals if the peak-location distribution is markedly skewed |

#### Bootstrap protocol constraints

| Constraint |
|------------|
| Frequency grid and horizon \(N\) remain **exactly** those of the original point estimate; **not** altered inside the bootstrap loop |
| **No** bootstrap replicate is discarded or re-weighted by proximity to **539.9** |
| The bootstrap distribution is **fully recorded before** any compatibility test with the claimed value |

**Any** of the three resampling schemes, with pre-declared \(B\) and a percentile or basic interval, supplies a quantitative uncertainty for \(\hat T\) that is **free of the number 539.9**.  
That interval is the one that later participates in the **optional** compatibility check.

### Null significance (related, still free of 539.9)

| Method | Role |
|--------|------|
| Residual / block bootstrap distribution of peak period | Uncertainty for \(\hat T\) |
| Phase-randomisation surrogates | Significance of the original spectral peak |
| Random shuffle of \(\Phi_t\) | Simple null (destroys dependence and spectrum shape) |

None of these uses 539.9.

### Horizon control

- Maximum lag / total length \(N\) is **declared before the run**.  
- **Not** tuned to be an integer multiple of 539.  
- Typical choices: **powers of two**, or fixed multiples of the expected **short contraction depth** (e.g. \(2^{10}\) or \(2^{12}\) steps; cf. \(N_\star=14\) only as a scale hint for short runs, not as a period).  
- Horizon is part of the **pre-registered design**.

### Estimator summary

| Situation | Estimator |
|-----------|-----------|
| Uniform discrete steps (default) | Ordinary periodogram on natural DFT grid |
| Long trajectories, lower variance | Multitaper (3–5 Slepian tapers), same grid |
| Irregular / gapped valid steps | Lomb–Scargle, independent frequency grid |

**Any** of the above, used with a frequency grid and horizon that **do not privilege \(1/539.9\)**, satisfies the protocol.

---

## P3 — Compatibility test (**post-estimation only**)

After \(\hat T\) and its uncertainty have been **recorded**:

- One **may** test whether \(\hat T\) is statistically consistent with **539.9**.  
- That test is a **separate, optional hypothesis check**.  
- It is **not** part of the period estimation itself.

Examples (pre-register one):

- \(|\hat T-539.9|\le\delta\) with \(\delta\) fixed in advance;  
- 539.9 inside a \(1-\alpha\) CI for \(T\);  
- phase-error series at **fixed** period 539.9 (test only) consistent with a declared noise model.

---

## P4 — Report

| Report | Role |
|--------|------|
| Map, \(N\), \(\Delta t\), ensemble size | Design |
| Estimator (periodogram / multitaper / Lomb–Scargle) | Methods |
| Pre-processing (linear / poly detrend) | Methods |
| \(\hat T\), bootstrap scheme, \(B\), percentile CI (full boot dist. recorded) | **Primary** result |
| Peak \(p\)-value (phase-rand / shuffle) | Primary (still free of 539.9) |
| Compatibility with 539.9 (if run) | **Secondary** — only after bootstrap recorded |
| ACE reminder | \(N_\star=14\neq 539\); long period not forced by contraction |

---

## What this is / is not

| Is | Is not |
|----|--------|
| Standard spectral estimation without a privileged bin at \(1/539.9\) | Derivation of 539 from ACE |
| Outside the No-Go | Insertion of 539.9 into dynamics or estimator |
| 539.9 only at final optional compatibility step | 539.9 as definition of period or horizon |

---

## Minimal pseudocode

```text
# Pre-register: map, N (e.g. 2^12), estimator, detrend, bootstrap scheme, B=2000
# No use of 539.9 until optional final test

for seed in ensemble:
    n[t] = iterate(map, seed, N)
    Phi  = phase_observable(n)
    trend, r = linear_detrend(Phi)        # optional: low-order poly
    # FORBIDDEN: notch/bandpass near 1/539.9

    I = periodogram(Phi_detrended)        # or multitaper / Lomb-Scargle
    # frequency grid fixed: f_k = k/N  (or independent LS grid)
    T_hat = 1 / f[argmax(I)]              # POINT ESTIMATE FIRST

    # Bootstrap AFTER point estimate — same grid, same N; no 539.9
    for b in 1..B:                        # B = 2000 default
        if residual_bootstrap:
            r_star = sample_with_replacement(r)
            Phi_b = trend + r_star
        elif phase_randomisation:
            Phi_b = ifft( |DFT| * exp(i*U(0,2π)) )
        elif block_bootstrap:
            Phi_b = resample_blocks(Phi_detrended, L)  # L ~ sqrt(N) or Politis-White
        I_b = periodogram(Phi_b)          # IDENTICAL frequency grid
        T_boot[b] = 1 / f[argmax(I_b)]
        # FORBIDDEN: drop/reweight replicates by proximity to 539.9

    CI = percentile(T_boot, 2.5%, 97.5%)  # fully record distribution
    # optional: basic interval, normal approx, BCa

record(T_hat, CI, T_boot)                 # PRIMARY — still no 539.9

# OPTIONAL — post-estimation only (after bootstrap is fully recorded):
compatible = test(T_hat, CI, claimed=539.9, delta=pre_registered)
```


---

## Relation to Status of Record

- ACE for \(T^\sharp\): closed; \(N_\star=14\); essential No-Go on 539 stands.  
- This protocol: **permitted** empirical route; spectral machinery **never** references 539.9 until an optional final compatibility check.

See: `ACE_Status_of_Record.md`
