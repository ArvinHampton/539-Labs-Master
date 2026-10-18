# rev4 part 5: insert new sections 11-12 and appendix; add \fc macro
p='bridge_c_consolidated_rev4.tex'
t=open(p).read()
def rep(a,b):
    global t
    n=t.count(a); assert n==1,(n,a[:60]); t=t.replace(a,b)
rep(r'\newcommand{\fm}{\mathfrak{m}}', r'\newcommand{\fm}{\mathfrak{m}}'+'\n'+r'\newcommand{\fc}{\mathfrak{c}}')
fam=open('rev4_sec_family.tex').read(); hs=open('rev4_sec_hs.tex').read(); app=open('rev4_app.tex').read()
i=t.index(r'\section{Status and dependencies}')
j=t.rfind('%====',0,i); j=t.rfind('\n',0,j)+1 if t.rfind('%====',0,i)>i-200 else i
t=t[:j]+fam+'\n'+hs+'\n'+t[j:]
k=t.index(r'\section*{Source reports}')
k2=t.rfind('%====',0,k)
if k2>k-200: k=t.rfind('\n',0,k2)+1
t=t[:k]+app+'\n'+t[k:]
open(p,'w').write(t); print('ok')
# (applied after first build attempt) inline dims_table.tex: \input inside tabular breaks \bottomrule
t=open(p).read(); d=open('dims_table.tex').read().rstrip('\n')
if r'\input{dims_table.tex}' in t:
    t=t.replace(r'\input{dims_table.tex}',d); open(p,'w').write(t)
