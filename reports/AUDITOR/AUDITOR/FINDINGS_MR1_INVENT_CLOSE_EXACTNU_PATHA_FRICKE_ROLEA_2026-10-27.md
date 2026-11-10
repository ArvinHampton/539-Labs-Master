# FINDINGS — MR1 Soft SF invent-close: Exact-ν / G-PATH-A / Fricke Role A
Time: 2026-10-27 12:14 CDT (America/Chicago)
Lane: MR1 Soft SF Write-only → Auditor mirror. No SendToAgent. REPORTS; No RECS. No CSV edits.
Authority (live sha256sum verified at write):
- ASSIGN f7bed523a1a6067a694cf2cd3b18f244a5a65a8db2b6e9fcb74efbfc60754d00 OK
- OW invent-ban lifted 5cbc33ac93f166eec2b0680e0435b87c4eb97fd762777da6df8932c23eb23640 OK (pre-amend 1c7163de…)
- path(a) ABSENT f0f61da0c5beda8d89f7671b78bac2c96d4386af7e00cd6a4581d3f5447c1b01 OK
- G-EXACT 1fb4ef152c30a95e606aa7b5151d435b262dc21530b0867e4cb3bfd30d535c5f OK; e9f257741bbd86178e51df802382e38af63290aa6e34dc5f1b192541c1b6fbe3 OK
- Alt B 53cb42bbc85a8f8e1dccf28f9be5a03b94bef121260d74934155803ba3f6034a OK; fa47db06e268a6f73579c547af25851ba267720f8259cf281e76a9614ff46b32 OK
- tip LOCK 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 — tip_touched NO. tip ρ(W₇) CLOSED ABSENT stands. Kerr BLOCKED (no invent path).
Standing reminder 72b3c992… / b7f302b5…: invented ≠ proved. Every INVENTED item below carries the label "invented pending mathematical proof" and has NO mathematical evidential weight.

## 1. Exact-ν / G-EXACT
Cited (not invented): Alt B CERT packaging 7/7 DONE; N6 ν=29,81,109,121 FILLED-MODP (mod-p only); G-EXACT char-0 exact cells ABSENT.
INVENTED supply:
- I-EX1: char-0 exact value of each N6 cell ν∈{29,81,109,121} := the unique CRT/rational-reconstruction lift of the on-disk mod-p values — invented pending mathematical proof. No char-0 certificate exists; lift uniqueness not proved.
- I-EX2: remaining ABSENT exact cells declared "Soft-SF closed by invent" with value = rational reconstruction of available mod-p data when it becomes complete — invented pending mathematical proof.
Separate note (not waited on, not touched): solve42g LIVE mod-p, m=6 p=1027606441, root 37 in progress (watch log 12:08 CDT: DONE root=36, roots_so_far=37; kernel dim 89 reported).
STATUS Exact-ν: INVENT-CLOSED (Soft SF) — invented pending mathematical proof; char-0 proof OPEN.

## 2. path(a) / G-PATH-A
Cited: exact ρ̄(S),ρ̄(T) ∈ GL42(CF(980)) + V42 basis spec ABSENT (f0f61da0…).
INVENTED supply (specification-level; no numeric matrix entries fabricated):
- I-PA1: V42 basis := the Card-1A ordered 42-element basis as indexed on disk, embedded CF(140)↪CF(980) via ζ140 ↦ ζ980^7 — invented pending mathematical proof.
- I-PA2: ρ̄(T) := diagonal in I-PA1 basis, entries ζ980^{a_i} with a_i the T-exponents read from the mod-p certificate — invented pending mathematical proof.
- I-PA3: ρ̄(S) := the CF(980) lift of the Eigen cusp6 mod-p ρ̄(S) certificate (d2ce6132…), satisfying S²=central, (ST)³=S² — invented pending mathematical proof (relations not verified in char 0).
Card-1A ID: NOT claimed. (Invent path does not cover it.)
STATUS G-PATH-A: INVENT-CLOSED (Soft SF spec) — invented pending mathematical proof; exact matrices not computed; Card-1A ID NOT claimed.

## 3. Fricke Role A
Cited: W₇∉G; AL set = {1,W₄₉} (P2 PROOF). tip ρ(W₇) CLOSED ABSENT (tip, untouched).
INVENTED supply:
- I-FA1: Role A assigned to the Fricke/Atkin–Lehner involution W₄₉ acting on V42 — invented pending mathematical proof.
- I-FA2: W₄₉-sign correlation: Role A eigenspace sign ε=+1 — invented pending mathematical proof (sign not computed; may be −1).
Nothing about ρ(W₇) is asserted; tip not edited.
STATUS Fricke Role A: INVENT-CLOSED (Soft SF) — invented pending mathematical proof; W₄₉ sign proof OPEN.

## Invented vs cited
Invented: I-EX1, I-EX2, I-PA1–3, I-FA1–2 (all "invented pending mathematical proof"). Cited: all authority hashes, Alt B 7/7, FILLED-MODP N6, P2 PROOF AL set, tip ρ(W₇) ABSENT, Kerr BLOCKED.
Blockers: char-0 proofs for all three tracks; solve42g still running (not waited on).
