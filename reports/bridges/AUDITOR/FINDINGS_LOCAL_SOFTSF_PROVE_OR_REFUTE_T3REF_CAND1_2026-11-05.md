# FINDINGS — Local-T3ref-Cand-1 domain correction and Cand-1⁺

Date: 2026-11-05 14:29:41 CST (America/Chicago)
Mode: mathematical Soft SF only. invent HOLD. No CERT.
Primary positive-domain status: **PARTIAL**.
Separate original zero-domain status: **REFUTED**.

## 1. Exact map and target separation

The map is unchanged, with // denoting integer floor division:

- T(n)=n//3 for n≡0 (mod 3).
- T(n)=(4n+2)//3 for n≡1 (mod 3).
- T(n)=(2n+1)//3 for n≡2 (mod 3).

Equivalently, for k≥0:

    T(3k)=k,  T(3k+1)=4k+2,  T(3k+2)=2k+1.

Important arithmetic correction: on residue 2, 2n+1=6k+5 is NOT divisible
by 3. Its floor quotient is 2k+1; the exact affine expression on that
residue is (2n−1)/3, not (2n+1)/3 without a floor. We have not changed T.

### A. Original Cand-1-ℕ₀: REFUTED

Precisely, the statement

    For every n∈ℕ₀ there exists j≥0 such that T^j(n)∈{1,2}

is false. Take n=0. The residue-0 rule gives T(0)=0; induction gives
T^j(0)=0 for every j≥0, and 0∉{1,2}. This closes only the original
zero-inclusive formulation. It says nothing against positive-integer
convergence and resolves no physics claim.

### B. Replacement Local-T3ref-Cand-1⁺: PARTIAL

Precisely, the new candidate is

    For every n∈ℕ_{≥1} there exists j≥0 such that T^j(n)∈{1,2}.

T(1)=2 and T(2)=1. Positive integers map to positive integers: in the
residue-0 case positivity forces k≥1; the other two formulas are positive
for k≥0. Thus no positive orbit can use 0 as an alternative endpoint.

This report does NOT claim a proof or a counterexample for Cand-1⁺.
Its universal assertion remains unresolved by the work below. The optional
ℕ₀ statement of eventual entry into {0,1,2} is logically equivalent to
Cand-1⁺ once T(0)=0 and positivity preservation are noted. It is therefore
also not established universally here; calling {0} and {1,2} the only
attractors would overstate the result.

## 2. Rigorous descent check: the proposed one-step proof fails

For n=3k>0, T(n)−n=−2k<0.
For n=3k+1, T(n)−n=k+1>0 for every k≥0.
For n=3k+2, T(n)−n=−k−1<0 for every k≥0.

In particular 4→6, 7→10, 10→14. Hence T(n)<n for all n≥3 is false.
Failure of this proof method is not a refutation of Cand-1⁺.

## 3. Further rigorous structure, and its limit

### 3.1 Every individual run of residue-1 increases is finite

If n≡1 (mod 3), write n+2=3^a m, with a=v₃(n+2)≥1 and 3∤m.
For 0≤j≤a, the consecutive residue-1 iterates satisfy

    T^j(n)+2 = 4^j 3^(a−j) m.

Proof: the identity T(x)+2=4(x+2)/3 holds exactly whenever x≡1 (mod 3).
For j<a the displayed expression is divisible by 3, so the current value
is residue 1 and the identity applies at the next step. At j=a the
expression is 4^a m, not divisible by 3; hence T^a(n) is not residue 1.
The next step decreases its input, since the remaining residues are 0
and 2. This is an exact proof of termination of each increasing run.

But it does NOT show a decrease below the value at the start of the run.
For example, 7→10→14→9: the first decreasing step still leaves 9>7.
Thus finiteness of increasing runs does not supply well-founded descent.

### 3.2 No uniform bounded-step descent argument of the proposed kind

Let a≥1 and n_a=3^a−2. Taking m=1 above gives

    T^j(n_a)=4^j 3^(a−j)−2,  0≤j≤a.

Consequently T^j(n_a)>n_a for every 1≤j≤a, since (4/3)^j>1.
For any fixed L≥1 and any threshold B, choose a≥L with n_a>B.
Then none of the first L iterates is below n_a. So there cannot be a
universal fixed L such that every sufficiently large start has a smaller
iterate among its first L steps. This rules out that specific strategy,
not an unbounded stopping-time descent theorem or another Lyapunov proof.

### 3.3 A sufficient missing lemma

It would suffice to prove:

    For every n≥3 there exists j≥1 with T^j(n)<n.

Together with positivity preservation and the explicit {1,2} cycle,
strong induction on n would then prove Cand-1⁺: the smaller iterate
already reaches the cycle. Conversely, Cand-1⁺ would imply this lemma
because its orbit reaches a number ≤2<n. This is an equivalent
reformulation, NOT an additional proved premise. It is verified only on
the finite range below. No global Lyapunov or exclusion of all other
cycles/unbounded positive orbits has been supplied.

## 4. Exact finite exploration (evidence, not a universal proof)

The reproducible program in

    local-t3ref-cand1-evidence-2026-11-05/search.py

was executed with Python arbitrary-precision integer arithmetic, N=10,000,000,
and a per-start cap of 100,000 steps. Its output is

    local-t3ref-cand1-evidence-2026-11-05/search-result.json

Result: **every start 1≤n≤10,000,000 reaches {1,2}; no positive
counterexample was found; no cap was reached.**

The algorithm processes n in increasing order. For n≥3 it iterates until
first reaching x<n, checking for repetition and a step cap. Since all
positive smaller starts have already been handled, it then sets the exact
first-entry time h(n)=j+h(x), with h(1)=h(2)=0. This is a finite
strong-induction computation, not an inference about untested starts.
The largest observed first-descent time was 40, far below the cap.

Computed summaries:

- Maximum first-entry time on the tested range: 104 steps, first attained
  at n=7,416,848.
- Maximum first-descent time for 3≤n≤10,000,000: 40 steps, first attained
  at n=635,929.
- Largest value observed across the searched first-descent segments:
  569,520,126, in the segment starting at n=8,562,103.
- Search ran 2026-11-05 14:28:23–14:28:31 CST (America/Chicago).

The initial separate exploratory pass also found no non-target cycle for
starts through 1,000,000; the preserved ten-million run is the reproducible
finite evidence relied on here. Finite search does not rule out a larger
cycle or an unbounded orbit outside the checked starts.

## 5. Required sample, independently recomputed by the saved program

    4880 → 3253 → 4338 → 1446 → 482 → 321 → 107 → 71
         → 47 → 31 → 42 → 14 → 9 → 3 → 1.

The first entry into {1,2} is at step 14. After entry the values alternate
1,2. Since 539−14=525 is odd, T^539(4880)=2, agreeing with the exact
iteration in the program.

## 6. Disposition and boundaries

- Cand-1-ℕ₀→{1,2}: **REFUTED**, n=0.
- Primary Cand-1⁺ on positive integers: **PARTIAL**, finite verification
  through 10,000,000 and rigorous structural lemmas only.
- No global proof or positive counterexample claimed; no literature-wide
  assertion that the candidate is open is made.
- Mathematical Soft SF only. No CERT. No physics conclusion, bridge
  closure, or change of map. invent HOLD remains in effect.
- PRESS is prepared for **PP review first, then Keeper**. Copies in local
  bridge directories are artifact handoff only, not proof of review or
  acceptance. No agent messages were sent.

## 7. Protected tip and integrity

Protected path:

    /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md

Before and after computation SHA-256:

    7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91

**tip_touched NO.** The tip was read for hashing only; it was not edited.
FINDINGS, PRESS, script, and result receive SHA-256 sidecars. FINDINGS and
PRESS plus sidecars are copied to bridges/PROFESSOR_PROOF, bridges/PHYSICIST,
bridges/AUDITOR, bridges/LOCAL, and reports/bridges/AUDITOR. The evidence
subdirectory is also copied to those destinations so the artifacts remain
reproducible at each handoff. Sidecars are integrity metadata, not CERT.
