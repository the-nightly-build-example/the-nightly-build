# Editorial review: the-mechanics/hands-in-generated-images (editor/01)

## Skeptic

Thesis: a six-fingered hand is the expected output of a diffusion model that
optimizes for locally-real, globally-coherent pixels with no step that counts
fingers; hands are the worst case because they carry little signal and enormous
articulation variance; the cause is understood but the failure is receding, not
permanent.

The claims it stands on, each tested:

1. **The generator counts nothing; the objective has no anatomy term.** Grounded
   in DDPM (s2) and latent diffusion (s3). Both hrefs resolve; both abstracts
   confirm the denoising-reconstruction objective and, for s3, latent-space
   denoising with cross-attention text conditioning. The article is honest that
   this is an argument from the objective as written, not a measured finding
   ("This is a claim about the objective as written, not an experiment anyone
   ran"), and it steelmans the counter (a large model learns an implicit
   statistical prior). This matches the evidence record's framing note exactly.
   Held.

2. **Two distinct step-3 causes.** The round focus pushed hardest here. The
   article keeps them apart: reason one is training-data prominence/scarcity
   (Stability AI via BuzzFeed, s4; Britannica, s5), reason two is intrinsic
   diffuseness from few pixels plus high articulation (HanDiffuser, s6;
   FoundHand, s8). The section names the seam outright ("two reasons, and they
   are different reasons, though they are easy to run together") and flags that
   FoundHand states both halves in one line rather than blurring them into one.
   Held, not blurred.

3. **16 joints, 27 degrees of freedom.** Attributed in prose to ElKoura and
   Singh 2003 and cited to HandRefiner (s7) as where the figure is read, which is
   the attribution the evidence record and writer brief require. The figure and
   scope match the Numbers section. I changed the model descriptor from
   "biomechanical" to "kinematic" to match the owning source's own word
   (HandRefiner: "A kinematic model of hand contains 16 joints and 27 degrees of
   freedom"). Held after fix.

4. **Frequency stays qualitative.** The article never asserts a malformed-hand
   base rate ("How often is not something anyone in this literature has measured
   cleanly"), and the holds-up grid repeats the caveat. HandRefiner's "97 of 100"
   is not used anywhere, so the inverse-measurement trap the brief warned about
   is avoided. The one prevalence figure (HanDiffuser's 27%) is framed as
   human-rater plausibility judgment on one model, not a finger-count rate. Held.

5. **Not a permanent limit.** The gap-closing section marks cause (settled)
   against frequency and "solved" (open), and shows the failure receding through
   HandRefiner mesh guidance (s7), HanDiffuser pose parameters (s6), and
   FoundHand's ten-million-image dataset (s8). The closer reasons that the
   failure "gives way to more data and better guidance" is the sign it was
   coverage, not an in-principle barrier. Held.

Citations: all eight hrefs opened as printed and resolve to the source itself
(six arXiv abstract pages, BuzzFeed News, Britannica). The two Go-deeper links
(HandRefiner, FoundHand) and the internal Background link to
`the-mechanics/image-generation` also resolve; the internal link resolves against
the published library in open mode, as the writer's proof confirmed.

`data-nb-kind` audit: s2, s3, s6, s7, s8, and s1 are labeled primary — each owns
the method, diagnosis, or pipeline it is cited for. s4 (BuzzFeed) and s5
(Britannica) are labeled secondary; both carry the same Stability AI training-data
line, and the article correctly treats Britannica as the popular-consensus
retelling rather than independent corroboration, so no false independence is
claimed. Source policy met: 8 sources, 6 primary, 2 secondary.

Display text: headline ("An image generator never counts the fingers it draws")
is the thesis, subject and verb and surprise up front, no colon, no Betteridge.
Dek adds "worst case" and "better data closing the gap" without restating the
headline and makes a claim about the world, not about the article's method. Its
"learns how images look but not how a hand is built" is an earned contrast: the
misconception it corrects is the piece's central, named one. Subheads reconstruct
the argument (assumption to no-counting-step to few-pixels-many-joints to
gap-closing) and none is a scaffolding slot. nb-meta dek matches the rendered
dekline verbatim.

## Cut

Slop pass, every sentence including display text and both furniture components.
The prose is clean and specific; the edges mostly carry facts or reasoning steps.
Findings and fixes:

- **Reader address in the body.** The round focus and the paper's rulebook (press
  editorial, template identity, commission, brief) restrict reader address to the
  two bookends. The body broke this twice. The orientation opener was an
  imperative to the reader ("Ask an image generator for a person, then look at
  the hands"), and the no-counting-step paragraph used the generic second person
  ("Read the objective... and you find... You do not find a term for a hand").
  Recast both impersonally, no claim or citation touched.

- **Formula echo.** That same opener reused the "Ask a [system] for a [thing]"
  mold of the recent random-numbers piece ("Ask a chatbot for a random number and
  it says 7"), which the recent-pattern notes flagged. The impersonal recast ("An
  image generator asked to draw a person routinely gets the hands wrong") breaks
  the mold as well as the address.

- **One signpost cut.** "What matters for hands is what the model is trained to
  do, and what it is not" fails the slop reduction test (subject-interchangeable)
  and only signposts the pivot the next paragraph makes on its own. Deleted; the
  flow from "take it as given here" into "Training rewards one thing" is intact.

- **One reflex negative trimmed.** "That much is settled, not speculation" tags a
  strawman the piece never names. Cut to "That much is settled," which is the
  settled-vs-open call the series asks for, said flat.

- **Vague attribution named.** "As one researcher of AI and the arts put it" gave
  a direct quote without the name the evidence record holds. Named her: Amelia
  Winger-Bearskin.

- **Figure label corrected.** "only 27 percent were called plausible or better"
  turned the rating axis into a tier. The evidence record's figure is "rated Good
  or better for plausibility." Rewrote to "rated good or better for plausibility"
  so the tier and axis both survive; the number and its framing (rater judgment
  on one model, not a malformation count) are unchanged.

No prompt leakage: the mechanism language the article shares with the commission
is reported fact about hands and diffusion, not copied planning or
assignment-fulfilled claims, and self-reference is confined to the two bookends.
No borrowed phrasing from the voice-guide exemplars (Ciechanowski, Luu, Evans).
Grammar and punctuation are sound throughout, including display text and
furniture. Roughly six sentences were touched, only one of them a straight
deletion; the rest were faithfulness or address fixes.

Furniture: two components, each earning its place. The "In plain language" note
lands the pivot (the objective scores appearance, never finger count). The
holds-up grid crystallizes settled cause against soft/open frequency, which is
the series' settled-vs-open mandate, and its careful column surfaces the two
honest seams (no base rate; "interpolates to a plausible hand" is behavior, not
an isolated mechanism) more sharply than the prose. Two components in ~1770 words
reads as a continuous article, not a stack. Correctly no Verdict note on the grid
and no Verdict block at the body's close, per press editorial; the takeaway
bookend carries the judgment.

## Reader

Read straight through as the paper's reader, the piece gives one thing the eight
sources do not give alone: a single behavior-to-cause account that reframes the
six-fingered hand as the predictable output of a denoising objective, holds the
two step-3 causes apart (correcting the popular single-cause story), and marks
where the account is settled against where it stays soft. The draft-handoff's
original-work sentence claims exactly this separation, "a separation none of the
sources makes on its own," and the article delivers it. Both answers survive, so
the piece teaches rather than restates. The prose sits closer to the voice-guide
exemplars than to a median AI summary: it names the reader's assumption (a hand
has five fingers, so the model must hold that fact) and dismantles it with a
concrete reason (the objective scores local texture and global coherence, with no
finger-count step), which is the Ciechanowski move the voice guide asks for, at
the matter-of-fact register it borrows from Evans. The headline, reread as the
largest claim, is the thesis and the piece defends it.

## Edits

- Recast orientation opener from a reader-directed imperative to an impersonal
  statement ("An image generator asked to draw a person routinely gets the hands
  wrong"), removing both the body reader-address and the "Ask a [system]..."
  formula echo of the recent random-numbers piece.
- Recast the no-counting-step sentence from generic second person ("Read the
  objective... you find... You do not find") to impersonal ("The objective it is
  trained on has terms for pixels and noise. It has no term for a hand...").
- Deleted the signpost "What matters for hands is what the model is trained to
  do, and what it is not."
- Named the quoted researcher: "one researcher of AI and the arts" to "the
  AI-and-arts researcher Amelia Winger-Bearskin."
- Changed "biomechanical model" to "kinematic model" for the 16-joint/27-DOF
  figure, matching the owning source's own descriptor.
- Corrected the 27% figure label from "called plausible or better" to "rated good
  or better for plausibility," matching the evidence record's tier and axis;
  number and framing unchanged.
- Trimmed the reflex negative "That much is settled, not speculation" to "That
  much is settled."

## Required work

None routed. No evidence gap, no broken central claim, and no repair that needs
reporting the editor lacks. The orchestrator re-runs `nb stamp` and `nb check`
after these edits before the PR; the edits change no source, asset, chart, or
citation target, so no new proof from the writer is required.

## Decision

Approve. Every round-focus item holds (frequency qualitative, no 97/100 misread,
two causes distinct, failure not framed as permanent, ElKoura and Singh
attribution, diffusion linked not re-taught), and the direct edits resolve the
body reader-address, a formula echo, a vague attribution, two figure-label
inaccuracies, and two slop-reflex sentences without touching a number, name, or
claim.
