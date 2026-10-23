# Notes for updating the Zenodo record (not part of the PDF)

Record: 10.5281/zenodo.21536802 (v1 dated 24 July 2026). Nothing has been uploaded, pushed or sent; this file only prepares the update.

1. **Create a *new version* of the existing record** (Zenodo "New version" button) so the DOI concept is preserved, and upload `PureEven_MultiK_v2.pdf`. Set the version field to `v2` (or `2`).
2. **Resource type.** Set *Resource type* to **Publication → Preprint** (a research note / preprint, not a journal article). If "Preprint" is not offered in the form, use **Publication → Report** or **Working paper**; do not use "Journal article".
3. **Title** (unchanged): *Pure-Even Multi-k Families and the Arithmetic Core of Resonant Algebra*. **Author:** Arvin B. Hampton.
4. **Description / abstract** (arithmetic only; paste from the PDF abstract): Bring–Jerrard quintics $x^5+\alpha x+\beta$ with square discriminant are exactly the members of the two-parameter family $f_{m,k}$, $\alpha=256m^2-3125k^4/256$, $\beta=k\alpha$, $\operatorname{disc}=(256\alpha^2m)^2$; precise discriminant-height formula; explicit cross-k paths; Hilbert irreducibility consequence ($A_5$ is the generic group on every slice, $O(N^{1/2})$ integer exceptions); explicit degree-6 resolvent and a conic parametrisation of the $D_5$ fibres; reproducible computations on slices k = -8/5, -4, 4/5; Belyi negative control ($S_5$).
5. **Keywords:** Bring–Jerrard quintic; Galois group; A5; D5; Hilbert irreducibility; sextic resolvent; inverse Galois problem; discriminant.
6. **Subjects/classification** (optional): MSC 12F12 (inverse Galois theory), 11R32 (Galois theory), 12E05.
7. **Companion files.** The PDF states that the scripts used for its numbers are in a `scripts/` folder (plus `data/`) distributed with the note. If you want them on Zenodo, upload `scripts/` and `data/` from the same folder as additional files (zip them); the PDF does not claim any contents of the GitHub repository https://github.com/ArvinHampton/resonant-galois, whose contents were not inspected.
8. License and funding fields: keep as in v1.
