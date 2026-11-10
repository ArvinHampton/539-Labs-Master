# Edits applied to the COPIES of Bridge C Clean v2 tex in src/partII (sources untouched).
import re,glob,os
d='src/partII/'
log=[]
for f in sorted(glob.glob(d+'s*.tex')):
    s=open(f).read(); o=s
    s=re.sub(r'(?<![-\w{])P_s(?![A-Za-z-])',r'\\Porth_s',s)
    s=s.replace(r'\begin{propKone}',r'\begin{proposition}[K1]').replace(r'\end{propKone}',r'\end{proposition}')
    s=s.replace(r'\begin{cfp}',r'\begin{proposition}[CRT Factorization Proposition]').replace(r'\end{cfp}',r'\end{proposition}')
    if s!=o: log.append(f+': %d P_s renamed'%len(re.findall(r'\\Porth_s',s)))
    open(f,'w').write(s)
print('\n'.join(log))
# preamble -> strip to macros only; intro -> remove abstract/title/toc
s=open(d+'s00_preamble.tex').read()
mac=s[s.index(r'\newcommand{\Q}'):s.index(r'\title')]
open(d+'s00_macros.tex','w').write(mac)
s=open(d+'s01_intro.tex').read()
s=s[s.index(r'\tableofcontents')+len(r'\tableofcontents'):]
s=s.replace(r'\section{Introduction}\label{sec:intro}',r'\section{Introduction to Part~II}\label{sec:intro}')
s=s.replace('The paper is self-contained.','This part is self-contained.')
s=s.replace('nothing in it depends on','nothing in it depends on')
s=s.replace('Nothing in the paper has been externally refereed.','')
open(d+'s01_intro.tex','w').write(s)
b=open(d+'s26_bib.tex').read()
b=b.replace(r'\end{document}','')
open(d+'s26_bib.tex','w').write(b)
