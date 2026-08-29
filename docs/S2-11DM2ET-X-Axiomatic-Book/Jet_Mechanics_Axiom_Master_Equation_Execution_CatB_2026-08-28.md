Jet Mechanics from the Axiom and Master Equations
2026-08-28

Category B continuum execution only. Residual discrete CORE_FREEZE untouched. Pack+(S) only. Residual-flux provenance mandatory. Residual Ξ is not x_Zj, is not F_stall, and is not a jet transport coefficient. Twin Prime and RH unclaimed. SPARC L2 analog holds. Fifth-order Ledger M (g_s, Bridge C, residual_slash) is not used here.

Target observables, from CMS not from the axiom
- HIN-25-017: unfolded x_Zj = pT(leading recoil jet) / pT(Z) in pp and central PbPb at 5.36 TeV. Quarks lose energy. Strongly quenched quarks survive more often than a leading model allows.
- HIN-23-006: Z-hadron correlations at 5.02 TeV. Soft wake in 1–2 GeV hadrons. Dip near the Z, excess on the away side. Evidence of medium response.
- STAR Nature Communications 16, 9098 (2025): thermal dielectron thermometers T_LMR ≈ 2.01e12 K ≈ 173 MeV, T_IMR ≈ 3.25e12 K ≈ 280 MeV.

These numbers are data. They are not outputs of the derivation below until a scale and a coupling are produced.

1. What the axiom actually forces

Single axiom: exactly three generations of Standard-Model fermions.

Framework chain, already written:
- W_np = e³
- N_flux = floor(e³ × 3^5) = 4880
- Packaging under (S): 18 + 521 = 539. Fibre 3·68 + 5·67. 61 ω-punctures and 243 = 3^5 towers are packaging integers.
- G4 = 539.90 s sits in the master equations as the argument of sin(2π t / 539.90) and of the Phase Law φ(t) = exp(2π i t / 539.90 + δφ_11D).

Category A residual discrete algebra stops at the packaging integers and the T3 map. G4, leakage, and every plasma statement below are Category B.

2. Master-equation hosts that could carry a jet term

5.1 Energy leakage already contains a flavour-sum and an isotope-sum. Neither is a parton shower.

E_leak(t) includes
- the 118-isotope binding sum × sin(2π t / 539.90)
- the Higgs-echo packet
- the 0.181 ρ_DM PBH term
- couplings m_φ Φ, g_s X^M, g_11 Φ ψ

5.6 Quark flavour vibration is the only master equation that names quarks explicitly:

V_flavor(q,t) = sum_{q=u,d,s,c,b,t} m_q g_s X^M(t) sin(2π t / 539.9) e^{-t/τ} + leakage integrals + S ħ Ω e^{-S} + PBH term

5.3 Friction is cosmological drag:
F_friction(t) = 0.9 (γ−1) m_adj v0² (1000/539.9) exp[−t/(τ + γ_LQG N_simplex)] L + ...

None of these three lines contains x_Zj, a jet cone, a colour Casimir, or a fireball lifetime.

Allowed insertion point, same style as the Meso Stall force budget: a high-energy parton of energy E traversing a leakage-modified medium of length L loses energy at a rate that can be written into E_leak as work done on the medium.

ΔE_leak,jet = − ∫_0^L (dE/dℓ) dℓ

The wake is the medium response to that deposited energy. The Z is untouched because it carries no colour and does not couple to the strong part of the leakage channel.

That is a host, not a derivation.

3. L1. Local response form (allowed, unfixed)

Write the measured CMS ratio as a response function of the tagged energy:

x_Zj = ν_jet(E_Z / E_†, L / L_†)

In vacuum (pp) ν_jet → 1 up to ordinary QCD radiation.
In a medium (central PbPb) ν_jet < 1.

The wake density at soft pT is then
δn(pT ≈ 1–2 GeV) ∝ E_Z (1 − ν_jet) × R_wake(Δφ, Δη)

This is the SPARC L1 analogue: g_obs = g_bar ν(g_bar / g_†) became x_Zj = ν_jet(E_Z / E_†). The function ν_jet and the scales E_†, L_† are not fixed by the axiom.

Flavour hierarchy, if later used, can only enter through the existing V_flavor masses m_q as an input list, or through a colour factor that has not been derived. CMS Z+jet at leading order is already quark-rich. That selection is experimental, not an axiom output.

4. L2. Scale hunt from the allowed set

Allowed set for this execution: {3, e³, 4880, 18, 521, 539, 61, 243, G4, G, c, ℓ_P, ħ, T_brane}.
T_brane = 9.75e-11 N is already a phenomenological insertion. It is listed only to show it still fails.

Target QCD / CMS scales
- T_c ≈ 156 MeV ≈ 1.81e12 K (lattice crossover)
- STAR T_LMR ≈ 173 MeV, T_IMR ≈ 280 MeV
- Fireball lifetime τ_fb ≈ 10 fm/c ≈ 3.3e-23 s
- Fireball radius R_fb ≈ 10 fm = 1.0e-14 m
- QCD string tension σ_QCD ≈ 1 GeV/fm ≈ 1.6e5 N
- Jet transport q-hat of order 1 to 10 GeV²/fm
- Typical tagged E_Z of order 40 to 350 GeV (HIN-23-006 window)

What the allowed set actually produces

G4 as a clock against the fireball
τ_fb / G4 ≈ 3.3e-23 / 539.9 ≈ 6.1e-26
G4 / τ_fb ≈ 1.6e25
No integer from {3, 4880, 539, 61, 243} produces 10^25 or 10^{-26}.
Over a fireball the written sine sin(2π t / G4) is constant to one part in 10^25. It averages nothing and drives nothing inside one collision. Same obstruction as SPARC: the AC G4 carrier averages off the static observable.

G4 as an energy
ħ / G4 ≈ 1.22e-18 eV
Needed: 150 MeV to 300 GeV.
Miss: about 10^24 to 10^30.

G4 as a length
c G4 ≈ 1.62e11 m
Needed: 10 fm = 1e-14 m
Miss: about 10^25.

Written T_brane against QCD string tension
T_brane / σ_QCD ≈ 9.75e-11 / 1.6e5 ≈ 6e-16
Miss: about 10^15.
T_brane was already the wrong unit for solar-system S_D2 (miss ~10^32). It is also the wrong unit for a QCD flux tube.

Written R_11
Claimed 85 μm versus fireball 10 fm is a miss of about 10^10, and the written R_11 formula is already short by 10^29 of its own claimed value. Neither length is a jet path length.

Cosmological constant form Λ = 3 / (e³ ℓ_P²) is a continuum Category B claim for vacuum energy. It is not Λ_QCD ≈ 200 MeV.

Packaging integers
61, 243, 539, 4880 are dimensionless. Multiplying them onto ħc / ℓ_P or onto ħ / G4 does not land on 156 MeV, 10 fm, or 1 GeV²/fm without a free exponent. Integer-power fits of the SPARC type (ℓ_P 3^n, t_P 7^n) are excluded by the same rule used on 27 August 2026.

Nearest structured misses, recorded so they are not reused as derivations
- ħc / (ℓ_P × 539) is a Planck energy over 539, far above QCD.
- m_t / 539 ≈ 321 MeV, near STAR T_IMR by digit proximity only. The top mass is an input or a Category B fermion-mass fit, not an axiom output of this execution. Dividing it by B' is not a thermometer.
- T_STAR_LMR / T_c ≈ 1.11. No packaging integer produces that ratio as a prediction.

L2 obstruction, locked
No combination of the allowed set within a factor of three of
T_c, τ_fb, R_fb, σ_QCD, or q-hat.
The nearest numerology is underived. Catalog χ² of x_Zj is not opened.

5. What the master equations therefore do not give

They do not give ν_jet(E, L).
They do not give the CMS statement that highly quenched quarks survive more often than a leading model predicts.
They do not give the 1–2 GeV wake shape.
They do not give STAR’s two-window temperatures as outputs.
They do not replace the colour factor C_A / C_F = 9/4.
They do not identify residual Ξ with energy loss. Ξ is a weight-3/2 residual series of Bridge C. Its degrees are disc-35 lattice points. They are not GeV-femtometer transport.

6. Effective theory that remains allowed

Same status as SPARC P-effective and solar-system P-well: one measured medium scale may be inserted, then the response shape tested.

Insert T_med from STAR or lattice (input).
Insert L_path from Glauber geometry of the chosen centrality (input).
Keep the Z as a colourless tag (Standard Model, not an axiom output).
Write dE/dℓ = − κ_jet T_med² f(E / T_med) or any standard quenching kernel.
Then x_Zj and the wake become predictions of κ_jet only.

That is a one-parameter effective model. It is not a derivation from three generations. κ_jet is not produced by {e³, 4880, 539, G4}.

Flavour vibration V_flavor may modulate κ_jet at the G4 period in a cosmic-time average. A single PbPb event cannot see that period. A 539.9 s modulation of a collider observable would be a Category B search, not a locked term, and ICHEP 2026 HIN-25-017 does not report it.

7. Relation to fifth-order unification

Closed on 2026-08-28: jet mechanics is not derived from g_s, Bridge C, residual_slash, or PW(7,11;3^5). Those objects stay on Ledger M. This execution does not reopen them. The unit-orbit seed of discriminant 35 remains the only fifth-order contact already written into mechanics, and it is a Category B convention for Γ_snap, not for x_Zj.

8. Status

P-jet-L1. CLOSED AS FORM. Local response x_Zj = ν_jet(E_Z / E_†, L / L_†). ν_jet, E_†, L_† unfixed.

P-jet-L2. CLOSED AS OBSTRUCTION. Allowed set does not produce T_c, τ_fb, R_fb, σ_QCD, or q-hat. G4 sine is frozen across a fireball. T_brane is the wrong tension. Residual Ξ is not the kernel.

P-jet-wake. NOT DERIVED. Soft wake is allowed as the medium response to ΔE = E_Z (1 − ν_jet) after L1, once ν_jet is measured or inserted. Not an axiom output.

P-jet-catalog. NOT OPENED. No χ² against HIN-25-017 until L2 hits.

Residual discrete algebra, packaging, Option 3, No-Go, Bridge C discrete locks, and CORE_FREEZE unchanged.

Status code: JET_MECHANICS_AXIOM_MASTER_EQUATION_L2_OBSTRUCTION_2026-08-28
