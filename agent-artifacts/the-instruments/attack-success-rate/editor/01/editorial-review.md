# Editorial review: the-instruments/attack-success-rate (editor/01)

## Skeptic

Thesis: an attack success rate is not a safety grade but one measurement, the
share of one fixed list of requests, pushed by one attack, that one judge ruled
the model answered, and the same rate can mislead in both directions. The worked
case is Cisco's 100% for DeepSeek R1.

The claims it stands on, tested against the sources I reopened:

- The rate is built from four choices (list, attack, response window, judge),
  and each moves the number. Held. HarmBench's 510 behaviors / 100 validation /
  410 test, the 512-token window that "can change ASR by up to 30%," and the
  classifier's 93.19% human agreement (vs GPT-4 88.37%, AdvBench refusal 69.93%)
  all check against arXiv:2402.04249. GCG on Llama-2-13B = 30.2% checks.

- The judge alone swings the number. Held hardest, and it is the claim I most
  wanted to keep, so I pushed it. The 88 / 73 / 65 three-judge spread on one set
  of GPT-4o answers checks against arXiv:2407.11969 (GPT-4 88, rule-based 73,
  Llama-3-70B 65 — the article pairs each judge to the right figure). The table's
  Spearman values (0.90 / 0.85 / 0.82 / 0.25 / 0.16 / -0.39) round correctly from
  the evidence record's StrongREJECT figure, and the string-match negative and
  the GPT-4-judge 0.16 are read in the right direction. The too-high direction
  (Scots Gaelic 43% on GPT-4, re-scored vacuous by StrongREJECT) is cited to the
  StrongREJECT paper that owns the re-scoring, which is correct: the 43% is a
  reported rate, the vacuity is StrongREJECT's finding.

- A low score expires. Held. GCG transfer (GPT-3.5 86.6%, GPT-4 46.9%, Claude-2
  2.1%) checks against arXiv:2307.15043, and the article correctly frames the
  2.1% as resistance to one 2023 attack under GCG's looser non-refusing-attempt
  bar, not a general grade. The past-tense jump (GPT-4o 1% -> 88%, Claude-3.5
  Sonnet 0% -> 53%) checks against arXiv:2407.11969.

- Refusing more games the number at a hidden cost. Held. The (1 - refused)
  multiplier makes a total refuser score zero by construction, and XSTest
  (250 safe + 200 unsafe contrast prompts) is used only to name the over-refusal
  axis, with the mechanism linked out, exactly as the round's focus required.

- The misled case. Held. Cisco's 100% from 50 HarmBench prompts (not the full
  410), one algorithmic attack, auto refusal detection with human oversight,
  temperature zero, with Claude-3.5 Sonnet 36% and o1-preview 26% on the same
  set, all check against blogs.cisco.com; the uncaveated trade forwarding checks
  against SecurityWeek. The article steelmans ("The verdict may even be right")
  before weighing it, which holds the voice guide's line against sliding from
  "misleads" to "worthless."

Display text, descriptor by descriptor: headline ("A different attack turns 1%
into 88% on the same safety test") is the past-tense finding stated with the
number as the surprise, and it commits to what the expiration section proves;
"same safety test" is the fixed 100-prompt set with the attack, not the test,
changed. Dek names Cisco, the 50 requests, and the one attack, and adds what the
headline omits without restating it; it is a claim about the world, not a grade
of the article's own method. Every subhead is a step of the argument in the
piece's own nouns. No title, role, place, date, or quantity in display text
conflicts with its owning source.

data-nb-kind audit: s1 Cisco (primary, owns the DeepSeek ASR it produced),
s2 SecurityWeek (secondary, forwards Cisco), s3 HarmBench, s4 StrongREJECT repo,
s5 StrongREJECT paper, s6 XSTest, s7 past-tense, s8 GCG (all primary, each owns
the design or rates cited to it), s9 The Decoder (secondary). Every label matches
the primary/secondary test; no secondary is dressed as primary, and no label
hides a missing independent source.

Citations opened as printed: all nine hrefs resolve and land on the source
itself. s1, s2 confirm the 100% / 50-prompt / "lacks robust guardrails" facts
and the missing caveat; s3, s5, s6, s7, s8 confirm titles, authors, and the
headline figures; s4 confirms "the full dataset of 313 questions"; s9 confirms
the 1%-to-88% figure and the fragile-safety-training framing. No break found.

One borrow, not a break in the claim but in the prose, is recorded under Cut.

## Cut

Slop pass, every sentence including display text and furniture. The piece is
unusually specific (named benchmark, attack, and judge on every rate), so the
sentence-by-sentence and edge passes turned up almost nothing: no empty
conclusion, no puffery, no decorative-analysis copula, no vague attribution, no
self-reference outside the two bookends the template allows. No em-dash,
semicolon, or comma splice; colons introduce definitions and lists correctly.
The dek is two clauses joined by "and," not the banned comma triad. Headings and
edges do not mirror the recent Instruments formulas ("How eight tests become one
number", "The line X crossed had already been crossed"), and no
"measurement is itself a measurement" catchphrase appears.

Two changes made, both about phrasing rather than an empty edge:

1. Borrowed clause from a voice-guide exemplar. The draft's "Not who to cite for
   it, but the deeper origin" lifts "the deeper origin" from the Harford
   quotation the writer read ("I don't mean the now-standard request to cite
   sources, I mean the deeper origin of the data"). The slop test does not catch
   it because it reads as specific to the subject. The point underneath is the
   article's own, so I rewrote it in the piece's own vocabulary: "Not which paper
   to cite it to, but how it was built." "Built" is the word the next section
   already runs on, so the fix also tightens the setup. The "not X, but Y" shape
   stays because the misconception it corrects (a citation request standing in
   for how the number was made) is real and named, which the slop rule permits.

2. Mislocated referent. "Three words in that sentence are doing quiet work"
   pointed at the preceding sentence, which does not contain jailbreak, refusal,
   or attack success rate. Changed "that sentence" to "that report" so the
   locator matches the DeepSeek reporting the three terms actually come out of.

Delete test on the edges: the closers of the pipeline, judge, expiration, and
misled-case sections each carry a reasoning step and stay. "The judge is half the
number" is a flourish but grounded in the table's 0.16-to-0.90 spread, so it
survives. The article's last sentence ("It was never measuring the thing the
headline said it did") lands the conclusion the argument built and is not empty.

Furniture: the four-step process is correctly a numbered-steps component (stages
in order), and the grader-vs-human ranking is correctly a table (rows of one
shape, a comparison), its caption carrying the citation. Two components in a
2,000-word lesson reads as a continuous article, not a stack of blocks. No chart
or source asset is required: the table is the clearest single picture of judge
sensitivity, and the prose carries the rest. Chart provenance and assets are the
writer's in any case, so I add none.

## Reader

Read straight through as the paper's declared reader, I come away with something
no single source gives: one number decomposed into four buried choices, both
ways it misleads (a lenient judge counting vacuous non-refusal as success; a
static list understating exposure to a cheap new attack) shown as failure modes
of the same rate, and Cisco's 100% reread as "DeepSeek refused none of 50 prompts
under one attack," not "unsafe." Opening the original-work sentence confirms the
same synthesis the writer claimed, so the piece is a construction, not a
restatement of its sources. The prose sits with the voice-guide exemplars, not a
median summary: short plain claims, the concrete figure ahead of the abstract,
the Luu flat-verdict shape in the takeaway. The headline, reread as the largest
claim, is a specific defended finding with its number earned.

## Edits

- Rewrote the orientation's "Not who to cite for it, but the deeper origin: what
  set of requests..." to "Not which paper to cite it to, but how it was built:
  what set of requests...", removing phrasing borrowed from the voice guide's
  Harford quotation.
- Changed "Three words in that sentence are doing quiet work" to "Three words in
  that report are doing quiet work", fixing a referent that pointed at a sentence
  not containing the three terms.

## Required work

None. Both changes were the editor's to make and are made. No evidence gap, no
broken central claim, and no source-policy failure to route to the researcher or
writer.

## Decision

approve — every rate checks against the benchmark that owns it, every citation
resolves to its source, the two failure directions are taught as one number's,
and the two prose issues found were the editor's to fix and are fixed.
