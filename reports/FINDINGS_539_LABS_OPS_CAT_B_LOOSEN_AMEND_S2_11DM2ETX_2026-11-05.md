# FINDINGS AMEND — 539 Labs Ops / LQH ALU: loosen Cat B under S²-11DM²ET-X — 2026-11-05 ~12:15 CST America/Chicago
**ACK: OW `2c341bc70bbe9c064cb40641ba0d66dbae815053e62be998c55671d231686e49` MATCH (AMENDS ae380bf6c09980ec0a88dabbb02347a873b672f2b62b7f68fba2d5ddec9b30fa)**. I re-hashed it this turn.
AMENDS (does **not** edit) prior Ops FINDINGS `02b39a1556e4c6fc2e6dfb5013b85d4ce0174b8ad20c188ba64309a47ab0a22d` (`FINDINGS_CAT_B_LOOSEN_11D_TERNARY_2026-11-05.md`). tip Soft SF LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` — tip_touched **NO**. **No CERT.** Draft-only. REPORTS ONLY. Nothing published, sent, pushed, or spent. No invented proofs, measured traces, fake numbers, or CERT-adjacent security upgrades. Ops lane is LQH ALU engineering (not Eigen math).

## Framing (per AMEND §1–3)
The **S²-11DM²ET-X** extension of GR **encompasses the Category B side** of the LQH ALU / 11D ↔ ternary merger. Soft SF-loosened Cat B language **permits**:
- research and discussion under Cat B;
- adaptation of **alignment with observable datasets** (dataset classes named **generically only** — e.g. GW/EHT-type observational series, decoherence / noise-channel measurements, FPGA timing traces, Verilator sim logs, LMFDB-type tables; **no** specific dataset asserted, **no** alignment performed, **no** invented numbers).

Merger wording stays conditional: "*if* [Cat B item] holds within S²-11DM²ET-X, *then* it is consistent with / bridges to [Soft SF-proven T3 / Cat A math]". Soft SF does **not** invent proofs; Soft SF does **not** CERT. Invent-pending honesty fences on SECURITY claims are **not** upgraded to proven.

## Before → after (L1–L4 + newly framed items under looser standard)
| # | Claim / locus | Before (02b39a15…) | After AMEND (S²-11DM²ET-X Cat B) | Generic dataset class (alignment permitted, not done) | Status |
|---|---|---|---|---|---|
| L1 | SU(3)_c → discrete / 3-adic dictionary (ARCH §2.3) | `[BRIDGE-CANDIDATE-CatB→CatA]`; not proven; netlist INVENT-PENDING retained | Same bridge-candidate + **S²-11DM²ET-X Cat B research/discussion permitted**; *if* an explicit generator→ℤ₃-word map holds in S²-11DM²ET-X, *then* it bridges to Soft SF-proven T3/local modular stream. Netlist "not a verified hardware constraint" honesty line **kept**. | LMFDB-type / modular-form coefficient tables; decoherence / three-level system lab traces (generic) | Framing update; **not proven**; NEEDS-DEFINITION for math merge |
| L2 | Φ_q=61 / 539-step narrative (ARCH §5.4) | `[BRIDGE-CANDIDATE-CatB→CatA]`; not proven; "not a hardware verification oracle" retained | Same + **S²-11DM²ET-X Cat B research/discussion + dataset framing**; *if* Φ_q=61 restated as a definable claim holds, *then* it is consistent with Soft SF-proven T3/RTA results. Oracle honesty line **kept**. | Flux / phase simulation logs; Verilator / lab self-test trajectory logs (calibration only) | Framing update; **not proven**; NEEDS-DEFINITION |
| L3 | trit-ALU ↔ T3 residue-mux coupling (ARCH §8 Q5) | `[BRIDGE-CANDIDATE-CatB→CatA]`; not proven; §5.3 security does not loosen | Same + S²-11DM²ET-X Cat B research permitted; engineering locus of merger; *if* residue-class semantics couple as stated, *then* bridge to Cat A T3 (Canonical residue-1 branch 4q+2). §5.3 security **still hard invent-pending**. | FPGA timing traces; Verilator sim logs (generic) | Framing update; **not proven** |
| L4 | ALU word arithmetic ↔ T3 engine (ALU_SPEC §6) | `[BRIDGE-CANDIDATE-CatB→CatA]`; not proven; security sentence retained | Same + S²-11DM²ET-X Cat B research/discussion; *if* exactly-checkable balanced-ternary + T3 residue map holds, *then* ALU semantics bridge to Soft SF-proven T3 math. Security invent-pending **kept**. | Verilator KATs / sim logs; FPGA timing traces (generic) | Framing update; **not proven** |
| N1 (was O3 research slice) | FT / `[[n,k,d]]_3` / "manifold locking" as research topic (ARCH §2.2) | Hard refuse to loosen into bridge (prior O3) | **RELAXED into permitted Cat B research/discussion** within S²-11DM²ET-X: naming a candidate `[[n,k,d]]_3` (or qubit) code and studying syndrome/embedding is research-permitted. Claim that 128 LQH *is* FT DOE logical qubits, or that SU(3) manifold locking *replaces* QEC, remains **not proven** / **NEEDS-DEFINITION** — do **not** treat as bridge-proven. | Quantum-error / syndrome benchmark datasets; decoherence measurements (generic) | Research-permitted; **not proven** |
| N2 (was O4 research slice) | Substrate (SFQ / memristor / 2'b11 optimality) as Cat B research topic (ARCH §3, ALU_SPEC §1) | Hard refuse as fab/engineering fact (prior O4) | **RELAXED into permitted Cat B research topic** within S²-11DM²ET-X (analogous to Eigen O4 hardness/physics). Substrate may be discussed and aligned toward observable lab datasets. **Not** a fab-ready / foundry-ready claim; invent-pending honesty on cell libraries and arrays **kept**. | FPGA timing traces; cryogenic / SFQ lab pulse logs; memristor array characterization traces (generic) | Research-permitted; **not** fab-ready; **not proven** |

Tag legends in `ARCHITECTURE.md` / `ALU_SPEC.md` lightly updated to cite OW AMEND `2c341bc7…` / S²-11DM²ET-X Cat B research-permitted framing on L1–L4; invent-pending honesty lines retained.

## Objections revisited
### KEEP HARD invent-pending (do **not** loosen into proven; fences stand)
- **O1-sec** Shor/Grover immunity, novel complexity-slice, "proven" PQ reduction for HQH-539-512 — stay hard `[INVENT-PENDING-unverified]`. Bare T3 is not collision-resistant; no reduction exists. Soft SF does not invent a proof.
- **O2-meas** Measured SCA/TVLA / ISO 17825 / AI-SCA "defeat" **as fact** — stay hard invent-pending. No board traces in this tree; bridge wording does not substitute for measurement.
- **O5-pitch** Outbound Codex Module 5 investor/IP pitch language of "immunity" / complexity-slice as sellable fact — **not** adopted, **not** loosened, **not** CERT-adjacent. "Multiples of 539" `unstable_path_flag` remains not adopted.
- T4121 remains banned; T3 only.

### MAY RELAX (permitted Cat B research/discussion + generic dataset alignment; still **NOT proven**, NEEDS-DEFINITION for math merge)
- **O3→N1** FT / `[[n,k,d]]_3` research discussion (and related "manifold locking" as a research question) — permitted under Cat B / S²-11DM²ET-X; does **not** become a proven FT claim or QEC replacement.
- **O4→N2** Substrate as Cat B research topic (physics/hardness-adjacent, analogous to Eigen Soft SF AMEND O4) — permitted research/discussion + dataset alignment; **not** fab-ready.
- **L1 / L2** Φ_q=61 and SU(3) dictionary (already bridge-candidates) — get explicit **S²-11DM²ET-X + generic dataset framing**; remain **not proven** / NEEDS-DEFINITION for merge.
- **L3 / L4** engineering bridge loci — same S²-11DM²ET-X framing; security sentences stay invent-pending.

**Hard invent-pending retained:** O1-sec, O2-meas, O5-pitch (and related SECURITY claims).  
**Relaxed into Cat B research (not proven):** N1 (ex-O3 research slice), N2 (ex-O4 research slice), plus L1–L4 S²-11DM²ET-X framing.

## Locks
tip Soft SF LOCK `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` — tip_touched **NO** (this task did not open, edit, or fold tip / 7cddb188 paths). **No CERT.** Draft-only; nothing published, sent, pushed, or spent. Soft SF unpaid PRESS → PP Soft SF / Keeper per OW (not done here).
