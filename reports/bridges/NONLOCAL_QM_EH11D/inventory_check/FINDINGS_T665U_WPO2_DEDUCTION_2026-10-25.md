# FINDINGS t665u — W-PO-2 deduction attempt — 2026-10-25 00:24 CDT (America/Chicago)
Auth t665u (deduce only). PREREG prereg/T665U_WPO2_DEDUCTION_20261025/PREREG.md sha 599712c3293b6ee4fedb7c6cd26fc4765985b7631d52a6b59c42563d852ce231 written before result.log sha 388a4a24d54ca099a628801f9a936e79f0d44b49d9dd28438bfb6722c49af70c.
## Premise ledger
| Identity | Source | sha | Tag |
|---|---|---|---|
| Ω₁₁D=Ω₀·f_warp·f_curv·f_b·Φ_flux | OMEGA_11D_STRUCTURAL:10 | 946ba49cc76b4fe30ed0462469cac689dd83726b1309b9ee34307d6e01d79b08 | Cat B pin |
| f_warp/f_curv "explicit form requires compactification" | same :16-17 | same | Cat B pin |
| five terms "each scaled by the single geometric factor Ω₁₁D" | Codex docx :11 | e24c4904e4640182006e5c9d837491097eece69a9d0f398aa2820d77813672da | Cat A |
| N_flux=⌊e³·3⁵⌋=4880; 539.9 s closure | Explicit_Derivations :18,21 | bf202d05a5ed2e8bd657a0caa7bd2fc4d625a3077cc4fcf8ea55d0e9c56f3ace | Cat A |
| warped metric, kb≈0.797, kℓ11≈0.02531 | ARVIN_WRITTEN_NL_VARS | c4d92ca973617e02dcd4123950ae3641c147e75c4da48a7b4e5fd3cbd631d20c | CHAT (convention-unfixed; not forcing) |
| W-PO-3 PARTIAL CONFIRM | AUDITOR/AUDIT_STATUS.md:358 | f27c750e44318dc1cd1f9ad718fd08a8ed56d0fb4d5a6a1049ee2844d5b1b2c1 | Auditor |
## Verdicts
- F×Ω factorization: **DEDUCED** F_total = Ω₁₁D·(F̂_Coul^rel+F̂_SO+F̂_tors+F̂_flux+F̂_leak) (uniform scalar, distributivity, Codex Cat A). Per-term assignment of sub-factors: ABSENT (Codex has one undifferentiated Ω₁₁D).
- Ω₀: ABSENT — needs written 11D volume integral / normalization map from N_flux=4880.
- f_warp(k): ABSENT — needs written compactification ansatz→factor map (e.g. ∫e^{-nA}); CHAT metric not forcing (exponent/measure convention fork).
- f_curv(K): ABSENT — same gap; K=8k² (23010998) gives argument, not function.
- f_b: DEDUCED-tie only (f_b ↔ B'=539), no functional form.
- Φ_flux: DEDUCED-tie (phase locked to 539.9 s period, Cat A); no amplitude form.
- W-PO-2: remains **OPEN/ABSENT** (factor forms not forced); closes only on factorization-table half.
- W-PO-3: **PARTIAL** stands (t660u) + factorization DEDUCED; not finished.
No NL2. No Local Bridge fold. Prior FINDINGS untouched.
