# DRAFT — Owner Write Item (2): vector residual_factor / B1
**Date:** 2026-10-25 ~18:17 America/Chicago  
**Status:** DRAFT for Owner Written ACCEPT — **not** Cat A · **not** inserted into residual-C  
**Lane:** NL (ledger Item 2)  
**Owner ask:** t1013u pursue writing it  
**invent-ban:** held  

**Constraint source (RTA v12, Cat A inside RTA only):**  
`quantum-comp/reports/self-audit/zenodo/RTA_v12.txt` sha256 `f837aa377f0d57d1822d5d3243509f4a4a8c77a3aeaec7bf55e885de12303bcb`

---

## 0. What this Write is

An Author Written identification of the **Bridge / residual** object `residual_factor` as a **vector-valued** modular object, consistent with the RTA v12 scalar-W₇ no-go, plus an Author disambiguation of the symbol **B1** in that residual context.

RTA Cat A does **not** automatically transfer to residual-C. This Write, once Accepted, is Author Written guidance for Item (2); residual-C insert still needs a later separate Owner CONFIRM.

---

## 1. Constraint inherited from RTA (cite only; not re-proved here)

1. **Scalar W₇ no-go** (Thm 11.5(iii)): for no weight \(k\) and no constant \(\lambda\) is  
   \(C(\tau)-\lambda(7\tau)^{-k}C(-1/(7\tau))\) radially bounded at all rationals.  
   Consequence used here: any residual law compatible with RTA’s Bridge Series analysis must be **non-scalar**.

2. **Vector structure** (Thm 11.6): Siegel-theta lifts \(u_{\alpha,\beta}\) (140 labels) obey a unitary vector-valued \(S/T\) law; they span a **42-dimensional** subspace \(V\subset W_P\) (\(\dim W_P=72\)), with label representation isomorphic to the Weil representation of the even lattice \(N_2\).

3. **Leading order only** (RTA §1.3): the shadow \(\Xi\) is **not** identified; the vector-valued law of the related \(V_{35}\) story holds at leading order only.

4. **Cusp-pair limit** (RTA §14.1): at the cusp pair \((0,\infty)\), no **exact** vector-valued modular law with algebraic data can hold (Baker-conditional Cat A in RTA). So residual identification is at **leading radial order** only.

5. **Name collisions (must not reuse blindly):** in RTA, “B1” already means  
   - Bernoulli polynomial \(B_1(y)=y-\tfrac12\) (§2.1);  
   - the 1-dimensional summand of \(\rho_2\), with \(V_{\mathrm{cusp}}=B_1\otimes X^-\) (Thm 11.8 / Prop 19.4);  
   - the odd-\(d\) nonvanishing bound \(B_1=19\) (Thm on \(g_2\)).  
   None of these is the residual uniqueness symbol.

---

## 2. Proposed Owner Written text (ACCEPT / EDIT / REJECT)

> ### Write — residual_factor (vector)
>
> **(W2.1)** Consistent with RTA v12 Thm 11.5(iii) (scalar W₇ no-go) and Thm 11.6 (Siegel-theta vector law), the Bridge residual factor is **vector-valued**. No scalar modular or scalar W₇ slash residual law is admitted for `residual_factor`.
>
> **(W2.2)** Identify  
> \[
> \texttt{residual\_factor}\;:=\;\bigl(u_{\alpha,\beta}\bigr)\;\in\;V,
> \]  
> where \(V\) is the 42-dimensional \(S/T\)-invariant function span of the Siegel-theta lifts of RTA Thm 11.6 (Weil(\(N_2\)) label law), taken at **leading radial order only**.
>
> **(W2.3)** Do **not** claim: (i) identification of the shadow \(\Xi\); (ii) an exact algebraic vector law at the cusp pair \((0,\infty)\) beyond leading order; (iii) automatic Cat A transfer into residual-C; (iv) any uniqueness theorem for a residual scalar \(B_1\).
>
> **(W2.4) — B1 disambiguation (residual context).**  
> In residual / Bridge-C language, the symbol **`residual_B1`** (written out; not bare `B1`) means:  
> *the Author’s residual-side uniqueness / normalisation label for the vector `residual_factor` in \(V\)* — **and is not** the Bernoulli polynomial, **not** the \(\rho_2\) summand \(B_1\) with \(V_{\mathrm{cusp}}=B_1\otimes X^-\), and **not** the bound \(B_1=19\).  
> Until a separate Owner Write supplies a formula for `residual_B1`, its value and uniqueness proof remain **OPEN** (ABSENT as Cat A).

---

## 3. Owner choices still required before ACCEPT

| Choice | Options | Default in draft |
|---|---|---|
| A. Span | Full \(V\) (dim 42) vs \(V_{\mathrm{cusp}}\) (dim 6) vs “\(V\) or named sub-rep, Owner to specify later” | Full \(V\) (W2.2) |
| B. Symbol | Keep talking “B1” with collision warning vs rename to `residual_B1` | Rename to `residual_B1` (W2.4) |
| C. residual-C | Accept Write as Author Written guidance only vs also CONFIRM insert into residual-C now | Guidance only — **no insert** |

---

## 4. Standing after draft (unchanged until Owner ACCEPT)

- residual-C: **OPEN** (untouched)  
- Bridge: **PARTIAL** · READY: **NO**  
- Items (3)(4): still PENDING Owner Write  
- invent-ban: held  

## 5. Provenance

- Ledger Item 2: `ADOPTED_PATH_GUIDANCE_2026-10-25.md`  
- Shape candidate: `PURSUE_THREE_NEEDS_2026-10-25.md` Need (3)  
- NL geo-chase: ABSENT Written residual_factor/B1 (`FINDINGS_T_NL_GEO_BRIDGE_CHASE_RESUME` sha `4f84ffa2…`)  
