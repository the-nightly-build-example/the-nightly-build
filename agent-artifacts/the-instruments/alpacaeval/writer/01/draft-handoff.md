# Draft handoff: the-instruments/alpacaeval (writer/01)

## Original-work sentence

The article turns the researcher's separate verified figures into one teachable
path, using Zephyr's single headline number to carry a new reader from a win rate
that looks like a test score, through the judge-and-reference computation and the
measured length bias, to a portable rule for reading any win rate by its version,
judge, and reference that the evidence records but never assembles.

This work is visible in the piece: the four-step computation, the back-out count
(0.9060 x 805 is about 730), and the two-setting Zephyr table that resolves the
90.60% / 13.20% split into "the bar moved" rather than a contradiction.

## Proof result

`./nb check ... --series the-instruments --library /home/user/library-checkout`
(links included): **BLOCK: 0, PUBLISHABLE.** All seven source URLs resolve.

### Warning intentionally left

- `W-SOURCES-MIN` (7 sources; series floor is 8). The eighth source in the
  evidence record is Chatbot Arena (Chiang et al., arxiv 2403.04132). It is
  already-taught ground: the course covers it in `the-instruments/chatbot-arena-elo`.
  `press/editorial.md` requires taught ground to be a plain prose link to the
  earlier lesson, never a numbered source. I linked it in prose (at "Chatbot
  Arena" in the length-control section) and as a Background row, so cannot also
  cite it as source 8 without breaking that rule. Every other evidence source is
  cited. The single available secondary (Moonlight) is cited both to meet the
  series' at-least-one-secondary rule and to corroborate the contested 0.94
  figure.

## Precision points honored

- Every displayed number names its version/judge/reference: Zephyr 90.60%
  (AlpacaEval 1.0, GPT-4 judge, text-davinci-003) vs 13.20% LC / 10.99% raw
  (AlpacaEval 2.0, GPT-4-turbo judge and baseline). The 22.9%->64.3% swing is
  labelled AlpacaEval 2.0, one model, verbosity-only.
- Length control is shown as reducing verbosity gaming, not closing it: the null
  model scores 86.5% LC (higher than its 76.9% raw), stated plainly.
- Correlation cited as 0.94 to 0.98 (owned by Dubois); the README's 0.93 noted as
  the repository's rounding.
- The judge-human agreement digit (researcher flagged 68.1% vs 69.2%, unpinned)
  is not used anywhere, so no exact decimal rests on it.
- Recent-habit checks: no "two measures disagree / both true" headline reveal (the
  90.60/13.20 contrast lives mid-body as a worked case, not the hook); opener
  states the stakes without an enumerated roadmap; takeaway resolves the opener
  rather than restating a definition; the comparability section is named in
  AlpacaEval's nouns ("The reference model sets the bar"), not fid's phrasing.

## Open questions

None blocking. If a later revision wants the judge's human-agreement rate as a
load-bearing figure, the researcher must reopen the README evaluators table to
pin the exact digit; the current draft needs no researcher request.
