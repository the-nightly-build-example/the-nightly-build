# Editorial review: the-evidence/proximal-policy-optimization (editor/01)

## Skeptic

Thesis: PPO's one durable contribution is the clipped surrogate objective, a
single min-and-clip that removes a policy update's incentive to leave the trust
region so one batch of experience can feed several gradient steps; everything
about PPO aligning language models was built by later, separately authored work,
not shown by the 2017 paper, whose own evidence was small RL benchmarks with no
proof underneath.

Claims it stands on, and how each held:

1. The clip is the mechanism. Tested by recomputing the worked example and every
   table cell against Eq. 7. Advantage +2, r 1.5: true product 3.0, clip pins r
   at 1.2 for 2.4, min 2.4 — correct. All four table rows check out: +2/0.5 gives
   1.0 vs 1.6, min 1.0; -2/0.5 gives -1.0 vs -1.6, min -1.6; -2/1.5 gives -3.0 vs
   -2.4, min -3.0. The "capped only in the favored direction" caption is exactly
   right in all four cases. The one break: the -2/0.5 row's prose said the score
   "stops falling" past the floor. For a bad action pushed down, the objective
   rises (-2 toward -1.6) as it is suppressed and then flattens at the floor, so
   the reward stops *rising*, matching the +2 row's own wording. I checked this
   against the captured Figure 1, whose A<0 panel is flat at low r with the start
   dot on the downslope. Fixed directly.

2. The paper's evidence is 7 MuJoCo tasks (1M timesteps each) and 49 Atari games,
   never language models, and Atari is a split. Verified against the evidence
   Numbers and Contradiction 1: fast-learning metric PPO 30 / ACER 18, final-
   performance metric ACER 28 / PPO 19, abstract concedes only "similarly to
   ACER though it is much simpler." The article reports both metrics and names
   the reversal; it does not claim a sweep. The clip sweep (no clip -0.39, eps
   0.2 -> 0.82 best) matches Table 1. Held.

3. The paper proves nothing. The quoted words ("lower bound," "pessimistic
   bound," "emulates," "say, eps = 0.2," "chosen heuristically") all trace to the
   record. The article correctly does **not** use the confabulated "calls its
   update a heuristic" line the evidence flagged as unsupported. Held.

4. The LM reputation was built later and is now being routed around. Ziegler 2019
   (774M GPT-2, s6), InstructGPT 2022 (175B, PPO by name, s3), DPO (s7, drops the
   RL), GRPO (s8, drops the value network, quote "of comparable size as the
   policy"), R1 (s9, live-circulation only). GRPO mechanics are cited to
   DeepSeekMath, not R1, matching the record's limitation note. The PPO-as-RLHF
   bridge is attributed to the later papers throughout ("None of what makes PPO
   famous now is in the 2017 paper"), never to the 2017 paper. Held.

Display text checked descriptor by descriptor: headline (both halves true and
defended), dek (claims the durable idea and the later-built trust, no restatement
of the headline), five subheads (each a step of the argument in the piece's own
nouns). data-nb-kind audited against the record: 7 primary, 2 secondary (Huang
37-details blog; R1 as context) — correct, and the source floor (>=6, >=3
primary, >=1 secondary) is met with 9. Citation hrefs are canonical arXiv IDs
matching the described papers; the equation and figure carry data-nb-url to the
PDF page 3 where Eq. 7 and Fig. 1 sit. No miscitation found.

## Cut

Four sentences failed the slop test and were removed:

- "There is a catch." A signpost announcing a turn the next two sentences deliver;
  the "the catch is" family in spec/slop.md.
- "That is the entire mechanism." A self-summary in the "X is the whole Y" family;
  the completeness point survives in the takeaway.
- "The honest status is layered." An empty conclusion ("the X is Y" with a vague
  assessment naming nothing checkable).
- "...no model above a few million parameters of policy network." A quantitative
  claim the evidence record does not carry (it gives the MuJoCo net as a two-layer
  64-unit MLP and no Atari net size). Cut as an unsupported nonessential clause;
  the sourced scale contrast in the next sentence (175B vs a simulated cheetah)
  carries the point.

No borrowed phrasing from the voice-guide exemplars, no prompt leakage (the
lesson's self-description sits only in the bookends, where the template allows it,
and is reworded, not lifted from the commission). Grammar and punctuation are
clean; the single semicolon (TRPO/PPO parallel) is a controlled use and the proof
already clears the em-dash and banned-term counts. Furniture earns its place: no
nb-note is present, so the desk's reflex "note + single table" pattern does not
appear, and the equation, the four-row table, and the captured Figure 1 each do
distinct work (formal statement, recomputable numbers, the paper's own plot).
Edges, dek, and headings do not fall into the flagged molds (no "the YEAR ORG
paper that..." dek, no present-tense "how it's used today" heading; the closer is
past-tense and particular).

## Reader

What the piece gives beyond its sources: a recomputable four-case model of the
clip a newcomer can check by hand, plus an honest map separating what the 2017
paper proved (a robust, simpler-to-tune method on small RL benchmarks, no proof,
a split Atari result) from what the field now trusts PPO for (aligning 175B
models), with the bridge attributed to later papers and its erosion by DPO and
GRPO shown. No single source hands over that arc. This matches the stated
original work. The prose sits closer to the voice-guide exemplars than a median
summary: terms are defined at the sentence that needs them, benchmark scale and
present-day use are held as two separate facts, and the writer is visible in the
concrete ("measured on a simulated cheetah learning to run," "a word used daily
by people who have never seen a MuJoCo robot"). The headline, read as the largest
claim, commits to the 2017-scope-versus-today gap the body defends.

## Visual evidence

Figure 1 (asset-1.png) is the PPO paper's own Figure 1, both panels, with the
r-axis ticks at 1-eps, 1, 1+eps and the red r=1 start dots retained and page
furniture cropped away — an honest crop of the evidence the worked example
spends. The caption is a factual cited label (Fig. 1, p. 3, data-nb-url to the
PDF) and matches the image (A>0 flat past 1+eps, A<0 flat below 1-eps). Kept.

## Edits

- Table, -2/0.5 row: "the score stops falling" -> "the score stops rising"
  (correctness: the objective rises as a bad action is suppressed, then flattens
  past the floor; now parallel to the +2 capped row).
- Benchmark-scope: removed unsupported clause "no model above a few million
  parameters of policy network"; sentence now reads "No language, no text."
- Orientation: cut signpost "There is a catch."
- Clipped-objective: cut self-summary "That is the entire mechanism."
- Second-life: cut empty conclusion "The honest status is layered."

## Required work

None blocking.

- writer/orchestrator (record, not a fix): the piece stays over the lesson band
  after trimming — 2479 words against a 2200 ceiling (W-LENGTH-HIGH, left
  standing). It cannot reach band without dropping a taught idea or the
  commission-required successor survey (Ziegler, InstructGPT, DPO, GRPO): the
  five body ideas are each distinct and the survey is mandated. The word counter
  also scores the annotated Eq. 7 LaTeX and the furniture captions as body words,
  inflating the count above the actual prose. This is a legitimate over-band
  state. W-SENTENCE-DENSITY (40 words, punctuation score 51) is the Eq. 7 TeX
  block read as a sentence, not real prose — the required annotated equation,
  left standing.

## Decision

approve — the thesis holds under the skeptic read, the one arithmetic/logic break
in the table is fixed, the slop cuts are made, the captured figure is honest
evidence, and the two remaining warnings are the legitimate over-band and
equation-density states recorded above, not publication-blocking work.
