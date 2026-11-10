#!/usr/bin/env python3
"""Typed check for the three Bridge Series C open problems (Owner voice call-1f7b6901, 2026-11-09 ~4:22 PM CST).
Each problem is a typed item made of obligations. Every obligation has a status label and an evidence file on disk.
An item is CLOSED only when every obligation is PROVED or an Owner DEFINITION. Each item closes independently:
to close one, add a new dated evidence file and update the status here in a new dated copy of this script (additive only).
The script verifies every evidence file exists and matches its .sha256 sidecar; a missing file or a mismatch fails the item."""
import hashlib, os, sys
from dataclasses import dataclass
from enum import Enum
R = os.path.dirname(os.path.abspath(__file__))
class S(Enum):
    PROVED="PROVED"; DEFINITION="OWNER DEFINITION"; CONDITIONAL="CONDITIONAL"; OPEN="OPEN"; REFUTED="REFUTED"
@dataclass
class Ob:
    name: str; status: S; evidence: str; note: str = ""
@dataclass
class Item:
    key: str; claim: str; obs: list
def sha(p):
    return hashlib.sha256(open(p,'rb').read()).hexdigest()
def check_ev(rel):
    p=os.path.join(R,rel)
    if not os.path.exists(p): return "MISSING"
    sc=p+".sha256"
    if not os.path.exists(sc): return "NO-SIDECAR"
    want=open(sc).read().split()[0]
    return "MATCH" if want==sha(p) else "MISMATCH"
XI_D="FINDINGS_LOCAL_DERIVE_XI_WEIL_VECTOR_CARRIER_FRICKE_PLUS1_DICTIONARY_2026-11-09.md"
XI_A="FINDINGS_PP_AUDIT_LOCAL_XI_WEIL_CARRIER_FRICKE_DICTIONARY_2026-11-09_1525.md"
BP="OWNER_WRITE_MAINCHAT_BLUEPRINT_1509_CORRECTED_ADOPTED_2026-11-09_1511.md"
DEF="RECORD_PP_LAMBDA0_RC_OWNER_DEFINITIONS_OW5a6e7177_2026-11-09_1515.md"
RCM="FINDINGS_PP_RC_KAPPA_VS_LADS_MISMATCH_2026-11-09_1515.md"
APP="FINDINGS_PP_AUDIT_MR1_S2_S4_APPELL_RC_2026-11-09_1516.md"
NLV="NL_DERIVED_TWISTED_VACUA_STABILITY_SPECTRUM_COMPARE_MN2_MN1_BBBW_N4880_G2_2026-11-09_1620.md"
L2="FINDINGS_PP_DERIVED_DEFS_D1_LAYER2_SEFF_T3_2026-11-09_1309.md"
ITEMS=[
 Item("P1 Xi","Xi is identified, so Bridge C A1 -> Xi -> RTA is complete",[
  Ob("Xi carrier type: +1 law on a vector-valued Weil carrier, not 49a1 (Owner blueprint correction)",S.DEFINITION,BP),
  Ob("LD-Xi1 (a),(b),(c): W49 acts as -1 on 49a1, S2(G0(49))+ = 0, g+ Eisenstein",S.PROVED,XI_A),
  Ob("LD-Xi3 twist f(x)chi, level 19600, Fricke +1",S.PROVED,XI_A),
  Ob("LD-Xi2 induced carrier (tautological by construction)",S.CONDITIONAL,XI_A),
  Ob("chi140 Weil character for all of G0(140)",S.CONDITIONAL,XI_A,"standard theorem, Bruinier LNM 1780; numerics on 34 elements"),
  Ob("Joint carrier level: 980 minimal; 'joint carrier' itself undefined",S.OPEN,XI_A),
  Ob("Owner adoption of one specific Xi (the object itself)",S.OPEN,XI_D,"no OWNER_WRITE names Xi"),
 ]),
 Item("P2 R_c / junction / Layer2","R_c, the junction and the Layer2 transfer have a source in the math corpus",[
  Ob("R_c := kappa*l_P, kappa = sqrt(2/Lambda0)",S.DEFINITION,DEF,"Owner 3:11 PM; DP-Rc not adopted"),
  Ob("R_c != L_AdS/2 forces nothing (independent scales)",S.PROVED,RCM),
  Ob("Physical role of an l_P-scale R_c in the vacuum",S.OPEN,RCM,"E4: Owner must define"),
  Ob("Appell-Lerch -> R_c route (S2b, S4b, S4c)",S.OPEN,APP),
  Ob("Israel junction: brane and face definitions; warped/twisted fibre",S.OPEN,NLV,"D3: no Owner record defines brane or face"),
  Ob("Layer2 D1-norm referent (DP-a)",S.CONDITIONAL,L2,"derived proposal pending Owner adoption"),
  Ob("Layer2 D1-norm -> Kerr area transfer",S.OPEN,L2,"a-5; only source of 'Layer2 LOCKED' is attach a71f388e"),
 ]),
 Item("P3 Lambda0","Lambda0 is fixed without circularity, so step one is not circular",[
  Ob("Lambda0 := ln(6+sqrt35)/sqrt10",S.DEFINITION,BP,"Owner 3:11 PM; definition, not derivation"),
  Ob("Lambda0 = sqrt(7/8) L(1,chi140) (class-number identity, bnfcertify)",S.PROVED,XI_A),
  Ob("kappa = sqrt(2/Lambda0) = 1.597622 arithmetic",S.PROVED,DEF),
  Ob("Derivation of Lambda0 from the dynamics (physical meaning beyond F1-F3)",S.OPEN,DEF,"not needed for non-circularity"),
 ]),
]
CLOSING={S.PROVED,S.DEFINITION}
def run():
    out=[]
    for it in ITEMS:
        bad=[]; fail=False
        out.append(f"== {it.key}: {it.claim}")
        for o in it.obs:
            ev=check_ev(o.evidence)
            if ev not in("MATCH",): fail=True
            out.append(f"  [{o.status.value:16}] [{ev:10}] {o.name}" + (f"  ({o.note})" if o.note else ""))
            if o.status not in CLOSING: bad.append(o)
        st="TYPE ERROR (evidence)" if fail else ("CLOSED" if not bad else ("PARTIAL" if len(bad)<len(it.obs) else "OPEN"))
        out.append(f"  -> {st}; blocking: {len(bad)} ({', '.join(b.status.value for b in bad)})")
    return "\n".join(out)
if __name__=="__main__":
    print(run())
