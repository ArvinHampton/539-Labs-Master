import re,os,sys,json,collections
C=sys.argv[1]
pats={'Q4_syn':r'\bgap ?[57]\b|bridge force|non-?local force|force coupling|geo(metric)?\s*(→|->|to)\s*alg|residual map',
'f_star':r'f_\*|f_\{\*\}|\bf_star\b|friction factor|f\(Ω|f_Ω|f_\{?Omega',
'H_model':r'Hamiltonian|\bĤ\b|\bH\s*=\s*[^0-9\s]|H_\{?(int|NL|eff|11D)',
'psi_state':r'wave ?function|\|ψ⟩|\|psi>|ψ\(|psi\(|state vector',
'rhoU':r'ρ₊₋|rho_\+-|ρ_\{\+-\}|ρ\+-',
'Trrho_tau':r'Tr ?ρ|Tr\(ρ\)|e\^\{?−\|Δt\||exp\(-\|Δt\|',
'ER_EPR':r'ER ?= ?EPR','Phi_y':r'Φ\(y\)|Phi\(y\)'}
h=collections.defaultdict(list)
for fn in sorted(os.listdir(C)):
  role=None
  for i,l in enumerate(open(os.path.join(C,fn),errors='ignore'),1):
    m=re.match(r'=== \[.*?\] (human|assistant) ',l)
    if m: role=m.group(1);continue
    if role!='human':continue
    for k,p in pats.items():
      if re.search(p,l,re.I): h[k].append(f'{fn}:{i}: {l.strip()[:200]}')
for k in pats: print(k,len(h[k]))
json.dump(h,open(sys.argv[2],'w'),ensure_ascii=False,indent=0)
