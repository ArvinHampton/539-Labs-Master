# Local-derived. gen_followup2b = gen_followup2 with the verdict logic fixed: a line counts as a hit only if the FINAL
# eigenspace (after the T(37^2) filter when it ran) is nonzero. (gen_followup2 would have mis-read D = 8's '-4: 2 -> after T(37^2) ...: 0'.)
# Second follow-up: records the finished s1e (Oc-2, level 784) result. Run ONLY after s1e (PID 932685) has exited.
# Writes FOLLOWUP2_LOCAL_t4436_BRANCHES_S1E_784_RESULT_<YYYY-MM-DD>_<HHMM>.md (+ sidecar) and a NEW final sidecar for the s1e log
# (s1e_oc2_small_levels_p11.log.final.sha256; no earlier sidecar file exists for the log). Refuses to overwrite anything.
import os, hashlib, datetime, subprocess, re
EV='evidence_local_t4436_branches_2026-11-09'
os.chdir('/workspace/quantum-comp/reports')
assert subprocess.run(['pgrep','-f','s1e_oc2_small_levels_p11.py'],capture_output=True).returncode!=0, 's1e still running'
def sha(p): return hashlib.sha256(open(p,'rb').read()).hexdigest()
now=datetime.datetime.now()
OUT=f'FOLLOWUP2_LOCAL_t4436_BRANCHES_S1E_784_RESULT_{now:%Y-%m-%d_%H%M}.md'
LOG=f'{EV}/s1e_oc2_small_levels_p11.log'; SC=LOG+'.final.sha256'
for p in (OUT,OUT+'.sha256',SC): assert not os.path.exists(p)
tip=sha('/workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md'); assert tip=='7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91'
F1=[f for f in os.listdir('.') if f.startswith('FOLLOWUP_LOCAL_t4436_BRANCHES_S1E_784_AND_PP_eb722a79_FIXES_')and f.endswith('.md')]
f1sha=sha(F1[0])
lines=open(LOG).read().splitlines(); l784=[l for l in lines if l.startswith('level 784')]
h=sha(LOG); open(SC,'x').write(f'{h}  s1e_oc2_small_levels_p11.log\n')
def info(D):
    for l in l784:
        if re.match(rf'level 784, char {D}:',l): return l
    return None
need=[8,28,56]; res={D:info(D) for D in need}
done=all(res[D] for D in need)
def final_dim(l):
    if 'dim 0' in l: return 0
    m=re.search(r'after T\(37\^2\) \(a_37\(Xi\)=\+6\): (\d+)',l)
    if m: return int(m.group(1))
    return int(re.search(r'a_11\(Xi\) = -4: (\d+)',l).group(1))
hit=[D for D in need if res[D] and final_dim(res[D])>0]
if done and not hit:
    verdict=('**[PROVED, new; PARI base]** No Oc-2 vector at level 784 for any admissible quadratic character D ∈ {1, −4, 8, −8, −7, 28, −56, 56}: '
             'in every nonzero space the joint eigenspace for a₁₁(Ξ) = −4 (T(121)) and a₃₇(Ξ) = +6 (T(37²)) is 0 (s1e; for D = 8 the T(121) eigenspace has dimension 2 and is killed by T(37²); for D = 1, 28 and 56 already T(121) gives 0 unless the line says otherwise), and the spaces for −4, −8, −7, −56 are 0 (s1e, s12). '
             'The Oc-2 784 row moves PENDING → PROVED (a non-existence statement at 784). Oc-2 itself stays OPEN (alive): its vector is expected only at higher level (COND T-Wald, level 78400), and 1568/3136/6272 belong to the O-b stream.')
    tally='Proposed, for PP to rule: 96 rows, PROVED 64 · CONDITIONAL 17 · OPEN 5 · REFUTED 9 · PENDING 1 (Oc-2 784 row PENDING → PROVED; J-2 9800 still PENDING).'
elif hit:
    verdict=f'**Nonzero −4 eigenspace found for D ∈ {hit}** (see lines). The 784 row is not a non-existence result; the candidate eigenspace needs the T(37²) filter recorded in the line and a PP audit. Grade: OPEN with a candidate, PP to rule.'
    tally='No grade change proposed until PP rules on the candidate. Ruled tally (eb722a79) stands: 63 / 17 / 5 / 9 / 2.'
else:
    verdict='s1e exited without a line for every remaining character (see log); the missing characters stay PENDING.'
    tally='Ruled tally (eb722a79) stands: 63 / 17 / 5 / 9 / 2.'
T=f'''# FOLLOW-UP 2 (Local-derived): Oc-2 at level 784, final s1e result, {now:%Y-%m-%d %H:%M} CST (America/Chicago)

- Additive; follows {F1[0]} (sha {f1sha}). Nothing earlier is edited. Nothing adopted (Owner t4436). Tip {tip} unchanged.
- Date note: the first follow-up was written 2026-11-10 00:32 CST; its file name and header say 2026-11-09 (generator slip). It stays as filed.

## s1e level-784 lines (all)
{chr(10).join('- '+l for l in l784)}

- s12 dims: 36 (1), 0 (−4), 42 (8), 0 (−8), 0 (−7), 34 (28), 0 (−56), 41 (56).
- s1e log final sha256: {h}; new sidecar s1e_oc2_small_levels_p11.log.final.sha256 (26a7c91e's at-filing sha 9228c983… stays as filed).

## Verdict
{verdict}

- Check values (PARI, this run's base): a₁₁(49a1) = 4, a₃₇(49a1) = −6, χ₁₄₀(11) = χ₁₄₀(37) = −1, so a₁₁(Ξ) = −4 and a₃₇(Ξ) = +6 (ellap on elltwist(E,140), conductor 19600). By the Shimura correspondence the T(p²)-eigenvalue of an Oc-2 vector is a_p(Ξ); T(121) and T(37²) commute, so the T(121) eigenspace is T(37²)-stable and the filter is exact.

## Tally
{tally}
J-2 9800: PENDING (other stream, s2e; not started by Local).
'''
open(OUT,'x').write(T); hh=sha(OUT); open(OUT+'.sha256','x').write(f'{hh}  {OUT}\n'); print(OUT,hh)
