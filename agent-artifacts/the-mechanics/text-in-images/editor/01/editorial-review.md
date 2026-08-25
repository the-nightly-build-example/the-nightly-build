# Editorial review: the-mechanics/text-in-images (editor/01)

## Skeptic

Thesis: a generated image gets its letters wrong before any pixel is drawn,
because the text encoder hands the drawing step a whole-word chunk with the
spelling already thrown away, and the fix is an encoder that reads the prompt
one character at a time. The piece stands on four claims.

1. The diffusion drawing step never receives letters; the prompt reaches it as
an encoded code through cross-attention, and to that step letters are texture.
Checked against s1 (SD model card: fixed CLIP ViT-L/14 encoder, "cannot render
legible text") and s2 (latent diffusion: cross-attention conditioning). Both
opened and both land on the source. Held.

2. The encoder tokenizes the prompt into subword chunks, so the individual
letters inside a chunk stop being represented; this is where spelling is lost.
Checked against s3 (Character-Aware paper), s4 (DALL·E 3's own diagnosis), and
s5 (CLIP's 49,152-token lower-cased BPE vocabulary). The DALL·E 3 blockquote is
verbatim to the evidence record's Sec 5.2 quote and deliberately begins at "We
suspect" to skip the source's own grammatical slip; the load-bearing sentence
is unaltered. Held.

3. The letters are degraded, not erased: a 540B model spells >99%, a mid-size
encoder about 66%, so the information is recoverable only at a scale most
generators will not pay for. Checked against s3 (PaLM 540B >99%, T5-XXL 66% on
common words). The article says exactly this and does not overclaim ("The
letters are not erased"). This is the review's first focus point and it is
held.

4. Two distinct levers fix it: encoder SIZE (Imagen's frozen T5-XXL, 4.6B) and
encoder TYPE (character-aware ByT5), with type helping more for less (25+ pts
common, 30+ rare; lead held against a char-blind rival trained 6.6x longer; a
43%-smaller char-aware encoder still wins; +4.8% Concat recipe). Checked against
s3 and s6 (Imagen: text-encoder scaling beats U-Net scaling). Size and type stay
separate throughout ("Size helped first" vs "the gain comes from reading
letters, not from a bigger model"). This is the review's second focus point and
it is held.

The settled-versus-open split the series wants is carried correctly: the encoder
governs whether the model *knows* the letters (settled), the drawing step governs
whether it can *shape and place* them (open), with the fought->fighted homophone
error (~11%, "about one try in nine") and the residual dropped/merged/misshapen
glyphs attributed exactly as the evidence attributes them (s3). No published
string-length limit for current systems is presented as known; it is flagged as
open, matching the evidence.

Display text audit. Headline states the finding with its surprise in front and
the piece defends it. Dek makes a world-claim (whole-word token, blurred
spelling, character-level fix), adds what the headline omits, and dodges the
comma-triad / semicolon-reversal / suspended-question molds. All five section
headings are concrete, in the piece's own nouns, and reconstruct the argument in
order. Every named figure (49,152; 4.6B; 66%; >99%; 25+/30+; 43%; +4.8%; 11%)
matches the evidence record's Numbers section. No number, name, date, or
quotation was altered.

data-nb-kind audit. s1-s7 primary, s8 secondary. s1/s4/s7 are maker documents
about their own models (primary); s3/s5/s6 are the method-owning papers
(primary); s2 owns latent diffusion (primary); s8 is the diffusers docs
describing DeepFloyd from outside the authoring party (secondary, genuinely an
independent author, not a relabeled primary). The commission's floor (>=8
sources, >=4 primary, >=1 secondary) is met. Labels correct.

Citations. All eight hrefs opened as printed. s1, s2, s3, s5, s6, s7, s8 each
land on the exact cited source (title and authors confirmed where the fetch
reached them). s4 is a ~28 MB PDF that exceeds the fetch ceiling; it is the
canonical OpenAI CDN path for the DALL·E 3 report, passed the writer's
link-check, and its quoted passage matches the evidence record verbatim, so the
citation stands. No miscitation found; no citation routed.

One near-error fixed directly (not routed): Imagen's text-rendering comparison
read "clearer than the earlier system's." Coming three paragraphs after the
DALL·E 3 discussion, "the earlier system" dangles and could be misread as DALL·E
3 (which postdates Imagen). The evidence's comparison is specifically Imagen vs
DALL·E 2 (Fig A.21, quoted-text prompts), so I named it: "clearer than DALL·E
2's." Evidence-supported; no claim changed.

## Cut

Sentence-by-sentence and edge passes against spec/slop.md. The prose is
concrete and the edges mostly carry facts or reasoning. Negative-parallelism
constructions ("not wrong so much as", "not a drawing mistake", "the gain comes
from reading letters, not from a bigger model", "not a general upgrade") each
correct a misconception the piece actually names (the "steadier hand" /
"just bad at text" belief, or the size-vs-type confusion), so they are earned
and stay. Zero em-dashes; no banned terms; no leverage/load-bearing/machinery.

One cut made, for prompt leakage plus method-summary. The orientation paragraph
ended: "Each step names one real part and what it does. Mark each as settled
engineering or a question the builders still cannot answer, and stop at the step
below which nothing would change the letters." That is a close paraphrase of the
series prompt and commission ("Each step names a real part... Mark which steps
are settled... a step where nothing below it would change the answer"), and it
describes the article's own method rather than teaching anything. The
settled/open lens and the "hit ground" idea are both delivered inline where they
are earned ("is settled", "This is the open part of the chain", "That is the
bottom of the chain"), so the preview was redundant signposting. Cut. The
paragraph now ends on the concrete orientation ("walking backward from the sign
to the moment the word entered the system"), which hands cleanly into "Start
with the part that makes the pixels."

Furniture. The note (quotation, label "The makers' own diagnosis") and the stat
strip are both doing real work and each stat is cited in nearby prose. I
tightened the third stat's label from "smaller encoder, same result" (ambiguous:
same as what?) to "smaller encoder, still wins", matching the prose sentence it
sits beside ("a version of it 43% smaller than T5-XXL still won"). No component
added or removed; the piece already reads as a continuous article, not a stack
of blocks.

Formula check against the recent-pattern notes. The opener avoids the "The X has
N parts" decomposition mold. The takeaway lands the diagnostic judgment (a
question that separates a real explanation from a shrug) rather than re-listing
the parts. Headings vary in build and none repeats the comma-and-clause rhythm
flagged. No catchphrase.

## Reader

Read straight through as the paper's smart, non-coder reader: what I have that
the sources alone would not give me is a single backward chain from a garbled
sign down to subword tokenization and back up, plus a diagnostic none of the
sources states outright, that you can read a bad sign two ways (a confident
real-looking wrong word is the encoder never having the spelling; a word bent
into almost-letters is the drawing step failing to shape letters it was given),
with the size-vs-type levers kept distinct. The draft-handoff's original-work
sentence claims exactly this synthesis, and it survives the read. The prose sits
closer to the voice-guide exemplars (Evans, Ciechanowski) than a median summary:
it states the behavior first, names the wrong belief before replacing it, walks
the chain one hand-off at a time, and closes the loop back on the sign. Headline
holds as the largest claim.

## Edits

- Cut two method-summary / prompt-leak sentences from the orientation paragraph
  ("Each step names one real part and what it does. Mark each as settled
  engineering... nothing would change the letters.").
- Changed "clearer than the earlier system's" to "clearer than DALL·E 2's" to
  remove a dangling referent; DALL·E 2 is the comparison the evidence records.
- Tightened stat-strip label "smaller encoder, same result" to "smaller encoder,
  still wins" for precision and to match the adjacent prose.

## Required work

None blocking. Optional, writer's call (not required for publication): the
Character-Aware paper's Figure 1 (matched prompts, character-blind top row vs
character-aware bottom row) would let a reader test the central claim visually;
the writer left it out under a medium-effort budget and the argument stands on
prose plus the controlled-experiment numbers. If the orchestrator wants the
stronger visual, route an asset capture to the writer (arXiv 2212.10562, cropped
to one matched pair with the two row labels). Not a condition of approval.

## Decision

approve. The keystone is held without overclaiming, size and type stay distinct
levers, every number matches the evidence, all citations land, no code slipped
in, and the remaining work (a source asset) is explicitly optional.
