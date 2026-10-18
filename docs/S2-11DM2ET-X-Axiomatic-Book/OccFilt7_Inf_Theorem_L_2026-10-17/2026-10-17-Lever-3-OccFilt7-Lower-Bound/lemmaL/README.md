Lemma L attempt (2026-10-17). All exact integer arithmetic (Python ints); no floating point in any test.
- tables.py N M     : builds a_n(m) = (-1)^m phi_n(m), n<=N, m<=M; asserts a_n(m) >= 0 (A1 check). Run `python3 tables.py 200 6000` first.
- pairing.py        : termwise injections even n -> odd n' (reflection n+n'=7 mod 14, n+7, n-7), d<=40000 -> out_pairing.txt
- window.py         : where the reflection pairing fails relative to the peak -> out_window.txt
- avg.py            : 'averaging' scheme e_n <= (o_prev+o_next)/2 -> out_avg.txt
- regions.py        : rho=m/n^2 windows where U (upper partner) / Dn (lower partner) termwise inequalities hold -> out_regions.txt
