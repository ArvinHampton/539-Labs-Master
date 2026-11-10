# FINDINGS — Auditor Residual-vs-Resonant CONFIRM — deduce_t713u_ga3_fill (2026-10-25)
Package: BRIDGE_C_35/deduce_t713u_ga3_fill/. Authority cited: t712s4471 (G-A3-only compute, schema 8d247feb…, class C); t713s4484 (ψ = psi-Cocycle ψ, partial accept); t713s4497 (defaults P1–P7 accepted: path i∞→x, principal branch, Ξ product-form N_trunc=106, ledger HOLD, col2=index/unit coeffs, Θ leading factor 1).
Executor FINDINGS_DRAFT c9c344e6… is NOT authoritative; this file is the Auditor record.

## Hashes (recomputed by Auditor)
| Artifact | sha256 | Verdict |
|---|---|---|
| PREREG.md | 49bd0b24fa2bd488a25d93293b47ec02d114b8c1d77d3bf7973234a8119e425b | MATCH (= PREREG.sha256) |
| RESULTS.md | c47552063ec7ae6fd3f875e0fecd51683505b64a1414ec6233aeb6fcd7df4398 | MATCH |
| SHA256SUMS (pkg) | 55e6d0a974724176dee68f862a6ec91822008feedf2ce8332438d083c4691973 | MATCH; -c 12/12 OK |
| Filled table | 4da09dec14b6881583bfd685e1c44eb3563bd649f25d05e6f8e91cd618e49d39 | MATCH |
| data/Xi_regen_N106.tsv | 35b186f9df70c2bf247432edcef946e5f66f0ddf1bbca2f4454a30b210707197 | MATCH |
| BRIDGE_C_35/STREAM_IDLE_LOCAL.md | eb065af81b0cf5a37145bec9914ff42656c311ea9e69dfc692153cae10736948 | MATCH |
| BRIDGE_C_35/inventory_check/SHA256SUMS | 1f8c570419fafc34decd5dd95d1c63732f9da73e24b43f6da0c4f13016e19c10 | MATCH; -c 73/73 OK |
| Schema v2 (deduce_t708u_ga3) | 8d247feb4f1b644dfbaf1d28237eaddfe9ba45c82d40464a2290d4721b0f8051 | UNALTERED |
| Executor draft | c9c344e6700d4a3ec2bd84a57af17d2aaa397ae21389caa5e9509715ab98d0e0 | MATCH (non-authoritative) |
Path note: inventory_check lives at BRIDGE_C_35/ root, not inside the package (claim path ambiguous; hash matches).

## Checks
1–2. All hashes MATCH; pkg SUMS OK; inventory 73/73 OK.
3. PREREG hashed before RESULTS: PREREG.sha256 present; RESULTS cites PREREG hash; mtime PREREG 10:47:26 < RESULTS 10:48:37 CDT. OK.
4. Scoping/provenance: PREREG cites t712s4471, t713s4484, t713s4497; P1–P7 all present; ledger Ξ 7dbd63af… stated NOT used (PREREG P4, RESULTS F0, table provenance). OK.
5. F1 FAIL (|δ| 62.97/7.08/5.56/35.14 ≫ tol); F2 δ≡0 NOT forced; F3 PASS (defect O(10), uncontrolled, N-sensitive). Reported as RESULTS states; labels honest — not altered.
6. Soft notes documented in RESULTS/table: partials 43/58/67 not reproduced (V-P variant), Written 78:6 absent from product form, no convergent tail bound (Ξ non-convergent on ℝ; N=150 shifts h O(1)), slash coeffs 4-dec. Documented; no integrity/ACCEPT-cite/Cat-A misuse ⇒ not escalated.
7. Filled table header + every row: "AUTHOR-CANDIDATE … class C … NOT Cat A until Arvin ACCEPT". OK.
8. Schema 8d247feb… unaltered; filled table is separate candidate file. OK.
9. Baselines stand: selectors 437d4571…; G-A1b CLOSED b34aebe6…; G-A3 schema draft 62283038…; NL 29ebbdd8… untouched.
10. BLOCKED compute CONFIRM 16350947… (t712u) SUPERSEDED by this CONFIRM for the G-A3 compute line.
11. Bridge PARTIAL; READY NO; residual-C OPEN; Bridge YES / δ≡0 / residual-C newly forced: NO/NO/NO.
12. CORE_FREEZE holds; SF-W7-3 stands; no order78.
13. No Cat A claim on filled values ⇒ no soft SF.

## Soft SF
NONE.

## Verdict
CONFIRM. G-A3 FILLED (class C, NOT Cat A until Arvin ACCEPT). F1 FAIL / F2 not forced / F3 PASS (uncontrolled).
