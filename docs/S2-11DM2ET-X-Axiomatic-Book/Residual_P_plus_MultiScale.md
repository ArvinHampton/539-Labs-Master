# Residual \(P^+\): multi-scale path enrichment (research)

**Status:** **Executed research** — permanent class **stable**; **not** theorem-locked; **not** packaging.  
**Programme:** Shell restriction note §2.7.  
**Probe:** `scripts/residual_p_plus_multiscale_probe.py` → `residual_p_plus_multiscale_results.json`.  
**Topology / quantization:** `P_plus_2Complex_Topology_Flux_Quantization.md` (M1 complex, Q0–Q8).  
**Provenance:** residual **(S)** only. No continuum Cartan. Option 3 / thin \(F\) kit **intact**.

---

## 1. Construction (executed)

Same-tower residual path 2-cells on default core:

| Quantity | Value |
|----------|------:|
| Towers with \(\ge 3\) residual indices | 56 |
| Unordered triples | **56** (each tower size exactly 3) |
| Consecutive index triples \((i,i+1,i+2)\) | **56** |
| Fully in window \(k<18\) | **3** |
| Fully in tower \(i\ge 17\) | **53** |
| Straddling shell | 0 |

Enrichment is **tower-local** and almost entirely outside the packaging shell (matches shell-note heuristic).

---

## 2. Stokes: \(\omega_P(\delta f)\)

Two conventions:

| Convention | Definition | \(\omega_P(\delta f)\) |
|------------|------------|------------------------|
| **Path-integrated** | \(\hat g(a,b)=f(b)-f(a)\); \(dg=\hat g_{ij}+\hat g_{jk}-\hat g_{ik}\) | **0** on all 56 |
| **Chord-zero** | only consecutive 1-skeleton edges; chords 0 | **0** on all 56 |

**Reason (chord-zero):** every triple is same-tower consecutive residual indices, so \(\delta f=0\) on their edges.

**Non-exact test** \(g_i=1+(i\bmod 3)\): path-integrated Stokes still vanishes (any path 1-cochain is exact under path integral); chord-zero is nonzero on all 56 triples — so \(d_P\) can act when the 1-skeleton convention allows it.

---

## 3. Differential upgrade

\[
D(\alpha\otimes\delta f)
=
\omega_2\otimes\delta f
-
\alpha\otimes\omega_P(\delta f).
\]

With \(\omega_P(\delta f)=0\):

- vertical piece \(\alpha\otimes\omega_P(\delta f)\) is the **zero** 3-cochain on charge-edge × path-triangle cells;
- closedness of the mixed representative is **not spoiled** by \(P^+\) under residual geometry.

---

## 4. \(H^2(F^+)\) proxy

Thin form ranks (same cell sample as form SS probe):

| Object | Value |
|--------|------:|
| \(\mathrm{rank}\,F^2\) generators \(\{t_w,s_{ad},t_{wf}\}\) | 3 |
| \(\mathrm{rank}\,\mathrm{im}\,D^1\) | 2 |
| \(\dim H^2\) thin proxy | **1** |
| \([s_{ad}]=[\alpha\otimes\delta f]\) in \(\mathrm{im}\)? | **No** (residual \(\gg 1\)) |
| Permanent class survives | **TRUE** |

Path \(H^2\) proxies (secondary multi-scale room, **not** packaging):

| Convention | Proxy |
|------------|--------|
| Path-integrated \(d_P\) from \(C^1\) | coker dim **56** (formal free path 2-cocycles) |
| Chord-zero \(d_P\) | \(\mathrm{rank}\,\mathrm{im}\,d_P\) computed; coker available in JSON |

**Design targets**

1. Preserve permanent mixed class — **met**.  
2. Controlled secondary path-2 room — **available as proxy only**.  
3. Provenance residual (S) — **met**.

---

## 5. Interaction with \(r_W\)

| Check | Result |
|-------|--------|
| Window pairing mass \(M_{\mathrm{win}}\) | unchanged (1-skeleton) |
| \(r_{18}\neq 0\) | still **TRUE** |

---

## 6. Lock decision

| Decision | |
|----------|--|
| Auto-lock \(P^+\) as kit theorem? | **NO** |
| Inflate 56 into packaging integer? | **NO** |
| Touch Option 3 / thin \(F\) kit? | **NO** |
| Continuum EC/TTC from \(P^+\)? | **Category B / O** |

**Reason:** residual \(\delta f\) has vanishing Stokes on the 56 same-tower triangles; the permanent class is stable. Secondary path-2 classes are convention-dependent proxies. Keep \(P^+\) as **optional residual R&D** after kit freeze.

**Status code:** `RESEARCH_STABLE_PERMANENT_CLASS_NOT_LOCKED`

---

## 7. One-line

**\(P^+\) adds 56 same-tower path 2-cells; \(\omega_P(\delta f)=0\) under residual geometry so \([\alpha\otimes\delta f]\) survives with \(\dim H^2=1\) proxy; multi-scale room is secondary/path-2 only — research, not locked.**

*Per aspera ad astra.*
