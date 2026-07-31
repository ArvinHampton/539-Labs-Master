# Target-Lemma Sketch, Literature, L5 Plan

**Status:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF` (active)  
**Claim:** none on RH.

---

## 1. Target-lemma sketch (Akatsuka → arg / \(A_X\))

### Setup

Write (schematically) the partial product logarithm near a zero \(\rho\) of multiplicity \(m\):

\[
\log P_x(s)
= m\log(s-\rho)
- \mathcal R_x^{(\mathrm{EP})}(s)
+ \text{(smooth / pole renormalizers)}.
\]

Then

\[
\theta_x(s)
= m\arg(s-\rho)
- \operatorname{Im}\mathcal R_x^{(\mathrm{EP})}(s)
+ \cdots.
\]

### Key point from Akatsuka-type expansions on the line

Akatsuka’s \(m\log\log x\) term is essentially **real** in the schematic expansion of \(\log P_x\) on the critical line when a DRH-type limit exists: it enlarges \(\lvert P_x\rvert\), **not** automatically \(\arg P_x=\theta_x\).

### Mechanisms toward a lower bound on \(\theta\) / \(A_X\)

| Tag | Mechanism | Role |
|-----|-----------|------|
| **M1** (primary) | Explicit formula / Hadamard / GHK: zero forces argument in the split \(\log\zeta=\log P_X+\log Z_X+\varepsilon\) | Pointwise path to off-line growth |
| **M2** | Harmonic conjugate of \(U_x=\log\lvert P_x\rvert\) | Good for averages; weak pointwise |
| **M3** | Complex phase of \(\log\log\) | Needs large Im main term; secondary |

**Route:** lower bound on \(\theta_{x_n}\) + slow variation on \([X,X^2]\) \(\Rightarrow\) lower bound on smoothed \(A_X\).

### Open obligations

| Tag | Obligation |
|-----|------------|
| O1 | Exact Akatsuka / Ramanujan-type expansion hypotheses (see O1 package) |
| O2 | M1 remainder \(\operatorname{Im}\mathcal R\) (→ M1.2) |
| O3 | Smoothing: \(\theta\to A_X\) with controlled loss |
| O4 | No circular RH (forbid RH-conditional inputs as load-bearing) |

---

## 2. Literature (exact citations)

| Work | Citation | Use |
|------|----------|-----|
| Conrad 2005 | *Partial Euler products on the critical line*, Canad. J. Math. **57** (2005), 267–297; [PDF](https://kconrad.math.uconn.edu/articles/eulerprod.pdf) | On-line modulus asymptotics; RH-strength / stronger |
| Goldfeld 1982 | *Sur les produits partiels eulériens…*, C. R. Acad. Sci. Paris Sér. I **294** (1982), 471–474 | Via Conrad Thm 1.1 |
| Akatsuka 2017 | *The Euler product for the Riemann zeta-function in the critical strip*, Kodai Math. J. **40** (2017), 79–101; DOI [10.2996/kmj/1490083225](https://doi.org/10.2996/kmj/1490083225); MR3626575 | Pointwise product vs zeros in right half-strip — O1 input |
| GHK 2007 | Gonek–Hughes–Keating, *A hybrid Euler–Hadamard product…*, Duke Math. J. **136** (2007), 507–549; [arXiv:math/0511182](https://arxiv.org/abs/math/0511182) | Unconditional split \(P_X Z_X\); M1 skeleton |
| Bui–Gonek–Milinovich 2015 | *A hybrid Euler–Hadamard product and moments of \(\zeta'(\rho)\)*, Forum Math. **27** (2015), 1799–1828; [arXiv:1302.5032](https://arxiv.org/abs/1302.5032) | Discrete moments at zeros (**under RH**) — diagnostic only |
| Sheth 2023/25 | Euler product asymptotics for elliptic \(L\)-functions, [arXiv:2312.05236](https://arxiv.org/abs/2312.05236) | Template for \(R_s(x)\); often **RH-conditional** |
| Ingham 1937/40 | Zero-density \(N(\sigma,T)\) | Medium-zero sums in M1.2 |
| Kadiri–Lumley–Ng 2018 | Explicit zero-density | Effective constants |
| Keating–Snaith / CFKRS | Moment conjectures / recipe | On-line modulus means — not arg lower bounds |
| LeClair | arXiv:1601.00914; *Symmetry* **13** (2021), 2014 | **Heuristic only** |

**Conrad–Goldfeld:** product asymptotics on the line are RH-strength (even deeper than RH in a precise sense).  
**Akatsuka:** pointwise product vs zeros in the right half-strip — O1 input.  
**GHK:** only unconditional pointwise hybrid suitable for M1 remainder analysis.

---

## 3. L5 numerical plan only

### Objects

| Object | Method |
|--------|--------|
| Primes | sieve to \(x_{\max}\) |
| \(\theta_x=\arg P_x(\sigma+it)\) | cumulative principal args of factors \((1-p^{-s})^{-1}\) |
| \(U_x=\log\lvert P_x\rvert\) | cumulative log-moduli |
| \(A_X\) | \(\int_1^2\theta_{X^v}\phi(v)\,dv\), \(\phi\) smooth bump on \((1,2)\) |
| \(\lvert\zeta\rvert\) | high-precision library at each test point |

### Batteries

- **On-line:** \(\sigma=1/2\), first Odlyzko zero ordinates  
- **Off-line:** \(\sigma=1/2\pm\delta\) at same heights; plus refined local minima of \(\lvert\zeta\rvert\) with \(\sigma\ge 0.60\) guard  
- **No** \(G_4\), \(\mu\), \(E_{\mathrm{leak}}\), 539.9

### Policy

- No RH claim from finite \(X\)
- Branch-cut checklist: cumulative arg (not `np.angle` of product)
- Record `branch_warnings` count
- Status string: `L5_DIAGNOSTIC_EXECUTED_NO_RH_CLAIM`

### Run

```bash
python scripts/rh_L5_phase_diagnostic.py --x-max 5000 --n-zeros 8
python scripts/rh_L5_phase_diagnostic.py --x-max 30000 --n-zeros 10 --max-minima 14
```

---

## 4. Mechanism map (Akatsuka m log log vs arg)

```text
log P_x  ≈  (real m log log x)  +  i θ_x  +  R
                 │                      │
                 │                      └─ needs M1 for zero-forced jump
                 └─ modulus growth on line (Akatsuka / Conrad)
```

Lower bound on \(\theta_{x_n}\) + slow variation on \([X,X^2]\) ⇒ lower bound on smoothed \(A_X\).  
Open: O1 exact expansion · M1 remainder · smoothing · no circular RH.
