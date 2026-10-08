# Eigenvalue & matrix work in the Grok project "Quantum Comp": search report

Generated 2026-10-08 (CT) from the read-only archive `/workspace/quantum-comp/grok-chats/`. No existing file was modified; every output is in this folder.
Chat URL pattern: `https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=<id>`. Quotes are verbatim, cited as `file:line` (paths are relative to `grok-chats/` unless shown otherwise). Numbers are quoted as written. Every verdict comes from `checks/` and is never written over a quote.

Outputs:
- `REPORT.md`: this report.
- `hits.tsv`: classified hits. Columns: chat_id, title, file, line, term, class (CORE / RELATED / FP / OTHER), theme, snippet.
- `hits_raw.tsv`: 1,931 unclassified wide-regex hits.
- `scan.py`, `classify.py`: the scanner and the rule classifier.
- `uncaptured_candidates.tsv`: strong and possible chats with no full text, with URLs.
- `build_candidates.py`: builds the candidates list.
- `checks/numeric_checks.py` → `checks/numeric_checks.json`: 48 checks.
- `checks/kplus_laplacian.py` → `checks/kplus_results.json`: rebuilds the K⁺ Laplacian over 30 gap orders.

## (a) Coverage

| Item | Count |
|---|---|
| Chats in the project (`all-chats.tsv`) | **621** |
| Chats with full verbatim text (`raw/chat-01..13.txt`) | **13** |
| … with any regex hit | 10 |
| … with real (non-false-positive) eigen/matrix content | 8 (01, 02, 05, 06, 07, 09, 11, 13) |
| … with CORE content | 6 (01 17 Theorems, 02 Pure Math Status, 05 Discrete Focus, 06 Nuclear Decay/CKM, 09 Architecture A, 11 Ramanujan/K3) |
| … false positives only | 03 (spectral *sequence* only), 10 (RH "gates") |
| … no hits | 04, 08, 12 |
| Extract-only chats (partial, analyst-written extracts in `extracts/`, `extracts/bounce/`) | 33 files; 32 have chat content, and 1 (a396b451 Bott Periodicity) is an "access blocked" stub |
| … with any hit | 24; 19 non-false-positive; 9 CORE (0ed64ceb, 374f8b17, 3dfb5604, 50df7219, 60bd2c1e, 931fd19f, 9357ac89, a0554ad6, ea74f77f) |
| Chats with **no full text** | **608** (621 − 13) |
| Chats with **no saved text at all** | **576** (608 − 32 with extracts; the Bott stub counts as no text) |
| Raw hits (wide regex) | 1,931: CORE 483, RELATED 696, false positive 722, OTHER (spectral sequence) 30 |

Broader `/workspace/quantum-comp` check (`datasets/`, 2.8 GB of non-chat data, was excluded):
- `reports/heavy-daily/` (1,058 files) holds summaries and outputs of later Grok Heavy chats in the same project. Their 25 chat ids, for example 615919d3 "S2-11DM2ET-X Hubble Resolution", 904fa40b, 292c1971, 11844219, 8f85c185 and 791c429e, are **not** in `all-chats.tsv`. They are reported separately in §(b)-F.
- `theorems/unification-proof.txt` is a paper ("Mathematical Proof of Unification", 3 Feb 2026), not a chat. Its matrices are checked in §(c)-G.
- `maths/theorem-lemma-chain-9-maths.txt` is a paper.
- `prompt.txt` holds the freeze. Line 7 keeps |V_us| = 1/φ², and line 10 lists the retractions.
- `reports/conflict-brief-for-grok.md` contains no other chat text.
- Data note: the extract file `extracts/a396b451-…md` uses an id that does not match the TSV id `a396e451-81f4-46bc-9365-818e8e86ef92` ("Bott Periodicity in HQCC Theorem"). The rest of the UUID matches, so this is probably a typo.

Classifier caveat: `class`/`theme` in hits.tsv come from rules and are meant for triage only. Each finding below was read in context.

## (b) Findings by theme

### B-1 Hamiltonians and quantum states

**The 17 Theorems of Entanglement**, ef92a5c4-6ea7-403c-8899-e037bcbfd197, https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=ef92a5c4-6ea7-403c-8899-e037bcbfd197. File `raw/chat-01.txt`; the attached paper source is `extracts/bounce/src-17-theorems-v5.txt`.
- Two-level leakage Hamiltonian:
  - 3434 "H₀ = E₊ |+⟩⟨+| + E₋ |−⟩⟨−|."
  - 3436 "H = H₀ + V(t) (|−⟩⟨+| + |+⟩⟨−|)."
  - 3437 "Diagonalizing the instantaneous Hamiltonian yields the adiabatic eigenvalues"
  - 3438 "E_±(t) ≈ (E₊ + E₋)/2 ± √[(E₊ − E₋)²/4 + V(t)²]."
  - 3440 "ΔE(t) ≈ V(t)² / |E₊ − E₋|."
  - 3442: ΔE_peak "≈ 0.619 meV"
  - 3448: τ_settle "≈ 22.5 attoseconds"
- 1913 "The effective ΔE is the eigenvalue difference between the forward (+U) and reversed (-U) projections, fixed at ΔE = 0.6 meV".
- 1921 "τ_settle = ħ / E_bind ≈ (6.582 × 10^{-16} eV·s) / (29.3 × 10^{-3} eV) ≈ 22.5 attoseconds". The 22.5 as figure is repeated at 1952, 2222, 2343, 2387, 2505 and 2679.
- Density matrices:
  - 1212: the global density matrix ρ_{+U⊕−U} "remains pure" after tracing out −U.
  - 2174: ρ_{12} ∝ exp(−(Δx/L_coh)²).
  - 3862 "ρ(Δx) = (1/2) \begin{pmatrix} 1 & e^{i Δφ(Δx)} \ e^{-i Δφ(Δx)} & 1 \end{pmatrix}"
  - 3866: V = |⟨σ_y⟩| = |exp[iδΔφ]| = exp[−(δΔφ)²/2].
- Pauli operators: 3988 "H_leak = ΔE(t) (σ_z^A − σ_z^B) / 2" (also at 4594 and 4640).
- Tubulin many-body Hamiltonian and open-system dynamics:
  - 6112 "H₀ = ∑{j=1}^N ε_j σ_z^j / 2 + ∑{j<k} J_{jk} σ_x^j σ_x^k / 2 + Ω ∑_{j} σ_x^j cos(ω_drive t)"
  - 6133: Born–Markov equation
  - 6192: H_mf
  - 6198–6202: Lindblad equation
  - 6203: "enhanced by √N"
  - 6323: H_S
  - Rates and T₂ at 6141–6149, 6172–6173 and 6218–6224 (checked in §c, A9–A12).
- Other items:
  - 247–257: Legendre transform ℋ = πq̇ − ℒ (standard).
  - 6498–6523: breathing-mode trace h(t) = −3h₀ sin(2πt/G₄) (convention only; not checked).
  - 2086/2129: "torsion operator" T_{539.9} = d + (e^{2πit/539.9} − 1) ∧ H_3.

Pasted-paper context (bounce extracts; qualitative):
- 3dfb5604 "Black Hole Singularity Quantum Resolution" (`extracts/bounce/3dfb5604-bh-singularity-quantum.md:19`) quotes the Gielen–Menéndez-Pidal paper: "Hamiltonian constraint C = π_k²/v² − π_v² + Λ ≈ 0", "self-adjoint extensions/boundary condition at v→0", and unitarity in unimodular time.
- 60bd2c1e (`extracts/bounce/60bd2c1e-betapbh-018.md:20`): "self-adjoint friction operator F_friction(t) with the exact coefficient 1000/539.9". No operator is exhibited.

### B-2 Qutrit and gate matrices
- No explicit qutrit gate matrix (3×3 unitary, Gell-Mann, clock/shift) appears in any saved chat text.
- Most "gate" hits are RH "zero-closure gates" in chat-05 and chat-10 (false positives).
- Closest items:
  - chat-01:4422 and 7356–7358: Cayley graph of ℤ₃*ℤ₂ and the "1001-simplex Cayley graph", "Exhaustive enumeration … 539 ± 1". This cannot be checked because no graph data is given.
  - **HQCC Theorem: Three-Generation Quark Masses**, a0554ad6-ff4b-43da-8381-0740173ec20e (extract only), https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=a0554ad6-ff4b-43da-8381-0740173ec20e
    - `extracts/a0554ad6-…md:5`: "Ternary Puncture + Cayley eigenvalue lemma"
    - `:25`: "A_21 adjacency matrix is never actually written out; no characteristic polynomial ever produced despite three requests."
  - a7a64802 "539-step embedding formalization" (`extracts/a7a64802-…md:18`): "constructive A₅/A₆ families from ternary-matrix templates" (pointer only).
- Strong uncaptured candidates for this theme are listed in §d: 457be4a1, 9c94142d, f429b85e, 02c01a2c, 6f1b4ead.

### B-3 Map and transition matrices (T3/HQCC) and the residual K⁺ complex

**Pure Math Status: 2026-08-12**, f363bbe6-b63f-4f70-ab21-9e314418f278, https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=f363bbe6-b63f-4f70-ab21-9e314418f278 (`raw/chat-02.txt`). This is the main eigenvalue computation in the archive.
- 1301–1303: "539 vertices (residual quanta under Principle (S))"; "594 edges: path edges plus same-tower complete edges"; "Fiber size distribution: 1 singleton, 185 doubletons, 56 tripletons"
- 1309–1311, three weight schemes:
  - "Unweighted — every edge weight 1"
  - "Tower-size weights — path edges weight 1; same-tower edges weight equal to fiber size (2 or 3)"
  - "Path-decay + tower boost — path-like edges weight 1/(1 + √|i−j|); same-tower edges weight 2"
- 1315, spectrum table: "Unweighted≈ 3.9×10⁻⁵≈ 4.53≈ 2.201 Tower-size≈ 5.3×10⁻⁵≈ 10.15≈ 4.141 Path-decay + tower≈ 2.1×10⁻⁵≈ 5.06≈ 1.411" (columns: gap, max, mean, mult. of 0)
- 1318–1321: "N(0.1) ≈ 53" "N(1) ≈ 162" "N(2) ≈ 242" "N(5) = 539 (saturated)"
- 1349 "Tr(e^{−t L}) = ∑_{i=1}^{539} exp(−t λ_i),"
- 1353: heat-trace table (t = 0.001 … 100)
- 1360 "Tr(e^{−t L}) = n − c₁ t + (c₂/2) t² − ⋯"
- 1362 "c₁ = Tr(L) c₂ = Tr(L²) Unweighted 1188 3896 Tower-size 2230 15808 Path-decay + tower 762 2148.5"
- 1363 "For the unweighted scheme, Tr(L) = 2E = 1188 exactly, matching the edge count 594."
- 1339–1342: normalised Laplacian, adjacency and weighted cohomology are listed as open extensions.

**Physics Unification Model: Discrete Focus**, c7fa7ae8-4e69-4150-a11d-c9a639bb4e88, https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=c7fa7ae8-4e69-4150-a11d-c9a639bb4e88 (`raw/chat-05.txt`)
- 981 "If we have a Hamiltonian path on 539 verts: edges_path = 538, triples = 537 — not 56"
- 985 "Jump edges: n_jump = 241, M = 36 * 241 = 8676"
- 991 "Incidence spectrum eigs: {2: 56, -1: 297, 1: 185, 0: 1}"
- 994 "Gaps on P+ triples: {5:6, 7:25, 9:24} — sum 6+25+24 = 55? or 56?"
- 4456 "Definition 1.3 (Transfer operator Ψ)"
- 4844 "Transfer Ψ. There is a residual transfer on squares such that total jump-mass equals (M=36\cdot n_{\mathrm{jump}}=8676=\Sigma_{G\text{-}F}), supported only on jump edges, orthogonal to stay-triple faces."

**T3 Map Free Orbit vs HQCC Resonant Theorem**, 295c374d-4923-4139-8dee-0a30f97f35b1, https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=295c374d-4923-4139-8dee-0a30f97f35b1 (`raw/chat-13.txt`)
- 29: "enrichment to K⁺ (V = 539, E = 594, F = 56, β0 = 1, β1 = 0, β2 = 0 over F2)"
- 43 "“The average Lyapunov argument does not prove exact termination length.”"
- 74–76 "Second mismatch – the printed Lyapunov number" … "The actual numerical value is ln(3)/539 ≈ 0.002038."

Lyapunov and stationary-measure items:
- chat-01:8525 (Public Grok, quoted in the chat): "The average absolute multiplier of the written map evaluates to 2/3, so the Lyapunov exponent evaluates to ln(2/3) ≈ –0.405". Depths are at 8518–8521.
- 1e7fe572 "HQCC Theorem Derives 539.9s Period", https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=1e7fe572-7afd-4d54-b7f0-aa3590b9aaaa, `extracts/1e7fe572-…md:9`: "𝔼_π[χ] = (2/3)ln(1/3) + (1/3)ln(4/3) = ln(4^{1/3}/3) ≈ −0.6365 < 0". Line 49 notes that the measure π is assumed and 3-adic equidistribution is unproven.
- 3da1f6d2 "Hampton Qutrit Collatz Theorem Proven", `extracts/3da1f6d2-…md:8`: "λ = −ln(27)/9 = −ln3/3 ≈ −0.4054651"
- eff2fe0b "Qutrit Collatz Map Termination Proof", `extracts/eff2fe0b-…md:22`: "Lyapunov L(n,g) = 539 − k". Line 42 says this is circular.
- 0ed64ceb "Ternary Map and Collatz Convergence Analysis", `extracts/0ed64ceb-…md:87`: the extract authors ask whether T3 induces a map on ℤ/9, i.e. a 9-state transfer matrix (check C6).
- Banach λ = ln3/539 is used as a contraction in a7a64802:12, 60de8d96:11 and 1e7fe572:14. It is **RETRACTED** in the freeze.

### B-4 Mixing matrices (CKM/PMNS) and mass spectra

**Nuclear Decay Types and Effects**, 6764f8a8-b6be-4e9a-bc6e-0dded1248c84, https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=6764f8a8-b6be-4e9a-bc6e-0dded1248c84 (`raw/chat-06.txt`)
- 84 "δ_CKM from arg(-V_{ud} V_{ub}^* / (V_{td} V_{tb}^*))"
- 86 "Textures (e.g., three-zero quark mass matrices) or Froggatt-Nielsen suppress off-diagonals"
- 102 and 115: J ≈ 3×10⁻⁵
- 113 "J = (m_t^2 - m_c^2)(m_c^2 - m_u^2)(m_t^2 - m_u^2) \sin \delta_{\text{CKM}} … / (12 m_W^6) J≈3×10^{-5} enhanced"
- Lines 80–125 also contain Tr(G G̃) and Tr(W W̃) topological terms, and ε_K via Im(V_td V_ts*).

**Ramanujan Mock Theta and K3 Unification**, 12a732e3-54f0-428f-ad29-c99487233847, https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=12a732e3-54f0-428f-ad29-c99487233847 (`raw/chat-11.txt`)
- 11: "The six physical quark masses are recovered as exact algebraic integers that satisfy the 7021 identity; these arise as eigenvalues of the discrete Frobenius warp / trace operators acting on the 5084-tower budget."
- 12: "Every CKM matrix element and entanglement invariant is stated to close to machine precision under the same arithmetic rigidity."
- No matrix is exhibited.

**9 Maths of Unification: Arvin Hampton's Closed Corpus**, 931fd19f-6cb5-4e0a-816e-63b4f10b69ba (extract), https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=931fd19f-6cb5-4e0a-816e-63b4f10b69ba
- :39 "trace = 178767.10 MeV "(exact 7021 identity)""
- :40 ""discrete Frobenius warp operator of order 539.9""
- :41 "Cabibbo 13.02° via SVD on partitioned up/down sectors"

**New 9 maths unification**, ea74f77f-3556-4062-9943-98b413a95001 (extract), https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=ea74f77f-3556-4062-9943-98b413a95001
- :67 "F_weak(t) = Tr[V_CKM† (g_11 Φψ + T_M2 M2(t)) V_CKM]"
- :49–50: "Vibrational Frobenius endomorphism Φ_11 of order 539.9"
- Cabibbo is 13.03° here vs 13.02° in 931fd19f.

Also:
- 60de8d96 "T3 Variant HQH-539 Model Implications", :15: "exactly six real units of norm 539.9 MeV survive in the T_{4121}-twisted ring".
- Freeze (`prompt.txt:7`): kept "|V_us|=1/φ²". Retracted (`prompt.txt:10`): |V_cb| 0.146.

### B-5 Spectral and trace work on zeta

**Pure Math Status** (f363bbe6, URL above), `raw/chat-02.txt`
- 613: "TMR phase condition cos((k_1-k_2)d-θ) as a candidate eigenvalue constraint on the phase operators."
- 799: "Construct mode operators H_{±} whose eigenvalue counting functions on each sector satisfy a Weyl law…"
- 927: "Classically one seeks a self-adjoint operator whose spectrum is exactly {γ_n}. A dual Weyl law is the weaker asymptotic statement that the eigenvalue counting function of the dual operators matches N(T) at leading order. Even a successful dual Weyl law would not by itself identify the spectrum with the zeros"
- 1060: "Zeta regularisation of the associated determinant produces terms involving log of the spectral parameter, but the resulting counting function for eigenvalues of −d²/dt² on a fixed-length interval is still linear in T (spacing π/L), not (T/2π) log(T/2π)."
- 1126: H± = −i d/dt + V±(t) with the IDS formula (check E6).
- 1213: "the mode spacing is 2π/G4 and the total linear density of states is of order 243/(2π) ≈ 38.7."
- 1331: "They cannot produce an unbounded counting function N(T) ∼ (T/2π) log(T/2π). The spectrum is finite of cardinality 539."
- Fredholm and zeta-regularised determinants are mentioned at 1021, 1040 and 1098 but never computed.

**Riemann Zeta Function Resonant Trace**, 374f8b17-ba93-464b-957a-d77412cc151b (extract only), https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=374f8b17-ba93-464b-957a-d77412cc151b
- :9 "Frobenius endomorphism Φ_11: ξ ↦ ξ^11, "order exactly 539.9"."
- :10 "Claim: ζ(s) = Mellin transform of trace over these modes"
- The resonant-trace integral, the unit ε = 331.3 with "log ε = 2π", and the "269 generators" are checked as E1–E3.

50df7219 "HQCC Theorem: Zero Non-Trivial Cycles" (extract), :12: "Resonant cyclotomic ring ℤ[ζ_539.9 + ζ_539.9^{-1}], "Frobenius of order 11"."

**Pure-Math Review: Architecture A Closed**, 1d909557-9613-424b-a74c-54be1db0ebd9, https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=1d909557-9613-424b-a74c-54be1db0ebd9
- `raw/chat-09.txt:335` "GUE+independence is heuristic only."
- The Selberg and Kronecker hits are false positives.

**Clay Problem AI**, cfd2aec3-eda0-420a-8953-4b817779ce2a, https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=cfd2aec3-eda0-420a-8953-4b817779ce2a
- `raw/chat-07.txt:425`: "Bombieri / Weil quadratic form ideas: on-line zeros ↔ positive-definite directions, off-line ↔ negative-definite; rank/moment comparison." (Literature pointer only.)

### B-6 Other
- 9357ac89 "7th…Resonant Temporal Torsion Cohomology", `extracts/9357ac89-…md:38`: "R_t = ℝ ⊗ det(T^*M)[T]" (determinant line bundle; notation only).
- chat-05:266: "−det g_ind" (induced-metric determinant in an action).
- chat-03 "Spiral Score": 6 hits, all "spectral sequence" (homological algebra; not eigen).
- Pasted-paper TT projector and kernel: 12faa925 "Inflation Without Inflaton Model" (`extracts/bounce/12faa925-…md:37`; qualitative).

### B-7 Outside the chat archive (not chats in all-chats.tsv; listed for completeness)
- `reports/heavy-daily/da927a09dac3-Matrix_Analogues_s5_s8_s11_Residues_Twin_Pairs_Pack_S_2026-08-26.md:10–41` (Grok Heavy output): lattice Gram "M_s = [[2, s], [s, s]] has determinant -s(s-2)", "Signature is (1,1)", plus the residue sets (F5–F13).
- `reports/heavy-daily/U1-GS-ZWEGERS-1d8e558.md:37`: "B_7 = [[1, 7/2],[7/2, 7/2]], det B_7 = −35/4" (F12).
- `reports/heavy-daily/DUAL_AND_RESIDUAL_GEOM_2026-08-17.md`: the same weighted K⁺ spectra as chat-02.
- Transfer operator L_φ and its secondary eigenvalues were requested but never written: `U1-E4-TRANSFER-69628dc.md` and `T3_TRANSFER_PRESSURE_NDUAL_2026-08-17.md`.
- The A_21 characteristic polynomial was never produced: `SQRT_ALL_MODEL_POLYNOMIALS_2026-08-18.md:197–206` and `POLYNOMIAL_ROOTS_TARGETS_2026-08-17.md:45`.
- `U1-E1-PERIOD-34729c9.md:30`: "Periods unavailable".
- Weil polynomials and the singular values 6.38/29.23 are stated without enough data to check.
- `theorems/unification-proof.txt` (a paper, not a chat):
  - 100–111: explicit 3×3 tridiagonal mass matrix
  - 115–122: sector eigenvalues
  - 124: "Koide relation emergent from ternary trace invariant det(M)/Tr(M)^3 ≈2/3"
  - 128: CKM = U_up†U_down
  - 138–142: |V_us|, |V_cb|, |V_ub|
  - 151–158: PMNS
  - Checked as G1–G4 and D3–D4.
- `maths/theorem-lemma-chain-9-maths.txt` (a paper): quark masses as eigenvalues of F539.9 (121, 872, 896, 931) and Lemma 4.2 CKM SVD (956–959).

## (c) Checked numeric claims
Verdicts:
- **HOLD**: the stated number or formula is reproduced.
- **FAIL**: it is not reproduced; the computed value is given.
- **QUALIFIED**: the number is right but the interpretation is wrong.
- **INFO**: a reference computation that does not test a claim.

Each row also notes whether `extracts/INGEST-PROTOCOL.md` / `prompt.txt` already marks the claim retracted. Full records are in `checks/numeric_checks.json`.

| ID | Source | Claim (verbatim/abridged) | Computed | Verdict | Retracted / flagged? | Note |
|---|---|---|---|---|---|---|
| B1 | raw/chat-05.txt:991-992 | Incidence spectrum eigs: {2: 56, -1: 297, 1: 185, 0: 1}; 56+297+185+1 = 539 = V | adjacency spectrum of disjoint fiber cliques (56 K3, 185 K2, 1 K1) = {2:56, -1:297, 1:185, 0:1}; see kplus_results.json | HOLD | No | computed in kplus_laplacian.py |
| B2 | raw/chat-13.txt:29 etc. | K⁺ (V = 539, E = 594, F = 56 ...) | Euler χ = 1; 594 = 538 path + 56 chords; n_jump = 241 recovered | HOLD | No |  |
| B3-unweighted | raw/chat-02.txt:1315 vs 1362 | mean eigenvalue ≈ 2.201 (unweighted); c₁ = Tr(L) = 1188 | Tr(L)/539 = 2.2041 | FAIL (minor, internal) | No | the mean of the 539 eigenvalues must equal Tr(L)/539 exactly; the table mean disagrees with the chat's own trace in the 3rd decimal |
| B3-tower-size | raw/chat-02.txt:1315 vs 1362 | mean eigenvalue ≈ 4.141 (tower-size); c₁ = Tr(L) = 2230 | Tr(L)/539 = 4.1373 | FAIL (minor, internal) | No | the mean of the 539 eigenvalues must equal Tr(L)/539 exactly; the table mean disagrees with the chat's own trace in the 3rd decimal |
| B3-path-decay | raw/chat-02.txt:1315 vs 1362 | mean eigenvalue ≈ 1.411 (path-decay); c₁ = Tr(L) = 762 | Tr(L)/539 = 1.4137 | FAIL (minor, internal) | No | the mean of the 539 eigenvalues must equal Tr(L)/539 exactly; the table mean disagrees with the chat's own trace in the 3rd decimal |
| B4 | raw/chat-02.txt:1315-1321, 1353, 1362 | spectral gaps 3.9e-5 / 5.3e-5 / 2.1e-5; max 4.53 / 10.15 / 5.06; N(0.1)≈53, N(1)≈162, N(2)≈242, N(5)=539; Tr L = 1188/2230/762; Tr L² = 3896/15808/2148.5; heat-trace table | reconstruction (path of 539 + 56 chords, 30 random gap orders): Tr L exact 1188/2230/762; Tr L² 3896 / 15806–15808 / 2148.5; gaps 4.03–4.08e-5 / 5.40–5.48e-5 / 2.15–2.19e-5; max 4.566–4.589 / 10.17–10.18 / 5.066; N(0.1)=51–52, N(1)=167–169, N(2)=242, N(5)=539; heat trace matches to ~0.04 for t≤2 and within ~0.1 for t=5–100 | HOLD (traces, N(2), N(5), mult0=1) / ≈HOLD order-dependent (gap, max, N(0.1), N(1)) | No | exact chord order is not recorded in the archive; small differences are within the spread of admissible orders |
| C1 | raw/chat-01.txt:8525 | The average absolute multiplier of the written map evaluates to 2/3, so the Lyapunov exponent evaluates to ln(2/3) ≈ –0.405 ... n = 10^18 ≈ 102 steps; n = 10^20 ≈ 114 steps | geometric mean of Canonical-T3 branch factors (1/3,4/3,2/3) = 2/3; ln(2/3) = -0.405465; ln(1e18)/0.405 = 102.3; ln(1e20)/0.405 = 113.7 | HOLD | No | holds as a GEOMETRIC mean; the arithmetic mean (1/3+4/3+2/3)/3 = 7/9 (conflict-brief A9) |
| C2 | extracts/1e7fe572...md (HQCC Theorem Derives 539.9s Period) | 𝔼_π[χ] = (2/3)ln(1/3) + (1/3)ln(4/3) = ln(4^{1/3}/3) ≈ −0.6365; λ_mean ≈ 0.529; N_⋆ = ⌈ln 4880/0.6365⌉ = 14 | -0.636514; ln(4^(1/3)/3) = -0.636514; e^E = 0.5291; ceil = 14 | HOLD | No | stationary distribution π = (2/3,1/3) over branches |
| C3 | extracts/3da1f6d2...md (Hampton Qutrit Collatz Theorem Proven) | λ = −ln(27)/9 = −ln3/3 ≈ −0.4054651 | −ln27/9 = -0.3662041 | FAIL | Flagged in extract/BATCH2 (not on freeze list) | already flagged in the extract / BATCH2-ROLLUP |
| C4 | raw/chat-13.txt:74-76 | The same proof text states λ = ln(3)/539 ≈ 0.99996. The actual numerical value is ln(3)/539 ≈ 0.002038. | ln3/539 = 0.002038; 1−ln3/539 = 0.99796 | HOLD (chat's correction) | Yes: Banach λ RETRACTED | Banach λ = ln3/539 is RETRACTED in INGEST-PROTOCOL.md / prompt.txt line 10 |
| C5 | raw/chat-01.txt:8518-8521 (Public Grok) | seed 10^19 reaches 1 in 96 steps; seed 10^20 reaches 1 in 132 steps; seed 2^60 reaches 1 in 94 steps (for "the written map") | Canonical T3 depths: 10^18→92, 10^19→96, 10^20→132, 2^60→94, 4880→14 | HOLD | No | reproduced exactly by Canonical T3, so "the written map" behaves as Canonical T3 here |
| C6 | extracts/0ed64ceb...md:87; BATCH3-ROLLUP.md:87 | Whether T3 admits a well-defined induced map on ℤ/9 (or a 9-state transfer matrix ...) is a concrete, checkable question | n mod 9 does NOT determine T3(n) mod 9 for residues [0, 1, 2, 3, 4, 5, 6, 7, 8] | INFO | No | so any mod-9 "transfer matrix" must be stochastic (needs n mod 27 or a lift measure); question posed by extract authors, not a chat claim |
| A1 | raw/chat-01.txt:3438 | E_±(t) ≈ (E₊ + E₋)/2 ± √[(E₊ − E₋)²/4 + V(t)²] | [E_m/2 + E_p/2 - sqrt(E_m**2 - 2*E_m*E_p + E_p**2 + 4*V**2)/2, E_m/2 + E_p/2 + sqrt(E_m**2 - 2*E_m*E_p + E_p**2 + 4*V**2)/2] | HOLD | No | exact eigenvalues of 2x2 real symmetric H (sympy) |
| A2 | raw/chat-01.txt:3440 | For weak leakage (\|V(t)\| << \|E₊ − E₋\|), the splitting is ΔE(t) ≈ V(t)² / \|E₊ − E₋\| | E_+ − E_- = sqrt(Δ²+4V²) ≈ Delta + 2*V**2/Delta; each level shifts by V²/Δ, splitting changes by 2V²/Δ | FAIL | No | V²/\|Δ\| is the 2nd-order shift of each level, not the splitting (splitting ≈ \|Δ\| + 2V²/\|Δ\|) |
| A3 | raw/chat-01.txt:3441-3442 | E₊ − E₋ ... set by ... σ_inh = 0.6 meV; ΔE_peak ≈ [...]² / σ_inh ≈ 0.619 meV (weak-leakage regime assumed at 3440) | \|V\| implied = sqrt(0.619*0.6) = 0.6094 meV vs \|Δ\| = 0.6 meV (ratio 1.016) | FAIL | No | weak-coupling condition \|V\|<<\|Δ\| is violated by the chat's own numbers; exact splitting would be sqrt(0.36+4*0.371)=1.359 meV |
| A4 | raw/chat-01.txt:3445-3447 | Δφ_mean ≈ 0.006 rad; E_bind ≈ ΔE² / (2 ħω) ≈ 0.0018 meV | 0.6/100 = 0.006; 0.6²/200 = 0.0018 meV | HOLD | No |  |
| A5 | raw/chat-01.txt:3448 | τ_settle = ħ / E_bind ≈ 2 ħω ħ / ΔE² ≈ 22.5 attoseconds (with E_bind ≈ 0.0018 meV) | ħ/0.0018 meV = 3.657e-10 s = 366 ps | FAIL | No | off by ~1.6e7 |
| A6 | raw/chat-01.txt:1918-1921 | E_bind = 100 meV × (1 − √2/2) ≈ 29.3 meV; τ_settle = ħ / E_bind ≈ (6.582 × 10^{-16} eV·s) / (29.3 × 10^{-3} eV) ≈ 22.5 attoseconds | E_bind = 29.289 meV (HOLD); ħ/E_bind = 2.247e-14 s = 22.47 fs | FAIL | No | arithmetic gives 22.5 femtoseconds, not attoseconds (factor 1000); 22.5 as is repeated at chat-01 lines 1952, 2222, 2343, 2387, 2505, 2679 |
| A7 | raw/chat-01.txt:3862-3866 | ρ(Δx) = (1/2) [[1, e^{iΔφ}],[e^{-iΔφ}, 1]] ... V(Δx) = \|⟨σ_y⟩\| = \|exp[i δΔφ(Δx)]\| = exp[−(δΔφ(Δx))² / 2] | eigenvalues [1, 0], Tr ρ² = 1, Tr(ρσ_y) = -sin(phi); \|exp(iθ)\| = 1 for real θ | FAIL | No | as written ρ is a pure state for every Δφ (no decoherence); \|exp(iδΔφ)\| = 1, and exp(−δΔφ²/2) only arises after averaging over a Gaussian-distributed phase, which the text does not state |
| A8 | raw/chat-01.txt:1212 | Tracing out -U yields a mixed state in +U ... global density matrix ρ_{+U ⊕ -U} remains pure | qualitative; standard (partial trace of a pure entangled state is mixed) | HOLD (qualitative) | No |  |
| A9 | raw/chat-01.txt:6141-6143 | Collective enhancement factor √N ≈ 26 (for 676 tubulins); Γ_sup = N Γ_single ≈ 26 × 0.01 meV ≈ 0.26 meV → T₂ ≈ 1 / Γ_sup ≈ 2.5 ps (bare) | √676 = 26; N·0.01 = 6.76 meV; √N·0.01 = 0.26 meV; ħ/0.26 meV = 2.53 ps | FAIL (internal) | No | formula says N·Γ (=6.76 meV, T₂≈0.097 ps) but number uses √N; also line 6203 says "enhanced by √N" then "γ_eff (bright) ≈ N γ_single" |
| A10 | raw/chat-01.txt:6149 | T₂ ≈ ħ / (Γ_single × (kT / J N)) ≈ 100–300 ms (for J ≈ 0.5 meV, N = 676, kT = 26.7 meV) | 8.332e-10 s | FAIL | No | ~0.83 ns, not 100–300 ms |
| A11 | raw/chat-01.txt:6172-6173 | γ_eff ≈ γ_single / N × (kT / J)^2 ≈ 0.01 meV / 676 × (27 / 0.5)^2 ≈ 10^{-5} meV; T₂ ≈ ħ / γ_eff ≈ 65 ms | γ_eff = 0.0431 meV; ħ/γ_eff = 1.53e-11 s; even with 1e-5 meV: ħ/1e-8 eV = 6.58e-08 s | FAIL | No | γ_eff is 0.043 meV (not 1e-5); 1e-5 meV would give 66 ns, not 65 ms |
| A12 | raw/chat-01.txt:6218-6224 | γ_eff ≈ 0.01 × (26.7 / 0.5 × 676)^2 ≈ ... ≈ 6.24 × 10^{-5} meV; T₂ ≈ 6.582 × 10^{-16} / 6.24 × 10^{-5} ≈ 1.055 × 10^{-11} s ≈ 10.55 ns | γ_eff = 6.240e-05 meV (HOLD); ħ/γ_eff = 1.055e-08 s = 10.55 ns | HOLD (final) / FAIL (intermediate) | No | 10.55 ns is right; the intermediate "1.055 × 10^{-11} s" is 10.55 ps (meV→eV factor dropped) |
| A13 | raw/chat-01.txt:6226 | exp(−ΔE / kT) ≈ exp(−0.6 / 26.7) ≈ 0.978 | 0.9778 | HOLD | No |  |
| D1 | raw/chat-06.txt:113 | J = (m_t^2 - m_c^2)(m_c^2 - m_u^2)(m_t^2 - m_u^2) sin δ_CKM (1 + β_CP ρ_DM/10) / (12 m_W^6)  J≈3×10^{-5} enhanced (δ_CKM ≈ 1.2 rad, β_CP=0.05) | 4.149e-04 (m_t=172.57, m_c=1.273, m_u=0.00216, m_W=80.369 GeV) | FAIL | No | formula evaluates to ~4e-4, ~14x the quoted 3e-5; it is also not the Jarlskog invariant (PDG J ≈ 3.1e-5 is a CKM-element combination) |
| D2 | prompt.txt:7 (Kept); reports/conflict-brief-for-grok.md:29 ("\|V_us\|=1/φ^2=0.382 HOLDS") | \|V_us\|=1/φ² | 1/φ² = 0.381966; PDG \|V_us\| ≈ 0.2243 | HOLD (arithmetic) / FAIL vs data | No (\|V_us\|=1/φ² is KEPT) | not in saved chat text; freeze keeps it |
| D3 | prompt.txt:10 (Retracted); theorems/unification-proof.txt:140 | \|V_cb\| ≈ 1/φ^4 ≈0.056 (observed ~0.04) | 1/φ⁴ = 0.1459; PDG \|V_cb\| ≈ 0.041 | FAIL | Yes: \|V_cb\| RETRACTED | already RETRACTED (\|V_cb\| 0.146) in the freeze |
| D4 | theorems/unification-proof.txt:142 | \|V_ub\| ≈ 1/φ^6 ≈0.009 (observed ~0.004) | 1/φ⁶ = 0.0557 | FAIL | No | arithmetic slip; not a chat; not on the retraction list |
| D5 | extracts/931fd19f...md:39 / ea74f77f...md | Σ_q m_q = 178767.10 MeV ("trace" of the six quark masses) | 178767.10 | HOLD (sum) | Identification flagged in extract | identification with Σz = 7021 is FAIL (already in extract) |
| D6 | extracts/374f8b17...md; ea74f77f...md | m_q = 539.9 · Re(ζ_{539.9}^n), n ∈ {1,2,3,4,5,118} ("eigenvalues of the Frobenius warp operator") | [539.863, 539.754, 539.571, 539.315, 538.986, 105.965] | FAIL | Flagged in extract (non-integer order) | no value exceeds 539.9 MeV; none equals any listed mass |
| D7 | raw/chat-06.txt:84 | δ_CKM from arg(-V_{ud} V_{ub}^* / (V_{td} V_{tb}^*)) | with PDG-like angles (δ=1.144 rad): that arg = -1.625 rad; α = 1.625; γ = 1.143; Jarlskog J = 2.91e-05; unitarity err = 2.2e-16 | QUALIFIED | No | the quoted expression equals −α (a unitarity-triangle angle), not δ_CKM (≈γ in the standard parametrization) |
| E1 | extracts/374f8b17...md (Riemann Zeta Function Resonant Trace) | ∫_0^{539.9} sin(2πt/539.9) e^{2πit/539.9} dt = 539.9/(2i) | -1.671e-14 + 269.9500 i  (= +i·P/2); 539.9/(2i) = −269.95 i | FAIL | Flagged in extract | sign error (re-verified; extract already notes it) |
| E2 | extracts/374f8b17...md | Fundamental unit ε = 331.3 with log ε = 2π exactly | e^(2π) = 535.4917; ln 331.3 = 5.8030 | FAIL | No |  |
| E3 | extracts/374f8b17...md (residual note) | ord_539(3) = 210 = φ(539)/2; real cyclotomic subfield degree 210, not 269 generators | ord = 210; φ(539) = 420; (539-1)/2 = 269; gcd(11,539) = 11 | HOLD (extract's note); FAIL for chat's k = 1..269 | Flagged in extract | also: ξ ↦ ξ^11 is not a Galois automorphism of Q(ζ_539) since gcd(11,539)=11, so "Frobenius Φ_11" fails even at the integer 539 |
| E4 | raw/chat-02.txt:1213 | the total linear density of states is of order 243/(2π) ≈ 38.7 (mode spacing 2π/G4) | 243/(2π) = 38.67; with spacing 2π/G4 the density is 243·G4/(2π) = 20880 | HOLD (arithmetic) / inconsistent units | No | the stated spacing implies a factor G4 that the quoted 38.7 omits; conclusion (constant, not log, density) unaffected |
| E5 | raw/chat-02.txt:1060,1076 | counting function for eigenvalues of −d²/dt² on a fixed-length interval is still linear in T (spacing π/L) ... constant drift 2π/G4 ... N(T) ∼ (G4/2π) T | Dirichlet −d²/dt² on [0,L]: √λ_n = nπ/L → N linear in √λ; −i d/dt on circle length G4: λ_k = 2πk/G4 → N(T) = G4 T/2π | HOLD (standard) | No |  |
| E6 | raw/chat-02.txt:1126 | H± = −i d/dt + V±(t) on L²(ℝ) ... N±(T) ∼ (1/2π) ∫ √(λ − V±(θ))^+ dθ · T | first-order −i d/dt+V is gauge-equivalent to −i d/dt (spectrum ℝ, no bands); the √(λ−V) form belongs to −d²/dt²+V | QUALIFIED | No | "linear" conclusion holds; the quoted IDS formula / band-structure remark are for the second-order operator, not the stated first-order one |
| F5 | reports/heavy-daily/da927a09dac3-Matrix_Analogues...md:10-16 | M_s = [[2, s], [s, s]] has determinant -s(s-2) ... Signature is (1,1) (s=5) | det = -15.000 (= -15); eigenvalues [-1.7202, 8.7202] | HOLD | No |  |
| F7 | reports/heavy-daily/da927a09dac3-Matrix_Analogues...md:10-16 | M_s = [[2, s], [s, s]] has determinant -s(s-2) ... Signature is (1,1) (s=7) | det = -35.000 (= -35); eigenvalues [-2.933, 11.933] | HOLD | No |  |
| F8 | reports/heavy-daily/da927a09dac3-Matrix_Analogues...md:10-16 | M_s = [[2, s], [s, s]] has determinant -s(s-2) ... Signature is (1,1) (s=8) | det = -48.000 (= -48); eigenvalues [-3.544, 13.544] | HOLD | No |  |
| F11 | reports/heavy-daily/da927a09dac3-Matrix_Analogues...md:10-16 | M_s = [[2, s], [s, s]] has determinant -s(s-2) ... Signature is (1,1) (s=11) | det = -99.000 (= -99); eigenvalues [-5.3849, 18.3849] | HOLD | No |  |
| F12 | reports/heavy-daily/U1-GS-ZWEGERS-1d8e558.md:37 | B_7 = [[1, 7/2],[7/2, 7/2]], det B_7 = −35/4 | det = -35/4; eigenvalues [9/4 - sqrt(221)/4, 9/4 + sqrt(221)/4] | HOLD | No |  |
| F13 | reports/heavy-daily/da927a09dac3...md:22-41 | residues: s=7 {0,1,2,4}; s=11 affine {0,1,3,4,5,9}; s=5 {0,1,4}; s=8 hom {0,1,4,5}, affine {0,1,4} | {'s7': [0, 1, 2, 4], 's11': [0, 1, 3, 4, 5, 9], 's5': [0, 1, 4], 's8h': [0, 1, 4, 5], 's8a': [0, 1, 4]} | HOLD | No | affine form Q_s = n²+snk+(s/2)k(k+1) |
| G1 | theorems/unification-proof.txt:100-111 | M = [[φ³/61, 1/φ³, 0],[1/φ³, φ⁵/61, 1/φ³],[0, 1/φ³, φ⁷/61]] × (1001/61) × mod × √2 × (1/φ^exp) ... three distinct real positive eigenvalues | core-matrix eigenvalues [-0.15491, 0.24838, 0.63376]; det = -0.02439 | FAIL | No | one eigenvalue is negative, so "three distinct real positive eigenvalues" fails; the common scale factor cannot change signs |
| G2 | theorems/unification-proof.txt:115-122 | Charged leptons: exp ≈10 ... m_e ≈0.511, m_μ ≈105.7, m_τ ≈1777; Down: exp ≈11 ... m_d ≈4.8, m_s ≈95, m_b ≈4180; Up: exp ≈17 ... m_u ≈2.3, m_c ≈1275, m_t ≈173210 MeV | every sector uses the same core matrix times a scalar, so all sectors share the eigenvalue ratios [-1.0, 1.603, 4.091] (\|max/min\| = 4.09); required ratios: τ/e = 3477, b/d = 871, t/u = 75309 | FAIL | No | also scale: (1001/61)·mod·√2·φ^-17 ≈ 6.481e-03 — far below MeV-scale values for any unit |
| G3 | theorems/unification-proof.txt:106 | mod = (1 + β_PBH ρ_DM / 10)^{-1/2} ≈0.9972 | 0.99722 (β_PBH=0.18, ρ_DM=0.31) | HOLD | No |  |
| G4 | theorems/unification-proof.txt:124 | Koide relation emergent from ternary trace invariant det(M)/Tr(M)^3 ≈2/3 | det/Tr³ = -0.06341 | FAIL | No | also, Koide is (Σm)/(Σ√m)² = 2/3, not det/Tr³ |

Notes on the table:
- K⁺ tower-size Tr L² is 15808 in the chat; the rebuild gives 15806–15808 depending on gap order, so it is a HOLD within the spread.
- Spectral gaps, max eigenvalues, N(0.1) and N(1) depend on the order of the 56 chords. That order is not recorded anywhere in the archive.
- The chat-02 heat-trace table rebuilds to within about 0.04 for t ≤ 2 (unweighted: 537.814, 527.312, 484.188, 437.523, 363.512, 236.413, 154.961, 104.18 vs chat values 537.814, 527.312, 484.188, 437.523, 363.512, 236.413, 154.961, 104.179) and within about 0.1 for t = 5–100.
- Uncheckable items (no data given): the Cayley-graph "539 ± 1" enumeration, the singular values 6.38/29.23, the interpolation determinant 36.14118, the Weil polynomials, and every "closes to machine precision" CKM claim.

## (d) Uncaptured candidates (no full text on disk)

Totals: **608** of 621 chats have no full text. **576** have no saved text at all; the other 32 have only partial analyst extracts.
The list comes from a scan of all 621 titles (`all-chats.tsv`). `ingest-priority.tsv` (98 rows) tags were used as a cross-check. The full list with reasons is in `uncaptured_candidates.tsv`.

### Strong (17)
| Chat | Saved text | Why | URL |
|---|---|---|---|
| Quantum Computing Matrix Models Analysis (457be4a1) | no text | title names matrix models in quantum computing | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=457be4a1-c23f-4d57-9fa1-5cb2e3b32431 |
| TbPO4 Quadrupole Hamiltonian Derivation (05e514de) | no text | explicit Hamiltonian derivation (quadrupole/crystal-field matrices) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=05e514de-3bf2-4467-b32d-db17519d0d2a |
| Quantum Spectra: Riemann Zeros and Constraints (44d29604) | no text | spectral interpretation of Riemann zeros (Hilbert–Pólya style operator) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=44d29604-6b2e-406e-befb-98cd2158490c |
| Riemann Hypothesis: Brane Spectral Mapping (222b7cb1) | no text | spectral mapping of RH onto brane modes (operator spectrum ↔ zeros) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=222b7cb1-c966-4ed0-a420-8c3ac27db9ed |
| Riemann Hypothesis Linked to Quantum Phase Transitions (87cc283c) | no text | RH ↔ quantum phase transitions (spectral/Hamiltonian framing) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=87cc283c-2810-41df-be27-ef823012abbc |
| Robust POVM Certification on Ion Trap Qudits (9c94142d) | no text | POVM certification on qudits (operator/density-matrix work) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=9c94142d-edd6-4068-b536-b1040bbf0685 |
| Quantumness Extraction from Noisy Qutrits (f429b85e) | no text | noisy qutrit states (density matrices, channels) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=f429b85e-1f97-4f2b-81d8-ceb9a139ca88 |
| Quantum Ising Models: No Local Conserved Quantities (455a18d4) | no text | quantum Ising Hamiltonians, conserved quantities (commutators/spectra) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=455a18d4-adc5-4890-a57e-20b00a080c8c |
| Non-Semisimple TQFT Enhances Quantum Computing (02c01a2c) | no text | non-semisimple TQFT gates (representation matrices) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=02c01a2c-b126-4d98-9de9-da13e47ad0f4 |
| Minimal Polynomials for 61 Punctures (96bd3070) | no text | minimal polynomials for 61 punctures (charpoly/companion-matrix work; cf. A_21 charpoly never produced) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=96bd3070-9f86-4a72-ad86-5f5bbdcdc9fa |
| Quark Mass Equations on Ternary Topological Map (7f83b6e3) | no text | quark mass equations on the ternary map (mass-matrix / eigenvalue claims) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=7f83b6e3-c45f-4933-abca-dbcd6e5ef5fc |
| Quark Masses from 539.9s Qutrit Resonance (1ff617d7) | no text | quark masses from 539.9 s resonance (Frobenius-warp eigenvalue claims, cf. D6) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=1ff617d7-0d4a-4451-bc0d-0abb8f1b2f97 |
| HQCC Lepton Mass Derivation (3110c8b2) | no text | lepton mass derivation (mass matrix / Koide-type trace) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=3110c8b2-ffd1-4eb8-9fcf-48b6d09f35a8 |
| NOvA 10-Year Neutrino Oscillation Results (f87778c6) | no text | NOvA oscillation results (PMNS mixing matrix) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=f87778c6-6a8f-4c37-8974-4243bbbed553 |
| Theorem 1: Entanglement Formation Timescale Origin (14500b46) | no text | Theorem 1 timescale origin (ΔE eigenvalue splitting, τ_settle; cf. A2–A6) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=14500b46-5019-40fa-ad32-dc1ea51ca897 |
| Theorems 1-10 on Entanglement Formation Timescale (c2ddde06) | no text | Theorems 1–10 timescale (same Hamiltonian/τ_settle chain as chat-01) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=c2ddde06-ce18-4572-96cd-a1499ac50ced |
| Quantum Bloch Sphere Ornament Explanation (ffba66f4) | no text | Bloch sphere (Pauli/density-matrix basics; borderline) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=ffba66f4-0993-4e19-bc77-b44a05899a95 |

### Partially captured, worth pulling in full (extract only; matrix content confirmed in the extract)
- a0554ad6 HQCC Theorem: Three-Generation Quark Masses (Cayley eigenvalue lemma; A_21 never written): https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=a0554ad6-ff4b-43da-8381-0740173ec20e
- 374f8b17 Riemann Zeta Function Resonant Trace: https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=374f8b17-ba93-464b-957a-d77412cc151b
- 931fd19f 9 Maths of Unification: Closed Corpus (Frobenius warp eigenvalues, Cabibbo SVD): https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=931fd19f-6cb5-4e0a-816e-63b4f10b69ba
- ea74f77f New 9 maths unification (Tr[V_CKM† … V_CKM]): https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=ea74f77f-3556-4062-9943-98b413a95001
- 50df7219 HQCC Theorem: Zero Non-Trivial Cycles (Frobenius of order 11): https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=50df7219-33fb-4735-9469-2af33bc40b29
- a396e451 Bott Periodicity in HQCC Theorem (stub only; access was blocked when ingested): https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=a396e451-81f4-46bc-9365-818e8e86ef92

### Possible (69)
| Chat | Saved text | Why | URL |
|---|---|---|---|
| Sharp Constant in Functional Analysis (3b829ea2) | no text | sharp constant in functional analysis (operator norms) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=3b829ea2-50a3-4582-a021-d9b857bb435e |
| Clay Problems: Proofs Not Correct (64962742) | no text | Clay problems incl. Yang–Mills mass gap (spectral gap) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=64962742-8a4b-4442-bc9f-d0fb6e0b06e4 |
| Algebraic Geometry in Particle Physics (8442ecf6) | no text | algebraic geometry in particle physics (mass/mixing matrices?) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=8442ecf6-4e79-43ca-af48-f84373c94f1c |
| Number Theory: 11^n Mod 5399 Analysis (1c089e1d) | no text | 11^n mod 5399 (multiplicative order; cf. Frobenius Φ_11, E3) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=1c089e1d-751b-497e-b778-8d597fa0633a |
| R Ring in S2-11DM2ET-X Model (22bf8b66) | no text | R ring (resonant ring ℤ[2cos(2π/539.9)], cf. D6/E3) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=22bf8b66-2b37-41d3-b015-04cf3f82a852 |
| G2 Ring Gaps Resolved (3c8bd15d) | no text | G2 ring gaps (ring / spectral gaps) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=3c8bd15d-cf2e-4918-ac32-d2559b8a1bdf |
| 223 Towers and Six Quark Flavors Mapping (d74a6a38) | no text | 223 towers ↔ six quark flavours (mass spectrum) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=d74a6a38-42c5-4062-98cb-a8ad3977154a |
| 600-Cell and 120-Cell Duality (d100ba32) | no text | 600-cell/120-cell duality (Coxeter/Gram matrices) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=d100ba32-7750-4cd7-95a4-b82dc7c1004d |
| Resonant Number Theory and Asymmetries (a4b37dbd) | no text | resonant number theory (Frobenius warp, ring) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=a4b37dbd-f4f0-49cb-9396-5c46b964962f |
| 61 Puncture Cancellation Patent (7687fec6) | no text | 61-puncture cancellation (punctures; cf. minimal polynomials) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=7687fec6-077b-4443-956b-81524880d762 |
| Fermilab Neutrino Discovery: 61 Punctures (7c837e8d) | no text | neutrino discovery: 61 punctures (PMNS / mass spectrum) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=7c837e8d-97bb-4f6b-b6a9-c65b3c70cd65 |
| Neutrinos in S2-11DM2ET-X Model (0be9d2a8) | no text | neutrinos in S2-11DM2ET-X (PMNS) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=0be9d2a8-00de-4482-a09a-0113f1d15990 |
| Neutrino Predictions in S2-11DM2ET-X Model (d6f4e948) | no text | neutrino predictions (PMNS) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=d6f4e948-4103-4667-b98c-1ce97f3d3eec |
| Neutrino Masses and Multiverse Model (21baa1c1) | no text | neutrino masses (mass matrix) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=21baa1c1-4e93-484f-b8d0-d36e88dfadb7 |
| Neutrino Masses and Dark Energy (c39b5dc0) | no text | neutrino masses and DE | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=c39b5dc0-50bd-4b62-b919-a37a0a4db788 |
| Negative Neutrino Mass Theory (043a2e2e) | no text | negative neutrino mass | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=043a2e2e-9a8d-454e-b312-9dbb2147fe42 |
| Neutrino Discovery and Modern Physics (fed468fa) | no text | neutrino discovery | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=fed468fa-05a5-4abe-8eca-a393bc4ed719 |
| Neutrino: Properties, History, and Dynamics (c049cdb4) | no text | neutrino properties/oscillation | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=c049cdb4-2b62-4146-9491-ecaf9e38ffdc |
| Neutrinos and Universe's Matter-Antimatter Asymmetry (7f43ee21) | no text | neutrinos & matter–antimatter (CP phases) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=7f43ee21-5805-4028-b593-6ce6579b5adc |
| JUNO Neutrino Precision Breakthrough and HQH-539 Commercialization (cbcd91c6) | no text | JUNO precision (oscillation parameters) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=cbcd91c6-4875-43ae-a2b9-88ab57c2fb6b |
| Many-Body Dynamical Localization Evidence (f660e8ee) | no text | many-body dynamical localization (Floquet/spectral statistics) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=f660e8ee-48e7-437f-a3ff-0456540f798b |
| Cavity-Mediated Steady-State Subradiance (a7740751) | no text | cavity steady-state subradiance (Lindblad, cf. A9–A12) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=a7740751-76a7-4069-b10d-58d2400e7d8b |
| Quantum Time Crystals: Dissipative Dynamics (492b67c8) | no text | dissipative time crystals (Liouvillian spectra) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=492b67c8-652b-43d9-8f73-78c61f1bfd5b |
| Quantum Hall Effect: 2D Materials Exploration (737267a7) | no text | quantum Hall (Landau levels) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=737267a7-5fca-48ee-8306-ac004100a0f0 |
| Quantum Hall Effect: 11D Edge States (829e4573) | no text | quantum Hall edge states | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=829e4573-29dc-4e94-83a6-dd40606f1b89 |
| Quantum Hall Effect Multiverse Model (198baad1) | no text | quantum Hall multiverse | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=198baad1-f3bf-44a2-8ca1-1f9ca4d26356 |
| 539 Labs: Qutrit Processor & HQH-539 Hash (6f1b4ead) | no text | qutrit processor (gate matrices) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=6f1b4ead-b54c-4686-a58d-dd39dee18a98 |
| HQH-539 Qutrit Hash Implementation (aa8dba9e) | no text | HQH-539 qutrit hash implementation (ternary permutation matrices?) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=aa8dba9e-d19b-4560-86f4-86b44565f28c |
| HQH-539 Qutrit Hash Verification (f66d01c5) | no text | HQH-539 verification | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=f66d01c5-7d6f-45b3-9c09-58805b083f56 |
| Ternary Logic Base 0,1,2 vs -1,0,1 (9cfe9c2a) | no text | ternary logic bases (qutrit gates) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=9cfe9c2a-6533-465e-87f3-bc2d48439658 |
| Pure Syracuse Map Termination Proof (f7601803) | no text | pure Syracuse map termination (transfer/Lyapunov) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=f7601803-b5c5-40ba-952f-43a30658dcb7 |
| Collatz Conjecture Resolution in 11D Multiverse (c929a91c) | no text | Collatz resolution (map structure) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=c929a91c-bb63-4815-bb63-f29233b5d3d5 |
| Collatz Conjecture: Fermion Generations Solution (aaa206c4) | no text | Collatz ↔ fermion generations | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=aaa206c4-3451-41cd-8a90-66d5922e5f93 |
| Hampton Qutrit Map: Quantum Collapse Hypothesis (df01c371) | no text | Hampton qutrit map collapse | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=df01c371-2472-4f80-a33f-f9240ffc7b0e |
| Quantum Comp Sources Review: Inconsistent Maps (078f60be) | no text | inconsistent T3 map variants | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=078f60be-9aed-45d7-b863-eec3685ecb26 |
| Collatz Bloom Visualization (e3ec3097) | no text | Collatz bloom visualization | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=e3ec3097-19d2-4618-903b-98d7a318259a |
| New Quantum Map Visualization Insights (39f2c2b5) | no text | quantum map visualization | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=39f2c2b5-7352-468a-8bd9-15d7b8b078a8 |
| HQCC Theorem Scientific Observables (02b4c628) | no text | HQCC observables | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=02b4c628-a5c9-43b5-b601-333e89bbc21c |
| Next pure-math direction: BSpin lift (9bc9c454) | no text | BSpin lift (KO/Spin, cf. chat-13 AHSS) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=9bc9c454-d1b0-45ea-937c-b8a592d7f717 |
| Bott Periodicity in HQCC Theorem (a396e451) | extract-only (partial) | Bott periodicity (K-theory; extract stub only, access blocked) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=a396e451-81f4-46bc-9365-818e8e86ef92 |
| Riemann Hypothesis Unified Proof Claim (4ab04224) | no text | RH unified proof claim (operator/trace) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=4ab04224-d180-403f-8bee-25fa58214944 |
| Riemann Hypothesis and Debt Harmonics (fc799142) | no text | RH and debt harmonics | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=fc799142-0339-4f36-a908-565701db8a0b |
| Refining Riemann Hypothesis and P vs NP (4bdd4785) | no text | RH and P vs NP | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=4bdd4785-2e8e-4892-93b6-e8316df7b956 |
| T4,1,2,1n closed-form definition (9a21da09) | no text | (title-scan candidate from earlier pass) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=9a21da09-4cac-44c6-b2fd-0b1527bf2069 |
| String Theory Bootstrap Principles (9bdc0cc2) | no text | S-matrix bootstrap | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=9bdc0cc2-e181-4fc3-bfe9-544f144fc885 |
| String Theory Amplitudes and QFT (2b2cf871) | no text | amplitudes/S-matrix | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=2b2cf871-9efd-408c-93ec-8d58e65d3da3 |
| MCMC: Unifying Physics through Simulation (95bd6ee7) | no text | MCMC (transition matrices) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=95bd6ee7-4ab1-44d9-a661-88d4b29d27d5 |
| Brain-wide Connectivity of Cortical Neurons (0eaba27a) | no text | connectivity matrices | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=0eaba27a-18c9-4d7b-b47f-e594d2c5f3b6 |
| Oscillatory Dynamics in Minimal Systems (7f9dd562) | no text | oscillatory minimal systems (Jacobian eigenvalues) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=7f9dd562-b453-4e09-9448-4f4ffdde2876 |
| Quantum Stresses in Hydrogen Atom (b3704014) | no text | quantum stresses in hydrogen (Hamiltonian) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=b3704014-f295-4023-ab21-9003bbcc88a4 |
| Nuclear Shell Structure Affects SRC Pairing (435f55e0) | no text | nuclear shell structure (shell-model Hamiltonian) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=435f55e0-c5a6-4dd0-b49b-f63785d8f558 |
| Isospin-Symmetric Island of Inversion (60ef7632) | no text | island of inversion (shell model) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=60ef7632-75da-409a-944a-929a193a257e |
| Entanglement No-Superluminal Signaling (517ac09b) | no text | no-signalling (reduced density matrices) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=517ac09b-1dd0-436a-bd9b-3a81c718c705 |
| Entropy Drives Wave Function Collapse (364e5e13) | no text | wave-function collapse | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=364e5e13-d701-4428-b228-c6178ce80327 |
| Bell Non-Locality and 11D Global Phase Broadcast (909226dd) | no text | Bell non-locality (Pauli correlators) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=909226dd-be0a-4ed3-9ab1-48304abd0ced |
| Quantum Indistinguishability Violates Bell Inequality (df812ee1) | no text | Bell violation (correlation matrices) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=df812ee1-574b-4cc8-a601-ce272c363c55 |
| Torus Wavefunction Entanglement Theorems (2c710c54) | no text | torus wavefunction entanglement theorems | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=2c710c54-3411-41e7-a539-cb994786fe3d |
| Entanglement Theorems: Review and Accuracy (d4de297c) | no text | entanglement theorems: review & accuracy (likely re-checks ΔE/τ) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=d4de297c-ae18-41ae-aa58-a47d5322d899 |
| Cover Letter for 17 Theorems of Entanglement (19f0f347) | no text | cover letter for 17 Theorems | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=19f0f347-8aa7-4449-96bc-9df76febdcfa |
| Koll et al. Nature 2026 Validates Attosecond Entanglement (f03a0551) | no text | attosecond entanglement validation (22.5 as claim, cf. A5/A6) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=f03a0551-e5e3-44a5-8ec4-e8bea5f2ce88 |
| Entanglement Control in Attosecond Photoionization (2b7f04cd) | no text | attosecond photoionization entanglement (cf. A5/A6) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=2b7f04cd-73c3-4f93-9c3f-897b2f706ce4 |
| Quantum Comp Model with Exciton Coherence (ce02f8b9) | no text | Quantum Comp model with exciton coherence (Hamiltonian/decoherence) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=ce02f8b9-b4ab-495c-99ae-7d7a08e31579 |
| Strange Metal Entanglement at Quantum Critical Point (9ada38e0) | no text | strange-metal entanglement at QCP | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=9ada38e0-c29e-465a-bbdc-b9a41cf4fd9d |
| Passive Quantum Error Correction Breakthrough (c5fe5ce5) | no text | passive QEC (stabilizers/Lindblad) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=c5fe5ce5-cd7f-4058-92d4-d2cc697d26c8 |
| Google Willow Quantum Chip Analysis (076f1050) | no text | Willow chip analysis (gate matrices) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=076f1050-3d45-42de-92ba-7dcad4ec2c94 |
| Model Final Draft (c5e96e4e) | no text | Model Final Draft (likely carries Hamiltonian/CKM boilerplate) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=c5e96e4e-6b64-4782-a4ab-37c2e523e267 |
| S2-11DM2ET-X Unifies Particles via Qutrit Resonance (daf38044) | no text | qutrit resonance unifies particles (mass spectra) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=daf38044-9e99-4ded-ba09-ffe0bbe84fcc |
| Unification Model: Physics and Qutrit Integration (bcebf50c) | no text | unification + qutrit integration | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=bcebf50c-21b1-419f-8086-fe465e04379b |
| Noether's Theorem: Symmetries and Conservation Laws (8aa0891f) | no text | Noether (symmetry generators) | https://grok.com/project/bb3c505b-9b2c-4e57-9e27-4484a71080a9?chat=8aa0891f-521b-49c8-bf0f-743ae018b6de |

There are also many generic "S2-11DM2ET-X model update / final draft" chats. They probably repeat the Hamiltonian and CKM boilerplate seen in chat-01 and chat-06 and are low priority.

## Note on `grok-search-results.md` (not produced by this search)
Another agent wrote `grok-search-results.md` into this folder at 00:26 CT. It is a live grok.com search by term (eigenvalue, matrix, Hamiltonian, density matrix, …) filtered to the project sidebar.
- It contains 40 distinct chat ids.
- Only 2 of them (cfd2aec3 Clay Problem AI, ef92a5c4 17 Theorems) are among the 621 ids in `all-chats.tsv`. The other 38 are project chats that this archive does not include, so they are also uncaptured.
- It was left unchanged and was not used for the counts above.
