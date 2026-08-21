# Draft handoff: the-evidence/direct-preference-optimization (writer 01)

## Original work

This lesson turns the evidence record's separate claims into one teachable
argument: it renders DPO's closed-form result in plain words with no algebra,
then weighs the paper's own thin evidence (small models, a GPT-4 judge, and a
dialogue task where no working PPO baseline existed) against Zephyr's real
adoption and Xu et al.'s harder-task results to land a split verdict the record
lists only in parts.

## Proof result

`./nb check ... --series the-evidence` with links on: **BLOCK: 0, WARN: 0,
verdict PUBLISHABLE.** No warnings left standing. (An earlier
W-SENTENCE-DENSITY on the 51-word RLHF-stages sentence was fixed by splitting it
into four short sentences, not suppressed.)

Stamp: words 1771, reading 8 min, sources 6 (5 primary, 1 secondary), meeting
the lesson floor (min 6; primary ≥ 3, secondary ≥ 1).

## Open question / decision flagged

One departure from a record number, made under the brief's Xu caution. The
evidence record lists CodeContests as "PPO 22.4% vs DPO 3.2%." Verifying against
the paper's own full text (arxiv.org/html/2404.10719v3, Table 8) confirmed PPO
22.4% (test 10@1k) and AlphaCode-41B 16.4%, but showed DPO at ~0.0% on
CodeContests, not 3.2%. Per the brief ("confirm against the paper's own table;
if you cannot, state the comparison qualitatively"), I printed only the two
confirmed figures and rendered DPO's result qualitatively as "close to zero."
The SafeRLHF (99.5% vs 95.8%) and HH-RLHF human-eval (PPO 45 to DPO 29) cells
also checked out against the same source; I used only the human-eval count, as
the safety gap was too narrow to carry weight in the argument. If the researcher
can reconcile where the record's DPO 3.2% came from, that is worth a note, but it
does not change the article's claim.

The two Background lessons (the-evidence/instructgpt, the-evidence/deep-rl-from-
human-preferences) are linked in prose and in the band rather than re-taught, per
the press rule; InstructGPT and Christiano are still cited as numbered primaries
for the specific pipeline and preference-data facts the DPO contrast rests on.
