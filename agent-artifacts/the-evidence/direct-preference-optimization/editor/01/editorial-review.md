# Editorial review: the-evidence/direct-preference-optimization (editor/01)

## Skeptic

Thesis: "trained with DPO" means collapsing RLHF's reward model and PPO loop
into a single classification loss on preference pairs; that method claim is sound
and won open-model adoption, but the paper's "as good as PPO" half rests on thin
evidence, and later work still puts PPO ahead on the hardest tasks.

Four claims carry it.

1. **The mechanism.** DPO drops the separately trained scoring model and the
   reinforcement-learning loop because the optimal policy for any reward has a
   closed form, so the model already carries the score and the loss becomes a
   classification of preferred against dispreferred pairs. Held. The paper's
   abstract, opened at s1, states it solves RLHF "with only a simple
   classification loss," and the "In plain language" note renders the idea
   without algebra, as the commission required.

2. **The parity evidence is thin.** Three small models (GPT-2-large, a 6B model,
   Pythia-2.8B), GPT-4-judged win rates, and a dialogue task where the authors
   could not get PPO to beat the base model and substituted Best-of-128. Held.
   Model sizes and the substitution match the evidence record's own
   contradiction note; the article states the substitution plainly and does not
   let the dialogue result read as a real DPO-versus-PPO measurement.

3. **Adoption.** Zephyr-7B scored 7.34 on MT-Bench against Llama-2-Chat-70B's
   6.86, a 7B DPO model beating a 70B RLHF one. Held against s4 and the record.

4. **Later work puts PPO ahead on hard, out-of-distribution tasks.** Held, and
   checked hardest. I opened the Xu et al. paper's own HTML (Tables 8 and 14) and
   confirmed CodeContests PPO 22.4% (CodeLlama-34B, 10@1k), AlphaCode-41B 16.4%,
   and DPO 0.0% — so the article's qualitative "near zero" is faithful and the
   two printed figures are exact. The human-preference cell reads 45 / 26 ties /
   29 out of 100 evaluations, so the article's "45 times to 29" is an accurate
   reading of the raw counts, not a percentage mislabeled as a count. No change
   needed there.

One break. In the "not a clean reversal" paragraph, the article credited the
secondary (s5, Cameron Wolfe) with the claim that "DPO stays competitive with
PPO when the preference data matches the model's own outputs and the tuning is
careful." I opened s5: Wolfe says close to the opposite — a performance gap can
persist between offline methods like DPO and online PPO-RLHF, and DPO is used
*despite* that gap for its simplicity. The claim as printed is unsupported by its
own citation, and the evidence record carries it only as an uncited synthesis
(Contradictions #4). The summarization-lead half of the same sentence is in fact
a DPO-paper (s1) result, not a Wolfe one. I fixed this directly: I cut the
Wolfe-attributed generalization and rebuilt the paragraph's balance on facts the
sources own — the paper's summarization lead (recite s1) and Xu et al.'s own
placing of the gap on off-distribution tasks (recite s6). s5 remains cited once,
correctly, for adoption.

Every other citation opened cleanly and landed on the source itself: s1 (DPO
paper), s2 (Ouyang/InstructGPT, three-step pipeline and the 1.3B-beats-175B
line), s3 (Christiano, reward from comparisons, <1% feedback, MuJoCo/Atari), s4
(Zephyr), s6 (Xu). Both internal links resolve, and their link text reproduces
the linked lessons' exact titles. Every `data-nb-kind` is right: the DPO paper,
InstructGPT, Christiano, Zephyr, and Xu are each the primary that owns its
claim; Wolfe is the lone secondary, used for context, satisfying the floor.
Named people check out: Rafailov "and five coauthors at Stanford" matches the
six-author Stanford roster; "a team led by Shusheng Xu" matches the first author.

## Cut

The prose is voiced and clean; it earns the voice guide's register rather than
imitating its wording. Two edge sentences failed the delete test and I cut them,
both signposts stating an assessment the numbers right after them already carry:
"and this is where the size of the foundation matters" (trailing the three-tasks
opener) and "On a hard test the difference is stark." (opening the PPO paragraph,
in front of the CodeContests figures). Neither survived the placeholder test.

Two minor clarity fixes: I quoted "trained with DPO" at first use in the body so
it matches the bookends' treatment of the slogan, and I smoothed "tuned ... to
close to zero" to "to near zero" to remove the doubled preposition.

Recent-pattern comparison came back clean. The dek does not name the authors up
front and hangs off none of the three banned molds (semicolon reversal,
suspended question, comma triad); it uses a single concessive "though." The five
section headings are concrete, built differently from one another, and match none
of the flagged shapes ("X did A then B," possessive "the paper's own," "Where the
X comes from"). The opener avoids the arXiv-upload moment and "comes from a
single paper." The takeaway closes on the argument's own conclusion, not the
"what was named versus what was proved" ledger or a reader-directed "next time."
Diction is clear of "the difference between," the two-beat reversal, the "what it
named / what it established" antithesis, and "honest" as a virtue word — cutting
"the difference is stark" also removed the nearest echo of the banned diction.

No prompt leakage: the slogan and subject terms are the reader's own situation,
not lifted instructions, and no sentence claims the piece did its assignment. The
bookends carry the only self-reference, which the lesson template allows, and
each speaks to this lesson's particulars. Furniture earns its place: the
three-task table is the paper's central comparison laid out for scanning, and the
"In plain language" note is where the closed-form idea gets taught. No Verdict
block, correctly — the takeaway lands the split judgment without one. I found no
missing component the material was straining for.

## Reader

Read straight through, the lesson gives a reader more than any one source would:
what "trained with DPO" actually removes from the RLHF pipeline, the real size of
the foundation under the parity claim (small models, a model judge, a dialogue
task with no working PPO baseline), and a present-day verdict weighed across five
papers — adoption won on simplicity, parity unproven where answers leave the
data. That is the synthesis the draft handoff's original-work sentence promises,
and it survives. The prose sits nearer the voice-guide exemplars than a median
summary: the "one loss ... can read as too small a thing to work" beat is Evans's
earned deflation, the figures-with-scale is Luu's, and the slogan-then-mechanism
opening is Lee and Trott's. The headline holds as the largest claim the piece
defends.

## Edits

- Orientation: quoted "trained with DPO" at first body use, matching the bookends.
- Three-tasks: cut the trailing signpost "and this is where the size of the foundation matters."
- PPO-lead: cut the opener "On a hard test the difference is stark."
- PPO-lead: smoothed "DPO tuned the same base model to close to zero" to "to near zero."
- PPO-lead: cut the s5-miscited claim that DPO "stays competitive with PPO when the preference data matches the model's own outputs and the tuning is careful," and rewrote the "not a clean reversal" paragraph to rest on the paper's summarization lead (recite s1) and Xu et al.'s off-distribution framing (recite s6).

## Required work

- **writer:** re-run the proof links-on to BLOCK: 0 and supply a fresh stamp; my
  cuts changed the body word count, so the recorded 1771 is now stale.
- **orchestrator:** re-stamp after the writer's proof, before preparing the PR.
- **researcher (non-blocking, optional):** the evidence record's Contradictions
  #4 asserts DPO stays competitive with PPO when preference data matches the
  model's distribution, but attaches no source, and Wolfe (s5) does not support
  it. The article now stands on sourced facts without that generalization. If a
  later revision wants the explicit in-distribution-parity claim restored, it
  needs a source that actually establishes it.

## Decision

approve — every figure and citation checks out, and the one broken claim (a
secondary miscited for something it does not say) was fixable directly by cutting
it and reciting the sources that own the point; no publication-blocking work
remains beyond the routine re-proof and re-stamp my edits trigger.
