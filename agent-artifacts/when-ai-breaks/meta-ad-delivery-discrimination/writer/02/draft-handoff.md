# writer draft-handoff: when-ai-breaks/meta-ad-delivery-discrimination (writer/02, revision)

## Original work

The article takes four independently primary-sourced findings that no single
source states together — the 2019 controlled delivery study, HUD's charge,
the two settlements three years apart, and the 2025 independent audit of
Meta's fix — and assembles them into one causal chain a reader can follow
from mechanism to harm to response to (partial) verification, letting a
reader name the mechanism and recognize it outside this one company's ad
platform.

## Proof result

`./nb check .nb-work/when-ai-breaks/meta-ad-delivery-discrimination/library/when-ai-breaks/meta-ad-delivery-discrimination.html --series when-ai-breaks --library /tmp/claude-0/-home-user-the-nightly-build/d5bad8fd-c10f-5854-a93d-2fb67333d30d/scratchpad/library`

Ran once with `--no-check-links`, then once with links included. Both:

```
BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

`nb stamp` updated counts to words=2184, reading_minutes=9, sources=8 (down
from 2199/10 before the correction, since the fix nets a few words shorter).

No warnings intentionally left.

## Editorial requests resolved

- Re-read Imana, Shen, Heidemann, and Korolova (FAccT '25) directly —
  §4.1.1, §4.2.1, and Figure 3 — via the arXiv PDF (arxiv.org/abs/2506.16560)
  rather than relying on the evidence record's paraphrase, and confirmed the
  editor's read against the paper's own text: "In the left figure for
  gender, variance is less than 5% even without VRS in 15 out of 18
  cases... In the right figure for race, we see variance is more than 10%
  without VRS in all 18 cases. VRS reduces variance to less than 10% in all
  cases, bringing it down to less than 5% in 15 of the 18 cases." Fixed the
  stat strip to state the race result at Meta's 10% compliance threshold
  correctly (0/18 passing without VRS -> 18/18 with VRS) instead of the
  wrong, category-conflated "&lt;5/18 -> 15/18." Confirmed via §4.1.1 that
  all 36 paired experiments are declared as housing (the only category VRS
  is legally required to cover); fixed the "36 paired campaigns" sentence to
  drop the inaccurate "housing, employment, or credit ad" and say "a housing
  ad," leaving the following paragraph's already-correct treatment of the
  separate, voluntary employment/credit test untouched.
- Checked the takeaway bookend's summary of the audit against the
  correction: it states no specific pass-rate numbers, only that the fix
  worked for housing and not yet for employment/credit, which still holds
  under the corrected figures. No change needed there.
- Preserved every other settled item from editor/01 (headline, dek, the
  "identically targeted" framing throughout, the HUD-independence fix, the
  heading retitle, all five cuts, and the byline/author-count fix) exactly
  as the editor left them; touched only the two required sentences and the
  three stat-strip values.

## Open questions

None.
