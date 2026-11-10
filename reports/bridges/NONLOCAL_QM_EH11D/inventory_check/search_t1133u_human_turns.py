import re,os,sys,collections
pats={'f_star':r'f_\*|f_\{\*\}|\bf_star\b|f\*\s*=','eps_S8':r'ε_?S8|epsilon_?S8|eps_?S8|ε_\{S8\}','delta_t':r'δ\(t\)|delta\(t\)','dt11D':r'Δt_?\{?11D|Delta ?t_?11D','H0':r'\bH_?0\s*=|\bH₀\s*=','psi_coef':r'\bψ\s*=\s*[0-9]','tau_ent':r'τ_?\{?ent|tau_ent','233.38':r'233\.38','GMc3':r'GM/c\^?3|GM/c³','Omega11':r'Ω_?\{?11D|Omega_?11D|Ω₁₁D','Q4gap':r'gap ?5|gap ?7','Phi_y':r'Φ\(y\)|Phi\(y\)','Trrho':r'Tr ?ρ|Tr\(ρ\)'}
hits=collections.defaultdict(list)
for fn in sorted(os.listdir('chats')):
  role=None;
  for i,l in enumerate(open('chats/'+fn,errors='ignore'),1):
    m=re.match(r'=== \[.*?\] (human|assistant) ',l)
    if m: role=m.group(1);continue
    if role!='human':continue
    for k,p in pats.items():
      if re.search(p,l,re.I if k in('H0',) else 0): hits[k].append(f'chats/{fn}:{i}: {l.strip()[:220]}')
for k in pats: print(k,len(hits[k]))
import json;json.dump(hits,open('/tmp/hhits.json','w'),ensure_ascii=False,indent=0)
