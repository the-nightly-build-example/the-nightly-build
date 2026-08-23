# Draft handoff: the-evidence/adam-optimizer (01)

## Original work

This lesson turns the evidence record's separate claims into one worked
argument: it runs Reddi's counterexample as concrete arithmetic, showing that
the once-in-three <span>+C</span> gradient, divided by a large second-moment
term, outweighs the two <span>-1</span> gradients that should cancel it, so Adam
climbs to the worst point; and it holds the disproven 2015 theorem and Adam's
later-proven large-β2 convergence as two facts kept deliberately apart, which is
what lets the piece explain why a broken proof never dislodged the method.

## Proof result

`./nb check ... --series the-evidence --library <checkout>` (links included):
**BLOCK: 0, WARN: 0, PUBLISHABLE.** No warnings left standing. Stamped
words=1875, reading_minutes=8, sources=8 (6 primary, 2 secondary; source floor
is 6 total / 3 primary / 1 secondary).

The convergence nuance is held as the brief required: the 2015 proof is stated
as flat fact (Reddi names the Γ_t error), kept separate from the later-proven
claim that Adam converges under realistic large-β2 settings (Zhang et al. 2022;
Défossez et al., TMLR). No blanket "Adam does not converge" appears.

## Open questions

None for evidence or voice. One deliberate call for the editor's awareness: the
evidence flagged Reddi et al. Figure 1 (the iterate walking to +1) as the
strongest single image, but I worked the counterexample in prose with its real
quantities instead of capturing the asset, per the voice guide's steer toward a
worked case. The furniture that earns its place is the annotated Adam-update
equation (the one equation the lesson is about) and the scale table of the four
2015 experiments. No source asset or chart was used.
