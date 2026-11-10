# FINDINGS — Local Soft SF ACK: NOT-FEASIBLE RETRY 24h — 2026-10-27 (CDT)
Mode: Soft SF Write-only status ACK. REPORTS ONLY. No RECS. No invent.

## Live binds
| Clause | sha256 |
|---|---|
| tip Soft SF LOCK | 7cddb188ca340ad977516327065e8df88c3b16ed01bcd8301c5bf0f8bb5dfc91 tip_touched NO |
| OW NOT-FEASIBLE RETRY 24h | 291b54ea8bf86830071f7f91781cb5a6a408a9e49e771d7ddaf3db7b8c8238d5 |
| OW invent lift (live) | 649ddc2d224b3016675ec9d49f2c30a6ae0bd6441f6b4788093c2096a724352f |
| Standing (live) | 8e7e9ee9a326d49019333bbaf86997703afb0ff63505a438776bcbf3ef5a52b0 |
| TOKEN 90% | 86ad87631cb5bebc073e01e727d01352ba388df79eb20d401a048f122f2a903b |

## ACK
1. Local binds: invented-pending values recorded not-feasible must retry every 24 hours unless Owner sets otherwise; each retry Soft SF'd on disk with date + whether proof became feasible.
2. Local currently has no Local-owned invent marked not-feasible on disk (G-vi-1 Soft SF proof-pursuit Soft SF `dccf3a8c…` still OPEN / where-feasible). When any Local invent is recorded not-feasible, Local schedules Soft SF retries.
3. HARD GATE + where-feasible + TOKEN 90% still LIVE. Kerr BLOCKED. tip untouched.

## Soft SF
PRESS → Auditor Write-only Soft SF CONFIRM.
