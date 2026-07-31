# Commission — the-evidence / the-bitter-lesson

Date: 2026-07-31 (UTC) · Mode: open · Template: lesson · Section: Working Knowledge

## The document

Rich Sutton, "The Bitter Lesson," a short essay posted 13 March 2019 at
`incompleteideas.net/IncIdeas/BitterLesson.html`. Sutton is a founding figure of
reinforcement learning (co-author of the standard RL textbook, 2024 Turing Award).
The essay is roughly 1,100 words. It argues, from a reading of 70 years of AI
history, that "general methods that leverage computation" — search and learning —
have repeatedly beaten methods that build in human knowledge of the domain, because
compute per dollar keeps growing (Moore's law) while hand-built knowledge does not
scale. Its examples: computer chess (search beat chess knowledge, Deep Blue 1997),
computer Go (AlphaGo: search + self-play learning beat Go knowledge), speech
recognition (statistical/HMM then deep learning beat linguistic features), and
computer vision (learned features beat hand-designed ones like SIFT/edges).

## The angle

This is an Evidence-desk reading. State plainly **what kind of document this is**:
not a study with data, but a ~1,100-word argument from historical induction over a
handful of examples, by an authority, on a personal web page. That matters, because
it is now cited the way a proven law is cited — to justify pure scaling and to
dismiss whole research directions. The lesson's job is to let the reader see the
actual size of the foundation under the slogan.

Three ideas, taught completely, in this order:

1. **What Sutton actually claims**, in his words: the recurring pattern (human-
   knowledge approach wins early, gets overtaken by a general search/learning
   method once compute grows), and his stated cause (Moore's-law compute + methods
   that scale with it). Walk one example concretely (chess or Go) so the reader sees
   the pattern, not the slogan.
2. **The strength of the evidence.** It is an essay, not an experiment: a pattern
   read off four-or-five wins, with the losses and the human knowledge that stayed
   essential mostly unmentioned. Contrast that with the actual empirical scaling
   evidence the course has already taught — Kaplan (2020) and Chinchilla (2022) —
   which *do* have curves and numbers, and which refined "just add compute" into
   "spend it on the right mix of model and data." Sutton's essay predates and is
   coarser than that evidence.
3. **How it is used today vs. what it supports.** Where the citation outruns the
   text: the transformer architecture, RLHF/instruction tuning, and data curation
   are all human-designed structure that mattered enormously — so "throw out human
   knowledge" is not what the last five years actually did. Name the gap honestly.
   Also give the essay its due where it holds (hand-engineered features and search
   heuristics genuinely did lose to learned/general methods).

Do not turn this into a takedown or an endorsement. Report what the text says, show
the scale of its support, and weigh the citation against the evidence.

## Required contribution (the article's own work)

Separate what Sutton argued from the scripture it became, and test the slogan
against the very scaling evidence the course just taught (Kaplan → Chinchilla) and
against the human-designed pieces (transformer, RLHF) that the last five years
depended on. The reader should leave able to say what "the bitter lesson" does and
does not establish, and to spot when someone cites it as if it were a measured law.

## Source obligations

From `nb source-policy --series the-evidence`: **min 6 sources; primary ≥ 3,
secondary ≥ 1.** Aim higher on primary.

- The Bitter Lesson essay itself is the governing **primary** document — read every
  line; it is short.
- Primary empirical anchors already familiar to the course: Kaplan et al. 2020
  "Scaling Laws for Neural Language Models" (arXiv 2001.08361) and Hoffmann et al.
  2022 "Training Compute-Optimal Large Language Models" / Chinchilla
  (arXiv 2203.15556). Cite them as the measured evidence Sutton's essay lacks.
- For Sutton's own examples, prefer the primary: Silver et al. 2016/2017 AlphaGo /
  AlphaGo Zero (Nature) for the Go case; the Deep Blue record for chess.
- **Contradiction hunting is required.** Read at least one substantive critique of
  the essay (e.g., Rodney Brooks, "A Better Lesson," 2019, at rodneybrooks.com, and
  the widely-made point that transformers/RLHF/data-curation are human knowledge).
  A serious steelman of the essay is also required before weighing it.
- Verify the essay's date, Sutton's exact affiliation/title, and any quoted
  wording against the primary page.

## Prior coverage in this library (link, do not re-teach)

- `the-evidence/scaling-laws-kaplan` (2026-07-25) and `the-evidence/chinchilla`
  (2026-07-18): the measured scaling evidence — Background link, and the empirical
  counterweight to the essay. Do not re-derive their numbers; cite/link them.
- `the-evidence/emergent-abilities` (2026-07-20): scale-threshold claims and their
  re-scoring — relevant to "scale solves it" rhetoric.
- `the-evidence/instructgpt` (2026-07-22) and `deep-rl-from-human-preferences`
  (2026-07-29): RLHF as human-knowledge input that mattered — evidence against the
  strong reading of the slogan.
- `the-evidence/deepseek-r1` (2026-07-30): RL-only reasoning — a recent data point
  either side might claim; handle with care.

## Structures NOT to repeat (recent habits)

Recent Evidence pieces have leaned on the shape "the headline number traces to a
footnote / a smaller foundation than its citation implies." That underlying move
(citation outruns the document) is exactly this piece's subject, so it is fine —
but do **not** copy the recent *openers* or section cadences. Vary the opener from
the last week's "The 20XX paper …" and "The slogan … outgrew …" forms. No
"X is not Y; it is Z" thesis. No colon-subtitle headline.

## Neighboring articles tonight (make this distinct)

- `the-instruments/bleu`: a metric's construction and limits.
- `the-mechanics/instructions-are-data`: architecture of instruction-following.
- `what-could-go-wrong/the-off-switch`: corrigibility argument.
- `when-ai-breaks/gemini-image-generation`: a deployment failure.

This is the only piece tonight reading a foundational *text/argument*; keep it that.

## Output paths

- Article: `.nb-work/the-evidence/the-bitter-lesson/library/the-evidence/the-bitter-lesson.html`
- Context: `.nb-work/the-evidence/the-bitter-lesson/.nb-context/`
- Role artifacts under `agent-artifacts/the-evidence/the-bitter-lesson/{writing-coach,researcher,writer,editor}/NN/`

## Harness / model (resolved from balanced profile)

- harness: `claude-code-routine`
- writer model: `claude-sonnet-5`, effort medium (record in nb-meta)
- researcher & editor: `claude-sonnet-5`, effort high; writing-coach: `claude-sonnet-5`, effort low

## Bans to watch (merged banned-terms)

em-dash ≤ 4; `leverage` ≤ 1 (finance sense only) — note Sutton's own phrase is
"methods that leverage computation," so quote it once if needed and do not spend the
budget elsewhere; `load-bearing` 0; `revolutionary`/`revolutionize` 0;
`transformative` 0; `game-changing` 0; "AI race" 0; `machinery` 0.
