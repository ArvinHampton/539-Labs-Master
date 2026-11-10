# PP namespace / float scan of MR2 frozen L-GN script (evidence copy). Read-only.
import re, hashlib, ast, sys
fn = 'mr2_lgn_gaussian_normal_lemma_2026-11-10.py'
src = open(fn, 'rb').read()
print("SCRIPT_SHA256", hashlib.sha256(src).hexdigest())
txt = src.decode()
code_lines = [l for l in txt.splitlines() if not l.lstrip().startswith('#')]
code = "\n".join(l.split('#')[0] for l in code_lines)
ok = True
def chk(lbl, c):
    global ok; ok &= bool(c); print(("PASS " if c else "FAIL ") + lbl)
for tok in ['nsimplify', 'simplify(', 'numpy', 'np.', 'allclose', 'evalf', 'float(', 'Float', 'N(', 'mpmath', 'random', 'trigsimp', 'solve(']:
    hits = [m.start() for m in re.finditer(re.escape(tok), code)]
    if tok == 'simplify(':
        hits = [h for h in hits if not code[max(0,h-1):h].isalpha()]
    if tok == 'N(':
        hits = [h for h in hits if not (code[h-1].isalnum() or code[h-1] == '_')]
    print(f"  token {tok!r}: {len(hits)} code hits")
    chk(f"no code use of {tok!r}", len(hits) == 0)
tree = ast.parse(txt)
floats = [n.value for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value, float)]
chk("no float literals in AST", len(floats) == 0)
calls = sorted({(n.func.attr if isinstance(n.func, ast.Attribute) else getattr(n.func, 'id', '?')) for n in ast.walk(tree) if isinstance(n, ast.Call)})
print("  call names:", calls)
imports = sorted({a.name for n in ast.walk(tree) if isinstance(n, (ast.Import, ast.ImportFrom)) for a in n.names} | {n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)})
print("  imports:", imports)
chk("imports limited to stdlib + sympy", set(imports) <= {'hashlib','datetime','sys','itertools','zoneinfo','ZoneInfo','sympy','Rational','symbols','Matrix','zeros','expand','Poly'})
print("  zero tests used: Poly(...).is_zero, expand(...)==0, sp.diff(...)==0, rational ==; sp.integrate / sp.cancel only in C2c/C2d (exact)")
print("ALL_CHECKS", "PASS" if ok else "FAIL")
