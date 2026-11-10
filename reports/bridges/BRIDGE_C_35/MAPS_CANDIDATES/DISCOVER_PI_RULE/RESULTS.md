# RESULTS: DISCOVER_PI_RULE
PREREG sha256 f836369c6672361504992d3fe47f988c5a6f2e1a9701b51d699921f6773b96ee, hashed before the tests. Script hashes are in scripts/SHA256SUMS.

**Verdict: OBSTRUCTION.** Residual Category A structure does not force a unique non-degenerate 539-step Π word. RP1 shows that the word is exactly the seed mod 3^539, and every word occurs. RP2 shows that P_res only marks the local pattern "01".

| Test | Result | Category |
|---|---|---|
| T1: C10 on Π*_C1 = 0^539 (forced by C1, trivial-seed word) | 1 segment → **FAIL** | A |
| T2: C10 on Π*_max = (01)^269 0 (sha256 c2c26fda…) | 539 segments → **FAIL** | A (exact); the rule itself is a free extremal choice |
| T3c: RP4 uniqueness depends on the w_539 convention | 810 maximisers without it → **PASS** (confirms the uniqueness is fragile) | A |
| Map-C6 | **NOT RUN** (mod-4 S-profile undefined in the source) | — |

Map-C10: every canonical candidate fails. In fact, any word with exactly 4 constant-branch segments has at most 3 "01" transitions, so it carries at most 3 P_res hits (Category A). C10 is therefore essentially incompatible with a resonant (hit-rich) Π. Map-C6 stays OPEN/undefined. **Bridge: NO.**

Open next: the smallest forcing pattern would be a source-written selection on x mod 3^539 (for example "Π := the max-P_res word with terminal hit", which would make RP4 the rule), or an operational definition of C6's "mod-4 profile". Both are decisions for Arvin.
