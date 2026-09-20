# Muon g-2 hold — Belle II pending

Category B · 2026-09-20

Rule: ignore SM lattice QCD for muon g-2 until Belle II 2π or an independent space-like / storage-ring cross-check (MUonE, J-PARC).


## Experimental anchor (applied)

Fermilab E989 final, combined with E821, PDG-style 2026 review:

    a_mu^exp = 116592071.5(14.5) × 10^{-11}


## Theory split (logged, not applied)

WP25 (May 2025, experimental average updated June 2025) refused a new e+e- HVP average because KLOE / BaBar / CMD-3 2π cannot be combined. WP25 therefore used lattice LO-HVP 7132(61) × 10^{-11} and quotes

    a_mu^SM,WP25 = 116592033(62) × 10^{-11}
    Delta a_mu   = 38(63) × 10^{-11}

April 2026 Nature hybrid lattice + agreed low-energy data claims 0.5σ with experiment.
Those closures are not subtracted from E_leak.


## Belle II status (pending)

- 2π ISR on ~428 fb^{-1}: blinded. Sept 2025 talks show a 1.856 fb^{-1} sanity check only.
- 3π (191 fb^{-1}): published; 2.5σ high versus BaBar in the omega region.
- BaBar 2025 blinded 2π on 460 fb^{-1} confirms BaBar 2009. Preliminary 2009+2025 combination a_mu[2π, <1.8 GeV] = 514.4 × 10^{-10} (0.49%).

No Belle II 2π number exists to close the dispersive path.


## Equation hold

    E_leak^mu(t) = (Delta a_mu^{exp-disp} + delta a_mu^{-U})
                   · (g_{-U}^2 m_mu^2) / (8 π^2 M_{-U}^2)
                   · κ_dark
                   · sin(2 π t / 539.9)

Delta a_mu^{exp-disp} frozen at the WP20-style residual.
delta a_mu^{-U} remains free.
κ_dark = 243/539.
G4 carrier unchanged.

J-PARC g-2/EDM commissioning remains ~2028-29 (450 ppb statistical target). Not a 2026 closer.
