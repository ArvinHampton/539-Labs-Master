# FINDINGS — Soft SF: Gap2/β primary-source fetch (Local ONLY)
Date 2026-10-28 (CDT). Executor: Local Path. tip LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — tip_touched NO. Kerr BLOCKED. No prior FINDINGS rewritten (76a92e8b/e8f54ca3/db77a8e0/5ca1d6b2/7b0eb063/595d6102/1db3d053 untouched). β_s/A_s/α remain invent-pending per 5ca1d6b2 — NO Written promotion.

## Summary
| # | Primary | Status |
|---|---|---|
|2|Andrews, Amer. J. Math. 88 (1966)|ABSENT-with-rigor (bib pinned)|
|3|Dragonette, TAMS 72 (1952) 474–500|CLOSED (full text fetched)|
|4|Bringmann–Ono, Ann. Math. 171 (2010) 419–449|CLOSED (full text fetched)|
|1|Zwegers, Contemp. Math. 291 (2001) 269–277|ABSENT-with-rigor (metadata only)|
|5|Γ₀(2) = ⟨T, E⟩, E²=−I|CLOSED-equivalent (software doc + local check); Rankin/Shimura text ABSENT|

## 3. Dragonette 1952 — CLOSED
URL: https://www.ams.org/journals/tran/1952-072-03/S0002-9947-1952-0049927-8/S0002-9947-1952-0049927-8.pdf (AMS free-access issue, FreeFlag=Y). PDF sha256 c8d637f02eb0df3a52c43d9f8053099a0de17636ee70c236735606dfea520003.
Verified: title "Some asymptotic formulae for the mock theta series of Ramanujan", TAMS 72 (1952) pp. 474–500, DOI 10.1090/S0002-9947-1952-0049927-8. Theorem I (p.~477, (h,k)=1, hh'≡−1 mod k, transformation of f(q) near e^{2πih/k}); Theorem II / formula (1.7) asymptotic for A(n), coefficients of f(q) (p. 478). Lemmas §2. Note: OCR is poor, so formulas were checked for structure only and not symbol by symbol.
CONFIRM: the prior citation of Dragonette as the source of the f(q) asymptotic or transformation is consistent. No conflict.

## 4. Bringmann–Ono Annals 2010 — CLOSED
URL: https://annals.math.princeton.edu/2010/171-1/p08 → PDF https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n1-p08-p.pdf, sha256 3bb872896cd7340783a6e6cd717d17ec52f50be049ab6447c7f670c7aa36f37c. DOI 10.4007/annals.2010.171.419, pp. 419–449.
Verified: Theorems 1.1–1.5; §3.2 "Vector valued weak Maass forms of weight 1/2"; it says f(q) plays "a central role in the proof of the Andrews–Dragonette Conjecture" (citing [10] = Invent. 165 (2006)). References: [4] Andrews, "On the theorems of Watson and Dragonette for Ramanujan's mock theta functions", Amer. J. Math. 88 (1966) 454–490, MR 34#157; [13] Dragonette TAMS 72 (1952) 474–500; [34] Zwegers Contemp. Math. 291.
CONFIRM: these entries match the bibliographic data used in the prior stack.

## 2. Andrews AJM 88 (1966) — ABSENT-with-rigor
Tried: JSTOR (paywalled, no full text). Crossref lookup for 10.2307/2373073 resolved to an unrelated item, so that DOI guess is wrong. Pinned via Bringmann–Ono 2010 ref [4]: title, pp. 454–490, MR 34#157. The theorem text of the f(q) transformation was NOT verified from the primary. Keep citing it through Dragonette Thm I (fetched) and Bringmann–Ono 2006 or 2010.

## 1. Zwegers Contemp. Math. 291 — ABSENT-with-rigor
Tried: AMS conm/291 TOC (lists "S. P. Zwegers — Mock θ-functions and real analytic modular forms", MR 1874536). Crossref 10.1090/conm/291/04907 confirms pp. 269–277. Paywalled, and no free author copy was found (the uni-koeln author page returned nothing usable). The matrices in Thm 2.1 are NOT confirmed against this primary. They remain grounded through the thesis arXiv:0807.4834 (prior). Neither CONFIRM nor conflict.

## 5. Γ₀(2) generators — CLOSED-equivalent
URL: https://doc.sagemath.org/html/en/thematic_tutorials/explicit_methods_in_number_theory/modular_forms_and_hecke_operators.html (snapshot sha256 5542ddc03cda985d8f2164f83c3bad68dfb7adf80d99cd10cd8859bfffc24c69). The "Generators" section shows Gamma0(2).gens() = ([[1,1],[0,1]], [[1,-1],[2,-1]]), from the Farey-symbol algorithm (Kurth–Monien). The old Todd–Coxeter output also lists −I explicitly.
Supporting source: math.stackexchange.com/questions/2201149 (D. Loeffler), which gives Γ₀(2) ≅ Z * Z/2 in PSL₂.
Local check (numpy): E² = −I exactly, so −I ∈ ⟨T,E⟩.
Rankin and Shimura were NOT fetched, so the textbook citation is still ABSENT. CONFIRM the prior generator claim.

## Net
3 CLOSED (#3, #4, #5-equivalent) and 2 ABSENT-with-rigor (#1, #2). No conflicts found. β/A not promoted.
