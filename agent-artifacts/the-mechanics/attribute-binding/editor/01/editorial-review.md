# Editorial review: the-mechanics/attribute-binding (editor/01)

## Skeptic

Thesis: a text-to-image model puts a prompt's attributes on the wrong objects
because the prompt reaches the image model with no record of which adjective
belongs to which noun; the fault lives in the two parts that carry words into the
picture (text encoder and cross-attention), which is settled, while the division
of blame between them and whether fixes generalize are open.

Claims it stands on, and how each held:

- **Headline: "Image generators put a prompt's colors on the wrong objects."**
  Accurate and appropriately plural: the wrong-attribute behavior is documented
  on Stable Diffusion (T2I-CompBench, Attend-and-Excite, StructureDiffusion) and
  DALL-E 2 (Conwell & Ullman, Rassin et al.). Held.
- **Dek: SD binds a color to the right object at 0.38 out of 1, because the
  prompt is encoded with no record of which adjective belongs to which noun.**
  Makes a claim about the world, not a grade of method. 0.38 is the T2I-CompBench
  B-VQA color-binding score for SD v1.4 (evidence 0.3765), correctly given as a
  0-1 score rather than "38% of the time." The causal clause states the article's
  ground fact (structure is never encoded), which the round focus marks as the
  settled half, not the open blame-split. Held.
- **The tested prompt fails as shown.** "A yellow bow and a brown bench" yields a
  yellow (leaked) bench in the baseline; cited to s1 and carried by the asset.
  Verified against the image (see visual evidence below). Held.
- **T2I-CompBench: SD v1.4 scores 0.38 color, 0.12 spatial.** Matches evidence
  (0.3765 B-VQA; 0.1246 UniDet). "on top of" as a spatial-relation example is
  fair. Held.
- **Conwell & Ullman: 1,350 DALL-E 2 images, 169 judges, ~22% matched.** Matches
  evidence exactly (169 is the post-exclusion judge count; ~22% overall). Held.
  Relation-match numbers are labeled as relations, not conflated with color
  binding.
- **Pipeline claims** (CLIP 400M pairs, whole-caption objective; latent-diffusion
  cross-attention; causal-mask blending). Each cited to its owner: CLIP s4,
  Rombach s5, and the causal-mask reasoning to StructureDiffusion s6 (which is
  where that statement lives, not asserted of CLIP directly). Held.
- **The two fixes and the CLIP gap.** StructureDiffusion 19.2%->22.7% two-object
  color (s6); Attend-and-Excite full-prompt ~0.83 vs worse-served object
  0.60-0.63 lifted to 0.69-0.72 (s1). Both match evidence. Critically, the piece
  uses the CLIP gap as the honest quantified stand-in and describes it as
  full-prompt vs worse-served-object similarity, and it does NOT assert a
  single-object-vs-two-object accuracy pair anywhere. Round-focus item cleared.

Pushed hardest on the claim I most wanted to keep, the "encoder hands over a bag
of concepts" reading, and it does not overreach: the draft presents it as "the
tidy story," then complicates it in front of the reader (Attend-and-Excite
recovers a large share touching only cross-attention; the encoder-side fix barely
moves the numbers), and states outright that the split "does not settle where the
fault lives" because each method favors the part it touched and the numbers "can
not be compared directly." This is competing-method evidence, marked as open, not
a controlled decomposition. Round-focus item cleared.

data-nb-kind audit: s1-s7 primary (method/benchmark/observation papers that own
their numbers firsthand), s8 secondary (a 2025 review synthesizing others).
Labels are correct; the one review is the one secondary, and no primary label
hides a missing independent source. Source floor met (8 sources, 7 primary, 1
secondary).

Every citation href opened and resolves (HTTP 200): s1 2301.13826, s2 2307.06350,
s3 2208.00005, s4 2103.00020, s5 2112.10752, s6 2212.05032, s7 2210.10606, s8
2511.10136. The three "Go deeper" links (2307.06350, 2301.13826, 2511.10136) also
resolve. Note, not a break: arXiv 2307.06350 now serves T2I-CompBench++ while the
citation label carries the original T2I-CompBench title; the SD v1.4 scores are
identical across both versions and the URL lands on the paper's own abstract page,
which the evidence record explicitly sanctioned. No change made.

No arithmetic to recompute beyond the reported figures, all of which match their
denominators and owners. No break found; nothing routed from this read.

## Cut

Ran the placeholder test sentence by sentence, then walked the edges out of
order, then the delete test.

- No em-dashes, no decorative "-ing" trailing clauses, no elaborate copula, no
  vague attribution, no puffery, no fluff openers. Grep and manual pass both
  clean.
- One negative-parallelism line ("The wrong-colored object is not a rendering
  glitch. It is what happens when...") corrects a real, named misconception, that
  the wrong color is a low-level drawing fault rather than an encoding/binding
  one, and is the payoff the takeaway earns. Stays.
- One self-reference ("This lesson works backward...") sits in the "Why this
  matters" bookend, which the lesson template explicitly licenses to address the
  reader (slop.md, "A template or a press may allow one of these failures"). It
  still says something: it names the backward-causal-chain approach and the
  marking of disagreement, and the card closes on a concrete learning objective.
  Stays.
- Edge sentences all carry a fact or a reasoning step. The article's last
  sentence gives the reader an actionable question tied to the two-step
  mechanism, not a signpost; it survives the delete test.
- Formula check against the recent-pattern notes: opener is a plain base
  statement (Wolfram move), not a confident-wrong-output line and not the "the
  model never X before it draws a pixel" mold; headings vary in construction
  (subject-verb / noun phrase / where-clause / how-clause); the dek avoids the
  comma-and mold and the colon lead; no colon-subtitle headline. No formula
  found.
- Prompt-leakage check against commission and briefs: the commission's "red cube
  on a blue sphere" example and its "bag of concepts" phrase are not lifted; the
  article uses the source's own "yellow bow and brown bench" and reworks the
  concepts framing into "the tidy story." No planning labels, selection rules, or
  assignment-fulfilled claims. Clean.
- Exemplar-borrowing check against the voice guide's quoted passages (Wolfram,
  Alammar, Olah): the draft uses their moves (plain base statement; revise the
  first guess and check it; mark settled and open together) without borrowing any
  distinctive wording. Clean.
- Furniture: the stat strip and the two-row table both do work, and the table's
  caption honestly warns that the two gains measure different quantities on
  different prompt sets and cannot be lined up, which is the exact editorial point
  the section needs. Neither is decorative; the piece does not read as a stack of
  blocks. No component added or removed.

Zero sentences failed the slop test. No cuts required.

## Reader

Read straight through as the paper's declared reader: what I have that the
sources alone would not give me is a single backward causal chain from the
visible wrong-colored bench to one ground fact (the sentence's structure was
never encoded), plus a reading of the two fix papers against each other that
separates what their combined evidence settles (the fault sits in the encoder
and the cross-attention, because every working fix reaches into one of those two
parts) from what it leaves open (how the blame divides) - a weighing neither
paper performs alone. The draft-handoff's original-work sentence claims exactly
this, and it survives the read. The prose sits closer to the voice-guide
exemplars than to a median AI summary: it states the base mechanism plainly
before opening it, corrects its own first account in front of the reader, and
marks the settled and open steps in the same breath. The headline, reread as the
largest claim, is accurate.

## Visual evidence

Inspected asset-1.png (Attend-and-Excite Fig. 2, "incorrect attribute binding"
column). The crop retains the exact prompt label "A yellow bow and a brown
bench" and the source's "Incorrect Attribute Binding" label, and omits the
catastrophic-neglect column, correct discipline. Verified the row identities the
caption asserts by reading the panels: top row benches are yellow (top-left) and
orange-yellow (top-right), the leaked-attribute baseline; bottom row benches are
brown (bottom-left) and dark maroon/brown (bottom-right), the corrected
Attend-and-Excite outputs. The evidence the argument spends - yellow landing on
the bench in the baseline and not in the fix - is retained. Caption is a factual
cited label (source 1, data-nb-locator "Fig. 2"), with interpretation kept to
prose. Asset passes; no recrop routed.

## Edits

None. The draft required no direct changes.

## Required work

None.

## Decision

approve - the argument holds claim by claim, the asset and its caption faithfully
carry the evidence, all citations resolve and are labeled correctly, the
single-vs-two-object number is correctly avoided in favor of the CLIP-gap
stand-in, and the "bag of concepts" reading is cleanly framed as an open question;
the prose is clean against spec/slop.md with nothing to cut.
