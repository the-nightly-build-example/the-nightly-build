# writer draft-handoff: the-instruments/rewardbench (01)

## Original work

The article turns a RewardBench leaderboard number into its executable
steps — the 2,985 fixed chosen-versus-rejected pairs, the four-section split,
the per-prompt weighted mean, and the reference code's 984-not-447 upweighting
of PRM-Math inside Reasoning that never surfaces on the leaderboard itself —
and holds that mechanical account against three separately-measured downstream
failures (Frick et al.'s Berkeley finding of a negative slope at the top of
the v1 leaderboard versus post-DPO Chatbot Arena rank; Sharma et al.'s 95%
sycophancy figure on the Claude 2 preference model against baseline truthful
comparators; the Singhal and Park length-bias decompositions on named
datasets), so a reader can see exactly what a RewardBench score does and does
not commit its holder to about the chatbot the reward model would train.

## Proof

Command: `./nb check .nb-work/the-instruments/rewardbench/library/the-instruments/rewardbench.html --series the-instruments --library /home/user/library-checkout`

Result: `BLOCK: 0  WARN: 0  verdict: PUBLISHABLE` (links checked).

No warnings intentionally left. All prior W-SENTENCE-DENSITY warnings were
resolved by splitting the sentences the check flagged, and the source-kind
BLOCK was resolved by adding the Ken Yeung / The Letter Two secondary source
(s10) that corroborates the RewardBench 2 release and its cross-family policy
caveat.

## Open questions

None. The evidence record supported the commissioned angle in full and the
brief's precisions are honored in the prose: Frick's Figure 4 is quoted for
direction only, without a fabricated Pearson; the Pearson 0.87 is scoped to
RewardBench 2 versus best-of-N accuracy across seven downstream tasks and not
to RewardBench 1 versus Chatbot Arena; Singhal's length-bias figures are named
per dataset (WebGPT ~2%, RLCD ~27%, Stack Exchange ~53%); Sharma's 95% is
named against the baseline-truthful comparator on the curated misconceptions
set, with the 45% helpful-truthful comparator noted alongside.
