# order75 PREREG — BRIDGE_C_35 (LOCAL modular lane)
Written 2026-10-24 ~23:20 CDT America/Chicago, before any order75 computation. CORE_FREEZE; new files only; order55–74 untouched; labels RG* only; no nonlocal EH11D/Ω₁₁D/F_total.

Pins (verified pins/SHA256SUMS 9 OK; SHA256SUMS bc2a9184…6186):
- Trunc pin b77fe22bb4a2ef001340cf262fa30a62803b69a7144a3f40695287fab6427493 (N=100)
- G1/S-B-1 pin 6c66dbc0ba675976805178c65697f38e805fd7078f28f353877ee9eba4742ab2 (B(v,w)=v^T M w, sgn(0):=0)
- W-PO-1 003e74bfe09bbb38a3dee457d18912eaf1fa301078c2d66956ca62ff606a95e3 (M=[[2,s],[s,s]])
- Parents: order74 PREREG 42850e59…, RESULTS 68ff36f5…, ADDENDUM_NSB1 dd679fba…, STREAM 309bb4c2…, GATE (order57) 640da80d…, ledger 7dbd63af….

## Tests
- RG75a pin integrity: abort on any mismatch.
- RG75c numeric C at N=100, s=7: same construction as order74 script (Q(n,k)=n²+snk+(s/2)k(k+1); P̂_orth over n,k≥0; H_s weight (sgn B(c1,v) − sgn B(c2,v))/2, c1=(-1,1), c2=(-4,1); B(c_i,v)=c_i^T M v natural instantiation — soft OPEN). PASS iff R=200,400,800 boxes give identical tables to deg≤100; report negative exponents.
- RG75d claim check: every C coeff deg 0..100 ∈ {0,1,3/2} exactly (Fraction). Reported PASS/FAIL separately; on FAIL list outliers, no repackaging.
- RG75e residual law for C: OPEN (no residual_slash/Fricke/C-law invent). T1–T4 hunt optional, cannot close C-law.
- RG75f G1 OPEN≠ACCEPT unless outer_* Written found (expect ABSENT); Ξ HOLD; GATE 640da80d binds.
- Bridge PARTIAL / READY NO unless residual law lands.
- order74 N=40 dump remains non-Cat-A exploratory; not cited as PASS.
