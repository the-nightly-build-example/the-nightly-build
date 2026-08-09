# Editorial review: the-instruments/fid (editor/01)

## Skeptic

Thesis: FID is a distance between two Gaussian summaries of Inception-v3 features,
one for real images and one for generated; it tracks real damage inside a single
fixed pipeline but breaks comparability across setups, so the number can move a
long way while the pictures hold still. Load-bearing claims: (1) the construction
— pool3 2048-dim features, one multivariate Gaussian per set, Fréchet /
Wasserstein-2 distance between them; (2) the documented misled case — Projected
FastGAN and StyleGAN2 tie on FFHQ Inception-FID (5.28 / 5.30) yet split on a
CLIP-feature distance (4.67 / 2.76) and under human inspection; (3) three inputs
move FID without changing images (feature network via ImageNet-class matching,
sample count, resizing/compression); (4) the criticism is bounded — the three
failures break comparability, not within-pipeline sensitivity.

Construction, term by term. InceptionV3 pool3 / 2048-dim, mean + covariance
Gaussian, maximum-entropy justification, Fréchet = Wasserstein-2: all match the
owning primary (Heusel et al., 1706.08500, Appendix A1) as recorded in evidence.
The annotated equation is transcribed exactly:
`d^2 = ||m - m_w||^2 + Tr(C + C_w - 2(C C_w)^{1/2})`, and its two legend terms
(squared center gap; trace of the covariance term) label the two halves
correctly. No overclaim: the piece states plainly that the Gaussian is a modeling
choice with a cost and cites the "not actually Gaussian" rebuttal (Jayasumana,
2401.09603) right beside it, matching the evidence's internal tension.

The split case, figure by figure. FFHQ FastGAN 5.28 / StyleGAN2 5.30 (tie), CLIP
StyleGAN2 2.76 / FastGAN 4.67 (StyleGAN2 ahead), human inspection favoring
StyleGAN2 — all owned by Kynkäänniemi et al. (2203.06026, Fig. 7) per evidence.
The ImageNet-class lever: 5.30 → 4.70 (top class) and 5.30 → 1.78 (deeper
features, "a two-thirds cut" = −66%), with CLIP moving "about four percent"
(evidence: −4.3%). Directions and denominators check out. Sample-size: FID biased,
linear in 1/N, bias model-dependent, two identical DCGAN runs swap rank, "no
comparison at a fixed sample count is reliable" (Chong & Forsyth, 1911.07023);
>50,000 images in practice (Borji, 2103.09396). Resizing: 299px, filter aliasing,
0.64 → 7.43 gap vs correct resize, JPEG churches 4.00 → 3.48, three of four
libraries alias (Parmar, 2104.11222). Every figure traces to its owning primary
with the right direction. The bound holds: the "Where the number keeps its word"
section carries Heusel's monotonic-degradation defense and the comparability-not-
sensitivity frame, so the criticism never implies the number is worthless.

Chart as evidence. `chart-1.py` hardcodes StyleGAN2 [5.30, 2.76] and FastGAN
[5.28, 4.67], matching the evidence and Kynkäänniemi Fig. 7 exactly; the script's
docstring cites the owning primary. The rendered PNG is honest: linear y-axis 0–6
labeled "distance (lower is better)", a legend, grouped bars from zero (no
truncation), StyleGAN2 gold and FastGAN blue consistent across both groups. The
0.02 Inception gap correctly reads as a visual tie; the CLIP gap reads wide. Title
and caption ("Inception features rate them a tie; CLIP features … rank StyleGAN2
well ahead. Lower is better.") are factual and cited to s4. The chart shows exactly
the writer's stated original act — the Inception-tie beside the CLIP-split in one
image — and does not overstate it. Alt text matches the numbers.

data-nb-kind audit. Eight sources, seven primary + one secondary. Each primary
owns its claim (s1 Projected GAN claim, s2 FID definition, s3 non-Gaussian
rebuttal, s4 ImageNet-class split, s5 sample-size bias, s7 resizing, s8 Inception
Score); s6 Borji is correctly the lone secondary, a survey reporting from outside
the authoring party. Labels are all correct. (The review brief's "9 primary / 1
secondary" does not match the article's 8 sources; the article's own count and
every label are right, so I treat the brief line as stale, not a defect.)

Citation hrefs. Opened all ten external hrefs as printed; each resolves to the
correct paper by title and authors (s1–s8 plus the two Go-deeper links). The
abstract-only pages for Borji, Salimans, and the CLIP detail in Kynkäänniemi do
not surface the figure/section-level facts the article cites, but the hrefs land
on the right documents and the evidence record establishes those facts with
correct locators, which is what the citation standard requires. Both internal
cross-links (`../the-mechanics/reading-images.html`, `../the-evidence/gans.html`)
exist in the published library and resolve.

No claim was retired. The skeptic read found nothing false.

## Cut

Ran a dedicated slop pass over every sentence including display text and
furniture. The prose is largely subject-locked: the sand-pile earth-mover analogy,
"The pictures did not improve by two-thirds. The bookkeeping did.", "The last input
is plumbing.", and the named FastGAN/StyleGAN2 case could not be moved to another
article. Negative-parallelism count stayed within the earned limit: "They break
comparability between setups, not sensitivity within one" is the honest bound the
evidence requires (a real, named contrast), and "It reads real-image statistics,
which the Inception Score never does" is a cited factual contrast — no invented
strawman "not" clauses. No banned em-dash/semicolon reflexes in the body; the one
caption semicolon is a tight, valid join. No prompt leakage: the briefing stack's
"break comparability" is the natural technical description, not a copied planning
label, and no sentence claims the article fulfilled its assignment. No borrowed
clause from the voice-guide exemplars (Silver / Smith / Spiegelhalter); the humor
is FID-native and aimed at the arithmetic, as the guide asks.

One sentence failed the delete test and was cut: "Hold onto that." in the
construction section. It is a forward signpost carrying no fact, claim, or
reasoning step, and the return it promises (the Gaussian-assumption caveat) is
cited once and never cashed later, so it points to a payoff that does not come.
Deleting it loses nothing.

One formula, routed not cut because the repair needs new prose. The Why-card
closer — "By the end you will be able to follow the calculation yourself and see
which FID comparisons carry weight and which ones only look like they do" — falls
into the exact mold the review brief flagged. Every recent Instruments Why card
closes the same way: "By the end of this lesson you can take any '$X per million
tokens' claim, see the choices packed inside it, and…" (cost-per-token), "By the
end you will be able to take any 'AI scored X% on ARC-AGI' claim and ask the two
questions…" (arc-agi), "By the end, you can take any tokens-per-second claim and
ask four questions" (tokens-per-second), and the same "By the end you will/can…"
opening across swe-bench, glue, gpqa, bleu, training-compute, humaneval,
hallucination-rate, perplexity, and frontiermath. This is `spec/slop.md` Formula:
a closer built to the pattern of prior articles, a house cadence stamped across
the shelf. The content is FID-specific; the construction is the shelf template.
It needs the writer to state FID's payoff in a differently-built sentence, off the
"By the end you [will/can] … any … claim and …" shape.

Headings vary in construction (no comma-and joins recur); the opener avoids the
flagged "Every few months a lab announces…" mold; the takeaway avoids "read the
claim precisely / now you know which one you are looking at" and does not reuse
"None of this makes the metric worthless." No "In plain language" note label
appears. The holds-up grid earns its place: it sets the three defenses beside the
three cautions in a way the prose does not, it sits mid-body rather than closing
it, and no Verdict note is used, so the judgment lands in The takeaway as the
press requires.

## Reader

Reading what survives straight through as the paper's declared reader — smart,
widely read, no time in a codebase — I finish able to run FID from an image to a
score and to name the three ways the number moves while the pictures stay fixed,
with one chart that makes the tie-and-split visible where the source prints only
separate numbers. That is more than any single source gives: it is the
construction, the three failure modes, and the honest bound assembled into one
frame, exactly the original-work act the draft handoff claims (recompute the
Fréchet distance on CLIP features, draw the tie beside the split, generalize to
the shared "hold the pictures fixed, move an input" frame). The prose sits closer
to the voice-guide exemplars than to a median summary — it builds the number
before it turns on it, reaches for a reader-owned comparison for the hardest step,
and keeps its doubt aimed at the arithmetic. The headline holds as the largest
claim the piece defends.

## Edits

- Cut "Hold onto that." from the construction section (signpost; failed the delete test).
- Ran `nb stamp`: words 1903 → 1900, reading_minutes 8, sources 8.

## Required work

- writer: Rewrite the Why-card closing promise so it does not open "By the end you
  [will/can] …" or follow the shelf's "take any … claim and [say what it does /
  does not] …" shape. Keep FID's specific payoff (following the calculation; which
  comparisons carry weight); break the cross-article formula the whole Instruments
  Why-card set shares.

## Decision

revise — the article is factually sound and the chart is honest evidence, but the
Why-card closer is a shelf-wide `spec/slop.md` Formula that needs a writer rewrite
beyond a word or clause.
