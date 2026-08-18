# Quantitative Cascade Monte Carlo Modeling for DM Decay Channels

**Status:** Category B continuum exploration only  
**Date:** 2026-08-18  
**Parent note:** Model_DM_Decay_to_Local_Physics_Framework_CatB.md  
**Residual discrete algebra (O_res, packaging 18+521 under Principle (S), K+, A4+/A5+, free T3 under Option 3, permanent class):** Category A pure mathematics, independent, and untouched.  
**Residual-flux provenance:** mandatory. Continuum statements do not derive from the residual discrete core.

## Purpose

Secondary electromagnetic and hadronic cascades convert primary decay products into the photons, electrons, positrons and neutrinos that are actually observed. A quantitative Monte Carlo treatment is required to translate the primary injection rate (decay width times local dark-matter density) into two concrete quantities:

1. the final photon and lepton spectra that confront Fermi-LAT, INTEGRAL, AMS-02, XMM-Newton and related instruments;
2. the fraction of energy that thermalises locally and can therefore source the beta-like gravitational contribution through the stress-energy tensor.

## Standard tools

Publicly available codes already perform the necessary cascade calculations:

- DarkHistory (and successors) tracks energy deposition into ionization, excitation and heating of the intergalactic medium as a function of redshift. Preferred tool for 21-cm and CMB constraints.
- gamma-Cascade and related packages propagate high-energy photons and electrons through the cosmic microwave background and extragalactic background light, producing the softened secondary spectra observed at Earth.
- CRPropa handles three-dimensional propagation including magnetic fields, pair production, inverse-Compton scattering and synchrotron losses; useful for Galactic and extragalactic morphology.
- PPPC4DMID supplies pre-computed secondary spectra for a wide range of primary channels and can be used as a fast look-up table before full Monte Carlo runs.

## Essential physical processes

1. Photon-photon pair production on the CMB and extragalactic background light.
2. Inverse-Compton scattering of electrons and positrons on the same backgrounds.
3. Synchrotron radiation in Galactic and intergalactic magnetic fields.
4. Bremsstrahlung and ionization losses on ambient gas.
5. Hadronic cascades (pion production and subsequent decays) whenever the primary channel produces quarks or gluons.
6. Redshift evolution of all background photon fields and of the expanding universe.

## Quantitative outputs required

A. Secondary photon spectrum dN_gamma / dE at Earth (or at a chosen redshift) for each primary mass and channel. For primary energies above a few TeV the spectrum approaches a nearly universal shape below approximately 100 GeV; the Monte Carlo must quantify residual dependence on injection redshift and magnetic-field strength.

B. Energy-deposition fractions. The fraction of the injected energy that ends in free-streaming photons (gamma-like observable), free-streaming electrons/positrons, local ionization and heating (contributes to the beta-like gravitational channel and to 21-cm heating), and neutrinos (invisible).

Typical numbers for electromagnetic cascades at high redshift indicate that 20 to 40 percent of the energy can be deposited locally into ionization and heating once the cascade has fully developed, while the remainder remains in continuum photons that free-stream. Precise fractions are mass-, redshift- and environment-dependent and must be extracted from the Monte Carlo.

C. Local energy-injection rate after cascading. Primary rate (Gamma_chi times rho_DM) multiplied by the local deposition fraction f_dep. For the long lifetimes already required by observation (10^25 to 10^29 seconds) this rate remains many orders of magnitude below the size of the existing continuum dark-matter density coefficients (including the 0.181 factor). The Monte Carlo therefore confirms that no numerical re-tuning of those coefficients is needed.

D. Morphological and temporal signatures. If primary decays occur inside the condensed mirror plasma, the Monte Carlo should also track the spatial distribution of the leaked secondaries after they cross the D2-brane portals. Any residual modulation at the 539.9-second period would appear as a time-dependent variation in the local deposition rate; quantifying its amplitude is a higher-order target.

## Practical quantification steps

1. Choose representative primary masses (7 keV, 10 MeV, 100 GeV, 10 TeV) and the two baseline channels (pure photon line, pure e+ e-, and a mixed weak-like channel).
2. Run DarkHistory for the high-redshift deposition fractions relevant to 21-cm and CMB bounds.
3. Run gamma-Cascade or CRPropa for the present-day photon and positron spectra that confront Fermi-LAT, INTEGRAL and AMS-02.
4. Extract the local thermalisation fraction f_dep(m_chi, z, channel).
5. Multiply the primary injection rate by f_dep to obtain the effective beta-like energy density available for gravitational effects.
6. Verify that the resulting photon spectra lie below current upper limits for all lifetimes longer than the windows already quoted in the parent note.

## Expected numerical scale

For a lifetime of 10^28 seconds the primary energy-injection rate is already only a few parts in 10^11 of the dark-matter density per Hubble time. After cascading, the locally thermalised fraction is at most of order 0.3, so the beta-like gravitational source term remains negligible compared with the existing continuum coefficients. The Monte Carlo therefore serves mainly to confirm consistency rather than to generate a detectable signal.

## Open quantitative tasks

- Full parameter scan of f_dep across the mass range 1 keV to 100 TeV.
- Inclusion of the portal transmission probability (baseline strength approximately 0.005) as a multiplicative filter on the secondary flux that reaches the ordinary sector.
- Assessment of any residual 539.9-second modulation that survives cascade averaging.
- Propagation of uncertainties arising from intergalactic magnetic-field strength and extragalactic background light models.

## Residual independence statement

All continuum constructions presented in this note, including cascade spectra, deposition fractions, portal filters and any modulation by the 539.9-second period, are Category B exploratory statements only. The residual discrete algebraic core of the framework remains Category A pure mathematics, independent, and untouched. No derivation of continuum physics from the residual discrete algebra is asserted. Residual-flux provenance is required for every continuum claim.

## Outlook

These Monte Carlo quantifications convert the qualitative cascade discussion already present in the continuum framework into concrete spectra, deposition fractions and residual rates that can be compared directly with existing and forthcoming multi-messenger data. The next natural extension is the application of the same cascade machinery to stellar interiors and stellar datasets.
