# 539-Labs-Master — directory overview

Updated 2026-07-31. For cross-repo layout see [REPOS.md](REPOS.md).

```text
539-Labs-Master/
├── README.md                 # Entry point: T3, raw vs resonant, Category A/B
├── REPOS.md                  # Full GitHub map (roles of every repo)
├── SECURITY.md               # Claim-labeling protocol
├── PROPRIETARY.md
├── PAPERS.md                 # Paper / Drive index
├── TREE.md                   # This file
└── docs/
    ├── Quantum-Comp-Recommended-Skills.md
    ├── hqh539-verification/  # KAT / avalanche / goldens / profile freeze
    │   ├── hqh539.py
    │   ├── crypto_hqh.py
    │   ├── golden_vectors*.json
    │   ├── avalanche*.py / benchmark*.py
    │   └── rtl_vectors*/     # stimulus / expected .dat
    └── S2-11DM2ET-X-Axiomatic-Book/   # Living axiomatic book (main body)
        ├── README.md         # Topic index (start here)
        ├── PROGRAMME_BASELINE.md
        ├── CLAIM_TABLE_Master.md
        ├── PROVENANCE_TABLE.md
        ├── CLOSED_CONSTANTS.md
        ├── Foundational_Arithmetic_Packaging.md
        ├── Object539_NonCircular_Construction.md
        ├── Resonant_Layer_Resolved.md
        ├── H0_539_Honest_Options.md
        ├── NoGo_Theorem_Canonical.md
        ├── Architecture_A_*  # A0–A5⁺ residual stack
        ├── Residual_*        # product complex, form SS, P+
        ├── HQH539_Security_Reductions_Exploration.md
        ├── HQH539_Formal_Games_and_Hard_Problem_Pi.md
        ├── RH_*              # pure Cat A RH research track
        ├── rh_pure_cata/     # RH pure-Cat-A extract pack
        ├── Executive_Summary_*.md
        ├── PUSH_LOG_*.md
        ├── scripts/          # probes and verifiers
        └── data/README.md    # bulk datasets offline
```

**Not present in this repo (despite older notes):** top-level `hqh539/python/`, `docs/hqcc/`, `docs/model/`, `docs/papers/`. Those roles are covered by `docs/hqh539-verification/`, the axiomatic book, and [PAPERS.md](PAPERS.md).

**Hardware / RTL** live in [539-Labs-repo](https://github.com/ArvinHampton/539-Labs-repo).  
**Live product** lives in [hqh539-engine](https://github.com/ArvinHampton/hqh539-engine).
