# FINDINGS — MR1 Soft SF Write-only Cat A cite hunt: Hecke over Q(√35) / residual candidate C (2026-11-03)
Status: Soft SF FINDINGS. Reports only. No CERT. No RECS. tip_touched NO.
Authority: OW 8a0325da19ba3802652a654523b681cf74a623d28a4f1a4484999420098a453b (verified MATCH); tip LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (verified MATCH pre/post); ACK FINDINGS edb0dc42… PRESS c9efc7e9….
Arithmetic note: 35≡3 mod 4 ⇒ disc(Q(√35))=140; ramified primes 2,5,7 (consistent with cue).

## Live-check table (2026-11-03, arxiv.org/abs meta tags or doi.org CSL-JSON)
| # | Citation | ID | Live result |
|---|---|---|---|
| L1 | Dembélé, Voight, "Explicit methods for Hilbert modular forms" | arXiv:1010.5727 | MATCH |
| L2 | Shimura, "The special values of the zeta functions associated with Hilbert modular forms", Duke Math. J. (1978) | doi:10.1215/S0012-7094-78-04529-5 | MATCH |
| L3 | Bruinier, van der Geer, Harder, Zagier, "The 1-2-3 of Modular Forms" (Springer 2008; incl. Bruinier's Hilbert modular forms chapter) | doi:10.1007/978-3-540-74119-0 | MATCH |
| L4 | Atkin, Lehner, "Hecke operators on Γ0(m)", Math. Ann. (1970) | doi:10.1007/BF01359701 | MATCH |
| L5 | Zwegers, "Mock Theta Functions" (thesis) | arXiv:0807.4834 | MATCH |
| L6 | Bruinier, Funke, "On two geometric theta lifts" | arXiv:math/0212286; doi:10.1215/S0012-7094-04-12513-8 | MATCH (both) |
| L7 | Bruinier, Ono, Rhoades, "Differential operators for harmonic weak Maass forms and the vanishing of Hecke eigenvalues" | arXiv:0802.0963 | MATCH |
| L8 | Bringmann, Ono, "The f(q) mock theta function conjecture and partition ranks", Invent. Math. (2006) | doi:10.1007/s00222-005-0493-5 | MATCH |
| X1 | arXiv:0712.0574 (decoy ID) | — | MISMATCH: resolves to Meerschaert–Nane–Xiao, large deviations / fBm. Not BOR. Excluded. |
| X2 | Zagier, "Quantum modular forms" (Clay Math. Proc. 11, 2010) | no arXiv/DOI resolved this run | NOT LIVE-CHECKED → excluded from PRESENT/PARTIAL |
| X3 | Eichler/Shimura/Knopp period-cocycle originals | no ID live-resolved this run | NOT LIVE-CHECKED → excluded |
| X4 | LMFDB Hilbert MF page for field 2.2.140.1 | URL tried returned "Page Not Found" | NOT LIVE-CHECKED |

## Ranked results by hunt item
1. Hecke setup over Q(√35): PARTIAL — L1, L2, L3 give the general Hilbert modular framework over real quadratic/totally real fields. No live-checked source specific to Q(√35) (disc 140) found → specific-field reference ABSENT.
2. Right T_𝔭 space (parallel weight, Γ0(𝔫), Hecke at primes of O_K): PRESENT (definitional) — L1 (Hecke operators T_𝔭 on Hilbert modular forms of level 𝔫, explicit algorithms), L3 (Bruinier chapter). L2 background (PARTIAL). L4 = elliptic Γ0(N)/Fricke/Atkin–Lehner analogue, PARTIAL.
3. "Hecke deformation" T_p·exp(Θ) or T_p+εΘ: ABSENT. No source found defining Hecke operators deforming an exponential of a theta form or a linear T_p+εΘ deformation. Nearest framework (PARTIAL only): L7 (Hecke action interacting with ξ/D operators on harmonic Maass forms), L6 (theta lifts).
4. Computable candidate C (residual/polar coefficient): PARTIAL — L5 (explicit completions/shadow formulas for mock theta functions, Mordell integrals), L8 (exact Fourier coefficient formulas for mock theta f(q) via harmonic Maass/Poincaré series), L7 (principal/polar parts and ξ-operators), L6 (Fourier expansion of lifts). These give computable coefficient/polar-part formulas for standard objects only. No published object matching project "C" with Fricke-transfer residual on Q(√35) → as-asked: ABSENT.

## GAP (project jargon, not published terms)
"transfer element C", "Bridge Series C", "residual_slash", "V₃₅" — no published usage; GAP. Not in Cat A PRESENT.

## Status-only
Prior Exact-ν/Fricke/Path-A (507caaf1…) status-only; not reopened. Kerr unlock not relied on. Video EXCLUDED. invent-pending (status only) for any C construction.

## Conclusion for Physicist/PP
Item1 PARTIAL (field-specific ABSENT); Item2 PRESENT; Item3 ABSENT; Item4 PARTIAL framework / ABSENT as asked. Counts: PRESENT 1, PARTIAL 2, ABSENT 1. Mismatch: arXiv:0712.0574 ≠ BOR (correct 0802.0963). No CERT. No RECS.
