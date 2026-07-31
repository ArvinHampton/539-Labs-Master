# Pair correlation — practical status for the pure Category A programme

**Status label:** `RH_OPEN_DEBT_ARGUMENT_NOT_A_PROOF`  
**Category:** pure **A**.  
**Axiom ZLA** applies. No model constants. RH open.

**Companions:** `RH_Remaining_Analytic_Obligations.md` (O-PC), `RH_L4_NonCircular_Checklist.md`, `RH_Zeta_Language_Admissibility.md`.

---

## Practical status (frozen)

1. **Pair correlation is a classical, ZLA-admissible source of constraints on zeros.**  
   Montgomery’s pair correlation conjecture (PCC) and its partial theorems / form-factor asymptotics are statements about the zeros of \(\zeta\) (or about sums over those zeros). They use only zeros, \(\zeta\), and classical auxiliaries — **in-language** under Axiom ZLA.

2. **Under PCC (or strong enough partial pair correlation), one already has strong almost-all statements about simplicity and criticality.**  
   Classical consequences in the literature (almost all zeros simple; almost all on the critical line, in the sense of density-one sets of ordinates under the stated hypotheses) are **not re-proved here**; they are recorded as **known infrastructure** feeding the zero-side of the phase programme. They constrain the **spectral** side (zeros), not yet the **phase of the partial Euler product**.

3. **Pair correlation has not yet been converted into the phase lower bound required by the target lemma.**  
   The conversion has **not** been carried out. Full specification of the required implication, the four missing steps (local isolation → hybrid \(\arg Z_X\) → remainder domination → transfer to \(P_X/A_X\)), and why PCC / \(S(t)\) / diagnostics do not close the gap:  
   **`RH_OPC_Conversion_Gap.md`**.

4. **O-PC therefore remains open.**  
   Goal of O-PC: rigorous translation of pair-correlation type hypotheses into **phase** lower bounds for \(P_X\) / \(A_X\), with tracked errors, ZLA-clean.

5. **Position in the dependency ledger:** O-PC sits **upstream of, or parallel to, O-M1.2**.  
   - **Upstream:** a PC\(\to\)phase theorem could supply zero-spacing / isolation input that makes uniform M1.2 easier.  
   - **Parallel:** M1.2 can also proceed from classical zero-density alone (O-M1.2 as stated), without PC.  
   Either route may feed O-M1.3bis \(\to\) M1.4 \(\to\) O-TL. O-PC is **not** optional decoration; it is a **first-class open obligation**, but **not** the unique gate to O-M1.2.

---

## What this is not

| Claim | Status |
|-------|--------|
| PCC proved | **No** (conjectural; partial results classical) |
| Almost-all simplicity/criticality under PCC re-derived in this repo | **Not claimed** — cited as classical under PCC |
| O-PC closed | **No** |
| Target lemma / RH | **Open** |
| Pair correlation replaces O-M1.2 | **No** — upstream or parallel only |

---

## Revised dependency sketch (O-PC)

```
                    ┌──► O-M1.2 (classical density alone)
O-PC (open) ────────┤
                    └──► (feeds spacing / almost-all input)
                              │
O-Moll (optional) ────────────┤
                              ▼
                         O-M1.3bis ──► M1.4 ──► O-TL
```

---

## One-liner

**Pair correlation is ZLA-admissible classical input and already yields strong almost-all zero statistics under PCC, but it has not been turned into a phase lower bound for \(A_X\); O-PC stays open, upstream of or parallel to O-M1.2.**

*Per aspera ad astra.*
