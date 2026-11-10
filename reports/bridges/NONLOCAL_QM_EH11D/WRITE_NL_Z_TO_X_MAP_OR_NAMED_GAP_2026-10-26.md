# WRITE — NL z→x map or named gap (T2.3) — Soft SF write-only, non-tip — 2026-10-26
Lane: Non Local Path · Project Quantum Comp NONLOCAL_QM_EH11D · Written ~18:00 CDT (America/Chicago)
Proof standard (`ef6da7e7…`): each claim is a **PROOF** or a **named UNPROVEN-GAP**. COOK OW `08c8cdb9…`. **Result: PARTIAL + GAP.** The map itself remains a NAMED GAP. The lemmas proved here are about SAMPLE candidates and about obstructions.

## 1. Authority table (live sha256sum, 2026-10-26)
| Item | sha256 |
|---|---|
| COOK OW | 08c8cdb9f851f85add943c18705a77c4de899464e29c9389e1663a42dcc05411 |
| Invent-ban lift | ef6da7e7d6d97e115cabf7fa661fbc262180cdde9de39b41a123da2347076192 |
| Free-pursue FINDINGS (T2.1–T2.3 source) | f82989d74faaf2c59eb9b52c95d3ae7fb516fa0893c67171c022c906b1b0816d |
| PROOF NL-JOIN-1 | 946a5910ead0631eca28c5971a74d28d61b66e853f8cb8d88c1cd7b42c88d2fe |
| δ_W₇ invent-scope (nodes {1/7,3/7,5/7,1}, x∈(0,1]) | 45bc050a5c003b4858c1f4e39adf720379dd419ad64830de84384a82e1f3d561 |
| Sheet params (z = 1…118) | da91ad83ac35a2f3a897dbd1794b90d102b409284012b889d6b74849e3af5998 |
| Hybrid runnable-spec | 27058bad386fc64dff071324e4f4d248a60113c68349917b42656c93025fe980 |
| Deepen LIFT8 | dcc48a554f322d3b424a921201e342bcfeed0b90ebdd220db51d34aa6c670af4 |
| Write 1 g_s index (this batch) | 1330e8f21b2aa33c1ac8447fd0005ca929fb1e59025fb365a201cb8da54d58f9 |
| PR1 E_leak dependency (FYI cite only) | 9363abad0c859b1e843fc054e586545a3f5cd0f889a1af0af0f61357fabe514b |
| tip Soft SF LOCK (read-only) | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 |

## 2. The gap
- The corpus defines reverse parity only on the RPPT 118-element table indexed by z (Corrected 7D §3.1 `4758d180…`; sheet `da91ad83…`).
- The δ_W₇ node set lives on a phase x∈(0,1] (`45bc050a…` §3).
- **There is no Written map z∈{1…118}→x, and no Written RPPT parity involution on x** (FINDINGS T2.3).
Results already landed (cited, PROOF-BACKED in `f82989d7…`):
- T2.1: W₇x = −1/(7x) sends every x>0 to a negative value, so it does not preserve (0,1].
- T2.2: x↦1−x sends the odd-numerator sevenths {1/7,3/7,5/7} to the even ones {6/7,4/7,2/7}, and sends 1↦0∉(0,1].

## 3. Attempt

### Lemma Z0 (PROOF, obstruction): no parity involution on (0,1] can be the restriction of W₇.
By T2.1, W₇((0,1]) ⊂ (−∞,0), so W₇ has no restriction to a self-map of (0,1]. Any Written involution on x therefore has to be a new object. It cannot be read off from W₇. ∎

### SAMPLE candidate C1 (SAMPLE / UNPROVEN, not Owner-accepted): x = z/118.
This is the simplest normalization of {1…118} into (0,1]. It is **not Written** anywhere in the corpus and is offered only as a test object.
- **Lemma Z1 (PROOF, about C1):** C1 is injective, its image lies in (0,1], and the only δ_W₇ node it hits is x=1 (at z=118). *Proof:* injectivity and range are immediate. Suppose z/118 = k/7 with k∈{1,3,5}. Then 7z = 118k. Since 118 = 2·59 and 7∤118, we get 7 | k, which is impossible for k∈{1,3,5}. ∎
  *Consequence:* under C1 the odd-sevenths nodes are **never sampled exactly**. Stratifying by them would need bins, not node hits.
- **Lemma Z2 (PROOF, about C1):** the reflection x↦1−x is not closed on C1's image. *Proof:* z=118 gives x=1, and 1−1 = 0 = 0/118, which is not in the image (z≥1). ∎

### SAMPLE candidate involution P1 (SAMPLE / UNPROVEN): z ↦ 119 − z.
- **Lemma Z3 (PROOF, about P1):** P1 is a fixed-point-free involution of {1…118}. It reverses parity: z and 119−z always have opposite parity. Under C1 it acts as x ↦ 119/118 − x. *Proof:* P1∘P1 = id. A fixed point would need 2z = 119, which is impossible. The sum z + (119−z) = 119 is odd, so the two have opposite parity. The formula for x is direct substitution. ∎
- **Lemma Z4 (PROOF):** P1 under C1 does not map the δ_W₇ node set into itself. *Proof:* the node set's intersection with the image of C1 is {1} (Z1), and P1 sends x=1 to 1/118 ≠ 1. ∎

Whether "reverse parity" in Corrected 7D means z↦119−z, an even/odd split of z, or something else is **not Written**. P1 is therefore SAMPLE only.

### UNPROVEN-GAP Z5: the missing Written objects
1. **Map definition:** a Written φ: {1…118} → (0,1] (or a Written statement that x is not a function of z), with its source sha.
2. **Parity involution statement:** a Written involution ι on z, on x, or on both, that defines RPPT "reverse parity". If both are Written, they must also satisfy a compatibility law φ∘ι_z = ι_x∘φ.
3. By Z0, ι_x cannot be W₇. If the Owner wants it to relate to δ_W₇, a different normalization of x is needed (for example x∈ℍ, or |W₇x|).
Until items 1 and 2 exist, every RPPT↔δ_W₇ correlation stays a candidate, and C1 and P1 stay SAMPLE.

> **SLOT NL-ZX-MAP-01 (named; NOT decided):** Owner Writes φ (accept C1, or give another map) **and** ι (accept P1, or give another involution), or Writes that no z↔x link exists. This Write accepts neither on the Owner's behalf.

## 4. Explicit non-claims
tip_touched **NO**. Kerr / Path4 C2–C3 **NO**, and there are no Kerr numerics. No χ² data, dof or coefficients. No map is asserted as Owner-accepted, and C1 and P1 are SAMPLE / UNPROVEN. No MC. No tip fold. Eight-only. Soft SF → **Auditor**. sha256 is in the `.sha256` sidecar.
