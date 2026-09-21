# Draft handoff: what-could-go-wrong/negative-side-effects (01)

## Original work

The piece draws the shown/analogy/present boundary that no single source in the
record draws for itself: it separates what the impact-measure experiments
actually demonstrated (avoidable damage, then damage measurably curbed, inside
tabular gridworlds and one 26x26 Game-of-Life board) from the untested claim
about open-world agents, and it reclassifies ToolEmu's failures as a different
mechanism (underspecification plus hallucination in an emulated sandbox) rather
than a demonstration of the classic proxy-optimization side-effect problem.

## Proof

`nb check ... --series what-could-go-wrong --repo ...` (links included):
**BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** Stamp: 2200 words, 10 min, 11
sources (10 primary, 1 secondary — the Saisubramanian survey, s9). No warnings
left standing.

The word count sits at the top of the 1200-2200 band by design; the earlier
draft ran to 2429 and was trimmed to 2200 while splitting the sentences the
density check flagged. If the editor cuts further, there is now no slack, so any
added sentence needs an equal cut.

## Evidence handling the editor should know about

- **Unverified figures were not printed.** Per the brief and the record's own
  cautions, I did not print the SafeLife table cells (0.35 / 0.21) or the
  AUP-on-SafeLife ratios (27.8% / 39%), which the record flags as reached via a
  summarizing fetch and needing cell-level re-verification. The prose uses the
  qualitative claims the record carries as solid ("a fraction of what the
  untreated agent caused, at comparable reward"). No researcher request needed.
- **Printed figures are the record's verified ones:** the AI Safety Gridworlds
  reward structure (+50 / -1 / -5 / -10), AUP's "as few as five, default thirty"
  auxiliary rewards, and ToolEmu's 23.9% / 68.8%.
- **ToolEmu boundary held.** It is used only in the present section, stated as
  real evidence against "feedback handles it" but explicitly not a demonstration
  of the classic mechanism, and marked as an emulated sandbox.
- **Turner's "dissolved" claim** is attributed at retrospective strength (a
  personal blog retrospective, not a result) and weighed against ToolEmu, per
  the brief.

## Open questions for the editor / next round

- **RLHF-vs-RL transfer contradiction, compressed.** The record lists Turner's
  separate "reward is not the optimization target" argument as a contradiction
  that weakens the gridworld-to-LLM bridge in either direction. I address the
  transfer gap generally in the "No result reaches a real open-world agent"
  section (the bridge was never built; every result is a reward-maximizer on a
  fully visible board), but cut the reward-is-not-the-target argument by name to
  hold the word band. If the editor wants that contradiction named explicitly,
  it costs roughly 40 words and needs an offsetting cut.
- **"Who presses it now, and what they want done."** The record carries no named
  present-day advocate demanding a specific policy on side effects. I framed the
  present honestly as (a) an ongoing research program whose remedies mostly lean
  on human feedback (survey, s9) and (b) the live Turner-vs-ToolEmu dispute over
  whether language-model agents inherit the problem. This is a genuine thinness
  in the record, not an omission; if a named contemporary campaigner is wanted,
  the researcher would need to supply one.

## Voice

No open voice-guide ambiguity. The two required plain-English glosses (relative
reachability; attainable utility preservation) are earned by the gridworld
example in the sentence that first uses each term, per the guide and the lesson
template's stricter term rule.
