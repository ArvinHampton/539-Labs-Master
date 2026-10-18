# Robustness of the s=14,17,18,22,23 violations against a too-small modulus: retest at L*k for k built from
# all primes dividing 2*s*(s-2)*D (powers up to 16 for 2), and report the fraction of hit classes that stay mixed.
import json, sys, sympy
from uL_periodicity import run
s = int(sys.argv[1]); P = int(float(sys.argv[2]))
primes = sorted(set(sympy.factorint(2*s*(s-2)*(s*s-2*s)).keys()) | {2, 3})
ks = sorted({1, 4, 8, 16} | set(primes) | {p*p for p in primes if p < 8})
r = run(s, P, ks=tuple(ks))
print(json.dumps({"s": s, "L": r["L"], "Pmax": P, **{k: (v["classes_hit"], v["classes_mixed"]) for k, v in r.items() if k.startswith("k=")}}), flush=True)
