# deduce_t761u_path_psi_accept — PREREG (2026-10-25, America/Chicago)
Authority (verbatim): Arvin ACCEPT **PB-α** (all recommended): P-β (path i∞→x) + BR-α (principal Arg∈(−π,π]) + ψ-α KEEP (psi-Cocycle). NOT PB-β/γ/δ/ε.
Pattern: mirrors deduce_t761u_outer_accept (O-α).
Cite: Written menu 9af6bdcef231fff63b2e0f4f5fa9e9f4dc11730dec6ed56192b3aa02aeae7333 / RESULTS 4c062296c9f209cf32f05b161ceb97e814315db5040dbd9fc58278a90f9e945d / PREREG 411c16b6a0c5d4859d6ad62722578d885a264a45a37e2184795a02efe66003f0 / FINDINGS c64db3a4ecbd69704fdc5173707397aa23f6a77480b0c5499cc2e5ffee144f7a / SUMS f6efb32f4a6b6fb721dfe6464bfd7bd3f48139ba7cc7b7e029b9404a3577daf6; Written Auditor CONFIRM MATCH soft SF-1 94ac4072b1dfa4e74087036813d62b83a979447fd94886503bc06eb7f5847391; O-α MATCH b467bb54b7d759416cf9898ba806926758f01efb7fe8c0624edf13458d35a5f0; AW-α MATCH aac04151accb03b0464ffaf2fff09b733af99b820a97479f262a6d82f60b13d1.

## Scope (verbatim ACCEPT, PB-α only)
- P-β: ACCEPT path = i∞→x (1bab65c4 L32 Written). NOT P-α/γ/δ (0→i∞ b329c67c L21 / 552541cf L46 / 22959c01 L57 not adopted).
- BR-α: ACCEPT principal Arg∈(−π,π]; (w−x)^{−1/2} principal. Soft SF flag: ACCEPT-default from t713s4497 / t713u PREREG 49bd0b24… P3, NOT Written HD (HD branch unspecified).
- ψ-α: KEEP ψ ≡ psi-Cocycle (t713s4484 ACCEPT stands; 1be7f7d1…).
NOT accepted: PB-β/γ/δ/ε. No G-A3 reopen; 4da09dec… not revived; no numeric h/δ; δ≡0/Bridge YES not forced.

## Methods
M1 live-verify: Written CONFIRM 94ac4072…; O-α b467bb54…; AW-α aac04151…; Written menu/RESULTS/PREREG/FINDINGS/SUMS; MASTER 544de792…; B3-α b96ff7bd…; T-α 5f5f2832…; X4 ABSENT 2bb870b4…; HD 1bab65c4…; b329c67c/552541cf/22959c01(6d0a7777…); t713u PREREG 49bd0b24…; psi-Cocycle 1be7f7d1…; sha256sum -c on path_psi_written + outer_accept SUMS. Critical mismatch ⇒ ABORT, no Cat A.
M1b hygiene: soft SF-1 (Written log b329c67c L21/L16 mis-extraction) fixed in THIS package via logs/written_lines_corrected.txt re-extracted from real b329c67c file; Written package NOT edited.
M2 PIN: path/branch/ψ CLOSED under PB-α as ACCEPT-sourced Cat A AUTHOR-ACCEPT Written, path/branch/ψ only.
M3 confirm branch NOT labelled Written HD; G-A3 stays PAUSED; 4da09dec… not revived; no ledger≡HD Cat A.
M4 confirm δ≡0 / Bridge YES / residual-C NOT newly forced.
M5 append STREAM LOCK (after path_psi_written LOCK; hygiene #9 not rewritten).

## Force criteria (pre-stated)
- F-A: critical basis sha mismatch ⇒ ABORT.
- F-B: path/branch/ψ CLOSED under PB-α iff F-A passes and ACCEPT covers P-β+BR-α+ψ-α verbatim.
- F-C: δ≡0 / Bridge YES newly forced? Expected NO.
- F-D: residual-C closes? Expected OPEN (G-A3 PAUSED, X4 ABSENT, R-C1).
- F-E: branch treated as Written HD / G-A3 reopen / 4da09dec revived? Expected NO.
Soft SF if: branch default treated as Written HD; 4da09dec… revived; G-A3 auto-reopened; any silent Cat A beyond PB-α path/branch/ψ; numeric h/δ introduced; ledger≡HD as Cat A.
Constraints: CORE_FREEZE (except author supply); SF-W7-3; Residual-vs-Resonant; invent-ban; no nonlocal EH11D; no order78; AW-α + O-α stand; B3-α KEEP + T-α KEEP stand; G-A3 PAUSED; R-C1 stands; Bridge PARTIAL; READY NO; NOT AW-X4/O-X4.
