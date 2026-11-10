# FINDINGS — Cat B loosen for 11D ↔ ternary merger — LQH ALU draft — 2026-11-05
Draft-only. No CERT. No publish/send/push. No proofs invented.

## 1. ACK
ACK Owner Soft SF as Written OW call-9ee0f248 — `/workspace/quantum-comp/reports/OWNER_WRITE_CALL_9ee0f248_LOOSEN_CAT_B_11D_TERNARY_MERGER_2026-11-05.md`, sha256 `ae380bf6c09980ec0a88dabbb02347a873b672f2b62b7f68fba2d5ddec9b30fa` (re-verified on disk 2026-11-05 ~12:10 CST). Loosen = relax Cat B as hard barriers so they can be bridged into Cat A / Soft SF-confirmed math; not proof, not CERT.

## 2. Inventory (Cat B / ENGINEERING / INVENT-PENDING touching 11D ↔ ternary)
| # | Location | Claim | Old tag | Merger-relevant? |
|---|---|---|---|---|
| I1 | ARCH §2.1 | Balanced ternary / SU(3) generators | ESTABLISHED | Yes (already Cat A-side; no change) |
| I2 | ARCH §2.2 | 128-trit word width | ENGINEERING | Weak; unchanged |
| I3 | ARCH §2.2 | 128 LQH = FT DOE logical qubits / SU(3) "manifold locking" replaces QEC | INVENT-PENDING | Yes — **refused** (O3) |
| I4 | ARCH §2.3 | SU(3)_c → discrete / 3-adic dictionary | INVENT-PENDING | Yes — **loosened** (L1) |
| I5 | ARCH §3 | SFQ / memristor LQH cell readiness | INVENT-PENDING | Substrate — **refused** (O4) |
| I6 | ARCH §4 | Dual-rail defeats AI-SCA / ISO 17825 timing-safe | INVENT-PENDING | **refused** (O2) |
| I7 | ARCH §5.1–5.2 | HQH-539-512: 539 Canonical T3 steps, residue-1 branch 4q+2, SHA3 sandwich | ENGINEERING | Yes — basis of L3/L4 |
| I8 | ARCH §5.3 | Shor/Grover immunity, complexity class, proven PQ reduction | INVENT-PENDING | **refused** (O1) |
| I9 | ARCH §5.4 | Qutrit flux Φ_q = 61 tied to 539-step narrative | INVENT-PENDING | Yes — **loosened** (L2) |
| I10 | ARCH §6 | Planning LUT/Fmax | INVENT-PENDING | No; unchanged |
| I11 | ARCH §8 Q5 | Trit-ALU ↔ T3 residue-mux coupling | open question | Yes — **loosened** (L3) |
| I12 | ALU_SPEC §1 | 2'b11 encoding optimal for SFQ/memristor | INVENT-PENDING | Substrate — unchanged (O4) |
| I13 | ALU_SPEC flags | "multiples of 539" unstable_path_flag | INVENT-PENDING | Not adopted; unchanged (O5) |
| I14 | ALU_SPEC timing | Measured constant-time / TVLA | INVENT-PENDING | **refused** (O2) |
| I15 | ALU_SPEC §6 | ALU word arithmetic ↔ T3 engine relation | (untagged) | Yes — **loosened** (L4) |

## 3. Loosened items (new tag `[BRIDGE-CANDIDATE-CatB→CatA]`, all "not proven")
- **L1 (I4, ARCH §2.3)** Old: `[INVENT-PENDING]` "physics dictionary is not a verified hardware netlist constraint". New: `[BRIDGE-CANDIDATE-CatB→CatA]` SU(3)_c → discrete/3-adic dictionary is a bridge candidate between the 11D/nonlocal stream and T3 local modular stream; required bridge object = explicit map from SU(3) generators to operators on Z_3-valued words, to be checked against Cat A / Soft SF filter items. Not proven. The INVENT-PENDING "not a netlist constraint" line is **retained**.
- **L2 (I9, ARCH §5.4)** Old: `[INVENT-PENDING]` out of scope. New: `[BRIDGE-CANDIDATE-CatB→CatA]` Φ_q = 61 is a bridge candidate to be restated as a definable math claim (NEEDS-DEFINITION) about the 539-step T3 walk and tested against Soft SF-proven T3/RTA results. Not proven. "Not a hardware verification oracle" INVENT-PENDING line **retained**.
- **L3 (I11, ARCH §8 Q5)** Old: open question. New: `[BRIDGE-CANDIDATE-CatB→CatA]` trit-ALU ↔ T3 residue-mux coupling is the engineering locus of the merger; T3 residue-class semantics (Canonical residue-1 branch 4q+2) is the bridge point to Cat A. Not proven; §5.3 security claims explicitly do not loosen.
- **L4 (I15, ALU_SPEC §6)** New: `[BRIDGE-CANDIDATE-CatB→CatA]` exactly-checkable balanced-ternary arithmetic + T3 residue map form a bridge candidate between ALU semantics and Soft SF-proven T3 math. Not proven. Following INVENT-PENDING security sentence **retained**.
- Tag legends in both files extended with the new tag + "not proven, no CERT".

## 4. Soft SF objections (refused to loosen)
- **O1** Shor/Grover immunity, novel complexity slice, "proven" PQ reduction for HQH-539-512 — stay hard INVENT-PENDING. Loosening security claims into a bridge would read as near-proof; bare T3 is not collision-resistant; no reduction exists.
- **O2** SCA/TVLA / ISO 17825 / AI-SCA "defeat" — measured-hardness claims need board traces; no bridge wording substitutes for measurement.
- **O3** 128 LQH = fault-tolerant DOE logical qubits / SU(3) manifold locking replacing QEC — fault-tolerance counts need a named [[n,k,d]]_3 code; stays INVENT-PENDING.
- **O4** Substrate readiness (SFQ cells, memristor dual-rail arrays, 2'b11 optimality) — engineering/fab facts, not math bridges; unchanged.
- **O5** "Multiples of 539" unstable_path_flag and Codex Module 5 investor/IP pitch (outbound Cat A/B 539labs voice) — not loosened, not adopted; no CERT-adjacent or "immunity" language introduced anywhere.
- T4121 remains banned; T3 only (no T4121 occurrences in draft folder).

## 5. Locks
tip Soft SF LOCK `7cddb188…` — tip_touched NO. No CERT. Draft-only; nothing published, sent, pushed, or spent. Soft SF unpaid: PRESS + PP Soft SF / Keeper per OW §5 (not done here).
