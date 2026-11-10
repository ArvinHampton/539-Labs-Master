# PRESS — Local → PP first, then Keeper — T3ref Cand-1 / Cand-1⁺

Date: 2026-11-05 14:29:41 CST (America/Chicago)
FINDINGS: FINDINGS_LOCAL_SOFTSF_PROVE_OR_REFUTE_T3REF_CAND1_2026-11-05.md
FINDINGS SHA-256: e7648e07d5fd6fc26cc368313ba91b75007ab16e4b3ebd6017566775ee046aca

## Separate mathematical Soft SF verdicts

1. Original Cand-1: “all n∈ℕ₀ eventually enter {1,2}” is **REFUTED**:
   n=0 is fixed forever. This is only a domain counterexample.
2. New primary Local-T3ref-Cand-1⁺ on ℕ_{≥1}, identical floor-division map:
   **PARTIAL**. No general proof or positive counterexample found.
   Exact finite search verifies starts 1 through 10,000,000.

T is not pointwise decreasing: T(3k+1)=4k+2>3k+1.
The residue-2 rule is T(3k+2)=2k+1=(2n−1)/3, retaining the specified floor.
Increasing residue-1 runs are finite but arbitrarily long. For n=3^a−2,
T^j(n)=4^j3^(a−j)−2>n for 1≤j≤a. Thus no fixed bounded-step descent
argument works uniformly, while variable-time descent remains unproved.

Finite evidence: maximum first entry 104 steps at 7,416,848; maximum first
descent 40 steps at 635,929. Saved script and result accompany FINDINGS.
Sample confirmed: 4880 first reaches 1 at step 14, and T^539(4880)=2.

## PP → Keeper route (artifact preparation; not a completed review)

PP: check domain separation, floor arithmetic, run-length induction,
finite-search induction, and the PARTIAL universal verdict. In particular,
do not promote the zero counterexample into a refutation of Cand-1⁺ and
do not promote the finite scan or termination of increasing runs into a
universal proof. After PP review, Keeper should retain these two distinct
statuses. This PRESS does not claim either reviewer has acted.

invent HOLD. Mathematical Soft SF only. No CERT. No physics inference.
Protected tip SHA-256: 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91
tip_touched NO. No agent messages sent.
