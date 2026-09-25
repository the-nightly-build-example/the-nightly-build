# Editorial review: the-evidence/elmo (editor/01)

## Correct

Thesis: ELMo made a word's representation depend on its whole sentence and set a
new state of the art on six tasks at once by being added on top of existing
models; the field kept the idea (contextual representations from a language model
pretrained on unlabeled text) and dropped the method it shipped (a frozen
two-layer biLM whose layer states are weighted and concatenated as features)
inside a year. I could state the thesis and its claims from the draft alone.

Claims under it, and how each held:

1. ELMo's mechanism (biLM, freeze-and-concatenate, higher layer = word sense,
   lower layer = syntax). Reopened the ELMo paper past the evidence quotes. The
   freeze-the-weights-and-concatenate description, the per-task weighted sum of
   layers, and the split of labor between the two biLSTM layers all check against
   §3.3 and the intro. The architecture line (two biLSTM layers, 4,096 units,
   512-dim projections, character input, ten epochs on the one-billion-word
   corpus) matches §3.4, and the piece is honest that no single parameter total
   is stated. Held.

2. The six-task table. Recomputed every row against the paper's Table 1. Metric,
   previous SOTA, baseline, and ELMo-plus-baseline match exactly for SQuAD, SNLI,
   SRL, Coref, NER, SST-5. The "error cut" column is the relative reduction in
   the paper's own baseline error, not the gain over previous SOTA: SQuAD
   4.7/18.9 = 24.9%, SNLI 0.7/12.0 = 5.8%, SRL 3.2/18.6 = 17.2%, Coref 3.2/32.8 =
   9.8%, NER 2.06/9.85 = 21%, SST-5 3.3/48.6 = 6.8%. The caption states this
   basis correctly, the prose is consistent with it ("cut the baseline's
   remaining error"), and keeping the baseline column is what makes the figures
   internally checkable. The SNLI prose ("passed the previous record by a tenth
   of a point," 88.7 vs 88.6) checks. Held.

3. Idea-vs-method split, precise in both directions. This was the priority. The
   piece does not overstate into "ELMo was a dead end": it says the idea is "the
   ground the models after it stand on" and "now everywhere." It does not
   understate the displacement: the method "lasted about a year in frontline use
   before fine-tuning a whole Transformer took its place." Verified against
   BERT's own paper that the distinction is drawn as BERT draws it. BERT's
   feature-based definition naming ELMo, the "shallow concatenation of
   independently trained left-to-right and right-to-left LMs" quote (Introduction,
   quoted in the note with the correct locator), and the "strictly more powerful"
   bidirectional claim all match the source. The piece is careful that BERT's
   complaint is about the delivery, not the idea. Held.

4. Credit correction. CoVe (context vectors from an MT encoder, a year earlier)
   and ULMFiT (LM pretraining plus fine-tuning, submitted weeks before ELMo v1)
   check against their abstracts and the evidence record's dates. The "ImageNet
   moment" is attributed to Ruder (July 2018) and applied to ELMo, ULMFiT, and
   the OpenAI transformer jointly, which is what the source says; the piece
   explicitly corrects the common misattribution to ELMo alone. Held.

Labels: headline, dek, and every subhead check against the sources. SQuAD's
"more than a hundred thousand questions written by crowdworkers about Wikipedia
passages" matches the SQuAD abstract (cited to its owner, not to ELMo).
data-nb-kind audit: ELMo, BERT, SQuAD, CoVe, ULMFiT marked primary; the Ruder
retrospective marked secondary. Correct against the primary/secondary test. Every
href opened and lands on its source; internal Background/Go-deeper links resolve
under the proof. No break required a fix; the draft was already sound on the
numbers.

## Reads well

Two body sentences went because they broke the template's rule that the body
speaks to no one and never mentions the lesson.

- "This is the split the lesson has been tracing" narrated the lesson from inside
  the body. Recast the paragraph's topic sentence to state the split in the
  article's own nouns ("ELMo's idea and ELMo's method ended up in different
  places") without referring to the piece.
- "A reader who keeps only 'state of the art on six tasks' misses that spread"
  gestured at a hypothetical reader. Replaced with a direct statement ("The
  single summary, 'state of the art on six tasks,' hides that spread") that keeps
  the point and drops the reader.

Nothing else read as filled-in from a pattern. The edges hold up: the section
openers are concrete ("The test of the idea was breadth"), the closers land on
real content ("The phrase is often pinned on ELMo alone now. Ruder pinned it on
all three." / "The first part the field kept. The second it did not."), and the
article's last sentence is the earned judgment, not a moral. The "not X but Y"
in the six-task section corrects a real misreading the section just set up (that
the win's size is the point), so it stays. The procedural "you" in the mechanism
section is generic method description in the voice guide's register, not an
address to the reader, so it stays.

## The experience

The rendered page teaches the four ideas in order and reads straight through. The
six-task table carries the result faster than prose could and keeps the uneven
spread visible (SQuAD's 24.9% down to SNLI's 5.8%), which is the scale point the
desk wants; no chart or source asset would add evidence the table does not
already hold, so none was added. What the piece gives beyond its sources: it
separates the idea ELMo is credited with from the method it actually shipped and
shows, from ELMo's own results and BERT's own positioning, that the field kept
the first and dropped the second within a year. That is a real read of two papers
that neither paper performs for the reader, and it survives the straight-through
read. The recent-pattern risk (staging this as a closing "the famous X was not
the real X" reveal) is avoided: the split is stated in the mechanism section and
carried through the results, the credit correction, and BERT, so it is the spine.

## Edits

- Recast the what-bert-replaced topic sentence from "This is the split the lesson
  has been tracing. ELMo's idea, that..." to "ELMo's idea and ELMo's method ended
  up in different places. The idea, that..." (removed body self-reference).
- Replaced "A reader who keeps only 'state of the art on six tasks' misses that
  spread." with "The single summary, 'state of the art on six tasks,' hides that
  spread." (removed hypothetical-reader gesture).
- Re-ran `./nb stamp` (words=1966) and `./nb check ... --series the-evidence`
  with links: BLOCK: 0, WARN: 0, PUBLISHABLE.

## Decision

approve. The argument is right and shown from the primary papers, the six-task
numbers recompute exactly, the idea/method split is precise in both directions,
and the two body self-references are fixed; the proof is clean with links.
