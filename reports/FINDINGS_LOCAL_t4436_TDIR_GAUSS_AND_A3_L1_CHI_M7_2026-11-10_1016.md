# FINDINGS (Local-derived): T-Dir discharged for χ₁₄₀ and χ_{-7}; L(1,χ_{-7})=π/√7 PROVED (a-3 T-CNF discharged). 2026-11-10, written 10:16 CST (America/Chicago)

- **Scope.** Additive. Nothing is edited, deleted, renamed or moved (in particular the T-theta1 filing FINDINGS_LOCAL_t4436_T_THETA1_UNARY_THETA_2026-11-10_1010.md is not rewritten). No CERT. No Gemini. Nothing sent outside. Tip /workspace/residual-c-field-WRITTEN_PREMISES_DRAFT.md = 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91, checked before and after writing. "Resonant algebra" (RTA historical alias only). A citation alone never makes a claim PROVED (OW 36683379). **Nothing is adopted.**
- **Authority.** Owner t4436. This file pursues items 6 of 26a7c91e §N (T-Dir / T-CNF for the two Dirichlet characters appearing in the a-2, a-3 and b-1 rows), by F0-5 (Poisson) plus exact Gauss sums and an elementary Fourier series. It does not duplicate T-theta1; it cites the already-filed evaluation G(χ_{-7})=i√7 and applies it.
- **Running jobs were not disturbed.** No large PARI job was started.
- **Base.** F0-5 (1-D Poisson summation); the Fourier series of {x}−1/2 on (0,1), computed below; finite arithmetic in ℤ[ζ₅] and Kronecker symbols, certified in s14. The evaluation G(χ_{-7})=i√7 is carried from the T-theta1 filing (s13 [G], G²=−7 in ℤ[ζ₇] and the sine-sign under ζ↦e(1/7)), which is awaiting PP and is not re-edited here.

## 1. Gauss sums

Write G(χ) := Σ_{k=0}^{f−1} χ(k) e(k/f) for a primitive character χ of conductor f, with e(z)=exp(2πi z).

**Product formula.** If χ₁, χ₂ are primitive of coprime conductors f₁, f₂, and χ=χ₁χ₂ (then primitive of conductor f₁f₂), one has G(χ)=χ₁(f₂)χ₂(f₁) G(χ₁)G(χ₂). Proof: every residue n (mod f₁f₂) is uniquely n=f₂x+f₁y with x (mod f₁), y (mod f₂). Then χ₁(n)=χ₁(f₂x)=χ₁(f₂)χ₁(x), χ₂(n)=χ₂(f₁y)=χ₂(f₁)χ₂(y), and e(n/(f₁f₂))=e(x/f₁)e(y/f₂). The double sum factors.

**G(χ_{-4})=2i.** Certificate [G4]: χ_{-4}(0)=χ_{-4}(2)=0, χ_{-4}(1)=1, χ_{-4}(3)=−1, and e(1/4)=i, e(3/4)=−i, so G= i −(−i)=2i.

**G(χ₅)=√5.** In ℤ[ζ₅]/(Φ₅), Φ₅=1+x+x²+x³+x⁴, let φ=ζ+ζ⁴ and ψ=ζ²+ζ³. Certificate [G5]: φ+ψ=−1 and φψ=−1 exactly, so φ,ψ are the roots of X²+X−1=0, namely (−1±√5)/2. Under the standard embedding ζ↦e(1/5), φ=2cos(2π/5)>0, so φ=(−1+√5)/2. The Gauss sum is G=ζ+ζ⁴−ζ²−ζ³=φ−ψ=1+2φ (since φ+ψ=−1), and G²=5 exactly in the field. Substituting the positive root gives G=1+2·(−1+√5)/2=√5.

**G(χ_{-7})=i√7**, carried from the T-theta1 filing (s13 [G]): G²=−7 in ℤ[ζ₇], and G=2i(sin(2π/7)+sin(4π/7)−sin(6π/7)) with a positive parenthesis, so the standard embedding is the upper-half-plane root +i√7.

**G(χ_{140})=√140.** Factor χ_{140}=χ_{-4}χ_{-35} (because (−4)(−35)=140) and χ_{-35}=χ₅χ_{-7} (because 5·(−7)=−35), all factors primitive, conductors coprime in pairs. Certificate [G140]: the Kronecker values are χ_{-4}(35)=−1, χ_{-35}(4)=1, χ₅(7)=−1, χ_{-7}(5)=−1. Thus G(χ_{-35})=χ₅(7)χ_{-7}(5) G(χ₅)G(χ_{-7})=i√35, and G(χ_{140})=χ_{-4}(35)χ_{-35}(4) G(χ_{-4}) G(χ_{-35})=(−1)·(2i)·(i√35)=2√35=√140.

## 2. Poisson inversions for the even and odd thetas

Let χ be primitive of conductor f, and write t=−2iτ as in PP 0f1d3361 Θ2, so e(n²τ)=exp(−π t n²). The Fourier transform on ℝ with ĥ(ξ)=∫ h(x) e^{−2πi x ξ} dx satisfies, for the Gaussian g(x)=exp(−π t x²), ĥg(ξ)=t^{−1/2} exp(−π ξ²/t), by F0-5 / Θ2. Differentiating in the linear parameter, or using FT[x g]=(i/2π)(ĝ)′, gives FT[x exp(−π t x²)](ξ)= −i(ξ/t) t^{−1/2} exp(−π ξ²/t).

**Twisted Poisson.** For primitive χ and Schwartz h, Gauss inversion (apply the defining sum to χ̄) is χ(n)=(1/G(χ̄)) Σ_{k=0}^{f−1} χ̄(k) e(k n/f). Thus
Σ_n χ(n) h(n) = (1/G(χ̄)) Σ_k χ̄(k) ĥ(−k/f).
For every real character of §1 one has the explicit evaluation G(χ)²=χ(−1)f, and χ̄=χ, so the prefactor rearranges (with ĥ even or odd according as h is even or odd) to G(χ)/f, and
Σ_n χ(n) h(n) = (G(χ)/f) Σ_m χ(m) ĥ(m/f).

**Even case, χ(−1)=+1.** Let h(x)=exp(−π t x²), so ĥ(ξ)=t^{−1/2} exp(−π ξ²/t). Define Θ(u,χ):=Σ_n χ(n) exp(−π n² u / f). The left side of twisted Poisson is Θ(t f, χ). Setting u=t f gives
Θ(u,χ) = (G(χ)/√f) u^{−1/2} Θ(1/u, χ).

**Odd case, χ(−1)=−1.** Let h(x)=x exp(−π t x²), with the FT recorded above, and define Θ₁(u,χ):=Σ_n χ(n) n exp(−π n² u / f). The same substitution u=t f gives
Θ₁(u,χ) = (G(χ)/(i √f)) u^{−3/2} Θ₁(1/u, χ),
since 1/i=−i. For χ=χ_{-7} one has G/(i√7)=1, which is the inversion of the T-theta1 filing §6 in the present normalisation.

## 3. Functional equations (T-Dir, for these two characters)

**Even character, χ=χ₁₄₀, f=140, G=√140.** For Re s large,
∫_0^∞ Θ(t,χ) t^{s/2} dt/t = 2 (f/π)^{s/2} Γ(s/2) L(s,χ),
because the n=0 term of Θ vanishes (χ(0)=0) and ∫_0^∞ exp(−π n² t/f) t^{s/2} dt/t = (π n²/f)^{−s/2} Γ(s/2). Write I(s)=∫_0^∞ Θ(t,χ) t^{s/2} dt/t = I_{0,1}+I_{1,∞}. On (0,1) set t=1/u and apply §2: Θ(1/u,χ)=(G/√f) u^{1/2} Θ(u,χ). This gives
I(s) = ∫_1^∞ Θ(t,χ) ( t^{s/2} + (G/√f) t^{(1−s)/2} ) dt/t,
which converges for every s (Θ(t,χ) decays exponentially as t→∞) and therefore supplies the meromorphic — here entire — continuation of (f/π)^{s/2} Γ(s/2) L(s,χ). Comparing I(s) with I(1−s) yields
Λ(s,χ) := (f/π)^{s/2} Γ(s/2) L(s,χ) = (G/√f) Λ(1−s,χ).
Here G/√f=√140/√140=1, so **Λ(s,χ₁₄₀)=Λ(1−s,χ₁₄₀)**, with root number +1. In particular L(s,χ₁₄₀) is entire (Γ(s/2) has poles at nonpositive evens, cancelled in the usual way by the trivial zeros of L, and the integral representation has no poles).

**Odd character, χ=χ_{-7}, f=7, G=i√7.** The Mellin transform of Θ₁ is
∫_0^∞ Θ₁(t,χ) t^{(s+1)/2} dt/t = 2 (f/π)^{(s+1)/2} Γ((s+1)/2) L(s,χ).
The same split, with the odd inversion of §2 and G/(i√f)=i√7/(i√7)=1, gives
Λ(s,χ) := (f/π)^{(s+1)/2} Γ((s+1)/2) L(s,χ) = Λ(1−s,χ),
with root number +1. Thus L(s,χ_{-7}) is entire, and **Λ(s,χ_{-7})=Λ(1−s,χ_{-7})**.

This is the functional equation and entire continuation of these two Dirichlet L-functions, on F0-5 plus the exact Gauss sums of §1. **T-Dir is discharged for χ₁₄₀ and χ_{-7}**, which are the only characters used in the b-1 row. (T-Dir as a general theorem about all Dirichlet L-functions is not claimed.)

## 4. The value L(1,χ_{-7})=π/√7 (a-3)

Let χ be odd and primitive of conductor q, and let ψ(x)={x}−1/2 for non-integral x. The Fourier coefficients are elementary:
∫_0^1 (x−1/2) e(−n x) dx = −1/(2πi n) for n≠0,
which is an integration by parts (the boundary terms cancel because (x−1/2)e(−nx) is periodic up to a sign that matches). Hence, for x∈(0,1),
{x}−1/2 = − Σ_{n≠0} e(n x)/(2πi n).
Set x=a/q with a=1,…,q−1, multiply by χ(a) and sum. The left side is (1/q) Σ_a a χ(a), because Σ_a χ(a)=0. The right side is
− Σ_{n≠0} 1/(2πi n) · Σ_a χ(a) e(n a/q) = − Σ_{n≠0} χ̄(n) G(χ) /(2πi n),
using Σ_a χ(a)e(n a/q)=χ̄(n)G(χ) (and χ(n)=0 when q|n). Split n>0 and n<0:
Σ_{n≠0} χ̄(n)/n = L(1,χ̄) − χ̄(−1) L(1,χ̄) = 2 L(1,χ̄),
since χ is odd. Thus
(1/q) Σ_a a χ(a) = − G(χ) L(1,χ̄) /(π i),
or
L(1,χ̄) = − (π i /(q G(χ))) Σ_{a=1}^{q−1} a χ(a).

For χ=χ_{-7}, one has q=7, χ̄=χ, G=i√7, and certificate [S7]: Σ_{m=1}^{6} m χ_{-7}(m)=1+2−3+4−5−6=−7. Therefore
L(1,χ_{-7}) = − (π i /(7 · i√7)) · (−7) = π/√7.

This evaluation does not use the class number formula. The a-3 row's condition tag T-CNF is therefore discharged: **L(1,χ_{-7})=π/√7 is PROVED**. (The 60-digit lfun agreement in s6 remains an illustration only.)

## 5. What this does not discharge

- **a-2 / T-CNF.** The even-character companion is the log-sine formula L(1,χ)=−(G(χ)/f) Σ_{a=1}^{f−1} χ(a) log sin(π a/f), which follows from the same method with −log|1−e(a/f)| in place of the sawtooth, but the identification of that sum with 4 log(6+√35)/√140 is precisely the class number formula for ℚ(√35) (whose inputs h=2 and ε=6+√35 are already PROVED in ab20f7ca). The a-2 value therefore stays **COND [T-CNF]**. No attempt is made here to evaluate the log-sine sum independently.
- **b-1 / T-spin.** With T-Dir discharged for the two factors, the statement "Λ is entire and Λ(1−s,π)=Λ(s,π)" under a-2 or a-3 still depends on the identification Λ(s,π,std)=Λ(s,χ)² ∏_{i=1}^{23} Λ(s−i,χ)Λ(s+i,χ) (or the a-3 analogue), which is the T-spin tag. The b-1 row stays **COND [T-spin]**. Root numbers of the Dirichlet factors are now +1 by proof, not by the 76-digit illustration.
- **T-spin itself, T-Kostant, T-Wald, T-AL-new, C2/C3, and T-cond** are not addressed. T-theta1 remains as filed, awaiting PP, and is not reargued.

## 6. Proposed grades (subject to PP ruling)

- **a-3, L(1,χ_{-7})=π/√7:** COND [T-CNF] → **PROVED**.
- **T-Dir,** for the two characters used in b-1: discharged. The b-1 row remains **COND [T-spin]** only.
- **a-2** unchanged, still COND [T-CNF] (and T-spin on its other row).
- **Proposed t4436 tally, subject to PP, and independent of the still-pending T-theta1 ruling:** from the last ruled tally 63/17/5/9/2, the a-3 change alone would give **64/16/5/9/2**. If PP also accepts the already-filed T-theta1 discharge, the two changes together would give **65/15/5/9/2**. Bridge C is unchanged at 47/11/5/2/1 + V₈₄ (66 rows). Nothing is adopted.

## 7. Evidence (new; evidence_local_t4436_branches_2026-11-09/; each file has a .sha256 sidecar)

| File | sha256 |
|---|---|
| s14_tdir_gauss_L1_chi_m7.py | c1200359ef01a4158c969026b11569ac7a1a41fffcbbae7c18e9fb3aeac7d78f |
| s14_tdir_gauss_L1_chi_m7.log | c1ecaae34a94903b077682be0625db42da3d5655a37fd7a3e9950065e173ef27 |

Running jobs and the tip were not touched. Local-derived. Nothing adopted.
