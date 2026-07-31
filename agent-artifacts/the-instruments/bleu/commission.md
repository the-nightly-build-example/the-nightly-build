# Commission — the-instruments / bleu

Date: 2026-07-31 (UTC) · Mode: open · Template: lesson · Section: Working Knowledge

## The measurement

BLEU (Bilingual Evaluation Understudy): the automatic score, introduced by Papineni,
Roukos, Ward, and Zhu at IBM in "BLEU: a Method for Automatic Evaluation of Machine
Translation," ACL 2002 (`aclanthology.org/P02-1040/`). For two decades it was the
default number for ranking machine-translation systems, and it still appears on
model cards for translation and multilingual tasks. The course has already read
`the-evidence/attention-is-all-you-need` (2026-07-26), which reported a BLEU of 28.4
on English–German — so the reader has met the number and is owed how it is made.

## The angle

An Instruments-desk lesson: teach how the number is built, step by step, then show
exactly what it can and cannot support, with at least one real case where it misled.

Three ideas, taught completely, in order:

1. **How BLEU is computed.** Modified n-gram precision: count how many 1-, 2-, 3-,
   and 4-word runs in the candidate translation also appear in the human reference,
   but *clip* each n-gram's count at the number of times it appears in the reference
   (so repeating "the the the" can't inflate the score). Take the geometric mean of
   the four precisions, then multiply by a **brevity penalty** that punishes
   translations shorter than the reference (precision alone rewards saying less).
   Work one short sentence example with real integers so the reader can compute it.
2. **What the number can support, and what it cannot.** BLEU measures surface
   n-gram overlap with one or more reference translations. It does not read meaning:
   a correct paraphrase using different words scores low; a fluent-sounding wrong
   translation that reuses reference words scores high. It is a **corpus-level**
   statistic — reliable over a test set, noisy on a single sentence. Its absolute
   value is not comparable across languages, tokenizations, or numbers of
   references; two labs reporting "BLEU 34" may have measured different things
   (the reproducibility problem sacreBLEU was built to fix, Post 2018).
3. **A real case where it misled.** Callison-Burch, Osborne, and Koehn,
   "Re-evaluating the Role of BLEU in Machine Translation Research," EACL 2006
   (`aclanthology.org/E06-1032/`): BLEU ranked systems in an order human judges
   disagreed with; a rule-based system beat a statistical one with humans but not on
   BLEU. Say what that cost (years of research optimizing a proxy). If a cleaner or
   more recent misranking case is verified, use it instead or alongside.

## Required contribution (the article's own work)

Show that a single BLEU number silently encodes choices — tokenization, how many
references, brevity handling, corpus vs. sentence — and that the field has
repeatedly caught BLEU ranking the worse system higher. The reader should leave able
to ask, of any reported BLEU, "measured how, against what references?" and to know
why a BLEU gain is weak evidence that translations actually improved.

## Source obligations

From `nb source-policy --series the-instruments`: **min 8 sources; primary ≥ 4,
secondary ≥ 1.**

- **Primary, read in full:** Papineni et al. 2002 (the defining paper — read the
  formulas, the brevity penalty, the human-correlation experiments and their sample
  sizes). Callison-Burch et al. 2006 (the misranking evidence). Post 2018 "A Call
  for Clarity in Reporting BLEU Scores" (sacreBLEU, arXiv 1804.08771). Vaswani et
  al. 2017 for the 28.4 EN-DE figure (cross-link the reader already holds).
- Additional primary candidates: a WMT findings paper reporting BLEU-vs-human
  correlation; the sacreBLEU tool documentation; the original NIST/BLEU correlation
  numbers. Verify every formula and every quoted score against the owning paper.
- **Contradiction hunting required:** find defenders of BLEU (cheap, fast,
  reproducible with sacreBLEU, correlates acceptably at the corpus level for MT) and
  present that steelman before weighing the critique. Note metrics that replaced or
  supplement it (chrF, COMET, BLEURT) only as much as the lesson needs.

## Prior coverage in this library (link, do not re-teach)

- `the-evidence/attention-is-all-you-need` (2026-07-26): where the reader met BLEU
  28.4 — Background link and the natural hook.
- `the-instruments/perplexity` (2026-07-28): another intrinsic metric whose value
  shifts with tokenization — a close cousin; link it, and make sure this lesson's
  tokenization point is distinct (BLEU's is about cross-report comparability).
- `the-instruments/humaneval-pass-at-k`, `mmlu`, `swe-bench`: prior "how a score is
  made and gamed" lessons — same desk, different number. Do not reuse their openers.

## Structures NOT to repeat (recent habits)

The Instruments desk has repeatedly opened on a shocking swing ("the same model
scored X and Y"). BLEU's story is quieter — a construction and a slow misdirection —
so do not force that opener shape. No colon-subtitle headline; no "not X but Y"
thesis; vary section cadence from the recent library's comma-and-clause headings.

## Neighboring articles tonight (make this distinct)

Same as the edition list; this is the only *metric-construction* piece tonight.

## Output paths

- Article: `.nb-work/the-instruments/bleu/library/the-instruments/bleu.html`
- Role artifacts under `agent-artifacts/the-instruments/bleu/{writing-coach,researcher,writer,editor}/NN/`

## Harness / model

harness `claude-code-routine`; writer `claude-sonnet-5` effort medium; researcher &
editor `claude-sonnet-5` effort high; coach `claude-sonnet-5` effort low.

## Bans to watch

em-dash ≤ 4; `leverage` ≤ 1; `load-bearing` 0; `revolutionary`/`transformative`/
`game-changing` 0; "AI race" 0; `machinery` 0. A worked numeric example is expected;
use a table or listing for the n-gram counts rather than packing them into prose.
