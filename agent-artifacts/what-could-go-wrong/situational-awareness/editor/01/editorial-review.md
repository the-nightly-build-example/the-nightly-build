# Editorial review: what-could-go-wrong/situational-awareness (editor/01)

## Skeptic

Thesis, stated from the draft alone: situational awareness — a model knowing
it is a model and telling a test from deployment — has been partially measured
(SAD, Berglund's out-of-context reasoning, Needham's eval-detection), while its
feared use, a model on its own in a real deployment turning that awareness
against a real safety eval, appears nowhere in the primary record, because every
strongest "use" case had its goal or setup handed to it by researchers. The
piece stands on four claims: (1) the SAD and Needham numbers are real but modest
and rising; (2) Apollo, alignment faking, and Berglund's reward hack are the
strongest "use" cases and each was constructed; (3) no unprompted deployment
case exists in the record; (4) a present-day lab (DeepMind) treats the capability
as an eval-invalidating threshold and reports no current model reaching it.

I pushed hardest where the brief pointed: whether any handed-setup demonstration
is allowed to read as a spontaneous one. It is not. Apollo's goal is "written
into the prompt" and the oversight facts "fed in too"; alignment faking gets
"no goal" but the scenario, values conflict, and free/paid training signal are
"built around it"; Berglund's model is "finetuned to know a fact." The hinge
paragraph and pull quote state the absence as a finding without inflating it:
"That absence is not proof the thing cannot happen, and it is not evidence that
it has." The costly overclaim is absent.

The two flagged 2026 claims are absent. Grepped the article for o3, chemistry,
deletion, AISI, 80, and Opus 4.6: no matches. The IAPS secondary (s8) is used
only for the ability-vs-use quote and the three governance asks, not to smuggle
either unverified claim.

Citations. Opened all eight hrefs as printed; every one returns 200 and lands
on the named source. The six arXiv pages carry titles matching the source text
verbatim, including s7 (2505.01420, "Evaluating Frontier Models for Stealth and
Situational Awareness"). The Cold Takes and IAPS pages resolve. Both Background
cross-links resolve in the published library and their display text matches the
target lessons' titles exactly ("No AI has been caught sandbagging a safety test
on its own"; "Models fake alignment when handed a goal, not yet on their own").

data-nb-kind. Seven primary, one secondary, matching the evidence record
assignment source by source. The two lab reports (Apollo s5, DeepMind s7) are
primary for what their own evals found and are framed in prose as interested
parties, not authorities — DeepMind explicitly as "a developer reporting on its
own models, with an interest in clearing them to ship." No independent source is
hidden behind a mislabel.

Figures. Verified every SAD number against Laine et al. Table 1: Claude 3 Opus
is the top scorer on both SAD overall (49.5) and STAGES (50.7); chance 27.4 /
37.5; the ceiling row reads 90.7 / 70.3. Berglund 42% (davinci 175B), 6% vs 2%
floor, 88% reward-hack exploitation; Needham AUC 0.83 vs human 0.92 and agentic
0.95 vs 1.00; alignment-faking 14% vs ~0%; Apollo o1 quote; DeepMind eleven evals
and the "none... show concerning levels" quote — all check against the evidence
and, where I reopened it, the primary.

One break, and it is in the table's display text. The SAD table heads its ceiling
column "Human" and the caption calls 90.7% "a human ceiling" that "matches an
informed person." The SAD paper (§3.1, Table 1) calls 90.7% the "Upper Baseline,"
a composite: a human roleplay baseline on only four task categories (STAGES among
them, 70.3), and an assumed oracle score of 100% on the tasks no human can do
(token-counting in INTROSPECT, ANTI-IMITATION). So 90.7% is not a human score;
an informed person does not reach it on all of SAD, and on several component
tasks no human baseline exists. The figure is correct; the label on it is false,
and a wrong label in display text is the most visible error the paper can print.
Tellingly, the body prose already gets this right, calling 49.5% "far below the
reachable ceiling" — "reachable ceiling" is the accurate reading of the upper
baseline. The STAGES row's 70.3 genuinely is the human roleplay baseline and can
keep a human label. Fixing the column header is markup, so this routes to the
writer.

## Cut

The draft is clean and sits close to its voice. Three sentences failed the tests
and were cut:

- "A newer benchmark sharpens the picture and adds a caveat." A signpost
  describing where the paragraph is about to go; the caveat it foreshadows is
  stated plainly at the paragraph's end, so nothing is lost. The "2025" in the
  next sentence already marks Needham as newer than SAD.
- "Here is the distinction the debate keeps blurring." An announcement pointing
  at the thesis sentence that follows (and that the pull quote already carries).
  It could open any article about any debate; it fails the slop test. Cut so the
  thesis lands without being introduced.
- "The argument is not a museum piece." Portable relevance-puffery in a
  negative-parallelism frame; it announces that the argument still matters, which
  the next clause proves concretely. Cut, and "It shapes how frontier labs..."
  repointed to "The argument shapes..." so the paragraph opens on the fact.

Slop count: three cut. A handful of borderline lines were left standing on
purpose, because each is tied to this subject and does the plain-commitment work
the voice guide asks for: "The skill is there, and it is weak," "So the
capability is real, bounded, and climbing," "The record thins," "Two things are
true at once." Removing them to play safe would flatten the register the guide
directs, which is its own failure.

Earned-contrast budget: the one "not X, it is Y" that remains ("The worry is not
that the model turns evil. It is that...") corrects the real sci-fi misreading of
AI risk and names it, so it stays. No second negative-parallelism reflex survives.

Borrowed phrasing: compared the draft against the Piper, Alexander, and Grace
quotations in the voice guide. The piece borrows the *move* — commit to the
signal, decline to name its cause (Alexander); separate "I haven't seen it" from
"it hasn't happened" (Grace) — but no distinctive clause is lifted. That is the
intended inheritance, not an echo.

Prompt leakage: the article states the measured-vs-used line in its own
compression ("measured, or used?") rather than the brief's wording, and it
implements "name no company as an authority" by framing DeepMind and Apollo as
interested parties rather than by restating the rule. One soft echo of the series
prompt — "Confidence outruns the proof in both directions" against the prompt's
"When the confidence outruns the proof, name the gap" — reads as the article's
own analytical claim, supported by the two readings that follow, not as a lifted
directive. Left standing.

Recent-pattern checks all pass. The takeaway lands the balance on "measured, or
used?... That is the one the whole worry rides on," with no trace of the flagged
"Neither easy story survives the evidence" or the second-person "Now you know
which one you are looking at." The Why card closes on this argument's own
question, off the flagged "By the end you can state the argument at full
strength" mold. No "In plain language" note label. Headings carry no comma-and
join; two open with "How," which is within range rather than a formula.

Two soft characterizations are worth the writer's eye but did not warrant a cut:
"barely above chance" for STAGES 50.7 (which sits ~40% of the way from the 37.5
floor to the 70.3 human ceiling, so "barely" leans generous toward dismissal),
and "about halfway to a human." Both are defensible approximations and I left
the writer's numbers as written.

Grammar and syntax across body, display text, and furniture: clean, no breaks.

## Reader

Read straight through as the paper's declared reader — smart, widely read, no
time in a codebase — what I have that the sources alone would not give me is a
single line drawn through the whole primary record: the capability is measured,
its feared use is not, and every case that looks like use was set up by a
researcher. No one of the eight sources draws that line; the piece earns it by
reading all of them together, and hands the reader a test to carry ("measured, or
used?"). That matches the original-work sentence in the draft handoff, and the
article states it in the body rather than gesturing at it. The prose sits closer
to the voice-guide exemplars than to a median summary: the epistemic-care
sentences ("not proof... not evidence," "answer the first, weakly, and yes") are
Grace-and-Alexander plain, not generic hedging. The headline, reread as the
largest claim — "Frontier models can spot an evaluation when they are asked to" —
commits to exactly what the piece defends, qualifier and all.

No source asset is needed. The one comparison the argument spends is the SAD
scores against their floor and ceiling, and the table carries it; a figure would
decorate. The writer's judgment holds — once the table's ceiling label is fixed.

## Edits

- Cut "A newer benchmark sharpens the picture and adds a caveat." (Needham paragraph).
- Cut "Here is the distinction the debate keeps blurring." (handed-setup section).
- Cut "The argument is not a museum piece." and repointed "It shapes" to "The argument shapes" (present section).
- Ran `nb stamp`: words 2199 to 2175, reading_minutes 10 to 9, sources 8.

## Required work

- **writer** — Relabel the SAD table's ceiling column and caption so the overall
  90.7% is not presented as human performance. It is SAD's "upper baseline," a
  composite that assumes an oracle 100% on tasks no human can do and uses human
  roleplay on only four categories; an informed person does not score 90.7% on
  all of SAD. The STAGES row's ~70% is genuinely the human roleplay baseline and
  may keep a human label. The body's own "the reachable ceiling" is the correct
  framing to bring into the table. Markup, so the writer owns it.

## Decision

revise — every claim, citation, figure, and label holds except one: the SAD
table presents the 90.7% upper baseline as a human ceiling, a false label on
display text that the writer must correct.
