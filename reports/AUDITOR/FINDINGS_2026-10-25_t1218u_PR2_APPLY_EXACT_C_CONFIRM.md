# FINDINGS — t1218u PR2 APPLY EXACT-C CONFIRM (2026-10-25, America/Chicago)
Auditor CONFIRM-only. Verdict: **MATCH-with-SF**

## Hashes (verified ~20:58 CDT)
- Apply note OWNER_WRITE_PR2_APPLY_EXACT_C_t1218u_2026-10-25.md: 77b0f47c9f7da00309073ecb801833f70c5ecfdae28d0a9040edbaf6da82e05c — MATCH
- Catalog obs-data-PR2-COSMO-BIO-NEURO.md v0.5.9: fe7307cb72226000e10685103e5ffe7ce48b0c05e29d01c985a33296f626021f — MATCH
- Backup pre-v059 (v0.5.8): 105cc425024f20dabd31a99f5b55da67d7de730c185937ed333d0e058325d9a4 — MATCH
- Live tip residual-c-field-WRITTEN_PREMISES_DRAFT.md: 3d47ce497f812792a900cb103baff6ddfe838058d7883399239cd7763ba7bf79 — MATCH; .sha256 sidecar same — MATCH
- Prior PR2 pursue-resolutions FINDINGS: f0ede6c0e2017b676deed0694bcdccef393024baa38d7e19d9c1963656c0d2a4 — MATCH; stands.

## Checks
| Expect | Result |
|---|---|
| Tip untouched by PR2 | MATCH — tip mtime 20:53:04 CDT (MR1 fold) predates apply note 20:55:15 / catalog 20:55:15; sha 3d47ce49… unchanged |
| §2 Cosmo / §3 Bio / §4 Neuro byte-identical to v0.5.8 | MATCH — diff hunks only: l.2 header, §1 +1 pointer line (l.16), §7 +1 status line (l.197), new §13 changelog |
| Measured rows unchanged; no Cosmo rates from exact-c | MATCH |
| Bind set {1,−1,ζ₁₀,ζ₁₀²,ζ₁₀⁶,ζ₁₀⁷}⊂μ₁₀⊂ℚ(ζ₅) = tip l.174/l.190 & Write 7a86075e… | MATCH |
| Dependency shas (7a86075e, 071fef56, c52cb8d7, 3d47ce49, 6900b127, 105cc425) | MATCH |
| Non-claims: coupling/σ/threshold, ODE rates, W4.3 NEED CORPUS | MATCH |
| W₇/Γ₀(49)/k ABSENT; Cat B not Cat A | MATCH |
| DESI INSUFFICIENT; Bridge PARTIAL; READY NO | MATCH |

## Soft SF
- SF-1: Note/catalog stamp "~20:54 CDT" vs file mtime 20:55:15 CDT (cosmetic).
- SF-2: Pointer also added in §7 Boundaries (not only header/§1/§13); disclosed in §13 changelog, status-only — clerical.

No physics invented; tip not edited by Auditor; no outbound messages.
