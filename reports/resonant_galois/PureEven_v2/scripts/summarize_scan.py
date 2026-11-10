import json, collections
res = json.load(open("../data/scan_results.json"))
out = []
def P(s=""): print(s); out.append(s)
for part, pred in (("integers 1<=m<=300", lambda r: '/' not in r['m']), ("fractions p/q, 2<=q<=10, 0<m<=10", lambda r: '/' in r['m'])):
    P(f"== {part} ==")
    P(f"{'k':>6} {'tested':>7} {'irred':>6} {'A5':>5} {'D5':>4} {'undet':>6} {'reducible':>9} | pari A5/D5/other(irr) | frob!=pari | D5<=>resolvent root violations")
    tot = collections.Counter()
    for k in ("-8/5", "-4", "4/5"):
        rs = [r for r in res if r['k'] == k and pred(r)]
        c = collections.Counter(r['frob'] for r in rs)
        irr = sum(r['irr'] for r in rs)
        pc = collections.Counter(r['pari'] for r in rs)
        dis = sum(1 for r in rs if r['frob'] in ('A5','D5') and r['frob'] != r['pari']) + sum(1 for r in rs if r['frob']=='undetermined' and r['pari'] not in ('reducible',))
        viol = sum(1 for r in rs if r['irr'] and (r['pari'] == 'D5') != bool(r['res_root']))
        P(f"{k:>6} {len(rs):>7} {irr:>6} {c['A5']:>5} {c['D5']:>4} {c['undetermined']:>6} {c['reducible']:>9} | {pc['A5']}/{pc['D5']}/{sum(v for g,v in pc.items() if g not in ('A5','D5','reducible'))} | {dis} | {viol}")
        tot.update(dict(n=len(rs), irr=irr, A5=c['A5'], D5=c['D5'], und=c['undetermined'], red=c['reducible']))
    P(f"{'total':>6} {tot['n']:>7} {tot['irr']:>6} {tot['A5']:>5} {tot['D5']:>4} {tot['und']:>6} {tot['red']:>9}")
    P()
# list D5 and reducible and undetermined
P("D5 fibres (k, m, cleared A, B):")
for r in res:
    if r['frob'] == 'D5': P(f"  k={r['k']} m={r['m']}  x^5+({r['A']})x+({r['B']})  pari={r['pari']}")
P("undetermined:", ) 
for r in res:
    if r['frob'] == 'undetermined': P(f"  {r}")
P("reducible fibres:")
for r in res:
    if r['frob'] == 'reducible': P(f"  k={r['k']} m={r['m']}  x^5+({r['A']})x+({r['B']})")
P("min/max number of Frobenius primes used:", )
P(str((min(r['nprimes'] for r in res if r['irr']), max(r['nprimes'] for r in res))))
open("../data/scan_summary.txt","w").write("\n".join(out)+"\n")
