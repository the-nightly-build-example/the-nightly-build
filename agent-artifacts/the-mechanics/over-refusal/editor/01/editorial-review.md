# Editorial review: the-mechanics/over-refusal (round 01)

Skeptic: thesis "a refusal a reader reads as a judgment is a trained response
to surface features, not a conclusion; for open-weight models that
harmful-refusal reflex reduces to one internal direction researchers can
subtract or add, but whether the over-refusal case rides that same direction
is unresolved"; tested 4 claims (fine-tuning installs refusal and it
generalizes by surface features; InstructGPT vs Constitutional AI precision;
single direction in open-weight models; over-refusal as open question) plus
every number in the two tables and the vendor-concession claim; broke: the
piece's own recurring "threshold"/"switch" metaphor, introduced specifically
for Arditi's confirmed internal single-direction mechanism, was being reused
in two later passages to describe the Minecraft/yoga over-refusal cases as if
that same confirmed mechanism explained them — quietly re-settling the exact
question idea 4 says is open. Fixed by cut, not returned to the writer (see
below). No numeric, attribution, or sourcing error found: InstructGPT/
Constitutional AI are kept precisely separated (InstructGPT predicted the
risk in 2022, was not itself refusal-trained; Constitutional AI reports the
over-generalization happening, in an earlier assistant); XSTest 250/200,
Minecraft 96%+4% vs 0%+4%, OR-Bench Hard-1K figures (Claude-2.1 99.8, GPT-4o
6.7, Llama-3.1-70B 3.0, plus Llama-2-70b and Qwen-1.5-72B), and Hasan &
Biswas's r = −0.032 all check against the evidence record exactly; no vendor
quote was invented (the OpenAI safe-completions "brittle" / "when to refuse
rather than what constitutes unsafe output" line is verbatim); `data-nb-kind`
is correct throughout (Hasan & Biswas secondary, the other 8 primary); the
single-direction result is explicitly scoped to "openly released models" /
"closed, proprietary models might not work the same way" in the prose itself,
not only in a locator.

Cut: 5 sentences/clauses cut or trimmed; worst tell: a self-describing
signpost sentence ("This lesson works backward from that mismatch, marking
each step settled or still open, even for the people who build these
systems") that both graded the piece's own method and lifted its closing
clause almost verbatim from the series' own standing direction
(`press/series/the-mechanics/prompt.md`: "Mark which steps are settled
engineering and which are open questions even for the people who build these
systems") — prompt leakage, not reporting.

Reader: this gives me the one visible, checkable thing none of the nine
sources states on its own — a marked causal chain from "a safe prompt got
refused" down through trained-not-native, surface-feature generalization, a
named internal direction confirmed for genuine harmful refusal in open-weight
models, to the explicit, undecided question of whether over-refusal rides
that same direction. That chain, and its settled/open boundary, is the
draft-handoff's claimed original work, and it survives in the article's own
closing paragraph of the "same switch, misfiring?" section. Voice reads close
to the exemplars (Karpathy's evidence-before-claim order, Nanda's
definition-then-honest-limit rhythm) rather than a median AI summary: each
step is checkable, agency verbs are absent, and the open/settled boundary is
stated once, plainly, not hedged three different ways. Headline retested as
the largest claim: "A safe prompt gets refused because a trained switch fires
on a word" is true on the settled reading (idea 1's surface-feature trigger)
and, after the cuts below, no longer overreaches into the still-open claim
that the internal single-direction mechanism itself explains the over-refusal
case.

## Direct edits made

1. Cut the self-describing, prompt-leaking sentence closing the orientation
   section ("This lesson works backward from that mismatch, marking each
   step settled or still open, even for the people who build these
   systems.") — signpost plus a near-verbatim lift from the series direction.
2. Cut "A refusal is not a conclusion the model reaches." (kept the factual
   remainder as "A refusal is an output shape that scored well in training,
   nothing more.") — this was a second instance of the piece's one permitted
   agency-correcting "not X, it is Y" contrast, which the brief and
   draft-handoff both reserve for the takeaway alone.
3. Cut "not intent, but" from "not intent, but vocabulary" — a redundant
   hedged-contrast mold restating the same already-established point.
4. Cut ", not a conclusion drawn about the request" from the single-direction
   paragraph — a third instance of the same reserved agency correction,
   again outside the takeaway.
5. Cut "; over-refusal and jailbreaking are the same threshold, failing in
   opposite directions" — this explicitly equated the over-refusal mechanism
   with the confirmed single-direction mechanism, which section
   "Is over-refusal the same switch, misfiring?" had just said is unresolved.
6. Changed "crossed a threshold" to "matched a pattern" in the takeaway's
   final sentence — "threshold" is the piece's own word for Arditi's
   specific internal direction; reusing it for the Minecraft case, one
   sentence after flagging that exact link as open, risked quietly resolving
   idea 4. "Matched a pattern" keeps the sentence true on the settled
   reading (idea 1) without invoking the unsettled one.
7. Updated `nb-meta.words` from 2198 to 2147 to keep the declared count
   honest after the net loss of 51 words from cuts 1–5 (cut 6 is a like-for-
   like word swap). `reading_minutes` (9) is unchanged; the new count still
   rounds to the same minute at the article's own established words-per-
   minute rate.

Verified after edits: "machinery" 0 uses; "load-bearing" 0; em-dash 0;
"leverage" 0; revolutionary/transformative/game-changing 0; agency verbs
(decides/judges/understands/wants/believes) never predicated of the model —
the two remaining hits on "decide" and "judgment" are both negations/
comparisons stating what the model does *not* do, and now occur in exactly
one place each, the takeaway and the vendor-framing paragraph, matching the
brief's ≤1 scoped correction. HTML tag balance checked programmatically after
all edits; no mismatches.

## Furniture

Both `nb-table` components checked against the evidence record figure by
figure: the XSTest table (250 safe / Minecraft subtype / 200 unsafe,
Llama-2-70B-chat vs GPT-4) and the OR-Bench Hard-1K table (five vendors,
99.8% down to 3.0%) match Table 2/Table 1 of their sources exactly, sentence-
case captions and headers, each figure cited in the adjoining prose. Clear
purpose, no formula problem, no changes needed.

## Required work by owner

None. No claim, source, or asset problem needed the researcher; no missing
prose, structure, or proof issue needed the writer. All fixes above were
cuts or word/clause-level substitutions made directly in the article.

## Decision

No redraft required.
