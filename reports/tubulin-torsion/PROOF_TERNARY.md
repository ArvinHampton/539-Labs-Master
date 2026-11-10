# PROOF — Ternary extension (Lemmas 4–5, formalized)
Balanced Ternary Subset Sum (BTSS): input positive integers b_1..b_m, integer T′. Question: ∃ x ∈ {−1,0,1}^m with Σ x_j b_j = T′.

## Lemma 4a. BTSS is NP-hard (SS ≤_p BTSS). Status: PROVED
Given SS (a_1..a_n, T); if T > Σ := Σa_i map to fixed NO instance (m=1, b_1=1, T′=2). Else let B := 2(Σ+2)+1 (odd, B > 2Σ+4). Weights, for i=1..n: u_i := B^i + a_i, v_i := B^i. Target T′ := Σ_{i=1}^n B^i + T. Size poly (numbers have O(n log B) bits).
(⇒) x solves SS: set y_{u_i} = x_i, y_{v_i} = 1 − x_i ∈ {0,1}. Sum = Σ B^i + Σ x_i a_i = T′.
(⇐) Let y ∈ {−1,0,1}^{2n} with Σ y_{u_i}u_i + y_{v_i}v_i = T′. Write d_i := y_{u_i}+y_{v_i} ∈ [−2,2] and d_0 := Σ y_{u_i} a_i ∈ [−Σ, Σ]. Then Σ_{i=0}^n d_i B^i = Σ_{i≥1} 1·B^i + T. All digits on both sides lie in (−B/2, B/2) (|d_0| ≤ Σ < B/2, |d_i| ≤ 2, 0 ≤ T ≤ Σ). Balanced base-B representation with digits in (−B/2,B/2), B odd, is unique (standard: reduce mod B, digit is the unique residue representative in that interval; subtract, divide by B, induct). Hence d_i = 1 for i ≥ 1 and d_0 = T. d_i = 1 with entries in {−1,0,1} forces (y_{u_i},y_{v_i}) ∈ {(1,0),(0,1)} (other options would need an entry of 2), so y_{u_i} ∈ {0,1} and Σ y_{u_i} a_i = T: SS solved. ∎ Membership in NP obvious, so BTSS is NP-complete.

## Lemma 4b. BTSS ≤_p ternary RPP (C = {−1,0,1}). Status: PROVED
Given (b, T′), S := Σ b_j. If |T′| > S output fixed NO instance. Else M := 2^k > 2S (k = ⌈log2(2S+1)⌉+1), w_j := b_j, s := (0,0), t := (m, T′ mod M), L := m.
Iff: (⇒) as in Lemma 3 with c_j = x_j. (⇐) path gives c ∈ {−1,0,1}^m with Σ c_j b_j ≡ T′ (mod M); both lie in [−S, S], an interval of length 2S < M, on which reduction mod M is injective ⇒ equality. Layering identical to Lemma 2(a). ∎

## Theorem B. Ternary RPP is NP-complete (succinct). Status: PROVED (composition of 4a, 4b; NP membership as Theorem A).

## Lemma 5 (PDF: det(H) ≠ 0 over the group ring eliminates cancellation). Status: PARTIAL (see PROOF_GROUP_RING_LEMMA5.md, 2026-10-31: det ≠ 0 does not eliminate signed cancellation — counterexample C2; ℤ⁺ coefficients give zero cancellation trivially; hardness survives on det≠0 slice via odd M). Prior NF-WHY note retained below.
Obstruction: (i) the "group ring of ternary states" and its Hankel matrix are undefined in the PDF; (ii) cancellation between +1 and −1 choices is not eliminated by any determinant condition — it is handled in Lemma 4a by base-B digit separation and in 4b by M > 2S; (iii) as shown in PROOF_HANKEL_POSITIVITY.md, det ≠ 0 does not control sign/positivity anyway. Lemma 5 is not needed for Theorem B and is not proved.
