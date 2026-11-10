# PREREG: DISCOVER_GRADING_PATH: computationally discovered candidate path predicate, fibre map and ±1 grading
Written 2026-10-24 at about 7:30 PM CDT, after exploration (scripts/explore.py, logs/explore.log; hashes in data/explore.sha256) and before every test below. Owner: Arvin Hampton. Arvin's instruction: "It will need to be computationally discovered." Nothing here is claimed to be a written source. All of it is **Category B** until proved. No bridge claim. Source rule (Architecture_A_Ores_Programme §6): functions on T3 orbits must be labelled as a free-dynamics probe (Option 3). D1–D3 are so labelled.

## Exploration findings that motivate the definitions (pre-test, disclosed)
- T3(u) mod 9 is determined by u mod 27.
- The mod-9 charge-transition matrix (over lifts mod 27) has row and column sums 3.
- Hits on class 3 mod 9 never occurred twice in a row in 200 sample paths.

## Definitions (exact, re-runnable)
- **Charge of a T3 value:** q(u) = u mod 9. This is the written charge partition C_q evaluated on integers; O_res ⊂ C₃ (x_j = 21+9j ≡ 3 mod 9).
- **Path predicate (Option-3 free-dynamics probe) P_res(u_i)** := [q(u_i) = 3], the "residual-charge hit".
- **Fibre map on hits:** β̂(u) := ((u − 21)/9) mod 8 for u ≡ 3 (mod 9). It agrees with the written β♯(x_j) = j mod 8 on O_res.
- **±1 grading on O_res (carrier-only, no orbits):** g(x_j) := (−1)^{τ(x_j)}, with τ the written tower label.
- **Paths:** u₀ = SHA3-512(b"holdout-" + str(s)) as an integer, s = 0..999 (holdout, disjoint from exploration seeds); u_{i+1} = T3(u_i), i = 0..538, giving 539 transitions per path.

## D1 (exact, Category A once proved; exhaustive check)
For every integer u ≡ 3 (mod 9): T3(u) ≡ 1 (mod 3), so T3(u) ≢ 3 (mod 9). Every predecessor class of charge 3 lies in {0, 4, 5}.
Check: all u < 3·10⁶ plus a proof by residues mod 27. PASS iff there are no counterexamples and the proof holds.

## D2 (holdout statistics of P_res)
Prediction: over all 1000 × 539 transitions, the hit fraction h satisfies |h − 1/9| ≤ 4σ, with σ = √(p(1−p)/n), p = 1/9, n = 539 000. Also, zero consecutive hit pairs.
PASS iff both hold. **Flag:** a pass is what pseudo-random behaviour predicts; it is not bridge evidence.

## D3 (holdout fibre distribution of hits under β̂)
Prediction: the χ² statistic of hit counts over the 8 β̂-classes vs uniform is ≤ 24.32 (p = 0.001, 7 dof).
PASS iff χ² ≤ 24.32. Same flag as D2.

## D4 (grading uniqueness on K⁺; exact)
Prediction: g is the unique ±1 grading on O_res, up to a global sign, that is (i) constant on every same-tower edge of K⁺ and (ii) on path edges (j, j+1) has g(j)g(j+1) = (−1)^{δf(j)}.
Check: solve over F₂ on the K⁺ 1-skeleton (A2_enrich, read-only import). PASS iff the solution space has dimension exactly 1 over F₂ (affine; the global sign is the kernel) and contains g.
**Flag:** the existence half holds by construction. Only uniqueness, which needs connectivity, carries content.

## D5 (non-vacuous link test: grading × path)
Prediction: on holdout paths, the hits u with 21 ≤ u < 4880 never occur (u_i ≥ 2^400 for i ≤ 539). So the signed hit sum Σ g over hits that land in O_res is 0 for every path.
**Flag:** this is expected from magnitude alone. It documents that P_res cannot reach O_res itself, only its charge class.
