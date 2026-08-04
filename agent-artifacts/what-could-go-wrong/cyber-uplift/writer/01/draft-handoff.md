# Draft handoff: what-could-go-wrong/cyber-uplift (01)

## Original work
This piece splits the single "AI cyber uplift" worry into three claims of
different evidential standing, then shows from the sourcing itself that the two
strongest demonstrations of AI finding real vulnerabilities (Big Sleep and the
DARPA challenge) were both produced by defenders, turning the headline
capability into evidence against the decisive-attacker-advantage claim rather
than for it.

## Proof result
`nb check ... --series what-could-go-wrong --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0, PUBLISHABLE.** 2199 words (band
1200-2200). No warnings left standing. Earlier W-LENGTH-HIGH and
W-SENTENCE-DENSITY warnings were resolved by trimming and by splitting the four
flagged sentences, not waived.

## Contradictions and calibration handled in prose
- Novice/expert dispute reported unresolved: Brundage (widen the set of actors)
  set directly against NCSC (advanced uplift concentrates among the
  already-capable; novices lifted only in low-skill access work), with the
  benchmark ceilings noted as pointing NCSC's way. No source reconciles them and
  the piece does not.
- Attacker/defender symmetry carried as the spine: both lead demonstrations are
  defensive programs; the piece states the balance could tip either way and that
  no result shows it tipping decisively toward attack.
- Doom and dismissal poles each pinned to their missing evidence. The maximalist
  doom pole is presented as analysis with no primary behind it (per the evidence
  record's honest gap), sourced nowhere; NCSC's "almost certainly more volume" is
  named as the strongest *sourced* claim and explicitly a long way short of a
  decisive edge.
- Interested-party sourcing flagged in prose at each point: Big Sleep (the team
  that scored the find also built the tool), Phuong/Gemini (a lab grading its own
  models), XBOW (a vendor selling the capability; the human-review-before-
  submission caveat kept from the TechRepublic secondary).

## Open questions
- None blocking. No operational attack detail was included; capability is
  discussed only at the level of the public evals and the SQLite bug's own
  published description.
- One process note, not an evidence gap: the visual render probe (`nb
  render-check`) skipped because no Chrome is available in this environment, so
  the three furniture components (stat strip, comparison table, NCSC position
  card) were confirmed against the documented markup and the deterministic proof
  rather than a rendered screenshot. Worth an eyeball at editor stage if a
  browser is available.
- I did not capture a source asset. The evidence record proposed three candidate
  figures (Cybench Table 2, Phuong Table 7, the AIxCC results figure); I judged
  the three-row benchmark table carries the capability-ceiling argument more
  honestly and robustly than cropping a PDF figure, and no chart series was
  needed. Flagging in case the editor wants the Cybench 11-minute-line figure
  added.
