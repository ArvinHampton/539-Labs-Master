# Kernel construction for Remark 8.5

Date: 2026-10-03
Status: exploration. No kernel constructed. Not a reopening.
CORE_FREEZE unchanged. No new residual-flux object.

## Construction

A two-sided factor needs a kernel. On the Dual-plus-minus cocycle matrix M, a kernel vector v satisfies M v = 0. Object A in Theorem 8.4 is that kind of vector for a different matrix. Remark 8.5 asks for a factor that acts on both sides, so the construction would also need a left vector w with w M = 0, and a factorization through those vectors.

## Obstruction already recorded

The Dual-plus-minus matrix is 8 by 8. Its smallest singular value is 6.38. A singular value that far from zero means there is no right kernel and no left kernel. residual_slash was the candidate and cannot be Object B. Nineteen candidates were refused on 13 September. No fourth matrix was written.

## What is not a construction

Inserting a vector and calling it a kernel does not make M v zero. Rescaling M does not create a zero singular value. Identifying Slash_two with Object B, with Per_off, or with the tubulin card does not produce w or v. The tubulin card is off this stack.

## Close of this pass

No kernel is constructed. Slash_two stays empty. Theorem 8.4 stays Object A only. The next step remains the one already named: an operator in the written Pack+(S) data that is not residual_slash, or a negative close.
