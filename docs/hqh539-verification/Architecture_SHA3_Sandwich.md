# SHA3 sandwich implications for HQH-539

**Status:** Structural security analysis (2026-08-01)  
**Construction (Option A / REF):**

```text
                    ┌─────────────────────────────────────────┐
  message || salt → │ SHA3-512  →  ℤ  →  T^539  →  encode    │ → SHA3-512 → digest
                    │  (seed)         (middle)   (min-BE)     │   (finalize)
                    └─────────────────────────────────────────┘
```

Code (`hqh539.py`):

1. `seed = int(SHA3-512(message ‖ salt))`  
2. `fp = T^{539}(seed)` with Canonical \(T\) (r1 → \(4q+2\))  
3. `digest = SHA3-512( encode(fp) ‖ salt ‖ DOMAIN_SEP )` with `DOMAIN_SEP = b""` (REF)  
4. `encode(fp) = fp.to_bytes(⌈bitlen/8⌉, BE)` (minimal big-endian)

**Companion notes:** `Architecture_Collision_4q2.md`, `Architecture_Residue1_4q2_Map.md`, `RFC_Profile_Freeze_Option_A.md`  
**Not a security reduction.** Hardness remains: computationally infeasible with known methods, pending peer review.

Probe snapshot: `sha3_sandwich_analysis_results.json`

---

## 1. Why the sandwich exists

Bare \(T\) (and bare \(T^{539}\)) is **not** a collision-resistant compression function:

- Constructive one-step collisions (r0–r1, r0–r2) that **lift** under iteration  
- Strong **contraction** (~−0.585 bit/step) → free seeds collapse in width  

The outer SHA3 layers supply:

| Layer | Role |
|-------|------|
| **Inner SHA3 (seed)** | Commits the message into a 512-bit seed; adversary does not freely choose integer seeds |
| **Middle \(T^{539}\)** | Domain-specific “qutrit collapse” / product differentiator (not a CR primitive alone) |
| **Outer SHA3 (finalize)** | Randomizes variable-width fingerprint into fixed 512-bit digest; re-binds salt |

Without both SHA3 faces, marketing \(T^{539}\) as a general-purpose CR hash would be unjustified on present structure.

---

## 2. Game-wise implications (informal)

Let \(H(m,s) = \mathrm{SHA3}(\mathrm{encode}(T^{539}(\mathrm{int}(\mathrm{SHA3}(m\|s)))) \| s)\).

### 2.1 Collision resistance (CR)

A collision \(H(m,s)=H(m',s)\) with \(m\neq m'\) (fixed salt) implies one of:

| Path | Meaning | Relies on |
|------|---------|-----------|
| **C1** Seed collision | \(\mathrm{SHA3}(m\|s)=\mathrm{SHA3}(m'\|s)\) | Break SHA3-CR (same length suffix salt) |
| **C2** Mid collision | \(\mathrm{seed}\neq\mathrm{seed}'\) but \(T^{539}(\mathrm{seed})=T^{539}(\mathrm{seed}')\) | Find SHA3 outputs in a \(T^{539}\)-collision pair |
| **C3** Encode alias | \(\mathrm{fp}\neq\mathrm{fp}'\) but \(\mathrm{encode}(fp)=\mathrm{encode}(fp')\) | Should not occur for minimal BE integers |
| **C4** Outer SHA3 collision | Different finalize payloads, same digest | Break SHA3-CR |

**C1 / C4** are standard SHA3 problems.  
**C3** fails for distinct non-negative integers under minimal big-endian (unique representation).  
**C2** is the **sandwich-specific** path: not free integer collisions, but collisions **inside the image of SHA3-512** (as a 512-bit string interpreted as an integer).

> **Implication:** Proven constructive collisions of bare \(T\) (e.g. \(T(6)=T(1)\)) do **not** automatically yield HQH message collisions. An attacker must still place **both** seeds in \(\mathrm{Im}(\mathrm{SHA3})\) (preimage/multi-preimage style work against SHA3) or find a fresh mid-collision among hash outputs.

There is **no** claim here that C2 is computationally hard — only that it is **not free**.

### 2.2 Preimage resistance (PR)

Given \(d = H(m,s)\), find \(m'\).  
Rough ladder:

1. Invert outer SHA3 → recover \(\mathrm{encode}(fp)\|s\) (SHA3 preimage), or  
2. Find any payload that outer-hashes to \(d\), then  
3. Invert \(\mathrm{encode}\) → \(fp\), then  
4. Find \(\mathrm{seed}\) with \(T^{539}(\mathrm{seed})=fp\) (huge preimage tree of \(T\)), then  
5. Invert inner SHA3 for that seed.

Middle \(T\) **increases** preimage branching (many formal preimages per step) but **does not** remove the outer/inner SHA3 barriers. Contraction makes many seeds share fingerprints **in principle**; under random-oracle seeds the expected mid multi-collisions among \(q\) messages scale with image size of \(T^{539}\circ \mathrm{int}\circ \mathrm{SHA3}\).

### 2.3 Second preimage

Similar to CR with one message fixed; C2 still requires a second seed in the same \(T^{539}\) fiber **and** in SHA3 image.

---

## 3. What the sandwich does *not* give

| Non-implication | Why |
|-----------------|-----|
| “HQH-CR ⇔ SHA3-CR” | C2 mid-path may exist even if SHA3 is ideal |
| “HQH-CR ⇔ \(T\) is CR” | \(T\) is **not** CR; sandwich still may be CR |
| Indifferentiability from RO | Structured middle map; not argued here |
| PRF from secret salt alone without proof | Salt is bound twice, but no reduction written |
| Quantum security | Not analyzed |
| Immunity to length-extension | SHA3 is fine; sandwich irrelevant to classic LE |

---

## 4. Encoding and domain-separation subtleties

### 4.1 Minimal big-endian `encode(fp)`

- **Injective** on \(\mathbb{Z}_{\ge 1}\) (and unique width).  
- **Width leaks** bit-length of \(fp\) (and thus coarse size after collapse) to anyone who sees finalize **inputs**; the public digest alone does not expose width if outer SHA3 is opaque.  
- **\(fp = 0\):** Python `to_bytes(0, "big")` **raises** — empty-message paths that collapse to 0 would throw. Empirically rare from 512-bit seeds; still an **implementation footgun** (should use at least 1 zero byte).

### 4.2 Concatenation `encode(fp) ‖ salt`

- **Fixed salt** (usual hash API): map \(fp \mapsto \mathrm{encode}(fp)\|s\) is injective → outer CR reduces cleanly to “distinct payloads.”  
- **Adversarial variable salt** (odd API where salt is attacker-chosen per call and compared across salts): concatenation **without length framing** admits split ambiguities (`F1‖S1 = F2‖S2`).  
  → Prefer `len` prefixes or `SHA3( encode(fp) ‖ domain ‖ salt )` with clear domain separation if multi-salt protocols collide across salts.  
- REF `DOMAIN_SEP = b""` means **no** extra domain tag between fingerprint and salt (product DOMAIN RFC remains optional/deferred).

### 4.3 Double salt binding

Salt enters **inner** and **outer** SHA3. Effects:

- Same message, different salt → different seed **and** different finalize (strong separation in practice).  
- Does not by itself prove related-key security.

---

## 5. Middle map under the sandwich

| Property of \(T^{539}\) | Sandwich reading |
|------------------------|------------------|
| Not CR alone | Acceptable **only because** seeds are SHA3-committed |
| Constructive fibers | Attack surface **C2** if fibers hit SHA3 outputs |
| Contraction to ~196 bits | Finalize input entropy **≤** residual state entropy ≪ 512; outer SHA3 still outputs 512 bits (expansion/randomization, not entropy creation) |
| r1 = \(4q+2\) exact | Algebraic hygiene; **not** a CR source (see collision note) |
| 539 steps fixed | Public, constant-time friendly iteration count |

**Entropy note:** Once the state is ~196 bits, the outer SHA3 cannot create 512 bits of entropy from the fingerprint alone; security claims are about **one-wayness / collision difficulty**, not about 512-bit min-entropy of digests under free message choice (standard for all wide hashes).

---

## 6. Attack sketches (none claimed practical)

| Sketch | Idea | Blocker |
|--------|------|---------|
| Lift bare \(T\)-pair | Use \((1,6)\) etc. as seeds | Need SHA3 preimages of those integers |
| Multicollision on fibers | Poll many messages until two share \(fp\) | Depends on effective image size of \(T^{539}\circ\mathrm{SHA3}\); not free |
| Finalize width oracle | Use timing/errors on `to_bytes` | Implementation issue; use fixed-width P32 if needed |
| Cross-profile mix | REF vs PRODUCT_T4121 digests | Operational; not cryptanalysis |
| Salt-split | Variable salt concat ambiguity | Don’t use unframed variable salts across comparisons |

---

## 7. Empirical snapshot (engineering)

From `sha3_sandwich_analysis_results.json` (5k sequential messages, empty salt):

| Check | Result |
|-------|--------|
| Unique inner seeds | 5000/5000 |
| Unique fingerprints after \(T^{539}\) | 5000/5000 |
| Unique digests | 5000/5000 |
| Salt separates digests | Yes |

This only rules out trivial small-sample collapse; it does **not** prove CR.

---

## 8. Design recommendations (sandwich hygiene)

1. **Keep both SHA3 faces** — never ship raw \(T^{539}\) as a hash API.  
2. **Fix `fp=0` encode** — use `max(1, ⌈bitlen/8⌉)` or fixed 32-byte P32 for RTL parity.  
3. **Frame finalize payload** if salt is ever variable in a multi-salt CR game: e.g. `u16(len(fp_bytes)) ‖ fp_bytes ‖ salt ‖ domain`.  
4. **Profile tags** in protocols (Option A REF vs historical T4121).  
5. **Constant 539** — no message-dependent round counts.  
6. **Do not claim** “based on SHA3 so CR follows” without a written C2 bound.

---

## 9. What a future reduction must handle

A credible CR reduction argument would need at least:

1. Model of SHA3 (RO or standard assumption).  
2. Bound on probability that two independent RO outputs fall in the same \(T^{539}\) fiber.  
3. Treatment of \(\mathrm{encode}\) and salt framing.  
4. Explicit exclusion of free integer-seed games (API is message-based).

Until then, public language stays:

> Computationally infeasible with known classical and quantum methods, pending independent peer review of the full security reduction.

---

## 10. One-diagram summary

```text
  message          free integers
     │                  │
     ▼                  ▼
  SHA3-512          (forbidden API)
     │                  │
     ▼                  ▼
   seed ──► T^539 ──► fp     ← constructive collisions live HERE
     │                  │         but need seed∈Im(SHA3)
     │                  ▼
     │              encode (min-BE)
     │                  │
     └──── salt ───────►│
                        ▼
                    SHA3-512 ──► 512-bit digest
```

**Sandwich implication:**  
Middle map may be algebraically “weak” as a free function; the **commitment** of the inner hash and the **randomization** of the outer hash are load-bearing. Collision analysis of \(4q+2\) alone neither breaks nor proves HQH — it clarifies that **C2 (mid-fiber under SHA3 outputs)** is the structural hinge.

---

*Per aspera ad astra.*
