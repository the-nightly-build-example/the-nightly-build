# Editorial review: what-could-go-wrong/data-poisoning (editor/01)

## Skeptic

Thesis: the data-poisoning fear rests on real, reproducible lab results, but the
two most alarming ones come from separate experiments and do not chain, so the
"any model could already carry a safety-surviving backdoor planted by ~250
documents" claim is not something anyone has shown. The piece stands on four
load-bearing claims, one per demonstration:

1. A clean-testing model can hide a trigger (BadNets 2017).
2. Injecting poison into a real web corpus is cheap (Carlini 2023).
3. ~250 documents plant a backdoor almost regardless of scale (Souly 2025).
4. A hand-installed backdoor survives the full safety stack (Sleeper Agents 2024).

I tried to break the spine claim, that 3 and 4 do not compose, by hunting every
place they could touch. They stay apart. The prose keeps "easy to install"
attributed only to Souly (never run through safety training, decays under
continued clean training, narrow gibberish trigger, <=13B) and "survives safety
training" attributed only to Sleeper Agents (hand-written SFT, researcher-chosen
trigger). The four-row table is built so the two columns that would compose never
align: Souly's row reads "Not tested; decayed under continued clean training"
under *Survived safety training?*, while the only "Yes" row (Sleeper Agents) got
in via "Wrote the triggers in directly," not fractional poisoning. The
synthesis section and the takeaway both say joining them assumes an experiment
no one has run. Discipline holds. The gap is named in both directions: dismissal
answered by real, reproducible persistence; alarm answered by the absence of any
in-the-wild frontier case.

Rates checked against owning primaries and the evidence record: 99.5% clean /
within a fifth of a point and >99% triggered (BadNets); $60/yr, 0.01% of
LAION-400M/COYO-700M, ~40,000-75,000 images, ten datasets, 6.5% of Wikipedia
within ~half an hour, 0.00025% local CLIP (Carlini); ~250 constant, 100
unreliable / 500 consistent, 600M-13B, 0.00016% of tokens, 6.5% Wikipedia restated
as ~0.27% of a large web corpus (Souly, not double-counted); near-99% on the true
trigger after adversarial training, ~55% vulnerable-code rate, persistence rising
with size/CoT (Sleeper Agents). All match. The two figures the brief warned live
only in charts (finer per-variant persistence) are not printed; only the two
text-supported numbers (near-99%, ~55%) appear. Good.

Named people: Gu / Dolan-Gavitt / Garg, Souly and Carlini among authors, and
Mavroudis (principal research scientist, Alan Turing Institute, study co-author)
all match the record. "Evan Hubinger, led" is consistent with the record's
"Hubinger et al." and is correct as first author; not a blocker.

data-nb-kind audit: six primary (s1-s6), two secondary (s7-s8). s4 (Anthropic)
and s5 (OATML) are co-authoring institutions of the Souly paper, so primary is
defensible; heise and Fortune are outside parties, correctly secondary. Every
citation sup resolves to its #sN anchor; every source-list href is the real
source page (arXiv /abs/, Anthropic, OATML, heise, Fortune) and all resolve.
nb-meta title/dek match the rendered title and dekline.

Two breaks found, both routed to the writer because they are source text /
quotation fidelity:

- s5 (OATML) prints the descriptive title "A near-constant number of documents
  can poison a model." The real on-page H1 is "Poisoning Attacks on LLMs Require
  a Near-constant Number of Poison Samples" (verified by fetching the page). This
  is the same string as the arXiv paper title at s3, because the blog post reuses
  the paper title; the correct fix is the verbatim title, disambiguated in the
  source line if the writer wishes.
- s8 (Fortune) prints "Anthropic study on how little bad data it takes to poison
  AI models." The real headline is "A small amount of bad data can 'poison' even
  the largest AI models, researchers warn" (verified). Descriptive, not verbatim.
- The Mavroudis quotation is altered inside quote marks. The article prints a
  model that "when it detects a specific sequence of words, foregoes its safety
  training." Fortune's verbatim is "when, for example, it detects a specific
  sequence of words, it foregoes its safety training." A dropped "it" and a
  silently removed "for example," put words slightly off from what a named,
  on-record person said. Route the exact text so the writer can render it
  verbatim (with a marked elision) inside the word budget.

s4 (Anthropic) title verified correct; heise (s7) matches its slug; not flagged.

## Cut

The earns-its-place pass found the prose lean. One direct cut: the trailing
colon-clause "the more capable the model, the better it kept its secret" was a
voiced restatement of the sentence it hung off ("Persistence grew with model
size and with chain-of-thought training") with no new fact, and its "kept its
secret" framing warmed a passage the voice guide wants held flat. Cut it; the
sentence now ends on the fact.

The recurring demonstrated-vs-analogy contrast is licensed to exceed the usual
one-or-two ceiling here, and each crossing pays its way with a new fact
(concept-not-economics; injection-but-no-LM-plus-fixes; constant-count-but-not-
safety-tested-and-decays; survives-but-hand-installed; then the both-directions
gap). Not a seesaw. The two "neither X nor Y" contrasts (bluster/settled fact;
dismissal/alarm) are both real and specified. No prompt leakage: the opener's
preview is this-lesson-specific and licensed by the template, not copied
instruction. Headings are this argument's own steps and avoid the recent
"Where the evidence stops and X takes over" mold; no nb-position or stat strip.
Grammar and punctuation are clean, zero em-dashes.

The worst structural tell is furniture, not prose: the body closes on an
`nb-note-strong` labeled "Verdict" that restates the finding. The press
direction is explicit that a lesson lands its judgment in the takeaway and must
not close the body with a Verdict note or any block that restates the finding,
naming it a retired-template leftover. This one duplicates the takeaway's
judgment. Removing it is markup, so it routes to the writer.

## Reader

Read straight through as the smart, time-poor reader this paper serves, the
piece gives something the four sources alone do not: an assembled, side-by-side
account of why the two scariest results cannot be stacked, made legible in a
table whose columns are arranged so the non-composition is visible rather than
asserted, plus the honest both-directions gap. That is the original-work claim
in the handoff, and it holds. The prose sits closer to the Carlini/Schneier
exemplars, evidentiary discipline at one flat temperature, than to a median
summary; it steelmans the fear at full strength and weighs it with the same
hand. The headline, read as the largest claim, is exactly what the body proves.

## Edits

- Cut ": the more capable the model, the better it kept its secret" from the
  Sleeper Agents persistence sentence (voiced restatement, no new cargo).
- Ran `./nb stamp`: words 2198 -> 2187, sources 8, reading 10 min.

## Required work

- writer: Remove the "Verdict" `nb-note-strong` block that closes the
  why-they-dont-combine section. The press direction forbids closing the body
  with a Verdict note or any block that restates the finding; the takeaway
  already lands this judgment. (Removal frees words.)
- writer: Correct the s5 source title to the verbatim OATML H1, "Poisoning
  Attacks on LLMs Require a Near-constant Number of Poison Samples"; disambiguate
  from s3 in the source line if wanted (it is the blog announcement of the same
  paper).
- writer: Correct the s8 source title to the verbatim Fortune headline, "A small
  amount of bad data can 'poison' even the largest AI models, researchers warn."
- writer: Render the Mavroudis quotation verbatim. Fortune's text is: "when, for
  example, it detects a specific sequence of words, it foregoes its safety
  training." Restore the second "it" and mark the "for example," elision (e.g.
  "when ... it detects a specific sequence of words, it foregoes its safety
  training"); do not print altered words inside quote marks.

No researcher work needed; the claim set is complete and correctly used. No
orchestrator work needed.

## Decision

revise: the spine, rates, and sourcing labels are sound, but the body closes on
a press-forbidden Verdict note and two source titles plus a named person's quote
are printed non-verbatim, all writer-owned.
