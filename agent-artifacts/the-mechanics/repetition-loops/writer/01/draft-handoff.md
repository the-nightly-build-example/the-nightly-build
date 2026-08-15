# Draft handoff: the-mechanics/repetition-loops (01)

## Original work

The article assembles the eight sources into one backward descent, from the loop
on the screen to the point where it opens up, and pins each fix to the exact step
it reaches: it holds the measured self-reinforcement effect (settled, carried by
two independent primaries) apart from its contested cause (Welleck's training
objective against Fu's high-inflow structure), so no single paper's explanation
is allowed to stand as the answer the evidence does not settle.

## Proof result

`./nb check ... --series the-mechanics --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.**

No warnings left standing. The one warning the link-free pass raised
(W-SENTENCE-DENSITY, a 61-word sentence in the Why-this-matters opener) was fixed
by splitting it into short sentences, not waived.

## Handling of the brief's guardrails

- Mechanism figures are kept on their own scales, each with its source and model:
  Holtzman's Table 1 (GPT-2 Large, the paper's repetition score) in a table read
  against itself; Xu's "more than nine cases out of ten" (modern LMs, several
  corpora); Welleck's seq-rep-4 and token-rep numbers (Wikitext-103). The
  decoding section states plainly that figures from other papers sit on other
  scales, so nothing is stacked onto one axis.
- No denominator is asserted for the Holtzman Repetition% figures. They are
  presented as "the paper's own repetition score," with the note that the rows
  are meant to be read against each other rather than as a share of anything
  outside the table (Section 4's exact metric was not openable in the evidence).
- Step 4 (why a trained model raises probability on its own recent output) is
  marked genuinely open: Welleck and Fu are both steelmanned, and the section
  states the effect is settled while its cause is not.
- Only evidence-record sources are cited; nothing from Discarded was used.

## Open questions

- None blocking. One decision for the editor's eye: I did not capture the source
  assets the evidence offered (Holtzman Fig. 1 / Fig. 4, Xu's curve). The
  researcher could only reach those papers via ar5iv HTML because the PDFs did
  not parse, so a clean figure crop was not reliably capturable, and the
  self-reinforcement curve has no numeric series in the evidence to build an
  honest `nb chart` from. Step 1 is carried by the concrete opening description,
  step 2 by Holtzman's Table 1 numbers in a table, and step 3 by the authors'
  Figure 4 sentence quoted in a note. If a later round wants the Figure 4 image
  itself, that needs a researcher pass that captures it from the source.
