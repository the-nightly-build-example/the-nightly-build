# Draft handoff: what-could-go-wrong/ai-control (writer 01)

## Original-work sentence

The article assembles the six primary control results into one
demonstrated-versus-projected argument and uses the original experiment's own
upfront-auditing baseline (15% safety) as a fixed yardstick: it shows that the
adaptive-attack collapse returns every protocol to exactly the floor the 2023
demonstration was built to beat. The evidence record lists these results as
separate, explicitly non-comparable entries; the throughline that ties the
collapse back to the demonstration's own starting number is the article's, not
the record's.

## Proof result

`nb stamp` then `nb check ... --series what-could-go-wrong --library
/home/user/library-checkout` (links included): **BLOCK: 0, verdict PUBLISHABLE.**
words=2200 (band 1200-2200), reading_minutes=10, sources=8 (6 primary, 2
secondary; series floor 8 / >=4 primary / >=1 secondary met). All source links
resolved under the link check. em-dashes=0; no banned terms; nb-meta dek is
byte-identical to the rendered dekline.

### Warning intentionally left standing

- `W-SENTENCE-DENSITY` on one 50-word / 3-join sentence in "Even its advocates
  call control a stopgap": *"The case rests on three things the evaluation must
  establish: that the red team drew out the model's real capacity to do the harm,
  that the control measures behave the same in deployment as in the test, and
  that developers extrapolate conservatively from test to a real-world chance of
  harm."* This is a deliberate colon-plus-three-parallel-clauses construction in
  the register the voice guide holds up (Schneier's parallel-consequence
  sentence). It reads as one controlled sentence; splitting it would force
  repeating the stem and read choppier. Left as a long sentence under control per
  spec/editorial.md. Every other density warning from earlier rounds was fixed by
  splitting.

## Numbers discipline (as applied)

- Every control figure carries its setup and audit budget in prose: APPS at 2%
  audit over 5,000 problems (trusted editing 92/94, untrusted monitoring 79/96,
  trusted monitoring 62/97, baselines 100/2 and 15/100); Ctrl-Z/BashBench 58%->7%
  at 1% audit; Control Tax monitor AUC 0.92-0.96 with no robust worst-case safety
  at <=5% budget; adaptive injection scored 0 on all 375 injected samples.
- The four papers are never placed in one ranking. The only comparison table
  holds solely the original paper's own protocols and baselines (same task, same
  models, same 2% budget), which are internally comparable.
- No dollar figure invented for the "control tax": the piece states plainly that
  the study reports monitor cost/AUC and the low-budget failure rather than one
  headline number.
- Refinement carried: the skeptical half arrives before superhuman. Both the
  Control Tax low-budget failure and the adaptive-injection collapse are
  human-level-model results, framed as breaking "before the models get smart."
- Proponents' own limit is given in their own words (Shlegeris & Greenblatt
  quote in a note; the stopgap framing).

## Open questions

None blocking. Two notes for the editor:

- The Redwood blog and the LessWrong dialogue titles could not be confirmed by
  automated fetch (JS-rendered pages); they are cited from their URL slugs and
  the evidence record's attribution. The arXiv titles for s1, s3, s4, s5, s6
  were confirmed against the live /abs/ pages.
- The four Background rows and two Go deeper rows are all optional reading and
  the lesson stands without them; deceptive-alignment and ai-boxing are also
  linked in body prose (plain links, not numbered sources) per press editorial.
