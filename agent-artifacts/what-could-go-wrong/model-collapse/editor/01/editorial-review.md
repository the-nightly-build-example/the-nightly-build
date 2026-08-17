# Editorial review: what-could-go-wrong/model-collapse (editor/01)

## Skeptic

Thesis: recursive training that *replaces* real data with a prior model's
synthetic output collapses generative models, demonstrated in controlled
experiments; a follow-up paper shows *accumulating* data instead avoids
collapse in everything it tested, but that fix carries a named exception and
an unresolved theoretical tension, so how far it travels to real training
pipelines is not settled.

Claims tested:

1. **Replacement collapses models, tails first.** Held. Checked the Nature
   paper's Definition 2.1 and the OPT-125m/wikitext2 experiment against the
   evidence record's quotes and figures. The article's 34-baseline and
   +20–28-point figures match the source exactly, and "roughly 60 to 80
   percent worse" is defensible arithmetic on those two sourced numbers
   (20/34 = 59%, 28/34 = 82%).
2. **Accumulation avoids collapse across model classes.** Held, and verified
   beyond the evidence record: I pulled the actual Gerstgrasser et al. PDF
   (arXiv:2404.01413) and confirmed Figures 2, 4, and 5 match the article's
   claim and locators exactly — language models, diffusion, and VAEs all
   held roughly flat under accumulation and degraded under replacement. The
   article's own figure citations (§2.1, Fig. 2, Fig. 4, Fig. 5) are correct
   against the primary source, not just the evidence record's paraphrase.
3. **10% retention is not accumulation.** Held. The article keeps this
   distinction explicit and separately labeled, as the round focus required.
4. **The Martínez exception and Dohmatob tension are real, unresolved, and
   distinct.** Held on inspection, but the dek as drafted broke this claim.
   The original dek's clause "with one exception the paper itself names"
   read ambiguously enough to imply one of Gerstgrasser's *own tested*
   architectures failed to accumulate — it did not; all of Gerstgrasser's
   own experiments held up. The Martínez case is a different paper's
   different architecture, only *cited* by Gerstgrasser as an unresolved
   flag. Rewritten the dek to state only the accumulation finding and moved
   the exception entirely into the body, where it is already handled
   correctly (see Edits).
5. **A found arithmetic break, fixed at the source.** "It matched or beat
   code models built with an order of magnitude more parameters and
   training data" (phi-1 vs. StarCoder-Prompted) understated the gap: 15.5B
   vs. 1.3B parameters is ~12x (an order of magnitude, correct), but 1T vs.
   ~7B training tokens is ~143x — over two orders of magnitude, not one.
   The evidence record's own Numbers section already carries both exact
   figures, so fixed directly rather than routing: named the actual
   comparison model and gave the two ratios separately instead of
   collapsing them into one inaccurate magnitude.

Citations and kinds: spot-checked every href against the evidence record;
all eight match exactly. Confirmed the Oxford press release (s5, secondary)
resolves and the Gal quote is verbatim. The Nature URL (s2) redirects to a
login gate, which is Nature's normal access wall for every reader, not a
miscitation. Kind labels (6 primary / 2 secondary) match the researcher's
own classification and the content descriptions; no relabeling needed.
Named-person check: Yarin Gal is introduced only as "one of the paper's
coauthors," which is true and does not overclaim a title. Directional
claims (fixed-fraction persistence in Dohmatob, shrinking-share exemption
in Gerstgrasser) checked against the evidence record's quotes and hold in
the direction stated.

No broken central claim required routing to the researcher or writer.

## Cut

Full slop pass against `spec/slop.md`, edges read in and out of order,
against the recent-pattern record, and against the briefing files for leakage.

- Cut one self-reference sentence in the body ("Whether that is close
  enough to a fix is the question the rest of this lesson tests.") The
  lesson template is explicit that the body never mentions the lesson;
  bookends are the one place that's allowed. The sentence was pure
  signpost — deleting it loses no fact, and the next section's heading
  already carries the reader forward.
- Cut a self-grading lead-in ("That is worth stating plainly rather than
  resolving:") that graded the article's own interpretive choice rather
  than continuing the analysis. The load-bearing claim behind it (the two
  papers' differing assumptions leave the tension genuinely open) survives
  as a direct sentence.
- Rewrote a sentence that lifted the evidence record's own phrasing
  ("No source read for this record disputes...") into reader-facing prose
  almost verbatim ("No source in this record contests..."). "This record"
  is the researcher's internal artifact, not something a reader has;
  rewrote as a direct declarative claim carrying the same fact without the
  leaked reference.
- Varied one of the two "Keeping..." headings (anaphora flagged in the
  round focus). Kept "Keeping the old data around stops the collapse
  across three tasks" for the primary rebuttal section since it is this
  piece's central, strongest result; retitled the partial-retention
  section "A fixed slice of the old data slows the collapse without
  stopping it," which states the section's actual finding rather than
  echoing the neighbor heading's opener.
- Rewrote the dek per the round focus: cut the "X, and Y, with Z" comma
  triad (~48 words, three clauses) down to one lean sentence (~21 words)
  carrying a single, accurate surprise — the accumulation finding — and
  moved the exceptions into the body, where the unresolved-tension section
  already carries them correctly and in more careful, accurate terms than
  the old dek's compressed clause did.
- Checked "It is not a counter-example to either paper. It is evidence
  that..." against the negative-parallelism ban: kept it. The misconception
  it corrects (does phi-1's success undercut the collapse findings?) is
  real, is the exact tension the commission asks the piece to address, and
  the sentence is followed immediately by specific, earned reasoning
  (curated vs. indiscriminate use), not a vague assertion.
- Em-dash count: 1, inside a direct quote from Gerstgrasser reproducing the
  source's own punctuation — well under the house limit of 4, and not the
  writer's own tic.
- No instances found of vague attribution, decorative analysis, puffery, or
  unearned punchlines. No banned lexical terms (leverage, load-bearing,
  revolutionary, transformative, game-changing, AI race, machinery) present.
- No verdict block; the holds-up grid (the press's mandated substitute) is
  used correctly, and no company is named as an authority anywhere in the
  piece.

Roughly six sentences failed a test outright (the two self-reference/
self-grading sentences, the leaked-phrasing sentence, plus the dek and one
heading counted as display-text failures); the phi-1 magnitude line was a
factual break rather than a slop failure. No repeated pattern beyond the
single heading anaphora and the dek's comma-triad shape, both named in the
round focus and both fixed.

## Reader

Reading it straight through as the declared reader: I leave able to sort
any future model-collapse claim into one of three regimes — replacement,
fixed partial retention, or full accumulation — and to know that only one
of them has been shown to avoid the problem, with a named, unresolved
exception even to that one. That classification is the article's own
synthesis; neither source paper frames the landscape that way, and the
takeaway's closing instruction ("ask which of three regimes it is actually
describing") hands the reader a tool the sources alone do not supply. This
matches the draft handoff's original-work claim, and it holds up under a
reader's eye, not just as a stated intent.

The prose sits closer to the voice-guide exemplars than a median AI
summary: the partial-retention section uses Piper's concession-before-claim
move ("It is tempting to read... It is a different operation") to correct
a real, specific misreading rather than asserting the point flatly, and the
worked example (34 to +20–28 perplexity points, the jackrabbit color-morph
drift) sits directly next to the claim it tests in Luu's style rather than
being narrated after the fact.

Headline as the largest claim: "Generative models fed only their own
output collapse within nine generations" is the strongest demonstrated
fact in the piece, named with its actor and its number, and the piece
defends it in the first section before complicating what it implies. It
does not overreach into the extrapolation the rest of the piece is
careful not to make.

## Edits

- Rewrote the dek in both the rendered `<p class="nb-dekline">` and the
  `nb-meta` JSON `"dek"` field, identically, from a 48-word three-clause
  comma-triad stack to a 21-word single sentence stating only the
  accumulation finding.
- Cut the self-referential closing sentence of the orientation section's
  third paragraph ("Whether that is close enough to a fix is the question
  the rest of this lesson tests.").
- Retitled the partial-retention section's heading from "Keeping 10 percent
  of the original data only slows the climb" to "A fixed slice of the old
  data slows the collapse without stopping it," to break the anaphora with
  the accumulation section's heading.
- Trimmed the self-grading lead-in "That is worth stating plainly rather
  than resolving:" from the unresolved-tension section, leaving the
  underlying claim as a direct sentence.
- Rewrote "It matched or beat code models built with an order of magnitude
  more parameters and training data" to "It matched or beat
  StarCoder-Prompted, a code model built with about twelve times its
  parameters and more than a hundred times its training tokens," correcting
  an understated training-data ratio using figures already in the evidence
  record's Numbers section.
- Rewrote "No source in this record contests that replacing real data..."
  to "Even that reading does not dispute the core demonstration: replacing
  real data...", removing a phrase leaked from the evidence record's own
  internal language.

## Required work

None. No open item requires the researcher or writer.

## Decision

**Approve.** The central claims hold against the primary sources (including
a direct check of the Gerstgrasser PDF's Figures 2, 4, and 5, not just the
evidence record), the three regimes stay distinct, the Martínez and
Dohmatob tensions are named and correctly left unresolved, the Schaeffer
reading is steelmanned, and no company is invoked as an authority. The
round focus's three items — dek length/shape, heading anaphora, and asset
provenance — are resolved, plus one further slop pass and one numeric
correction made directly. Nothing remaining needs reporting.
