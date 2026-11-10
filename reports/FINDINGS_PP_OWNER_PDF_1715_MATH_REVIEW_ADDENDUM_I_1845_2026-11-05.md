# ADDENDUM I — Owner t4098 18:45 (same review; exact by hand; relay-based; No CERT; no .tex)

## Proposed A: F=⊕L0..L_{M−1} → B=⊕L1..L_M, diagonal −T_i, identities I_i on the subdiagonal
- ILL-TYPED: the block in row 2, column 1 maps the input L0 to the output L2. An identity there needs L0=L2.
- Counterexample: all L_i=K, M=2, T1=T2=1. Then A=[[−1,0],[1,−1]] with det 1, so A is invertible and ker A=0.
  The compatible trajectories (t,t,t) still exist, and the state x_M does not even appear in F.
  So ker A does NOT enforce x_i=T_i x_{i−1}.
- If ker A=0, then dimF−dimB = −dim coker A (with a minus sign).
- The surrogate N−|W| := n0−n_M is zero iff n0=n_M, regardless of the coefficients. This is a definition; identifying it with the original N and |W| is OPEN.

## Correct operator (PROVED)
- D: ⊕_{i=0}^M L_i → ⊕_{i=1}^M L_i, with (Dx)_i = x_i − T_i x_{i−1}. Its block rows are [… −T_i  I …].
- D is surjective, and ker D ≅ L0 via x0. On ker D, x_M = P x0 where P = T_M⋯T_1.

## Exact boundary-matching criterion (PROVED)
- Add the boundary constraint C0 x0 + C_M x_M = 0. Then
  {trajectories satisfying it} ≅ ker(C0 + C_M P).
  It is trivial iff C0 + C_M P is injective.
- Fixed start x0=0 (C0=I, C_M=0): the kernel is 0, with no invertibility assumption on the T_i.
- End constraint R x_M=0 (C0=0, C_M=R): the kernel is ≅ ker(R·T_M⋯T_1).
- Proof: compatibility gives x_M = P x0, so the constraint reads (C0 + C_M P) x0 = 0, and x0 determines the whole trajectory.

Original N/W/capacity: OPEN.
