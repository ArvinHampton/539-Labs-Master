# FINDINGS — NL Soft SF backup naming (t2158u, 2026-10-25, America/Chicago)

## Convention (REGISTERED)
NL stub backups MUST be `obs-bridge-NL-61Omega-photon-brane.pre-<tag>-<8hex>.md` (insert `.pre-` before tag; never `….md.pre-…`). <8hex> = first 8 hex of backed-up content sha256.

## Renames (mv; content sha MATCH)
1. /workspace/obs-bridge-NL-61Omega-photon-brane.md.pre-crosslist-lag-fc14a0a3.md → /workspace/obs-bridge-NL-61Omega-photon-brane.pre-crosslist-lag-fc14a0a3.md — fc14a0a3a26668df19888de68933fb41c55aa67d7523be7538c5def9ea6873b0 MATCH
2. /workspace/obs-bridge-NL-61Omega-photon-brane.md.pre-next-promote-8a4b8406.md → /workspace/obs-bridge-NL-61Omega-photon-brane.pre-next-promote-8a4b8406.md — 8a4b84061b65fc96d37b5a35043877a50bd71a5a0231f654656848c3cbe0ac0f MATCH
3. /workspace/obs-bridge-NL-61Omega-photon-brane.md.pre-pursue-resolutions-8a4b8406.md → /workspace/obs-bridge-NL-61Omega-photon-brane.pre-pursue-resolutions-8a4b8406.md — 8a4b84061b65fc96d37b5a35043877a50bd71a5a0231f654656848c3cbe0ac0f MATCH
No .sha256 sidecars existed for old backup names.

Already correct (left): /workspace/obs-bridge-NL-61Omega-photon-brane.pre-softsf-tippin-6f0f9a7a.md — 6f0f9a7acb44a6ac7d0ff74241ecda2c7e9fe01e2c8aa7b464c45901208193db

## Stub
Stub body had no full `.md.pre-…` cites (no cite edits needed). Pre-edit backup /workspace/obs-bridge-NL-61Omega-photon-brane.pre-backup-naming-644c235c.md (644c235c… MATCH). t2158u log line appended: 644c235cf4158d3c7392ead7cda51930e2adcd9da34422894993f8431d44873d → a3127f4a8dc666668e0daa6e97e3cd249609078d04c238d480aff690ee866d23; sidecar updated.

## Status
tip Soft SF LOCK d0b1e3016182eab1522c5fa6b2743e7c8c48d5446d8b0e59b3acfdd61bb09851 — tip_touched NO.
Soft SF history: sealed packs (t2132u–t2156u) citing `.md.pre-…` paths left unchanged (history).
Packaging f_*/Ω/ω Owner-hold; Q7 KEEP; Bridge PARTIAL / READY NO. Rename + documentation only; nothing invented.
