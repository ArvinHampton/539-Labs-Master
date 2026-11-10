"""Build PureEven_MultiK_v2.pdf from v2.md:  Markdown -> HTML (python-markdown, md_in_html, tables),
math rendered with KaTeX (node; install with `npm install katex` in $KATEX_DIR), HTML -> PDF with headless Chrome.
LaTeX was not available on the build machine, hence this route.  Intermediate HTML goes to $BUILD_DIR (default /tmp/kt/build)."""
import os, re, json, subprocess, sys, html
import markdown
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
KATEX_DIR = os.environ.get("KATEX_DIR", "/tmp/kt"); BUILD = os.environ.get("BUILD_DIR", "/tmp/kt/build")
os.makedirs(BUILD, exist_ok=True)
src = open(os.path.join(ROOT, "v2.md"), encoding="utf-8").read()
maths = []
def stash(m, display):
    maths.append((m.group(1), display)); return f"@@MATH{len(maths)-1}@@"
src = re.sub(r"\$\$(.+?)\$\$", lambda m: stash(m, True), src, flags=re.S)
src = re.sub(r"\$(.+?)\$", lambda m: stash(m, False), src, flags=re.S)
json.dump([{"t": t, "d": d} for t, d in maths], open(os.path.join(BUILD, "math.json"), "w"))
subprocess.run(["node", "-e", """
const k=require('%s/node_modules/katex'),fs=require('fs');
const a=JSON.parse(fs.readFileSync('%s/math.json'));
const o=a.map(x=>k.renderToString(x.t,{displayMode:x.d,throwOnError:true,output:'html'}));
fs.writeFileSync('%s/math_out.json',JSON.stringify(o));""" % (KATEX_DIR, BUILD, BUILD)], check=True)
rendered = json.load(open(os.path.join(BUILD, "math_out.json")))
body = markdown.markdown(src, extensions=["tables", "md_in_html", "sane_lists"])
body = re.sub(r"@@MATH(\d+)@@", lambda m: rendered[int(m.group(1))], body)
# proofs end with a QED box (already via \blacksquare in text); wrap tables for page breaks
css = open(os.path.join(HERE, "paper.css")).read()
doc = f"""<!doctype html><html><head><meta charset="utf-8"><title>Pure-Even Multi-k Families and the Arithmetic Core of Resonant Algebra</title>
<link rel="stylesheet" href="file://{KATEX_DIR}/node_modules/katex/dist/katex.min.css"><style>{css}</style></head><body>{body}</body></html>"""
open(os.path.join(BUILD, "v2.html"), "w", encoding="utf-8").write(doc)
pdf = os.path.join(ROOT, "PureEven_MultiK_v2.pdf")
subprocess.run(["google-chrome", "--headless=new", "--no-sandbox", "--disable-gpu", "--allow-file-access-from-files",
                "--no-pdf-header-footer", f"--print-to-pdf={pdf}", f"file://{BUILD}/v2.html"], check=True, timeout=180)
print("wrote", pdf)
