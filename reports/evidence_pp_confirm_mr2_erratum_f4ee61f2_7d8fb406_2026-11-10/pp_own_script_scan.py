# PP scan of PP's own independent-check script for forbidden tokens / float literals / MR2 imports.
import re, ast, hashlib
fn = 'pp_independent_checks.py'
src = open(fn, 'rb').read(); txt = src.decode()
print("SCRIPT_SHA256", hashlib.sha256(src).hexdigest(), fn)
code = "\n".join(l.split('#')[0] for l in txt.splitlines())
ok = True
for tok in ['nsimplify', 'simplify(', 'numpy', 'allclose', 'evalf', 'float(', 'Float', 'mpmath', 'mr2_', 'import mr2', 'riemann_at_point']:
    hits = [m.start() for m in re.finditer(re.escape(tok), code)]
    if tok == 'simplify(':
        hits = [h for h in hits if not code[max(0, h-1):h].isalpha()]
    print(("PASS " if not hits else "FAIL ") + f"no code use of {tok!r} ({len(hits)} hits)"); ok &= not hits
fl = [n.value for n in ast.walk(ast.parse(txt)) if isinstance(n, ast.Constant) and isinstance(n.value, float)]
print(("PASS " if not fl else "FAIL ") + "no float literals in AST"); ok &= not fl
print("ALL_CHECKS", "PASS" if ok else "FAIL")
