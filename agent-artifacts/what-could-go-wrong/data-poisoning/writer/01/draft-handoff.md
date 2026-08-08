# Draft handoff: what-could-go-wrong/data-poisoning (writer 01)

## Original work
This piece turns the evidence record's scattered "these do not compose" caveat
into the article's organizing spine, and makes it visible in a four-row table
whose "how the trigger got in" and "survived safety training?" columns never
line up in a single row — showing structurally that no one experiment chains
cheap installation to safety-survival, which no source states as a single claim.

## Proof
Full `nb check` with links (series what-could-go-wrong, library
/home/user/library-checkout): `BLOCK: 0`, `WARN: 0`, verdict PUBLISHABLE.
Stamped: words 2198 (band 1200-2200), sources 8 (6 primary, 2 secondary),
reading 10 min. Zero em-dashes; banned-term and density warnings all resolved
by splitting and trimming, not by substitution. No warning left standing.

## Discipline held (editor's first check)
The two headline results are kept in separate frames throughout and never
composed. "Easy to install" is attributed only to Souly et al. (~250 documents,
never run through safety training, decays under continued clean training,
narrow gibberish trigger at <=13B). "Survives safety training" is attributed
only to Sleeper Agents (installed by hand-written SFT with a researcher-chosen
trigger, not fractional poisoning). The synthesis section and the Verdict note
state plainly that joining them assumes an experiment no one has run. BadNets
is framed as concept-only (attacker owns the whole training run), not as
evidence for cheap fractional poisoning. Carlini's 6.5% of Wikipedia is
reconciled with Souly's ~0.27% of DOLMA as one finding in two denominators, not
double-counted. Per-variant Sleeper Agents figures are limited to the two the
evidence carries as text (near-99% post-adversarial-training on the true
trigger; ~55% vulnerable-code rate); no figure-only percentage is printed. The
gap is named in both directions, and the absence of any in-the-wild case is
stated.

## Editorial decisions worth a look
- No figure was rendered. The evidence's "Source assets" section offers a chart
  (Souly's near-constant curve) and photographs, but the record supplies no
  plottable verified numeric series (the per-model-size perplexity curves are
  described, not tabulated), and honest source-asset capture was not available
  in this run. The comparison table carries the visual load and needs no
  external capture. If the editor wants a figure, it requires a new researcher
  series or a captured asset.
- Two source titles are descriptive, not verbatim published headlines: the
  Oxford OATML blog (s5) and the Fortune report (s8). Their exact on-page
  titles were not in the evidence record; the URLs resolve and the publishers
  and dates are correct. Flag if verbatim titles are wanted.

## Open questions
None blocking. The claim set was treated as complete; no researcher request is
needed for this round.
