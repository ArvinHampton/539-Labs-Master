#!/usr/bin/env python3
# PP: execute a byte-identical copy of MR2's frozen script (path argv[1]) in-process, then inspect its exact objects:
# (i) no sympy Float anywhere in coef/eR2/cA squares; (ii) nsimplify in E1 is the identity on its (already-rational) inputs;
# (iii) source-level scan: no 'simplify(' other than 'nsimplify(', no float literals in arithmetic, no numpy/allclose/evalf.
import sys, io, runpy, contextlib, hashlib, re, datetime
from zoneinfo import ZoneInfo
print("RUN_START_WALLCLOCK", datetime.datetime.now(ZoneInfo("America/Chicago")).strftime("%Y-%m-%d %H:%M:%S %Z"))
print("SCRIPT_SHA256", hashlib.sha256(open(__file__,'rb').read()).hexdigest())
path=sys.argv[1]; src=open(path).read()
print("TARGET_SHA256", hashlib.sha256(open(path,'rb').read()).hexdigest())
import sympy as sp
ok=True
def chk(l,c):
    global ok; c=bool(c); ok&=c; print(("PASS " if c else "FAIL ")+l)
code=[ln.split('#')[0] for ln in src.splitlines()]
body="\n".join(code)
chk("S1 no bare simplify( call (only nsimplify)", re.findall(r'(?<![n\w])simplify\s*\(', body)==[])
chk("S2 nsimplify appears exactly once (E1 inst)", len(re.findall(r'nsimplify\s*\(', body))==1)
chk("S3 no numpy / allclose / evalf / N( / float(", not re.search(r'numpy|allclose|evalf|\bN\(|float\(', body))
chk("S4 no decimal float literals in code (outside comments/strings)", not re.search(r'(?<![\w.])\d+\.\d+', re.sub(r'"[^"]*"|\'[^\']*\'','',body)))
buf=io.StringIO()
with contextlib.redirect_stdout(buf):
    ns=runpy.run_path(path, run_name="__main__")
print("TARGET_ALL_CHECKS_LINE", [l for l in buf.getvalue().splitlines() if l.startswith("ALL_CHECKS")])
def nofloat(e): return not any(isinstance(x,sp.Float) for x in sp.preorder_traversal(e))
chk("N1 MR2 coef[riem2,ric2,weyl2,gb] and eR2 contain no Float", all(nofloat(ns['coef'][n]) for n in ['riem2','ric2','weyl2','gb']) and nofloat(ns['eR2']))
chk("N2 MR2 cA riem2/ric2/weyl2/Rs contain no Float", all(nofloat(ns['cA'][n]) for n in ['riem2','ric2','weyl2','Rs']))
k=ns['k']; a_=ns['a_']
s_={k[i]:([a_]*4+[0]*6)[i] for i in range(10)}
raw=[sp.expand(ns['coef'][n].subs(s_)) for n in ['riem2','ric2','weyl2','gb']]
chk("N3 E1 inputs to nsimplify are Float-free and nsimplify(x) == x for each (nsimplify is a no-op here)", all(nofloat(x) and sp.nsimplify(x)==x for x in raw))
print("ALL_CHECKS","PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
