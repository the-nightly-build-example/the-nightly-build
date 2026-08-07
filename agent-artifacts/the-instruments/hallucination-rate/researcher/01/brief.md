# researcher brief: the-instruments/hallucination-rate (01)

Inputs:
- editorial-direction.md — citation standard, series territory, declared reader
- commission.md — subject, angle, boundaries, source policy

Output: researcher/01/evidence.md

Research questions (answer each against the owning primary):
- The pipeline: read Vectara's HHEM Hallucination Leaderboard method and its
  published rates. Record exactly: what text the models summarize (the dataset),
  how a summary is scored for faithfulness, what the HHEM classifier model is and
  how it was trained/validated, and the exact rates published for a few named
  models (dated). State clearly that this measures summary faithfulness, not
  general truthfulness.
- The number is not one quantity: contrast with at least one other named
  hallucination benchmark that defines the failure differently (e.g. FaithBench;
  and TruthfulQA as a DIFFERENT thing — measuring imitation of human
  falsehoods). Record how the definitions differ.
- The automated judge dependency: note that scoring depends on a judge model and
  link (do not re-derive) the position-bias problem the-instruments/llm-as-a-judge
  owns; record any measured error rate of the HHEM classifier itself.
- The 'misled' case: find a documented instance where a low published
  hallucination rate was read as general reliability (in marketing, procurement,
  or press) and what that cost, or a model topping the faithfulness board while
  still fabricating in open use. Source it.
Contradiction hunt: Vectara's own caveats about scope; critiques that the
leaderboard's task is unrepresentative. Steelman both.

Verify every number against the primary that owns it. Record each source's own
resolvable URL (not the fetch route). Classify primary vs secondary with a
reason. Fill the Contradictions section only after a real search for what breaks
the angle. Meet the source policy in the commission. Report the evidence path,
the record's most important limitation, and whether the evidence undermines the
commissioned angle.
