# Local-derived. Generator for FOLLOWUP_LOCAL_t4436_BRANCHES_S1E_784_AND_PP_eb722a79_FIXES_2026-11-09_<HHMM>.md. Refuses to overwrite.
import os, hashlib, datetime, re, subprocess
EV='evidence_local_t4436_branches_2026-11-09'
os.chdir('/workspace/quantum-comp/reports')
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
now=datetime.datetime.now(); hhmm=now.strftime('%H%M')
OUT=f'FOLLOWUP_LOCAL_t4436_BRANCHES_S1E_784_AND_PP_eb722a79_FIXES_2026-11-09_{hhmm}.md'
assert not os.path.exists(OUT) and not os.path.exists(OUT+'.sha256')
chk={'FINDINGS_LOCAL_t4436_ALL_MENU_BRANCHES_2026-11-09_2224.md':'26a7c91e218e6a0c',
     'ERRATUM_LOCAL_t4436_BRANCHES_26a7c91e_PP_AUDIT_FIXES_2026-11-09_2302.md':'ab20f7ca7e234e88',
     'FINDINGS_PP_AUDIT_LOCAL_ERRATUM_ab20f7ca_2026-11-09_2305.md':'eb722a79fe11f624'}
for f,p in chk.items(): assert sha(f).startswith(p), f
TIP='/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md'; tip=sha(TIP)
assert tip=='7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91'
L=open(f'{EV}/s10c_alpha_gb1_highdeg_certificates.log').read().splitlines()
ncert=sum(1 for l in L if l.startswith('CERT ')); nno=sum(1 for l in L if l.startswith('NO CERT'))
summ=[l for l in L if l.startswith('third pass:')]
running=subprocess.run(['pgrep','-f','s10c_alpha_gb1_highdeg'],capture_output=True).returncode==0
guard=open('/tmp/s10c_memguard.txt').read().strip() if os.path.exists('/tmp/s10c_memguard.txt') else ''
if summ: state='finished normally (summary line present).'
elif running: state='still running at filing time; counts are from the log so far.'
elif guard: state='stopped by Local\'s memory guard to protect the other stream\'s ob_v3 job ('+guard+').'
else: state='stopped by its own 6000 s `timeout` before finishing the list (the log has no summary line). The unreached jobs are the 6-variable ones.'
tried=ncert+nno; unreached=146-tried
tot=144+ncert; rest=290-tot
s1e=open(f'{EV}/s1e_oc2_small_levels_p11.log').read().splitlines()
s1e784=[l for l in s1e if l.startswith('level 784')]
s1e_run=subprocess.run(['pgrep','-f','s1e_oc2_small_levels_p11.py'],capture_output=True).returncode==0
newf=[f for f in ['s10c_alpha_gb1_highdeg_certificates.py','s10c_alpha_gb1_highdeg_certificates.log','s10c_alpha_gb1_highdeg_certificates.txt','s12_oc2_784_cusp_dims.py','s12_oc2_784_cusp_dims.log','gen_followup1_t4436.py'] if os.path.exists(f'{EV}/{f}')]
rows='\n'.join(f'| {f} | {sha(EV+"/"+f)} |' for f in newf)
T=f'''# FOLLOW-UP (Local-derived) to 26a7c91e + erratum ab20f7ca: PP eb722a79 fixes (C2′, CNF′), A1′ certificates, Oc-2 level 784 status, 2026-11-09 {now.strftime('%H:%M')} CST (America/Chicago)

- **Status:** additive. 26a7c91e and ab20f7ca are not edited. This file supersedes only the wording named below.
- **Audit answered:** FINDINGS_PP_AUDIT_LOCAL_ERRATUM_ab20f7ca_2026-11-09_2305.md (sha eb722a79fe11f624f4cb12792d16d6be042ae43240fba06f74e9c7a1796f4479, recomputed; matches its sidecar). PP accepted all of ab20f7ca. **Ruled tally: 96 rows, PROVED 63 · CONDITIONAL 17 · OPEN 5 · REFUTED 9 · PENDING 2**, with c-2 PROVED.
- **Discipline:** Owner t4436, "Let the math lead the pursuits on all open paths". Every menu candidate stays a labelled branch. **Nothing is adopted.** A citation alone never makes a claim PROVED (OW 36683379). "Resonant algebra" is used throughout; RTA appears only as a historical alias.
- **Rules kept:**
  - Additive files only. Nothing was deleted, renamed, moved or overwritten; s9b is not edited.
  - No CERT, nothing sent outside. The other stream's files and its ob_v3 job were not touched.
  - J-2 at 9800 was **not** started; it will be run as s2e by the other stream.
  - Tip {tip} is unchanged (checked by this generator at write time).

## C2′ (c-2 row, final wording)

> **c-2 [PROVED, PP eb722a79]** For every **odd** q and every n ≥ 1, SO(V) has exactly two orbits on the Lagrangians (n-dimensional totally singular subspaces) of the split 2n-dimensional nondegenerate symmetric bilinear space (V,B) over F_q. Any reflection r_v with B(v,v) ≠ 0 swaps the two orbits. **One SO-orbit has ∏_{{i=1}}^{{n−1}}(q^i+1) members**, and the Codex contour 2∏_{{i=1}}^{{23}}(23^i+1) at (24, 23) equals the number of Lagrangians, i.e. exactly two SO-orbits.

- **q odd is used twice:**
  - in the Witt step, f₁ = x − ½B(x,x)e₁ needs 2 invertible;
  - in the reflection step, v = e₁+f₁ has B(v,v) = 2 ≠ 0.
- **"Family" → "SO-orbit".** Wherever 26a7c91e's c-2 row and ab20f7ca's C2 section say "family" or "the two families", read "SO-orbit" or "the two SO-orbits".
- **The r_v remark is restated as: dim(U ∩ r_vU) = n−1.** U ∩ r_vU ⊇ U ∩ v^⊥, which has dimension ≥ n−1. Also r_vU ≠ U, since otherwise r_v ∈ Stab(U) ⊂ SO.
- **Not claimed:** that an SO-orbit equals a parity class (codim U∩U₀ mod 2). The ab20f7ca sentence "r_v changes dim(U∩gU) parity" is withdrawn as a claim beyond the dimension statement above. The count does not use it.

## CNF′ (cosmetic note on s9b)

- s9b's printout reads "x^2-35y^2=+-5 => … 5u^2-7y^2=+-1; mod 5: **-7y^2=2y^2** in [0, 2, 3]". It should read **−7y² ≡ 3y² (mod 5)**.
- The printed value set {{0, 2, 3}} is correct (3y² mod 5 ∈ {{0, 3, 2}}), and ±1 ≡ {{1, 4}} is not hit, so 𝔭₅ is not principal and h(140) = 2 stands.
- s9b is not edited (its sha is in ab20f7ca §E).

## A1′ (optional: certificates for the 146 remaining GB = [1] jobs; no grade change either way)

**Method (s10c):**
- Target: Σ c_i g_i = P^k (k = 1, 2), with deg c_i ≤ D for D = 4…7.
- The degree is found by a rank test mod 2^61−1. Exact cofactors are then solved over ℚ on the pivot columns, and **each identity is verified by exact sympy.expand**.
- Only verified identities count.

**Run:**
- Status: {state}
- Of the 146 jobs it tried {tried}: **{ncert} certified**, {nno} not certified within D ≤ 7; {unreached} not reached.
- Jobs were ordered by support size (2, 4, 5, then 6 τ-variables).
- Local added a memory guard (kill only if s10c's RSS > 2.5 GB or system available memory < 700 MB) to protect the other stream's ob_v3. {"It fired: " + guard if guard else "It did not fire."}

**Running total of certified GB = [1] jobs:** s10 96 + s10b 48 + s10c {ncert} = **{tot} of 290**. The other **{rest}** verdicts rest on sympy's exact Buchberger, which is disclosed in the computational base.

Grade: α-3 stays **PROVED** (unchanged).

## Oc-2 at level 784 (s1e)

- **s1e status:** {"still running (PID 932685), on character D = 8 since about 22:15 CST" if s1e_run else "finished"}. Lines on record:
{chr(10).join("  - " + l for l in s1e784)}
- **New, s12 (cheap PARI mfdim of the same cuspidal spaces):**
  - dim S_{{3/2}}(Γ₀(784), χ_D) = 36 (D = 1), 0 (−4), 42 (8), **0 (−8)**, **0 (−7)**, 34 (28), **0 (−56)**, 41 (56).
  - D = 1 and −4 agree with s1e.
- **[PROVED, new; PARI base]** There is no Oc-2 vector at level 784 for D ∈ {{1, −4, −8, −7, −56}}: D = 1 has no −4 eigenspace (s1e), and the other four spaces are 0.
- **[PENDING]** D ∈ {{8, 28, 56}} (dims 42, 34, 41) need the T(121) test that s1e is still running. Oc-2 stays OPEN (alive) and its 784 row stays PENDING.
- The final s1e result, the final sha of its log, and a new sidecar for the log will be recorded in a **second follow-up file** when s1e ends.

## J-2 at 9800

PENDING, to be run as s2e by the other stream. Not started by Local.

## Tally

- **PP-ruled (eb722a79): 96 rows, PROVED 63 · CONDITIONAL 17 · OPEN 5 · REFUTED 9 · PENDING 2.**
- This file changes no grade:
  - C2′ and CNF′ are wording only.
  - A1′ adds evidence.
  - At 784, three more characters are settled inside the still-PENDING row.
- Bridge C stays PARTIAL. The PP Bridge C rollup (46/11/5/2/1 + V₈₄, PP 0f1d3361) is separate and unchanged.

## E. New evidence (evidence_local_t4436_branches_2026-11-09/; each file gets a .sha256 sidecar)

| File | sha256 |
|---|---|
{rows}
'''
with open(OUT,'x') as f: f.write(T)
h=sha(OUT)
with open(OUT+'.sha256','x') as f: f.write(f'{h}  {OUT}\n')
print(OUT,h)
