# Editorial review: the-instruments/rouge (editor/01)

## Skeptic

Thesis: a ROUGE score is recall-oriented string overlap between a machine
candidate and a human reference; it is strong evidence in the narrow home
setting it was built for (short, extractive, single-document news with strong
references, at the system level) and blind to whether an abstractive summary is
faithful. The piece stands on five claims, each tested against the primary it
cites.

1. ROUGE is n-gram/LCS overlap that never reads meaning. Held. Lin (s1) owns the
   definitions; the "In plain language" note and orientation state recall
   orientation correctly (it credits the candidate for recovering the
   reference's units and ignores what the candidate adds).

2. The hand-worked example. Recomputed independently. Reference "the cat sat on
   the mat" (6 unigrams, "the" twice), candidate "the cat sat on a mat".
   ROUGE-1: five reference unigrams recovered, clipped, = 5/6 = 0.83. ROUGE-2:
   reference bigrams the cat / cat sat / sat on / on the / the mat; candidate
   breaks the last two; 3/5 = 0.60. ROUGE-L: LCS "the cat sat on mat" = 5, so
   5/6 = 0.83. The table (5/6, 3/5, 5/6) is correct. The single substitution
   dropping ROUGE-2 to 0.60 is stated correctly.

3. Meaning-blindness via Lin's own reversed-sentence case. Recomputed. Reference
   "police killed the gunman". Both "police kill the gunman" and "the gunman
   kill police" share exactly one reference bigram, "the gunman", so both get
   ROUGE-2 = 1/3. Correct. The ROUGE-L split 0.75 (LCS 3 of 4) vs 0.50 (LCS 2 of
   4) is correct in both the recall-only and beta=1 readings, since the
   reference length is 4 either way. The headline names ROUGE-2 specifically,
   which keeps it accurate rather than indicting ROUGE in general.

4. The dimension picture is kept distinct, which was this round's main risk. The
   article does not claim general weak correlation. Prose and the SummEval table
   (s6) report ROUGE weakest on coherence and relevance, higher on consistency,
   ROUGE-L weak across all four. Every table cell matches the record's Table 2
   figures. The consistency caveat is carried with SummEval's own words ("low
   abstractiveness of most neural models"), so the confound is stated, not
   hidden.

5. Faithfulness stated as "does not track," not "rewards the unfaithful." Held,
   and the BERTS2S guard survives intact: the paragraph explicitly says the
   best-ROUGE model was also the most faithful and that overlap and faithfulness
   moved together there. Maynez's very-weak Spearman band (0.10-0.20 for
   ROUGE-1/2/L, entailment 0.43) matches the record. Graham (s3) is used only
   for variant fragility (0.79 down to 0.29 across 192 variants; best ROUGE
   matching, not beating, BLEU), never as a weak-correlation citation. Bhandari
   is not cited at all, so it cannot be miscited. Sai 2022 (s4) is the secondary
   and is used only for outside characterization (taxonomy placement and the
   meaning-blindness of LCS matching), carrying no standalone correlation
   number.

Breaks found and their disposition:

- BART model card, "exactly three numbers... nothing else." I opened the card
  (s2) as printed. It reports ROUGE-1 42.949, ROUGE-2 20.815, ROUGE-L 30.619 as
  the article states, but also ROUGE-LSUM 40.038, a loss, and a generation
  length. So "exactly three numbers" and "nothing else" are contradicted by the
  primary. Fixed in place: the Why card now says the card "reports its quality
  only in ROUGE scores"; the orientation keeps the three accurate values and
  says "No human rating and no faithfulness check sit beside them." The
  argument's real point (the only quality evidence is overlap; no human or
  faithfulness check) is preserved and is now accurate.

- References direction, in the home-setting warning. The draft said the
  references "push toward the surface" and that a faithful reworder "would be
  scored against a reference that did not," which reverses the cited finding.
  The record's Copeck figure (via s5) is that no more than 55% of a reference
  ("model") summary's vocabulary appears in the source, i.e. references
  generalize away from the source, and that is precisely what penalizes a
  faithful rewording. The draft also used the source's term "model summary,"
  which this lesson's reader would read as the machine summary. Fixed to match
  the record's direction and to use the article's own term "reference."

- "One of the most downloaded summarizers on Hugging Face." Unsupported by the
  record (no download ranking); cut as a nonessential superlative and replaced
  with the record-supported "a widely used summarizer."

- "100 CNN/DailyMail summaries" (SummEval prose and table caption). Imprecise:
  the study rated the summaries of 100 articles across 16 models. Corrected to
  "summaries of 100 CNN/DailyMail articles" in both places.

- "A companion paper" for Kryscinski (s8). Kryscinski is an independent
  Salesforce paper, not a companion to the Google/Maynez study the sentence
  before it. Fixed to "A separate 2020 paper."

Citations: I opened all eight hrefs as printed. All resolve to the correct
source (Lin, BART card, Graham, Sai survey, Kryscinski, SummEval, Maynez all
confirmed by title and author; the NIST s5 endpoint serves the actual paper PDF
from the authoring body). The 30%-inconsistent figure is attributed to the
Kryscinski paper that retells it, which the record permits. data-nb-kind labels
are sound: the BART card is a primary self-report artifact for the claim it
carries, and Sai is the lone secondary.

## Cut

Slop pass, every sentence including display text, tables, and bookends. Three
sentences failed and were removed or reduced:

- "That is a real setting, and it is a narrow one." The section closer reduces
  to the exact "X is real, and it is Y" mold, and adds no fact the enumerated
  conditions before it had not. Deleted; the section now closes on the concrete
  list of conditions.

- "The problem is not that ROUGE points the wrong way. It is that it does not
  point at faithfulness at all." A restatement of the "does not track... not
  that it rewards the unfaithful" sentence three lines earlier, and a third
  consecutive negative-parallelism construction in one paragraph. Deleted; the
  single earned correction (which the round required) stays.

- "the reason it became the standard is worth stating plainly." A meta-signpost
  about the article's own move. Trimmed to a plain concession that leads
  straight into the 0.99 figure.

The one negative-parallelism construction kept ("does not track faithfulness,
not that it rewards the unfaithful") corrects a real, named misconception and is
exactly the guard this round demanded, so it is earned. "Meaning-blindness is
not a bug a better ROUGE variant would fix. It is what a string-overlap count
is." also earns its contrast against the ROUGE-L partial-recovery point just
made.

Edges, deks, and headings checked against the recent-pattern notes. The opener
does not use the "By the end you will know X" or "every flagship ships an X
score" molds. The takeaway lands on a plain statement of what a ROUGE number is
and the open question it leaves, not on the banned negative-parallelism close.
The dek is a single stance, no semicolon reversal, suspended question, or comma
triad. Headings reconstruct the argument in the piece's own nouns with varied
construction, no comma-and triad. No prompt leakage: the "not worthless / read
it for what it is" center is a conclusion the body earns, not lifted planning
language, and no distinctive phrasing was borrowed from the voice-guide
exemplars (the exemplars shaped the count-in-front-of-the-reader method, not
wording). Punctuation clean: no em-dashes, no semicolons, colons used for
payoffs only. Furniture (two nb-tables, the nb-note, the two bookends) is all
documented and each block does real work; no missing component would make the
argument clearer than the hand-worked tables already do, so no asset was
requested.

## Reader

Read straight through as the paper's declared reader, ROUGE met for the first
time, the piece gives what the scattered papers do not: one six-word example
counted by hand to three different scores, and a single rule that reconciles
SummEval's consistency correlation with Maynez's near-zero faithfulness
correlation (overlap tracks faithfulness only where the summary copies its
source). The original-work sentence claims exactly that pairing, and it holds
against the article. The prose sits closer to the voice-guide exemplars than to
a median summary: it lays every figure out before drawing the conclusion and
keeps an even hand, naming what ROUGE is good for before where it goes blind.
The headline, reread as the largest claim, is one the overlap-and-meaning
section defends precisely, and it names ROUGE-2 rather than ROUGE in general.

## Edits

- Why card: cut "one of the most downloaded summarizers on Hugging Face" and the
  "states its quality in exactly three numbers, and all three are ROUGE" claim;
  replaced with "a widely used summarizer, reports its quality only in ROUGE
  scores."
- Orientation: removed "as its only measured quality" and "nothing else" from
  the BART sentence, keeping the three ROUGE values; recast to "No human rating
  and no faithfulness check sit beside them" and "those numbers."
- Home setting: rewrote "The references themselves push toward the surface... A
  summary that reworded faithfully would be scored against a reference that did
  not" to the record's actual direction ("generalize away from the source... A
  candidate that rewords the source just as faithfully, but in different words
  than the reference used, is scored down for the mismatch") and changed "model
  summary" to "reference summary."
- Home setting: cut the closer "That is a real setting, and it is a narrow one."
- Home setting: trimmed "the reason it became the standard is worth stating
  plainly" to "it became the field standard for good reason."
- Dimensions: "100 CNN/DailyMail summaries" to "summaries of 100 CNN/DailyMail
  articles" in the prose and in the table caption.
- Faithfulness paragraph: cut "The problem is not that ROUGE points the wrong
  way. It is that it does not point at faithfulness at all."
- Faithfulness paragraph: "A companion paper" to "A separate 2020 paper."

## Required work

- researcher (non-blocking, record accuracy only): the evidence record states
  the BART model card shows "No other metric... appears on the card." The card
  as printed also reports ROUGE-LSUM 40.038, a loss, and a generation length.
  The article no longer relies on the false "nothing else," so this does not
  block publication, but the record should be corrected so later rounds do not
  inherit it.
- orchestrator: re-stamp after these edits. A few sentences were cut, so the
  stored word count (2006) and reading time need refreshing; the count remains
  well within the 1200-2200 band.

## Decision

Approve. The reframe is accurate on every point this round put at risk, the
arithmetic and Lin's reversed-sentence example recompute correctly, all eight
citations resolve, and the remaining accuracy and slop issues were fixable in
place; no publication-blocking work is left for the researcher or writer.
