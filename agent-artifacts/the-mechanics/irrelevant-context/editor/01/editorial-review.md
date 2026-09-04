# Editorial review: the-mechanics/irrelevant-context (editor/01)

## Skeptic

Thesis, stated from the draft alone: a model's answer to a word problem is
conditioned on the whole surface string, and the model has no reliable step that
separates the tokens the question needs from the ones that are only scenery, so
renaming, renumbering, or adding one true-but-irrelevant sentence can move the
output. That much is settled engineering. What it implies about "reasoning" is
open, and the sharpest claim (that these models do not reason at all) leans on
the one benchmark whose "irrelevant" clauses may not have been irrelevant.

The claims it stands on, and how each held:

- **Adding one irrelevant sentence lowers accuracy (Shi/GSM-IC).** 95.0% base to
  72.4% per-problem, 6.0% under the strict "every variant" measure, no more than
  18% surviving all variant types. All three match the evidence Numbers block and
  the record's quote ("no more than 18% ... for all types of irrelevant
  information"). The href resolves to the Shi et al. paper. Held.
- **Regenerating names/numbers is a spread, not a point, and numbers hurt more
  than names (Mirzadeh/GSM-Symbolic).** Gemma2-9B worst-to-best > 12 points,
  Phi-3.5-mini ~15; original score near the middle of the changed-names spread
  but near the top of the changed-numbers one. Matches the record and the paper's
  abstract. Held. I pushed on the headline against this: the body's own honest
  statement is that names sit near the middle (a symmetric spread), so "rename ...
  and the model does worse" reads as an emblem of the surprising behavior, not a
  claim that renaming reliably lowers the mean. The dek supplies the honest
  magnitude ("a little" for names, "a lot" for the added sentence), so head and
  dek are honest together. Left as written.
- **The mechanism: tokens in, no relevance filter, matching to training patterns
  (Dziri/Faith and Fate).** "Linearized subgraph matching ... without necessarily
  developing systematic problem-solving skills"; accuracy decays as a problem
  needs paths rare in training. Quote and direction match the paper. Held.
- **GSM-NoOp's 65% is the lone contested link.** The "up to 65% across all
  state-of-the-art models" and "no evidence of formal reasoning" both verify
  against the GSM-Symbolic abstract and the record's quotes. The per-model table
  (o1-preview 92.7→77.4, GPT-4o 94.9→63.1, Gemma2-9B 79.1→22.3) matches the
  Numbers block exactly, and the caption cites s3 with the Table 1 locator the
  record supplies. The Sturb re-analysis (117 of 945 clauses unambiguous; filtered
  drop 0–2 points, "statistically indistinguishable from zero"; unfiltered set
  reproduces the ~65% drop) verifies against the post itself. Held, and the
  settled/open line is drawn exactly where the review brief asked: the settled
  mechanism rests on the clean perturbations, the 65% is isolated and attributed,
  and o1-preview's resistance sits in the table, not buried.

Display text, descriptor by descriptor. Headline: a claim the piece defends
(surface change moves the answer), sentence case, present tense, no colon, no
quoted-prompt mold. Dek: adds the magnitude and the open question without
restating the headline; it makes claims about the world, not a grade of the
article's method; it is two clauses joined by "and", not a banned triad. Subheads
are all sentence case, each a step in the piece's own nouns, and reconstruct the
argument in order; none is a scaffolding slot, and the close is "Where this leaves
the reasoning question," not the "what the fixes reach" shape the commission
flagged. Named figures in display text (the table's three models and their two
columns) match the record. No place, date, or affiliation in display text is
wrong.

data-nb-kind audit, against the authorship-and-stake test. s1–s6 are correctly
primary: each authoring party owns the claim it is cited for (OpenAI/GSM8K,
Shi/GSM-IC, Mirzadeh/GSM-Symbolic, Dziri/Faith and Fate, Nezhurina/AIW,
Wu/counterfactual tasks). s7 (AppleInsider) is correctly secondary and is used
only for reception ("coverage carried it as proof"), not for a number. s8 (Sturb)
is the borderline: by the strict test it owns its own rerun, so it is primary for
the 117/945 audit and the 0–2 point figure the article cites it for. Marking it
secondary is the conservative call, matches the evidence record's lead
classification, keeps the contested 65% figure's primary anchor in Mirzadeh (s3),
and does not hide a missing independent source, because the prose openly
attributes the audit to a single "2026 re-analysis." Left as classified.

Every citation href opened as printed. All eight resolve and land on the correct
source (title, authors, and load-bearing claim confirmed on each). No miscitation
found; no citation is cited for something its source does not carry.

One introduced specific broke: the opening described GSM8K problems as "two or
three arithmetic steps." The GSM8K paper states 8.5K problems and does not fix a
step count (its own description is a 2–8 step range), and the evidence record
carries no step count. The specific was unsupported and understated, so I
generalized it rather than assert a number no source owns. Fixed directly.

## Cut

The prose sits at the register the voice guide sets: it opens on the behavior
concretely (95.0% to 72.4% on the strongest Shi setup) before any mechanism,
gives the effect as two sourced numbers with their qualifier rather than one
dramatic figure, and holds both halves of the open question without resolving it,
which is the Willison move the guide names. No borrowed phrasing from the guide's
quoted writers survived into the draft; the distinctive lines ("The wording is
all it has," the closing "Does the claim survive renaming the people?") are the
article's own and depend on its nouns.

One sentence failed the slop test and was cut: "This is the honest edge of what
is known." It reduces to "This is the X edge of what is Y" and grades the passage
rather than doing its work; the sentences after it already mark settled from open
plainly, so nothing real was lost. That cut also removed a second use of "honest"
as a self-approving frame (the other is "The honest answer needs two numbers,"
which I kept: it introduces the genuine micro/macro distinction that follows and
carries a reasoning step).

Edges otherwise hold. Paragraph and section openers and closers each carry a fact
or a reasoning step; the body's last line before the takeaway ("the leap from
there to they cannot reason at all runs ahead of what the clean tests have shown")
is the conclusion the argument built, not a signpost. The negative-parallelism
constructions present ("not the arithmetic itself," "not formatting but content,"
"matching ... rather than running a general procedure") each correct a real,
named misconception (the getting-math-wrong lesson, the prompt-sensitivity lesson,
and the reasoning claim the piece is about), so they are earned, not reflex.
Punctuation is within tolerance: zero em-dashes, three semicolons, each joining a
tight parallel or contrast. No prompt leakage: the reader-situation sentences in
the "Why this matters" bookend are template-allowed reader address, and no
selection rule, planning label, or "assignment fulfilled" claim reached the prose.

Furniture earns its place and is all documented: the two bookends, the stat strip
(three cited headline numbers), the "The added clause" note (the kiwi worked
case), and the three-row GSM-NoOp table (which carries the reasoning-tuned-resists
contradiction the brief wanted shown, not buried). None is a formula, and the
piece reads as a continuous article, not a stack of blocks. I looked for a missed
component and found none needed; no code appears, per the series rule. The
commission's three named formulas are all avoided. The full edge comparison
against the last five Mechanics lessons could not be run here (the published
library is not in this checkout and `nb history` returns none), so that library
comparison remains the orchestrator's; against the specific patterns the
commission and brief named, the piece is clean.

## Reader

Read straight through as the paper's declared reader, new to how these systems
work: I come away able to say why a cosmetic change moves the answer (the model
has only the tokens and matches the whole string to training patterns, with no
relevance filter), able to separate the settled behavior from the contested
"cannot reason" claim, and holding a usable test for the next reasoning claim I
meet ("does it survive renaming the people?"). No single source gives that; it is
the article's sequencing of six primaries into one settled-then-open argument and
its isolation of the lone contested number. The original-work sentence claims
exactly this synthesis, and the article delivers it. The prose sits closer to the
voice-guide exemplars than to a median summary: plain, unhurried, both halves
stated. The headline as the largest claim holds up with the dek beside it.

## Edits

- "two or three arithmetic steps" → "a short chain of arithmetic": removed an
  unsupported and understated step count no source owns (GSM8K fixes no count).
- Cut "This is the honest edge of what is known." from the closing body
  paragraph: a signpost that failed the slop test and graded rather than reasoned;
  the following sentences already mark settled from open.

## Required work

None. Both changes were the editor's to make; no fact was introduced, no number,
name, date, or quotation altered, no citation's purpose changed, and no claim of
the article changed. No researcher or writer work is outstanding.

## Decision

approve — the settled/open line is drawn honestly and every reported figure and
citation verifies; the two remaining issues (an unsupported step count and one
slop signpost) were fixable directly and are fixed.
