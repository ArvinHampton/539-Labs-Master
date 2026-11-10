# Frozen (chmod a-w + sidecar) before the logged run. MR2 2026-11-09. Erratum to ed0e5bd6 per PP 4314f4c1: exact Aut(GL(2,3)), Aut(Isom) and their action on irreps; corrected [F4] sign lines of 69a10b84. Additive; no network.
import hashlib, io, contextlib, numpy as np
from math import cos, sin, pi, acos
def P(*a): print(*a, flush=True)
R='/workspace/quantum-comp/reports/'; f=R+'MR2_MN2_KK_A_IRREP_LABELS_BOLZA_LOW_LEVELS_AUT48_2026-11-09.py'
h=hashlib.sha256(open(f,'rb').read()).hexdigest()
P(f"[0] irrep-labels .py sha256 {h} ({'MATCH ff800541' if h.startswith('ff800541') else 'MISMATCH'}); exec'ing its group/irrep part (text before the FEM section), its own output suppressed")
src=open(f).read().split('# ---------------- F: vector FEM')[0]
with contextlib.redirect_stdout(io.StringIO()): exec(src)
tags=[q['tag'] for q in rows]; CV=[charvec(q['rep']) for q in rows]
def ext(imgs, gens, dom):
    s={E0:E0}; fr=[E0]
    while fr:
        nf=[]
        for a in fr:
            for g_,im in zip(gens,imgs):
                b=MT[a][g_]; c=MT[s[a]][im]
                if b in s:
                    if s[b]!=c: return None
                else: s[b]=c; nf.append(b)
        fr=nf
    return s if len(s)==len(dom) and len(set(s.values()))==len(dom) else None
def classes(dom):
    cl=[];seen=set()
    for i in dom:
        if i in seen: continue
        c=frozenset(MT[MT[g][i]][INV[g]] for g in dom); cl.append(c); seen|=c
    return cl
def inner(s,dom): return any(all(s[x]==MT[MT[g][x]][INV[g]] for x in dom) for g in dom)
# --- Aut(GL(2,3)) = Aut(Aut+) ---
D48=G48i; S48=set(D48)
gx=None
for x in D48:
    if order(x)==2 and x!=Jidx:
        S={E0};fr=[E0]
        while fr:
            nf=[b for a in fr for b in (MT[a][z],MT[a][x]) if b not in S]; S|=set(nf); fr=list(set(nf))
        if len(S)==48: gx=x; break
auts=[]
for a in D48:
    if order(a)!=8: continue
    for b in D48:
        if order(b)!=2: continue
        s=ext([a,b],[z,gx],D48)
        if s: auts.append(s)
cl48=classes(D48); c8=[c for c in cl48 if order(next(iter(c)))==8]
ninn=sum(inner(s,D48) for s in auts)
swap=sum(1 for s in auts if s[z] not in next(c for c in c8 if z in c))
P(f"[A1] Aut(GL(2,3)) by exhaustive search over images of (z, x) (orders 8, 2; z = r_AB r_AC, x an order-2 element with <z,x> = Aut+), full homomorphism + bijection check: |Aut| = {len(auts)}, inner {ninn}, |Out| = {len(auts)//ninn}")
P(f"[A1] order-8 classes: {len(c8)} (sizes {[len(c) for c in c8]}); automorphisms swapping them: {swap} of {len(auts)}")
th=[(cv,d) for cv,d in irr48 if d==3]
for cv,d in th:
    full={g:cv[G48i.index(g)] for g in D48}
    fixed=all(all(abs(full[s[g]]-full[g])<1e-9 for g in D48) for s in auts)
    vals=sorted(set(int(round(full[g])) for c in c8 for g in c))
    P(f"[A1] 3-dim Aut+ irrep {lab48(cv,d)}: character on all order-8 elements = {vals}; fixed by every automorphism: {fixed}")
# --- Aut(Isom) ---
invs=[i for i in range(n) if order(i)==2]
A96=[]
for a in invs:
    for b in invs:
        if order(MT[a][b])!=8: continue
        for c in invs:
            if order(MT[a][c])==2 and order(MT[b][c])==3:
                s=ext([a,b,c],[rAB,rAC,rBC],list(range(n)))
                if s: A96.append(s)
D96=list(range(n)); Z=[g for g in D96 if all(MT[g][x]==MT[x][g] for x in D96)]
inn96=[s for s in A96 if inner(s,D96)]
P(f"[A2] Aut(Isom) by exhaustive search over images of the Coxeter triple (involutions; product orders 8, 2, 3), full homomorphism + bijection check: |Aut| = {len(A96)}, |Z| = {len(Z)}, |Inn| = {len(inn96)}, |Out| = {len(A96)//len(inn96)}")
def perm(s):
    out=[]
    for k,cv in enumerate(CV):
        m=[j for j,cw in enumerate(CV) if all(abs(cw[s[g]]-cv[g])<1e-6 for g in D96)]; out.append(m[0])
    cyc=[];seen=set()
    for k in range(len(out)):
        if k in seen or out[k]==k: continue
        c=[k];seen.add(k);j=out[k]
        while j!=k: c.append(j);seen.add(j);j=out[j]
        cyc.append('('+' '.join(tags[i] for i in c)+')')
    return ''.join(cyc) or 'id'
pres=lambda s: set(s[g] for g in G48i)==set(G48i)
cnt={}
for s in A96:
    key_=(pres(s),perm(s)); cnt[key_]=cnt.get(key_,0)+1
for (p_,pm),c in sorted(cnt.items(),key=lambda t:(not t[0][0],t[0][1])):
    P(f"[A2] {c:3d} automorphisms, preserve Aut+ (holomorphic subgroup): {p_}; induced permutation of the 13 Isom irreps: {pm}")
P(f"[A2] Aut+ labels of the swapped 3-dim irreps: " + ", ".join(f"{q['tag']} -> {aut_decomp(q)}" for q in rows if q['d']==3))
# --- corrected [F4] lines of 69a10b84 ---
P("[F4'] corrected sign format of the 69a10b84 [F4] table (|cos psi| = |cos(pi k/8)|/sin(pi/3); cos psi fixed only up to sign):")
for k in range(1,8):
    c=abs(cos(pi*k/8))/sin(pi/3)
    P(f"     k={k}: cos psi = " + (f"\u00b1{c:.6f}" if c>1e-12 else "0") + " -> " + (f"psi = {acos(c):.6f} rad (real)" if c<=1 else "no real psi (|cos psi| > 1): no SO(3) rep"))
