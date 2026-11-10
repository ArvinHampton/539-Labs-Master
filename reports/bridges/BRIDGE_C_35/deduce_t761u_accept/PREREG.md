# deduce_t761u_accept — PREREG (2026-10-25, America/Chicago)
Authority: Arvin t761u ACCEPT **AW-α** (all recommended): AW-1a-0 + AW-2a + AW-3a + AW-4a of AUTHOR-WRITTEN Ξ defs menu sha cbb884a4f6c01d4c9b2dceebb2b47a2dd5ff201e245c6253ae3dd71df9162402. NOT AW-β/γ/δ; NOT AW-X4 (G-2 unresolved).
Pattern: mirrors deduce_t756u_accept (T-α KEEP) / deduce_t748u_accept (B3-α KEEP).
Cite: Auditor CONFIRM face665ba803e36eb57d060cae64ad7f103b26fd171470d3d63713c5df186707; menu cbb884a4…; RESULTS d39c86fb938f5304b4ad254ee2a552d753be474d930f8f5ba0871b19bc57ddf7.

## Scope (verbatim ACCEPT)
AW-α ACCEPT all recommended from menu cbb884a4…:
- AW-1a-0: χ_even(k)=1 iff k≥0 and k≡0 mod 2; χ_odd(k)=1 iff k≥0 and k≡1 mod 2; INCLUDE k=0 (χ_even(0)=1).
- AW-2a: ϑ_even=ϑ_odd=ϑ(q;z):=Σ_{j≥0}(j+z)q^{(j+z)²} (HD L24 plain form).
- AW-3a: n is ϑ-offset; locked specialization n=1.
- AW-4a: N_trunc=106.
NOT accepted: AW-β/γ/δ; AW-X4 (G-2 sign unresolved — ledger q^{-outer} vs HD q^{+outer}). Soft SF if anyone treats ledger Ξ ≡ HD Ξ as Cat A from this ACCEPT.

## Methods
M1 live-verify shas: Auditor CONFIRM face665b…; menu cbb884a4…; t761u_xi_written RESULTS d39c86fb… / PREREG ab192b9f… / SUMS 181eedbd… (+ sha256sum -c rc=0); MASTER inventory 544de792…; baselines B3-α KEEP CONFIRM b96ff7bd…, T-α KEEP CONFIRM 5f5f2832…, ledger Ξ 7dbd63af5afbdf61…, X4 ABSENT 2bb870b4…. Any critical (1–6) mismatch ⇒ ABORT, no Cat A claim.
M2 PIN: Ξ defs (χ, ϑ, n, N_trunc) CLOSED under AW-α as ACCEPT-sourced Cat A AUTHOR-ACCEPT Written, scoped to Ξ defs only. No coefficient table numbers (schema stays empty).
M3 Unlock path NOTED, not executed: Ξ ledger computable → R-PKG1 Ξ input defined; X4 reduces to (ii)/G-2; G-A3 reopen path (#5) possible via non-rejected route — G-A3 stays PAUSED until Arvin explicitly reopens.
M4 confirm δ≡0 / Bridge YES / residual-C NOT newly forced; AW-X4 / ledger≡HD NOT claimed.
M5 append STREAM LOCK to STREAM_IDLE_LOCAL.md (after t761u_xi_written LOCK; hygiene not rewritten).

## Force criteria (pre-stated)
- F-A: any critical basis sha mismatch ⇒ ABORT.
- F-B: Ξ defs CLOSED under AW-α iff F-A passes and ACCEPT covers AW-1a-0/2a/3a/4a verbatim.
- F-C: δ≡0 / Bridge YES newly forced? Expected NO.
- F-D: residual-C closes? Expected OPEN (G-A3 PAUSED, X4 ABSENT, R-C1).
- F-E: AW-X4 / ledger≡HD Cat A? Expected NO (G-2 unresolved).
Constraints: CORE_FREEZE (except this author supply); SF-W7-3; Residual-vs-Resonant; invent-ban for numerics; no nonlocal EH11D; no order78; no AW-X4; no auto G-A3 reopen; REJECTED fill 4da09dec… not revived; B3-α KEEP + T-α KEEP stand; R-C1 stands; Bridge PARTIAL; READY NO.
