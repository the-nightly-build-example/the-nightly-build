# Editorial review: the-evidence/whisper (editor/01)

## Skeptic

The thesis is one design property seen twice: the decoder that always predicts a
next token is what carries Whisper across audio it never trained on, and the same
always-emit design is what fills silence with fluent, invented words. The article
stands on four claims, and I pushed hardest on the synthesis, since it is the
lesson's original work.

- **Whisper's edge is robustness, not lowest error.** Held. The paper's own
  Table 2 shows Whisper Large V2 and wav2vec 2.0 Large tied at 2.7 on LibriSpeech
  clean, and the abstract/Section 3.2 call the 2.5 best-model number "relatively
  unremarkable," roughly a modern supervised baseline or mid-2019. Verified in the
  paper text. The article never claims Whisper is the most accurate transcriber.

- **The robustness result is quantified honestly.** Held after a fix. Table 2's
  Average row (wav2vec 29.3, Whisper 12.8, 55.2% relative error reduction) is
  computed over 13 rows, excluding only the LibriSpeech-clean tie; I recomputed
  both averages from the per-dataset numbers and they land on 29.3 and 12.8, so
  "thirteen other datasets" is the correct denominator. But the prose describing
  the movement was wrong: it said the supervised model's error "nearly triples
  while Whisper's barely rises." From the 2.7 tie, wav2vec climbs to 29.3 (an
  order of magnitude) and Whisper to 12.8 (nearly fivefold). Neither is "triples"
  or "barely." The direction was right, the magnitudes false, overstating
  Whisper's robustness. Rewritten to the comparative truth the table supports:
  the supervised model's error climbs far more steeply than Whisper's. The table
  caption's "audio neither trained against" was also false for the LibriSpeech
  Other row (the supervised model trained on LibriSpeech); recast to "the thirteen
  other datasets."

- **The scale and weakness of the supervision.** Held. 680,000 hours total,
  117,000 across 96 other languages, 125,000 of translation, ~65% of compute on
  English, and the "transcript-ese" machine-transcript filter are all stated
  verbatim in the paper. The derived ~438,000-hour English figure was correctly
  left out. LibriSpeech at ~1,000 hours confirmed against OpenSLR.

- **Hallucination is the same design, measured against a different guarantee.**
  Held, and this is where the synthesis proves. The paper (Section 6) names
  "complete hallucination where the model will output a transcript entirely
  unrelated to the actual audio"; the model card names the mechanism (the model
  combines next-word prediction with transcription). Both quoted accurately except
  one: the card says "high-risk domains like decision-making contexts," and the
  article quoted "higher-risk." Corrected. The article does not present the paper
  as refuted; it states plainly that average-WER robustness and per-record
  reliability are different measurements, which is the honest reading.

No single figure is offered as the hallucination rate. Koenecke's 1.4% is the
study's own measured value (its abstract rounds to "roughly 1%"; the intro and
Section 3 give 1.4%), correctly scoped as rising with non-vocal duration and
concentrated in the aphasia group; the AP field counts (8 of 10 meetings, half
of 100+ hours, nearly all of 26,000) are labeled uncontrolled practitioner
tallies. All display-text numbers, names, and the Nabla deployment figures
(30,000 clinicians, 40 health systems, ~7 million visits, audio erased for "data
safety reasons") check against the AP article. The WER worked example (6+3+1 over
13 = 76.9%) is verbatim from Jurafsky & Martin.

data-nb-kind audit: five primary (paper, WER textbook, OpenSLR, model card,
Koenecke), one secondary (AP). Each is the party that owns its claim; the AP is
correctly outside the authoring party. Source floor met. Every href opens to the
source itself: arXiv abstract page, the chapter PDF, the OpenSLR corpus page, the
model-card file, the FAccT paper PDF, and the AP article at the correct slug.
Zero-shot is linked to the-evidence/gpt-2, not re-taught.

One accepted seam, not routed: the orientation cites the 2.5 best-model number
and the table cites 2.7 for Large V2. Both are the paper's and both are labeled
for what they are, so the piece is honest, not inconsistent.

## Cut

One sentence cut outright for slop: the orientation's closing "To see why that is
the interesting claim, you first need to know what the error rate counts" was a
pure signpost pointing where the piece was going; the WER section stands without
it. Two slop tells rewritten in place rather than left: "That movement is the
whole subject of the paper" (the "X is the whole Y" family) became "That movement
is what the paper measures," and the topic sentence "The scale is the point, and
it is easier to feel against..." lost its empty "is the point" opener while
keeping the anchoring comparison the voice guide asks for.

Edge sentences otherwise hold: the dek leads in Whisper's own nouns (hours, the
robustness gap, medical transcripts) and breaks the recent "The [X] paper
[verb]..." mold; the section headings reconstruct the argument and avoid the
"What 'X' actually names" and author/number-count formulas the brief flagged. The
two "It is not X, it is Z" contrasts (robustness is not a lower score; scale did
not buy the lowest error) survive because the misconception they correct — that
robustness means the best benchmark number — is real and named throughout. The
bookends address the reader as the template allows, and each is particular to this
lesson: the opener sets up what was measured and why silence gets filled, and the
takeaway resolves it with the question the lesson teaches the reader to ask.

## Reader

Reading only the article, I come away with something no single source gives: the
same next-token decoder is both the source of Whisper's robustness and the source
of its hallucinations, and the paper's robustness is an average over many
transcripts while medical and legal use needs a per-record guarantee the paper
never made. The original-work sentence claims exactly this, and the article
delivers it. The prose sits with the voice-guide exemplars, not a median summary:
it teaches WER from a worked transcript, anchors 680,000 hours against 1,000,
scopes the 1.4% honestly, and marks where the evidence stops. The headline holds
as the largest claim — it transcribes audio it never trained on, and silence no
one spoke.

## Edits

- Rewrote the robustness-movement sentence: the supervised model's error "climbs
  far more steeply than Whisper's" replaces the false "nearly triples while
  Whisper's barely rises."
- Recast the table caption to "the two models tie on the clean benchmark and
  diverge across the thirteen other datasets," removing the false "audio neither
  trained against."
- Corrected the model-card quotation from "higher-risk domains" to "high-risk
  domains."
- Cut the orientation signpost "To see why that is the interesting claim, you
  first need to know what the error rate counts."
- Rewrote "That movement is the whole subject of the paper, and it is bought with
  scale" as "That movement is what the paper measures, and scale is what buys it."
- Trimmed "The scale is the point, and it is easier to feel against what came
  before" to "The scale is easier to feel against what came before."
- Dropped the loose "clean" from "short, clean clips" (the Koenecke segments are
  aphasia-corpus audio, disproportionately affected); now "short clips."
- Restored the source's real title to s5: "Careless Whisper: Speech-to-Text
  Hallucination Harms."

## Required work

- **orchestrator**: stamp the article. Three sentences were cut or shortened, so
  the nb-meta word count and reading time will recompute. No reporting, no new
  evidence, and no redraft are needed; the article proves (`nb check`,
  no-check-links, BLOCK 0 WARN 0) and no href changed, so the full link proof is
  unaffected.

## Decision

approve — the central synthesis is earned from the primary documents and every
number checks; the two correctness faults (a false robustness magnitude and a
misquoted model card) and the slop were fixable directly, and only stamping
remains.
