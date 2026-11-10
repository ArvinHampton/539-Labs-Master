# MR2 NOTE — QC of HW-plane Ricci²/Weyl² filing f4ee61f2, before send
2026-11-10, written 11:25:54 CST (America/Chicago). Additive MR2 record only. Nothing else is edited by this file. The parent report is unedited. Junction UNSOLVED. Wording: resonant algebra. Nothing is adopted. No CERT.

## Parent
- `/workspace/quantum-comp/reports/MR2_BRANCH_ATTEMPT_HW_FIXED_PLANE_BOUNDARY_RICCI2_WEYL2_2026-11-10.md`, sha256 `f4ee61f26ad536800792b510f29f714c9c622fd11a8c378e545a8a38976c330d` = sidecar, written 11:24:09 CST, header = mtime, mode 644.
- Script `/workspace/quantum-comp/reports/mr2_hw_plane_ricci2_weyl2_2026-11-10.py`, sha256 `cd289c73043595e303fc5f2d5a0c2e7ba0b2fa5b5cdef33489dcf0231a9c695d` = sidecar, frozen 11:21:00 CST, mode 444. Identical `cp -p` original in `/workspace/mr2-hw-curv-1110/`.
- Log `/workspace/quantum-comp/reports/mr2_hw_plane_ricci2_weyl2_2026-11-10.log`, sha256 `d5396417b7d3c3ad1212bb8748abe90b26910c89a448081334801038e10b6f23` = sidecar, mtime 11:21:49 CST, sidecar 11:21:55, mode 444. Identical original. First two lines: `RUN_START_WALLCLOCK 2026-11-10 11:21:05 CST` and `SCRIPT_SHA256 cd289c73…`. Freeze ≤ run start. Exit 0, `ALL_CHECKS PASS` (33 checks), `RUN_END_WALLCLOCK 2026-11-10 11:21:49 CST`.
- Tip `7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91` MATCH before and after this write. Not a tip edit.

## Integrity checked by MR2 (not the author of the parent computation)
- All inventory prefixes cited in the parent, plus 2368ffbd, 5511845e, and 384096a8, equal their live files and sidecars.
- No `simplify`, no floats, no `np.allclose` in the frozen script. `nsimplify` appears only in instance E1, already disclosed in the parent, to normalise an already-rational polynomial.
- Scratch pretest `/tmp/scratch_pretest.py` sha256 `8fccc9919e36fb11aac9d951dcf7494404565b38e8f21965b290a8f1c2ce0ffb` exists as disclosed; it is not cited as evidence.

## Self-disclosed nits (no grade proposed by this note; PP to audit the parent)
- N1. The parent title block says “by MR2 (executor)”. The author is Math Research 2. No existing file is edited.
- N2. §6 item 6 writes that odd G₄ with tangent legs forces the charge balance \(N_{M5} + n_{inst} = 2N = 9760\). The integer 9760 is the in-repo wall charge (PP aeb9ab13, exact), used as a **stated premise** in row 10, and is not adopted. Odd G₄ with bounded tangent legs forces the *form* of the charge balance; it does not by itself force that integer.
- N3. The inventory row for FINDINGS_PP_AUDIT_NL_Y14_STAGE2_Y15_FIBRE_ISRAEL_2026-11-09_1953.md is marked “(read)” with no sha. Independently: sha256 `077e417db7f24ece269d7dcde21bc89e260bbe1102d985c63ab60aa94813c23b` = sidecar.

No other grade or tally change is proposed here. Parent tally remains 12/2/2/1 = 17 + 1 bookkeeping, unadopted, pending PP. Junction UNSOLVED.
