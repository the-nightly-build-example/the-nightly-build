# draft-handoff: the-mechanics/false-confidence (01)

## Original work

The article assembles the evidence record's scattered and partly conflicting
claims into one retraceable mechanism from behavior to cause: it separates the
token probability a model computes from the confidence it prints, then lays the
base-model calibration, the post-training degradation, and the
elicited-versus-unsolicited verbalized-confidence findings along a single spine
with a worked calibration figure at its center, an ordering no one source in the
record supplies.

## Proof result

`./nb check ... --series the-mechanics --library <checkout>` (links included):
**BLOCK: 0, WARN: 0, PUBLISHABLE.** Stamped words=2100, reading_minutes=9,
sources=8 (7 primary, 1 secondary). No warnings intentionally left; all four
initial W-SENTENCE-DENSITY warnings were resolved by splitting the sentences.

Both narrowed claims are written in their defensible form: (1) the default
assertive tone and the unsolicited "I'm 95% sure" are uninformative (Xiong),
while an explicitly elicited numeric confidence can be better calibrated than the
token probabilities (Tian, ~50% relative ECE cut, marked as uneven); (2) the
softmax is not called the only internal signal — P(True)/P(IK) (Kadavath) and
latent representations (Lin) are named as trainable uncertainty signals. No
numeric GPT-4 ECE is asserted in prose; Figure 8 is used qualitatively.

## Open evidence question (owner: researcher / orchestrator)

The evidence record states Figure 8 gives "NO numeric ECE" and that the magnitude
is "only shown visually." That is not what the primary shows: GPT-4 Figure 8
prints **ECE: 0.007** (pre-train, left panel) and **ECE: 0.074** (ppo /
post-trained, right panel) as in-plot text annotations, read directly from the
report PDF (page 12) and visible in the captured asset (asset-1.png). I followed
the brief and did NOT build any prose claim on these numbers, and I kept the
Figure 8 worked example qualitative. But the asset faithfully reproduces the
report's own figure, annotations included, rather than cropping out what is source
evidence. If the orchestrator wants those two numbers used in the prose (they are
a genuine, primary-owned base-vs-RLHF ECE pair, exactly the "actual numbers" the
commission originally asked for), they must enter through a corrected researcher
evidence artifact, not be added independently here.
