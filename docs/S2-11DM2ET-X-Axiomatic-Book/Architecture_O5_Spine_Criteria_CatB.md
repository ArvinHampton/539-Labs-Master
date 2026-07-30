# O5 — Spine Criteria for Primary K⁺ (Category B)

**Status:** `O5_BALL_SPINE_PROVED_CAT_B`  
**Parent:** `CB4_SMOOTH_SPIN_FILL_OPEN_CAT_B` ⊂ continuum Cat-B track  
**Date:** 2026-07-30  
**Probe:** `scripts/o5_spine_criteria_catB_probe.py` → `o5_spine_criteria_catB_results.json`  
**Depends on (read-only):** O4 collapsible / π₁=1; A4⁺ unique BSpin; A5⁺ H_* ≅ pt  

---

## HARD FIREWALL

| Rule | Status |
|------|--------|
| A0–A5⁺ residual locks | **Untouched** |
| Option 3 / No-Go | **Intact** |
| Free T^♯ | **Forbidden** |
| G₄ = B³ / S³ as residual foundation | **Forbidden** |
| Continuum → residual Category A | **Forbidden** |
| Closed special spine of closed 3-manifold | **Not claimed** (and false for K⁺) |

All conclusions below are **Category B**.

---

## 0. Question O5

> Does primary \(K^+\) arise as a PL spine of a compact 3-manifold with boundary (especially a 3-ball), so that a regular neighborhood realizes that manifold?

**Answer (Cat B):** **Yes — spine of a 3-ball.**  
Proof route: collapsibility (O4) + certified PL embedding in \(\mathbb{R}^3\) (S6) ⇒ regular neighborhood \(N(K^+)\) is a PL 3-ball with spine \(K^+\).

---

## 1. Inputs from prior locks / Cat-B results

| Input | Status |
|-------|--------|
| Census V=539 E=594 F=56 | locked / rechecked |
| \(H_*\cong\mathrm{pt}\) | A5⁺ |
| Unique BSpin | A4⁺ |
| Collapsible / π₁=1 | O4 `PI1_TRIVIAL_PROVED_CAT_B` |

---

## 2. Methods executed

| ID | Method | Result |
|----|--------|--------|
| S1 | Singularity census | Edge–face mult: 0→426, 1→168, ≥2→**0** |
| S2 | Vertex-link planarity | **All planar** |
| S3 | Matveev almost-simple checklist | Not a **closed** special spine; ball-spine candidate |
| S4 | Classical spine theorems | Embed + collapsible ⇒ ball neighborhood |
| S5 | Structure | 56 **vertex-disjoint** tripleton triangles; 0 mixed faces; 185 doubleton chords |
| S6 | Constructive PL embedding in \(\mathbb{R}^3\) | **Validated** (0 improper tri–tri, 0 edge–tri piercings) |

---

## 3. Local necessary criteria (PASS)

1. **Planar vertex links** — necessary for 3-manifold polyhedral spine; all links planar.  
2. **No book edges of multiplicity ≥2** — \(K^+\) is a union of triangular plates + 1-skeleton arcs (surface pieces with free edges), not a closed special spine.  
3. **Free edges allowed** — normal for spines of manifolds with boundary (ball).  
4. **Collapsible** — O4; needed for neighborhood to be a ball once embedded.

---

## 4. Structure theorem (combinatorial)

**Theorem O5.1 (Cat B, combinatorial).**  
The 2-cells of primary \(K^+\) are exactly **56 vertex-disjoint** triangles (one per tower tripleton). There are no mixed-tower faces. The 1-skeleton is the path on 539 vertices plus same-tower chords (185 doubletons + tripleton edges).

This disjoint-plates-along-a-path structure is what makes a straight-line embedding tractable.

---

## 5. Constructive PL embedding (S6)

**Scheme.**

- Place index-\(i\) vertices at \((i,0,0)\) by default.  
- For each tripleton face \(\{a,b,c\}\) with face index \(f\), lift the three vertices into a unique \(z=2+f\) slice with distinct \((y,z)\) offsets so the triangle is non-degenerate.  
- Realize every edge as a straight segment; every face as the filled triangle.

**Checks executed.**

| Check | Result |
|-------|--------|
| Non-degenerate face areas | PASS |
| Improper triangle–triangle intersections | **0** |
| Improper edge–triangle piercings | **0** |
| Straight-line embedding valid | **True** |

**Theorem O5.2 (Cat B).**  
The map above is a PL embedding \(|K^+|\hookrightarrow\mathbb{R}^3\).

(Category B continuum geometry only; not a residual foundation theorem.)

---

## 6. Ball spine from embed + collapse

**Classical fact (library).**  
If a collapsible 2-polyhedron \(P\) is PL-embedded in \(S^3\) (or \(\mathbb{R}^3\subset S^3\)), then a regular neighborhood \(N(P)\) is a PL 3-ball and \(P\) is a spine of \(N(P)\).

**Theorem O5.3 (Cat B).**  
Primary \(K^+\) is a **PL spine of a 3-ball**.  
Proof: O4 collapsible + O5.2 embedding + classical regular-neighborhood fact.

**Corollary O5.4 (Cat B).**  
In dimension 3, PL ⇔ smooth for manifolds, so \(N(K^+)\) carries a smooth structure as a 3-ball. CB4 checklist **O5** and **O6** are settled for the ball case.

---

## 7. What this is not

| Claim | Status |
|-------|--------|
| Closed special spine of a closed 3-manifold | **False / not claimed** (no triple lines) |
| Residual Category A | **Forbidden** |
| \(G_4=539.90\,\mathrm{s}\) identified with ball geometry | **Forbidden** |
| Unique BSpin on \(K^+\) already extended to the ball | **Open → O7** |
| HQH-539 security reduction | **Not claimed** |

---

## 8. Updated CB4 checklist

| ID | Statement | Status |
|----|-----------|--------|
| O1 | \(H_*\cong\mathrm{pt}\) | SATISFIED (A5⁺) |
| O2 | Unique BSpin on \(K^+\) | SATISFIED (A4⁺) |
| O3 | PL cone fill CB1 | SATISFIED |
| O4 | \(\pi_1=1\) / collapsible | **PROVED Cat B** |
| **O5** | **Spine of compact 3-manifold (ball)** | **PROVED Cat B** |
| **O6** | **Smooth structure** | **SATISFIED Cat B** (dim-3 PL⇔smooth for the ball) |
| **O7** | **Spin extension to \(M\cong B^3\)** | **OPEN Cat B** (live next) |
| O8 | No residual A promotion | HARD RULE |

---

## 9. Live next obstruction: O7

Extend the unique A4⁺ \(B\mathrm{Spin}\) structure on \(K^+\) to a spin structure on the regular neighborhood ball \(N(K^+)\cong B^3\).

Note: \(B^3\) is contractible and admits a unique spin structure up to isomorphism; the question is **compatibility / extension** from the skeleton data \(\Phi^{\mathrm{Spin}}\) of A4⁺, still Category B.

---

## 10. Bottom line

> **O5 closed under Category B:** primary \(K^+\) PL-embeds in \(\mathbb{R}^3\) by an explicit straight-line scheme; with O4 collapsibility it is a spine of a PL (hence smooth) 3-ball.  
> Not a closed special spine. Residual Architecture A through A5⁺ untouched.  
> **Next live Cat-B item: O7 spin extension.**

*Per aspera ad astra.*
