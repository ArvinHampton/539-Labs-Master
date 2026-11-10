# MR2 FINDINGS — DUAL-CONTINUE — GAP-SK-p3-1a (2026-10-27)
STATUS: GAP-SK-p3-1a CLOSED (by self-contained proof + p=3,5,7 machine check; verbatim lit for classification; lit for dim-1 I(1)-invariants only implicit) | NOT OPERATIVE | tip_touched NO | Kerr BLOCKED | REPORTS ONLY, no RECS | no new invented values

Parent: reports/MR2-FINDINGS-DUAL-CONTINUE-gap-sk-p3-1_2026-10-27.md sha256 0be31458e0e1bbf71d38bd4a194d6b75aa870b72f662801af120f8878c839d6b
Eigen relay: bridges/EIGEN/EIGEN_REVIEW_RELAY_MR2_GAP_SK_P3_1_2026-10-27.md sha256 aad75c88ea92364505b33838ef1ca98920e0b99e87f1a3872bf42012a9ddb643
Tip: /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md sha256 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 (checked before and after; unchanged)

Claim (step 2 of GAP-SK-p3-1): every irreducible smooth F̄p[K]-rep, K=GL2(Zp), is Sym^s F̄p^2 ⊗ det^a inflated from GL2(Fp), 0≤s≤p−1, and dim σ^{I(1)} = 1.

## (a) Literature (lit/bm/, line numbers of the .txt)
- breuil_GL2Qp_I.txt (sha 3b5f0a8e7a58de7a3c37c4391bf6d855704ddbc947b0b9deaa17c1edf3154518), L389–392 VERBATIM (classification): "A torsion près par les caractères, les σ~r donnent toutes les représentations lisses irréductibles de dimension finie de KZ sur F̄p ([2])." with σ~r = Sym^{r1}⊗…⊗Sym^{rf}, rj∈{0,…,p−1} (L376–379); [2]=Barthel–Livné, Duke (L1565). L189–197 defines I(1) (a≡d≡1 mod ϖ, i.e. pro-p Iwahori). L1103: "I(1) est un pro-p-groupe, V^{I(1)} ≠ 0".
- 1309.1658.txt (sha 69ff1168ed345bd884c4eaf6112a108fe5e21ccc20d43baea35094c646224d69), L124–127 VERBATIM: "Recall that the finite dimensional irreducible F-representations of GL2(Zp) are of the form σn,m := Symn F2 ⊗ detm, n ∈ {0,…,p−1}, m ∈ {0,…,p−2}."
- breuil_paskunas_supersingular.txt (sha cefcae816aa0414f2d989891366c783161711051597f0d641c77647a64960ba2), L557–561 VERBATIM: "We call a weight an irreducible representation of K (hence of Γ) on F̄p. A weight can be written: Sym^{r0}… ⊗ η … where the ri are integers between 0 and p − 1"; L546–548: "χ : I → F̄p× the character giving the action of I on σ^{I1}" — presupposes dim σ^{I1}=1 (IMPLICIT, not a stated lemma).
- breuil_GL2Qp_II.txt (sha 245f62ee00f8c392bfc1dbe0ce5a14d40a634e137c161ec2d07414cd0362b273), L1351–1354 Lemme 5.1.2 (σ^{I(1)} dim 1 + generates ⇒ irreducible) — converse direction only.
- 1209.5205.txt (sha 4ac1a4c57fe6a38e1f05210e0c6e57df06eb8e875cb01852aaa57c5031fe8592): no verbatim statement found (grep I(1)/U(Fp)/Sym-invariants).
Fate (a): classification VERBATIM-SOURCED (3 files); "dim Sym^r^{I(1)} = 1" NOT found verbatim in the 5 files — closed instead by proof (b) + check (c).

## (b) Proof
Convention: g=[[a,b],[c,d]] acts on Sym^s = ⊕ F̄p x^{s−i}y^i by x↦ax+cy, y↦bx+dy.
1. Factoring. K(1)=ker(K→GL2(Fp)) is open, normal, pro-p. For smooth V≠0 over char p, V^{K(1)}≠0 (a vector's orbit spans a finite F̄p-space on which a finite p-group acts; a p-group fixes a nonzero vector of any nonzero F_p-space, hence of any finite-dim F̄p space by restricting to the Fp-span of an orbit). V^{K(1)} is K-stable (normality), so V irreducible ⇒ V=V^{K(1)}: V factors through GL2(Fp); in particular finite-dim.
2. Sym^s⊗det^a (0≤s≤p−1) is irreducible, with U-fixed line F̄p x^s (step 4). Any nonzero subrep W has W^U≠0 (U(Fp) a p-group), so x^s∈W; w=[[0,1],[1,0]] gives y^s, and u_t y^s=(tx+y)^s=Σ C(s,i) t^i x^i y^{s−i}; since C(s,i)≢0 mod p for s≤p−1 and Vandermonde in t∈Fp (p≥s+1 points) is invertible, all monomials lie in W ⇒ W=Sym^s.
3. Completeness. Torus diag(α,δ) acts on x^s⊗det^a by α^{s+a}δ^a; labels (s+1, s+a mod p−1, a mod p−1), s∈[0,p−1], a∈[0,p−2], are pairwise distinct ⇒ p(p−1) pairwise non-isomorphic irreducibles. By Brauer, #irreducible F̄p-reps = #p-regular classes of GL2(Fp) = (p−1) central + (p−1)(p−2)/2 split + (p²−p)/2 elliptic = p²−p. Hence the list is complete.
4. Invariants. I(1)={a≡d≡1, c≡0 mod p} maps onto U(Fp)={u_t=[[1,t],[0,1]]}, so σ^{I(1)}=σ^{U(Fp)} (det^a trivial on U). u_t: x↦x, y↦tx+y. For f=Σc_i x^{s−i}y^i put g(Y)=f(1,Y), deg g ≤ s ≤ p−1; u_t f=f ⇔ g(Y+t)=g(Y) ∀t. Finite difference Δg=g(Y+1)−g(Y): if deg g=d with 1≤d≤p−1, leading coeff of Δg is d·c_d≠0 (d<p), so Δg≠0. Hence fixed ⇔ g constant ⇔ f=c x^s. dim σ^{I(1)}=1. (Bound s≤p−1 is sharp: for s=p, y^p−x^{p−1}y is also fixed.) ∎

## (c) Computation
scripts/mr2_gap_sk_p3_1a_verify.py sha256 afde9e970780c7342d0b6e7619143074b4f698b455506899377b068393a4af52
scripts/mr2_gap_sk_p3_1a_verify.out sha256 29b02ba557fd56763f992661f67fa6521fff3f9d28340e36fd961b76e25297ad
p=3,5,7, all 0≤s≤p−1: kernel of {u_t−1 : t∈Fp} mod p has dim 1 spanned by x^s; GL2(Fp)-span of x^s = full Sym^s; label count = p(p−1) = #p-regular classes (6, 20, 42). Output: ALL_OK. (Kernel dim over Fp = over F̄p, base change.)

## Fates
- GAP-SK-p3-1a: CLOSED (proof b, check c; classification also verbatim in lit a). Residual: dim-1 I(1)-invariants is not quoted verbatim from the 5 files (only implicit in Breuil–Paškūnas L546–548); Brauer's count theorem used as standard (not quoted). Neither affects closure by proof.
- GAP-SK-p3-1: unchanged CLOSED+FLAG per Eigen relay; this file discharges the step-2 citation flag only.
- NOT OPERATIVE. tip_touched NO. Kerr BLOCKED (untouched). No new invented values.
