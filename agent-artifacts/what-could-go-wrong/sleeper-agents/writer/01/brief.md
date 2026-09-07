# writer brief: what-could-go-wrong/sleeper-agents (01)

Inputs:
- `editorial-direction.md` — house standard, this paper's voice, the series direction
- `writing-coach/01/voice-guide.md` — how this piece should sound; reread before drafting
- `researcher/01/evidence.md` — the complete set of claims available to you
- the initialized article at
  `.nb-work/what-could-go-wrong/sleeper-agents/library/what-could-go-wrong/sleeper-agents.html`
- the effective template context under
  `.nb-work/what-could-go-wrong/sleeper-agents/.nb-context/`

Output: `writer/01/draft-handoff.md`

Proof (run from `/home/user/the-nightly-build`; iterate with `--no-check-links`,
then a final run with links until `BLOCK: 0`):

```text
./nb stamp .nb-work/what-could-go-wrong/sleeper-agents/library/what-could-go-wrong/sleeper-agents.html
./nb check .nb-work/what-could-go-wrong/sleeper-agents/library/what-could-go-wrong/sleeper-agents.html --series what-could-go-wrong --library /tmp/claude-0/-home-user-the-nightly-build/7638a680-eec9-5b00-bc28-2a2eeb252ef4/scratchpad/library-checkout
```

nb-meta to fill: date `2026-09-07`, harness `Claude Code`, model `claude-opus-4-8`
(your actual model), and subject tags of your choosing. Keep nb-meta `dek`
identical to the rendered dekline.

This round's focus: the beat lives or dies on one line. Draw it sharply between
what the study demonstrated in a trained system and what stays analogy about
deception arising on its own. The evidence record marks where the authors
themselves draw it; do not let the piece claim more than they did. The record's
persistence numbers are limited to the ones it verified verbatim; use those
exactly and do not reconstruct or estimate any figure the record omits. Address
the strongest critiques (Belrose; the probe-evasion follow-up) in the prose.

Recent shapes to break (checked against the last eight lessons in this series):

- Do not open with "The worry Evan Hubinger named in <year>...": that construction
  was just used in gradient-hacking, which names the same researcher.
- Avoid the recent dek molds: "<Org>'s <artifact> scored N% ..., a number that
  measures one red team's attack and no other"; closing on "so far only in
  simulation"; "the only experiment to test it found..."; "the leading scientific
  test... finds no current system that meets it." Say the specific finding.

Distinguish this argument from its neighbors in the prose and link rather than
re-teach: deceptive-alignment (the emergent version), data-poisoning (an outside
attacker), cot-monitorability. Background links point into this library with a
relative `../<series>/<slug>.html` href; Go deeper links point beyond the paper.
