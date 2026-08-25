# Editorial review: the-evidence/clip (editor/01)

## Skeptic

Thesis: CLIP's most-cited number, 76.2% zero-shot on ImageNet, was real, but the
famous parity with a supervised ResNet-50 leaned on human prompt-writing and a
private 400-million-pair dataset, and the same model is strong on shifted natural
photos while weak on counting, satellite, and traffic-sign tasks. Read as a claim
about naming photo categories in words the number holds; read as proof CLIP
learned to see unaided it does not. The piece also credits two genuine strengths
so the read is not a pure debunk.

Claims it stands on, each tested:

- **76.2% zero-shot on ImageNet with none of the 1.28M ImageNet labels.**
  Confirmed against the paper (abstract states it matches the original ResNet-50
  without the 1.28M training examples; 76.2% is the best model, ViT-L/14@336px).
  The article correctly drops the "@336px" as a simplification without distorting
  the figure.
- **Prompt engineering plus 80-prompt ensembling added nearly five points.**
  Confirmed word for word in the primary: template "+1.3%", ensemble "an
  additional 3.5%", combined "almost 5%". The article's central honesty move,
  keeping the ViT-L/14 headline (76.2%) distinct from the ResNet-50 variant where
  the 1.3/3.5 gains were measured, matches the evidence's explicit warning and the
  paper. The headline attaches "nearly five points" to CLIP's ImageNet score
  generally, which is the paper's own "almost 5%" statement, and the body then
  disambiguates the two models. Holds.
- **400M pairs (WIT) never released; only code and weights were.** Confirmed at
  the openai/CLIP repo: it ships code and weights via clip.load and names no
  dataset. Holds.
- **Robust to distribution shift, gap closed "by up to 75%", cause is data
  diversity (Fang 2022).** Both confirmed: the CLIP paper's own "up to 75%"
  sentence, and Fang et al.'s abstract quote "the more diverse training
  distribution is the main cause." Holds.
- **Contamination audit near-null.** Confirmed: median overlap 2.2%, "overall
  accuracy is rarely shifted by more than 0.1%", max 0.6% on Birdsnap. The article
  calls Birdsnap "one bird dataset", which is accurate. Holds.
- **Weak on counting, satellite, traffic signs, tumor detection.** Confirmed
  against the paper's own list; the "paper's own caveat" note quotes the
  non-expert-humans sentence exactly. Holds.
- **Reproduced on open data: OpenCLIP on LAION-2B hit 80.1%; scaling curves differ
  (Cherti 2022).** Both confirmed against the LAION blog and Cherti's abstract
  ("the OpenAI and OpenCLIP models exhibit different scaling behavior"). Holds.

Nothing broke. I pushed hardest on the claim I most wanted to keep, that prompt
work bought several of the headline points, and it survives because the paper
applies prompt engineering to its reported scores and states the ~5-point figure
itself; the only nuance (magnitude measured on ResNet-50, not the headline model)
is already handled in the body.

Display text and labels, verified descriptor by descriptor:

- Headline, dek, and all five authored subheads are claims about the world the
  piece establishes, not method grades.
- Authors named in the dek (Radford, Kim, OpenAI coauthors) match the paper
  masthead and evidence.
- Every figure in display text (76.2%, 400 million, +1.3/+3.5/~5, 80.1%) matches
  its owning primary.
- The two Background link display texts match the exact titles of the target
  lessons (word-embeddings and reading-images) on disk. The two Go deeper links
  (arXiv 2103.00020, mlfoundations/open_clip) are correctly labeled.

`data-nb-kind` audit against the researcher's primary/secondary test (authorship
and stake): s1 CLIP paper, s2 openai/CLIP repo, s4 Fang, s5 LAION, s6 Cherti all
own their claims = primary (5). s3 Hugging Face docs reports on CLIP from outside
the authoring party = secondary (1). 5 primary + 1 secondary, matching the
evidence record and the brief.

Citation hrefs: opened all six as printed. Each lands on the source itself
(arXiv abstract pages, the GitHub repo, the HF model doc, the LAION blog), not a
fetch endpoint. All resolve.

## Cut

One sentence failed the slop test: the signpost "Two things are worth keeping
separate." opening the model-distinction paragraph in the prompts section. It
described the article's own method rather than doing reasoning; the two sentences
after it make the ViT-L/14-vs-ResNet-50 distinction on their own. Cut directly.

The rest held under a sentence-by-sentence pass and a separate edge pass (first
and last sentence of every paragraph, section, and furniture component, read out
of order):

- Negative-parallelism check: two constructions, both earned. "The web-scale
  pile of images, not the language captions or the contrastive method, was doing
  the work" corrects a named misconception that Fang tested and ruled out. The
  takeaway's "Read as X, it holds. Read as Y, it does not." names both readings
  as real, which is the article's thesis. Neither is a strawman.
- Recent-pattern / formula check against the brief's notes: the piece does not
  use the "What <authors> actually built" heading mold, does not march through
  the [shorthand vs reality] -> [what X built] -> [numbers table] -> [what
  inherited the name] structure (it opens by stating the result, puts its table
  inside the prompts section, and closes on reproduction), and the takeaway is a
  two-way reading of the number, not the "ask which of the two" directive mold.
  The dek is two clauses joined by "and", not a comma triad, semicolon reversal,
  or suspended question.
- Prompt-leakage check against commission and brief: the bookend framing ("tell
  the model apart from the setup around it") is the lesson's own reader-takeaway,
  reworded, not lifted; the reader-address is allowed in the two bookend cards.
- Punctuation and grammar: clean. No em-dash overuse, colons used for payoff, no
  comma splices.

Furniture: the stat strip (76.2% / 0 / 400M), the prompt-gain table, and the
"paper's own caveat" note each do work (the note carries the paper hedging in its
own voice, the Resnick move the voice guide asks for). None is decorative; none
reads as a stacked block. No missed component: the strong-vs-weak spread and the
75% robustness figure are carried adequately by the prose table and the paper's
weak-task quote, so no source asset is required (see Required work).

## Reader

Read straight through as the course reader, what I have that the sources alone
would not give me: a single number pulled apart into what it measured (naming
categories in words), what it borrowed (hand-written prompts and a private 400M
dataset), and what it genuinely earned (distribution-shift robustness the paper's
own follow-up traces to data diversity, and a contamination audit that clears the
score). The draft-handoff's original-work sentence claims exactly this, and the
article delivers it. Both answers survive: the piece does something to the
evidence the evidence does not do itself. The prose sits close to the
voice-guide exemplars (plain worked example before the abstraction, boundaries
stated as flat declaratives) rather than a median summary. The headline, reread
as the largest claim, commits to a finding the body defends.

## Edits

- Cut the signpost sentence "Two things are worth keeping separate." from the
  prompts section; the paragraph now opens on "The 76.2% headline is the best
  model, a vision transformer called ViT-L/14."

## Required work

None blocking.

- Optional (writer), not requested: a source asset (CLIP Figure 5, the
  per-dataset strong-vs-weak spread) would be the single most useful visual if
  one were wanted, but the prose table plus the paper's weak-task quote lets the
  reader test the claim, so I am not requesting it.
- The deliberately omitted 85.4% linear-probe number and ResNet-50's own ~76.1%
  figure stay omitted: the teach list is complete without them, and adding either
  would need verification the evidence flags as not-yet-done. No action.

## Decision

approve. Every claim holds against the primary sources, all six citations land on
their source, display text and labels are accurate, both genuine strengths are
credited, and the one slop sentence was cut in place.
