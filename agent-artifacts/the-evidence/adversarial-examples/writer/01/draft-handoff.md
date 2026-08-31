# Draft handoff: the-evidence/adversarial-examples (writer 01)

## What the article does to the evidence that the evidence does not do itself

It turns the evidence record's flat, verified claim set into a taught argument:
it builds the paper's linear explanation up from the reader's wrong first guess
(that a model fooled by invisible noise must be too complex) so the
panda-to-gibbon mechanism becomes ordinary, derives the fast gradient sign
method as that explanation's obvious consequence, and then weighs the paper's
two halves against a decade of later primaries into one calibrated verdict,
"neither solved nor stuck," that no single source in the record states.

## Proof result

Final `./nb check ... --series the-evidence` (links included): **BLOCK: 0,
WARN: 0**, verdict PUBLISHABLE. `nb stamp` wrote words=2198, reading_minutes=10,
sources=9 (8 primary, 1 secondary). All source and reading-band links resolve.
`nb render-check` reports "no Chrome in this environment; skipped" — the KaTeX
equation and `nb-table` are authored to the documented furniture markup but were
not visually confirmed in a browser here; CI's render probe should be watched.

Warnings intentionally left: none.

## Framing corrections carried (from the brief)

- "Still unsolved" is stated as a wide gap WITH measured progress: PGD adversarial
  training is a durable partial defense, CIFAR-10 robust accuracy rose from ~46%
  (Madry 2018, 20-step PGD) to ~74% (Bartoldson 2024, stronger attack) against
  ~94% clean, and Bartoldson's ceiling argument is given. Not "nothing works."
- The linear explanation is presented as the paper's claim and then as contested
  (Tanay & Griffin boundary tilting; Ilyas non-robust features; Akhtar & Mian
  survey records no field consensus), never as settled fact.
- The paper's own single-step FGSM adversarial training is shown to be downgraded
  (gradient masking); the "harnessing" idea survives only in Madry's multi-step
  (PGD) form.
- Provenance: framed as Goodfellow and Szegedy advancing their own 2013
  predecessor, not one group correcting a rival.
- Verified figures used exactly: epsilon 0.007; panda 57.7% to gibbon 99.3% on
  GoogLeNet; MNIST 89.4%/97.6%, 99.9%, and adversarial-training 0.94% to 0.84%
  clean / 89.4% to 17.9% adversarial (the table).

## Open items for the editor

- Source display titles (e.g. Bartoldson 2404.09349) were filled from the
  standard published titles of these well-known papers; the evidence record
  supplied URLs, authors, and kinds but not titles. All URLs resolve; titles
  are display text, not claims, but worth a glance.
- The panda source asset (`asset-1.png`) was captured from arXiv 1412.6572 p.3
  Fig. 1 with all three panels, operators, and class/confidence labels retained;
  the printed "Figure 1:" descriptive caption was cropped out per the asset rule.
