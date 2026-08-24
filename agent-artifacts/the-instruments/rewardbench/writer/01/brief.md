# writer brief: the-instruments/rewardbench (01)

Inputs: .nb-work/the-instruments/rewardbench/agent-artifacts/the-instruments/rewardbench/editorial-direction.md
        .nb-work/the-instruments/rewardbench/agent-artifacts/the-instruments/rewardbench/writing-coach/01/voice-guide.md
        .nb-work/the-instruments/rewardbench/agent-artifacts/the-instruments/rewardbench/researcher/01/evidence.md
        .nb-work/the-instruments/rewardbench/library/the-instruments/rewardbench.html   the initialized article; edit it in place
        .nb-work/the-instruments/rewardbench/.nb-context/   effective template contract, runtime assets, and furniture catalogs
Output: .nb-work/the-instruments/rewardbench/agent-artifacts/the-instruments/rewardbench/writer/01/draft-handoff.md
Proof:  ./nb check .nb-work/the-instruments/rewardbench/library/the-instruments/rewardbench.html --series the-instruments --library /home/user/library-checkout

Recent habits to break (paper-wide, from the last several published lessons; the
voice guide names no prior article):

- Why cards keep opening by telling the reader what they have heard ("You have
  read that...", "You keep hearing that..."). Open on this lesson's particulars.
- Why cards keep closing on "By the end you will know what A, B, C, and D."
  Avoid that enumeration.
- Why cards keep narrating themselves ("This lesson builds/lays out..."). Address
  the reader without the "this lesson [verb]" frame.
- Takeaways keep resolving with "The question was whether..." and closers built
  as "That is real, and it is what X." Avoid both.
- Headlines keep pairing two independent clauses with a comma and "and." Vary the
  construction.
- Deks: avoid the comma-triad closed with "and," the semicolon reversal, and the
  suspended "...the real question is whether."

Outline: derive this piece's sections from its own argument, not the near-fixed
arc recent lessons run.

This round's focus: the record's Contradictions and precisions are load-bearing.
The mechanical account (2,985 prompt/chosen/rejected trios, four sections, per-
prompt weighted averaging with math upweighting inside Reasoning) is anchored
in the paper and the dataset card. For "leaderboard rank does not predict
chatbot quality," lean on Frick et al.'s PPE paper (Figure 4 negative
correlation between RewardBench 1 top scores and downstream RLHF performance —
quote the direction and the paper's wording, do not fabricate a Pearson value)
and AI2's own RewardBench 2 concession that scores are a prerequisite but not
sufficient. The Pearson 0.87 is RewardBench 2 vs best-of-N accuracy, not
RewardBench 1 vs Chatbot Arena; do not conflate them. For length bias, Singhal's
"length is everything" finding is dataset-dependent (about 2% of PPO gain is
non-length on WebGPT, about 53% on Stack Exchange); if used, name the dataset.
For Sharma's 95%, name the comparator: preference model preferring sycophantic
over baseline truthful on a curated misconceptions set. Link earlier lessons
(instructgpt, chatbot-arena-elo, llm-as-a-judge, alpacaeval) for shared
machinery rather than re-teaching it.
