# FINDINGS — Eigen Pack I D1/D2/D3 pure-math review — 2026-11-05

Status: REVIEW ONLY. No CERT. Tip untouched. No Sage, no matrix generation, no Gemini, no file-hash validation beyond locating the named Pack I fulltext by its published sha prefix.
Usage gate: 83.3% weekly (below 90%); proceeded. Time: ~16:25 CST (America/Chicago).

## Source reviewed

**Pack I companion fulltext** (Owner Soft SF DOCUMENT-ONLY):
`/workspace/quantum-comp/reports/OWNER_DOCUMENT_EXECUTION_DIRECTIVE_UNLOCKING_REVIEW_BLOCKERS_FULLTEXT_2026-11-05.md`
Fulltext sha256 (from sidecar, prefix match as tasked):
`9d2d7e2a3d95152888de3d607ed09a2cf926b2cfc4b6782a5045a158ac6e4a18`

Scope of this review: Eigen-lane claims aimed at blockers **D1** (descent `ℚ(ζ₄₉)→ℚ`), **D3** (cyclotomic norm → `ℚ`-height at polar rank 11197), **D2** (cleared integral matrix), and the claim that **25 primes are sufficient**. Non-Eigen Pack I sections (Appell/`R_c`, Cand-1+, Israel junction, Agent P1–P5) are out of Eigen D1–D3 scope and are not verdicted here except where needed for separation.

Verdict labels (as tasked):
- **REJECT** — precise mathematical claim false or inconsistent (with counter-argument)
- **PROVED-CORRECT** — verifiable
- **OPEN** — unknown, unfamiliar, or unproved

## Claim board (Eigen / D1–D3)

### C0. Group fact: `Gal(ℚ(ζ₄₉)/ℚ) ≅ (ℤ/49ℤ)×`, order 42, cyclic

**Verdict: PROVED-CORRECT.**

`φ(49)=42`. For odd prime `p`, `(ℤ/p^kℤ)×` is cyclic; here `p=7`, `k=2`. Tiny check: `|(ℤ/49ℤ)×|=42` with generators (e.g. 3,5,10,…). This fact alone does not close D1 or D3.

### C1. “Mod 140 Kronecker filter” resolves D1 (descent to `ℚ`)

Pack I text (verbatim sense): obstruction was mixing split/inert primes; filtering residues “strictly via the Kronecker filter modulo 140 (not 35)” resolves descent; with QI constants `(A,B)` locked, “the cyclotomic norm maps canonically onto a bounded `ℚ`-height.”

**Verdict: REJECT** (as a proof / resolution of D1).

**Counter-argument:**
1. **Descent is Gal-stability of the kernel, not a CRT prime filter.**  
   Let `A` be the polar matrix over `K=ℚ(ζ₄₉)`. Descent of `ker(A)` (left) to `ℚ` means the `K`-subspace `ker(A)⊂K^{11700}` is stable under `Gal(K/ℚ)` (equivalently, it is the extension of a `ℚ`-subspace). That is a property of `(A,ker)` over `K`.  
   Choosing which rational primes to use later for modular reduction / CRT does **not** imply Gal-stability. A correct split law for complete splitting in `ℚ(ζ₄₉)` is `p≡1 (mod 49)`, which the N36 runner already targets via `p≡1 (mod 980)`. Relabeling the prime list by a “Kronecker filter mod 140” cannot create Gal-invariance that was not already present in `A`.
2. **Mod 140 is not the split modulus for `ℚ(ζ₄₉)`.**  
   Tiny check: `n=1+140k` is not always `≡1 (mod 49)` (e.g. `k=1`, `n=141≡43 (mod 49)`). Conversely `n≡1 (mod 49)` need not be `≡1 (mod 140)`. So “filter mod 140” is neither necessary nor sufficient for the `ζ₄₉` split condition. (Mod 140 is natural for characters / fields tied to `lcm(4,5,7)=140`, e.g. aspects of `ℚ(ζ₁₄₀)`, not a substitute for proving `ker` descends from `ℚ(ζ₄₉)`.)
3. **QI constants `(A,B)` are a non sequitur for D1.**  
   Bi-Lipschitz / quasi-isometric constants for a map of a Bruhat–Tits tree into hyperbolic space are geometric data. They do not determine whether a cyclotomic linear kernel is Gal-invariant, nor do they define a “canonical” map from cyclotomic field norms to the multiplicative height of rational RREF entries.

**D1 status after Pack I:** still **OPEN** (unproved). Pack I does not supply a valid descent proof. Prior Eigen evidence remains mod-`p` stabilizer checks at two primes only.

### C2. Height bound correctly derived for rank 11197 over `ℚ(ζ₄₉)` (D3), via Kronecker+(A,B)

Pack I cites the conditional envelope `log₂ H ≤ 1.62×10⁷` and asserts that with the Kronecker filter aligned this bound holds and clears the blocker.

**Verdict: REJECT** (as a correct derivation of a D3 height bound / as “UNLOCKED”).

**Counter-argument:**
1. The figure `1.62×10⁷` originates as a **conditional L1–Hadamard envelope** in `FINDINGS_EIGEN_N36_HEIGHT_BOUND_2026-11-05.md`, explicitly **not** a closed proof: it assumed descent, an integral model, house/norm control, and `H≤Had`, with cyclotomic degree-`φ(49)=42` norm inflation called out as a further gap. Pack I does not repair those hypotheses.
2. Pack I gives **no derivation** of Hadamard at polar rank **ρ=11197**, no house bound on `ℤ[ζ₄₉]`-entries, and no lemma passing from `|N_{K/ℚ}(det)|` (or Plücker norms) to the rational height `H` of Gal-invariant RREF entries. Naming “Kronecker filter” and `(A,B)` does not constitute that lemma.
3. Therefore D3 is **not** correctly derived in Pack I. The envelope remains conditional; D3 remains **OPEN**.

### C3. “25 target primes … structurally sufficient” given that envelope (clears blocker)

**Verdict: REJECT.**

**Counter-argument (arithmetic, theorem `2H² < M`):**  
If `log₂ H ≤ 1.62×10⁷`, uniqueness of height-`≤H` rationals requires  
`log₂ M > 1 + 2 log₂ H ≈ 3.24×10⁷` bits.  
At ~22.9 bits/prime, that is **≳ 1.4×10⁶ primes**.  
Twenty-five primes give only `log₂ M ≈ 25×22.918 ≈ 573` bits.  
`573 > 3.24×10⁷` is false. So the conjunction  
“(`log₂ H ≤ 1.62×10⁷`) and (25 primes suffice under `2H²<M`)”  
is **internally inconsistent**.

Separately, the existing 25-prime holdout reconstruction **fails** (prior Eigen FINDINGS): so those 25 primes do not, in the running CRT/LLL pipeline, produce a verified rational RREF.

### C4. D2: “synthesizable script” clearing dens via “128-LQH ALU register array” yields the integral matrix

Pack I: preparing a synthesizable script over the 128-LQH ALU register array to clear rational denominators, yielding a stable integer matrix for disk storage; status “PROCESSING”. No script body is included in the Pack I fulltext.

**Verdict: REJECT** (as a sound construction of the N36 D2 object).

**Counter-argument:**  
Clearing denominators of the **actual** polar matrix (or of its `ℤ[ζ₄₉]` coefficient model) is, in the abstract, a standard and potentially sound step toward an integral model. Pack I does **not** describe that step. It substitutes an RTL / 128-LQH ALU register-array synthesis narrative. That hardware layout is not the N36 polar matrix `11700×13305` over `ℚ(ζ₄₉)` / `ℤ[ζ₄₉]`, and synthesizing ALU RTL does not construct the cleared integral polar matrix required for Hadamard row norms. Category error ⇒ not a sound D2 construction for the Eigen blocker. (Script not supplied; not run, per task.)

**D2 status:** still **OPEN / MISSING DATA** (no integral matrix on disk; Pack I does not provide one).

### C5. Tracking table rows “EIGEN (D1/D3) UNLOCKED” and “EIGEN (D2) PROCESSING”

**Verdict: REJECT** for “UNLOCKED” on D1/D3 (see C1–C3).  
**OPEN** as a process label for D2 “PROCESSING” (documentary status only; no math content).

## Are 25 primes sufficient?

**Refuted** — as Pack I’s claim of structural sufficiency under the cited envelope (inconsistent with `2H² < M`).  
**Refuted in practice** for the current CRT/holdout pipeline (holdout fails on the 25-prime corpus).  
Whether some much smaller true `H` would make 25 primes enough under `2H²<M` remains **OPEN** on the upper-bound side (no proved `H`), but Pack I’s affirmative claim is rejected.

## Summary table

| Claim | Verdict |
|---|---|
| C0 Gal ≅ (ℤ/49ℤ)× order 42 cyclic | **PROVED-CORRECT** |
| C1 Mod 140 Kronecker ⇒ D1 descent to ℚ | **REJECT** |
| C2 Height bound / D3 derived via Kronecker+(A,B) at rank 11197 | **REJECT** (D3 still OPEN) |
| C3 25 primes structurally sufficient under cited envelope | **REJECT** |
| C4 D2 ALU/RTL clearing script = sound N36 integral matrix construction | **REJECT** |
| C5 D1/D3 “UNLOCKED” | **REJECT** |
| 25 primes sufficient? | **Refuted** (Pack I claim + current holdout); true-`H` sufficiency still OPEN without an upper bound |

## Hygiene

- Tip Soft SF LOCK `7cddb188…` not modified.
- No CERT. No Gemini. No Sage. No matrix generation. No external send.
- Companion PRESS: `PRESS_EIGEN_PACK_I_D1_D3_REVIEW_2026-11-05.md`.
