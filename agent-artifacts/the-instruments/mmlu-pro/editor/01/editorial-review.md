# Editorial review: the-instruments/mmlu-pro (editor/01)

## Skeptic

Thesis: MMLU-Pro is not a harder MMLU but three separate repairs to three named
MMLU defects, each earning a different grade, and the rebuild changed the subject
toward STEM along the way. So a reader should trust a large like-for-like gap,
discount a small one, and read a cross-setting gap as no gap.

The claims it stands on, and how each held:

1. The guess-rate repair worked by construction (headline claim). Four options to
ten drops the random floor from 25% to roughly 10%. Verified against the MMLU
paper (25.0% baseline, s5) and the MMLU-Pro paper (ten options, s4). The single
qualification the article prints is correct and load-bearing: 17% of items carry
fewer than ten options, mean 9.47, so the floor sits just above 10%. This is the
one claim I most wanted to keep and it survives the hardest push: no choice of
prompt or grader moves an arithmetic floor.

2. MMLU-Pro measures a different, STEM-weighted subject mix. 12,032 questions
across 14 disciplines; 6,810 (56.6%) from MMLU, so 43% new; Math the largest
discipline at 1,351. All verified against the paper's composition tables (s4) and
the evidence record. The "not simply a harder MMLU" framing is the commission's
central contribution and the numbers carry it.

3. Three defects, three grades. Guess rate finished; label noise reduced but never
re-measured; prompt sensitivity reduced (4-5 points to about 2 across 24 prompt
styles, s2) but answer order untested. The piece does not overclaim: it states
plainly that no one has measured MMLU-Pro's own post-review error rate, and that
MMLU-Pro is "steadier against prompt wording and simply untested against answer
order." This is exactly the honest grading the brief demanded, and it does not
force the desk's "cited number is hollow" debunk.

4. A gap's meaning depends on setup and saturation. The Llama 4 card reports the
same Maverick model at 62.9 and 80.5 (17.6, printed as an 18-point spread) because
one run is pretrained 5-shot EM and the other instruction-tuned 0-shot accuracy;
verified firsthand against the card (s1). Top of the board near 88%, top four
within a point, dated August 2026, cited to the TIGER-Lab card (s6); the read date
matches today, so no refresh is owed.

Figures reopened and confirmed against the primaries: option count 4 to 10; item
count 12,032/14; CoT gain +1.5 (MMLU) to +19.1 (MMLU-Pro) for GPT-4o (s4);
prompt-sensitivity 4-5 to ~2 (s2); MMLU error rate 6.49% and the Virology 57% /
16th-to-1st reversal (s8); answer-order drops of 6 and 27 points on MMLU only,
never run on MMLU-Pro (s9). The MMLU-Pro+ follow-up (s7) supports "reward for
reasoning is not proof of reasoning" without overreaching.

Display text checked descriptor by descriptor. One factual slip found and fixed:
the orientation said MMLU-Pro sits "in the row where MMLU used to sit" on the Llama
4 card, but the card still lists MMLU, immediately above MMLU-Pro. I trimmed the
false clause to "near the top of its benchmark tables," which the fetch confirms.
Name and title checks passed: Aryo Gema leads the "Are We Done with MMLU?" team;
TIGER-Lab led by Wenhu Chen at Waterloo; producer named as a research group, not a
company, per the researcher's naming note.

data-nb-kind audit: nine sources, eight primary and one secondary (Data Phoenix,
s3, used only for Hugging Face's "noisy"/"too easy" framing as context, which is
the correct use of a secondary). Every label matches the primary/secondary test.
Meets the min-8 / >=4-primary / >=1-secondary policy. Two arxiv entries for the
same paper (s2 abstract, s4 full text) are the researcher's deliberate split, each
citation landing on the artifact that owns its specific claim; not padding.

Every citation href opened as printed. All nine return 200 and land on the source
itself (s1 GitHub card, s2/s4/s5/s7/s8/s9 arXiv, s3 Data Phoenix, s6 TIGER-Lab
dataset card). The internal Background/prose link to `../the-instruments/mmlu.html`
resolves in the production library (`library/the-instruments/mmlu.html` exists in
the library checkout); it is absent from the work tree only because the sibling
article is not staged there.

No broken central claim, no missing evidence, no source-policy failure. Nothing
routed to the researcher.

## Cut

The draft came in clean; the writer clearly worked from the voice guide. The
sentence-by-sentence slop pass, the edges pass, the dangling-referent pass, and
the delete test together surfaced two sentences that failed, both removed:

- "Start with how the number is made." A directive to the reader closing the
orientation section. The body speaks to no one, and the following section heading
already carries the transition. Cut, not repaired.
- "as promised" in "Whether they repaired MMLU's known flaws has, as promised,
three separate answers." The article narrating its own earlier promise. Cut the
two words; the sentence keeps its referent from the preceding "two levers."

Held on inspection and kept: "So MMLU-Pro is not MMLU made harder" is an earned
negative parallelism, correcting the commission's central misconception, which the
piece names in the same breath. The bookend comma-triads (learning outcomes in Why
this matters, the three-part rule in the takeaway) are the lesson template's
permitted reader-addressing furniture and each clause says something distinct. The
colons all introduce what their clause promises. Zero em-dashes; the four
semicolons are all inside the Google Fonts URL, none in prose. No banned lexical
terms.

Borrowed-phrasing check against the voice-guide quotations: none lifted. The
Rogers-style pivot is rebuilt as a statement ("MMLU-Pro turns out to have three
different answers to it"), not the borrowed "Or do they?"; no "axiom/theorem,"
"shockingly robust," or Goodhart phrasing carried over. Leakage check against the
commission and brief: the three-grades contribution and the reader's operating
rule are reworded in the article's own terms, not lifted.

Recent-pattern comparison: the headline breaks the desk's recurring
"cited-number-is-hollow" mold and states a repair that worked, as the brief asked.
The dek avoids both flagged builds (no comma-triad, no "one flat average over N
datasets"). Headings vary in construction; only one uses the comma-and build. No
reflex nb-table: the writer used nb-steps for the ordered build and a two-number
nb-stat-strip, both cited in nearby prose, and left the optional construction
table out rather than stacking blocks. Furniture is proportionate and the piece
reads as a continuous article.

## Reader

Read straight through as the paper's declared reader, one sentence on what I have
that the sources alone would not give me: a grade for each of MMLU's three named
defects and a single rule for reading an MMLU-Pro gap between two models, neither
of which any one source states. The original-work sentence in the handoff claims
exactly this synthesis, and the article delivers it. Both answers survive, so this
is not a restatement of the sources. The prose sits with the voice-guide
exemplars, committing to specific verdicts and a specific rule, rather than the
hedged median summary. The headline, reread as the largest claim, is a specific
surprising finding the piece defends: adding six wrong answers fixed the guessing
problem.

## Edits

- Orientation: changed "near the top, in the row where MMLU used to sit" to "near
the top of its benchmark tables" (the Llama 4 card still lists MMLU, above
MMLU-Pro, so the original was a false specific).
- Orientation: cut the closing signpost "Start with how the number is made."
- Levers: cut "as promised" from "has, as promised, three separate answers."

## Required work

None. No item routed to researcher, writer, or orchestrator. (Note for the
orchestrator only: the edits removed a few words, so re-stamp word count before the
PR, as the process already provides.)

## Decision

approve — the piece grades each repair honestly, claims no answer-order robustness,
keeps the STEM-composition caveat, and every figure and citation checks out against
the primaries; the three edits were prose and one factual-label fix, none
publication-blocking.
