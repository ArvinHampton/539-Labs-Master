# RFC (OPTIONAL, NOT ACCEPTED): Reintroduce product DOMAIN string

**Status:** DRAFT / DEFERRED  
**Parent freeze:** Option A (Canonical REF is law) — `DOMAIN_SEP = b""` for product REF.

## Proposal

Optionally restore `DOMAIN_SEP = b":HQH-539-RESONANT:"` (or a shorter RTL-friendly constant) for:
- Phase3 RTL padding/domain separation
- Explicit domain separation between HQH modes (STD / KDF / SIG)

## Why deferred

1. Option A freezes engine REF with **empty** domain.
2. Current Phase3 RTL still embeds a product domain constant for historical vectors.
3. Changing domain is a **breaking** digest change; requires new KATs + re-vector + peer communication.

## Acceptance criteria if revived

- [ ] Explicit product version bump / profile id
- [ ] Dual KATs (REF-empty vs DOMAIN-tagged) for one release cycle
- [ ] Engine `DOMAIN_SEP`, Phase3 RTL, and docs updated in one commit
- [ ] Security language unchanged (still pending reduction)

**Do not implement until this RFC is ACCEPTED.**
