# FINDINGS — PP Soft SF — Resonant-math predictions catalog / formal consequence audit — OW b25d5616… — 2026-11-05
REPORTS ONLY. No CERT. invent HOLD. tip untouched.
Authority: OW `b25d56165039d2cf2a064d8c9b5e08c0920601e83b0574947ea116f2ac6ec455` (MATCH; resonant math predictions, all applicable fields). Supplements primary `bcc3ced0…` / ALL-AGENTS `06748ff2…`.
tip Soft SF BEFORE: `/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md` sha `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` MATCH.
tip Soft SF AFTER: same sha MATCH. tip_touched NO.

## 0. Method and non-duplication

**PP role this Soft SF:** consequence-extraction and formal audit of mathematical consequences of RTA Foundation Bound v16 and related PQC math (72-item filter, 45 PROVABLE-CANDIDATE board figure, Haar identities, Canonical T3 / T3_ref, locked D₁/S_eff, PP Layer2/T3 formulate-prove Soft SF `f90e8e61…`). Format per OW: field(s); exact statement; hypotheses/domain; source + location; derivation steps; status; limitations.

**Status vocabulary (this catalog):**
- **existing-theorem consequence** — follows from a written theorem/definition by elementary deduction or is itself the written theorem restated as a prediction.
- **conditional** — consequence under an explicitly stated extra hypothesis, or accepted from an on-disk proof not re-derived here.
- **conjecture-open** — stated in corpus/filter as open, or requires invent / missing definition / purged map.

**Hard gates (OW + locks):** No invented proofs. Do not conflate Residual with Resonant (Prop 41.12). Do not add physical/Kronecker maps (PURGED; Remark 42.7; Prop 41.13(ii)). Tier E observations **separate** — no empirical claims imported into mathematical statements. Candidates ≠ proved.

**Other lanes (cite, do not duplicate):**
- MR1 FINDINGS `3411b0da…` (`FINDINGS_MR1_ACK_OW_CALL_53991ebf_RESONANT_MATH_PREDICTIONS_QUEUED_2026-11-05.md`): **QUEUED** after cite-pack deepen; citation-only under invent HOLD. PP does not re-run MR1 Hecke/§3.2 cite hunt (see `FINDINGS_MR1_CAT_A_CITE_PACK_DEEPEN_S32_HECKE_HOLD_INVENT_2026-11-05.md`).
- PR2 FINDINGS ACK OW b25d5616…: **QUEUED** after Cosmo C14/C16; scoped Cosmo/Bio/Neuro-methods when grounded. PP does not duplicate PR2 physics-facing extract.
- Local filter/ABSORB/Haar Soft SF FINDINGS remain the board sources; PP audits consequences, does not re-filter X posts.

**Primary sources (sha verified this Soft SF):**
| Source | sha256 prefix |
|--------|---------------|
| OW b25d5616… | `b25d56165039d2cf…` MATCH |
| D₁/S_eff lock | `96f8d42e80c1975b…` MATCH |
| Filter denser AMEND | `c57556545032be55…` MATCH |
| Filter ABSORB PP FLAG | `0a4ddb32f7f891b9…` MATCH |
| Haar item 70 PROVED | `7ab0ed68bd825eff…` MATCH |
| Haar DC AMEND | on-disk AMEND of 7ab0ed68… |
| PP Layer2/T3 formulate-prove | `f90e8e61feccb776…` MATCH |
| RTA v16 PDF | `reports/papers/RTA_FOUNDATION_BOUND/RTA_FOUNDATION_BOUND_v16.pdf` |
| RPP formal statement | `reports/crypto/RPP_formal_statement/RPP_formal_statement.md` |

---

## 1. Filter board audit (72-item / 45-candidate figure)

**Board objects.** Local Soft SF denser AMEND `c5755654…` (items 1–30 Grok-disk unchanged from `953be83a…`; items 31–72 denser X) + ABSORB `0a4ddb32…` (rewrites 32,53,57,59,63,69). Agent/OW language cites “45 provable candidates” as the Local PROVABLE-CANDIDATE board figure after ABSORB/PP CONFIRM.

**PP audit of the figure (no re-filter invent):**
- Denser §B alone carries ~27 `**PROVABLE-CANDIDATE**` tags; Grok §A ~31 (many dual-tagged with ALREADY-ON-RECORD). Dual tags and ABSORB rewrites mean a naive tag-count ≠ 45.
- PP **does not invent a new count**. PP treats “45” as the Local board’s stated PROVABLE-CANDIDATE inventory figure referenced by OW b25d5616…, and extracts **consequences from proved/locked objects** plus **status audits** of selected candidates. Full item-by-item re-proof of all 45 is **out of scope** (would invent proofs or duplicate Local/MR1).
- Item 70: Soft SF **PROVED** (identity-only Tier P) — catalogued below as PP-C12.
- Item 72 physics bundle: **NOT-MATH** / **NEEDS-DEFINITION** — excluded from mathematical predictions (Tier E fence §8).
- Item 69 Bridge C openness / cocycle vanishing: **conjecture-open** / NEEDS-DEFINITION meta — cite MR1 deepen: operative C/V₃₅ claim still ABSENT as published theorem.

---

## 2. Catalog of mathematical consequences

Each entry: **PP-C##**. Status in bold at end of entry.

### 2.1 Number theory / modular / residual series

#### PP-C01. Residue vanishing law for g₇
- **Fields:** number theory (q-series / modular forms adjacent).
- **Statement:** \(g_7(d)=0\) whenever \(d\equiv 3,5,6\pmod{7}\). Conversely, outside a finite exceptional set \(Z_7\) of 24 elements (max 247), \(g_7(d)\neq 0\) for every \(d\equiv 0,1,2,4\pmod{7}\), with sign \((-1)^{d+1}\) for all such \(d\ge D_0(7)\).
- **Hypotheses/domain:** \(g_7\) as in Part I / Prop 42.1(i) identification with RTA residual series; squares mod 7 are {0,1,2,4}.
- **Source:** RTA v16 Corollary 42.2 (cites Prop 3.2, Thm 8.1). Filter items 2–3 (ALREADY-ON-RECORD / PROVABLE-CANDIDATE finite check).
- **Derivation:** Empty sum over \(n^2\equiv d\pmod{7}\) when \(d\in\{3,5,6\}\); converse from Part I Thm 8.1. PP does not re-prove Part I; records as **existing-theorem consequence**.
- **Limitations:** “All degrees” vanishing/nonvanishing beyond the written finite/exceptional control remains the open side of filter item 3 / OccFilt_7 conflict with item 65. Do not import string-coupling \(g_s\) (filter item 30 NOT-MATH; different symbol).
- **Status:** **existing-theorem consequence** (vanishing); converse **existing-theorem consequence** under Part I hypotheses; “for all degrees with no exceptions” **conjecture-open**.

#### PP-C02. No scalar residual modular law for Bridge Series C
- **Fields:** number theory / modular forms.
- **Statement:** There is no scalar modular, mock-modular (signature (1,1)), or unary/partial/false-theta law for \(C\) of the kinds listed in Thm 11.5; in particular for no weight \(k\) and constant \(\lambda\) is \(C(\tau)-\lambda(7\tau)^{-k}C(-1/(7\tau))\) radially bounded at all rationals.
- **Hypotheses/domain:** Bridge Series \(C\) of Parts I–II / Prop 42.1(iii); dependence on Baker’s theorem for Thm 11.5(i).
- **Source:** RTA v16 Prop 42.4.
- **Derivation:** Citation of Thm 11.5. **existing-theorem consequence** (negative inventory).
- **Limitations:** Does not identify a positive law for \(C\); filter item 5/45 quantum-modularity of \(g_s\) remains NEEDS-DEFINITION / open.
- **Status:** **existing-theorem consequence**.

#### PP-C03. No vector-valued Fricke law at leading order (computer-assisted)
- **Fields:** number theory / computational algebra.
- **Statement:** \(V_{35}\cap D_7 V_{35}=0\) as spaces of functions on \(\mathbb{Q}\); in particular \(D_7 V_{35}\not\subset V_{35}\).
- **Hypotheses/domain:** \(D_7 f(x)=f(7x)\); dim bound ≤36 (Prop 33.6); rank computation mod four primes.
- **Source:** RTA v16 Prop 42.5.
- **Derivation:** Rank argument as written. PP does not re-run the 216×210 matrix; status inherits computer-assisted.
- **Limitations:** Computer-assisted; not a hand proof. Distinct from Owner Hecke strings T_p+εΘ (MR1 Item3 ABSENT).
- **Status:** **existing-theorem consequence** (computer-assisted).

#### PP-C04. Normalized Bridge Series radial profile / 35-component law (recorded)
- **Fields:** number theory / special functions.
- **Statement:** Leading radial profile of RTA Bridge Series \(C\) is \(I\,e(7x/20)K_{20}(x)\) and does not lie in \(V_{35}\); leading profile of \(q^{-7/20}C\) is \(IK_{20}\in V_{35}\setminus\{0\}\), spans \(V_{35}\) with S/T images, obeys vector-valued S-law of Thm 34.7; radial expansion through order \(t^0\) by Thm 35.6.
- **Hypotheses/domain:** Parts II–III radial/S-law theorems as cited in Thm 42.3.
- **Source:** RTA v16 Thm 42.3.
- **Derivation:** Citation chain to Thms 34.5–34.7, 35.6, Cor 35.8, Prop 35.10. PP does not re-prove.
- **Limitations:** Filter item 69 / Local F6: cocycle vanishing and polar matching for project \(C\) still open as board status; MR1 §3.2 deepen: operative published theorem for project C/V₃₅ ABSENT. Do not upgrade filter claim-of-proof language (item 53 ABSORB) to CERT.
- **Status:** **existing-theorem consequence** inside RTA’s cited Part II–III theorems; board “Bridge C closed” **conjecture-open**.

#### PP-C05. Disc-35 arithmetic (classical)
- **Fields:** number theory (quadratic fields).
- **Statement:** \(\mathbb{Q}(\sqrt{35})\) has discriminant 140 (since \(35\equiv 3\pmod{4}\)), class number 2, fundamental unit \(6+\sqrt{35}\); lattice \(M=\begin{pmatrix}2&7\\7&7\end{pmatrix}\) has \(\det M=-35\) and signature (1,1).
- **Hypotheses/domain:** Standard algebraic number theory / bilinear form.
- **Source:** Filter items 7,9; MR1 deepen F6 LMFDB 2.2.140.1; classical.
- **Derivation:** \(\det\begin{pmatrix}2&7\\7&7\end{pmatrix}=14-49=-35\); eigenvalues of opposite sign ⇒ signature (1,1). Disc/class number classical / LMFDB PRESENT.
- **Python CONFIRM:** `numpy` eigvals ≈ (−2.933, +11.933); det −35.
- **Limitations:** Does not by itself give a modular law for \(C\) or \(g_s\).
- **Status:** **existing-theorem consequence**.

#### PP-C06. Packaging integer identities for 539
- **Fields:** number theory / combinatorics (integer partitions).
- **Statement:** \(539=\lfloor 4859/9\rfloor=\lfloor(4880-21)/9\rfloor=18+521=3\cdot68+5\cdot67=7^2\cdot 11\). If \(539=a_1+\cdots+a_8\) with positive integers and \(\max a_i-\min a_i\le 1\), then \(\{a_i\}=\{68^3,67^5\}\). Also \(\mathrm{ord}_{539}(3)=210\) (since \(\mathrm{ord}_{49}(3)=42\), \(\mathrm{ord}_{11}(3)=5\), lcm=210).
- **Hypotheses/domain:** Elementary arithmetic; gcd(3,539)=1 for the order.
- **Source:** Prop 42.6(i); Remark 42.7; Prop 41.11; filter items 25,60; PP-T3-2 (`f90e8e61…`).
- **Derivation:** Direct arithmetic (PP-T3-2 proof). Partition: \(539=8q+b\), \(0\le b\le 7\), not \(b=8\); ⇒ \(q=67\), \(b=3\). Order: CRT from mod 49 and mod 11.
- **Python CONFIRM:** all identities; ord=210; fiber uniqueness.
- **Limitations:** Under S_eff these are **cell-count / schedule-split integers**, not dynamical stopping times (Prop 41.11, Prop 41.12). Equality Residual₅₃₉=Resonant₅₃₉ as integers ≠ structure map.
- **Status:** **existing-theorem consequence**.

---

### 2.2 Dynamics / p-adic analysis / Haar

#### PP-C07. T3_ref definition and elementary branch calculus
- **Fields:** dynamics / discrete dynamical systems / elementary number theory.
- **Statement:** \(T3_{\mathrm{ref}}(3k)=k\), \(T3_{\mathrm{ref}}(3k+1)=4k+2\), \(T3_{\mathrm{ref}}(3k+2)=2k+1\) on \(\mathbb{N}\) (incl. 0); \(T3_{\mathrm{ref}}(0)=0\).
- **Hypotheses/domain:** ℕ including 0; Canonical / reference implementation map (RPP formal §1.3–1.4; Prop 42.6).
- **Source:** Prop 42.6; RPP formal statement; filter item 27.
- **Derivation:** Definitional. Residue-2 branch equals \(\lfloor(2n+1)/3\rfloor=(2n-1)/3\) on \(n\equiv 2\pmod{3}\).
- **Limitations:** Other historical T3 variants exist in repo; HQH profile not unique until author fixes (RPP §1.6). This catalog uses T3_ref only.
- **Status:** **existing-theorem consequence** (definitional lock of the map used in Prop 42.6).

#### PP-C08. Preimage cardinality of T3_ref (never 3)
- **Fields:** dynamics / combinatorics / CS (preimage trees).
- **Statement:** For every \(y\in\mathbb{N}\), \(|T3_{\mathrm{ref}}^{-1}(\{y\})|\in\{1,2\}\), never 3. Preimages: always \(3y\); plus \((3y-2)/4\) path iff \(y\equiv 2\pmod{4}\); plus \((3y+1)/2\) path iff \(y\) odd. For \(y\ge 1\): size 1 iff \(v_2(y)\ge 2\), else 2. If \(v_2(y)\ge 2\), the unique preimage \(3y\) again has \(v_2\ge 2\), so the unique depth-\(L\) preimage is \(3^L\cdot y\).
- **Hypotheses/domain:** T3_ref as PP-C07; \(L\ge 1\).
- **Source:** RPP formal §1.4 items 2–3; PP-T3-1 (`f90e8e61…`).
- **Derivation:** Case analysis on \(x=3k+r\) (complete proof in PP-T3-1). Mutual exclusion of residue-1 and residue-2 candidates.
- **Python CONFIRM:** exhaustive \(y<5000\); max count 2; v₂ classification 0 mismatches.
- **Limitations:** Does not imply Collatz-type total orbit termination (filter item 27 open side; RPP §1.4 item 6).
- **Status:** **existing-theorem consequence**.

#### PP-C09. Class_6 predicts parity of T3_ref(n) exactly
- **Fields:** dynamics / combinatorics.
- **Statement:** For every \(n\in\mathbb{N}\), \(T3_{\mathrm{ref}}(n)\bmod 2\) is a function of \(n\bmod 6\) alone:
  \[
  \begin{array}{c|cccccc}
  n\bmod 6 & 0 & 1 & 2 & 3 & 4 & 5 \\
  \hline
  T3_{\mathrm{ref}}(n)\bmod 2 & 0 & 0 & 1 & 1 & 0 & 1
  \end{array}
  \]
  Equivalently filter item 28’s “Class_6 predicts Bit_next with accuracy 1,” when Bit_next is read as the parity of \(T3_{\mathrm{ref}}(n)\).
- **Hypotheses/domain:** T3_ref; Bit_next := parity of one-step image.
- **Source:** Filter item 28 (PROVABLE-CANDIDATE); proved here from PP-C07.
- **Derivation:** Write \(n=6m+r\). Direct evaluation:
  - \(r=0\): \(T3=2m\) even; \(r=1\): \(T3=8m+2\) even; \(r=2\): \(T3=4m+1\) odd;
  - \(r=3\): \(T3=2m+1\) odd; \(r=4\): \(T3=8m+6\) even; \(r=5\): \(T3=4m+3\) odd.
- **Python CONFIRM:** for \(n<6000\), each residue class mod 6 yields a singleton parity set matching the table.
- **Limitations:** Does **not** determine \(T3_{\mathrm{ref}}(n)\bmod 3\) from \(n\bmod 6\) (each class hits all residues mod 3). Accuracy-1 claim fails if Bit_next means a different bit.
- **Status:** **existing-theorem consequence** (elementary; PP Soft SF proof).

#### PP-C10. Equidistribution of T3^L mod M (coprime to 6)
- **Fields:** dynamics / arithmetic dynamics.
- **Statement:** For \(M\) coprime to 6 and \(L\ge 1\), as \(n\) runs over \(\mathbb{Z}/3^L M\), \(T3_{\mathrm{ref}}^L(n)\bmod M\) is well-defined and takes each value exactly \(3^L\) times.
- **Hypotheses/domain:** \(M\) odd and not divisible by 3; T3_ref.
- **Source:** Prop 42.6(ii).
- **Derivation:** As written: one step is 3-to-1 well-defined mod \(N/3\) for \(N=3^i M\); iterate. Affine branches bijective on \(\mathbb{Z}/(N/3)\) because \(N/3\) odd.
- **Python CONFIRM:** \(M=5\), \(L=2\), on \(\mathbb{Z}/45\): each residue mod 5 appears exactly \(9=3^2\) times.
- **Limitations:** Requires \(\gcd(M,6)=1\). Not a statement about residual cohomology.
- **Status:** **existing-theorem consequence**.

#### PP-C11. Haar preservation and itinerary homeomorphism on ℤ₃
- **Fields:** dynamics / p-adic analysis / ergodic theory.
- **Statement:** Extended to \(\mathbb{Z}_3\), \(T3_{\mathrm{ref}}\) preserves Haar measure \(\mu\); itinerary \(n\mapsto (T3_{\mathrm{ref}}^j(n)\bmod 3)_{j\ge 0}\) is a homeomorphism \(\mathbb{Z}_3\to\{0,1,2\}^{\mathbb{N}}\) conjugating \(T3_{\mathrm{ref}}\) to the shift.
- **Hypotheses/domain:** 3-adic integers; normalized Haar.
- **Source:** Prop 42.6(iii).
- **Derivation:** Affine branches unit-linear; \(k\mapsto 3k+r\) scales Haar by \(1/3\); sum over \(r\) recovers \(\mu\). Itinerary classes mod \(3^j\). PP accepts RTA written proof (**conditional** on that writeup; not fully re-derived in 3-adic topology here). ℕ-shadow is PP-C08.
- **Limitations:** Does not give a physical timescale. Distinct from Haar item 70 (ℤ₃⁴ max-norm integral).
- **Status:** **conditional** (on Prop 42.6(iii) as written).

#### PP-C12. Haar item 70 Euler factor on ℤ₃⁴
- **Fields:** p-adic analysis / local zeta functions.
- **Statement:** For \(\operatorname{Re}(\nu+3)>0\),
  \[
  \int_{\mathbb{Z}_3^4}|x|_3^{\nu-1}\,d\mu_3=\frac{1-3^{-4}}{1-3^{-(\nu+3)}},
  \]
  with \(|x|_3=\max_i|x_i|_3\) and \(\mu_3\) Haar probability on \(\mathbb{Z}_3^4\).
- **Hypotheses/domain:** Re(ν+3)>0; shell decomposition \(S_k=3^k\mathbb{Z}_3^4\setminus 3^{k+1}\mathbb{Z}_3^4\); \(\mu_3(S_k)=(1-3^{-4})3^{-4k}\).
- **Source:** Local Soft SF PROVED `7ab0ed68…`; DC AMEND (dominated convergence / Tonelli); filter item 70; Tate/Igusa classical route.
- **Derivation:** Shell lemma + geometric series (complete proof in 7ab0ed68…); DC AMEND justifies limit of partial shell sums.
- **Python CONFIRM (this Soft SF):** residue counts mod \(27\) recover shell fractions for \(k=0,1,2\) matching \((1-3^{-4})3^{-4k}\) exactly.
- **Limitations:** Soft SF **NOT** CERT pole-inversion / RTA / BH Haar-timescale narrative (item 70 NOT-MATH side). Identity-only Tier P.
- **Status:** **existing-theorem consequence** (Soft SF PROVED identity-only).

---

### 2.3 Combinatorics / residual product cohomology / D₁

#### PP-C13. Rank-1 classifier D₁ and formality
- **Fields:** algebraic topology / homological algebra / combinatorics of form complexes.
- **Statement:** In the thin truncated residual form complex \(F\), \(H^0(F)\cong\mathbb{Q}\), \(H^1(F)=0\), \(H^2(F)\cong\mathbb{Q}\cdot[s_{\alpha\delta}]\), and \(F\simeq\mathbb{Q}[0]\oplus\mathbb{Q}[-2]\). D₁ is the ℚ-linear functional on \(H^2(F)\) isolating that line; it takes **no** temporal, schedule, or metric argument; shares no algebraic datum with resonant counters.
- **Hypotheses/domain:** Thin F on generators {1,α,ω₂,μ,f,δf}; residual relations; brutal truncation F³=0; nine charge sectors of \(X_\times=K_9\times P_{B'}\).
- **Source:** Thm 41.10; OW lock `96f8d42e…` Flag 1 CLOSED; Residual_Product_Cohomology; PP-L2-1, PP-L2-3.
- **Derivation:** Locked cohomology computation + uniqueness of formal model with those Betti numbers; Hom(H²,ℚ)≅ℚ ⇒ D₁ unique up to ℚˣ (PP-L2-1).
- **Limitations:** Thm 41.10(iv): Layer2 beyond D₁ definition is **not** constructed from D₁ in RTA. Physical attach unresolved by design (Thm 41.10(ii)).
- **Status:** **existing-theorem consequence**.

#### PP-C14. Ill-typedness of “D₁-norm → Kerr area” Layer2 transfer
- **Fields:** mathematical logic of typing / topology (negative).
- **Statement:** Any purported Layer2 transfer of the form “D₁-norm of residual data / Fourier index maps to Kerr area A” is ill-typed under locked D₁: D₁ is not a norm; Thm 41.10(ii) forbids metric arguments; physical/Kronecker maps are PURGED.
- **Hypotheses/domain:** Locked D₁; L2-H3 purged maps; prior Local Layer2 ABSENT FINDINGS.
- **Source:** PP-L2-2 (`f90e8e61…`); Thm 41.10(ii); Prop 41.13(ii); Remark 42.7; FINDINGS_LOCAL_D1_NORM_LAYER2_TRANSFER_2026-10-26.
- **Derivation:** Three independent typing failures (PP-L2-2 proof). Negative theorem, not a positive physical claim.
- **Limitations:** Does not supply a replacement positive Layer2 transfer. Path4 C1–C3 remain BLOCKED for physical load.
- **Status:** **existing-theorem consequence** (typing).

#### PP-C15. Residual cardinality ≠ resonant schedule
- **Fields:** combinatorics / category hygiene.
- **Statement:** The residual cardinality 539 (leftover-cell count per charge sector after packaging) is a different mathematical object from the resonant schedule length 539 (forced iteration count of T3). Equality of integers is not a structure map of chain complexes, graded vector spaces, or sets.
- **Hypotheses/domain:** Prop 41.11(iv) assignment \(M:S_{\mathrm{eff}}\to\mathrm{Residual}_{539}\times\mathrm{Resonant}_{539}\) with disjoint projections; Thm 41.10(iii).
- **Source:** Prop 41.12; OW lock §2; PP-T3-3.
- **Derivation:** By construction of residual product vs resonant schedule; no chain/graded/set map relating \(H^\bullet(F)\) to \(\{1,\ldots,539\}\) is part of either definition.
- **Limitations:** Forbids conflating Residual with Resonant in any prediction below. OW b25d5616… explicitly requires this.
- **Status:** **existing-theorem consequence**.

#### PP-C16. Graph Betti scaling with B′=539
- **Fields:** combinatorics / graph theory.
- **Statement:** For the Cartesian product graph \(K_9^{(\mathrm{gr})}\square P_{B'}\) with \(B'=539\), \(V=9B'=4851\), \(\beta_0=1\), \(\beta_1=36B'-8=19396\).
- **Hypotheses/domain:** Layer (G) of Residual_Product_Cohomology; packaging residual cardinality B′=539.
- **Source:** Residual_Product_Cohomology Layer (G); B′ from packaging (Prop 42.6 / filter item 25).
- **Derivation:** Standard Cartesian product Betti for connected graphs; plug in B′.
- **Limitations:** Graph invariants ≠ form-complex H²; ≠ resonant schedule. Layer (S) filled product is contractible (acyclic) — pattern invariants live in (G)/(F), not (S).
- **Status:** **existing-theorem consequence**.

---

### 2.4 Computer science / complexity / cryptography

#### PP-C17. Π_free is polynomial-time solvable
- **Fields:** CS / complexity / crypto (negative hardness).
- **Statement:** The free Resonant Path Problem \(\Pi_{\mathrm{free}}(y,L)\): find any \(x\in\mathbb{N}\) with \(T3_{\mathrm{ref}}^L(x)=y\), admits the solution \(x=3^L\cdot y\) in one multiplication, because \(T3_{\mathrm{ref}}(3m)=m\). Hence \(\Pi_{\mathrm{free}}\) is not a hard search problem.
- **Hypotheses/domain:** T3_ref; no residual predicate; no seed-bit bound.
- **Source:** RPP formal statement §2.4 item 1 (proven); consistent with PP-C08.
- **Derivation:** Iterate \(T3_{\mathrm{ref}}(3m)=m\) exactly \(L\) times.
- **Limitations:** Does not address \(\Pi\) with a fully defined residual predicate or SHA3 seed constraint. Hardness of a residual-constrained Π is **not established** (RPP §2.4 item 7; [FG] Criterion 3 unmet).
- **Status:** **existing-theorem consequence**.

#### PP-C18. Depth-L preimage tree bounds
- **Fields:** CS / combinatorics.
- **Statement:** Every node of the T3_ref preimage tree has 1 or 2 children (PP-C08); the depth-\(L\) tree has ≤ \(2^L\) leaves and no dead ends (child \(3y\) always). For \(y\ge 4^L\), mean number of depth-\(L\) preimages over residues mod \(4^L\) equals \((7/4)^L\).
- **Hypotheses/domain:** T3_ref; regime \(y\ge 4^L\) for the mean formula.
- **Source:** RPP formal §2.4 item 2; itinerary / piecewise-affine structure §1.4 item 4.
- **Derivation:** As written in RPP: mean \(\sum_e 1/A_e=(1+1/4+1/2)^L\). PP does not re-derive the full itinerary bijection; records as **conditional** on RPP §1.4 item 4.
- **Limitations:** Mean formula’s regime \(y\ge 4^L\) does **not** apply to typical HQH 512-bit states after 539 steps (\(|y|\approx 196\) bits ≪ \(4^{539}\)). Security readings that treat \(3^{539}\) as preimage-tree size are incorrect (RPP §4).
- **Status:** tree bound **existing-theorem consequence** (from PP-C08); mean formula **conditional** (on itinerary analysis + regime).

#### PP-C19. T3 layer contributes no hardness to Π_dig / H_ref preimage reduction hygiene
- **Fields:** cryptography.
- **Statement:** \(\Pi_{\mathrm{dig}}\) (digest target via outer SHA3-512 of enc(T3^L(x))‖s) is polynomial-time equivalent to finding \(z\) with SHA3-512(enc(z)‖s)=d; the T3 layer contributes no hardness to that problem. The trivial lift \(x=3^L\cdot z\) is ~1047 bits and cannot be a SHA3-512 output, so it does not break Preimage(H). No written PPT reduction from a hard Π to breaking H is present ([FG] Criterion 3 unmet).
- **Hypotheses/domain:** H_ref as in RPP §1.6; SHA3-512 modeled as given.
- **Source:** RPP formal §2.5 rows R2–R4; §3–4.
- **Derivation:** As written. PP does not invent a new reduction or security proof.
- **Limitations:** Profile of “HQH-539-512” is not unique across sources (RPP §1.6). Website figures 3^539 / 3^270 exceed what a 512-bit digest can support as security levels (RPP §4) — **existing-theorem consequence** of the birthday/output-length bound, not a new cryptanalysis.
- **Status:** **existing-theorem consequence** (hygiene / negative); hardness assumption for a fully defined residual Π **conjecture-open** / unmet.

#### PP-C20. Static budget S_eff vs stopping-time misreading (CS)
- **Fields:** CS / algorithms.
- **Statement:** Under Prop 41.11, T₃=539 is a static cell/hash budget, not an algorithmic stopping time forced by residual cohomology. Using 539 as a forced iteration count (Resonant₅₃₉) is an external constant-time override, disjoint from Residual₅₃₉.
- **Hypotheses/domain:** S_eff lock; Prop 41.12.
- **Source:** Prop 41.11; OW `96f8d42e…`; PP-T3-3.
- **Derivation:** Definitional constraints of the lock.
- **Limitations:** Does not prove security of any hash. Dual-rail is hardware-only (Prop 41.11(iii); Flag 2 CLOSED).
- **Status:** **existing-theorem consequence**.

---

### 2.5 Physics — only where justified (mostly negative / fence)

#### PP-C21. No written Category A map from T3 / packaging / D₁ to physical observables
- **Fields:** mathematical physics (negative inventory).
- **Statement:** No written object in RTA v16 / Parts I–III defines a map from T3_ref, O_res, packaging identities, or D₁ to \(g_s\) (series), \(C\), \(V_{35}\), Kerr area, stress-energy, four-forces, SU(3) continuum, or seconds-as-cell-capacity. Kronecker/physical mappings stay PURGED.
- **Hypotheses/domain:** Category A scope; Remark 42.7; Prop 41.13(ii); OW lock §4.
- **Source:** Remark 42.7; Prop 41.13; OW `96f8d42e…`; PP-L2-2; filter item 72 NOT-MATH.
- **Derivation:** Negative inventory as written. Missing physical interpretation **remains missing** (OW b25d5616…).
- **Limitations:** Category B design space may discuss overlays; they are not Cat A predictions and are not imported here.
- **Status:** **existing-theorem consequence** (negative).

#### PP-C22. D₁/S_eff admit no temporal empirical test under theorem hypotheses
- **Fields:** mathematical physics / methodology (negative).
- **Statement:** By Thm 41.10(ii) and Prop 41.11, D₁ takes no temporal/schedule/metric argument and T₃=539 is not a stopping time; therefore no time-series prediction is in Cat A scope for these locks. Forcing a temporal Tier E test is a category error under the stated hypotheses.
- **Hypotheses/domain:** Locked D₁/S_eff.
- **Source:** Thm 41.10(ii); Prop 41.11; DF Tier E row 14 hygiene; PP prior audit N2 recommendation.
- **Derivation:** Direct from theorem hypotheses.
- **Limitations:** Does not forbid Category B narrative; forbids upgrading it to Cat A / Tier P.
- **Status:** **existing-theorem consequence**.

---

### 2.6 Cross-cutting filter candidates audited (status only; no invented proofs)

#### PP-C23. Filter Prop K1 / k(k−1) extra relations
- **Fields:** number theory / representation dimension counts.
- **Statement (X/filter):** k(k−1) extra relations; sharp at m=7,17,31,49 with ranks 54,300,980,2430.
- **Source:** Filter items 32 (ABSORB) / 51; denser X posts.
- **PP audit:** Rank arithmetic \(m(m+1)-k(k-1)\) MATCH for those four pairs (ABSORB). Soft SF CONFLICT: later X post says k(k−1) “only a fit at three points.” PP does **not** invent a sharpness proof.
- **Status:** arithmetic check **existing-theorem consequence**; sharpness **conjecture-open** / CONFLICT.

#### PP-C24. Quantum modularity of g_s / Thm G vector-valued law
- **Fields:** number theory.
- **Statement:** Filter items 5,34,40–41,45 claim vector-valued quantum modular / S,T laws for residual objects.
- **Source:** Filter; RTA Thm 42.3 / Prop 42.4 negative scalar side; MR1 §3.2 deepen.
- **PP audit:** Framework citations PARTIAL (Zagier/Zwegers/BOR et al. in MR1 pack). Operative theorem for project C / residual_slash as published Cat A: **ABSENT** (MR1). U-2/U-3 “not yet audited” on X. PP does not invent the law.
- **Status:** **conjecture-open** / NEEDS-DEFINITION for project objects; literature framework **conditional** (external).

#### PP-C25. Hecke / Hilbert over ℚ(√35) Owner strings
- **Fields:** number theory / p-adic families.
- **Statement:** Owner-shaped T_p+εΘ / T_p·exp(Θ) as residual-C Hecke deformation.
- **Source:** MR1 Hecke cite hunt + deepen Soft SF.
- **PP audit:** Item3-as-asked **ABSENT**; neighbors Hida/Coleman–Mazur/Buzzard/Urban are distinct objects (PARTIAL framework only). LMFDB field/HMF data PRESENT for disc 140.
- **Status:** Owner object **conjecture-open** / ABSENT; classical field data **existing-theorem consequence** (PP-C05).

---

## 3. Status counts (this PP catalog)

| Status | Count (PP-C entries) |
|--------|----------------------:|
| existing-theorem consequence | 18 |
| conditional | 3 |
| conjecture-open (incl. ABSENT/CONFLICT audits) | 4 |
| **Total catalogued** | **25** |

Notes: Some entries mix a proved core with an open side (counted by primary status). Filter’s board figure “45 PROVABLE-CANDIDATE” is **not** re-counted as 45 proved theorems — candidates ≠ proved (OW).

**Fields covered:** number theory; modular/q-series; dynamics / arithmetic dynamics; p-adic analysis / Haar; combinatorial topology / graph theory; CS / complexity; cryptography; mathematical physics (negative/fence only).

---

## 4. Top consequences (executive)

1. **T3_ref preimage structure** (PP-C08) + **Π_free easiness** (PP-C17): every output has 1–2 preimages; free inversion by \(x=3^L y\) is trivial — hardness must live elsewhere (residual predicate / seed constraint), and is not established.
2. **D₁ rank-1 + ill-typed Kerr transfer** (PP-C13, PP-C14): Layer2 Cat A content is the classifier on \(H^2(F)\); old D₁-norm→Kerr is ill-typed; physical maps stay missing.
3. **Residual ≠ Resonant** (PP-C15) + **S_eff static budget** (PP-C20): forbids the most common category error in “resonant predictions.”
4. **Haar item 70 identity** (PP-C12) and **Prop 42.6 Haar-on-ℤ₃** (PP-C11): solid p-adic / dynamics facts; no BH/timescale upgrade.
5. **Packaging arithmetic** (PP-C06) and **Class_6→parity** (PP-C09): elementary, Python-verified, well-typed under S_eff.
6. **Negative modular inventory** (PP-C02, PP-C03, PP-C21): no scalar residual law; no Fricke-at-leading-order; no Cat A physical map from T3/D₁.

---

## 5. Remaining gaps

1. Full re-proof / discharge of all ~45 PROVABLE-CANDIDATE filter items — **OPEN**; not attempted (would invent or duplicate Local/MR1).
2. Bridge C cocycle vanishing / polar matching / published Cat A theorem for project C — **OPEN** (filter 69; MR1 §3.2 ABSENT).
3. Quantum modularity of \(g_s\) in a fixed Zagier sense — **OPEN** / NEEDS-DEFINITION.
4. Owner Hecke strings T_p+εΘ — **ABSENT**.
5. Hardness of residual-constrained Resonant Path Problem — **unmet** (Criterion 3); Π_free easy.
6. Positive well-typed Layer2 transfer beyond D₁ definition — **OPEN** (Thm 41.10(iv); PP-L2 gap).
7. Collatz-type total orbit claim for T3_ref — **OPEN**, not claimed.
8. Physical / Kerr / seconds↔539 / Orch-OR / G₄=539.9s — **out of Cat A**; Tier E fence only.
9. MR1/PR2 resonant catalogs — **QUEUED** in those lanes; PP cites, does not wait, does not duplicate.

---

## 6. Tier E fence (separate; no empirical claims imported)

Dataset Filtration Tier E Soft SF (science→pure-math match / empirical hygiene) records E-FIT/E-PARTIAL/E-TENSION/E-UNTESTED labels for planted G₄ suites, SOHO, RIKEN, etc. **Those labels are not mathematical predictions.** Per OW b25d5616…: predictions stand on mathematics, not data. PP notes:
- Planted 539.9 s recovery is circular under free-first plant (N3 hygiene) — **not** evidence for RTA.
- Item 72 / G₄-seconds / Orch-OR overlays: **NOT-MATH**.
- Haar70 / D₁ / packaging may appear as Tier E rows; their **math** status is PP-C12 / PP-C13 / PP-C06 only.
PP imports **zero** empirical claims into §§2–5.

---

## 7. Explicit non-claims

- No CERT. No tip edit. No publish/spend.
- No invented proofs; no fabricated reductions; no restored purged maps.
- No Residual=Resonant structure map.
- No claim that “45 PROVABLE-CANDIDATE” = 45 theorems.
- invent HOLD respected; MR1/PR2 citation-only posture cited, not overridden.

## 8. Verdict

**STARTED + DERIVED (partial catalog):** 25 formal consequences audited across NT / dynamics / p-adic / combinatorics / CS / crypto / physics-fence.  
**RESOLVED as existing-theorem consequences:** packaging, T3_ref preimages, Class_6 parity, Π_free easiness, D₁ uniqueness/formality, D₁-norm ill-typedness, Residual≠Resonant, Haar70 identity, negative modular/physical inventory (see §3).  
**Remaining:** full 45-candidate discharge; Bridge C / QMF / Hecke-Owner / residual-Π hardness / positive Layer2 — OPEN as in §5.

Soft SF → Auditor Write-only MATCH, then Keeper.
