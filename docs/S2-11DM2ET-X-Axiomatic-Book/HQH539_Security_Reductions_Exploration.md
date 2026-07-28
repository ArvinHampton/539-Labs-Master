# Exploration of HQH-539 security reductions

**Status:** Category B exploration ledger — **no completed security reduction**.  
**Audience:** internal foundation layer / selective peer review.  
**Companions:** `Foundational_Arithmetic_Packaging.md`, `Object539_NonCircular_Construction.md`, `Resonant_Layer_Resolved.md`, Master `SECURITY.md`.

---

## Mandatory framing

All security claims for HQH-539 are **Category B proprietary framework claims**. They are stated only as:

> Computationally infeasible to break with known classical and quantum methods, pending independent peer review of the full S²-11DM²ET-X security reduction.

| Forbidden | Required |
|-----------|----------|
| “Provably secure” | Locked phrasing above |
| “Unbreakable” | Explicit Category B label |
| “Information-theoretic” (for HQH-539 hardness) | Pending independent peer review of the full reduction |
| Claiming a completed, externally verified reduction | Honesty: **none is claimed or supplied here** |

Category A claims remain those that reduce only to standard primitives (e.g. properties of **SHA3-512** under classical/quantum models such as Grover), without invoking the resonant ternary schedule as a hardness source.

---

## 1. Intended security goals

A standard cryptographic hash or KDF is expected to provide:

| Goal | Role for HQH-539 |
|------|------------------|
| Preimage resistance | Hard to find \(m\) given \(H(m)\) |
| Second-preimage resistance | Hard to find \(m'\neq m\) with \(H(m')=H(m)\) |
| Collision resistance | Hard to find \(m\neq m'\) with \(H(m)=H(m')\) |
| High diffusion / avalanche | Single-bit or single-trit input changes → ~50% output-bit flips |
| Resistance to differential and linear cryptanalysis | Structured attacks on the ternary schedule |
| Constant-time execution | Side-channel resistance in software (arithmetic selection on \(T_3\)) |
| Domain separation and fixed output length | SHA3-512 front-end; fixed 539-round body; fixed digest width in product wrappers |

HQH-539 is **constructed** to meet these goals under the **fixed-round regime** below. Construction intent is **not** a proof.

---

## 2. Structural ingredients available for a *future* reduction

These may enter a future argument; they **do not** constitute a reduction by themselves.

### 2.1 Fixed iteration budget (packaging)

Exactly **539** steps under the resonant layer as hard budget (`Resonant_Layer_Resolved.md`):

\[
L_{\mathrm{pack}}
=
\Bigl\lfloor\frac{e^{3}}{\ln 3}\Bigr\rfloor
+
\Bigl(
\Bigl\lfloor\frac{N_{\mathrm{flux}}}{9}\Bigr\rfloor
-
\Bigl\lceil\frac{N_{\mathrm{flux}}}{N_{\mathrm{tow}}}\Bigr\rceil
\Bigr)
=
18+521
=
539,
\]

or single-shot
\[
L_{\mathrm{pack}}'
=
\Bigl\lfloor\frac{N_{\mathrm{flux}}-f_{\max}}{9}\Bigr\rfloor
=
539
\]
under Principle (S) (`Foundational_Arithmetic_Packaging.md`).

| Property | Status |
|----------|--------|
| Non-circular integer (no 539 on RHS) | Yes, under (S) |
| Engineered hard budget | Yes — **not** unrestricted \(T_3\) stopping time |
| Free \(T^\sharp\) basins produce 539 paths | **No** (still 2; Option 3) |

### 2.2 Canonical \(T_3\) step

Integer ternary Syracuse map (Canonical T3), implemented with **arithmetic selection** for constant-time behaviour in production code paths.

**Variant note:** T4121 was evaluated and **set aside**: observed avalanche / preimage behaviour was **weaker** than retained Canonical T3 coefficients (Master `SECURITY.md`).

### 2.3 Domain separation

Initial **SHA3-512** conversion of the message (and optional salt) before ternary rounds — Category A interface to a standard sponge/hash.

### 2.4 Residual carrier \(\mathcal{O}_{\mathrm{res}}\) (optional combinatorial material)

Explicit set of residual flux quanta with
\[
\lvert\mathcal{O}_{\mathrm{res}}\rvert
=
\Bigl\lfloor\frac{N_{\mathrm{flux}}-f_{\max}}{9}\Bigr\rfloor
=
539
\]
(`Object539_NonCircular_Construction.md`).

**Locked provenance for any crypto use:** residual flux quanta under Principle (S) + democratic charge-sector partition — **not** free \(T^\sharp\) origin (`Architecture_A_Ores_Programme.md` §0).

May be used for combinatorial key material or diffusion schedules in **future** designs; not a reduction by itself.

### 2.5 Internal empirical / engineering evidence

| Evidence | Status |
|----------|--------|
| Statistical avalanche observations | Examined internally; **not** a formal reduction |
| Known-Answer Tests (KATs) | Exist in product trees; implementation checks, not hardness proofs |
| Constant-time \(T_3\) step review | Examined internally; platform-dependent; not a full side-channel proof |

---

## 3. What a security reduction would need to establish

A rigorous reduction would map the hardness of finding a **preimage**, **second preimage**, or **collision** for HQH-539 to a **well-defined hard problem**.

### 3.1 Candidate hard problems (discussed; not established)

1. **Fixed-round inversion.** Invert the 539-step ternary iteration under the hard budget (and any projections / checksums present in the full primitive).  
2. **Combinatorial preimage.** Recover a preimage across residual cores, charge/tower labels, or \(\mathcal{O}_{\mathrm{res}}\)-indexed schedules.  
3. **Diffusion breakage.** Break diffusion properties induced by ternary branching under the fixed schedule (differential / linear distinguishers with non-negligible advantage).

### 3.2 Explicitly *not* a standard reduction target (without extra hypotheses)

Claims that rely on the physical **\(G_4=539.9\,\mathrm{s}\)** brane-leakage clock remain internal to S²-11DM²ET-X and are **not** reducible to standard number-theoretic assumptions without additional **physical** hypotheses. They must not be marketed as cryptographic hardness assumptions in the Category A sense.

### 3.3 Completion criteria (none met)

| Criterion | Status |
|-----------|--------|
| Precise game-based definitions (preimage / SPR / CR) for the published HQH-539 API | Pending full public reduction write-up |
| Hard problem \(\Pi\) with accepted status or clear physical/combinatorial statement | Pending |
| PPT reduction \(R\) with advantage relation | **Not completed** |
| Peer review / independent cryptanalysis | **Pending** |
| Published reduction paper | **Not claimed** |

---

## 4. Current status (ledger)

| Item | Status |
|------|--------|
| Combinatorial packaging \(18+521=539\) under (S) | Verified building block |
| Residual carrier \(\mathcal{O}_{\mathrm{res}}\) | Verified building block (residual-flux provenance) |
| Resonant layer = hard budget | Locked interpretive resolution |
| Canonical T3 retained vs T4121 | Engineering choice from internal hardness observations |
| SHA3-512 domain separation | Standard Category A front-end |
| Statistical avalanche / KATs / constant-time \(T_3\) | Internal examination only |
| **Formal security reduction** | **Pending** |
| **Full cryptanalysis** | **Pending** |
| **Independent verification** | **Pending** |

---

## 5. Separation from foundation-layer math

| Foundation result | Crypto use |
|-------------------|------------|
| Packaging length under (S) | Supplies **round count** only |
| \(\mathcal{O}_{\mathrm{res}}\) | Optional combinatorial material; not free dynamics |
| ACE \(N_\star=14\), free basins \(=2\) | **Must not** be sold as “539-step natural hardness from \(T^\sharp\)” |
| No-Go on \(\lambda=\ln 3/539\) from democracy | Intact; does not yield a Banach-rate reduction |
| Architecture A on \(\mathcal{O}_{\mathrm{res}}\) | Combinatorial/topological programme; **not** a crypto proof |
| Bott / \(KO\) discrete layer | Not a security reduction |

---

## 6. Summary

HQH-539 is a **fixed-round ternary construction** whose length is supplied by the **non-circular packaging** under Principle (S). The residual carrier \(\mathcal{O}_{\mathrm{res}}\) enlarges the set of rigorously defined combinatorial objects that may be used for key material or diffusion, always under **residual-flux provenance**.

**No completed security reduction is claimed.**  
All statements of hardness remain under the locked language of **computational infeasibility with known methods**, pending **independent peer review of the full reduction**.

Further exploration of concrete reduction arguments, unpublished parameters, or proprietary attack surfaces is **company confidential** and is **not** expanded here.

---

## 7. Preferred citation snippets

**Category B hardness (only allowed form):**
> Proprietary framework claim (S²-11DM²ET-X) — not independently verified, pending external cryptanalysis. Computationally infeasible to break with known classical and quantum methods, pending independent peer review of the full S²-11DM²ET-X security reduction.

**Round count (foundation, not hardness):**
> The HQH-539 iteration budget equals the packaging length \(L_{\mathrm{pack}}=18+521\) under Principle (S), equivalently \(\lfloor(N_{\mathrm{flux}}-f_{\max})/9\rfloor\).

**Carrier (if used):**
> Optional combinatorial material may reference \(\mathcal{O}_{\mathrm{res}}\), the residual democratic charge-sector flux core of cardinality \(\lfloor(N_{\mathrm{flux}}-f_{\max})/9\rfloor\), not free \(T^\sharp\) basins.
