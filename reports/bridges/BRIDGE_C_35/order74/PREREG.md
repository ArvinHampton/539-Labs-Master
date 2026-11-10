# order74 PREREG — BRIDGE_C_35 (LOCAL lane)
Written 2026-10-24 ~23:10 CDT America/Chicago. CORE_FREEZE; new files only; labels RG* only; local modular only; no invent; no push/send; no nonlocal EH11D/Ω₁₁D/F_total.

## Source pin
pins/G1_REOPEN_AND_S_B1_WRITINGS_2026-10-24.md sha256 6c66dbc0ba675976805178c65697f38e805fd7078f28f353877ee9eba4742ab2 (re-verified = pins/SHA256SUMS; chat-locked t604u; Drive ABSENT).

## Parents
order73 PREREG 36101dc0cc12b94ef5462a965e2d04684f5037c87b0430f71e65615352d48a45; RESULTS 3109808ba6b0bb78192f785d75756ee266b4f5dec5c8d6a2159dcce6096a3605; STREAM 2ef696feb6305d0f38179dbac915e989331baf55711dec16320103cf5c4a93a3; W-PO-1 003e74bfe09bbb38a3dee457d18912eaf1fa301078c2d66956ca62ff606a95e3; P̂_orth a6dfcec47df013db993c0165d4e99abb085291bfb824e7dd1d2232806600bf32; confirmed ledger b10193b4ab7ee0fbf757a94dd9141deecf48c0597a24189e1863b2a3fe0afd08; GATE_DECISIONS order57 640da80d794020eca6abf5f6e863cf1ebdbee1fa5171adeb311f57d86cd76570 (not mutated; addendum as order74/GATE_DECISIONS_ADDENDUM.md).

## (a) G1 review protocol
Status at ingest: OPEN. ACCEPT only if corpus now contains written (i) outer_even_coeff / outer_odd_coeff tables (non-unit), (ii) outer_residual_factor, (iii) full (non-selected/non-partial) Ξ Fourier table — i.e. the order68 REJECT reasons are cured in writing. Otherwise verdict stays OPEN (pin opened review; no evidence to REJECT anew nor ACCEPT). Ξ HOLD until ACCEPT; no numeric Ξ.

## (b) Numeric C plan (RG74c)
s=7; M=[[2,7],[7,7]]; B(v,w)=v^T M w; sgn(0):=0; c1=(-1,1), c2=(-4,1); w(v)=½(sgn B(c1,v) − sgn B(c2,v)); Q_s(n,k)=n²+7nk+(7/2)k(k+1).
P̂_orth = Σ_{n,k≥0} q^{Q_s}; H_s = Σ_{v∈Z²} w(v) q^{Q_s(v)}; C = P̂_orth − H_s.
Degree truncation: N = 40 (keep exponents ≤ 40). Enumeration box |n|,|k| ≤ R with R=200 and stability check at R=400 (identical coefficients required; else PARTIAL). Any exponent < 0 with w≠0 reported (not dropped) and flags PARTIAL. PASS = tables stable and dumped. No residual_slash identity; residual law for C OPEN.

## (c) Rules
Bridge YES requires T1–T5 written AND residual law for C written. READY YES requires every track written-satisfied and G1 not REJECT. Numeric C alone does not change either.

## (d) T1–T4: corpus hunt for written bodies; FOUND only if a statement/formula body exists, ABSENT if only named.

## (e) RG47f-bis HOLD unless written forces otherwise. Invent-ban.
