# Convert PAPER_gk_v1/PAPER.md (read-only) into LaTeX for Part I, renumbering sections by OFFSET.
import re, subprocess, sys
OFF=2
src=open('/workspace/quantum-comp/reports/s_family_paths/PAPER_gk_v1/PAPER.md').read()
lines=src.split('\n')
# drop title block (up to line 12) ; split appendices/references
body='\n'.join(lines[12:])
main,rest=body.split('## Appendix A. Computational reproduction',1)
appA,rest=rest.split('## References',1)
refs,appB=rest.split('## Appendix B. Zero sets',1)
tags=set(re.findall(r'\\tag\{(\d+\.\d+)\}',src))
def rn(x):  # "6.3.1" -> shifted
    p=x.split('.'); 
    if p[0].isdigit() and 1<=int(p[0])<=7: p[0]=str(int(p[0])+OFF)
    return '.'.join(p)
KW=r'(?:Theorems?|Thms?\.|Lemmas?|Propositions?|Props?\.|Corollar(?:y|ies)|Cor\.|Definitions?|Remarks?|Sections?|Tables?|§)'
ITEM=r'\d+(?:\.\d+)*'
pat=re.compile(r'('+KW+r'\s*)('+ITEM+r'(?:\s*(?:,|–|-|and|/|or|to)\s*(?:'+KW+r'\s*)?'+ITEM+r')*)')
PROT=[('[1, Theorem 1.1]','@@C1@@'),('[1, (3.10)]','@@C2@@'),('[1, Remark 3 after Theorem 1.1]','@@C3@@'),('Chern [1] (Theorem 1.1, error term (3.10), Remark 3)','@@C4@@')]
UNPROT={'@@C1@@':'\\cite[Theorem~1.1]{Chern}','@@C2@@':'\\cite[(3.10)]{Chern}','@@C3@@':'\\cite[Remark~3 after Theorem~1.1]{Chern}','@@C4@@':'Chern \\cite{Chern} (Theorem~1.1, error term (3.10), Remark~3)'}
def fix(t):
    for a,b in PROT: t=t.replace(a,b)
    def r1(m):
        return m.group(1)+re.sub(ITEM,lambda k:rn(k.group(0)),m.group(2))
    t=pat.sub(r1,t)
    t=re.sub(r'\\tag\{(\d+\.\d+)\}',lambda m:'\\tag{'+rn(m.group(1))+'}',t)
    t=re.sub(r'\((\d\.\d+)\)',lambda m:'('+rn(m.group(1))+')' if m.group(1) in tags else m.group(0),t)
    t=re.sub(r'\[1\]',r'\\cite{Chern}',t); t=re.sub(r'\[2\]',r'\\cite{Arb}',t)
    # headings: strip numbers
    t=re.sub(r'^(#+) (?:\d+(?:\.\d+)*\.?|[AB]\.\d+) ',r'\1 ',t,flags=re.M)
    t=t.replace('<div class="thm" markdown="1">','\n::: thm\n').replace('<div class="proof" markdown="1">','\n::: proof\n').replace('</div>','\n:::\n')
    return t
def pandoc(md):
    pass
    r=subprocess.run(['pandoc','-f','markdown+tex_math_dollars+raw_tex+pipe_tables+fenced_divs','-t','latex','--shift-heading-level-by=-1','--wrap=preserve'],input=md,capture_output=True,text=True,check=True).stdout
    for a,b in UNPROT.items(): r=r.replace(a,b)
    return r
summary,mainrest=main.split('\n## 1. Definitions',1); mainrest='1. Definitions'+mainrest
out=pandoc(fix(summary.replace('### Summary of results','#### Summary of Part I')) )
out2=pandoc(fix('## '+mainrest))
apA=pandoc(fix('## Computational reproduction for Part I'+appA))
apB=pandoc(fix('## Zero sets of $g_k$'+appB))
d='/workspace/quantum-comp/reports/papers/RTA_FOUNDATION_BOUND/src/partI/'
open(d+'p1_summary.tex','w').write(out); open(d+'p1_body.tex','w').write(out2)
open(d+'p1_appA.tex','w').write(apA); open(d+'p1_appB.tex','w').write(apB)
print(sorted(tags))
# --- layout post-processing of four wide displays (content unchanged) ---
b=open(d+'p1_body.tex').read()
R=[(r"\[g(n)=E(n)+\sum_{\ell\in L_{>0}}2\pi\Delta_4(\ell)\Bigl(\frac{24n+\Delta_2}{\Delta_3(\ell)}\Bigr)^{-\frac{\Delta_1+1}{2}}",
    r"\begin{multline}g(n)=E(n)+\sum_{\ell\in L_{>0}}2\pi\Delta_4(\ell)\Bigl(\frac{24n+\Delta_2}{\Delta_3(\ell)}\Bigr)^{-\frac{\Delta_1+1}{2}}\\"),
   (r"e\!\left(-\frac{nh}{k}\right),\tag{6.2}\]", r"e\!\left(-\frac{nh}{k}\right),\tag{6.2}\end{multline}"),
   (r"\[|E(n)|\le\frac{N^2}{\pi\nu}e^{2\pi\varrho\nu}\!\!\sum_{\ell\in L_{>0}}\!e^{\pi\Delta_3(\ell)/3}+2e^{2\pi\varrho\nu}\Bigl\{",
    r"\begin{multline}|E(n)|\le\frac{N^2}{\pi\nu}e^{2\pi\varrho\nu}\!\!\sum_{\ell\in L_{>0}}\!e^{\pi\Delta_3(\ell)/3}\\+2e^{2\pi\varrho\nu}\Bigl\{"),
   (r"}\Bigr)-\!\!\sum_{\ell\in L_{>0}}\!\Delta_4(\ell)e^{\pi\Delta_3(\ell)/24}\Bigr\}.\tag{6.3}\]",
    r"}\Bigr)\Bigr.\\\Bigl.-\!\!\sum_{\ell\in L_{>0}}\!\Delta_4(\ell)e^{\pi\Delta_3(\ell)/24}\Bigr\}.\tag{6.3}\end{multline}"),
   (r"\[Z_{14}=\{2,7,8,11,14,21,22,28,32,35,37,42,44,46,53,56,70,77,84,86,88,98,102,112,126,140,154,168,182,224\},\]",
    r"\begin{multline*}Z_{14}=\{2,7,8,11,14,21,22,28,32,35,37,42,44,46,53,56,70,\\77,84,86,88,98,102,112,126,140,154,168,182,224\},\end{multline*}"),
   (r"+8K_{G},\qquad K_3\ge", r"+8K_{G},\]\[K_3\ge")]
for a,c in R:
    assert b.count(a)==1,(a[:40],b.count(a)); b=b.replace(a,c)
open(d+'p1_body.tex','w').write(b)
a=open(d+'p1_appA.tex').read()
x="The proofs in this paper were rewritten and re-checked against these sources; where the earlier statements differ, this paper's statements are the ones proved."
assert x in a; a=a.replace(x,"The proofs in Part~I were written out and checked against these sources.")
a=a.replace("unchanged copies of the following earlier directories","unchanged copies of the following directories")
open(d+'p1_appA.tex','w').write(a)
