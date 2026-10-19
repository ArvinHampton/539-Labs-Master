# NOTE — invalid-evidence scripts in this package

The following scripts build the label maps neg and Z_q with the transposed convention X[j(i),i]:
- comm_modl.py
- irr_modl*.py
- split_modl.py
- vecfam.py
- vec_check.py
- sec_sparse.py
- sec_valid.py
- p_old.py

Their "sectors" are therefore not ρ-invariant, and their outputs (in OUTPUTS_BUNDLE) are **invalid evidence**. They are kept for provenance only. This also covers the 21:15 CDT "retraction" section of the snapshot, which is superseded.

The valid evidence is:
- Symmetry_Audit_2026-10-18/ (sec_fixed, p_old_fixed, exact_commute);
- sec_fixed_49_1,1.json;
- lift_check.json;
- hcountB, hcountC, hcountD (orbit-sum ranks; independent of the label maps);
- factor_dims*;
- weil_cyclic*.

See ERRATUM_2_Rev5_2026-10-18.md.
