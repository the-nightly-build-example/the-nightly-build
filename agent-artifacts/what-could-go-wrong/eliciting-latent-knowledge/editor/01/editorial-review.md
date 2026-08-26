# Editorial review: what-could-go-wrong/eliciting-latent-knowledge (editor/01)

## Skeptic

Thesis: reading out what a model internally treats as true is an unsolved problem
in exactly the cases a human cannot check; the one hopeful empirical result was
shown to track the loudest activation feature rather than truth; the strong form
of the worry is a forecast about systems no one has built. The piece stands on
four claims, and I opened every citation href against the source it prints.

Claim 1 — the SmartVault setup and the two-reporter fork (cited s1, s2). Stated
at full strength: an AI models the vault better than the human watching, a
reporter answers in human words, and a tampered camera splits what the AI knows
from what the human would conclude. The direct translator and the human
simulator earn identical training scores because nothing a human can label pulls
them apart. This matches the evidence record's paraphrase and locators. The
report itself (s1) is a Google Doc whose body WebFetch could not render past the
interface chrome, but the href resolves to the source document, and the framing,
date, and "open problem which we believe is central to alignment" wording are
confirmed on the ARC announcement (s2, opened and verified). Held.

Claim 2 — CCS is the empirical toe-hold (cited s3, s4). Verified against both the
Burns abstract (s3) and the ar5iv full text (s4): 71.2% CCS versus 67.2%
calibrated zero-shot, averaged across 6 models and 10 QA datasets, a 4-point
gain; accuracy holds when models are prompted to answer incorrectly (zero-shot
drops up to 9.5%, CCS does not); the authors state they did not evaluate active
lying or deception, and that CCS depends on a truth direction existing whose
conditions are unclear. Every figure and hedge the article uses is in the source.
Held.

Claim 3 — Farquhar debunks CCS (cited s5), with Roger earlier (s6). Verified
against the Farquhar full text: Chinchilla-70B, the IMDb sentiment task, the
inserted distractor ("Banana"/"Shed", or a fictional character's stated opinion),
task accuracy falling to about chance while the probe tracks the planted feature,
CCS predictions close to plain PCA, and Theorem 1 (for any binary feature there
is a probe with optimal CCS loss inducing it). Roger's LessWrong post (s6, the
one secondary) confirmed: dated March 13, 2023, many orthogonal probes achieve
low CCS loss and high accuracy, so CCS finds one truth-like feature among many,
not the model's unique belief. Held. Crucially, the article does not resolve the
Burns/Farquhar tension in CCS's favor: it reports Burns's 4-point gain as real on
standard QA, then reports that it collapses the moment a more prominent feature
competes, and lets the debunking stand. Reported fact, projection, and synthesis
stay distinct.

Claim 4 — truth is readable only on the checkable side; the strong claim is
projection (cited s7, s8, s2). Verified: Marks & Tegmark (s7) show LLMs linearly
represent truth of simple factual statements, read by a difference-in-means
probe that generalizes; their statements are the cities-style checkable facts
("The city of X is in country Y"), so the article's "such as whether Beijing is
in China" is a faithful illustration of the dataset's form, not an invented fact.
Cywiński et al. (s8) is a 2025 Taboo-model proof of concept using logit lens and
sparse autoencoders, which its authors call a toy-organism step needing harder
tests. The article uses each exactly as its authors bound it, then draws the line:
none reaches the worst case, which does not exist, so the strong worry is a
forecast reasoned from how training works rather than measured in a deployed
system. Held.

data-nb-kind audit: seven primary (s1, s2, s3, s4, s5, s7, s8) and one secondary
(s6, Roger/LessWrong). Every label is correct. s3 and s4 are the same Burns paper
(abstract and full text), both primary and not passed off as independent
corroboration. No wrong label hides a missing independent source. Every href
resolves to the source it prints.

No broken central claim, no miscitation, no source-policy failure. Nothing routed
to the researcher.

## Cut

Sentence-by-sentence and edge passes against `spec/slop.md`. Five sentences
failed and I cut them directly; the body is otherwise clean, and the two bookends
address the reader within their documented allowance while still saying something.

The pattern across the five was signposting: sentences that framed, calibrated,
or announced a reaction instead of teaching, with a stronger concrete sentence
already beside them. The orientation opened on "The setup in the report is small
enough to check by hand" — a tell that also left "the report" as a dangling
definite referent for a reader arriving from a link, since nothing before it
names the report; cutting it opens the section on the vault scene the voice guide
asks for. "not a solved one" was tautological after "open problem." "and this is
the part that catches people" narrated the reader's reaction. "It worked well
enough to matter" graded the result the numbers below it establish, and the
paragraph's own last sentence carries that calibration better. "Set each piece
where it belongs" was a method signpost the section heading already frames.

Recent-pattern check held up. The opener is not the "When people warn that X..."
mold and not "By the end you will be able to..."; no section is titled "Who makes
the case now"; the takeaway avoids the "X is here. Y is here. Z is not." staccato
and "how worried to be tracks that one gap"; the over/under-confidence weighing
uses "Treating X overshoots... Treating Y the other way," not the
booster/dismisser device the brief flagged; "doing the work" is absent. The
negative-parallelism instances that remain ("not deceptive alignment, nor
mesa-optimization"; "forecast... rather than measured"; "open research, not a
demonstrated failure") each correct a real, named misconception and are earned.
Headline and dek commit to claims the piece defends; the dek adds who/when and the
projection point without restating the headline. No prompt leakage: the "direct
translator"/"human simulator" terms are the ELK report's own, and the
demonstrated-vs-projected line is the beat's subject rendered in the article's
terms, not lifted planning language. No borrowed phrasing from the voice-guide
exemplars.

Furniture: the single stat strip (+4 pts vs ~50%) is documented engine furniture,
cited in nearby prose, and earns its place by putting the two load-bearing numbers
side by side. I considered the writer's flagged holds-up grid for the salience
section and declined it: the demonstrated-vs-projected sorting is already done in
prose in its own section, a grid would duplicate the note the writer already cut
for duplication, and the grid's documented summary row is a "Verdict" note this
press explicitly bans as a leftover. One component, left as is.

## Reader

Read straight through as the paper's declared reader, what I have that the sources
alone would not give me: a way to sort five papers' worth of claims into
demonstrated and projected, and one test question to put to any future
"we can read model minds" or "we are hopeless" claim — is it shown on an answer a
human could already check, or on the worst case, where no one can. No single
source hands that over; ARC poses the problem, Burns and Farquhar dispute one
method, Marks & Tegmark and Cywiński bound the positive results, and the article
is the thing that lines them up against the ELK line. The original-work sentence
in the handoff claims exactly this split, and it survives. The prose sits closer
to the voice-guide exemplars than a median summary: it opens in the vault scene
before naming the abstraction, states each limit in the open (CCS "well enough to
matter" but debunked; truth readable "only ever... where a person could already
check"), and keeps the register plain where it is most pointed. The headline, read
as the largest claim, is one the piece defends.

## Edits

- Cut orientation opener "The setup in the report is small enough to check by hand." — weak tell and a dangling "the report" referent for a first-time reader; section now opens on the vault scene.
- Cut "not a solved one" from the ARC-framing sentence — tautological after "open problem."
- Cut "and this is the part that catches people" — signpost narrating the reader's reaction; "The human simulator is not lying. It has no plan to deceive." stands.
- Cut paragraph opener "It worked well enough to matter." — grades the result the numbers below it establish; paragraph's closing sentence carries the calibration.
- Cut section opener "Set each piece where it belongs." — method signpost the heading already frames; section now opens "On the demonstrated side:".
- Ran `./nb check` (links off) after the edits: BLOCK 0, WARN 0, PUBLISHABLE.

## Required work

- orchestrator: re-stamp the article (`nb stamp`) so `words`/`reading_minutes` in
  nb-meta reflect the five cut sentences, then run the final links-on proof before
  preparing the PR. Routine post-edit step; the prose-only cuts introduced no
  markup, citation, or link change and the links-off check already passes clean.

No researcher work (every citation verified against its source; no evidence gap).
No writer work (no broken claim, no reporting to redo, no chart or asset).

## Decision

approve — the SmartVault case is stated at full strength, the Burns/Farquhar
tension is presented and left standing rather than resolved in CCS's favor, the
demonstrated-vs-projected line is sharp and every citation checks out against its
source; the five slop cuts were made directly and only the routine re-stamp and
final proof remain.
