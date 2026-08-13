# Draft handoff: when-ai-breaks/tessa-eating-disorder-chatbot (writer 01)

## Original-work sentence

The article fuses the two incompatible causal accounts (NEDA's "unauthorized
generative feature" and Cass's "it was the pre-written script") into one
scope-misuse mechanism that survives either resolution, showing the harm follows
from placing a prevention-validated tool in an acute-support role rather than
from any particular technical trigger, which no single source in the evidence
record does on its own.

Where it is visible: the orientation section fixes the two facts the payoff
needs (validated only for prevention in at-risk users; a fixed script by
original design), the mechanism section states the reader-swap plainly and then
walks the "if scripted / if generated" fork to the same conclusion, and the
Koko section generalizes the pattern.

## Proof result

Command run (from `/home/user/the-nightly-build`):
`./nb check .nb-work/.../library/when-ai-breaks/tessa-eating-disorder-chatbot.html --series when-ai-breaks --library /home/user/library-checkout`

Result: **BLOCK: 1**, WARN: 1. Links included and all resolve. Not `BLOCK: 0`.

- `B-SOURCE-KIND` — 2 primary source(s) cited; series asks for at least 4.
  **This is the only blocker and I cannot clear it from the current evidence
  record.** See the researcher request below. It is not a wiring or markup
  problem: every other check passes, all placeholders are gone, display text is
  clean, and no slop/density/banned-term/em-dash warnings remain.

Everything else that was blocking or warning earlier is resolved: orientation
anchor restored (`data-nb-section="orientation"`), flex-section count back
inside 0-4, all `W-SENTENCE-DENSITY` and `W-PLACEHOLDER` warnings cleared, meta
stamped (words 1962, reading 9, sources 5).

### Warning intentionally left

- `W-SOURCES-MIN` — 5 sources against a series floor of 8. This is the same
  deficit as the blocker: the evidence record supplies only five usable sources.
  It stands until the researcher request below is filled. Clearing the 4-primary
  block will also lift this warning if the new primaries bring the total to 8+.

## Open evidence question (the blocker — needs the orchestrator/researcher)

The evidence record supplies only **2 primary sources**, both developer research
papers (Fitzsimmons-Craft et al. 2022, IJED; Chan et al. 2022, JMIR Formative).
The three other primaries the commission expected — **NEDA's own statements**,
**Sharon Maxwell's original documentation**, and **Cass/X2AI's own description
of Tessa** — were only reachable through NPR and KFF and are correctly typed
`secondary` in the record (the researcher flagged this in "Open items": the
originals "resisted direct fetch"). I did not reclassify them as primary to game
the floor, and I did not fabricate sources or fetch new evidence myself.

To reach `BLOCK: 0` the article needs **at least two more primary sources** (four
primary is a hard block; eight total is a warning). Precise request, in
descending value:

1. **NEDA's own dated statements** at a first-party or archival URL: the
   May 30, 2023 takedown statement and Liz Thompson's June 7, 2023
   clarification (the "separate decisions… conflated" language). Both are quoted
   in the draft via NPR (s4) and would upgrade to primary if retrieved.
2. **Sharon Maxwell's original documentation** (her Instagram post/screenshots)
   at its own URL — currently cited via NPR (s4).
3. **Cass / X2AI's own description of Tessa** (company page or Rauws's own
   statement) — the vendor side of the cause dispute, currently only via NPR.
4. Lower priority but real: the helpline workers' first-person account
   (`workerorganizing.org`, Abbie Harper) that the researcher hit a 403 on; it
   would add the union's own voice and a source, though the labor angle is
   deliberately kept to "sequence, not motive" in the draft.

Any two of items 1-3 clear the 4-primary block; three of them (or three plus the
union piece) also clear the 8-source warning. When they arrive, the swap is
mechanical: the relevant NPR/KFF-carried quotes move to cite the first-party
source, kinds update, re-stamp, re-prove. No prose rewrite is required.

## Handling notes (sensitive subject)

- **Harm described, not manual-ized.** The draft names the *categories* of
  advice (intentional weight loss, a daily calorie deficit, calorie counting,
  self-weighing/measurement) and omits the specific numeric targets in the
  record (the ~500-1,000 cal/day and ~1-2 lb/week figures). That is the minimum
  needed to establish the failure; the exact figures read as a usable
  instruction set, so they are held back per the brief.
- **Cause presented as contested, never asserted.** Headline and dek carry only
  what is solidly established (scope mismatch; the documented weight-loss advice;
  the takedown) and make no generative-AI causal claim. The dispute lives in the
  mechanism section as two attributed position cards plus a "What would settle
  it" note; the single-sourced "Cass acted without approval" claim is explicitly
  flagged as not something the lesson can state as fact.
- **"Replacement" walk-back carried.** The helpline section states both that
  NEDA pointed users to Tessa and that NEDA later called the two "separate
  decisions" that were "conflated," and rests the spine on the point that holds
  either way (Tessa was in front of acute helpline-seekers regardless).
- **No source asset used.** The screenshot asset the evidence lists is
  deliberately not reproduced; the harm is established in prose from the three
  corroborating parties. No chart: the core teaching is a categorical scope
  distinction, not a trend, so effect-size figures would not clarify it.
- **Habits avoided.** Why-this-matters does not use the "By the end you will
  know X… You will also see Y" formula; the closer is named for Koko rather than
  the desk's recurring "where the same weakness runs now" mold; the takeaway
  does not land on negative parallelism; the dek avoids the banned molds.

## Open voice question

None blocking. One judgment call for the editor: the Why-this-matters bookend
keeps one earned negative-parallelism thesis line ("the failure is in the role,
not the wiring"), because the misconception it corrects — that you must resolve
the technical cause to see the failure — is the piece's actual subject and is
named. If the editor reads it as a reflex rather than an earned contrast, it can
go without loss.
