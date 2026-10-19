# Analytic Cat-B push — sections new since rev6 (Continuation 2, D.0–D.4, E.0–E.3, Round 3, Round 4)

Excerpt of `2026-10-18-Analytic-CatB-Push.md` (local source sha256 f553bee521e976dd25f7159feeb3736fb260179135060c3b59bcae7ab248f397), lines 274–625, i.e. everything after the snapshot already on Master in `Analytic_CatB_Push_2026-10-18/2026-10-18-Analytic-CatB-Push.md` (which ends at C.3). Pushed 2026-10-19 with Bridge C rev7.

Edits relative to the source text (labels only; no mathematical content changed): four occurrences of the retired letter label for the CRT factorization statement were replaced by "CFP" (CRT Factorization Proposition), per `NOTE_LABEL_CFP.md` in this folder. "Lemma R" in this excerpt means the q-adic reduction lemma of C.2 (rev6/rev7 PDF: Lemma 14.9), not Lemma R of rev. 4. "Theorem 1/2/3" refer to the report's own §§1–3 (rev7 PDF: Theorem 14.6, Proposition 14.8).

Categories: A = proved or exact; B = floating-point only. No TPC/RH claims; distinct from HQCC termination claims. CORE_FREEZE holds. File paths in the text refer to the local folder `2026-10-18-Analytic-CatB-Push/`; the new files are in this folder (scripts as files; text outputs in OUTPUTS_BUNDLE_2026-10-19.txt; small pickles in BINARIES_B64_BUNDLE_2026-10-19.txt).


---

## Continuation 2, 2026-10-18, 22:07 CDT onward ("pursue all open")

New files in `2026-10-18-Analytic-CatB-Push/`:
- `even_N_theorem.py` → `even_N_theorem.json`, `even_N_theorem.log`
- `ea_N8.py` → `ea_N8.json`, `ea_N8.log`
- `sym_P8_K13.log`, `sym_P12_K13.log`, `sym_P1_K15.log`, and the matching pickles once those runs finish

### D.0 General-formula checks for N = 32, 35, 45 (Cat A)

`gauss_local_run.log` now reads:
- N = 32: 199,680 tests, 0 mismatches.
- N = 35: 327,600 tests, 0 mismatches.
- N = 45: 421,200 tests, 0 mismatches.

The N = 49 run is still going; its line will appear in `gauss_local_run.log`. (The buggy first-attempt process was stopped; it was writing only to `gauss_local_run_first_attempt_bugL.log`.)

### D.2 Even-N periods derived from the 2-adic reduction (Cat A)

**Setup.** For N = 2^k, the CFP gives H(c) = T₂ = Σ_{y mod 2^n} e(a(A2·y² + B2·y + 2C)/2^n), with n = k+1. Lemma R reduces this using:
- v = v₂(A2), where A2 = sΔ/g² = s(s−2)(7s−32)/g²;
- the parity of B2 = 2c·B(w,u₂) + s·b;
- C = Q₊(cw).

**2-adic valuations by class of s:**
- **s odd:** v = 0, and B2 is odd (s and b are odd). For n ≥ 2 the base case with β′ odd gives 0, so H ≡ 0.
- **s ≡ 2 mod 4:** g₂ = 2 and v = v₂(s−2) ≥ 2. Also B2 ≡ 2 mod 4, because b is odd and B(w,u₂) is even. So 2^v ∤ B2 and H ≡ 0.
- **s ≡ 4 mod 8:** g₂ = 4, v = 2+1+2−4 = 1, and m and b are odd. Then α′ = Q₂(u₂) ≡ 1 + 0 + 2 ≡ 3 mod 4, B2 ≡ 4(c·n_w + 1) mod 8, and C ≡ c²n_w² mod 4.
- **s ≡ 8 mod 16:** v = 1, m is odd and b is even. Then β′ = B2/2 ≡ 2c·n_w·m mod 8, which is even.
- **16 | s:** m is even and b is odd, so n_w is odd. Then A2 ≡ 2m² ≡ 0 mod 8 (v ≥ 3), B2 ≡ 0 mod 8, and C ≡ c² mod 4.

**N = 2 (n = 2).** When v = 1, the base case j = 1 needs β′ odd. But β′ is even in both v = 1 classes, so those give 0. When 16 | s, v ≥ 2 = n, and T = 4·[4 | B2]·e(2aC/4) = 4(−1)^c. So:

  **H_{1/2}(c) = 4(−1)^c·[16 | s]**, period 16.

**N = 4 (n = 3).** In the v = 1 classes, j = 2 and β′ is even, so H ≠ 0, and all the phases are determined (above) independently of s. When 16 | s, v ≥ 3 = n gives T = 8·e(aC/4). So:

  **H_{a/4}(c) = 0 if 4 ∤ s; = 4(1 + i^a) if s ≡ 4 mod 8 or s ≡ 8 mod 16; = 8·e(ac²/4) if 16 | s.**

The period is 16. This was checked exactly (in Z[ζ₈]) for s < 2000, a = 1, 3, and all c: 31,920 tests, 0 mismatches.

**N = 8 (n = 4).** There are 15 distinct H-vectors over s mod 96 and a ∈ {1,3,5,7} (exact, `even_N_theorem.log`). The classes are:

| class | shape |
|---|---|
| 4 ∤ s | 0 |
| s ≡ 0 mod 32 | depends on a |
| s ≡ 16 mod 32 | depends on a |
| s ≡ 8 mod 16 | depends on a |
| s ≡ 4 mod 8, b ≡ 3 mod 4 | independent of a |
| s ≡ 4 mod 8, b ≡ 1 mod 4 | independent of a |

**Where the 32 and the 3 in 96 come from (s ≡ 4 mod 8):**
- At n = 4 the reduction keeps one more 2-adic digit than at N = 4. Then α′ ≡ m² + 4 + (s/2)b² ≡ 5 + s/2 mod 8, which depends on s mod 16. Also s·b mod 16 enters B2, so b mod 4 matters. In the 16 | s class, v₂(A2) depends on s mod 32.
- b mod 4 = ((s−8)/4)·g₃⁻¹ mod 4, and g₃⁻¹ = 3 ≡ −1 mod 4 when 3 | g, i.e. s ≡ 2 mod 3. So b mod 4 has period 48. The data confirm this: class D (b ≡ 3 mod 4) is exactly [s ≡ 4 mod 16] XOR [s ≡ 2 mod 3].
- Hence the period is lcm(32, 48) = 96. This matches the exhaustive result.
- The D and E classes are related by the reflection u₂ → −u₂ mod 4 (Lemma 2), so ea_E,r = (−1)^r·ea_D,r. This agrees with the table in D.3.
- For the 16 | s and 8 mod 16 classes, the dependence on a comes through (2/a) and i^a in the base case.

**Status.**
- N = 2 and N = 4: fully conceptual (Cat A).
- N = 8: the invariants that matter (s mod 32 in the 16 | s class, s mod 16, b mod 4) and the factor 3 are explained conceptually. That the shapes really are distinct is exact (Cat A), but by exhaustive check.

### D.3 Explicit ea tables at x = a/8 (Cat A; `ea_N8.json`)

ea_r for r = 1..4. ea_1 = ea_3 = 0 in the first three rows. Full data are in the JSON.

| class (representative s) | a = 1 | a = 3, 5, 7 |
|---|---|---|
| s ≡ 0 mod 32 (32) | (0, 1 − √2(1+i)/12, 0, −1/64 + 7√2(1+i)/15360) | the √2(1+i) terms become √2·(−1+i), (−1−i), (1−i) |
| s ≡ 16 mod 32 (48) | (0, −√2(1+i)/12, 0, 7√2(1+i)/15360) | same rotation |
| s ≡ 8 mod 16 (24) | (0, √2(1+i)/24, 0, −√2(1+i)/30720) | same rotation |
| s ≡ 4 mod 8, b ≡ 3 mod 4 (36) | (−4, 1/2, 3/64, −1/128) | same for all a |
| s ≡ 4 mod 8, b ≡ 1 mod 4 (12) | (4, 1/2, −3/64, −1/128) = (−1)^r × previous row | same for all a |
| 4 ∤ s | 0 | 0 |

How the tables were checked:
- That every s in a class gives the same ea follows because H is the same on each class mod 96. That was checked exactly in `even_N_theorem.py`, and ea is computed from H.
- ea = 0 for 4 ∤ s was checked exactly for s = 5..299.

### D.1 t^{11/2} and t^{13/2} at x = 1/4 and x = 1/6 (Cat A; numerics Cat B)

**Symbolic run.** `sym_engine.py` was run at P = 8 and P = 12 with K = 13, giving `sym_universal_P8_K13.pkl` and `sym_universal_P12_K13.pkl` (both finished 22:28 CDT).

**Closed form (Cat A).** For e = 11, 13:

  c_e(s) = γ₀·A_e(s) + Σ_r eb_r·Y_{e,r}(s) + Σ_r ea_r·X_{e,r}(s,g),

with these universal functions (in s, g) and the exact class constants below. `hs_coeffs.py` evaluates this exactly for any s. Class constants and c₁₁, c₁₃ values for s = 5..20 (x = 1/4) and selected s (x = 1/6) are in `class_data_N4_N6.json/.log`.

**x = 1/4:**
- 4 | s: γ₀ = (1+i)/2 and eb = (0, 1/3 − i/6, 0, …).
- ea is given by the D.2 shapes: ea = eb when 16 | s, and ea = (0, (1+i)/12, 0, …) otherwise.

**x = 1/6:**
- γ₀ = 0 for every s.
- Example, s = 16: eb = (6, 3/4 − i√3/12, −1/4, …) and ea = (−6, 3/4 − i√3/12, 1/4, …), i.e. ea_r = (−1)^r·eb_r here.
- Example, s = 8: ea = 0, because 16 ∤ s.

**New vanishing results (Cat A).**
- **x = ±1/4, 4 ∤ s:** H_s(±i·e^{−t}) = O(t^M) for every M.
  - Proof: G(j) is killed by a sign-reversing shift. For s odd, Q₊(j,k+4) − Q₊(j,k) ≡ 2s ≡ 2 mod 4. For s ≡ 2 mod 4, Q₊(j,k+2) − Q₊(j,k) ≡ 2 mod 4. Hence γ₀ = eb = 0. Also ea = 0 by D.2 (N = 4).
- **x = 1/6, odd s:** O(t^M) for every M. By the CRT factorization (the CFP, which applies equally to G and γ₀), the Gauss data contain the x = 1/2 factor, and that factor vanishes for odd s (Prop. O).
- Both are confirmed by exact zeros at s = 5, 7, 9, … in `class_data_N4_N6.log`.

**Independent engine, |difference| at t^{9/2}, t^{11/2}, t^{13/2}:** 0 at double precision for x = 1/4 at s = 8, 12, 16, and for x = 1/6 at s = 8, 16 (`check_engine_K13_x14.jsonl`, `check_engine_K13_x16.jsonl`).

**60-digit direct sums (Cat B; `run_numerics2.sh` → `numerics_F/G/H.jsonl`):**

| case | rel. err. c₁₁ | rel. err. c₁₃ |
|---|---|---|
| s = 8, x = 1/4 | 2.0e−13 | 1.7e−9 |
| s = 8, x = 3/4 (complex conjugate, as expected) | 2.0e−13 | 1.7e−9 |
| s = 8, x = 1/6 | 8.0e−10 | 8.3e−7 |

**Limits of the numerics.** Larger s at x = 1/4 or 1/6 would need ≳ 10⁷ terms per value of t, because the window scales as (mP)⁻²; I did not run them. Those cases rest on the Cat A form plus the engine agreement.

### D.4 t^{15/2} at x = 0: status as of 23:12 CDT (in progress)

**First attempt failed.** `sym_engine.py 1 15` stopped at 22:55 CDT with a sympy `HeuristicGCDFailed` exception inside `simplify`. The log is kept as `sym_P1_K15_attempt1_HeuristicGCDFailed.log`.

**Rerun.** I started `sym_engine_K15.py` at 23:11. It is the same mathematics, except that `sp.simplify` is wrapped: when simplification fails, the exact unsimplified expression is kept. It writes `sym_universal_P1_K15.pkl` and `sym_P1_K15.log`.

**Prepared for when it finishes:**
- `closed_forms_K15.py` will produce the exact R₁₅ and S₁₅ and check them on held-out values of s.
- `numerics_mp_K15.py` subtracts the expansion through t^{11/2} and fits c₁₃ and c₁₅, for Cat B support.

---

## Continuation 3 (box clock 22:58 CDT, 2026-10-18)

**Clock note.** The box was restored from a VM snapshot ("virtual machine fork" in dmesg), so the box clock now reads earlier than some timestamps written above in D.4. The D.4 rerun of `sym_engine_K15.py` restarted with the box and is running again.

**Label change.** From here on, the CRT factorization statement (C.2) is called the **CRT Factorization Proposition (CFP)**. It is the same statement that sections C.2–D.2 call by a retired letter label (see NOTE_LABEL_CFP.md); the earlier text is left unedited, as appended sections must not rewrite it.

### E.0 General-formula checks, now complete (Cat A, exact)

- N = 49: 802,620 tests, 0 mismatches (`gauss_local_run.log`).
- With N = 32, 35, 45 (D.0), the closed form of H(c) from the CFP plus Lemma R agrees exactly with brute force for every N in {2–13, 15, 16, 21, 25, 27, 32, 35, 45, 49}, all a coprime to N, s < 200, and every c.

### E.1 Status of the other remaining items

| item | status | category | where |
|---|---|---|---|
| x = 1/4 and 1/6 at t^{11/2}, t^{13/2} | done | form: A; engine agreement: A-level consistency; 60-digit numerics: B | D.1 |
| even-N periods 16 (N = 2, 4) | done, conceptual | A | D.2 |
| even-N period 96 (N = 8) | origin of the factors 32 and 3 explained; distinctness of the classes by exact exhaustive computation over the proved period bound | A | D.2 |
| N = 8 ea tables | done | A | D.3, `ea_N8.json` |
| t^{15/2} at x = 0 | running | — | E.2 (below, once finished) |

### E.2 t^{15/2} at x = 0: OPEN (not obtained)

**What happened.**
- The first attempt (`sym_engine.py 1 15`) crashed with sympy `HeuristicGCDFailed` (`sym_P1_K15_attempt1_HeuristicGCDFailed.log`).
- The rerun (`sym_engine_K15.py`, with simplify failures kept as exact unsimplified expressions) accumulated about 35 minutes of elapsed run time.
- After that, repeated box snapshot restores stopped its progress: the elapsed time stayed frozen at 35:11 across three consecutive 13-minute waits.
- No `sym_universal_P1_K15.pkl` was produced, so no t^{15/2} coefficient, closed form, or numeric check exists. **Nothing is claimed at t^{15/2}.**

**To finish:**
1. Rerun `python3 sym_engine_K15.py 1 15` (estimated ≈ 1.5 h of CPU) on a box that is not being restored.
2. Then run `python3 closed_forms_K15.py 1 15` for the exact R₁₅ and S₁₅, with checks on held-out values of s (Cat A).
3. Then run `numerics_mp_K15.py` for 60-digit Cat B support.

### E.3 What stays open overall
- t^{15/2} at x = 0 (E.2).
- A fully conceptual (non-exhaustive) proof that the N = 8 classes are pairwise distinct (D.2). Their distinctness is currently established by exact exhaustive computation over the proved period bound.
- Direct numerics at x = 1/4 and 1/6 for s ≠ 8. These need ≳ 10⁷ terms; the Cat A form and the exact engine agreement stand without them.

---

## Round 3 (from 23:40 CDT, 2026-10-18)

Labels: the CRT Factorization Proposition is "CFP"; see `2026-10-18-Analytic-CatB-Push/NOTE_LABEL_CFP.md`.

### F.2 The six N = 8 classes are pairwise distinct: proof without a scan over s (Cat A)

**Reduction to residues.**
- Q₊ mod 8 depends only on s mod 16 and on (n,k) mod 16, because k(k+1)/2 mod 8 is 16-periodic and s ↦ s+16 changes Q₊ by 16nk + 8k(k+1).
- Hence H_{a/8}(c) is a function of (s mod 16, u₂ mod 16, w mod 16), with k_w·m − b·n_w ≡ 1 mod 16.

**Residue constraints of each class** (exact, from m = 3s/g, b = (s−8)/g, g = g₂g₃):
- **A (s ≡ 0 mod 32):** s ≡ 0 mod 16, g₂ = 8, m = 6t/g₃ with t = s/16 even, so 4 | m; b odd.
- **B (s ≡ 16 mod 32):** same, but t is odd, so v₂(m) = 1.
- **C (s ≡ 8 mod 16):** g₂ = 8, m = 3(s/8)/g₃ is odd, b is even.
- **D/E (s ≡ 4 mod 8):** g₂ = 4, and the data are coupled exactly: b·g₃ = s/4 − 2, m = 3b + 6/g₃, s ≡ 4(b·g₃ + 2) mod 16. D is b ≡ 3 mod 4 and E is b ≡ 1 mod 4.
- **Zero class (4 ∤ s):** H ≡ 0 (D.2).

**Invariants**, for a = 1:
- I1 = max_c |H(c)|;
- I2 = the support of H;
- I3 = the phase of H(0);
- I4 = H(1)/H(0).

**Hand derivation of the invariants from Lemma R** (n = 4, j = n − v):
- **I1:** |H| = 2^v·|base|. For v = 1 the base case j = 3 gives |1 + i^{α′}|·2^{3/2} = 4, so |H| = 8 (classes C, D, E). For v ≥ 3 the bound is 16 (classes A, B).
- **Valuations:** v₂(A2) = 3 for B, because v₂(2m²) = 2v₂(s) − 5 = 3 < v₂(sb²) = 4. And v₂(A2) ≥ 4 for A.
- **I2:**
  - In B (v = 3, j = 1), H(c) = 16·[β′ odd]·(phase), with β′ = B2/8 ≡ c + 2 mod 4. Here B(w,u₂) ≡ 4·odd mod 16 because n_w is odd and v₂(m) = 1, and sb ≡ 16 mod 32. So the support is exactly the odd c.
  - In A, 16 | B2 for every c, so |H| = 16 everywhere.
- **I3, C vs D/E:**
  - In C, b is even, so β′(0)/2 = sb/4 ≡ 0 mod 4 and α′ ≡ m² ≡ 1 mod 8. That gives H(0) = 2·(1+i)·2√2 = 8·e(1/8), which is not real.
  - In D/E, β′(0)/2 is odd and α′ ≡ 5 + s/2 mod 8 ∈ {7, 3}. Both values give H(0) = +8, which is real.
- **I4, D vs E (the g₃-scaling argument):**
  - Scaling u₂ ↦ 3u₂ (and w ↦ 3⁻¹w) gives Q₊(11ν) − Q₊(ν) ≡ 4·(2Q₂(ν)) + 5s·k ≡ 4k mod 8, using 3⁻¹ ≡ 11 mod 16 and s ≡ 4 mod 8.
  - The extra factor (−1)^{k} shifts β′ by 4. That flips the sign exactly when c·n_w is odd, because β′/2 ≡ c·n_w + 1 mod 2.
  - Together this gives H′(c) = (−1)^{c(k_w + n_w)}·H(c) = (−1)^c·H(c), since k_w + n_w is odd when m and b are odd.
  - Under the coupling above, this scaling is what separates b ≡ 1 from b ≡ 3 mod 4. Hence I4(E) = −I4(D) ≠ 0.

**Exact residue-level confirmation.** This enumerates every residue tuple satisfying each class's constraints; it is not a scan over s.
- `n8_distinct_residues.py` → `.json/.log`:
  - A: (I1, I2) = (16, full support).
  - B: (16, odd c only).
  - C: (8, full support), with I3 = e(1/8).
  - D and E: (8, full support), with I3 = ±1, which is real.
- `n8_DE_residues.py` → `.json/.log`, using the exact D/E coupling: **I4 = +1 for every residue tuple with b ≡ 3 mod 4 and −1 for every tuple with b ≡ 1 mod 4**, for all a ∈ {1,3,5,7}.
- These invariant values are pairwise different across the six classes, so the classes are pairwise distinct for every s.

**Status: Cat A.** The proof is the residue reduction plus a finite computation over residues, together with the hand derivation above. It no longer depends on the exhaustive scan over s mod 96.

### F.3 Label note (done)

`2026-10-18-Analytic-CatB-Push/NOTE_LABEL_CFP.md` records that the retired letter label in C.2–D.2, `gauss_local.py` and `even_N_theorem.py` means the CFP. No earlier file was edited.

### F.1 t^{15/2} at x = 0: status (updated below if it finishes)

- Running detached with checkpoints: `sym_engine_e15_ckpt.py` → `e15_ckpt.pkl` (one entry per finished term) and `e15_ckpt.log`.
- It reuses the exact e ≤ 13 entries of `sym_universal_P1_K13.pkl` and computes only e = 15.
- The full run `sym_engine_K15.py` is also still running in parallel.
- No CloudAgent tool is available to me in this session, so the cloud fallback could not be used.

### F.1 (result) t^{15/2} at x = 0 (Cat A; numerics Cat B)

**Run.** The full detached run `sym_engine_K15.py 1 15` finished and wrote `sym_universal_P1_K15.pkl`. The checkpointed fallback had finished 10 of its 17 edge terms and was stopped as no longer needed; its partial state is in `e15_ckpt.pkl` and `e15_ckpt.log`.

**Closed form** (`closed_forms_K15.py` → `closed_P1_K15.log/.json`, `closed_P1_e15_K15.pkl`). The **R + S√Δ form persists at t^{15/2}**, with Δ = (s−2)(7s−32):
- At every integer sample s, the exact coefficient splits uniquely into a rational part plus a rational multiple of √Δ, with g kept as a symbol (the split is asserted at each point).
- Both interpolants pass exact checks at 10 held-out values of s.

The result is c₁₅ = √(2πs)·[R₁₅(s) + S₁₅(s,g)·√Δ], with

  R₁₅ = −(109395s¹⁶ + 101686679952s¹⁵ − 3187115618544s¹⁴ + 46293465582144s¹³ − 413519826187232s¹² + 2541079636386048s¹¹ − 11380877198270208s¹⁰ + 38384599582350336s⁹ − 99282599963294976s⁸ + 198565733544910848s⁷ − 307079253310144512s⁶ + 364192854191898624s⁵ − 325264051610320896s⁴ + 211726943991627776s³ − 94811608546541568s² + 26109726815158272s − 3332235344216064)/(148002103413964800(s−2)⁹).

S₁₅ is a polynomial in g (even powers) over (s−2)⁹(7s−32)⁹; it is given in full in the JSON. The denominator pattern (s−2)^{(e+3)/2} continues.

**Checks** (`check_K15.py` → `check_K15.json/.log`):
- The K = 15 pickle reproduces all K = 13 coefficients exactly (difference 0 at 60 digits).
- c₁₅(5) = 0 exactly, consistent with H₅ ≡ 0.
- The independent engine agrees exactly at double precision for s = 6, 7, 9.

**60-digit direct sums (Cat B; `numerics_mp_K15.py`, `run_numerics_K15.sh` → `numerics_K15_{I,J,K}.jsonl`).** The expansion through t^{11/2} is subtracted, then c₁₃ and c₁₅ are fitted:

| s | rel. err. c₁₃ | rel. err. c₁₅ |
|---|---|---|
| 20 | 1.7e−14 | 2.6e−10 |
| 32 | 7.9e−13 | 4.5e−9 |
| 8 | 2.0e−8 | 8.9e−6 |

### Round 3 summary

| item | result | category |
|---|---|---|
| t^{15/2} at x = 0 | closed form R₁₅ + S₁₅√Δ; the R + S√Δ form persists | A (numerics B) |
| N = 8 classes pairwise distinct | separated by the invariants I1–I4, derived by hand from Lemma R plus a finite residue computation, with no scan over s | A |
| CFP label note | `NOTE_LABEL_CFP.md` | done |

**Open:** t^{17/2} and beyond (mechanical, about ×3.3 cost per order); and the S₁₅ structure (degree in g) has not been analysed beyond the stored expression.

---

## Round 4 (from 00:13 CDT, 2026-10-19): t^{17/2} at x = 0, and the structure of S_e

### G.1 t^{17/2}: running (checkpointed)

- `sym_engine_K17.py` runs detached. It reuses the exact e ≤ 15 entries of `sym_universal_P1_K15.pkl`, computes only e = 17 with the K15 engine functions, and checkpoints every term to `e17_ckpt.pkl`. The log is `e17_ckpt.log`.
- It needs about 130 MB of RSS, so memory is not a constraint (about 13 GB was free).
- Results will be appended below.

### G.2 Structure of S₁₁, S₁₃, S₁₅ (exact factorizations; `S_structure.py` → `S_structure.txt`)

Write S_e·(s−2)^k(7s−32)^k = Σ_j σ_{e,2j}(s)·g^{2j}, with k = (e+3)/2. The following are exact factorizations for e = 11, 13, 15 (**Cat A for each e**):
- **Even powers only.** g appears only in even powers g⁰, g², …, g^{e+1}.
- **Top coefficient.** σ_{e,e+1} = const·(s−2)^{(e+1)/2}. The constant carries the Bernoulli numerator of B_{e+1}: 691 for e = 11, from B₁₂ = −691/2730, and 3617 for e = 15, from B₁₆ = −3617/510.
  - Interpretation: this is the r = e+1 Bernoulli term of the u₂-edge, ea_{e+1}·m^{−e} with m = 3s/g.
- **Monomial prefactors.** For 1 ≤ j ≤ (e+1)/2, σ_{e,2j} = const·s^{(e+1)/2−j}·(s−2)^j·(s−8)^{μ_j}·φ_{e,j}(s), with:
  - μ_j = 0 for 2j ≥ (e+1)/2+2, and μ_j = 2((e+1)/2 − 2j) + 2 … 
  - concretely for e = 15: (s−8)², (s−8)⁶, (s−8)¹⁰, (s−8)¹⁴ at g⁸, g⁶, g⁴, g²;
  - the (s−8) powers come from b = (s−8)/g.
- **Pairing.** The irreducible factors pair up: σ_{e,2j} and σ_{e,2j′} with 2j + 2j′ = (e+1) + 2 share the same irreducible cofactor. For e = 15:
  - 5s² − 24s + 64 is shared by g¹⁴ and g⁴;
  - 39s⁴ − 520s³ + … by g¹² and g⁶;
  - 715s⁶ − … by g¹⁰ and g⁸.
  - The same holds for e = 11 and e = 13.
- **g⁰ coefficient.** σ_{e,0} = s^{(e+1)/2}·(an irreducible polynomial of degree e+1).

The general pattern for all e is a **Cat B observation** (seen at e = 11, 13, 15, plus e = 17 once available). I have not proved it.

### G.0 Correction to G.2

In G.2, the bullet on μ_j is garbled. The correct exponent of (s−8) in σ_{e,2j} is **μ_j = max(0, e + 3 − 4j)**. It holds at e = 11, 13, 15, 17.

### G.1 (result) t^{17/2} at x = 0 (Cat A; numerics Cat B)

**Run.** The checkpointed run `sym_engine_K17.py` stalled once while the box was being snapshot-restored. I restarted it from `e17_ckpt.pkl`, which holds all 19 edge terms (i = 0..18) plus the area term. It then wrote `sym_universal_P1_K17.pkl`. Peak memory was about 130 MB.

**Closed form** (`closed_forms_K17.py` → `closed_P1_K17.log/.json`, `closed_P1_e17_K17.pkl`). **The R + S√Δ split persists at t^{17/2}**: it is unique at every sample s, and both interpolants pass exact checks at 10 held-out values of s.

  R₁₇ = −(s−4)(4849845s¹⁷ − 139775079348190s¹⁶ + 4391653076651984s¹⁵ − 64485995190114784s¹⁴ + 587401536016337504s¹³ − 3714939847797673024s¹² + 17295972435926054144s¹¹ − 61318189806712178176s¹⁰ + 168842316810232253696s⁹ − 364897146815430053376s⁸ + 620945503623155695616s⁷ − 829144581888081657856s⁶ + 859500612187255734272s⁵ − 677947939703511580672s⁴ + 393271495268941955072s³ − 158191900792352407552s² + 39411813310930092032s − 4580182201382993920)/(472422714097375641600(s−2)¹⁰).

S₁₇ is in the JSON. The (s−4) factor reappears in R at e = 9, 13, 17, i.e. e ≡ 1 mod 4.

**Exact checks** (`check_K17_quick.py` → `check_K17_quick.json`):
- c₁₇(5) = 0.
- The e ≤ 13 coefficients agree with the independent K13 run, with difference 0 at 60 digits. (The e ≤ 15 entries of the K17 pickle are inherited from K15 by construction, so I compared against the independent run instead.)

**Independent engine** (`check_K17.py` → `check_K17.log`): exact agreement at double precision for s = 6. The s = 7 and 9 rows were still being computed when this was written and will be appended to the log.

**60-digit direct sums (Cat B; `numerics_mp_K17.py`, `run_numerics_K17.sh` → `numerics_K17_{I,J,K}.jsonl`).** The expansion through t^{13/2} is subtracted:

| s | rel. err. c₁₅ | rel. err. c₁₇ |
|---|---|---|
| 20 | 2.6e−14 | 3.5e−10 |
| 32 | 1.2e−12 | 6.1e−9 |
| 8 | 3.0e−8 | 1.2e−5 |

### G.3 S₁₇ structure (`S_structure_with17.txt`)

The G.2 patterns all hold at e = 17 (exact factorization; **the general pattern remains a Cat B observation**):
- Only even powers of g occur, up to g¹⁸.
- The top coefficient is 43867(s−2)⁹/296528117760. Here 43867 is the numerator of B₁₈ = 43867/798.
- σ_{17,2j} = const·s^{9−j}·(s−2)^j·(s−8)^{max(0, 20−4j)}·φ_j.
- The cofactors pair as (g¹⁶, g⁴), (g¹⁴, g⁶) and (g¹², g⁸); g¹⁰ is self-paired.
- σ_{17,0} = s⁹·(an irreducible polynomial of degree 18).

### G.4 Universal-piece identity: frozen R_e vs the axes S^ax_e (Cat A, exact)

`compare_axes.py` → `compare_axes.json/.log` compares exactly the frozen x = 0 rational part R_e from this folder with S^ax_e from `../2026-10-18-Algebraic-Round3/c7/axes_RS_forms.json`. For e = 7 and 9, R_e was recomputed from the K13 pickle by `closed_forms_K13_low.py` → `closed_P1_e{7,9}_lowK13.pkl`.

**Result: R_e − S^ax_e = 0 exactly for e = 7, 9, 11, 13**, i.e. t^{7/2} through t^{13/2}. So the identity "frozen rational part = axes S-part" holds through t^{13/2}. (By contrast, R_e ≠ R^ax_e, as expected.)

Comparing at t^{15/2} and t^{17/2} would need the axes forms at K ≥ 15, which do not exist yet.

### Round 4 status

| item | result | category |
|---|---|---|
| t^{17/2} at x = 0 | R₁₇ + S₁₇√Δ; split, 10 held-out checks, s = 5 vanishing, lower orders | A |
| t^{17/2}, engine match | s = 6 done; s = 7, 9 still running | A-level consistency |
| t^{17/2}, numerics | 3 values of s | B |
| S_e structure | exact factorizations at e = 11..17; the general pattern is not proved | A per e; pattern B |
| frozen R vs axes S | equal exactly at e = 7..13 | A |
