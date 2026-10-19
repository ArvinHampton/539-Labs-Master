import json
D=json.load(open('local_eps.json')); C=json.load(open('compare.json')); M=json.load(open('minpolys.json'))
def f(z): return f"{z[0]:+.6f}{z[1]:+.6f}i"
L=["| χ (k,e,1) | ∞-type | ε_𝔭₂ | ε_𝔭₅ | ε_𝔭₇ | ε_∞₁ε_∞₂ | ∏_v ε_v | W (lfunrootres) | max |∏−W| |","|---|---|---|---|---|---|---|---|---|"]
for r,row in zip(D['results'],C['per_char']):
    k,e,_=r['chi']
    if k>=12: continue
    def ent(P):
        ru=r['local'][P]['A']['root_of_unity_840']; z=r['local'][P]['A']['numeric']
        return (f"e({ru})" if ru is not None else f(z)+" (not a root of 1)")
    inf='+1' if sum(r['inf'])==0 else '−1'
    L.append(f"| ({k},{e},1) & ({k+12},{e},1) | {r['inf']} | {ent('P2')} | {ent('P5')} | {ent('P7')} | {inf} | {f(r['prod_A']['numeric'])} | {f(r['W_numeric'])} | {max(r['abs_diff'], D['results'][[x['chi'] for x in D['results']].index([k+12,e,1])]['abs_diff']):.1e} |")
L.append("")
L.append("| χ class | ε_5(π₅)=λ₅ε_𝔭₅ | ε_7(π₇)=λ₇ε_𝔭₇ | χ_𝔭₅(−1) | χ_𝔭₇(−1) | ω_π₅(−1) | ω_π₇(−1) | W₂₅² (Atkin–Li) | W₄₉² (Atkin–Li) |")
L.append("|---|---|---|---|---|---|---|---|---|")
for r,row in zip(D['results'],C['per_char']):
    k,e,_=r['chi']
    if k>=12 or e==1: continue
    L.append(f"| k={k},{k+12} (e=0,1) | {f(row['P5']['eps_pi_p'])} | {f(row['P7']['eps_pi_p'])} | {row['P5']['chiP(-1)']} | {row['P7']['chiP(-1)']} | {row['P5']['omega_pi_p(-1)']} | {row['P7']['omega_pi_p(-1)']} | e({row['P5']['W_Q^2_AtkinLi_turns']}) | e({row['P7']['W_Q^2_AtkinLi_turns']}) |")
open('table.md','w').write("\n".join(L)+"\n"); print("\n".join(L))
