# EIGEN-TE-RHOBAR-N36-G1MEM — 2026-10-26 (America/Chicago)
## STATUS: GAP (named premises ABSENT). Path A was tried as a disk audit; it is not runnable. Path B: GAP.
Authority: Rule 3 AUTO ASSIGN, OWNER VOICE call-a0f3f1d1, OW 6b657e97…db918.
Cites, with sha256 re-verified this run: W1 ee9c36f9…da96 ✔; EXACT-CRT 8061c7b2…9d92 ✔; MR1 packaging 6ed0fc31…b0e2 (read; G1-mem defined at line 25); Q18 Sturm EIGEN-TE-Q18-STURM-PROP11-BOUND (b3172d39…, per .sha256 sidecar); ∞ RREF n36_basis_q18_inf_QQ_m7_crt6.sobj 74d8eb15…2686 under /workspace/grok-batches/eigen-n36-503/. Note: /workspace/eigen-n36-503/ does not exist; the artifacts are in grok-batches/eigen-n36-503/.

## What disk supports (Written, MATCH)
1. **Construction is genuine in char 0.** solve36w.sage builds F = Σ Φ_j h_j/Δ^m. Here Φ_j are Serre-derivative chains of the W1 theta seeds (D₆⊗A₄⊗A₆, Borcherds 1998 §4, with the intertwiner to ρ̄₃₆ CERT over CF(140)), and h_j are monomials in E4, E6, Δ at τ, 7τ, 49τ (genuine M_k(Γ₀(49))). The conditions are the full principal part plus the constant term at **all 8 cusps** (header line 8; polar sets have every exponent ≤ 0). So every **char-0** kernel vector gives an element of V = S₄(Γ₀(49), ρ̄₃₆). Membership of char-0 kernel vectors is structural and holds.
2. dim V = 503 is Written (reverse-dimcalc e2b26038…). Rank 503 holds at 6 primes p ≡ 1 mod 980 (EXACT-CRT).
3. The S/T classical families for ρ₄′/ρ₅′/ρ₇′ are PRESENT (W1 table, exact over CF(140)), so they are not ABSENT.

## What G1-mem actually needs, and why it stays open
G1-mem is about the **mod-p** kernel (and its QQ CRT ∞-image): are those vectors reductions of char-0 kernel vectors with p-integral coefficients? Reduction mod p can only raise the kernel dimension, so dim K₀ ≤ dim K_p = 503. Equality, which means the primes are good, is not shown.
- **ABSENT P1 (char-0 rank):** char-0 rank of the 11700×13305 polar matrix over Q(ζ980) = 13305 − 503. Equivalently, a Written theorem that Φ⊗h/Δ^m at m = 7 spans V. No such spanning or rank statement is on disk. EXACT-CRT itself says it is "not an independent char-0 linear-algebra proof".
- **ABSENT P2 (coordinated kernel):** solve36w saves only RREF(Kr·MT), not Kr, and uses uncoordinated ζ49 (EXACT-CRT Obstruction). The coordinated rerun solve36w_z.sage is LIVE (PID 2673289, p = 7946821). The completed _e1/_e2 logs exist, but no Q(ζ49) CRT of Kr is on disk. Even when it lands, CRT is again multi-prime, not char-0, unless paired with a char-0 verification. That verification would be: the reconstructed Kr has exactly zero polar part over Q(ζ980). This check **is** a valid char-0 certificate of P1's lower bound (503 exact char-0 kernel vectors), plus the denominators give p-integrality. It is not run.
- **Compute blocked:** host memory is 13/15 GB used by the LIVE solve42 + solve36w_z. Running the exact char-0 check now would disturb the LIVE processes (constraint), so it was not started.

## Path B (all-cusp Prop 1.1)
Q18 Sturm (b3172d39…) covers only the 89-dim cusp6 block and needs all 56 Ind components. The polar conditions in solve36w are imposed at all cusps, but the **truncation/injectivity** data (the q^18 image) is ∞-only. Even the scalar Γ₀(49) bound 4·56/12 ≈ 18.67 > 18 fails at depth 18. **ABSENT P3:** a Written vector-valued Sturm bound for S₄(Γ₀(49), ρ̄₃₆) (503-block) certifying injectivity of the ∞-truncation through q^18 (or a larger depth that is on disk). Not invented.

## ABSENT list
P1 char-0 rank / spanning at m = 7; P2 coordinated Kr over Q(ζ49) with an exact char-0 zero-polar check; P3 503-block all-cusp (or ∞-only) Sturm premise.
## Recommendation
When solve36w_z finishes: save Kr, CRT over Q(ζ49) with the coordinated r_p rule, then check exactly in char 0 that the polar part = 0 for 503 independent vectors. That closes G1-mem (P1+P2) **without** P3. P3 is still needed only if G1 injectivity relies on q^18 truncation.
## G1 promotion
**NO.** G1 stays PARTIAL, conditional on G1-mem.
## Tip
tip_pre = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91; tip_post: see sidecar line; tip_touched NO. No ν/Cat A coefficients written. No ν fill started. Kerr not touched.
