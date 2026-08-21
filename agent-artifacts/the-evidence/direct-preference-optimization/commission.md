# Commission: the-evidence/direct-preference-optimization

## Authorized work

Scheduled duty for 2026-08-21 returned `the-evidence` as an open section. One of
five articles commissioned tonight, one per due series. Process this article only.
Slug verified new against the full published library (30 the-evidence slugs).

## The document and the angle

The lesson reads the 2023 paper *Direct Preference Optimization: Your Language
Model Is Secretly a Reward Model* (Rafailov, Sharma, Mitchell, Manning, Ermon,
Finn; NeurIPS 2023). It is the paper behind the phrase "trained with DPO," now
the default post-training recipe for most open models.

What the document did: it showed you can align a language model to human
preferences without the two things RLHF used — a separately trained reward model
and a reinforcement-learning loop (PPO). DPO rewrites the RLHF objective so that
the optimal policy has a closed form, which turns preference tuning into a single
supervised classification-style loss on pairs of preferred/dispreferred
responses. The paper reports experiments on controlled sentiment (IMDb),
summarization (Reddit TL;DR), and dialogue (Anthropic Helpful-Harmless), claiming
DPO matches or beats PPO-based RLHF while being far simpler and more stable.

The teaching: state plainly what RLHF's pipeline was and what DPO removes from it
(link the published `the-evidence/instructgpt` for RLHF and
`the-evidence/deep-rl-from-human-preferences` for the preference-learning origin;
do not re-teach them). Show the real scale of the paper's evidence (its three
tasks and model sizes) so the reader sees the foundation under the "as good as
PPO" claim. Then bring it to the present: DPO won adoption in open-model
post-training, but whether it truly equals PPO is contested — later studies find
PPO still ahead on some benchmarks and DPO sensitive to responses outside its
preference data. Say plainly where the paper's claim holds and where later work
qualifies it.

## Boundaries

- Slug new. Related published slugs to link, not re-teach: `the-evidence/instructgpt`
  (RLHF/the InstructGPT recipe), `the-evidence/deep-rl-from-human-preferences`
  (preferences from comparisons), `the-mechanics/sampling-temperature` and
  `the-mechanics/sycophancy` if a mechanic needs grounding.
- Do not turn this into a math derivation. The desk reads the document and states
  what it did, its numbers, and its scale, in plain words. Give the idea of the
  closed-form-policy trick without asking the reader to follow the algebra.
- Tonight's neighbors (other series): the-instruments/big-bench-hard,
  the-mechanics/getting-math-wrong, what-could-go-wrong/unilateralists-curse,
  when-ai-breaks/arup-deepfake-fraud.

## Sources

Floor: at least 6 sources, at least 3 primary, at least 1 secondary. Leads
(verify each firsthand):

- **Primary — the DPO paper**, arXiv:2305.18290. The derivation's result (closed-
  form optimal policy; the classification loss), the three experimental tasks,
  the model sizes, and the exact comparisons to PPO/RLHF baselines.
- **Primary — the RLHF pipeline it simplifies**: the InstructGPT paper (Ouyang et
  al. 2022) and/or Christiano et al. 2017, for what a reward model and PPO loop
  are. (Both are published lessons — cite the primary, link the lessons.)
- **Primary — a DPO-vs-PPO follow-up**, e.g. Xu et al. 2024 (*Is DPO Superior to
  PPO for LLM Alignment?*) or a comparable study, for where PPO still wins and
  DPO's out-of-distribution sensitivity. This carries the "does it still hold"
  present-day angle.
- **Primary — a model report that post-trains with DPO** (e.g. Zephyr-7B,
  Tunstall et al. 2023, or a major open-model technical report), for real
  adoption.
- **Secondary — reporting/explainer** on DPO's rise, for context on how the
  method spread.

Search for what breaks the angle: if the paper's own claims are narrower than the
"replaced RLHF" story, quote the paper; if later evidence mostly vindicates DPO,
say so. Record contradictions in full.

## Furniture and charts

Lesson template. A chart earns its place only if a comparison is the point (for
instance DPO vs PPO win rates on the paper's tasks) and the evidence supplies the
verified series. Do not force one. No Verdict block.

## Production policy (from `nb production-policy`)

Profile `balanced`. writing-coach low, researcher high, writer medium, editor
high; model capable; none required. nb-meta `harness` "Claude Code", `model`
"capable". Runtime note: subagent roles inherit this session's model (Opus-tier,
"capable") and effort; per-role effort is the policy target, honored where the
harness allows. No required directive is traded down.

## Tags (writer to confirm)

dpo, rlhf, preference-optimization, alignment, post-training

## Recent patterns to break (habits not to inherit; five most recent the-evidence pieces)

- Dek: do NOT open by naming the authors and hanging a comma-and reversal off it
  ("[Researcher] did A, and that/then [the part it leaves out]"). Four of five
  recent deks name the researchers up front.
- Headings: avoid the "X did A, then/never B" reversal heading; the possessive
  "the paper's own [test/hedge]"; and the "Where the X comes from" heading.
- Opener: avoid the arXiv-upload moment ("went up on arXiv on [date]") and "comes
  from a single paper."
- Closer: avoid the "the difference between what was named and what was proved"
  ledger close and the reader-directed "the next time... the useful question is."
- Diction to avoid: "the difference between...", "outran / has outrun what it
  proved", the two-beat reversal ("The scale did not vanish. It moved."), and the
  "What it named... / What it established..." antithesis.
- Cross-series tics: no "By the end you will be able to..." promise; no "The next
  time..., ask..." numbered-questions close; "what the bare number hides";
  "honest" as a virtue word.
