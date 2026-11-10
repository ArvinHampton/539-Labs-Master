# RTA v18 SAFE OUTLINE — algebraic results and Owner definitions only
Date: 2026-11-09 ~16:52 CST (America/Chicago)
Ordered by: Owner voice call-9c8fa1db (relay), after Auditor readiness recommendation (sha 59da9186…): safe outline of proved algebraic results plus Owner definitions; **no geometric draft**.
Nature: **OUTLINE only**, not a manuscript draft and not a freeze. Nothing is locked by this file.
Tip 7cddb188 untouched. No CERT. No Gemini / outside service. Additive create only.

## 0. Purpose and hard rules
This outline is the scaffold Auditor called the “safe option”: list what is already on record as **PROVED** algebra (from frozen RTA Foundation Bound **v16**) together with today’s **Owner DEFINITIONS / conventions**, and keep every geometric claim out.

**Excluded from this outline (hard rule):**
- any vacuum claim (MN \(\mathcal{N}=2\), MN \(\mathcal{N}=1\), BBBW, former (D));
- any junction claim (Israel matching, cut \(b\), D3 solutions);
- any Bridge C **geometric** assertion (11D map, \(V_7^{\mathrm{eff}}\), \(G_5\), physical role of \(R_c\));
- any statement that freezes a neutral item.

The words **brane** and **face** appear below **only** as verbatim Owner definitions; **no geometric claim** is made from them here.

Status labels used below are kept distinct: **PROVED**, **CONDITIONAL**, **OPEN**, **REFUTED**, plus **DEFINITION** / **CONVENTION** for Owner choices (definitions are not proofs).

---

## 1. Source verification
| Object | Path | sha256 (full) | Check |
|--------|------|---------------|-------|
| RTA Foundation Bound **v16** (frozen) | `papers/RTA_FOUNDATION_BOUND/RTA_FOUNDATION_BOUND_v16.pdf` | `1fe7b8a2e245e90009c41726db13518b4c752e99ba4e08b4ffd006d8a73c3297` | Matches sidecar `RTA_FOUNDATION_BOUND_v16.pdf.sha256`. PDF not modified. |
| Theorem-label aid (optional) | `papers/RTA_FOUNDATION_BOUND_v17_DRAFT_2026-11-05_2037CST/audit_theorem_count_2026-11-05/v16_pdf_theorems_cleaned.csv` (+ Part I headers recovered from `pdftotext`) | — | Labels only; status comes from v16 itself. |
| Owner write t4337 (brane / face / Ξ) | `OWNER_WRITE_MAINCHAT_t4337_BRANE_M5_FACE_10D_XI_TWIST140_REST_NEUTRAL_2026-11-09_1644.md` | `f283cffd365ca7368a9f7b5dfdca7ee177ed54db25a28c1944999a5af755e5b6` | Matches sidecar. |
| Owner write blueprint (Λ₀, \(R_c\)) | `OWNER_WRITE_MAINCHAT_BLUEPRINT_1509_CORRECTED_ADOPTED_2026-11-09_1511.md` | `5a6e717732c413a39c89d9b95c9b17455ecf4da8dd64e8bb9d879f427e6a845c` | Matches sidecar. |
| Owner write t4315 (\(P_{\mathrm{rev}}\), \(G=\tfrac12 T^{(\mathrm{EH})}\)) | `OWNER_WRITE_MAINCHAT_t4315_PREV_T1_AND_HALF_TEH_CONVENTION_2026-11-09_1553.md` | `2d1e877e292832e905e1b566f6d89eb589e96c27512fc8e0756bb5a254edb58a` | Matches sidecar. |

v16 hash: **OK** (prefix `1fe7b8a2…`).

---

## 2. Owner DEFINITIONS (standing; not proofs)
Source: OW `5a6e7177…` (15:11) and OW `f283cffd…` (16:44), amending the 16:31 neutral state (`5f59e33e…`) **only** for brane, face, and Ξ.

| ID | Definition (verbatim sense) | Source sha | Notes |
|----|-----------------------------|------------|-------|
| D-Λ₀ | \(\Lambda_0 := \ln(6+\sqrt{35})/\sqrt{10}\) (\(\approx 0.7835772\)) | `5a6e7177…` | **DEFINITION.** Dynamical derivation of why this value is selected remains **OPEN** (see §6). |
| D-\(R_c\) | \(R_c := \kappa\,\ell_P\) with \(\kappa=\sqrt{2/\Lambda_0}\) (\(\approx 1.597622\)) | `5a6e7177…` | **DEFINITION** of the length. Physical role of \(R_c\) stays **OPEN / neutral** (OW `5f59e33e…`, confirmed `f283cffd…`). PP’s DP-Rc is **not** adopted. |
| D-brane | brane := a stack of wrapped M5-branes | `f283cffd…` | **DEFINITION only.** No vacuum, wall, or flux claim is asserted in this outline. |
| D-face | face := the 10D matching hypersurface | `f283cffd…` | **DEFINITION only.** No Israel / junction solution is asserted here. |
| D-Ξ | \(\Xi := 49a1 \otimes \chi_{140}\) (conductor \(19600\), Fricke \(+1\)); the twist by \(-20\) is **not** Ξ | `f283cffd…` | **DEFINITION.** Ties the proved class-number identity for \(\Lambda_0\) to Ξ’s twisting character; that link is structural, not dynamical. |

**Still neutral (not defined here):** joint carrier; \(R_c\)’s physical role; DP-a (no stance); Layer2 (no stance / not locked); baseline. See §6.

---

## 3. Owner CONVENTIONS (standing; not vacuum claims)
Source: OW `2d1e877e…` (15:53).

| ID | Convention | Source sha | Accompanying PROVED algebra (cited) |
|----|------------|------------|-------------------------------------|
| C-\(P_{\mathrm{rev}}\) | \(P_{\mathrm{rev}} =\) reading **T1**: \(P_{\mathrm{rev}} := (S\cdot\hat P)|_{H_-} = P_-\). T2 rejected. \(\hat P=(\gamma^0\Pi\otimes\sigma_x)K\) kept as inter-sector swap. | `2d1e877e…` | On \(H_-\): \(P_-^2=-1\) and \(P_- H P_-^{-1}=-H\) — **PROVED** (PP audit `c9c6ed65…` = `FINDINGS_PP_AUDIT_NL_F2_PREV_MINUS_U_SECTOR_2026-11-09_1530.md`). Geometric action of \(P_{\mathrm{rev}}\) on a bulk vacuum is **OPEN** (map bulk\(\to H\otimes\mathbb{C}^2\) missing) and is **not** claimed here. |
| C-G | Field-equation convention: \(G_{MN}=\tfrac12 T^{(\mathrm{EH})}_{MN}(G_{\mathrm{std}})=T_{\mathrm{std}}(G_{\mathrm{std}})\). Alternative of rescaling \(T^{(\mathrm{EH})}\) coefficients rejected. | `2d1e877e…` | \(T^{(\mathrm{EH})}=2\cdot T_{\mathrm{std}}\) — **PROVED** (PP audit `8be401ed…` = `FINDINGS_PP_AUDIT_NL_F1_TEH_ADS5S4SIGMA2_2026-11-09_1530.md`). No vacuum geometry and no \(G_5\) claim are made in this outline. |

---

## 4. Post-v16 PROVED arithmetic on record (2026-11-09)
These are algebraic / arithmetic facts filed after v16; each is marked with its findings source. None of them adopts a vacuum or solves a junction.

| ID | Statement | Status | Source file (sha prefix) |
|----|-----------|--------|--------------------------|
| A1 | \(W_{49}\) (Fricke \(\tau\mapsto -1/(49\tau)\)) acts as \(-1\) on the newform \(49a1=49.2.a.a\) | **PROVED** | PP audit `389c2f7c…` (`FINDINGS_PP_AUDIT_LOCAL_XI_WEIL_CARRIER_FRICKE_DICTIONARY_2026-11-09_1525.md`); Local XF C7 `72222fed…` |
| A2 | \(\dim S_2(\Gamma_0(49))=1\) and \(S_2(\Gamma_0(49))^{+}=0\) (the \(+1\) Fricke eigenspace of cusp forms vanishes) | **PROVED** | PP `389c2f7c…` |
| A3 | Twists of \(49a1\) by \(-20\) and by \(140\) both have conductor \(19600\) and Fricke sign \(+1\) (via \(\mathrm{ellrootno}=-1\Rightarrow w=+1\)) | **PROVED** | PP `389c2f7c…`; RELABEL `ce4d9e80…` |
| A4 | \(\Lambda_0=\mathrm{Reg}(\mathbb{Q}(\sqrt{35}))/\sqrt{10}\) with fundamental unit \(\varepsilon=6+\sqrt{35}\) (norm \(+1\)), PARI-certified | **PROVED** | MR1/PP amend `0ea030ae…` (`FINDINGS_MR1_B_SEC3_APPELL_RC_S2_S4_AMEND_PP_AUDIT_2026-11-09.md`) |
| A5 | Class-number identity: \(\Lambda_0=\sqrt{7/8}\cdot L(1,\chi_{140})\) (disc.\(140\), \(h(140)=2\), Dirichlet formula) | **PROVED** | MR1/PP `0ea030ae…`; typecheck log `6e7cd1c5…` |
| A6 | Weil / Eisenstein carrier \(g_+=\theta_1^2-7\theta_1(7\cdot)^2\) is Fricke \(+1\) at \(\Gamma_0(49)\) and Eisenstein (cusp projection \(0\)) | **PROVED** | Local `ae951f3e…`; RELABEL `ce4d9e80…` |

Under D-Ξ, A5 becomes a **structural** link from \(\Lambda_0\) to Ξ’s character \(\chi_{140}\). It is still **not** a dynamical derivation (**OPEN**, §6).

---

## 5. v16 algebraic theorem ledger (PROVED as stated by the manuscript)
Scope: printed **Theorem** headers in frozen v16 (`1fe7b8a2…`), recovered by `pdftotext` and cross-checked against the Auditor theorem-count CSV / Part I census.  
**This outline does not re-prove or re-audit them.** Items are listed because v16 itself presents them as theorems (Category A / Part I complete proofs, per v16’s own status conventions).

Where v16’s own Status box explicitly says the proof is **conditional** on an external citation (Baker, etc.), the item is listed under §5.4 as **CONDITIONAL** (as stated by v16), not as unconditional PROVED.

Citation restatement “Theorem 8.1 (Part I…)” in the foundation section is **not** double-counted.  
“Theorem 11.11” is **excluded**: v16 states it is not part of the law and stays Category B.

### 5.1 Part I — s-series (11 theorems)
| Thm | Short title / statement cue | Status in outline |
|-----|-----------------------------|-------------------|
| 5.1 | Squarefree \(k\): \(g_k(k(k+2))=0\) | **PROVED** (v16) |
| 5.3 | Zero classes at \(d=k^2+jk+b^2\) (prime-power \(k\)) | **PROVED** (v16) |
| 5.5 | Zero classes for \(b\in\{1,2\}\) | **PROVED** (v16) |
| 6.6 | \(A_1>A_2\) inequality (odd \(k\), except \((s,k)=(4,15)\)) | **PROVED** (v16) |
| 6.9 | \(g_k((k+2)^2-3)\neq 0\) for odd \(k\) with exactly two prime factors, except \(k=15,21\) | **PROVED** (v16) |
| 7.4 | One-sign classes: finiteness of zeros | **PROVED** (v16) |
| 7.6 | Sign law for \(g_2(d)\) | **PROVED** (v16) |
| 7.7 | Even \(k\geq 8\) at \(d_k=(k+2)^2-3\) | **PROVED** (v16) |
| 8.1 | Parity dominance for odd \(k\in\{3,\ldots,33\}\) | **PROVED** (v16) |
| 8.12 | Algorithm C: all 312 cells admit admissible \(\tau_0\) | **PROVED** (v16) |
| 8.22 | Complete zero sets for odd \(k\in\{3,\ldots,33\}\) | **PROVED** (v16) |

### 5.2 Part II — Bridge Series C (algebraic / modular structure)
| Thm | Short title | Status in outline |
|-----|-------------|-------------------|
| 11.1 | Shared remainder | **PROVED** (v16 Cat A) |
| 11.2 | Real-quadratic decomposition and ray class | **PROVED** (v16 Cat A) |
| 11.3 | Radial asymptotics and partial zeta values | **PROVED** (v16 Cat A) |
| 11.4 | Gauss-mean pattern and zero set | **PROVED** (v16 Cat A) |
| 11.6 | Theta lift and vector-valued \(S/T\) law | **PROVED** (v16 Cat A) |
| 11.7 | Lewis–Zagier period formula | **PROVED** (v16 Cat A) |
| 11.8 | Eisenstein/cusp split | **PROVED** (v16 Cat A) |
| 11.9 | Herglotz closed form | **PROVED** (v16 Cat A) |
| 11.10 | Closed form of \(E_R\) | **PROVED** (v16 Cat A) |
| 14.1 | Profile \(S/T\) law | **PROVED** (v16) |
| 15.3 | Cocycle of the \(E\)-part | **PROVED** (v16 Cat A) |
| 19.5 | Tensor factorisation for odd \(s\) | **PROVED** (v16) |
| 20.1 | Dimensions (orbit bound) | **PROVED** (v16) |
| 21.2 | Coset property | **PROVED** (v16 Cat A) |
| 21.3 | Squarefree criterion | **PROVED** (v16 Cat A) |
| 22.1 | \(H_s\) in closed form | **PROVED** (v16) |
| 22.5 | Period 72 at \(x=1/3\) | **PROVED** (v16 Cat A) |
| 23.7 | Closed forms for \(H_s^{\mathrm{axes}}\) | **PROVED** (v16 Cat A) |
| 24.1 | Structure of \(C_{\mathrm{third}}\) (coset / cone / kernel / chains) | **PROVED** (v16 Cat A) |
| 25.1 | Rational \(\zeta\)-curve | **PROVED** (v16 Cat A) |
| 25.2 | Radial expansion of \(g_s\) | **PROVED** (v16 Cat A) |
| 26.2 | Weil realisation of the label representation | **PROVED** (v16 Cat A) |
| 26.7 | \(N_2\)-polarised K3 surfaces | **PROVED** (v16 Cat A; cited Nikulin/Morrison) |
| 26.9 | Automorphisms of \(N_2\)-polarised K3 surfaces | **PROVED** (v16 Cat A; cited Torelli/Nikulin) |
| 27.4 | Uniqueness of the Maass completion | **PROVED** (v16 Cat A) |
| 27.7 | Uniqueness and residual ambiguity of the vector completion | **PROVED** (v16 Cat A) |
| 27.13 | Dimension of the cusp space | **PROVED** (v16) |

### 5.3 Part III — normalized profile, companions, local modular Cat A, foundation
| Thm | Short title | Status in outline |
|-----|-------------|-------------------|
| 33.4 | \(T\)-law and \(S\)-law | **PROVED** (v16) |
| 34.5 | Profile of \(C\) and of \(q^{-7/20}C\) | **PROVED** (v16) |
| 34.6 | Radial asymptotics at leading order | **PROVED** (v16) |
| 34.7 | Vector-valued \(S\)-law of \(C\) at leading order | **PROVED** (v16) |
| 35.4 | Expansion of a piece | **PROVED** (v16) |
| 35.6 | Radial expansion of the 105 companion series | **PROVED** (v16) |
| 37.10 | \(B_{\hat c_1,\hat e_2}=\varepsilon\sqrt{140}\,\vartheta_+\vartheta_-\) | **PROVED** (v16) |
| 37.11 | Laplacian defect of the orthant Siegel lift | **PROVED** (v16) |
| 37.13 | Transformation law of the 105 companions | **PROVED** (v16) |
| 38.2 | Completed odd part: trivial radial expansion | **PROVED** (v16) |
| 38.4 | \(A_1(S_E)=0\) | **PROVED** (v16) |
| 38.5 | \(A_1=A_{\mathrm{lines}}\) | **PROVED** (v16) |
| 39.2 | \(A_2(S_o)=0\) | **PROVED** (v16) |
| 39.3 | Coset-class decomposition at order \(t^0\) | **PROVED** (v16) |
| 39.4 | \(A_2=A_{\mathrm{lines}}^{(2)}+A_{\mathrm{corner}}\) | **PROVED** (v16) |
| 39.23 | Exact \(x\leftrightarrow 1/x\) symmetry of the residual of the fixed \(S\)-matrix law | **PROVED** (v16) |
| 40.1 | Equality of compact and ordinary induction | **PROVED** (v16 Cat A) |
| 40.2 | Socle reduction to \(K_1\)-invariants | **PROVED** (v16 Cat A) |
| 40.3 | Breuil–Mézard / Colmez dictionary identities | **PROVED** (v16 Cat A) |
| 40.5 | Filtration weight ten (\(w(\theta_3 f)=10\)) | **PROVED** (v16 Cat A) |
| 40.6 | Breuil socle formula | **PROVED** (v16 Cat A) |
| 40.10 | Classification of irreducibles of \(\mathrm{GL}_2(\mathbb{F}_p)\) (Brauer-free) | **PROVED** (v16 Cat A) |
| 41.1 | Local cite-lift F1 (weak NP-completeness of residual path problem on odd-\(M\) slice) | **PROVED** (v16 Cat A cite-lift) |
| 41.7 | \(\dim V_{35}^{\mathrm{Hilb}}=14\) and narrow-class components | **PROVED** (v16 Cat A) |
| 41.10 | Rank-one classifier \(D_1\) | **PROVED** (v16 Cat A) |
| 42.3 | Normalized Bridge Series and the 35-component law vector (foundation statement) | **PROVED** (v16) |

**Note (v16 itself):** Local cite-lifts F2–F3 are named in the v16 abstract alongside F1; only **Theorem 41.1** is the printed F1 theorem header. F2/F3 content beyond 41.1 is **status unverified** as separately numbered theorems in this outline (not invented).

### 5.4 v16 theorems whose own Status box is explicitly CONDITIONAL
| Thm | Short title | Condition named by v16 | Outline status |
|-----|-------------|------------------------|----------------|
| 11.5 | Baker obstruction: scalar no-go | Conditional on Baker’s theorem and the \(q\)-expansion principle | **CONDITIONAL** (as stated by v16) |
| 19.3 | Tensor factorisation, \(s=7\) | Conditional on cited congruence | **CONDITIONAL** (as stated by v16) |
| 20.5 | \(\dim V(98)=2406\) | Computer-assisted rank; Status notes stability hypotheses | **CONDITIONAL** / computer-assisted (as stated by v16) |
| 20.11 | Prime-square structure | Conditional on cited (C3); (C1)–(C2) proved | **CONDITIONAL** (as stated by v16) |
| 24.4 | Phase obstruction | (listed with analyticity hypotheses in neighboring Status text) | **CONDITIONAL** (as stated by v16) |
| 24.5 | Sign obstruction | Conditional on cited analyticity of harmonic-Maass cocycles | **CONDITIONAL** (as stated by v16) |
| 24.6 | Structure of \(C_{\mathrm{third}}\) | Partial reliance on cited genus formula | **CONDITIONAL** (as stated by v16) |

### 5.5 Explicitly not claimed by v16 (for clarity; not outline content)
Per v16 abstract / foundation language (not re-derived here): no Petersson formula for Ξ; no Kronecker/four-forces maps; no explicit formula for a boundary vector of \(C\); Bridge link **partial**; residual question for \(C\) **open**; catalogue-only entries (G-A3 \(h\)-table paused; X4 absent) are **not** theorems. Those stay outside this outline’s PROVED ledger.

---

## 6. Excluded / OPEN (not in outline)
Recorded so the outline cannot be misread as resolving them.

| Item | Status | Governing Owner write (sha prefix) |
|------|--------|-------------------------------------|
| Joint carrier | **UNDEFINED / neutral** | `5f59e33e…`; confirmed `f283cffd…` |
| Physical role of \(R_c\) | **OPEN / neutral** | `5f59e33e…`; `f283cffd…` |
| DP-a | **NO STANCE** (neither adopted nor rejected) | `5f59e33e…`; `f283cffd…` |
| Layer2 | **UNRESOLVED**, no stance; not locked | `5f59e33e…`; `f283cffd…` |
| Baseline / “comparison-phase baseline” | **None** | `5f59e33e…` |
| Vacuum choice | **HOLD** — no vacuum adopted; PP MN \(\mathcal{N}=2\) is recommendation only | `aaadb280…` |
| Junction (D3, cut \(b\)) | **OPEN** (definitions allow setup; no solution claimed here). NL has a derivation **go** (`48102805…`) but that is process, not a theorem in this outline | `f283cffd…`, `48102805…` |
| Bridge C (composition) | **PARTIAL** | v16 foundation; Owner record `f283cffd…` |
| Dynamical derivation of \(\Lambda_0\) | **OPEN** (A4–A5 are identities / definitions, not dynamics) | `f283cffd…`; MR1 S2b/S4c |
| Geometric action of \(P_{\mathrm{rev}}\) | **OPEN** (bulk\(\to H\otimes\mathbb{C}^2\) map missing) | stress-test / OW conventions |
| 11D map, \(V_7^{\mathrm{eff}}\), \(G_5\) | **On hold / excluded** from this outline | vacuum hold `aaadb280…`; Auditor readiness `59da9186…` |
| P5a (reading / referent) | **OPEN** (literal text typecheck issues on record) | not part of this algebraic outline |

**REFUTED in this outline’s scope:** none listed. (Separately on record: symmetrizing \(49a1\) to obtain a nonzero Fricke \(+1\) cusp vector is **REFUTED** by A1–A2; that is a negative algebraic fact, not a geometric claim.)

---

## 7. Counts (this outline)
| Bucket | Count | What is counted |
|--------|------:|-----------------|
| DEFINITION | 5 | D-Λ₀, D-\(R_c\), D-brane, D-face, D-Ξ |
| CONVENTION | 2 | C-\(P_{\mathrm{rev}}\), C-G |
| PROVED (post-v16 arithmetic) | 6 | A1–A6 |
| PROVED (v16 theorems, §§5.1–5.3) | 64 | Part I 11 + Part II 27 + Part III/local/foundation 26 |
| CONDITIONAL (v16 Status-explicit) | 7 | §5.4 |
| OPEN / neutral / excluded line-items | 12 | §6 table rows |
| REFUTED (in-scope note) | 1 | “symmetrize \(49a1\) to \(+1\) cusp vector” (algebraic; cited under A1–A2) |
| status unverified | 1 | printed theorem IDs for Local cite-lifts F2–F3 beyond Thm 41.1 |

**Total PROVED items listed:** \(6+64=70\).  
**Total CONDITIONAL items listed:** \(7\).  
**Definitions+conventions:** \(7\).

---

## 8. Problems / caveats
1. **v16 hash:** verified OK (`1fe7b8a2…` matches sidecar). No mismatch.
2. **Not a draft of geometric v18.** Auditor’s start conditions (curvature fix + joint table + PP EFT re-audit + Owner vacuum adoption + audited junction) are **not** met; this file deliberately stops at algebra + definitions.
3. **Theorem census:** Part I header `Theorem 6.9` is present in the PDF but was OCR/extracted with a control character in `pdftotext`; content was confirmed by reading the nearby proof text. Theorem **21.3** is present (Squarefree criterion) and included. Cleaned CSV under-counted some Part I headers; this outline restores them from the PDF text.
4. **Baker / citation conditionals:** seven theorems are listed as **CONDITIONAL** exactly because v16’s Status boxes say so. They are not silently upgraded to unconditional PROVED.
5. **Left out on purpose:** all vacuum/junction/EFT/11D material; NL junction go (`48102805…`) as a theorem; PP vacuum recommendation (`df503cd9…`); any joint-table numbers; any claim that Bridge C is complete.
6. **No tip / CERT / Gemini touch.**

---

## 9. Proposed future paper skeleton (headings only; empty of geometry)
These are **section headings for a later draft**, not content:

1. Introduction and status conventions  
2. Owner definitions and conventions (Λ₀, \(R_c\), Ξ, \(P_{\mathrm{rev}}\), \(G=\tfrac12 T^{(\mathrm{EH})}\); brane/face as definitions only)  
3. Part I ledger (s-series theorems)  
4. Part II ledger (Bridge Series C algebraic theorems)  
5. Part III ledger (normalized profile, companions, local modular Cat A)  
6. Post-v16 arithmetic (Fricke/\(W_{49}\), twists, class-number identity)  
7. Open / neutral board (explicit non-claims)  
8. (Reserved — geometric v18 body: **empty until Auditor start conditions**)  

End of safe outline.
