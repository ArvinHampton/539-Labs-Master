import re,sys
U={'§':r'\S{}','−':'-','√':r'$\surd$','≈':r'$\approx$','≥':r'$\geq$','≤':r'$\leq$','≡':r'$\equiv$','²':r'$^2$','³':r'$^3$','±':r'$\pm$','—':'---','–':'--','→':r'$\to$','×':r'$\times$','≠':r'$\neq$','ε':r'$\varepsilon$','ν':r'$\nu$','β':r'$\beta$','γ':r'$\gamma$','ρ':r'$\rho$','ψ':r'$\psi$','α':r'$\alpha$','χ':r'$\chi$','Δ':r'$\Delta$','τ':r'$\tau$','φ':r'$\varphi$','ħ':r'$\hbar$','Λ':r'$\Lambda$','κ':r'$\kappa$','ζ':r'$\zeta$','σ':r'$\sigma$','μ':r'$\mu$','Ω':r'$\Omega$','₃':r'$_3$','⁷':r'$^7$','·':r'$\cdot$','…':r'\ldots{}','“':"``",'”':"''",'’':"'",'Π':r'$\Pi$','δ':r'$\delta$','π':r'$\pi$'}
def esc(s):
  codes=[]
  s=re.sub(r'`([^`]*)`',lambda m:(codes.append(m.group(1)),f'\x00{len(codes)-1}\x00')[1],s)
  s=s.replace('\\',r'\textbackslash{}')
  for a,b in [('&',r'\&'),('%',r'\%'),('#',r'\#'),('_',r'\_'),('^',r'\^{}'),('~',r'\~{}'),('{',r'\{'),('}',r'\}')]: 
    s=s.replace(a,b) if a not in '{}' else s
  s=s.replace('\\_','\x01').replace('_',r'\_').replace('\x01',r'\_')
  s=re.sub(r'\*\*(.+?)\*\*',r'\\textbf{\1}',s)
  for k,v in U.items(): s=s.replace(k,v)
  s=re.sub(r'\x00(\d+)\x00',lambda m:r'\texttt{'+esc_code(codes[int(m.group(1))])+'}',s)
  s=re.sub(r'(https?://\S+?)([),.]?(\s|$))',lambda m:r'\url{'+m.group(1).replace(r'\_','_').replace(r'\%','%').replace(r'\#','#')+'}'+m.group(2),s)
  return s
def esc_code(c):
  c=c.replace('\\',r'\textbackslash{}')
  for a,b in [('_',r'\_'),('&',r'\&'),('%',r'\%'),('#',r'\#'),('^',r'\^{}')]: c=c.replace(a,b)
  for k,v in U.items(): c=c.replace(k,v)
  return '/\\allowbreak '.join(c.split('/')) if len(c)>30 else c
L=open(sys.argv[1]).read().split('\n')
o=[r'\documentclass[10pt]{article}\usepackage[margin=0.8in]{geometry}\usepackage{amssymb,longtable,array,url,hyperref}\usepackage[T1]{fontenc}\usepackage{lmodern}\sloppy\begin{document}']
depth=0;i=0
while i<len(L):
  l=L[i]
  if l.startswith('|'):
    rows=[]
    while i<len(L) and L[i].startswith('|'):
      if not re.match(r'^\|[-|]+\|$',L[i]): rows.append([esc(c.strip()) for c in L[i].strip('|').split('|')])
      i+=1
    o.append(r'{\small\begin{longtable}{p{0.04\linewidth}p{0.36\linewidth}p{0.44\linewidth}p{0.08\linewidth}}\hline')
    o.append(' & '.join(r'\textbf{'+c+'}' for c in rows[0])+r'\\\hline\endhead')
    for r in rows[1:]: o.append(' & '.join(r)+r'\\\hline')
    o.append(r'\end{longtable}}'); continue
  m=re.match(r'^( *)(- |\d+\. )',l)
  lvl=(len(m.group(1))//2+1) if m else 0
  while depth>lvl: o.append(r'\end{itemize}'); depth-=1
  while depth<lvl: o.append(r'\begin{itemize}'); depth+=1
  if l.startswith('# '): o.append(r'\begin{center}{\Large\bfseries '+esc(l[2:])+r'}\end{center}')
  elif l.startswith('## '): o.append(r'\section*{'+esc(l[3:])+'}')
  elif l.startswith('### '): o.append(r'\subsection*{'+esc(l[4:])+'}')
  elif m: o.append(r'\item '+esc(l[m.end():]))
  else: o.append(esc(l))
  i+=1
o+= [r'\end{itemize}']*depth
o.append(r'\end{document}')
open(sys.argv[2],'w').write('\n'.join(o))
