# Editorial review: the-mechanics/counting-objects-in-images (editor/01)

## Skeptic

Thesis: no current image generator counts reliably past a handful of objects,
and the reason is two complementary failures upstream of the canvas: a text
encoder that registers which object is present far better than how many, and a
diffusion process with no step that holds a count or checks the result against
the request. Small counts (five or fewer) are usually right, accuracy collapses
above that, newer models beat older ones, targeted fixes work, and rewording the
prompt makes it worse.

Claims it stands on, and how each held:

- **The encoder is quantity-weak (cause one).** Owned by CLIP (2103.00020) for
  the architecture and the counting limitation, by ARO (2210.01936) for the
  bag-of-words behavior on order/attribution, and by Paiss (2302.12066) for the
  count-specific gap and its caption-scarcity origin. Every cited passage checks
  out against the evidence record and the primaries I reopened. The article
  avoids ARO's disputed percentages (the record flagged VG-Relation coming back
  as both ~59% and ~63%) and states only the firmly-owned qualitative finding.
  Held.

- **The generation step has no per-object tally (cause two).** Owned by Rombach
  (2112.10752) for cross-attention conditioning and by Make It Count
  (2406.10210) for the absence of any counting/identity mechanism. The article
  holds this as a separate, complementary cause rather than collapsing it onto
  the encoder — the paragraph "The two blind spots are separate..." does exactly
  what the commission and writer brief required. Held.

- **The calibration (right small, collapses large; improving, unsolved).**
  Owned by Guo/T2ICountBench (2503.06884) and Huang/T2I-CompBench++
  (2307.06350). The prose figures (~60-80% for one to five, ~10-30% for six to
  ten, under 10% for eleven to fifteen; numeracy ~0.45 rising to ~0.62)
  reproduce the evidence record's owning-primary numbers exactly. Held.

Numbers, recomputed against the owning primary (this round's flagged risk):

- CLIP counting accuracy ~32% -> ~76% (Paiss). Record gives 31.67% -> 75.93%;
  the rounding is honest. The article states them as plain before/after figures
  and invents no ratio, so the earlier "three times" error (real ratio ~2.4x) is
  gone. Correct.
- Make It Count / CountGen deltas. Article says "roughly doubles" on one
  benchmark, "close to two-thirds" on another, "ahead of DALL-E 3 on both."
  Record: ~54% vs ~26% (54/26 = 2.08, doubles), ~48% vs ~29% ((48-29)/29 = 0.66,
  two-thirds), CountGen ~54/~48 vs DALL-E ~38/~36 (ahead on both). All three
  characterizations are accurate and carry no false precision. Correct.
- Prompt refinement "more than 40 percent relative" (Guo). Matches the record.
  Correct.
- No DALL-E 3 caption-quality claim appears anywhere (confirmed absent, as the
  brief required); DALL-E 3 shows up only as a chart data point and as the
  baseline the CountGen fix beats.

Display text, descriptor by descriptor: the headline is a claim the piece
defends (the encoder collapses "six" toward "apples/some" before a pixel
exists), not a restatement of the neighbor's fingers headline. The dek makes a
claim about the world (the accuracy curve), adds what the headline omits, and is
neither the ", and"-twist nor the comma-triad mold. Section subheads all name a
real step of the argument. Every named paper title in the source list I checked
against its arXiv page.

Citations: I opened all nine hrefs as printed. Eight land on the source's own
page with a matching title. **Source 1 was mislabeled**: the href
(arxiv.org/abs/2503.06884, Guo et al.) is the correct paper and is cited for the
right claims, but the printed title read "T2ICountBench: Are Large-Scale
Text-to-Image Diffusion Models Good Counters?", which is not the paper's title.
The arXiv page titles it "Text-to-Image Diffusion Models Cannot Count, and
Prompt Refinement Cannot Help." With the primary open and the correct string
unambiguous, I corrected the source label in place to match the page the link
lands on. The Background/Go-deeper links resolve too: the three internal
`../the-mechanics/...` targets exist in the published library, and the two
Go-deeper arXiv links are the same (correct) papers as sources 5 and 7.

No central claim broke; no missing evidence; the source floor is met (9 sources,
8 primary, 1 secondary) and every `data-nb-kind` matches the record.

## Cut

Slop pass, every sentence including display text and the two bookends (the
bookends are allowed to address the reader; I judged their content like any
other prose, and it says something specific to this lesson each time).

Self-reference was the recurring fault. The body is supposed to speak to no one
and never mention the lesson; four body sentences broke that or narrated the
article's own method, and I cut or recast each:

- Cut the orientation roadmap ("This lesson follows that chain... until nothing
  is left unexplained") — pure method-narration; the section now ends on its
  thesis.
- Recast "they name the exact task this lesson is about" to "they name counting
  outright."
- Cut the self-referential pointer "as explained in this lesson's Background
  reading" (the denoising background is already linked in the band).
- Cut "This is not a house problem invented for this lesson"; the Imagen
  evidence that follows ("Google's own... 'CLIP is ineffective at counting'")
  carries the not-invented point without the piece defending itself.

Negative parallelism: several instances, but each corrects a misconception the
piece actually names (rendering glitch, the obvious prompt fix, presence vs
count), so they are earned and stay.

Formula: the headings were the pattern to break. Four of five joined two clauses
on a comma ("Six Apples, and...", "...a Checklist, Not a Count", "Five
Objects..., Eleven...", "Three Fixes..., and the One That Doesn't") — stamped
within the single piece, and the last is the ", and"-twist the brief flagged. I
retitled three to vary the construction, kept the one genuine antithesis
("Five Objects Are Usually Right, Eleven Rarely Are"), and made sure the
headings still reconstruct the argument in order. No "Where X still Y" closing
heading; no echo of the fingers piece.

Punctuation: replaced four semicolons that joined independent clauses with
periods (painter section, the numeracy sentence, the figure caption, the
takeaway), per the direction's plainest-mark rule. No em-dashes in the piece.

Grammar: fixed "Researchers built to fix this failure" (researchers are not
built) to "Researchers working to fix this."

Prompt-leakage: the two sentences that echoed the commission's method framing
were the self-referential ones already cut; no lifted brief language remains.
Reader-situation details (grocery ad, slide icons) are reported facts, not
leaks. No borrowed phrasing from the voice-guide exemplars.

## Reader

Reading what survives as the paper's declared reader: I come away able to say
where "six" is lost and why. The prompt becomes a fixed-length embedding from a
CLIP-style encoder that logs "apple" reliably and "six" barely; that embedding
steers a diffusion process through cross-attention that spreads the concept over
the whole canvas with nothing tracking a count; so the number out is whatever the
training data made likely, reliable to about five objects and falling off fast
past that. No single cited source assembles this chain for a newcomer — each
owns one link — which is exactly the original-work sentence in draft-handoff.md,
and it holds up against the article. The piece is not a restatement of its
sources.

The prose sits closer to the voice-guide exemplars than to a median summary: it
walks downhill a step at a time (Ciechanowski), coins one plain phrase ("the
encoder's checklist") and reuses it (Willison), and states the settled half as
settled and the open half as open (Evans). The headline is the largest claim and
the body earns it.

## Edits

- Retitled section 1 heading to "What the Model Receives From \"Six Apples\""
  (was "Six Apples, and What the Model Actually Received").
- Retitled section 2 heading to "The Text Encoder Barely Registers the Number"
  (was "The Text Encoder Keeps a Checklist, Not a Count").
- Retitled section 5 heading to "The Fixes That Work Reach the Encoder and the
  Painter" (was "Three Fixes That Work, and the One That Doesn't").
- Cut the orientation method-narration sentence "This lesson follows that
  chain... until nothing is left unexplained."
- Recast "they name the exact task this lesson is about" to "they name counting
  outright."
- Cut "as explained in this lesson's Background reading" from the diffusion
  sentence.
- Cut "This is not a house problem invented for this lesson."
- Fixed "Researchers built to fix this failure" to "Researchers working to fix
  this."
- Changed four independent-clause semicolons to periods (painter "no step...
  prompt. Whatever count"; "around 0.45. Two model generations later"; figure
  caption "one to eight objects. The score is"; takeaway "wrong count. It takes
  both together").
- Corrected source 1's title label to the paper's actual arXiv title,
  "Text-to-Image Diffusion Models Cannot Count, and Prompt Refinement Cannot
  Help" (was the non-title "T2ICountBench: Are Large-Scale Text-to-Image
  Diffusion Models Good Counters?"); href, kind, and cited claims unchanged.

## Required work

None blocking. Two non-blocking observations for the record, neither owed before
publication:

- writer (optional): the committed chart plots numeracy-by-model-generation (the
  "improving" point), while the evidence record named the accuracy-versus-count
  collapse as the single clearest visual for the lesson. The collapse is carried
  well in prose and the chart is honest (caption and 0-0.8 range make the
  unsolved state plain), so this is a preference, not a defect.
- The Background band links three of the four taught pieces the brief named
  (omits reading-images). Background is optional reading and the lesson works
  without it; the three chosen are the tightest fits. Left as the writer set it.

## Decision

approve — the causal chain is sound, every number reproduces its owning primary,
all citations resolve, and the prose, heading, self-reference, punctuation, and
source-label fixes were made in place with nothing left to route.
