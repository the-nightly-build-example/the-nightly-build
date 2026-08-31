# Editorial review: the-evidence/adversarial-examples (editor/01)

## Skeptic

Thesis: the 2015 "Explaining and Harnessing" paper got the harder half right
(a one-step attack that still fools undefended classifiers) and the easier half
wrong (its own defense had to be rebuilt), and a decade of harder tests leaves
the problem measured but neither solved nor stuck. The article states this from
the draft alone, and the claims it stands on are legible.

The claims it rests on, tested:

1. **The paper's explanation is that models are too linear, not too complex, and
   that claim is contested.** The draft presents it as the paper's claim ("The
   2015 paper argued the reverse") and then names three challenges: Tanay &
   Griffin's boundary tilting, Ilyas et al.'s non-robust features, and the Akhtar
   & Mian survey recording no field consensus. The evidence record and the paper's
   own abstract ("primary cause ... is their linear nature") back the framing. It
   is not stated as settled. Held.

2. **FGSM is a one-step, single-backward-pass attack.** The equation and prose
   match Sec. 4 of the paper. Held.

3. **The paper's own single-step FGSM adversarial training was later downgraded
   (gradient masking); adversarial training survived only in Madry's multi-step
   PGD form.** The draft says exactly this and attributes the finding to Madry et
   al. 2018 (#s3). Matches the evidence record's Contradictions. Held.

4. **"Still unsolved" with measured progress, ceiling attributed to Bartoldson.**
   The draft carries both sides: CIFAR-10 robust accuracy ~46% (Madry, 20-step
   PGD) rising to ~74% (Bartoldson, stronger attack) against ~94% clean, called
   "real progress and a wide remaining gap at once," and the hard-ceiling claim is
   attributed to "the group that set the mark" (#s5). Not "nothing works." Held.

Provenance: the 2013→2015 relation is framed as the same researchers (Goodfellow
and Szegedy on both) returning to their own phenomenon, not a rival correction
("This was not one camp correcting another"). Correct and matches the record.

I tried to break the central claim (the calibrated verdict) by rereading each
cited source for what the piece spends it on. Nothing broke: every figure the
verdict rests on traces to its owning primary.

Display-text figures, verified descriptor by descriptor against the evidence
record's Numbers section: epsilon 0.007; panda 57.7% to gibbon 99.3% on GoogLeNet;
MNIST maxout 89.4% error at 97.6% confidence; shallow softmax 99.9%; adversarial
training 0.94%→0.84% clean and 89.4%→17.9% adversarial (the table); Madry MNIST
~89% and CIFAR-10 ~46% under 20-step PGD; Athalye 7 of 9, six broken fully and one
in part; Ilyas ~44% (record: 43.7%); Bartoldson ~74% at ~94% clean; Eykholt every
lab image (100%) and 84.8% of drive-by frames, stop read as a 45 mph sign. All
correct.

Headline, dek, and subheads checked as claims. Headline "One gradient step still
fools image classifiers, a decade on" is the piece's largest claim and it is
defended: FGSM still drops undefended models, and even the best defended models
miss ~26% of the hardest CIFAR-10 attacks. The dek makes three world-claims (the
linear blame, its later dispute, the rebuilt defense), does not restate the
headline, and matches the rendered dekline word for word. The subhead "Too linear,
not too complex" is a negative-parallelism construction, but it mirrors the paper's
own abstract and corrects the complexity suspicion the body names explicitly, so
the contrast is earned rather than invented.

`data-nb-kind` audit: eight sources marked primary, one (Akhtar & Mian survey)
marked secondary. Each primary owns the claim it is cited for; the survey reports
others' work and is correctly secondary and used only for the "no consensus" point.
No mislabels, no independent-source gap hidden behind a label.

Citations: every source href opened as printed. All nine arXiv abstract pages
return 200 and land on the paper's own page (not a PDF endpoint or mirror). The two
Background links (Wikipedia adversarial ML; arXiv 1409.4842 GoogLeNet) and the two
Go-deeper links (RobustBench; the Distill advex-bugs discussion) also resolve;
these sit in bookends, which carry no citations, so RobustBench being unusable as a
cited number (per the evidence record's Discarded note) does not bar it as optional
reading. Display source titles match the papers; two harmless variants noted for
the record — 1608.07690's arXiv title has a typo ("Persepective") the draft
silently corrects, and 1707.08945 uses the CVPR published title rather than the
arXiv v1 title. Both links still land on the right source.

No broken central claim, no missing evidence, no source-policy failure. Nothing
routed to the researcher.

## Cut

Slop pass, sentence by sentence including display text, captions, the equation
legend, and the table caption. The prose is disciplined: zero em-dashes (well under
the banned-terms cap), concrete nouns, real numbers ahead of every verdict. Four
sentences drew scrutiny and I acted on the ones that failed the delete test.

- Cut the forecast signpost closing the harness section ("That hope held up in
  part and broke in part, and sorting out which took the field years"). "Held up in
  part and broke in part" self-grades the argument the back half then delivers and
  duplicates the takeaway's "harder half right and easier half wrong"; the section
  now ends on the paper's stated optimism and the next section undercuts it
  cleanly.
- Trimmed a verbatim echo: "No search, no iteration" sat in the equation caption
  and again in the paragraph just below it. Kept it in the caption, rewrote the
  prose to carry only its live payload (the single pass is what made the attack
  cheap enough to run across a whole test set).

Reflex-punctuation repairs, per the editorial direction's period-is-default rule
(the piece held four semicolons, all avoidable):

- "Each pixel stays under the threshold of sight; the total does not" → period.
- "Adversarial training survived; the single-step version the paper used did not"
  → period.
- Figure caption "scaled by 0.007; added to the panda" → period.
- Equation legend "how far each pixel is allowed to move; 0.007 in the panda
  demonstration" → comma (the second half is a fragment, not an independent
  clause, so the semicolon was ungrammatical as well as reflexive).

Edge read, out of order: paragraph and section openers and closers carry facts or
reasoning steps, not filler. "Both parts have been argued over ever since" and "The
danger also lives elsewhere" are soft transitions but each carries a real forward
claim the next sentences cash out, so they stay. The takeaway's close ("a measure
of the problem: how small the change can be, and how far the strongest defenses
still fall short") resolves the opener's promise and states the conclusion the
argument built.

Dangling-referent read (arriving cold from a link): the body introduces its nouns
before leaning on them; the panda, GoogLeNet, FGSM, and transfer are each set up
before use. No referent lives only in the briefing.

Leakage: compared the authored text against the commission, writer brief, voice
guide, and evidence record for clause order, not just words. The bookend's "By the
end you will know ..." is the lesson template's required statement of what the
reader learns, not lifted planning language. "Neither solved nor stuck" is the
article's own synthesis, matching the draft handoff's original-work sentence. No
selection rules, planning labels, or assignment-fulfilled claims carried through.

Borrowed-phrasing check against the voice guide's quoted writers (Luu, Willison,
Aaronson): none of their distinctive phrases ("assembly line," "guessing the next
word," "purely a confusion over words," and the rest) appear in the draft. The
piece borrows the *move* — build the mechanism up, anchor to the panda's pixels,
numbers before the verdict — without borrowing any clause.

Recent-pattern check: the piece does not echo the five recent the-evidence
deks/headlines, avoids the "The X paper behind today's Y" and "did A until B"
molds, and does not reuse the denoising-diffusion shape (no stat-strip opener, no
"where the X comes from" closer). Its shape is a narrative panda opener into a
built-up mechanism into a calibrated verdict.

Furniture: three components, each earning its place — the panda source asset (the
whole argument in one image), the annotated FGSM equation (the one equation the
piece is about; exactly one annotated equation, within the limit), and the MNIST
before/after table. All three are documented engine furniture, authored to the
catalogue markup. No Verdict note, no stack-of-blocks, no missed component that
would materially help. Only the two bookends address the reader; the body speaks to
no one.

## Reader

Read straight through as the paper's declared reader, who knows only that a panda
can be nudged into a "gibbon." What I have that the sources alone would not give me:
a plain, ordered account of *why* the trick works (linearity summing thousands of
sub-threshold pixel nudges into one label-flipping move), and one calibrated verdict
— cheap attack real, own defense rebuilt, explanation never settled, gap measured
but open — that no single source states. The draft-handoff original-work sentence
claims exactly that synthesis, and both answers survive. The prose sits closer to
the voice-guide exemplars than to a median AI summary: it teaches the mechanism up
from the reader's wrong first guess rather than restating the abstract. The
headline, reread as the largest claim, holds.

## Edits

- Cut the forecast signpost "That hope held up in part and broke in part, and
  sorting out which took the field years" (self-grading, duplicated by the
  takeaway).
- Rewrote the post-equation sentence to drop the verbatim "No search, no
  iteration" echo of the caption, keeping the cheap-enough-for-a-whole-test-set
  point.
- "threshold of sight; the total does not" → period.
- "Adversarial training survived; the single-step version the paper used did not"
  → period.
- Figure caption "scaled by 0.007; added to the panda" → period.
- Equation legend "allowed to move; 0.007 in the panda demonstration" → comma.

## Required work

None. All changes were prose and punctuation, within the editor's remit. The
orchestrator re-runs `nb stamp` and `nb check` before the PR (the sentence cut
lowers the word count from the stamped 2198). Note for the orchestrator/CI only:
the writer's handoff flagged that `nb render-check` was skipped for lack of Chrome,
so the KaTeX equation and `nb-table` were not visually confirmed in a browser; the
markup matches the documented furniture, and CI's render probe should confirm the
visual render. No writer or researcher work needed.

## Decision

Approve. Every load-bearing figure verifies against its owning primary, every
citation resolves to its source, the four framing corrections (calibrated
"unsolved," contested linear explanation, downgraded single-step defense,
same-researchers provenance) are all present and correctly attributed, the source
asset retains exactly the evidence the argument spends, and the prose holds the
voice guide's register; the remaining faults were reflex punctuation and two slop
edges, all fixed in place.
