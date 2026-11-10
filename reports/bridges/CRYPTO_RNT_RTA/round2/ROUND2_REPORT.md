# Round 2: T3 itineraries → residues mod k vs OccFilt_k(∞)

For Arvin Hampton · 2026-10-23, about 10:16 PM CDT. Folder `bridges/CRYPTO_RNT_RTA/round2/`. Only new files were written. Nothing was pushed or sent.

## Conclusion
The itinerary route gives no bridge. I defined two natural maps from T3 itinerary words to residues mod k before any testing. Both are built from the affine form 3^j T3^j(n) = B_w n + C_w on a cylinder (proved, R0).
- **Multiplier B_w = 2^{a(w)}.** Proved to be a no-go before testing (R1). It gives no mass to the residue 0, so for odd k it can never reproduce the squares mod k. For k = 4, 8, 12 it collapses onto 0 or onto {4, 8}.
- **Translation constant C_w.** This one is order-sensitive and is not forced by P2/P3. It was tested exactly at j = 120 and **falsified**: the weak prediction held at 0 of 7 values of k and the strong one at 0 of 7. For odd k its law is uniform to all printed digits. For k = 4, 8, 12 it puts less mass on the squares than uniform does.
- **Open class k ≡ 0 mod 4.** The C-map "predicts" that MIX classes are outside OccFilt at k = 4 (c = 0) and k = 12 (c = 0, 4). That runs against the finite certificates, which show no zeros there up to 2·10⁷. At k = 8 the prediction is only conditional.

The Residual-vs-Resonant lock remains in force. P3 already showed that T3 is uniform on residue classes, and round 2 adds that T3's affine word data also carry no square-residue structure.

## Map table
| Map | Status |
|---|---|
| R-B multiplier w ↦ 2^{a(w)} mod k | proved no-go (R1) |
| R-C translation w ↦ C_w mod k | falsified (exact) |
| R-C on MIX classes (k = 4, 8, 12) | falsified at k = 4 and 12; at k = 8 conditional only |

## What would still be needed
A map that uses something beyond a single cylinder's affine data, for example the g_k-side variable d = n² + km itself. Any such map would have to be defined before testing, and it would no longer be a map from T3 alone. I see no natural candidate in the sources. I recommend closing the T3 ↔ g_k route as negative unless Arvin supplies a defining relation.

## Ledger
P1, P2 and P3 were added as entries **98, 99 and 100** in `s_family_paths/LEDGER_CatA_clean_v7/LEDGER_ADDENDUM_T3_2026-10-23.md` (+ .pdf). v7 ends at entry 97. The full v8 consolidation (A59, A60, A61, A48 REPORT_v3 and this addendum) is still pending.

Files: PREREG.md, PREREG.sha256, RESULTS.md, NOTES.md, scripts/rc.py, logs/.
