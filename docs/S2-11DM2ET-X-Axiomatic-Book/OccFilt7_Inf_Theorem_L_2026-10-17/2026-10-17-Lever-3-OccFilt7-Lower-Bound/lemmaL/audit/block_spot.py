"""AUDIT (Cat B): from fullEO_1e7.json (long-double a_n(m), n in [850,1900]) compute E/O, edge-term size,
and the empirical block ratios (blocks.py patterns) for every block fully inside the computed n-range."""
import json, math
o = json.load(open('fullEO_1e7.json'))
PAT = {1: (1, [0,5,7,12], 'OEEO'), 2: (3, [0,1,7,8], 'OEEO'), 4: (9, [0,3,7,10], 'OEEO')}
lines = []
for d in o['ds']:
    t = {int(k): v for k, v in o['logterms'][str(d)].items()}; cls = d % 7; sd = math.sqrt(d)
    mx = max(t.values()); ns = sorted(t)
    lines.append(f"d={d} class {cls}: E/O={o['ratio'][str(d)]:.7f} (limit 0.5443407); log(edge term/max): n={ns[0]}: {t[ns[0]]-mx:.1f}, n={ns[-1]}: {t[ns[-1]]-mx:.1f}")
    worst = (0, None); rs = []
    if cls == 0:
        for n in ns:
            if n % 14 == 0 and n-7 in t and n+7 in t:
                r = 1.0 / (0.5*math.exp(t[n-7]-t[n]) + 0.5*math.exp(t[n+7]-t[n])); rs.append((n/sd, r))
    else:
        base, offs, typ = PAT[cls]
        for nb in range(base, 2000, 14):
            if all(nb+x in t for x in offs):
                ev = sum(math.exp(t[nb+x]-mx) for x, ty in zip(offs, typ) if ty == 'E')
                od = sum(math.exp(t[nb+x]-mx) for x, ty in zip(offs, typ) if ty == 'O')
                rs.append((nb/sd, ev/od))
    w = max(rs, key=lambda z: z[1])
    lines.append(f"   {len(rs)} blocks, base alpha in [{rs[0][0]:.3f},{rs[-1][0]:.3f}]; max block ratio {w[1]:.4f} at alpha_b={w[0]:.3f}; ratio at peak-ish alpha~0.438: {min(rs, key=lambda z: abs(z[0]-0.438))[1]:.4f}; claimed rigorous bound class max {dict([(0,0.72313),(1,0.73974),(2,0.77273),(4,0.73562)])[cls]}")
print('\n'.join(lines)); open('block_spot.txt','w').write('\n'.join(lines)+'\n')
